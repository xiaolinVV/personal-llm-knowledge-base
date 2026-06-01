---
type: method
domain: learning-research
status: active
created: 2026-06-01
updated: 2026-06-01
source_refs: []
---

# Obsidian、iCloud 与 GitHub 同步策略

## 核心判断

本知识库只维护一份正文数据：iCloud Obsidian vault。

GitHub 负责版本化备份，iCloud 负责 Mac 与 iPhone 之间的文件同步。两者不是替代关系：

- iCloud 解决多设备实时访问。
- GitHub 解决历史版本、误删回滚和异地备份。
- 本机 Git 元数据留在非 iCloud 目录，避免把 `.git/` 交给 iCloud 同步。

## 当前路径

唯一工作目录：

```text
/Users/zhangshaolin/Library/Mobile Documents/iCloud~md~obsidian/Documents/personal-llm-knowledge-base
```

兼容入口：

```text
/Users/zhangshaolin/Documents/personal-llm-knowledge-base
```

这个兼容入口是 symlink，指向上面的 iCloud vault。以后 Codex、Terminal 和 Obsidian 都应进入同一份内容。

本机 Git 元数据：

```text
/Users/zhangshaolin/Library/Application Support/personal-llm-knowledge-base/gitdir
```

GitHub 远端：

```text
git@github.com:xiaolinVV/personal-llm-knowledge-base.git
```

## 日常工作流

1. 在 Mac Obsidian、iPhone Obsidian 或 Codex 中编辑同一个 iCloud vault。
2. 等 iCloud 把 iPhone 上的改动同步回 Mac。
3. 在 Mac 上检查 Git 状态。
4. 提交并推送到 GitHub。

常用命令：

```bash
cd /Users/zhangshaolin/Documents/personal-llm-knowledge-base
git status --short --branch
git add -A
git commit -m "docs(kb): 同步知识库"
git push
```

如果只是查看远端状态：

```bash
git fetch origin
git status --short --branch
```

## 不进入 iCloud 和 GitHub 的内容

以下内容不作为知识库正文同步：

- `.git/`：真实 Git 数据库在本机 Application Support。
- `.venv/`：本机 Python 环境。
- `.obsidian/`：Obsidian 本机配置，默认不进 Git。
- `local-media/`：大视频、ASR 中间产物、批量素材和本地媒体。
- `.env`：本机密钥和环境变量。

旧本地目录已退役为安全备份，其中的 `local-media/` 继续保留为本机大媒体存放处；不要把它移动进 iCloud vault。

## 恢复原则

如果 iCloud 出问题，优先从 GitHub clone 正文内容，再重新配置外置 gitdir。

如果 GitHub 历史需要回滚，先在 Mac 上 `git status` 确认 iCloud 已完成同步，再做 `revert` 或新提交。不要在 iPhone 还没同步完成时做强制回滚。
