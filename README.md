# AI Agent Fieldbook

这个仓库是一个 AI Agent 学习研究手册，用来沉淀资料消化、技术深挖、工具观察、真实案例拆解和必要的实验验证。

它不是资料收藏夹，也不是单纯的代码实验室。资料进来以后，必须尽量转化成清楚的理解、可复查的研究记录、必要时可运行的实验，以及最后的工程判断。

核心原则很简单：

- 先学官方原语，再学框架包装。
- 先做单 Agent，再做多 Agent。
- 先把工具调用、状态、追踪、评估弄清楚，再谈复杂 orchestration。
- 资料不能只收藏，要消化成笔记、研究判断或实验。
- 学完必须拆真实项目，否则只是背文档。

## 内容模型

这个 fieldbook 按四层沉淀内容：

1. 资料消化：视频、文章、课程、官方文档的学习笔记，放在 `notes/`。
2. 技术研究：围绕一个主题做深入分析，比如 Context Engineering、MCP、CLI 工具、Agent runtime，放在 `research/` 或专题文档中。
3. 案例拆解：真实产品、开源项目、行业场景的结构化拆解，放在 `research/use-cases/` 或 `research/open-source-projects/`。
4. 实验验证：只有当资料里有关键假设需要验证，才升级成 `labs/` 里的最小可运行实验。

不是每篇资料都需要变成实验。只有满足以下任一条件，才升级为 lab：

- 涉及一个可运行 API、SDK、工具链或 Agent 能力。
- 能验证一个具体工程判断。
- 能复现一个重要失败模式。
- 能产出一个可复用的小工具或最小 demo。

## 仓库结构

```text
.
├── docs/
│   ├── 00-learning-principles.md
│   ├── 01-roadmap.md
│   ├── 02-official-resources.md
│   ├── 03-openai-stack.md
│   ├── 04-anthropic-stack.md
│   └── 05-field-research-plan.md
├── labs/
│   ├── openai/
│   │   ├── 01-responses-api/
│   │   ├── 02-agents-sdk-basic/
│   │   ├── 03-tools-and-rag/
│   │   ├── 04-orchestration-handoffs/
│   │   ├── 05-guardrails-evals-tracing/
│   │   └── 06-sandbox-agents/
│   └── anthropic/
├── research/
│   ├── open-source-projects/
│   └── use-cases/
└── notes/
```

## 研究主线

### Phase 1: OpenAI 官方 Agent 技术栈

目标：掌握 OpenAI 官方 Agent 开发主线。

学习顺序：

1. Building agents 概念模型
2. Responses API
3. Agents SDK
4. Tools: function calling, web search, file search, MCP, code interpreter
5. Orchestration: handoffs, agent-as-tool, routing
6. Guardrails, tracing, evals
7. Sandbox agents 和长任务
8. 小型端到端项目

### Phase 2: Anthropic / Claude Agent 技术栈

目标：理解 Claude 生态的 Agent 开发方式，并和 OpenAI 栈对比。

学习顺序：

1. Claude Messages API
2. Tool use
3. Model Context Protocol
4. Claude Agent SDK
5. Computer use
6. Claude Code SDK
7. 与 OpenAI Agents SDK 做能力和工程边界对比

### Phase 3: 真实场景和开源项目拆解

目标：把官方知识落到真实系统里。

学习顺序：

1. 调研市面真实 Agent 应用场景
2. 筛选开源 Agent 项目
3. 拆解架构、工具边界、状态管理、评估方式
4. 复刻一个最小可用版本
5. 总结什么值得学，什么只是炫技

## 单个主题的沉淀标准

每研究一个主题，至少尽量留下这几样东西：

- 一份学习笔记或研究记录，放在 `notes/` 或 `research/`。
- 一份问题清单：哪些地方官方文档、视频或文章没讲清楚。
- 一份工程判断：这个能力适合什么场景，不适合什么场景。
- 如果值得验证，再补一个可运行实验，放在对应 `labs/` 子目录。

## 快速开始

准备环境变量：

```bash
cp .env.example .env
```

Python 路线建议使用 `uv` 或普通虚拟环境。第一阶段先不急着安装所有依赖，进入每个 lab 时按该 lab 的 README 安装需要的包。

## 当前状态

- [x] 升级为 `AI Agent Fieldbook` 定位
- [x] 建立 OpenAI 第一阶段路线
- [x] 预留 Anthropic 第二阶段
- [x] 预留真实场景和开源项目调研阶段
- [x] 完成 Lab 01: Responses API 最小实验（完整 API 路径仍需 `OPENAI_API_KEY` 验证）
- [x] 开始 Lab 02: Agents SDK Basic
- [x] 开始 Lab 03: Tools and Retrieval
- [x] 开始 Lab 04: Orchestration and Handoffs
