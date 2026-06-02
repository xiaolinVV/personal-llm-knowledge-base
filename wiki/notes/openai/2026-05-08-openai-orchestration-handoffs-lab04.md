# OpenAI Orchestration and Handoffs Lab 04

日期：2026-05-08

## 今天读了什么

- OpenAI Agents SDK multi-agent guide
- OpenAI Agents SDK handoffs guide
- OpenAI Agents SDK tools guide
- OpenAI Agents SDK tracing guide

官方资料：

- https://openai.github.io/openai-agents-python/multi_agent/
- https://openai.github.io/openai-agents-python/handoffs/
- https://openai.github.io/openai-agents-python/tools/
- https://openai.github.io/openai-agents-python/tracing/

## 跑了什么实验

新增实验文件：

- `wiki/labs/openai/04-orchestration-handoffs/support_orchestration_cli.py`

实验目标：

```text
用户问题
  -> TriageAgent 判断问题类型
  -> BillingAgent / TechSupportAgent / ResearchAgent 处理专业问题
  -> 输出 SDK run items 和最终回答
  -> 在 trace 中观察 handoff 或 agent-as-tool
```

先验证本地路由和工具边界，不调用 API：

```bash
uv run python wiki/labs/openai/04-orchestration-handoffs/support_orchestration_cli.py \
  "请帮我查一下 INV-1002 为什么还没结清，并说明能不能取消这笔扣费。" \
  --local-routing-only
```

运行 handoff 模式：

```bash
uv run python wiki/labs/openai/04-orchestration-handoffs/support_orchestration_cli.py \
  "请帮我查一下 INV-1002 为什么还没结清，并说明能不能取消这笔扣费。" \
  --mode handoff
```

运行 agent-as-tool 模式：

```bash
uv run python wiki/labs/openai/04-orchestration-handoffs/support_orchestration_cli.py \
  "ROUTER-7 网络不稳定，同时我想了解 handoff 和 agent-as-tool 的区别。" \
  --mode agent-as-tool
```

删除 specialist 看边界：

```bash
uv run python wiki/labs/openai/04-orchestration-handoffs/support_orchestration_cli.py \
  "ROUTER-7 网络不稳定，请帮我创建技术支持工单。" \
  --mode handoff \
  --disable-agent tech
```

## 关键理解

Lab 04 的核心不是“多个 Agent 看起来更高级”，而是控制权和工具边界。

`handoff` 适合一个 specialist 接管后续对话：

```text
TriageAgent
  -> BillingAgent
  -> BillingAgent 使用账务工具并回答
```

这种模式下，路由之后的控制权转移给 specialist。验收时应该在 `new_items` 里看到：

- `handoff_call_item`
- `handoff_output_item`
- `target_agent`

`agent-as-tool` 适合主 Agent 保持控制权：

```text
TriageAgent
  -> ask_tech_support_agent(...)
  -> ask_research_agent(...)
  -> TriageAgent 汇总最终回答
```

这种模式适合一个问题需要多个 specialist 的结果。验收时重点看：

- `tool_call_item`
- `tool_call_output_item`
- `tool_name`

真正重要的数据结构是：

```text
Specialist Agent = instructions + allowed tools + handoff description
```

如果三个 Agent 只是名字不同，工具和数据完全一样，那就不该拆。那不是架构，是噪音。

## 工程判断

这个能力适合：

- 客服系统按权限拆分：账务、技术支持、资料研究。
- 不同 specialist 的工具边界不同。
- 需要在 trace 里审计“谁处理了什么”。
- 一个主 Agent 需要调用多个专家结果再汇总。

这个能力不适合：

- 单 Agent 加两个 function tool 就能解决的问题。
- 还没搞清楚单 Agent 行为，就上来做复杂路由。
- 业务边界不稳定，今天按部门拆，明天按产品拆，后天按语言拆。
- 用 prompt 强行模拟权限。权限应该在工具和后端边界里，不该靠模型自觉。

## 不清楚的问题

- 当前环境没有设置 `OPENAI_API_KEY`，所以 handoff 和 agent-as-tool 的真实 API 路径还没验证。
- 需要在 Dashboard trace 里观察一次真实运行，确认 `handoff_call_item`、`handoff_output_item` 和 specialist 内部 `tool_call_item` 的具体顺序。
- 需要比较多意图问题在 `handoff` 与 `agent-as-tool` 下的表现：前者可能只能清楚转给一个 specialist，后者更适合汇总多个 specialist。
