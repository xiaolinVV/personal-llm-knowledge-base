# Lab 02: Agents SDK Basic

## 目标

用 OpenAI Agents SDK 做一个单 Agent，并和 Lab 01 的手写 Responses API 工具循环做对比。

## 要学的东西

- Agent 定义
- Runner / run
- function tool
- session
- tracing

官方资料：

- https://openai.github.io/openai-agents-python/quickstart/
- https://openai.github.io/openai-agents-python/tools/
- https://openai.github.io/openai-agents-python/sessions/
- https://openai.github.io/openai-agents-python/tracing/

## 最小实验

做一个客服 Agent：

- 工具 1：查询订单状态
- 工具 2：查询退款规则
- Agent 根据用户问题决定是否调用工具

实现文件：

- `support_agent_cli.py`

核心数据流：

```text
用户问题
  ↓
Runner.run_sync(agent, input, session=...)
  ↓
Agent 根据 instructions 和工具 schema 选择 function tool
  ↓
SDK 执行本地 Python tool
  ↓
SDK 把 tool output 交回模型
  ↓
返回 final_output，并在 result.new_items 中保留 message/tool call/tool output
```

Lab 01 手写了这个 run loop；Lab 02 的重点是观察 SDK 帮你隐藏了哪些步骤。

## 依赖

本仓库使用 `uv`：

```bash
uv sync
```

需要设置 OpenAI API key：

```bash
export OPENAI_API_KEY="你的 key"
```

默认模型使用 `gpt-5.5`，也可以覆盖：

```bash
export OPENAI_MODEL="gpt-5.5"
```

## 运行

先验证本地工具，不调用 API：

```bash
uv run python wiki/labs/openai/02-agents-sdk-basic/support_agent_cli.py ORDER-1001 --local-tools-only
```

运行完整 Agents SDK 实验：

```bash
uv run python wiki/labs/openai/02-agents-sdk-basic/support_agent_cli.py \
  "请查询 ORDER-1001 的物流状态，并说明如果我要退款应该怎么办。"
```

验证 session 的第二轮上下文：

```bash
uv run python wiki/labs/openai/02-agents-sdk-basic/support_agent_cli.py \
  "请查询 ORDER-1002 的物流状态。" \
  --follow-up "刚才那个订单如果现在取消，退款规则是什么？"
```

如果要把 session 存到本地 SQLite 文件，显式传路径：

```bash
uv run python wiki/labs/openai/02-agents-sdk-basic/support_agent_cli.py \
  "请查询 ORDER-1003 的物流状态。" \
  --session-db wiki/labs/openai/02-agents-sdk-basic/.sessions/lab02.sqlite
```

可用的演示订单：

```text
ORDER-1001
ORDER-1002
ORDER-1003
```

也可以试一个不存在的订单：

```bash
uv run python wiki/labs/openai/02-agents-sdk-basic/support_agent_cli.py \
  "请查询 ORDER-9999 的物流状态，并说明退款规则。"
```

## 验收标准

- Agent 能回答普通问题。
- Agent 能调用至少两个工具。
- 能在 trace 中看到模型调用和工具调用。
- instructions 不超过必要长度，业务逻辑不塞进长 prompt。

验收时重点看输出里的这些字段：

- `workflow_name`: trace 里用它过滤这次实验。
- `turns[].new_items[].type`: 应该能看到 `tool_call_item` 和 `tool_call_output_item`。
- `turns[].new_items[].tool_name`: 应该出现 `get_order_status`，退款问题里应出现 `get_refund_policy`。
- `turns[].final_output`: Agent 的最终回答。
- `turns[].last_response_id`: 底层 Responses API 响应 ID。

注意：Tracing 默认依赖 OpenAI 平台侧记录。CLI 会设置 `workflow_name`，但真正的 trace 需要在 Dashboard 里查看。

## 工程判断

Agents SDK 适合：

- 想少写手动 tool loop 的单 Agent。
- 需要统一观察 `new_items`、session、trace 的实验。
- 后续要接 guardrail、handoff、eval 的项目。

Agents SDK 不适合：

- 用 prompt 承载大量业务规则。规则应该下沉到工具和业务代码。
- 一上来暴露十几个工具让模型乱选。
- 还没弄清单 Agent 行为就做多 Agent。
