# AGENTS.md

本仓库是个人 Karpathy 式 LLM Wiki。根目录保留本文件作为 Codex 入口；完整维护规约见 [schema/agent-protocol.md](schema/agent-protocol.md)。

## 默认语言

对话、学习笔记、研究记录和仓库说明默认使用中文。代码、命令、API 字段、英文原始标题和提交信息可以使用英文。

## 三层结构

- `raw/`: 证据层。放待处理线索、来源卡片、网页快照、本地素材和准不可变原始材料。
- `wiki/`: 编译层。放 LLM 维护的资料笔记、稳定主题、研究、实验、输出、全局索引和日志。
- `schema/`: 规约层。放模板、Obsidian 视图、方法、迁移记录、主题地图和 agent protocol。

旧的生命周期顶层目录已经删除，不要再创建 `inbox/`、`sources/`、`notes/`、`knowledge/`、`research/`、`labs/`、`methods/`、`outputs/`、`meta/`、`archive/` 或 `docs/`。

## 核心原则

- 先判断层级，再判断主题。来源进 `raw/`，编译后的长期内容进 `wiki/`，规则和模板进 `schema/`。
- 官方资料优先。涉及 API、SDK、模型、产品行为、标准和工具能力时，优先核对官方文档。
- 不要把来源当知识。URL、PDF、网页、视频和截图只是证据入口；必须经过理解、压缩、质疑和重写后才算知识。
- 不要把 LLM 总结当事实。关键结论必须保留来源，必要时回到原文、代码或实验核验。
- 不要上来做复杂自动化。第一版坚持 Git + Markdown + Obsidian + 明确维护规则。
- 未验证就不要声称完成。未跑实验、未查官方文档、未复核来源时，明确写“未验证”。
- 高风险动作必须有人审：发邮件、改数据库、调用支付、部署、改线上配置、执行不受控 shell、写出仓库外文件。

## 固定入口

- `wiki/index.md`: 内容索引。回答问题或维护 wiki 前先读。
- `wiki/log.md`: 时间线日志。ingest、query、lint、migration、output write-back 都要追加。
- `schema/agent-protocol.md`: 维护协议。所有资料入库、查询、lint 和输出回写都按这里执行。
- `schema/templates/`: 新 Markdown 文件模板。
- `schema/meta/topic-map.md`: 主题地图。

## Skill 约定

`.codex/skills/` 保留为可执行 Skill 配置，不迁入 `schema/`。
Obsidian 文件浏览器隐藏点号目录；可通过 `schema/skills/` 这个 symlink 入口查看同一批 Skill 文件。

- 处理任意资料入库、分类、消化、升级、研究、输出回写时，优先使用项目内 `knowledge-base-workflow`。
- 处理学习视频沉淀时，同时使用项目内 `video-study-notes`，并按三层结构判断产物落点：原始资产进 `raw/assets/local-media/` 或外部路径，资料消化进 `wiki/notes/`，稳定主题才升级到 `wiki/topics/`。
