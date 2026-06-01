# OpenAI Agents SDK Lab 02

日期：2026-05-08

## 今天读了什么

- OpenAI Agents SDK quickstart
- OpenAI Agents SDK tools guide
- OpenAI Agents SDK sessions guide
- OpenAI Agents SDK tracing guide

官方资料：

- https://openai.github.io/openai-agents-python/quickstart/
- https://openai.github.io/openai-agents-python/tools/
- https://openai.github.io/openai-agents-python/sessions/
- https://openai.github.io/openai-agents-python/tracing/

## 跑了什么实验

新增实验文件：

- `50-实验验证/openai/02-agents-sdk-basic/support_agent_cli.py`

实验目标：

```text
用户输入客服问题
  -> Runner.run_sync(agent, input, session=...)
  -> Agent 根据工具 schema 选择 function tool
  -> SDK 调用本地 get_order_status / get_refund_policy
  -> SDK 把工具结果交回模型
  -> Agent 输出最终回答
```

本地工具验证命令：

```bash
uv run python 50-实验验证/openai/02-agents-sdk-basic/support_agent_cli.py ORDER-1001 --local-tools-only
```

完整 API 验证命令：

```bash
uv run python 50-实验验证/openai/02-agents-sdk-basic/support_agent_cli.py \
  "请查询 ORDER-1001 的物流状态，并说明如果我要退款应该怎么办。"
```

session 验证命令：

```bash
uv run python 50-实验验证/openai/02-agents-sdk-basic/support_agent_cli.py \
  "请查询 ORDER-1002 的物流状态。" \
  --follow-up "刚才那个订单如果现在取消，退款规则是什么？"
```

## 关键理解

Lab 01 直接使用 Responses API，需要自己处理：

- 读取 `response.output` 里的 `function_call`
- 解析工具参数
- 执行本地函数
- 组装 `function_call_output`
- 用 `previous_response_id` 接上下一轮模型调用

Lab 02 使用 Agents SDK 后，这段循环变成：

```python
result = Runner.run_sync(agent, question, session=session, run_config=run_config)
```

SDK 省掉了工具循环的样板代码，但不是魔法。工具边界、输入参数、返回结构、权限判断仍然是应用代码的责任。

`result.new_items` 是观察 SDK 行为的入口。里面会出现：

- `message_output_item`: 模型消息
- `tool_call_item`: 模型请求调用工具
- `tool_call_output_item`: 本地工具执行结果

`SQLiteSession` 解决的是会话历史问题。默认 `:memory:` 只在当前进程有效；如果传文件路径，才会跨进程保留。

Tracing 解决的是运行观察问题。代码设置了 `workflow_name = "Lab 02 Agents SDK Basic"`，方便在 OpenAI Dashboard 里过滤模型调用和工具调用。

## 工程判断

这个能力适合：

- 单 Agent 客服、查询、政策解释这类低风险流程。
- 想保留 trace、session、tool call 观察能力的实验。
- 后续逐步加 guardrail、eval、handoff 的项目。

这个能力不适合：

- 直接做高风险动作，比如退款、发邮件、改数据库。读工具和写工具必须分开，写工具要有人审。
- 把退款政策写成一大坨 prompt。政策应该放在工具或业务配置里。
- 过早做多 Agent。当前只需要一个 Agent 和两个工具，多 Agent 现在只是复杂性。

## 不清楚的问题

- 当前环境没有设置 `OPENAI_API_KEY`，所以完整 Agents SDK API 路径还没验证。
- 需要用真实 trace 看一次 `workflow_name`、tool call、tool output 在 Dashboard 里的呈现。
- 后续要比较：Agents SDK 的 session 与 Responses API 的 `previous_response_id` 在工程控制上的差异。
