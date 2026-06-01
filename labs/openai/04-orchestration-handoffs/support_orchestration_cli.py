from __future__ import annotations

import argparse
import hashlib
import json
import os
from typing import Any

from agents import (
    Agent,
    HandoffCallItem,
    HandoffOutputItem,
    MessageOutputItem,
    ModelSettings,
    RunConfig,
    Runner,
    ToolCallItem,
    ToolCallOutputItem,
    function_tool,
)


DEFAULT_MODEL = os.getenv("OPENAI_MODEL", "gpt-5.5")
WORKFLOW_NAME = "Lab 04 Orchestration and Handoffs"

INVOICES: dict[str, dict[str, str | None]] = {
    "INV-1001": {
        "status": "paid",
        "amount": "USD 49.00",
        "due_date": "2026-05-01",
        "note": "Monthly workspace subscription.",
    },
    "INV-1002": {
        "status": "open",
        "amount": "USD 149.00",
        "due_date": "2026-05-15",
        "note": "Annual support add-on renewal.",
    },
    "INV-1003": {
        "status": "refunded",
        "amount": "USD 20.00",
        "due_date": None,
        "note": "Partial refund for duplicate seat charge.",
    },
}

DEVICES: dict[str, dict[str, str]] = {
    "ROUTER-7": {
        "status": "degraded",
        "last_seen": "2026-05-08T09:42:00+08:00",
        "detail": "Packet loss detected after firmware update.",
    },
    "API-CLIENT-2": {
        "status": "healthy",
        "last_seen": "2026-05-08T10:10:00+08:00",
        "detail": "No recent authentication failures.",
    },
}

SUPPORT_ARTICLES: dict[str, dict[str, str]] = {
    "handoff": {
        "title": "When to hand off a customer conversation",
        "summary": "Use handoff when one specialist should take over the next turn.",
    },
    "agent-as-tool": {
        "title": "When to call another agent as a tool",
        "summary": "Use agent-as-tool when the caller should keep control and combine results.",
    },
    "billing-policy": {
        "title": "Billing policy escalation guide",
        "summary": "Refund promises require invoice status and policy lookup first.",
    },
}

SPECIALIST_NAMES = {
    "billing": "BillingAgent",
    "tech": "TechSupportAgent",
    "research": "ResearchAgent",
}


def dump_json(data: Any) -> str:
    return json.dumps(data, ensure_ascii=False, indent=2)


def normalize_identifier(value: str) -> str:
    return value.strip().upper()


def get_invoice_status_data(invoice_id: str) -> dict[str, Any]:
    normalized = normalize_identifier(invoice_id)
    invoice = INVOICES.get(normalized)

    if invoice is None:
        return {
            "invoice_id": normalized,
            "found": False,
            "status": "not_found",
            "amount": None,
            "due_date": None,
            "note": "No matching invoice exists in the demo database.",
        }

    return {
        "invoice_id": normalized,
        "found": True,
        "status": invoice["status"],
        "amount": invoice["amount"],
        "due_date": invoice["due_date"],
        "note": invoice["note"],
    }


def get_billing_policy_data(issue: str) -> dict[str, Any]:
    normalized = issue.strip().lower()

    if "refund" in normalized or "退款" in normalized:
        return {
            "issue": issue,
            "policy": "Refunds require a paid or duplicate charge record.",
            "risk": "Do not promise a refund without an invoice lookup.",
        }

    if "open" in normalized or "未付" in normalized or "扣费" in normalized:
        return {
            "issue": issue,
            "policy": "Open invoices can be cancelled before the renewal date.",
            "risk": "Cancellation after renewal requires billing review.",
        }

    return {
        "issue": issue,
        "policy": "Use invoice status first, then explain the matching billing rule.",
        "risk": "Unknown billing issue; avoid inventing policy details.",
    }


def get_device_status_data(device_id: str) -> dict[str, Any]:
    normalized = normalize_identifier(device_id)
    device = DEVICES.get(normalized)

    if device is None:
        return {
            "device_id": normalized,
            "found": False,
            "status": "unknown",
            "last_seen": None,
            "detail": "No matching device exists in the demo database.",
        }

    return {
        "device_id": normalized,
        "found": True,
        "status": device["status"],
        "last_seen": device["last_seen"],
        "detail": device["detail"],
    }


def create_tech_ticket_data(device_id: str, symptom: str) -> dict[str, Any]:
    normalized = normalize_identifier(device_id)
    digest = hashlib.sha1(f"{normalized}:{symptom}".encode("utf-8")).hexdigest()
    ticket_seed = int(digest[:8], 16) % 10000
    return {
        "ticket_id": f"TECH-{ticket_seed:04d}",
        "device_id": normalized,
        "symptom": symptom.strip(),
        "priority": "high" if normalized in DEVICES else "normal",
        "status": "created_in_demo",
    }


def search_support_articles_data(topic: str) -> list[dict[str, str]]:
    terms = topic.lower().split()
    matches: list[dict[str, str]] = []

    for article_id, article in SUPPORT_ARTICLES.items():
        haystack = f"{article_id} {article['title']} {article['summary']}".lower()
        if not terms or any(term in haystack for term in terms):
            matches.append(
                {
                    "article_id": article_id,
                    "title": article["title"],
                    "summary": article["summary"],
                }
            )

    return matches or [
        {
            "article_id": "no_match",
            "title": "No matching support article",
            "summary": "Ask a narrower question or add a new knowledge-base entry.",
        }
    ]


@function_tool
def get_invoice_status(invoice_id: str) -> dict[str, Any]:
    """Look up a demo invoice by invoice id.

    Args:
        invoice_id: Invoice id to look up, for example INV-1002.
    """
    return get_invoice_status_data(invoice_id)


@function_tool
def get_billing_policy(issue: str) -> dict[str, Any]:
    """Return the billing rule that applies to a refund, cancellation, or charge issue.

    Args:
        issue: Short description of the billing issue.
    """
    return get_billing_policy_data(issue)


@function_tool
def get_device_status(device_id: str) -> dict[str, Any]:
    """Look up a demo device or API client status.

    Args:
        device_id: Device id to look up, for example ROUTER-7.
    """
    return get_device_status_data(device_id)


@function_tool
def create_tech_ticket(device_id: str, symptom: str) -> dict[str, Any]:
    """Create a demo technical-support ticket.

    Args:
        device_id: Device or API client id.
        symptom: Customer-reported symptom.
    """
    return create_tech_ticket_data(device_id, symptom)


@function_tool
def search_support_articles(topic: str) -> list[dict[str, str]]:
    """Search the demo support knowledge base.

    Args:
        topic: Topic to search for.
    """
    return search_support_articles_data(topic)


def build_billing_agent(model: str) -> Agent:
    return Agent(
        name=SPECIALIST_NAMES["billing"],
        handoff_description="Handles invoices, charges, refunds, cancellations, and payment policy.",
        instructions=(
            "You are the billing specialist. Only handle billing questions. "
            "Use get_invoice_status for invoice ids and get_billing_policy before explaining refunds, "
            "cancellations, or charges. Do not diagnose technical issues."
        ),
        model=model,
        model_settings=ModelSettings(parallel_tool_calls=False, verbosity="low"),
        tools=[get_invoice_status, get_billing_policy],
    )


def build_tech_agent(model: str) -> Agent:
    return Agent(
        name=SPECIALIST_NAMES["tech"],
        handoff_description="Handles technical support, device status, API client issues, and tickets.",
        instructions=(
            "You are the technical support specialist. Only handle technical support questions. "
            "Use get_device_status before diagnosing known devices or API clients. "
            "Use create_tech_ticket when the user needs follow-up support. Do not discuss refunds."
        ),
        model=model,
        model_settings=ModelSettings(parallel_tool_calls=False, verbosity="low"),
        tools=[get_device_status, create_tech_ticket],
    )


def build_research_agent(model: str) -> Agent:
    return Agent(
        name=SPECIALIST_NAMES["research"],
        handoff_description="Handles support knowledge-base research and article lookup.",
        instructions=(
            "You are the research specialist. Only answer from the demo support knowledge base. "
            "Use search_support_articles and cite article_id values from the tool result. "
            "Say when the demo corpus has no matching article."
        ),
        model=model,
        model_settings=ModelSettings(parallel_tool_calls=False, verbosity="low"),
        tools=[search_support_articles],
    )


def build_specialists(model: str, disabled_agents: set[str]) -> dict[str, Agent]:
    builders = {
        "billing": build_billing_agent,
        "tech": build_tech_agent,
        "research": build_research_agent,
    }
    return {
        key: builder(model)
        for key, builder in builders.items()
        if key not in disabled_agents
    }


def build_handoff_triage_agent(model: str, specialists: dict[str, Agent]) -> Agent:
    available = ", ".join(agent.name for agent in specialists.values()) or "none"
    return Agent(
        name="TriageAgent",
        instructions=(
            "You are the triage agent. Decide whether the customer needs billing, "
            "technical support, or support-article research. Handoff to exactly one available "
            f"specialist when the request fits that specialist. Available specialists: {available}. "
            "If no available specialist matches, explain the boundary instead of guessing. "
            "Do not call specialist tools yourself."
        ),
        model=model,
        model_settings=ModelSettings(parallel_tool_calls=False, verbosity="low"),
        handoffs=list(specialists.values()),
    )


def build_agent_tool_triage_agent(model: str, specialists: dict[str, Agent]) -> Agent:
    tools = []
    if "billing" in specialists:
        tools.append(
            specialists["billing"].as_tool(
                tool_name="ask_billing_agent",
                tool_description="Ask BillingAgent about invoices, charges, refunds, or cancellations.",
            )
        )
    if "tech" in specialists:
        tools.append(
            specialists["tech"].as_tool(
                tool_name="ask_tech_support_agent",
                tool_description="Ask TechSupportAgent about device, API, or technical support issues.",
            )
        )
    if "research" in specialists:
        tools.append(
            specialists["research"].as_tool(
                tool_name="ask_research_agent",
                tool_description="Ask ResearchAgent to search support articles and cite article ids.",
            )
        )

    tool_names = ", ".join(tool.name for tool in tools) or "none"
    return Agent(
        name="TriageAgent",
        instructions=(
            "You are the triage agent. Keep control of the conversation. "
            "Use specialist agents as tools when you need their scoped expertise, then combine "
            f"their results into one concise answer. Available specialist tools: {tool_names}. "
            "If no tool covers part of the request, say that boundary clearly."
        ),
        model=model,
        model_settings=ModelSettings(parallel_tool_calls=False, verbosity="low"),
        tools=tools,
    )


def build_triage_agent(
    mode: str,
    model: str,
    disabled_agents: set[str],
) -> tuple[Agent, dict[str, Agent]]:
    specialists = build_specialists(model, disabled_agents)
    if mode == "handoff":
        return build_handoff_triage_agent(model, specialists), specialists
    return build_agent_tool_triage_agent(model, specialists), specialists


def classify_question(question: str) -> str:
    normalized = question.lower()
    keyword_map = {
        "billing": ["账务", "发票", "invoice", "refund", "退款", "扣费", "charge", "cancel"],
        "tech": ["技术", "故障", "device", "router", "api", "ticket", "登录", "报错"],
        "research": ["资料", "研究", "article", "knowledge", "文档", "引用", "handoff"],
    }

    scores = {
        route: sum(1 for keyword in keywords if keyword in normalized)
        for route, keywords in keyword_map.items()
    }
    route, score = max(scores.items(), key=lambda item: item[1])
    return route if score > 0 else "unknown"


def local_routing_demo(args: argparse.Namespace) -> None:
    disabled_agents = set(args.disable_agent)
    route = classify_question(args.question)
    specialists = {
        key: {
            "agent_name": name,
            "available": key not in disabled_agents,
            "tool_boundary": tool_boundary(key),
        }
        for key, name in SPECIALIST_NAMES.items()
    }

    print(
        dump_json(
            {
                "mode": args.mode,
                "question": args.question,
                "heuristic_route": route,
                "route_available": route in specialists and specialists[route]["available"],
                "specialists": specialists,
                "note": "This local demo does not call the model. Run without --local-routing-only to inspect SDK run items and platform trace.",
            }
        )
    )


def tool_boundary(agent_key: str) -> list[str]:
    boundaries = {
        "billing": ["get_invoice_status", "get_billing_policy"],
        "tech": ["get_device_status", "create_tech_ticket"],
        "research": ["search_support_articles"],
    }
    return boundaries[agent_key]


def raw_value(raw_item: Any, field: str) -> Any:
    if isinstance(raw_item, dict):
        return raw_item.get(field)
    return getattr(raw_item, field, None)


def summarize_run_item(item: Any) -> dict[str, Any]:
    agent_name = getattr(getattr(item, "agent", None), "name", None)

    if isinstance(item, HandoffCallItem):
        return {
            "type": item.type,
            "agent": agent_name,
            "handoff_tool": raw_value(item.raw_item, "name"),
            "call_id": raw_value(item.raw_item, "call_id"),
        }

    if isinstance(item, HandoffOutputItem):
        return {
            "type": item.type,
            "source_agent": item.source_agent.name,
            "target_agent": item.target_agent.name,
        }

    if isinstance(item, ToolCallItem):
        return {
            "type": item.type,
            "agent": agent_name,
            "tool_name": getattr(item, "tool_name", None) or raw_value(item.raw_item, "name"),
            "call_id": getattr(item, "call_id", None) or raw_value(item.raw_item, "call_id"),
        }

    if isinstance(item, ToolCallOutputItem):
        return {
            "type": item.type,
            "agent": agent_name,
            "call_id": raw_value(item.raw_item, "call_id"),
            "output": item.output,
        }

    if isinstance(item, MessageOutputItem):
        return {"type": item.type, "agent": agent_name}

    return {
        "type": getattr(item, "type", type(item).__name__),
        "agent": agent_name,
    }


def require_api_key() -> None:
    if not os.getenv("OPENAI_API_KEY"):
        raise SystemExit("OPENAI_API_KEY is not set. Set it before running API-backed Lab 04.")


def run_orchestration(args: argparse.Namespace) -> None:
    require_api_key()
    disabled_agents = set(args.disable_agent)
    triage_agent, specialists = build_triage_agent(args.mode, args.model, disabled_agents)
    run_config = RunConfig(
        workflow_name=WORKFLOW_NAME,
        trace_metadata={
            "lab": "04-orchestration-handoffs",
            "mode": args.mode,
            "disabled_agents": ",".join(sorted(disabled_agents)) or "none",
        },
    )
    result = Runner.run_sync(triage_agent, args.question, run_config=run_config)

    print(
        dump_json(
            {
                "model": args.model,
                "mode": args.mode,
                "workflow_name": WORKFLOW_NAME,
                "available_specialists": [agent.name for agent in specialists.values()],
                "new_items": [summarize_run_item(item) for item in result.new_items],
                "final_output": result.final_output,
                "last_response_id": result.last_response_id,
                "trace_note": "Open the OpenAI Dashboard trace viewer and filter by workflow name.",
            }
        )
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Lab 04: OpenAI Agents SDK orchestration, handoffs, and agent-as-tool demo.",
    )
    parser.add_argument(
        "question",
        nargs="?",
        default="请帮我查一下 INV-1002 为什么还没结清，并说明能不能取消这笔扣费。",
        help="Customer question for the triage agent.",
    )
    parser.add_argument(
        "--mode",
        choices=["handoff", "agent-as-tool"],
        default="handoff",
        help="Use handoff or call specialist agents as tools.",
    )
    parser.add_argument(
        "--model",
        default=DEFAULT_MODEL,
        help="OpenAI model id. Defaults to OPENAI_MODEL or gpt-5.5.",
    )
    parser.add_argument(
        "--disable-agent",
        choices=sorted(SPECIALIST_NAMES),
        action="append",
        default=[],
        help="Remove one specialist from the run to inspect system boundaries. Can be repeated.",
    )
    parser.add_argument(
        "--local-routing-only",
        action="store_true",
        help="Show local routing and tool boundaries without calling the OpenAI API.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    if args.local_routing_only:
        local_routing_demo(args)
        return

    run_orchestration(args)


if __name__ == "__main__":
    main()
