# Notes

资料消化目录，用来沉淀视频、文章、课程、概念解释、工具观察和临时 watchlist。

这里不是收藏夹。每篇笔记至少要把资料转成自己的理解、问题清单或工程判断。

## 主题目录

- [openai/](openai/)：OpenAI 主线学习笔记和实验复盘。
- [agent-systems/](agent-systems/)：Agent 架构、Agent Skill、Context Engineering、生产工程经验。
- [llm-basics/](llm-basics/)：token、采样参数等 LLM 基础概念。
- [mcp-cli-browser/](mcp-cli-browser/)：MCP、CLI 工具、浏览器自动化和 Codex Chrome。
- [rag/](rag/)：RAG 基础机制、最小实现和 Agentic RAG。
- [ragflow/](ragflow/)：RAGFlow 专项视频、官方资料、部署、评测和 Dify 集成。
- [watchlists/](watchlists/)：学习清单、候选资料和后续筛选入口。

## 归档规则

命名建议：

```text
YYYY-MM-DD-topic.md
```

视频、文章或课程笔记建议包含：

- 今天读了什么
- 核心观点是什么
- 哪些信息值得后续研究
- 哪些地方不清楚
- 这个能力适合什么场景
- 这个能力不适合什么场景

如果资料值得升级为实验，再补充：

- 准备验证什么判断
- 跑了什么实验
- 实验结论是什么

只有满足以下任一条件，才升级为 `labs/`：

- 涉及一个可运行 API、SDK、工具链或 Agent 能力。
- 能验证一个具体工程判断。
- 能复现一个重要失败模式。
- 能产出一个可复用的小工具或最小 demo。

不要把同一个主题拆得到处都是。新笔记先按主题归档；只有当它变成场景调研、开源项目拆解或可运行实验时，再升级到 `research/` 或 `labs/`。
