# Lab 04: Orchestration and Handoffs

## 目标

理解什么时候需要多个 Agent，以及 `handoff` 和 `agent-as-tool` 的边界。

## 要学的东西

- Handoff
- Agent as tool
- Routing agent
- Specialist agents
- 工具边界

官方资料：

- https://openai.github.io/openai-agents-python/multi_agent/
- https://openai.github.io/openai-agents-python/handoffs/
- https://openai.github.io/openai-agents-python/tools/
- https://openai.github.io/openai-agents-python/tracing/

## 最小实验

做一个多 Agent 客服系统：

- `TriageAgent`: 判断问题类型
- `BillingAgent`: 账务问题
- `TechSupportAgent`: 技术支持
- `ResearchAgent`: 资料研究

实现文件：

- `support_orchestration_cli.py`

核心数据结构：

```text
TriageAgent
  ├─ BillingAgent: get_invoice_status / get_billing_policy
  ├─ TechSupportAgent: get_device_status / create_tech_ticket
  └─ ResearchAgent: search_support_articles
```

同一组三个 specialist 支持两种编排方式：

```text
handoff:
用户问题 -> TriageAgent -> 转交给一个 specialist -> specialist 接管后续回答

agent-as-tool:
用户问题 -> TriageAgent -> 调用一个或多个 specialist tool -> TriageAgent 汇总最终回答
```

这两个模式不要混为一谈。`handoff` 是控制权转移；`agent-as-tool` 是主 Agent 调用子 Agent 后继续掌控最终输出。

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

先看本地路由和工具边界，不调用 API：

```bash
uv run python 50-实验验证/openai/04-orchestration-handoffs/support_orchestration_cli.py \
  "请帮我查一下 INV-1002 为什么还没结清，并说明能不能取消这笔扣费。" \
  --local-routing-only
```

运行 handoff 模式：

```bash
uv run python 50-实验验证/openai/04-orchestration-handoffs/support_orchestration_cli.py \
  "请帮我查一下 INV-1002 为什么还没结清，并说明能不能取消这笔扣费。" \
  --mode handoff
```

运行 agent-as-tool 模式：

```bash
uv run python 50-实验验证/openai/04-orchestration-handoffs/support_orchestration_cli.py \
  "ROUTER-7 网络不稳定，同时我想了解 handoff 和 agent-as-tool 的区别。" \
  --mode agent-as-tool
```

删除任意一个 specialist，观察边界：

```bash
uv run python 50-实验验证/openai/04-orchestration-handoffs/support_orchestration_cli.py \
  "ROUTER-7 网络不稳定，请帮我创建技术支持工单。" \
  --mode handoff \
  --disable-agent tech
```

可用演示数据：

```text
Invoices: INV-1001, INV-1002, INV-1003
Devices: ROUTER-7, API-CLIENT-2
Articles: handoff, agent-as-tool, billing-policy
```

## 输出说明

完整实验输出是 JSON，重点看：

- `mode`: 当前是 `handoff` 还是 `agent-as-tool`。
- `available_specialists`: 本次可用 specialist。
- `new_items[].type`: 是否出现 `handoff_call_item`、`handoff_output_item`、`tool_call_item`、`tool_call_output_item`。
- `new_items[].target_agent`: handoff 最终转给了哪个 specialist。
- `new_items[].tool_name`: agent-as-tool 或 specialist 内部 function tool 的调用情况。
- `workflow_name`: trace 里用它过滤这次实验。

## 验收标准

- 能解释为什么需要拆成多个 Agent。
- 每个 Agent 的工具不同。
- trace 中能看到 handoff 或 agent-as-tool。
- 删除任意一个 specialist 时，系统行为边界清楚。

## 工程判断

值得拆 Agent：

- 工具权限不同，例如账务能查发票，技术支持能建工单。
- instructions 明显不同，放在一个 Agent 里会互相污染。
- 需要 trace 里清楚看见谁处理了哪类问题。

不值得拆 Agent：

- 只是三个 prompt 名字不同，背后工具和数据完全一样。
- 单 Agent 加两个工具就能清楚解决。
- 为了“看起来像多 Agent”硬加路由层。

多 Agent 不是高级。边界清楚才有价值；边界不清楚就是把混乱拆成几份。
