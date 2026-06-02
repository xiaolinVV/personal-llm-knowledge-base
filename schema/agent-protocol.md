---
type: method
domain: meta
status: active
created: 2026-06-02
updated: 2026-06-02
source_refs:
  - ../README.md
  - ../wiki/topics/meta/karpathy-llm-knowledge-base-principles.md
---

# Agent Protocol

本文件是这个 Karpathy 式 LLM Wiki 的操作规约。根目录 `AGENTS.md` 只保留入口规则；具体 ingest、query、lint 和 output write-back 都按这里执行。

## 三个前提

1. 来源不是知识。`raw/` 只保存证据入口和原始材料。
2. Wiki 是编译产物。`wiki/` 由 LLM 维护，必须持续更新、交叉链接、标注冲突和未验证事项。
3. Schema 是约束。`schema/` 保存模板、方法、主题地图、Obsidian 视图和本协议。

## 固定入口

- `wiki/index.md`: 回答问题、入库或维护前先读，用它定位相关页面。
- `wiki/log.md`: append-only 时间线，记录 migration、ingest、query、lint、output write-back。
- `schema/meta/topic-map.md`: 判断主题边界。
- `schema/templates/`: 新 Markdown 文件模板。

## Ingest

新资料入库时按这个顺序做：

1. 判断材料是否只是线索、来源、已理解内容、研究问题、实验验证、输出成品或方法规则。
2. 原始线索放 `raw/inbox/`；来源卡片、网页快照、本地素材和准不可变原始材料放 `raw/sources/<domain>/`。
3. 已读懂的资料写入 `wiki/notes/<domain-or-topic>/`，必须用自己的中文重写，不贴长篇原文。
4. 跨来源稳定判断写入 `wiki/topics/<domain>/`；问题驱动判断写入 `wiki/research/`；可运行验证写入 `wiki/labs/`。
5. 每次 ingest 后更新 `wiki/index.md`，并向 `wiki/log.md` 追加 `## [YYYY-MM-DD] ingest | title`。

## Query

回答知识库问题时按这个顺序做：

1. 先读 `wiki/index.md`，再检索相关 `wiki/` 页面。
2. 涉及事实、API、SDK、模型行为、价格、法规或时效信息时，回到 `raw/sources/` 或当前官方来源核验。
3. 回答中区分“已由来源支持”“由 wiki 推断”“未验证”。
4. 有长期价值的问答沉淀为 `wiki/research/` 或 `wiki/topics/`，再更新 `wiki/index.md` 和 `wiki/log.md`。

## Lint

周期性维护时检查：

- 旧路径、断链和不存在的本地引用；
- 孤儿页面和缺少入口的主题；
- 同一主题的重复页面；
- 新来源推翻旧判断但旧页面未更新；
- 没有 `source_refs` 或来源不足的关键结论；
- 长期停留在 `raw/inbox/` 的材料。

Lint 结果追加到 `wiki/log.md`；需要持续追踪的问题写入 `wiki/research/` 或对应 `wiki/topics/` 页面。

## Output Write-Back

输出报告、PPT、文章或方案后，不把输出当终点：

- 最终产物放 `wiki/outputs/`，并创建 manifest。
- 新稳定判断回写 `wiki/topics/`。
- 新问题回写 `wiki/research/`。
- 可复用流程回写 `schema/methods/`。
- 新来源回写 `raw/sources/`。

## 路径规则

- 不再创建旧顶层目录：`inbox/`、`sources/`、`notes/`、`knowledge/`、`research/`、`labs/`、`methods/`、`outputs/`、`meta/`、`archive/`、`docs/`。
- `.codex/skills/` 是可执行 Skill 配置，保留在根目录。
- `schema/skills/` 是 Obsidian 可见的 symlink 入口，指向 `.codex/skills/`；它不是第二份副本。
- 大视频、ASR 中间物、批量截图和临时渲染文件放 `raw/assets/local-media/`、旧兼容 `local-media/` 或外部路径，不进 Git。
