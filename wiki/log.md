---
type: log
domain: meta
status: active
created: 2026-06-02
updated: 2026-06-02
source_refs:
  - ../README.md
  - ../schema/meta/migration-log.md
---

# Wiki Log

这是 Karpathy 式 LLM Wiki 的 append-only 时间线。每条记录使用固定格式：

```text
## [YYYY-MM-DD] action | title
```

## [2026-06-02] migration | 全量迁移为 raw/wiki/schema 模式

- 旧结构：`inbox/`、`sources/`、`notes/`、`knowledge/`、`research/`、`labs/`、`methods/`、`outputs/`、`meta/`、`archive/`、`docs/`。
- 新结构：`raw/`、`wiki/`、`schema/`。
- 迁移动作：证据层进入 `raw/`，LLM 编译层进入 `wiki/`，规约层进入 `schema/`。
- 特殊处理：`notes/ragflow/official-practice-cases/` 迁入 `raw/sources/ai/ragflow/official-practice-cases/`，因为这些文件是网页快照、图片、HTML、metadata、dataset 和文章镜像，不是资料消化笔记。
- 删除：`docs/README.md` 旧兼容入口。
- 保留：根目录 `AGENTS.md` 和 `.codex/skills/`，因为它们是 Codex 入口和可执行 Skill 配置。

未验证事项：

- 本次只验证路径结构、Git rename、忽略规则和本地 Markdown 链接。
- 没有重新核验每篇笔记中的事实、API、日期、模型行为或外部来源。
