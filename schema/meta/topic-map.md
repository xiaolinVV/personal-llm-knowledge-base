---
type: meta
domain: meta
status: active
created: 2026-05-30
updated: 2026-06-01
source_refs:
  - README.md
---

# 主题地图

本仓库顶层按 Karpathy 三层结构组织：`raw/`、`wiki/`、`schema/`。主题只负责索引和导航。

如果生命周期和主题冲突，生命周期优先。比如一篇 AI 视频笔记应该先进 `wiki/notes/ai-topic/`，不是因为主题是 AI 就直接放 `wiki/topics/ai/`。

## 一级主题

| 主题 | 范围 | 当前入口 |
| --- | --- | --- |
| `ai` | LLM、Agent、RAG、MCP、模型生态、AI 工程、AI 产品和行业案例 | `raw/sources/ai/`, `wiki/notes/`, `wiki/topics/ai/`, `wiki/research/`, `wiki/labs/openai/`, `wiki/labs/anthropic/` |
| `software-engineering` | 编程语言、架构、测试、工程效率、CLI、浏览器自动化、系统设计 | 暂未拆独立目录，先按生命周期进入对应目录 |
| `product-business` | 产品判断、商业模式、ToB 交付、行业研究、成本结构 | `wiki/research/use-cases/` |
| `learning-research` | 学习方法、研究方法、资料处理、写作、复盘 | `schema/methods/`, `schema/meta/`, `wiki/topics/meta/` |
| `life` | 生活管理、个人系统、日常决策 | 暂未拆独立目录 |
| `reading` | 读书笔记、书单、摘录和长期主题整理 | 暂未拆独立目录 |
| `finance` | 投资、财务、经济资料和个人财务研究 | 暂未拆独立目录 |
| `health` | 健康、运动、医疗资料和个人健康管理 | 暂未拆独立目录 |
| `misc` | 暂时无法归类但仍值得处理的材料 | 先进入 `raw/inbox/`，定期清理 |

## AI 子主题

| 子主题 | 当前入口 |
| --- | --- |
| OpenAI 官方栈 | `raw/sources/ai/official-resources.md`, `wiki/topics/ai/openai-stack.md`, `wiki/notes/openai/`, `wiki/labs/openai/` |
| Anthropic / Claude 栈 | `wiki/topics/ai/anthropic-stack.md`, `wiki/labs/anthropic/` |
| Agent Systems | `wiki/notes/agent-systems/`, `wiki/research/open-source-projects/` |
| RAG / Agentic RAG | `wiki/notes/rag/`, `wiki/notes/ragflow/`, `wiki/topics/ai/rag/` |
| MCP / CLI / Browser | `wiki/notes/mcp-cli-browser/`, `wiki/research/open-source-projects/browser-automation/` |
| AI 应用场景和商业边界 | `wiki/research/use-cases/` |

## Obsidian 入口

| 入口 | 用途 |
| --- | --- |
| [首页](../../00-首页.md) | 中文总入口，适合打开 vault 后先看。 |
| [生命周期 MOC](../obsidian/lifecycle-moc.md) | 按资料流转阶段浏览。 |
| [主题 MOC](../obsidian/topic-moc.md) | 按主题浏览，不替代生命周期归档。 |
| [复盘 MOC](../obsidian/review-moc.md) | 周/月复盘入口。 |
| [Knowledge Base](../obsidian/knowledge.base) | 用 Obsidian Bases 按属性查看内容。 |

## 维护规则

- 新主题不要直接建一级目录。先放进生命周期目录，再在本文件登记。
- 一个主题至少有 3 份以上有效材料，或者已经成为长期输出方向，才考虑拆子目录。
- 如果某个主题长期没有输出或复查，保留索引即可，不继续扩目录。
- `misc` 不是永久分类。超过一个月仍停在 `misc` 的内容，要么归类，要么归档，要么删除。
