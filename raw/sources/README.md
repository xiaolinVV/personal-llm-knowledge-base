# 来源索引

`raw/sources/` 是轻量来源索引层，保存原始采集文档、本地图片资产和原始材料入口，而不是保存知识本身。

来源可以是网页、论文、书、视频、PDF、代码仓库、课程、聊天记录或本地资产路径。来源没有经过理解、压缩、质疑和重写之前，不能冒充知识。

## 当前目录

- [ai/](ai/)：AI、LLM、Agent、RAG、MCP、工具链和相关官方资料入口。

## 轻量策略

值得保存但尚未消化的资料，默认采集成一份 Markdown 原始文档：

```text
raw/sources/<domain>/<source-type>/<YYYY-MM-DD-title-slug>.md
raw/sources/<domain>/<source-type>/<YYYY-MM-DD-title-slug>.assets/
  cover.<ext>
  images/
```

公众号文章和普通网页的正文图片默认下载到同名 `.assets/` 目录，并在 Markdown 中使用相对路径引用。Git 保存原始采集文档和少量关键附件。大视频、完整网页资产、批量截图、ASR 中间产物和下载缓存放 `raw/assets/local-media/`、旧兼容 `local-media/` 或外部路径。

新增原始采集文档使用 [source-card 模板](../../schema/templates/source-card.md)。
来源类型和采集状态见 [source-types](../../schema/meta/source-types.md)。
