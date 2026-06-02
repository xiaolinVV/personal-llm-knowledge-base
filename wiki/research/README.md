# 问题研究

`wiki/research/` 是问题驱动研究层，放已经超出单篇资料消化、并形成结构化判断的材料。

这里不按“收藏了什么资料”组织，而按“要回答什么问题”组织。

## 与其他目录的边界

- 来源入口放 `../../raw/sources/`。
- 单篇资料消化放 `../notes/`。
- 稳定、跨来源、可复用的 evergreen 知识放 `../topics/`。
- 能运行验证的最小实验放 `../labs/`。
- 最终报告、PPT、文章和方案放 `../outputs/`。

## 目录

- [use-cases/](use-cases/)：真实应用场景、商业边界、行业问题、评测数据集。
- [open-source-projects/](open-source-projects/)：开源项目、工具链、Agent runtime、CLI 和浏览器工具拆解。

## 当前重点

- [AI 应用层经济性与物理 AI](use-cases/AI%20应用层出清、成本结构、商业模式与%20Physical%20AI%20研究报告.md)
- [企业级 RAG 评测数据集](use-cases/2026-05-15-enterprise-rag-eval-datasets.md)
- [浏览器自动化专题研究](open-source-projects/browser-automation/)
- [RAGFlow 官方材料与实践案例](open-source-projects/ragflow/)

## 研究文件要求

每份研究至少说明：

- 要回答的问题；
- 主要证据来源；
- 核心判断；
- 反例或边界；
- 未验证事项；
- 后续可做的实验或输出。

新增研究优先使用 [research 模板](../../schema/templates/research.md)。
