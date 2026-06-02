---
type: meta
domain: meta
status: active
created: 2026-06-02
updated: 2026-06-02
source_refs:
  - ../../schema/agent-protocol.md
  - ../../schema/templates/source-card.md
---

# 来源类型与采集状态

本文件固定前期采集阶段的分类字段。先判断生命周期，再判断主题；先区分来源性质，再处理文件格式。

## 默认单文档采集

值得保存但尚未消化的资料，默认保存为一份 Markdown 原始采集文档：

```text
raw/sources/<domain>/<source-type>/<YYYY-MM-DD-title-slug>.md
raw/sources/<domain>/<source-type>/<YYYY-MM-DD-title-slug>.assets/
  cover.<ext>
  images/
    001.<ext>
    002.<ext>
```

Markdown 文档同时保存来源元数据、原始内容、采集日志和未验证事项。它属于 `raw/` 证据层，不是 `wiki/` 知识。

默认不要创建 `source.md`、`snapshot.md`、`metadata.json`、`capture-log.md`。只有复杂机器处理场景才允许额外保留 JSON 或 manifest，例如视频 `asset-manifest.md`。

## source_type

| source_type | 含义 | 默认动作 | 默认落点 |
| --- | --- | --- | --- |
| `wechat_article` | 微信公众号文章 | 抽元数据、HTML、封面图、正文图片，转换为一份 Markdown 原文文档 | `raw/sources/<domain>/wechat_article/` |
| `web_article` | 普通网页文章 | 抓正文、封面图、正文图片，转换为一份 Markdown 原文文档 | `raw/sources/<domain>/web_article/` |
| `official_doc` | 官方文档、API/SDK 文档、标准 | 抓正文或记录官方入口；涉及时效事实时标记需复核 | `raw/sources/<domain>/official_doc/` |
| `video` | 视频、课程、直播回放 | 抓元数据、字幕/ASR、章节、关键帧、评论摘要、资产清单；来源侧只生成一份 Markdown 文档 | `raw/sources/<domain>/videos/` |
| `github_repo` | GitHub 仓库 | 生成一份轻量拆解 Markdown，不克隆、不运行 | `raw/sources/<domain>/github_repo/` |
| `pdf_report` | PDF 报告、论文、白皮书 | 保存 PDF 路径，提取标题和正文快照为 Markdown | `raw/sources/<domain>/pdf_report/` |
| `ai_report` | 外部 AI 平台 Deep Research、临时 Codex/Claude 研究报告 | 保存报告原文 Markdown 和基础元数据；不默认拆解引用、摘要或核验 | `raw/sources/<domain>/ai_report/` |
| `personal_note` | 个人随手记录、灵感、待验证判断 | 保存到 inbox，标记为个人未验证想法 | `raw/inbox/` |

不要用 `pdf`、`html`、`markdown` 当 `source_type`。这些是 `media_format`。

## source_level

| source_level | 含义 | 使用规则 |
| --- | --- | --- |
| `primary` | 一手来源 | 官方文档、原论文、项目仓库、原始数据、标准。可作为强证据，但仍要注意时效。 |
| `secondary` | 人类二手分析 | 博客、媒体、课程、公众号、解读文章。关键事实要回到一手来源核验。 |
| `ai_secondary` | AI 生成二手分析 | Deep Research、外部 AI 报告、临时 Codex/Claude 研究。不能直接当事实。 |
| `personal` | 个人想法 | 灵感、判断、备忘。默认未验证。 |
| `derived` | 本知识库派生产物 | 已有来源基础上的输出草稿或正式产物，必须保留 `source_refs`。 |

## media_format

```text
html
markdown
pdf
docx
pptx
xlsx
image
audio
video
code
dataset
text
mixed
```

同一个 `source_type` 可以有不同 `media_format`。例如 AI 报告可能是 `markdown`、`pdf` 或 `html`。

## ai_report 边界

`ai_report` 是初始收集材料，不是已消化知识。默认只保存报告原件或导出快照：

- 一份 Markdown 原始采集文档保存报告正文或导出内容。
- frontmatter 记录平台、模型/工具、生成时间、导入时间、主题或原始任务、导出格式。
- 标记 `source_type: ai_report`、`source_level: ai_secondary`、`status: captured`。

默认不做这些动作：

- 不摘要；
- 不批判；
- 不核验事实；
- 不抽取引用链接；
- 不单独创建报告中引用的一手来源文档；
- 不把报告结论写入 `wiki/topics/`。

只有当用户明确要求“消化这份报告”“研究这份报告”“核验报告来源”时，才进入 `wiki/notes/`、`wiki/research/` 或拆分一手来源。

## status

```text
captured
capture_failed
to_digest
digesting
digested
used_in_research
used_in_topic
used_in_output
archived
discarded
```

- `captured`: 已保存原始采集文档，尚未消化。
- `capture_failed`: 已登记来源，但抓取失败或不完整。
- `to_digest`: 值得后续消化。
- `digesting`: 正在转成笔记或研究。
- `digested`: 已生成 `wiki/notes/`。
- `used_in_research`: 已进入 `wiki/research/`。
- `used_in_topic`: 已回写 `wiki/topics/`。
- `used_in_output`: 已用于 `wiki/outputs/`。
- `archived`: 保留但不再处理。
- `discarded`: 判断无价值，准备清理或已清理。

## capture_status

```text
success
partial
failed
```

- `success`: 正文、关键元数据和必要资产采集完成。
- `partial`: 主体可用，但字段、图片、附件或转写有缺失。
- `failed`: 无可用原始内容，只保留来源入口和失败原因。

## 图片本地化

公众号文章和网页文章默认下载正文图片：

- 正文图片保存到 `<slug>.assets/images/001.<ext>` 这类顺序文件名。
- 封面图保存到 `<slug>.assets/cover.<ext>`。
- Markdown 必须引用本地相对路径。
- 跳过头像、站点 logo、分享图标、tracking pixel 和统计脚本图片。
- 正文里的广告、二维码、作者名片默认保留，并在 `采集日志` 标注可能不是正文内容。
- 下载失败时保留 Markdown 占位和失败记录，不能伪装成完整抓取。
