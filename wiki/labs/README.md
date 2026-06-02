# 实验验证

`wiki/labs/` 是验证层，只放能验证具体判断的最小实验。

实验不是仓库主角。没有明确验证问题的代码，不进 `wiki/labs/`。

## 与其他目录的边界

- 资料来源放 `../../raw/sources/`。
- 学习笔记放 `../notes/`。
- 稳定主题放 `../topics/`。
- 结构化研究放 `../research/`。
- 实验结论如果稳定，要回写到 `../topics/` 或 `../research/`。

## 当前目录

- [openai/](openai/)：OpenAI Responses API、Agents SDK、工具调用、RAG、handoffs、guardrails、evals、sandbox 等最小实验。
- [anthropic/](anthropic/)：Anthropic / Claude 相关实验入口。

## 每个实验必须包含

- `README.md`：目标、依赖、运行方式、验收标准。
- 最小可运行代码。
- 明确的验证命令。
- 实验结论或复盘链接。
- 未验证事项。

新增实验优先使用 [lab 模板](../../schema/templates/lab.md)。
