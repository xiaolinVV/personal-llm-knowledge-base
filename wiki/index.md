---
type: index
domain: meta
status: active
created: 2026-06-02
updated: 2026-06-02
source_refs: []
---

# Wiki Index

这个文件是 LLM Wiki 的内容索引。回答问题、入库、lint 或输出回写前，先读这里，再进入相关页面。

> 本索引只证明文件存在和导航关系，不证明每篇内容的事实已经重新核验。

## Raw Inbox

| Page | Type | Status | Sources | Summary |
| --- | --- | --- | ---: | --- |
| [收件箱](../raw/inbox/README.md) | page |  | 0 | `raw/inbox/` 是临时入口，只放尚未处理的资料卡片、想法和待归档线索。 |

## Raw Sources

| Page | Type | Status | Sources | Summary |
| --- | --- | --- | ---: | --- |
| [来源索引](../raw/sources/README.md) | page |  | 0 | `raw/sources/` 是轻量来源索引层，保存原始采集文档、本地图片资产和原始材料入口，而不是保存知识本身。 |
| [AI Sources](../raw/sources/ai/README.md) | page |  | 0 | AI 领域来源索引。 |
| [AI 官方资料清单](../raw/sources/ai/official-resources.md) | page |  | 0 | 这是 AI 主题的来源索引，不是稳定知识文件。跨来源整理后的结论应进入 `../../../wiki/topics/ai/` 或 `../../../wiki/research/`。 |
| [Implementing Text2SQL with RAGFlow](../raw/sources/ai/ragflow/official-practice-cases/2024-09-24-implementing-text2sql-with-ragflow/article.md) | page |  | 0 | > |
| [用 RAGFlow 实现 Text2SQL](../raw/sources/ai/ragflow/official-practice-cases/2024-09-24-implementing-text2sql-with-ragflow/article.zh.md) | page |  | 0 | > 原文：RAGFlow 官方博客《Implementing Text2SQL with RAGFlow》 |
| [Agentic Workflow - What's inside RAGFlow 0.20.0](../raw/sources/ai/ragflow/official-practice-cases/2025-08-05-agentic-workflow-ragflow-v0.20.0/article.md) | page |  | 0 | > |
| [Agentic Workflow：RAGFlow 0.20.0 里面有什么](../raw/sources/ai/ragflow/official-practice-cases/2025-08-05-agentic-workflow-ragflow-v0.20.0/article.zh.md) | page |  | 0 | > 原文：RAGFlow 官方博客《Agentic Workflow - What's inside RAGFlow 0.20.0》 |
| [RAGFlow 0.20.0 - Multi-Agent Deep Research](../raw/sources/ai/ragflow/official-practice-cases/2025-08-07-multi-agent-deep-research/article.md) | page |  | 0 | > |
| [RAGFlow 0.20.0：Multi-Agent Deep Research](../raw/sources/ai/ragflow/official-practice-cases/2025-08-07-multi-agent-deep-research/article.zh.md) | page |  | 0 | > 原文：RAGFlow 官方博客《RAGFlow 0.20.0 - Multi-Agent Deep Research》 |
| [Tutorial - Building a SQL Assistant Workflow](../raw/sources/ai/ragflow/official-practice-cases/2025-08-12-sql-assistant-workflow/article.md) | page |  | 0 | > |
| [教程：构建 SQL Assistant Workflow](../raw/sources/ai/ragflow/official-practice-cases/2025-08-12-sql-assistant-workflow/article.zh.md) | page |  | 0 | > 原文：RAGFlow 官方博客《Tutorial - Building a SQL Assistant Workflow》 |
| [Tutorial - Build an E-Commerce Customer Support Agent Using RAGFlow](../raw/sources/ai/ragflow/official-practice-cases/2025-09-12-e-commerce-customer-support-agent/article.md) | page |  | 0 | > |
| [使用 RAGFlow 构建电商客服 Agent](../raw/sources/ai/ragflow/official-practice-cases/2025-09-12-e-commerce-customer-support-agent/article.zh.md) | page |  | 0 | > 原文：RAGFlow 官方博客《Tutorial - Build an E-Commerce Customer Support Agent Using RAGFlow》 |
| [RAGFlow in Practice - Building an Agent for Deep-Dive Analysis of Company Research Reports](../raw/sources/ai/ragflow/official-practice-cases/2025-10-30-company-research-report-deep-dive-agent/article.md) | page |  | 0 | > |
| [RAGFlow 实践：构建公司研究报告深度分析 Agent](../raw/sources/ai/ragflow/official-practice-cases/2025-10-30-company-research-report-deep-dive-agent/article.zh.md) | page |  | 0 | > 原文：RAGFlow 官方博客《RAGFlow in Practice - Building an Agent for Deep-Dive Analysis of Company Research Reports》 |
| [README](../raw/sources/ai/ragflow/official-practice-cases/2025-10-30-company-research-report-deep-dive-agent/dataset/huggingface/InfiniFlow_company_financial_research_agent/raw/README.md) | page |  | 0 | 待补摘要。 |

## Notes

| Page | Type | Status | Sources | Summary |
| --- | --- | --- | ---: | --- |
| [资料笔记](notes/README.md) | page |  | 0 | `wiki/notes/` 是资料消化层，用来把视频、文章、书、课程、会议、聊天记录、概念解释和工具观察转成自己的中文笔记。 |
| [LangChain 年度报告：Agent 现状与 2025 趋势](notes/agent-systems/2025-12-27-langchain-agent-engineering-report.md) | page |  | 0 | Agent 已经从“能不能做”的概念验证阶段，进入“怎么可靠上线”的工程阶段。真正的硬问题不是把 LLM 包成一个 Agent，而是把非确定性的模型行为放进可观测、可评估、可控权限、可承受延迟的生产系统里。 |
| [能用脚本就别用 Agent：脚本 / Skill / Agent 的能力分层](notes/agent-systems/2026-05-12-script-skill-agent-pyramid.md) | page |  | 0 | 这篇文章真正有价值的地方不是“贬低 Agent”，而是给 Agent 落地划了一个很实用的优先级：确定性任务先脚本化，半确定但需要模型判断的能力做成 Skill，只有路径不可预知、需要动态规划和复杂判断的任务才交给 Agent。 |
| [AI Agent 工作原理与 Harness 工程](notes/agent-systems/2026-05-18-ai-agent-harness-principles.md) | page |  | 0 | Agent 解决的是“模型如何通过思考、行动、观察来干活”；Harness 解决的是“模型干活时如何不把系统搞崩”。没有 Harness 的 Agent 只是会调用工具的聊天模型，能 demo，不等于能进生产。 |
| [AI 落地实践中的 SOP：从流程文档到 Agent 执行规程](notes/agent-systems/2026-05-23-ai-sop-in-agent-practice.md) | page |  | 0 | AI 落地里的 SOP 不是把传统流程文档塞进提示词，而是把业务规则、工具权限、决策分支、异常处理、人工升级、输出格式和评估样例，沉淀成 Agent 能执行、系统能约束、人能审计的操作规程。 |
| [Agent Skill 从使用到原理，一次讲清](notes/agent-systems/Agent Skill 从使用到原理，一次讲清.md) | page |  | 0 | Agent Skill 的本质不是把 Prompt 写长，而是把可复用的工作规则、参考资料和可执行脚本打包成一个按需加载的能力单元：模型先看轻量目录，命中任务后再读指令，必要时再读 Reference 或执行 Script。 |
| [Agent 的概念、原理与构建模式：从零打造一个简化版的 Claude Code](notes/agent-systems/Agent 的概念、原理与构建模式：从零打造一个简化版的 Claude Code.md) | page |  | 0 | Agent 不是一个神秘东西。它的核心就是：**大模型负责判断和生成下一步请求，Agent 主程序负责维护状态、调用工具、把结果再喂回模型，直到得到最终答案。** |
| [Context Engineering：概念与技术实现深度解析](notes/agent-systems/Context Engineering：概念与技术实现深度解析.md) | page |  | 0 | Context Engineering 不是训练模型，也不是单纯写 Prompt，而是在每一次模型调用前，决定哪些信息该保存、该选入、该压缩、该隔离，让模型在有限上下文窗口内看见刚好足够、结构清楚、成本可控的信息。 |
| [从 LLM 到 Agent Skill，一期视频带你打通底层逻辑！](notes/agent-systems/从 LLM 到 Agent Skill，一期视频带你打通底层逻辑！.md) | page |  | 0 | 这期视频的核心价值，是把 AI 应用开发里最容易混成一团的名词按工程调用链排好：LLM 负责预测下一个 Token；Context 是每次请求喂给模型的信息总和；Prompt 是其中的指令部分；Tool 是外部函数；MCP 是工具接入标准； |
| [Temperature & Top-p：掌控大模型的创造力开关](notes/llm-basics/Temperature & Top-p：掌控大模型的创造力开关.md) | page |  | 0 | Temperature 改的是概率分布的形状：低温放大高分 token 优势，高温压平差距；Top-p 改的是候选集合的边界：只保留累计概率达到阈值的头部 token，截断长尾垃圾词。两者都能影响随机性，但不是同一个旋钮。 |
| [Token 到底是什么？揭秘大模型背后的文字压缩术](notes/llm-basics/Token 到底是什么？揭秘大模型背后的文字压缩术.md) | page |  | 0 | Token 不是字，也不是词，而是 Tokenizer 根据词表和合并规则切出来的模型处理单位；Tokenizer 既是翻译器，把文本和数字互转，也是压缩器，把高频相邻片段合成更长 Token，从而减少模型需要处理的序列长度。 |
| [MCP 终极指南：从原理到实战，带你深入掌握 MCP（基础篇）](notes/mcp-cli-browser/MCP 终极指南：从原理到实战，带你深入掌握 MCP（基础篇）.md) | page |  | 0 | MCP 不是魔法，也不是“装个插件就智能了”。它的核心是：Host 启动或连接 Server，Server 暴露结构化工具，Host 把工具说明交给模型，模型决定调用哪个工具，Host 再把调用结果送回模型生成答案。真正要掌握的是这条数据流 |
| [为什么越来越多的人抛弃 MCP，转向 CLI？](notes/mcp-cli-browser/为什么越来越多的人抛弃 MCP，转向 CLI？.md) | page |  | 0 | 视频的核心判断是：CLI 在个人、本地、开发者场景里更省 Token、更快、更灵活；MCP 在企业、云端、需要结构化参数和权限边界的场景里更可控、更安全。更准确的说法不是“抛弃 MCP”，而是别拿 MCP 做 shell 本来就擅长的事情。 |
| [OpenAI Agents SDK Lab 02](notes/openai/2026-05-08-openai-agents-sdk-lab02.md) | page |  | 0 | 日期：2026-05-08 |
| [OpenAI Orchestration and Handoffs Lab 04](notes/openai/2026-05-08-openai-orchestration-handoffs-lab04.md) | page |  | 0 | 日期：2026-05-08 |
| [OpenAI Responses API Lab 01](notes/openai/2026-05-08-openai-responses-api-lab01.md) | page |  | 0 | 日期：2026-05-08 |
| [OpenAI Tools and Retrieval Lab 03](notes/openai/2026-05-08-openai-tools-rag-lab03.md) | page |  | 0 | 日期：2026-05-08 |
| [用 AI 生成可编辑 PPT：Codex + ImageGen + Presentations 最佳实践拆解](notes/openai/2026-05-20-douyin-codex-imagegen-presentations-ppt-sop.md) | page |  | 0 | 视频的核心 SOP 是：不要让图像模型直接生成整套死图 PPT，而是让 Codex 先做内容和任务编排，用 ImageGen/Image2 先选视觉方向、再生产视觉素材，最后交给 Presentations 生成可编辑 PPTX。这个方向对 |
| [实战体验OpenAI全新AI应用开发套件 - Responses API与Agents SDK](notes/openai/实战体验OpenAI全新AI应用开发套件 - Responses API与Agents SDK.md) | page |  | 0 | 这个视频适合作为 OpenAI Agent 技术栈的第一眼入口：**Responses API 是更底层的模型与工具调用接口，Agents SDK 是更上层的编排框架。** 前者解决“模型怎么连工具和状态”，后者解决“Agent、工具、ha |
| [RAG 工作机制详解——一个高质量知识库背后的技术全流程](notes/rag/RAG 工作机制详解——一个高质量知识库背后的技术全流程.md) | page |  | 0 | RAG 的本质不是“把文档塞给模型”，而是先把文档切成可检索的片段并建索引；用户提问时先检索相关片段，再用重排缩小范围，最后把问题和少量高相关片段交给大模型生成答案。 |
| [使用Python构建RAG系统 —— 用代码还原 RAG系统的每个细节](notes/rag/使用Python构建RAG系统 —— 用代码还原 RAG系统的每个细节.md) | page |  | 0 | 这期视频的价值不是“教你装几个库”，而是把 RAG 拆成五个清楚的函数边界：文档先切成 chunk，再把 chunk 变成 embedding 存进向量库；用户提问时先召回候选片段，再用 Cross-Encoder 重排，最后只把少量高相关 |
| [工业级实战：从传统RAG到Agentic RAG的进阶优化！](notes/rag/工业级实战：从传统RAG到Agentic RAG的进阶优化！.md) | page |  | 0 | 这个视频的核心价值是把传统 RAG 的“检索 -> 生成”线性流程，升级成“理解问题 -> 选择信息源 -> 生成答案 -> 评估答案 -> 必要时重试或人工介入”的闭环。但它不是落地指南，尤其缺少评估数据、权限边界、成本控制和可运行代码。 |
| [企业级 Hybrid RAG 与 RAGFlow 的设计取向](notes/ragflow/2026-05-13-enterprise-hybrid-rag-and-ragflow.md) | page |  | 0 | 企业级 hybrid RAG 不是“向量数据库 + 大模型”的聊天 demo，而是： |
| [RAGFlow 官方 Docker 部署记录](notes/ragflow/2026-05-13-ragflow-official-docker-deployment.md) | page |  | 0 | 初始部署日期：2026-05-13（服务器时区：Asia/Shanghai） |
| [RAGFlow 官方评测体系与测试数据集调研](notes/ragflow/2026-05-13-ragflow-official-evaluation-research.md) | page |  | 0 | 日期：2026-05-13 |
| [DeepSeek + RAGFlow 构建个人知识库，2026 本地化部署](notes/ragflow/DeepSeek + RAGFlow 构建个人知识库，2026 本地化部署.md) | page |  | 0 | 这个视频的核心路线是：用 Ollama 在本机跑 DeepSeek 和 embedding 模型，用 Docker Compose 启动 RAGFlow，再在 RAGFlow 里配置 Ollama provider，把个人资料导入知识库做检 |
| [Dify + RAGFlow：1 + 1＞2 的混合架构，详细教程 + 实施案例](notes/ragflow/Dify + RAGFlow：1 + 1＞2 的混合架构，详细教程 + 实施案例.md) | page |  | 0 | 这条视频的价值不是“Dify 和 RAGFlow 谁替代谁”，而是把职责拆干净：Dify 管应用入口、提示词、模型选择、Chatbot/Chatflow/Workflow/Agent 编排；RAGFlow 管知识库解析、分块、检索和可引用上 |
| [Qwen3 + RAGFlow 构建个人知识库](notes/ragflow/Qwen3 + RAGFlow 构建个人知识库.md) | page |  | 0 | 这个视频适合当作“个人知识库快速入门路线图”：用 Docker 起 RAGFlow，用 Ollama 或在线 API 接入 Qwen3，再配置单独的 embedding 模型，把文档上传到知识库后做检索问答。但个人演示不能直接推出企业可落地 |
| [RAGFlow 与企业 RAG 专项学习笔记](notes/ragflow/RAGFlow 与企业 RAG 专项学习笔记.md) | page |  | 0 | RAGFlow 不是 Dify/n8n/Coze 这种通用应用编排工具的同类替代品，它更像企业 RAG 的“上下文引擎”：负责把复杂文档解析成可检索、可调参、可引用、可评估的知识上下文。它的核心优势在 RAG 质量链路，不在炫酷工作流；企业 |
| [RAGFlow 作为外部知识库接入 Dify](notes/ragflow/RAGFlow 作为外部知识库接入 Dify.md) | page |  | 0 | 把 RAGFlow 接进 Dify，不应该理解成“把 RAGFlow 数据导入 Dify”。正确边界是：RAGFlow 继续负责文档解析、分片、索引、召回、重排和引用来源；Dify 只通过外部知识库 API 发起检索请求，把返回的 chun |
| [RAGFlow 命中率最高的 RAG 知识库引擎 本地部署 小白教程](notes/ragflow/RAGFlow 命中率最高的 RAG 知识库引擎 本地部署 小白教程.md) | page |  | 0 | 这是一份 RAGFlow Windows 本地部署入门演示：价值在于把 Docker Desktop、WSL、RAGFlow compose 启动、模型接入这些门槛串起来；标题里的“命中率最高”没有数据集和指标支撑，不能当技术结论，更不能把 |
| [RAGFlow：知识库终极引擎](notes/ragflow/RAGFlow：知识库终极引擎.md) | page |  | 0 | RAGFlow 的价值不在“又一个聊天知识库界面”，而在把企业 RAG 中最容易烂掉的部分前置成产品能力：文档理解、可配置 chunking、引用、异构数据源、召回重排和工作流。但企业真正上线还缺权限治理、批量数据生命周期、评估集、人审和运 |
| [RAGFlow：采用 OCR 和深度文档理解的新一代 RAG 引擎](notes/ragflow/RAGFlow：采用 OCR 和深度文档理解的新一代 RAG 引擎.md) | page |  | 0 | RAGFlow 的核心价值不是“又一个知识库聊天 UI”，而是把 OCR、DeepDoc 文档理解、模板化 chunking、引用溯源、异构数据源和检索工作流放到同一个 RAG engine/context layer 里；但它只能降低幻觉 |
| [RAGflow 知识库 + 参数可调架构 + 本地大模型，让 AI 化身佛学顾问](notes/ragflow/RAGflow 知识库 + 参数可调架构 + 本地大模型，让 AI 化身佛学顾问.md) | page |  | 0 | 这个视频的价值不在“佛学顾问”本身，而在展示一个窄领域 RAG 应用的最小闭环：把领域语料放进知识库，用知识检索约束回答，再通过 API 接到外部应用。别把它吹成通用企业方案。真正要落地，必须补上语料治理、chunk 策略、检索/重排参数、 |
| [RAGFlow 专项](notes/ragflow/README.md) | page |  | 0 | RAGFlow 相关资料集中在这里：视频消化、官方材料校准、部署与评测、Dify 集成、垂直案例和后续实验线索。 |
| [Ragflow 小白教程（详细重制版）](notes/ragflow/Ragflow 小白教程（详细重制版）.md) | page |  | 0 | 这个视频是一个偏实操的 RAGFlow Windows 本地部署和入门教程：它把 Docker Desktop、`.env`、端口、镜像、模型供应商、知识库解析、聊天、搜索和智能体都走了一遍；但视频基于 `v0.20.5`，当前 RAGFl |
| [用 RAGFlow 打造 AI 医疗问诊助手](notes/ragflow/用 RAGFlow 打造 AI 医疗问诊助手.md) | page |  | 0 | 这个视频只能作为“RAGFlow 医疗资料检索助手”的流程观察，不能当真实医疗落地范式。医疗场景里，RAGFlow 最多帮助检索和引用医学资料；诊断、处方、治疗建议、分诊结论必须有医生审核、合规边界、临床验证和责任归属。标题里的“解决90% |
| [零基础教程：RAGFlow 快速创建知识库和智能问答系统](notes/ragflow/零基础教程：RAGFlow 快速创建知识库和智能问答系统.md) | page |  | 0 | 这个视频说明了 RAGFlow 的最短上手路径：先配模型，再建知识库、上传文档、解析切片、测试召回，最后把知识库绑定到聊天助手并开启引用。它对新手有用，但企业落地不能停在“能问答”：权限、数据治理、评估集、引用可追溯、版本差异和 API 兼 |
| [中文 AI Agent 实践落地 YouTube 学习清单](notes/watchlists/2026-05-08-agent-practice-youtube-cn-watchlist.md) | page |  | 0 | 日期：2026-05-08 |
| [中文 AI Agent 技术栈 YouTube 学习清单](notes/watchlists/2026-05-08-agent-youtube-cn-watchlist.md) | page |  | 0 | 日期：2026-05-08 |

## Topics

| Page | Type | Status | Sources | Summary |
| --- | --- | --- | ---: | --- |
| [稳定知识](topics/README.md) | page |  | 0 | `wiki/topics/` 是稳定主题层，放跨来源整理后的 evergreen 文档。 |
| [AI Knowledge](topics/ai/README.md) | page |  | 0 | AI 领域稳定知识入口。 |
| [Anthropic / Claude Agent 技术栈](topics/ai/anthropic-stack.md) | page |  | 0 | 这一阶段放在 OpenAI 官方栈之后。原因很简单：先学透一套官方体系，再做横向比较。否则只是把两个生态的概念搅成一团。 |
| [OpenAI Agent 技术栈](topics/ai/openai-stack.md) | page |  | 0 | ```text |
| [Agentic RAG 从基础到企业级实践](topics/ai/rag/agentic-rag-from-basics-to-enterprise-practice.md) | page |  | 0 | > 校准日期：2026-05-16 |
| [Meta Knowledge](topics/meta/README.md) | page |  | 0 | 知识库结构和方法论层的稳定知识。 |
| [Karpathy 式 LLM 知识库理论原理](topics/meta/karpathy-llm-knowledge-base-principles.md) | page |  | 0 | > 本文只整理理论原理，不包含具体搭建步骤、工具安装教程或执行清单。 |

## Research

| Page | Type | Status | Sources | Summary |
| --- | --- | --- | ---: | --- |
| [问题研究](research/README.md) | page |  | 0 | `wiki/research/` 是问题驱动研究层，放已经超出单篇资料消化、并形成结构化判断的材料。 |
| [HTML Anything 调研报告：本地 Agent 驱动的 HTML 交付编辑器](research/open-source-projects/2026-05-15-html-anything-research.md) | page |  | 0 | 调研日期：2026-05-15 |
| [飞书官方 CLI 调研报告：面向 AI Agent 的企业 SaaS 操作入口](research/open-source-projects/2026-05-19-lark-cli-research.md) | page |  | 0 | 调研日期：2026-05-19 |
| [Open Source Project Research](research/open-source-projects/README.md) | page |  | 0 | 开源项目拆解目录。 |
| [浏览器自动化工具深度调研：Playwright、MCP、CLI 与 Agent 浏览器](research/open-source-projects/browser-automation/2026-05-14-browser-automation-tools-research.md) | page |  | 0 | 调研日期：2026-05-14；更新核对：2026-05-28 16:53 CST |
| [Agent-Native CLI 与真实浏览器工具调研：CLI-Anything、OpenCLI、bb-browser](research/open-source-projects/browser-automation/2026-05-21-agent-native-cli-browser-runtime-research.md) | page |  | 0 | 调研日期：2026-05-21；更新核对：2026-05-28 16:53 CST |
| [CloakBrowser 开源项目调研](research/open-source-projects/browser-automation/2026-05-25-cloakbrowser-research.md) | page |  | 0 | 调研日期：2026-05-25 |
| [Crawl4AI 开源项目调研](research/open-source-projects/browser-automation/2026-05-25-crawl4ai-research.md) | page |  | 0 | 调研日期：2026-05-25 |
| [CloakBrowser 深入落地使用手册](research/open-source-projects/browser-automation/2026-05-26-cloakbrowser-implementation-guide.md) | page |  | 0 | 调研日期：2026-05-26 |
| [CloakBrowser-Manager 开源项目调研](research/open-source-projects/browser-automation/2026-05-28-cloakbrowser-manager-research.md) | page |  | 0 | 调研日期：2026-05-28 |
| [Codex Chrome 插件：安装使用与实践案例汇总](research/open-source-projects/browser-automation/Codex Chrome 插件：安装使用与实践案例汇总.md) | page |  | 0 | Codex Chrome 插件的价值不是“AI 会点网页”，而是把 Codex 的任务规划、代码/文件能力、真实登录态 Chrome、多标签和人工确认机制接到一起，让它能处理一类以前只能靠人跨网页搬运、核对、整理和提交的工作流。 |
| [Browser Automation Research](research/open-source-projects/browser-automation/README.md) | page |  | 0 | 浏览器自动化专题研究入口。这里集中放直接涉及浏览器 runtime、CDP、真实浏览器控制、指纹浏览器、Web extraction browser pipeline 和 profile manager 的材料。 |
| [RAGFlow 官方实践案例的工程证据审计](research/open-source-projects/ragflow/RAGFlow 官方实践案例的工程证据审计.md) | page |  | 0 | - **RAGFlow 官方最强的一条证据线不是“通用企业知识库”，而是金融投研**。原因很直接：官方不仅给了完整的 `RAGFlow in Practice` 实践文，还在后续 release notes 里补上了对应的 `Company |
| [RAGFlow 官方材料 Deep Research](research/open-source-projects/ragflow/RAGFlow 官方材料 Deep Research.md) | page |  | 0 | 下文首次出现时，统一采用 **英文术语（专业中文对应）** 的写法，例如：RAG（检索增强生成）、Agentic RAG（智能体驱动检索增强生成）、Context Engineering（上下文工程）、Ingestion Pipeline（ |
| [RAGFlow Research](research/open-source-projects/ragflow/README.md) | page |  | 0 | RAGFlow 开源项目和官方材料研究入口。这里放源码、官方文档、release notes、实践案例证据等项目级拆解；视频和教程消化放在 [wiki/notes/ragflow](notes/ragflow/)。 |
| [software-technical-proposal Skill 深度评估报告](research/software-technical-proposal Skill 深度评估报告.md) | page |  | 0 | 先给结论：这个 skill 的大方向是对的，但还没有达到“高频、稳定、低风险地生成正式交付级技术方案”的状态。它最正确的地方有四个：第一，强调“先读采购文件和评分办法，再写方案”；第二，把模板定义成“可裁剪骨架”而不是固定目录；第三，明确区 |
| [企业级 RAG 问答质量测试数据集调研报告](research/use-cases/2026-05-15-enterprise-rag-eval-datasets.md) | page |  | 0 | 调研日期：2026-05-15 |
| [AI 应用层经济性与物理 AI Deep Research 提示词](research/use-cases/2026-05-17-ai-application-layer-deep-research-prompt.md) | page |  | 0 | 日期：2026-05-17 |
| [AI 应用层泡沫、成本结构与长期机会调研主题](research/use-cases/2026-05-17-ai-application-layer-economics.md) | page |  | 0 | 这个主题不能沉淀成“AI 应用层完蛋了”这种粗糙判断。更准确的研究命题是： |
| [AI 做 PPT：Codex app + ImageGen + Slides/Presentations 抖音调研报告](research/use-cases/2026-05-20-ai-ppt-codex-imagegen-slides-douyin-research.md) | page |  | 0 | 抖音是这类中文实践内容的更好前哨。 |
| [AI 生成 PPTX 实践 SOP：按 Agent / Skill 选路线](research/use-cases/2026-05-23-ai-pptx-sop-by-agent-skill.md) | page |  | 0 | 好的 PPTX 生成流程不是让模型一次吐成品，而是： |
| [AI 应用层出清、成本结构、商业模式与 Physical AI 研究报告](research/use-cases/AI 应用层出清、成本结构、商业模式与 Physical AI 研究报告.md) | page |  | 0 | 这份报告的核心判断不是“AI 应用不行了”，而是：**第一轮低壁垒、弱闭环、强补贴、弱付费的 AI 应用正在出清；而入口型、工作流型、开发者型、强约束垂直场景，以及一部分端侧与物理世界 AI，仍在建立长期价值。** 公开材料显示，行业主流公 |
| [Use Case Research](research/use-cases/README.md) | page |  | 0 | 真实应用场景调研目录。 |

## Labs

| Page | Type | Status | Sources | Summary |
| --- | --- | --- | ---: | --- |
| [实验验证](labs/README.md) | page |  | 0 | `wiki/labs/` 是验证层，只放能验证具体判断的最小实验。 |
| [Anthropic Labs](labs/anthropic/README.md) | page |  | 0 | 第二阶段再开始这里。不要在 OpenAI 第一阶段没完成前同时推进两个生态。 |
| [Lab 01: Responses API](labs/openai/01-responses-api/README.md) | page |  | 0 | 理解 OpenAI Agent 技术栈的底层原语。 |
| [Lab 02: Agents SDK Basic](labs/openai/02-agents-sdk-basic/README.md) | page |  | 0 | 用 OpenAI Agents SDK 做一个单 Agent，并和 Lab 01 的手写 Responses API 工具循环做对比。 |
| [Lab 03: Tools and Retrieval](labs/openai/03-tools-and-rag/README.md) | page |  | 0 | 让 Agent 接入真实信息源，并明确区分模型记忆、web search 和 file search。 |
| [OpenAI Agent Local Notes](labs/openai/03-tools-and-rag/data/openai-agent-local-notes.md) | page |  | 0 | 工具是 Agent 和外部世界之间的边界。读工具和写工具应该分开。查询订单、 |
| [Lab 04: Orchestration and Handoffs](labs/openai/04-orchestration-handoffs/README.md) | page |  | 0 | 理解什么时候需要多个 Agent，以及 `handoff` 和 `agent-as-tool` 的边界。 |
| [Lab 05: Guardrails, Evals, Tracing](labs/openai/05-guardrails-evals-tracing/README.md) | page |  | 0 | 从能跑变成能判断质量。 |
| [Lab 06: Sandbox Agents](labs/openai/06-sandbox-agents/README.md) | page |  | 0 | 学习让 Agent 在受控环境中处理文件、命令和长任务。 |
| [OpenAI Labs](labs/openai/README.md) | page |  | 0 | OpenAI 第一阶段实验目录。 |

## Outputs

| Page | Type | Status | Sources | Summary |
| --- | --- | --- | ---: | --- |
| [输出成品](outputs/README.md) | page |  | 0 | `wiki/outputs/` 是成品层，放最终交付物，例如 PPT、报告、文章、方案、图片成品和可复查的演示文件。 |

## Archive

| Page | Type | Status | Sources | Summary |
| --- | --- | --- | ---: | --- |
| [历史归档](archive/README.md) | page |  | 0 | `wiki/archive/` 是历史归档层。 |

## Schema

| Page | Type | Status | Sources | Summary |
| --- | --- | --- | ---: | --- |
| [Agent Protocol](../schema/agent-protocol.md) | method | active | 2 | Karpathy 式 LLM Wiki 的操作规约，定义 ingest、query、lint 和 output write-back。 |
| [来源类型与采集状态](../schema/meta/source-types.md) | meta | active | 2 | 固定采集阶段的来源类型、证据等级、状态和单文档落盘规则。 |
| [Source Card Template](../schema/templates/source-card.md) | template |  | 0 | 单文件原始采集文档模板，用于 `raw/sources/`。 |
