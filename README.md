# personal-llm-knowledge-base

这个仓库是一个 Karpathy 式 LLM Wiki。目标不是收藏资料，而是让 LLM 把原始资料持续编译成可读、可复查、可维护、可输出的 Markdown 知识系统。

核心判断很简单：

- 来源不是知识。URL、网页、PDF、视频和截图只是证据入口。
- Wiki 才是长期记忆。LLM 负责把来源读完、压缩、重写、交叉链接、更新旧判断。
- Schema 是约束。没有明确协议，LLM 只会把文件越写越乱。
- 不上来做复杂 RAG、向量库或知识图谱。第一版只用 Git + Markdown + Obsidian + 明确维护规则。
- 未验证就不要声称完成。没有查来源、没有跑实验、没有复核，就写“未验证”。

## 三层结构

```text
raw/
  -> wiki/
    -> schema/
```

每一层只做一件事：

- `raw/`：证据层。放待处理线索、来源卡片、网页快照、本地素材和准不可变原始材料。
- `wiki/`：编译层。放 LLM 维护的资料笔记、稳定主题、研究、实验、输出、全局索引和日志。
- `schema/`：规约层。放模板、Obsidian 视图、方法、迁移记录、主题地图和 agent protocol。

标准流转路径：

```text
raw/inbox/
  -> raw/sources/
    -> wiki/notes/
      -> wiki/topics/ 或 wiki/research/
        -> wiki/labs/
          -> wiki/outputs/
            -> wiki/topics/ 和 schema/methods/
```

## 顶层结构

```text
.
├── 00-首页.md
├── AGENTS.md
├── README.md
├── raw/
│   ├── inbox/
│   └── sources/
├── wiki/
│   ├── index.md
│   ├── log.md
│   ├── notes/
│   ├── topics/
│   ├── research/
│   ├── labs/
│   ├── outputs/
│   └── archive/
├── schema/
│   ├── agent-protocol.md
│   ├── templates/
│   ├── methods/
│   ├── meta/
│   └── obsidian/
└── .codex/
```

旧的 `inbox/`、`sources/`、`notes/`、`knowledge/`、`research/`、`labs/`、`methods/`、`outputs/`、`meta/`、`archive/`、`docs/` 顶层目录已经全量迁移并删除。迁移原因和映射见 [迁移记录](schema/meta/migration-log.md)。

## 快速入口

- [Obsidian 首页](00-首页.md)
- [Wiki Index](wiki/index.md)
- [Wiki Log](wiki/log.md)
- [Agent Protocol](schema/agent-protocol.md)
- [主题地图](schema/meta/topic-map.md)
- [Obsidian 使用说明](schema/obsidian/README.md)
- [Knowledge Base](schema/obsidian/knowledge.base)
- [AI 官方资料索引](raw/sources/ai/official-resources.md)
- [OpenAI Agent 技术栈](wiki/topics/ai/openai-stack.md)
- [Anthropic / Claude Agent 技术栈](wiki/topics/ai/anthropic-stack.md)
- [Agentic RAG 专题](wiki/topics/ai/rag/agentic-rag-from-basics-to-enterprise-practice.md)
- [资料笔记](wiki/notes/README.md)
- [研究报告](wiki/research/README.md)
- [实验验证](wiki/labs/README.md)
- [方法库](schema/methods/README.md)
- [输出成品](wiki/outputs/README.md)

## 操作规则

新增材料时先判断它处在哪一层，不要先想主题目录：

| 问题 | 应放位置 |
| --- | --- |
| 只是一个待处理线索？ | `raw/inbox/` |
| 只是来源和证据入口？ | `raw/sources/` |
| 已经读过并转成自己的理解？ | `wiki/notes/` |
| 跨来源、稳定、可复用？ | `wiki/topics/` |
| 围绕一个问题形成判断？ | `wiki/research/` |
| 需要跑代码验证判断？ | `wiki/labs/` |
| 已经产出报告、PPT、文章或方案？ | `wiki/outputs/` |
| 是可重复使用的方法？ | `schema/methods/` |
| 是仓库规则、主题地图或迁移记录？ | `schema/meta/` |

所有 ingest、query、lint 和 output write-back 都必须遵循 [Agent Protocol](schema/agent-protocol.md)，并更新 [Wiki Index](wiki/index.md) 和 [Wiki Log](wiki/log.md)。

## Obsidian 使用

Obsidian 是这个知识库的可视化前端，不是另一套目录规则。

- 打开 vault 后先看 [00-首页.md](00-首页.md)。
- 浏览结构用 [生命周期 MOC](schema/obsidian/lifecycle-moc.md)。
- 按主题找材料用 [主题 MOC](schema/obsidian/topic-moc.md)。
- 做周/月复盘用 [复盘 MOC](schema/obsidian/review-moc.md)。
- 需要筛选属性时用 [Knowledge Base](schema/obsidian/knowledge.base)。

## Codex Skills

- [knowledge-base-workflow](.codex/skills/knowledge-base-workflow/SKILL.md)：处理资料入库、分类、消化、升级、研究、输出回写时使用。
- [video-study-notes](.codex/skills/video-study-notes/SKILL.md)：处理学习视频、字幕、评论、关键帧和视频笔记时使用。

Obsidian 文件浏览器通常不会显示 `.codex/` 这种点号目录。为了可见性，仓库提供 [schema/skills/](schema/skills/README.md) 作为 `.codex/skills/` 的 symlink 入口；这不是副本，改动会落到真实 Skill 文件。

## 轻量来源策略

Git 主要保存 Markdown、来源卡片、少量关键附件、最终可复查成品和最小实验。

大视频、批量截图、完整网页资产、ASR 中间产物和临时渲染文件默认放 `raw/assets/local-media/`、旧兼容 `local-media/` 或外部路径；这些路径由 `.gitignore` 忽略。

## 内容质量线

每份长期内容至少要说明：

- 这是什么类型的内容；
- 属于哪个领域；
- 当前状态是什么；
- 来源是什么；
- 哪些结论已经验证；
- 哪些事项仍未验证。

新 Markdown 文件使用 `schema/templates/` 下的模板。旧文件不强制一次性补元数据，避免为了“整理”制造低价值 churn；在复查、迁移或升级时再补。
