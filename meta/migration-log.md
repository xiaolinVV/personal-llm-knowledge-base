---
type: meta
domain: meta
status: active
created: 2026-05-30
updated: 2026-06-01
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

## 2026-06-01：顶层生命周期目录恢复英文路径

### 核心判断

中文编号目录直接可读，但真实路径长期会给 Git、Codex、命令行、Markdown 链接和 GitHub 浏览制造额外摩擦。仓库真实数据结构应该稳定、短、工程友好；中文可读性应该交给 Obsidian 首页、MOC、主题地图和链接文本。

因此恢复原始英文顶层生命周期目录，不保留中文目录镜像，也不创建中文 symlink，避免两套路由同时存在。

### 已重命名目录

| 原目录 | 新目录 | 理由 |
| --- | --- | --- |
| `00-收件箱/` | `inbox/` | 恢复原始生命周期入口路径。 |
| `10-来源索引/` | `sources/` | 恢复来源索引路径。 |
| `20-资料笔记/` | `notes/` | 恢复资料消化层路径。 |
| `30-稳定知识/` | `knowledge/` | 恢复稳定知识层路径。 |
| `40-问题研究/` | `research/` | 恢复问题研究层路径。 |
| `50-实验验证/` | `labs/` | 恢复实验验证层路径。 |
| `60-方法库/` | `methods/` | 恢复方法库路径。 |
| `70-输出成品/` | `outputs/` | 恢复输出成品路径。 |
| `80-仓库治理/` | `meta/` | 恢复仓库治理路径。 |
| `90-历史归档/` | `archive/` | 恢复历史归档路径。 |

### Obsidian 补偿层

- 新增 `00-首页.md` 作为中文首页。
- 新增 `meta/obsidian/` 存放生命周期 MOC、主题 MOC、复盘 MOC 和 Base 视图。
- README、AGENTS、Skill 和模板全部改回英文真实路径。
- `docs/` 继续只做旧入口兼容，不重新承载知识。
