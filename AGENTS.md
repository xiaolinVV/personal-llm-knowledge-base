# AGENTS.md

本仓库是 AI Agent Fieldbook：面向 AI Agent 领域的长期学习研究手册。未来协作时遵守这些规则。

## 默认语言

对话和学习笔记默认使用中文。代码、命令、API 字段、提交信息可使用英文。

## 学习研究顺序

主线研究不要跳阶段；临时发现的新资料可以先沉淀，但深入研究和实验验证应尽量回到主线：

1. OpenAI 官方技术栈
2. Anthropic / Claude 技术栈
3. 真实应用场景和开源项目拆解
4. 自己实现小型 Agent 产品

## 工程原则

- 官方文档优先，博客和二手教程只能作为补充。
- 不要上来就做多 Agent。先把单 Agent、工具调用、状态、追踪和评估做好。
- 每个实验必须能说明一个具体问题，不能为了“看起来高级”添加复杂性。
- 资料不能只收藏。视频、文章、工具和案例要尽量消化成笔记、研究判断或实验验证。
- 学习笔记、研究记录、复盘和说明文档要写得通俗易懂。复杂逻辑优先用步骤、例子或 Mermaid 图解释，不要堆术语。
- 高风险动作必须有人审：发邮件、改数据库、调用支付、执行 shell、写文件。
- 未验证就不要声称完成。只说已经做了什么、还没验证什么。

## 文件约定

- `docs/`: 路线、原则、官方资源、主题索引和主线专题。
- `labs/`: 可运行实验，只放需要验证关键判断的最小实验。
- `notes/`: 视频、文章、课程、概念、工具的学习笔记和资料消化；按主题子目录归档。
- `notes/openai/`: OpenAI 主线学习笔记和实验复盘。
- `notes/agent-systems/`: Agent 架构、Agent Skill、Context Engineering、生产工程经验。
- `notes/llm-basics/`: token、采样参数等 LLM 基础概念。
- `notes/mcp-cli-browser/`: MCP、CLI 工具基础和选型笔记。
- `notes/rag/`: RAG 基础机制、最小实现和 Agentic RAG 笔记。
- `notes/ragflow/`: RAGFlow 专项视频、官方资料、部署、评测和 Dify 集成笔记。
- `notes/watchlists/`: 临时学习清单和候选资料筛选。
- `research/`: 研究报告入口索引。
- `research/use-cases/`: 实际应用场景调研。
- `research/open-source-projects/`: 开源项目拆解。
- `research/open-source-projects/browser-automation/`: 浏览器自动化、CDP、真实浏览器 runtime、CloakBrowser、Crawl4AI、Codex Chrome 相关研究入口。
- `.codex/skills/`: 项目内可复用 Skill。处理学习视频沉淀时优先使用 `video-study-notes`。

## 每次新增实验

每个 lab 至少包含：

- `README.md`: 目标、依赖、运行方式、验收标准。
- 最小可运行代码。
- 明确的验证命令。
- 学习笔记或复盘链接。
