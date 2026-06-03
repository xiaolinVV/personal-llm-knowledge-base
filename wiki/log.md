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

## [2026-06-02] method | 采集阶段自动化预处理规则

- 更新 `knowledge-base-workflow`：采集阶段默认生成来源目录包，包含来源卡、Markdown 快照、元数据、采集日志和必要本地图片资产。
- 更新 `source-card` 模板：新增 `source_type`、`source_level`、`media_format`、`capture_status`、图片统计和后续关联字段。
- 新增 `schema/meta/source-types.md`：固定来源类型、证据等级、载体格式、采集状态和图片本地化规则。
- 更新 `video-to-wiki`：增加 capture-only 边界，视频采集默认不生成 `wiki/notes/`，除非用户明确要求消化。

未验证事项：

- 本次只更新方法、模板和 skill 规则，没有实际抓取公众号、网页、视频、GitHub 仓库或 AI 报告样例。
- 图片下载、HTML 转 Markdown、GitHub API 拆解和视频 capture-only 的具体脚本行为尚未用真实样例验证。

## [2026-06-02] method | AI report 采集边界修正

- 修正 `ai_report` 默认动作：外部 AI 平台或临时 Codex/Claude Deep Research 报告属于初始收集材料，只保存报告快照和基础元数据。
- 默认不再拆解引用来源、不摘要、不核验事实、不创建一手来源文档；只有用户明确要求消化或研究报告时才做这些动作。

未验证事项：

- 本次仍未用真实 AI report 样例验证来源文档生成效果。

## [2026-06-02] method | 采集落盘简化为单文档

- 修正前一版过重设计：普通采集不再默认创建 `source.md`、`snapshot.md`、`metadata.json`、`capture-log.md` 多文件来源包。
- 新默认：每个来源保存为一份 `raw/sources/<domain>/<source-type>/<YYYY-MM-DD-title-slug>.md` 原始 Markdown 文档，图片和小资产放同名 `.assets/` 目录。
- 视频保留大资产例外：大文件、字幕、ASR、关键帧和 `asset-manifest.md` 仍放 `raw/assets/local-media/`，来源侧只生成一份 Markdown 文档引用资产清单。

未验证事项：

- 本次只更新方法、模板和 skill 规则，没有实际生成公众号、网页、视频、GitHub 或 AI report 采集样例。

## [2026-06-02] ingest | 为了不花那120刀，我把电脑清理软件做成了开源skill。

- 来源：微信公众号文章，原始链接 `https://mp.weixin.qq.com/s/NyOMIlOD986OC4SI9vmxlA`。
- 落点：`raw/sources/ai/wechat_article/2026-06-02-open-source-computer-cleanup-skill.md`。
- 分类：`domain: ai`，`source_type: wechat_article`，`source_level: secondary`，`media_format: html`。
- 采集状态：`partial`。已抽取标题、作者、公众号、发布时间、摘要、封面图 URL、正文图片数量和微信文章参数；未保存公众号全文和图片副本。
- 索引：已加入 `wiki/index.md` 的 Raw Sources 表。

未验证事项：

- 未运行文章中的开源 skill。
- 未核验 GitHub 仓库、CleanMyMac 价格、清理空间数据、截图内容或跨平台能力。
- 本次为来源收集，不生成 `wiki/notes/`、`wiki/research/` 或稳定主题结论。

## [2026-06-02] ingest | 分享一个我用了2年的深度研究Prompt，半小时帮你搞懂任何陌生领域。

- 来源：微信公众号文章，原始链接 `https://mp.weixin.qq.com/s/Y_uRMYBmdLWUPnz_ac7jWA`。
- 落点：`raw/sources/ai/wechat_article/2026-04-13-hv-analysis-deep-research-prompt.md`。
- 分类：`domain: ai`，`source_type: wechat_article`，`source_level: secondary`，`media_format: html`。
- 采集状态：`partial`。已抽取标题、作者、公众号、发布时间、摘要、封面图 URL、正文图片数量和微信文章参数；未保存公众号全文、长 Prompt 原文和图片副本。
- 索引：已加入 `wiki/index.md` 的 Raw Sources 表。

未验证事项：

- 未运行文章中的 Prompt 或 `hv-analysis` Skill。
- 未核验 GitHub 仓库、Skill 能力、arXiv 查询能力、PDF 输出能力或示例研究报告质量。
- 本次为来源收集，不生成 `wiki/notes/`、`wiki/research/` 或稳定方法论结论。

## [2026-06-03] method | 强化公众号和网页正文采集规则

- 强化 `knowledge-base-workflow`：公众号文章和普通网页默认必须保存原始正文 Markdown 和必要图片资产；摘要只能作为附加说明，不能替代 `原始内容`。
- 更新 `schema/agent-protocol.md`：Ingest 规则明确只有用户要求 `metadata-only`、`summary-only`、轻量采集，或正文采集失败时，才允许不保存正文。
- 更新 `schema/meta/source-types.md`：补充正文与图片本地化硬约束，并要求不保存正文时在 `capture_status`、`采集日志` 和 `未验证事项` 写明原因。
- 更新 `schema/templates/source-card.md` 和 `raw/sources/README.md`：模板和来源入口同步强调摘要不能替代正文。

未验证事项：

- 本次只强化规则，没有重新采集此前两篇微信公众号文章的正文和图片。
