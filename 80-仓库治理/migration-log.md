---
type: meta
domain: meta
status: active
created: 2026-05-30
updated: 2026-05-30
source_refs:
  - README.md
  - 30-稳定知识/meta/karpathy-llm-knowledge-base-principles.md
---

# 迁移记录

## 2026-05-30：从 AI Agent Fieldbook 扩展为个人 LLM 知识库

### 核心判断

旧结构把仓库锁在 AI Agent 主线上，`docs/` 又混合了路线、官方资源和稳定知识。问题不是文件名难看，而是数据结构不清楚：来源、笔记、知识、研究、实验和输出混在一起，后续一定会腐烂。

新结构按生命周期组织：

```text
00-收件箱 -> 10-来源索引 -> 20-资料笔记 -> 30-稳定知识/40-问题研究 -> 50-实验验证 -> 70-输出成品 -> 30-稳定知识/60-方法库
```

### 已移动文件

| 原路径 | 新路径 | 理由 |
| --- | --- | --- |
| `docs/00-learning-principles.md` | `80-仓库治理/principles.md` | 仓库原则属于治理层，不是普通文档。 |
| `docs/01-roadmap.md` | `80-仓库治理/roadmap.md` | 路线规划属于治理层。 |
| `docs/02-official-resources.md` | `10-来源索引/ai/official-resources.md` | 官方资料清单是来源索引，不是稳定知识。 |
| `docs/03-openai-stack.md` | `30-稳定知识/ai/openai-stack.md` | OpenAI 技术栈是稳定 AI 知识入口。 |
| `docs/04-anthropic-stack.md` | `30-稳定知识/ai/anthropic-stack.md` | Anthropic / Claude 技术栈是稳定 AI 知识入口。 |
| `docs/05-field-research-plan.md` | `80-仓库治理/ai-field-research-plan.md` | 这是 AI 阶段调研计划，属于路线治理，不是新增内容入口。 |
| `docs/06-agentic-rag-from-basics-to-enterprise-practice.md` | `30-稳定知识/ai/rag/agentic-rag-from-basics-to-enterprise-practice.md` | Agentic RAG 已经是跨资料整理后的稳定专题。 |
| `40-问题研究/karpathy-llm-knowledge-base-principles.md` | `30-稳定知识/meta/karpathy-llm-knowledge-base-principles.md` | 这是知识库结构原则，不是普通 research。 |

### 已保留目录

| 目录 | 处理方式 | 理由 |
| --- | --- | --- |
| `20-资料笔记/` | 保留并更新 README | 本来就是资料消化层。 |
| `40-问题研究/` | 保留并更新 README | 本来就是结构化研究层。 |
| `50-实验验证/` | 保留并补根 README | 本来就是验证层。 |
| `70-输出成品/` | 保留并补 README | 本来就是成品层，但需要 manifest 规则。 |
| `.codex/skills/` | 保留 | 这是可执行 Skill 配置，不和 `60-方法库/` 混用。 |
| `docs/` | 只保留兼容 README | 不再承载新内容，避免继续混层。 |

### 已新增目录

| 目录 | 用途 |
| --- | --- |
| `00-收件箱/` | 临时入口。 |
| `10-来源索引/` | 轻量来源索引。 |
| `30-稳定知识/` | 稳定知识层。 |
| `60-方法库/` | 方法库和模板。 |
| `80-仓库治理/` | 仓库治理层。 |
| `90-历史归档/` | 历史归档层。 |

## 2026-05-30：顶层生命周期目录中文化

### 核心判断

Obsidian 是主要可视化前端之一，顶层目录必须让人一眼看懂。英文生命周期目录对命令行友好，但对日常浏览不够直观；因此改成中文编号目录。编号负责稳定排序，中文负责语义清晰。

### 已重命名目录

| 原目录 | 新目录 | 理由 |
| --- | --- | --- |
| `inbox/` | `00-收件箱/` | 临时入口，编号最前。 |
| `sources/` | `10-来源索引/` | 只保存证据入口，不冒充知识。 |
| `notes/` | `20-资料笔记/` | 保存资料消化后的中文笔记。 |
| `knowledge/` | `30-稳定知识/` | 保存跨来源、可复用的长期知识。 |
| `research/` | `40-问题研究/` | 保存问题驱动的结构化判断。 |
| `labs/` | `50-实验验证/` | 保存验证具体判断的最小实验。 |
| `methods/` | `60-方法库/` | 保存模板、流程、提示词和复盘方法。 |
| `outputs/` | `70-输出成品/` | 保存 PPT、报告、文章、方案等最终成品。 |
| `meta/` | `80-仓库治理/` | 保存定位、主题地图、迁移记录和维护规则。 |
| `archive/` | `90-历史归档/` | 保存不再维护但仍值得保留的材料。 |

### 保留不改

- `docs/` 保留英文名，只作为旧入口兼容目录，不承载新知识。
- `.codex/skills/`、`.venv/`、`local-media/` 等技术目录不改名。
- `ai/`、`openai/`、`rag/`、`agent-systems/` 等子主题目录暂不中文化，避免制造无意义链接 churn。

### 不做的事

- 不批量重写旧笔记元数据。旧文件在复查或升级时再补。
- 不把历史输出里的旧标题全部改掉。输出是历史成品，不应该为了当前结构制造无意义改动。
- 不引入 RAG、向量库、知识图谱或自动抓取。先把文件边界立住。
