# 企业级 RAG 问答质量测试数据集调研报告

调研日期：2026-05-15  
调研目标：寻找可用于后续测试 RAG 问答效果的公开数据集，优先覆盖企业内部知识库、技术支持、金融文档、合同法务、跨文档推理、幻觉检测等真实问题。  
调研口径：GitHub 仓库、仓库 README、release 资产、公开数据说明、论文链接和数据下载入口。仓库状态抓取于 2026-05-15。  

## 结论

如果只选一个主数据集，选 `EnterpriseRAG-Bench`。

它目前最接近企业内部知识库 RAG：模拟公司内部数据，覆盖 Slack、Gmail、Linear、Google Drive、HubSpot、Fireflies、GitHub、Jira、Confluence 等来源；问题有金标答案、预期文档、答案事实点，能同时评检索和生成。

但不要指望一个数据集解决所有问题。RAG 问答质量不是一个单分数问题。正确的数据结构是：

1. 主评测集：测企业内部知识库全链路。
2. 专项补充集：分别测金融 PDF、技术支持、合同法务、多轮对话、跨文档推理、幻觉。
3. 自建小型中文金标集：测我们自己的业务文档、中文表达、权限和元数据过滤。

推荐组合：

```text
第一批：EnterpriseRAG-Bench + FinanceBench + RAGTruth
第二批：MTRAG + MultiHop-RAG + TechQA + LegalBench-RAG/CUAD
第三批：按需要补 FinRAGBench-V、KG-RAG-datasets、Open RAG Benchmark、CRAG-MM
```

## 核心判断

【值得做】

公开数据集已经足够支撑第一版 RAG 评测体系。真正的问题不是“有没有数据”，而是不要把不同失败模式混成一个总分。

【关键洞察】

- 数据结构：评测样本至少要有 `question`、`gold_answer`、`expected_doc_ids/evidence`、`answer_facts`、`question_type`。没有证据字段的数据集，只能弱评答案，不能严肃评 RAG。
- 复杂度：先统一成内部评测 schema，再写评测逻辑。不要让评测器里到处都是 `if dataset == ...`。
- 风险点：英文公开数据不能替代中文企业数据；模拟企业数据不能替代真实权限、真实组织术语和真实历史包袱；许可证和商用权限必须单独确认。

【方案】

1. 先用 `EnterpriseRAG-Bench` 做主基准，跑通“检索召回 + 答案事实覆盖 + 不可回答拒答”的完整链路。
2. 用 `FinanceBench` 补 PDF、表格、数值推理和证据引用。
3. 用 `RAGTruth` 补 hallucination/factuality 评估，不要拿它当完整检索数据集。
4. 用 `MTRAG` 和 `MultiHop-RAG` 补多轮、跨文档和上下文依赖。
5. 用 `TechQA`、`LegalBench-RAG`、`CUAD` 补企业技术支持和合同法务。
6. 最后自建 50 到 200 条中文企业金标样本。没有这一步，中文企业 RAG 评测就是半成品。

## 数据集分层

### 第一优先级：企业 RAG 主测试集

| 数据集 | 来源 | 数据规模和结构 | 适合评什么 | 当前判断 |
| --- | --- | --- | --- | --- |
| EnterpriseRAG-Bench | <https://github.com/onyx-dot-app/EnterpriseRAG-Bench> | 约 50 万企业模拟文档，500 个核心问题，100 个额外 metadata 问题；字段包含问题、金标答案、答案事实点、预期文档 ID | 企业内部知识库全链路 RAG、跨系统检索、冲突信息、找不到答案、元数据依赖 | 主数据集，优先采用 |
| MTRAG | <https://github.com/IBM/mt-rag-benchmark> | 110 个人工多轮对话，842 个任务；4 个语料域：Wikipedia、Cloud 技术文档、Finance、Government；另有 200 个合成对话 | 多轮 RAG、追问、不可回答、部分可回答、上下文依赖 | 第二主数据集，用来补企业 RAG 的对话属性 |

### 第二优先级：企业常见业务专项

| 数据集 | 来源 | 数据规模和结构 | 适合评什么 | 当前判断 |
| --- | --- | --- | --- | --- |
| FinanceBench | <https://github.com/patronus-ai/financebench> | 开源 150 条金融 QA，含金标答案、证据、PDF；完整集声称 10,231 个问题，需联系作者 | 财报 PDF、表格、数值抽取、证据引用、金融问答 | 金融/财务类 RAG 必测 |
| TechQA | <https://github.com/IBM/techqa> | IBM 技术问答数据，训练/开发数据和约 80 万 TechNotes 在 Hugging Face | 企业技术支持、产品文档、故障排查问答 | 适合客服/售后/技术支持 RAG |
| LegalBench-RAG | <https://github.com/zeroentropy-ai/legalbenchrag> | 法律合同检索 benchmark，ground truth 到文件路径和字符区间；数据下载在 Dropbox | 合同检索、精确证据定位、法律条款 RAG | 法务/合同检索强相关 |
| CUAD | <https://github.com/TheAtticusProject/cuad> | 合同理解数据集，仓库包含 `data.zip`；专家标注合同审查任务 | 合同条款抽取、法律问答证据定位 | 可作为 LegalBench-RAG 的底层补充 |
| KG-RAG-datasets | <https://github.com/docugami/KG-RAG-datasets> | SEC 10-Q v1：20 个文档、195 个 QnA；另有航空事故、临床试验、政府报告草稿 | 多文档长文档 RAG、单文档多 chunk、多文档聚合 | 小而实用，适合做结构化 RAG 小实验 |

### 第三优先级：能力专项和补充 benchmark

| 数据集 | 来源 | 数据规模和结构 | 适合评什么 | 当前判断 |
| --- | --- | --- | --- | --- |
| MultiHop-RAG | <https://github.com/yixuantt/MultiHop-RAG> | 2,556 个查询；证据分布在 2 到 4 个文档；带 metadata | 跨文档推理、多跳检索、metadata 参与推理 | 推荐作为跨文档专项 |
| RAGTruth | <https://github.com/ParticleMedia/RAGTruth> | 2,965 个 source，17,790 个 RAG 响应；人工标注 hallucination span；QA 子集 989 source、5,934 response | 答案忠实度、幻觉检测、回答质量分类 | 用来评回答，不是主检索集 |
| FinRAGBench-V | <https://github.com/zhaosuifeng/FinRAGBench-V> | 金融多模态 RAG，中文和英文金融文档页，问题覆盖表格、图、文本和视觉引用 | 金融多模态 RAG、视觉证据引用 | 有多模态需求再上 |
| Open RAG Benchmark | <https://github.com/vectara/open-rag-bench> | 1,000 篇 arXiv PDF，3,045 个 QA；包含文本、表格、图片 | 科研 PDF、多模态 PDF、表格/图片混合检索 | 技术 PDF 场景可用，但不够企业内部 |
| CRAG-MM | <https://github.com/facebookresearch/CRAG-MM> | 多模态、多轮 RAG；图像、问题、答案、检索内容；14 个领域 | 视觉 RAG、多轮视觉问答、可穿戴/真实世界图像场景 | 不是企业知识库主线，按需使用 |
| RAGBench | <https://github.com/rungalileo/ragbench> | 聚合 HotpotQA、MS MARCO、HAGRID、ExpertQA 等数据，用于 RAG eval 框架基准 | 通用 RAG 评估框架比较 | 可作 baseline，不作为企业主集 |

## 重点数据集拆解

### 1. EnterpriseRAG-Bench

仓库：<https://github.com/onyx-dot-app/EnterpriseRAG-Bench>  
Hugging Face：<https://huggingface.co/datasets/onyx-dot-app/EnterpriseRAG-Bench>  
Leaderboard：<https://huggingface.co/spaces/onyx-dot-app/EnterpriseRAG-Bench-Leaderboard>  
论文：<https://arxiv.org/abs/2605.05253>  

抓取状态：

- GitHub stars/forks：330 / 30
- 最近 push：2026-05-08
- 最新 release：`v1.0.0`，发布时间 2026-03-29
- release 资产包含 `all_documents.zip`，大小约 1.26GB；也提供按数据源切片的 zip 和 `questions.jsonl`
- 仓库 license 文件是 MIT；数据集本身的使用条款仍应以 Hugging Face dataset card 和 release 说明为准

数据结构：

```json
{
  "question_id": "qst_0001",
  "question_type": "basic",
  "source_types": ["github"],
  "question": "问题文本",
  "expected_doc_ids": ["dsid_xxx"],
  "gold_answer": "金标答案",
  "answer_facts": ["答案事实点 1", "答案事实点 2"]
}
```

问题类型覆盖：

- basic：单一文档简单事实
- semantic：关键词不直接匹配，需要语义检索
- intra-document reasoning：单文档远距离信息组合
- project related：项目相关文档聚合
- constrained：多个候选文档中按条件筛选正确答案
- conflicting info：文档之间有冲突
- completeness：需要找全多个相关文档
- high level：高层总结，没有单一 ground truth document
- info not found：答案不存在，需要拒答
- metadata-dependent：额外问题集，依赖元数据过滤

价值：

- 它测的是企业 RAG 真问题：多系统、多格式、内部术语、冲突、过期、找不到答案。
- 它的字段直接支持检索和生成双评估。
- 它提供 answer evaluation 目录，支持 correctness、completeness、document recall、invalid extra documents。

风险：

- 数据是模拟企业，不是真实企业。它能测结构性能力，不能证明真实业务上线可用。
- 主要是英文。中文企业制度、合同、公告、流程文档仍要自建金标。
- 数据量较大，第一次下载和索引要有存储和时间预算。

采用建议：

```text
必须采用。先抽 50 条 smoke set，再跑完整 500 条。
```

### 2. MTRAG

仓库：<https://github.com/IBM/mt-rag-benchmark>  
论文：<https://doi.org/10.1162/TACL.a.19>  
MTRAG-UN 论文：<https://arxiv.org/abs/2602.23184>  

抓取状态：

- GitHub stars/forks：138 / 29
- 最近 push：2026-05-01
- 仓库 license 文件是 Apache-2.0

数据结构：

- MTRAG human：110 个多轮对话，平均 7.7 轮，转换为 842 个 evaluation tasks。
- MTRAG synthetic：200 个合成对话。
- 语料域：ClapNQ、Cloud 技术文档、FiQA、Government。
- MTRAG-UN：666 个任务，超过 2,800 个对话 turn，关注不可回答、问题不完整、非独立问题、用户不理解模型答案等开放挑战。

价值：

- 企业 RAG 很少是单轮问答。用户会追问、补充、纠正、质疑。MTRAG 正好测这块。
- Cloud 技术文档域贴近技术支持。
- 提供 retrieval tasks、generation tasks 和 evaluation scripts。

风险：

- Banking 和 Telco 两个企业域在 README 中标注为 coming soon，不能现在当作可用数据。
- 多轮评估更复杂，不适合作为第一版唯一数据集。

采用建议：

```text
第二批采用。先用 Cloud + FiQA 两个域，别一开始全量铺开。
```

### 3. FinanceBench

仓库：<https://github.com/patronus-ai/financebench>  
论文：<https://arxiv.org/abs/2311.11944>  

抓取状态：

- GitHub stars/forks：312 / 58
- 最近 push：2024-12-03
- GitHub license 字段为空；仓库未发现标准 LICENSE 文件

开源数据：

- `data/financebench_open_source.jsonl`：150 条开源 QA
- `data/financebench_document_information.jsonl`：文档元信息
- `pdfs/`：相关财报 PDF
- `results/`：论文中模型输出和人工评审结果

字段包括：

- `question`
- `answer`
- `justification`
- `evidence`
- `company`
- `doc_name`
- `question_type`
- `question_reasoning`

价值：

- 金融文档是企业 RAG 的硬题：PDF、表格、页码、数值单位、年份、指标口径。
- gold answer 和 evidence 都在，适合评“答案是否由证据支持”。

风险：

- 开源样本只有 150 条。完整集需要联系作者。
- license 不清楚，正式商用或公开 benchmark 报告前要确认。

采用建议：

```text
第一批采用，但只把它当金融专项，不要和 EnterpriseRAG-Bench 混成一个总分。
```

### 4. RAGTruth

仓库：<https://github.com/ParticleMedia/RAGTruth>  
论文：<https://arxiv.org/abs/2401.00396>  

抓取状态：

- GitHub stars/forks：247 / 31
- 最近 push：2024-12-02
- 仓库 license 文件是 MIT

数据结构：

- `dataset/source_info.jsonl`：source、prompt、QA/Data2txt/Summary 的基础信息
- `dataset/response.jsonl`：模型回答、模型名、温度、人工 hallucination span、quality 标记
- 总体：2,965 个 source，17,790 个 response，14,289 个 hallucination spans
- QA 子集：989 个 source，5,934 个 response

价值：

- 它不是为了测“能不能召回正确文档”，而是为了测“回答有没有编造、有没有和上下文矛盾”。
- 对训练或校验 answer evaluator 很有价值。

风险：

- 不适合作为企业主检索 benchmark。
- 标注粒度是回答中的 hallucination span，接入我们的评测体系要单独做映射。

采用建议：

```text
第一批采用，用于答案忠实度和幻觉专项，不用于检索召回主分。
```

### 5. MultiHop-RAG

仓库：<https://github.com/yixuantt/MultiHop-RAG>  
Hugging Face：<https://huggingface.co/datasets/yixuantt/MultiHopRAG>  
论文：<https://arxiv.org/abs/2401.15391>  

抓取状态：

- GitHub stars/forks：443 / 37
- 最近 push：2025-04-03
- README 标注 license 为 ODC-BY

数据结构：

- 2,556 个 query
- 每个 query 的 evidence 分布在 2 到 4 个文档
- 问题涉及文档 metadata
- 仓库提供简单 retrieval、QA 和 evaluation 脚本

价值：

- 专门测跨文档推理和 metadata。企业 RAG 常见失败就是“召回一个片段看似对，但缺另一个关键约束”。

风险：

- 不是企业内部语料。
- 需要确认数据字段和我们内部 schema 的映射。

采用建议：

```text
第二批采用，专门做 multi-hop 分项。
```

### 6. LegalBench-RAG 和 CUAD

LegalBench-RAG：<https://github.com/zeroentropy-ai/legalbenchrag>  
CUAD：<https://github.com/TheAtticusProject/cuad>  

LegalBench-RAG 抓取状态：

- GitHub stars/forks：187 / 21
- 最近 push：2025-05-30
- 仓库 license 文件是 MIT
- 数据下载通过 Dropbox

CUAD 抓取状态：

- GitHub stars/forks：506 / 152
- 最近 push：2023-07-13
- 仓库包含 `data.zip`

价值：

- LegalBench-RAG 的 ground truth 到字符区间，适合严肃测检索是否定位到合同中的精确证据。
- CUAD 是专家标注合同理解数据集，可补合同条款抽取和问答。

风险：

- 法律数据的 license、原始合同来源和使用约束要仔细确认。
- LegalBench-RAG 更偏 retrieval benchmark，不是完整问答生成 benchmark。

采用建议：

```text
有合同/法务场景就采用。没有法务场景则先放第二批，不要污染主线。
```

### 7. TechQA

仓库：<https://github.com/IBM/techqa>  
数据：<https://huggingface.co/datasets/PrimeQA/TechQA>  
论文：<https://arxiv.org/abs/1911.02984>  

抓取状态：

- GitHub stars/forks：29 / 10
- 最近 push：2025-09-17
- README 说明 train/dev 数据和 80 万 TechNotes 在 Hugging Face

价值：

- 企业问答里“技术支持/产品文档/故障排查”非常常见。
- TechNotes 语料规模大，适合测长尾技术问题检索。

风险：

- 老数据集，原始任务更偏传统 QA，不是为现代 RAG 专门设计。
- license 和数据使用条款要单独看 Hugging Face。

采用建议：

```text
如果后续重点是客服、售后、工程支持，第二批采用。
```

## 不建议直接作为主集的数据

### 通用开放域 QA

例如 HotpotQA、MS MARCO、Natural Questions、TriviaQA。

它们不是没用，而是不适合作为企业 RAG 主评测。它们更多测搜索/百科问答，测不出：

- 内部系统多源数据
- 公司黑话和项目代号
- 文档冲突和过期
- 权限/部门/时间等 metadata 过滤
- 找不到答案时是否拒答
- 表格、合同、流程制度的精确证据

可以做 baseline，不能做最终验收。

### 只提供框架、不提供清晰金标的问题集

有些仓库叫 RAG benchmark，但实际是代码 demo、论文复现实验或模型评估脚本。没有问题、金标答案和证据文档，就不要纳入我们的主评测数据。

## 统一评测 schema 建议

不要让每个数据集的字段污染评测器。导入阶段统一转换。

建议内部格式：

```json
{
  "id": "string",
  "dataset": "enterprise-rag-bench",
  "language": "en",
  "domain": "enterprise_internal",
  "question_type": "basic",
  "source_types": ["github"],
  "question": "string",
  "gold_answer": "string",
  "answer_facts": ["string"],
  "expected_doc_ids": ["string"],
  "evidence": [
    {
      "doc_id": "string",
      "text": "string",
      "page": 1,
      "char_start": 0,
      "char_end": 100
    }
  ],
  "must_refuse": false,
  "metadata_constraints": {
    "department": "string",
    "date": "string"
  },
  "license_note": "string",
  "source_url": "string"
}
```

最小字段：

```text
id
dataset
question
gold_answer 或 answer_facts
expected_doc_ids 或 evidence
question_type
```

## 评测指标建议

先把指标拆开，不要上来算一个总分。

### 检索指标

| 指标 | 说明 |
| --- | --- |
| Recall@k | 预期证据文档是否在前 k 个结果里 |
| MRR@k | 第一个正确证据出现得有多靠前 |
| nDCG@k | 多个证据时排序是否合理 |
| Evidence coverage | 需要多个证据时是否找全 |
| Invalid extra docs | 是否引入多余错误文档 |

### 生成指标

| 指标 | 说明 |
| --- | --- |
| Answer fact coverage | `answer_facts` 覆盖多少 |
| Faithfulness | 回答是否被检索证据支持 |
| Refusal correctness | 答案不存在时是否拒答 |
| Conflict handling | 文档冲突时是否说明冲突并给完整答案 |
| Numeric exactness | 数值、单位、年份、口径是否精确 |

### 分组指标

必须按问题类型拆分：

- basic
- semantic
- multi-hop
- constrained
- conflicting info
- completeness
- not found
- metadata-dependent
- multi-turn
- legal
- finance
- technical support

一个总分没用。总分只能给老板看，不能指导修系统。

## 后续落地路径

### 第 1 步：建立样本目录

建议后续创建：

```text
wiki/labs/rag-eval-datasets/
  README.md
  data/
    enterprise-rag-bench.sample.jsonl
    financebench.sample.jsonl
    ragtruth.sample.jsonl
  scripts/
    normalize_enterprise_rag_bench.py
    normalize_financebench.py
    normalize_ragtruth.py
  schema/
    rag_eval_case.schema.json
```

注意：这是后续实验，不是本报告已经完成的工作。

### 第 2 步：先做 smoke set

不要一开始全量下载和索引。先抽：

- EnterpriseRAG-Bench：50 条
- FinanceBench：30 条
- RAGTruth QA：50 条 response
- MultiHop-RAG：30 条

目标是验证评测链路，不是刷分。

### 第 3 步：补中文企业金标

最少做 50 条中文样本：

- 20 条单文档制度问答
- 10 条跨文档流程问答
- 5 条冲突信息
- 5 条历史版本/过期文档
- 5 条找不到答案
- 5 条 metadata 约束，例如部门、时间、地区、角色

这一步不能省。公开英文 benchmark 不能代表中文企业环境。

### 第 4 步：形成评测报告模板

每次评测输出至少包含：

```text
数据集版本
索引配置
chunk 策略
embedding 模型
rerank 模型
top_k
生成模型
prompt 版本
检索指标
生成指标
按 question_type 拆分结果
失败样例
修复建议
```

没有这些元数据，评测结果无法复现。

## 数据集采用优先级

| 优先级 | 数据集 | 原因 |
| --- | --- | --- |
| P0 | EnterpriseRAG-Bench | 最贴企业内部知识库，字段适合全链路评测 |
| P0 | FinanceBench | 金融 PDF 和数值推理是企业 RAG 硬题 |
| P0 | RAGTruth | 专门补回答忠实度和 hallucination |
| P1 | MTRAG | 补多轮对话和上下文依赖 |
| P1 | MultiHop-RAG | 补跨文档推理和 metadata |
| P1 | TechQA | 补技术支持/产品文档 |
| P1 | LegalBench-RAG/CUAD | 补合同法务 |
| P2 | KG-RAG-datasets | 小规模多文档长文档实验 |
| P2 | FinRAGBench-V | 金融多模态 |
| P2 | Open RAG Benchmark | 科研 PDF 多模态 |
| P2 | CRAG-MM | 视觉多轮 RAG |
| P2 | RAGBench | RAG eval 框架 baseline |

## 风险清单

1. 许可证风险：多个仓库的 GitHub license 字段为空，数据 license 可能不同于代码 license。正式商用前必须逐个确认。
2. 语言风险：多数数据是英文。中文企业 RAG 必须自建中文金标。
3. 任务错配：RAGTruth 测幻觉，LegalBench-RAG 测检索，FinanceBench 测金融 QA。不要混成一个总分。
4. 数据污染：公开 benchmark 可能进入模型训练语料。报告结果只能作为相对参考，不能当绝对生产能力证明。
5. 模拟数据风险：EnterpriseRAG-Bench 虽然贴企业场景，但仍是模拟公司数据。
6. 成本风险：EnterpriseRAG-Bench 全量文档约 1.26GB 压缩包，索引、embedding、rerank 都有成本。
7. 评测器风险：LLM-as-judge 本身会错，必须保留可审计证据和失败样例。

## 本次没有做的事

- 没有下载全量数据。
- 没有本地索引。
- 没有跑 RAGFlow、Dify 或自研 RAG 系统评测。
- 没有验证 Hugging Face 数据集 license。
- 没有做中文金标样本。

没有验证就不装作验证过。本报告只是数据集选型和落地方案。

## 来源索引

- EnterpriseRAG-Bench GitHub：<https://github.com/onyx-dot-app/EnterpriseRAG-Bench>
- EnterpriseRAG-Bench Hugging Face：<https://huggingface.co/datasets/onyx-dot-app/EnterpriseRAG-Bench>
- EnterpriseRAG-Bench 论文：<https://arxiv.org/abs/2605.05253>
- MTRAG GitHub：<https://github.com/IBM/mt-rag-benchmark>
- MTRAG 论文：<https://doi.org/10.1162/TACL.a.19>
- MTRAG-UN 论文：<https://arxiv.org/abs/2602.23184>
- FinanceBench GitHub：<https://github.com/patronus-ai/financebench>
- FinanceBench 论文：<https://arxiv.org/abs/2311.11944>
- RAGTruth GitHub：<https://github.com/ParticleMedia/RAGTruth>
- RAGTruth 论文：<https://arxiv.org/abs/2401.00396>
- MultiHop-RAG GitHub：<https://github.com/yixuantt/MultiHop-RAG>
- MultiHop-RAG Hugging Face：<https://huggingface.co/datasets/yixuantt/MultiHopRAG>
- MultiHop-RAG 论文：<https://arxiv.org/abs/2401.15391>
- TechQA GitHub：<https://github.com/IBM/techqa>
- TechQA 数据：<https://huggingface.co/datasets/PrimeQA/TechQA>
- TechQA 论文：<https://arxiv.org/abs/1911.02984>
- LegalBench-RAG GitHub：<https://github.com/zeroentropy-ai/legalbenchrag>
- LegalBench-RAG 论文：<https://arxiv.org/abs/2408.10343>
- CUAD GitHub：<https://github.com/TheAtticusProject/cuad>
- CUAD 官网：<https://www.atticusprojectai.org/cuad>
- CUAD 论文：<https://arxiv.org/abs/2103.06268>
- KG-RAG-datasets GitHub：<https://github.com/docugami/KG-RAG-datasets>
- FinRAGBench-V GitHub：<https://github.com/zhaosuifeng/FinRAGBench-V>
- FinRAGBench-V 论文：<https://arxiv.org/abs/2505.17471>
- Open RAG Benchmark GitHub：<https://github.com/vectara/open-rag-bench>
- Open RAG Benchmark 数据：<https://huggingface.co/datasets/vectara/open_ragbench>
- CRAG-MM GitHub：<https://github.com/facebookresearch/CRAG-MM>
- CRAG-MM 数据组织：<https://huggingface.co/crag-mm-2025>
- RAGBench GitHub：<https://github.com/rungalileo/ragbench>
- RAGBench 数据：<https://huggingface.co/datasets/rungalileo/ragbench>
