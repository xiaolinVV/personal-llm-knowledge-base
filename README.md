# personal-llm-knowledge-base

这个仓库是一个个人 Karpathy 式 LLM Knowledge Base，用来把资料、想法、研究、实验和输出沉淀成长期可维护的 Markdown 知识系统。

它不是 AI Agent 专项仓库，不是资料收藏夹，也不是纯代码实验室。AI Agent 仍然是核心主题之一，但它现在属于更大的 `ai` 领域。新的主线是：**用 LLM 把原始资料编译成可读、可改、可复用、可持续维护的知识文件，再通过输出反哺知识结构。**

核心判断很简单：

- 知识库的价值不在于保存多少资料，而在于资料能不能被转化、复查、组合和输出。
- 目录结构就是数据结构。原始资料、资料笔记、稳定知识、研究报告、实验代码和输出成品不能混在一层。
- 第一版只使用 Git + Markdown + 清晰目录 + 模板 + 维护规则。不上来做向量库、RAG、知识图谱或复杂自动化。
- 未验证的内容必须标注为未验证；LLM 总结不能冒充事实。

## 生命周期模型

标准流转路径：

```text
inbox/
  -> sources/
    -> notes/
      -> knowledge/ 或 research/
        -> labs/
          -> outputs/
            -> knowledge/ 和 methods/
```

每一层只做一件事：

- `inbox/`：临时入口。只放尚未处理的资料卡片、想法和待归档线索，不能长期堆积。
- `sources/`：轻量来源索引。保存 URL、书籍、论文、视频、PDF、网页快照说明、外部路径和采集日期。大媒体和中间资产默认不进 Git。
- `notes/`：资料消化层。视频、文章、书、课程、会议和聊天记录先变成自己的中文笔记。
- `knowledge/`：稳定知识层。只放跨来源整理后的 evergreen 文档，要求可维护、可复用、可被未来输出调用。
- `research/`：问题驱动研究。只有超出单篇资料消化、形成结构化判断的内容才进入这里。
- `labs/`：验证层。只验证具体工程判断、API、SDK、工具链或失败模式，不为了看起来高级而写实验。
- `methods/`：方法库。放模板、提示词、资料处理流程、复盘流程、维护规则和可复用工作法。
- `outputs/`：成品层。放最终 PPT、报告、文章、方案等；每个新输出目录需要有 manifest 说明来源、目标和生成过程。
- `meta/`：仓库治理层。放定位、主题地图、迁移记录、命名规则、质量标准和维护节奏。
- `archive/`：历史归档层。只放不再维护但仍值得保留的旧结构、旧计划或废弃材料索引。

## 顶层结构

```text
.
├── inbox/
├── sources/
│   └── ai/
├── notes/
│   ├── agent-systems/
│   ├── llm-basics/
│   ├── mcp-cli-browser/
│   ├── openai/
│   ├── rag/
│   ├── ragflow/
│   └── watchlists/
├── knowledge/
│   ├── ai/
│   └── meta/
├── research/
│   ├── open-source-projects/
│   └── use-cases/
├── labs/
│   ├── anthropic/
│   └── openai/
├── methods/
│   └── templates/
├── outputs/
├── meta/
├── archive/
└── docs/
```

`docs/` 是旧入口兼容目录，不再新增内容。稳定文档已经迁移到 `meta/`、`sources/` 和 `knowledge/`。

## 快速入口

- [仓库原则](meta/principles.md)
- [主题地图](meta/topic-map.md)
- [迁移记录](meta/migration-log.md)
- [Karpathy 式 LLM 知识库原则](knowledge/meta/karpathy-llm-knowledge-base-principles.md)
- [AI 官方资料索引](sources/ai/official-resources.md)
- [OpenAI Agent 技术栈](knowledge/ai/openai-stack.md)
- [Anthropic / Claude Agent 技术栈](knowledge/ai/anthropic-stack.md)
- [Agentic RAG 专题](knowledge/ai/rag/agentic-rag-from-basics-to-enterprise-practice.md)
- [资料笔记](notes/README.md)
- [研究报告](research/README.md)
- [实验验证](labs/README.md)
- [方法模板](methods/README.md)
- [输出成品](outputs/README.md)

## Codex Skills

- [knowledge-base-workflow](.codex/skills/knowledge-base-workflow/SKILL.md)：处理资料入库、分类、消化、升级、研究、输出回写时使用。
- [video-study-notes](.codex/skills/video-study-notes/SKILL.md)：处理学习视频、字幕、评论、关键帧和视频笔记时使用。

## 归档判断

新增材料时先判断生命周期，不要先想主题目录：

| 问题 | 应放位置 |
| --- | --- |
| 只是一个待处理线索？ | `inbox/` |
| 只是来源和证据入口？ | `sources/` |
| 已经读过并转成自己的理解？ | `notes/` |
| 跨来源、稳定、可复用？ | `knowledge/` |
| 围绕一个问题形成判断？ | `research/` |
| 需要跑代码验证判断？ | `labs/` |
| 已经产出报告、PPT、文章或方案？ | `outputs/` |
| 是可重复使用的方法？ | `methods/` |
| 是仓库规则、主题地图或迁移记录？ | `meta/` |

如果一个文件看起来能放两个地方，优先按生命周期判断。主题只负责索引，不负责替代生命周期。

## 轻量来源策略

Git 主要保存：

- Markdown 知识文件；
- 来源卡片和索引；
- 少量关键附件；
- 最终可复查成品；
- 可运行的最小实验。

Git 默认不保存：

- 大视频；
- 批量截图；
- 完整网页资产；
- ASR 中间产物；
- 临时渲染文件；
- 无 manifest 的生成中间件。

本地大资产继续放 `local-media/` 或外部路径；`.gitignore` 已经忽略 `local-media/`。

## 内容质量线

每份长期内容至少要说明：

- 这是什么类型的内容；
- 属于哪个领域；
- 当前状态是什么；
- 来源是什么；
- 哪些结论已经验证；
- 哪些事项仍未验证。

新 Markdown 文件使用 `methods/templates/` 下的模板。旧文件不强制一次性补元数据，避免为了“整理”制造垃圾改动；在复查、迁移或升级时再补。
