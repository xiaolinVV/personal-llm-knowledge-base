---
type: meta
domain: meta
status: active
created: 2026-05-30
updated: 2026-05-30
source_refs:
  - README.md
  - knowledge/meta/karpathy-llm-knowledge-base-principles.md
---

# 迁移记录

## 2026-05-30：从 AI Agent Fieldbook 扩展为个人 LLM 知识库

### 核心判断

旧结构把仓库锁在 AI Agent 主线上，`docs/` 又混合了路线、官方资源和稳定知识。问题不是文件名难看，而是数据结构不清楚：来源、笔记、知识、研究、实验和输出混在一起，后续一定会腐烂。

新结构按生命周期组织：

```text
inbox -> sources -> notes -> knowledge/research -> labs -> outputs -> knowledge/methods
```

### 已移动文件

| 原路径 | 新路径 | 理由 |
| --- | --- | --- |
| `docs/00-learning-principles.md` | `meta/principles.md` | 仓库原则属于治理层，不是普通文档。 |
| `docs/01-roadmap.md` | `meta/roadmap.md` | 路线规划属于治理层。 |
| `docs/02-official-resources.md` | `sources/ai/official-resources.md` | 官方资料清单是来源索引，不是稳定知识。 |
| `docs/03-openai-stack.md` | `knowledge/ai/openai-stack.md` | OpenAI 技术栈是稳定 AI 知识入口。 |
| `docs/04-anthropic-stack.md` | `knowledge/ai/anthropic-stack.md` | Anthropic / Claude 技术栈是稳定 AI 知识入口。 |
| `docs/05-field-research-plan.md` | `meta/ai-field-research-plan.md` | 这是 AI 阶段调研计划，属于路线治理，不是新增内容入口。 |
| `docs/06-agentic-rag-from-basics-to-enterprise-practice.md` | `knowledge/ai/rag/agentic-rag-from-basics-to-enterprise-practice.md` | Agentic RAG 已经是跨资料整理后的稳定专题。 |
| `research/karpathy-llm-knowledge-base-principles.md` | `knowledge/meta/karpathy-llm-knowledge-base-principles.md` | 这是知识库结构原则，不是普通 research。 |

### 已保留目录

| 目录 | 处理方式 | 理由 |
| --- | --- | --- |
| `notes/` | 保留并更新 README | 本来就是资料消化层。 |
| `research/` | 保留并更新 README | 本来就是结构化研究层。 |
| `labs/` | 保留并补根 README | 本来就是验证层。 |
| `outputs/` | 保留并补 README | 本来就是成品层，但需要 manifest 规则。 |
| `.codex/skills/` | 保留 | 这是可执行 Skill 配置，不和 `methods/` 混用。 |
| `docs/` | 只保留兼容 README | 不再承载新内容，避免继续混层。 |

### 已新增目录

| 目录 | 用途 |
| --- | --- |
| `inbox/` | 临时入口。 |
| `sources/` | 轻量来源索引。 |
| `knowledge/` | 稳定知识层。 |
| `methods/` | 方法库和模板。 |
| `meta/` | 仓库治理层。 |
| `archive/` | 历史归档层。 |

### 不做的事

- 不批量重写旧笔记元数据。旧文件在复查或升级时再补。
- 不把历史输出里的旧标题全部改掉。输出是历史成品，不应该为了当前结构制造无意义改动。
- 不引入 RAG、向量库、知识图谱或自动抓取。先把文件边界立住。
