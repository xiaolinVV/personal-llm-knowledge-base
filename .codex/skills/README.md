# Codex Skills

这是本仓库的可执行 Skill 配置目录。Codex 通过根目录下的 `.codex/skills/` 发现这些 Skill，因此不要把本目录迁入 `schema/`。

为了让 Obsidian 文件浏览器能看到这些 Skill，仓库提供了一个可见别名：

- [schema/skills](../../schema/skills)：指向 `.codex/skills/` 的目录 symlink。

这不是第二份副本。通过 `schema/skills/...` 打开的文件和 `.codex/skills/...` 是同一份文件。

## 当前 Skill

- [knowledge-base-workflow](knowledge-base-workflow/SKILL.md)：资料入库、分类、消化、升级、研究、输出回写。
- [video-to-wiki](video-to-wiki/SKILL.md)：学习视频证据采集、来源登记、标准 wiki 笔记编译和 index/log 回写。

兼容说明：`video-study-notes` 是旧名称，已经由 `video-to-wiki` 取代；后续不要新增旧名称引用。

## 规则

- 不要移动 `.codex/skills/`，否则会破坏 Codex 的工具发现。
- 新增或修改 Skill 时，继续以 `.codex/skills/<skill-name>/` 为真实路径。
- 在 Obsidian 中阅读和编辑时，可以使用 `schema/skills/<skill-name>/` 这个可见入口。
