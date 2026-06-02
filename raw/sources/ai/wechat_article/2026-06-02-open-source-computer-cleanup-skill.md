---
type: source
domain: ai
source_type: wechat_article
source_level: secondary
media_format: html
status: captured
created: 2026-06-02
updated: 2026-06-02
captured_at: 2026-06-02 22:47:41 +0800
published_at: 2026-06-02 09:58:00 +0800
author: 数字生命卡兹克
publisher: 数字生命卡兹克
platform: 微信公众号
language: zh-CN
source_url: https://mp.weixin.qq.com/s/NyOMIlOD986OC4SI9vmxlA
canonical_url: https://mp.weixin.qq.com/s/NyOMIlOD986OC4SI9vmxlA
capture_tool: wechat-article-extractor
capture_status: partial
image_count: 24
image_downloaded: 0
image_failed: 0
account_name: 数字生命卡兹克
account_id: gh_94dba26f8ca0
account_biz: MzIyMzA5NjEyMA==
msg_mid: 2647682858
msg_idx: 1
msg_sn: 0bdfd10a71c2746e17dab2157aab6369
msg_desc: Mac和Windows都有救了
msg_cover_url: https://mmbiz.qpic.cn/sz_mmbiz_jpg/2jjfQoZLoqXr9sGI1QsbLPk9hI2icC7fBSkibJItnBicVXLbjHCd40lfq9knDl8YFEF1VPKturRF4bflbgtIVcjGxGarY504EP65VjQX2rI6LA/0?wx_fmt=jpeg
related_notes: []
related_research: []
related_topics: []
source_refs: []
---

# 为了不花那120刀，我把电脑清理软件做成了开源skill。

> 采集说明：这是 `raw/` 证据层来源卡，尚未消化为知识。出于版权合规，本文件不保存公众号全文和图片副本，只保留元数据、原文入口、非逐字摘要、可追踪链接和未核验事项。

## 基本信息

- 来源类型：微信公众号文章
- 证据等级：secondary，人类二手分析 / 经验文章
- 载体格式：HTML
- 作者：数字生命卡兹克
- 机构 / 发布方：数字生命卡兹克
- 平台：微信公众号
- 发布时间：2026-06-02 09:58:00 +0800
- 采集时间：2026-06-02 22:47:41 +0800
- 原始链接：https://mp.weixin.qq.com/s/NyOMIlOD986OC4SI9vmxlA
- 规范链接：https://mp.weixin.qq.com/s/NyOMIlOD986OC4SI9vmxlA
- 摘要：Mac和Windows都有救了
- 封面图：原文有封面图，未下载本地副本
- 正文图片：23 张，未下载本地副本

## 内容提要（非原文）

这篇文章用一个“让 Codex 只读分析电脑存储”的小例子，讨论 Agent 和 Skill 对传统工具型软件的冲击。作者看到 X 上有人用一句 prompt 让 Codex 分析 MacBook 存储并找出大文件，于是在自己的 MacBook Air 上复现，发现 B 站离线缓存、Chrome 数据、开发环境和 Claude / Codex 相关文件占用了大量空间。

作者认为传统 Mac / Windows 清理软件的核心能力，本质是扫描文件、解释风险、给出清理动作。既然 Agent 能读取系统状态、理解文件语义并生成操作建议，那么这类明确规则任务可以被 Agent + Skill 重做一遍，而不必依赖固定 UI 的传统清理软件。

文章随后介绍作者做的一个开源清理垃圾 skill：支持 Mac 和 Windows，先进行只读扫描，再生成可交互 HTML 报告。报告包含磁盘总览、占用排行、清理优先级、绿 / 黄 / 红三色风险分级，以及打开路径、移到废纸篓、手动确认等动作入口。作者强调扫描阶段只读，真正清理必须由用户在报告页面主动确认。

作者用自己的机器和同事的 Windows 机器做了展示，并把这个 skill 与 CleanMyMac 做对比。作者的核心判断是：Agent 给出的路径、大小、解释和删除影响比传统清理软件更透明，也更容易按用户的具体需求定制。文章最后把这个案例上升为一个更大的判断：很多靠单一明确功能存在的工具型软件，未来竞争对手可能不是另一家软件公司，而是用户手里的 prompt 和 Agent skill。

## 原文中出现的外部链接

- GitHub 仓库：https://github.com/KKKKhazix/khazix-skills

## 原始内容

原文全文未保存。需要回看完整正文、截图和作者语境时，回到原始链接：

https://mp.weixin.qq.com/s/NyOMIlOD986OC4SI9vmxlA

## 采集日志

- 采集工具：`wechat-article-extractor`
- 采集状态：partial
- 已抽取字段：标题、作者、公众号、发布时间、摘要、封面图 URL、正文图片数量、原始链接、公众号 ID、biz、mid、idx、sn
- 缺失字段：`account_alias`、`account_description`、`msg_source_url`、`tags`
- 图片下载失败：无下载失败；本次按版权合规策略跳过封面和正文图片本地化
- 正文处理：抽取器成功读取正文 HTML；本文件未保存全文，只保存非逐字摘要和来源入口
- 其他问题：文章中关于清理效果、软件价格、跨平台能力和安全性的说法均为作者经验陈述，未做外部核验

## 需要核验的事实

- GitHub 仓库 `KKKKhazix/khazix-skills` 是否存在、当前是否包含该清理 skill、许可证和使用说明是什么。
- 该 skill 是否确实支持 Mac 和 Windows，以及运行方式、权限边界和删除确认机制是否与文章描述一致。
- 作者提到的清理空间数值、CleanMyMac 扫描结果和价格信息均未核验，不能直接写入稳定知识。
- “工具型软件会被 Agent / Skill 冲击”是作者判断，需要结合更多来源和实际案例再升级为研究结论。

## 处理状态

- [ ] 已阅读
- [ ] 已转成笔记
- [ ] 已进入研究
- [ ] 已提炼为稳定知识
- [ ] 已用于输出

## 后续动作

- 如果要消化这篇文章，下一步应进入 `wiki/notes/agent-systems/` 或 `wiki/notes/mcp-cli-browser/`，用自己的语言重写文章的工程判断。
- 如果要研究这个 skill 本身，先采集 GitHub 仓库为一手来源，再检查代码结构、权限边界和实际可运行性。

## 未验证事项

- 未运行文章中的 skill。
- 未核验 GitHub 仓库、CleanMyMac 价格、清理空间数据或截图内容。
- 未保存公众号全文和图片副本；未来引用具体原文表述时必须回到原文核对。
