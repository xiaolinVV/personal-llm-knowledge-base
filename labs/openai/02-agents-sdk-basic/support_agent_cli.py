from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
from typing import Any

from agents import (
    Agent,
    MessageOutputItem,
    ModelSettings,
    RunConfig,
    Runner,
    SQLiteSession,
    ToolCallItem,
    ToolCallOutputItem,
    function_tool,
)


DEFAULT_MODEL = os.getenv("OPENAI_MODEL", "gpt-5.5")
WORKFLOW_NAME = "Lab 02 Agents SDK Basic"

ORDERS: dict[str, dict[str, str | None]] = {
    "ORDER-1001": {
        "status": "shipped",
        "eta": "2026-05-10",
        "last_update": "Package left the Shanghai sorting center.",
    },
    "ORDER-1002": {
        "status": "processing",
        "eta": "2026-05-12",
        "last_update": "Payment confirmed; waiting for warehouse pickup.",
    },
    "ORDER-1003": {
        "status": "delayed",
        "eta": None,
        "last_update": "Carrier reported a weather delay; new ETA is not confirmed.",
    },
}

REFUND_POLICIES: dict[str, dict[str, str | bool]] = {
    "shipped": {
        "eligible": True,
        "window": "Request a return within 7 days after delivery.",
        "detail": "Shipping fees are not refunded unless the item is damaged.",
    },
    "processing": {
        "eligible": True,
        "window": "Cancel before warehouse pickup for a full refund.",
        "detail": "If pickup has started, wait for delivery and open a return request.",
    },
    "delayed": {
        "eligible": True,
        "window": "Ask support to review the delay before cancelling.",
        "detail": "A full refund is available if the carrier confirms the package is lost.",
    },
    "not_found": {
        "eligible": False,
        "window": "No refund policy can be applied without a matching order.",
        "detail": "Ask the customer to verify the order id.",
    },
}

AGENT_INSTRUCTIONS = """
You are a customer support assistant for a small demo store.
Use get_order_status for order status, shipping, delivery ETA, or missing-order questions.
Use get_refund_policy for refund, cancellation, or return-policy questions.
Keep the final answer concise and mention which tool result it is based on.
Do not invent order data.
""".strip()


def normalize_order_id(order_id: str) -> str:
    return order_id.strip().upper()


def get_order_status_data(order_id: str) -> dict[str, Any]:
    normalized = normalize_order_id(order_id)
    record = ORDERS.get(normalized)

    if record is None:
        return {
            "order_id": normalized,
            "found": False,
            "status": "not_found",
            "eta": None,
            "last_update": "No matching order exists in the demo database.",
        }

    return {
        "order_id": normalized,
        "found": True,
        "status": record["status"],
        "eta": record["eta"],
        "last_update": record["last_update"],
    }


def get_refund_policy_data(order_status: str) -> dict[str, Any]:
    normalized = order_status.strip().lower()
    policy = REFUND_POLICIES.get(normalized)

    if policy is None:
        return {
            "order_status": normalized,
            "eligible": False,
            "window": "Unknown order status.",
            "detail": "Ask support to inspect the order before promising a refund.",
        }

    return {
        "order_status": normalized,
        "eligible": policy["eligible"],
        "window": policy["window"],
        "detail": policy["detail"],
    }


@function_tool
def get_order_status(order_id: str) -> dict[str, Any]:
    """Look up a demo store order by order id.

    Args:
        order_id: Order id to look up, for example ORDER-1001.
    """
    return get_order_status_data(order_id)


@function_tool
def get_refund_policy(order_status: str) -> dict[str, Any]:
    """Return the refund policy for an order status.

    Args:
        order_status: Order status such as shipped, processing, delayed, or not_found.
    """
    return get_refund_policy_data(order_status)


def build_agent(model: str) -> Agent:
    return Agent(
        name="Demo Store Support Agent",
        instructions=AGENT_INSTRUCTIONS,
        model=model,
        model_settings=ModelSettings(
            parallel_tool_calls=False,
            verbosity="low",
        ),
        tools=[get_order_status, get_refund_policy],
    )


def summarize_run_item(item: Any) -> dict[str, Any]:
    if isinstance(item, ToolCallItem):
        return {
            "type": item.type,
            "tool_name": item.tool_name,
            "call_id": item.call_id,
        }

    if isinstance(item, ToolCallOutputItem):
        return {
            "type": item.type,
            "call_id": item.call_id,
            "output": item.output,
        }

    if isinstance(item, MessageOutputItem):
        return {"type": item.type}

    return {"type": getattr(item, "type", type(item).__name__)}


def dump_json(data: Any) -> str:
    return json.dumps(data, ensure_ascii=False, indent=2)


def local_tool_demo(order_id: str) -> None:
    print(
        dump_json(
            {
                "order_tool": get_order_status_data(order_id),
                "refund_tool": get_refund_policy_data("shipped"),
            }
        )
    )


def run_agent(args: argparse.Namespace) -> None:
    if not os.getenv("OPENAI_API_KEY"):
        raise SystemExit("OPENAI_API_KEY is not set. Set it before running the Agents SDK lab.")

    session = SQLiteSession(args.session_id, args.session_db)
    agent = build_agent(args.model)
    run_config = RunConfig(
        workflow_name=WORKFLOW_NAME,
        trace_metadata={
            "lab": "02-agents-sdk-basic",
            "session_id": args.session_id,
        },
    )

    first_result = Runner.run_sync(
        agent,
        args.question,
        session=session,
        run_config=run_config,
    )

    turns: list[dict[str, Any]] = [
        {
            "input": args.question,
            "new_items": [summarize_run_item(item) for item in first_result.new_items],
            "final_output": first_result.final_output,
            "last_response_id": first_result.last_response_id,
        }
    ]

    if args.follow_up:
        follow_up_result = Runner.run_sync(
            agent,
            args.follow_up,
            session=session,
            run_config=run_config,
        )
        turns.append(
            {
                "input": args.follow_up,
                "new_items": [summarize_run_item(item) for item in follow_up_result.new_items],
                "final_output": follow_up_result.final_output,
                "last_response_id": follow_up_result.last_response_id,
            }
        )

    print(
        dump_json(
            {
                "model": args.model,
                "workflow_name": WORKFLOW_NAME,
                "session_id": args.session_id,
                "session_db": args.session_db,
                "turns": turns,
                "trace_note": "Open the OpenAI Dashboard trace viewer and filter by workflow name.",
            }
        )
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Lab 02: OpenAI Agents SDK single support-agent demo.",
    )
    parser.add_argument(
        "question",
        nargs="?",
        default=(
            "请查询 ORDER-1001 的物流状态，并说明如果我要退款应该怎么办。"
        ),
        help="Question for the support agent.",
    )
    parser.add_argument(
        "--model",
        default=DEFAULT_MODEL,
        help="OpenAI model id. Defaults to OPENAI_MODEL or gpt-5.5.",
    )
    parser.add_argument(
        "--session-id",
        default="lab02-demo-session",
        help="Session id for SDK-managed conversation memory.",
    )
    parser.add_argument(
        "--session-db",
        default=":memory:",
        help="SQLite session db path. Use a file path to persist memory across processes.",
    )
    parser.add_argument(
        "--follow-up",
        help="Optional second turn. Uses the same SDK session as the first turn.",
    )
    parser.add_argument(
        "--local-tools-only",
        action="store_true",
        help="Run the local tool wrappers only; does not call the OpenAI API.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    if args.session_db != ":memory:":
        Path(args.session_db).parent.mkdir(parents=True, exist_ok=True)

    if args.local_tools_only:
        local_tool_demo(args.question)
        return

    run_agent(args)


if __name__ == "__main__":
    main()
