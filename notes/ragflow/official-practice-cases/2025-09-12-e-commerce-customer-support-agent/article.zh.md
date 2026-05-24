---
title: "教程：使用 RAGFlow 构建电商客服 Agent（中文学习版）"
source_url: "https://ragflow.io/blog/tutorial-build-an-e-commerce-customer-support-agent-using-ragflow"
canonical_url: "https://ragflow.io/blog/tutorial-build-an-e-commerce-customer-support-agent-using-ragflow"
published: "2025-09-12T00:00:00.000Z"
based_on: "article.md"
translation_type: "中文学习版，保留原文结构、关键流程、关键 Prompt 和工程学习笔记，非逐字硬翻"
image_count: 21
---

> 原文：RAGFlow 官方博客《Tutorial - Build an E-Commerce Customer Support Agent Using RAGFlow》  
> 本文件是面向本仓库实践学习的中文译读版。英文原文归档见 [article.md](article.md)，原始 HTML 见 [original.html](original.html)。  
> 配图均已本地化，路径沿用 `images/`。

# 使用 RAGFlow 构建电商客服 Agent

发布时间：2025-09-12  
阅读时长：约 7 分钟

![图 1：电商客服场景](images/01-phonecall-0766db01288954bc13b6d882fa9434de.png)

## 这篇文章到底在做什么

电商零售平台已经大量使用智能客服，但传统客服系统常见问题很直接：能处理固定问答，处理不了更复杂、带上下文的需求。用户可能会问：

- 购买前想比较不同产品型号的功能差异；
- 说明书丢了，需要客服指导某个功能怎么用；
- 家电、家居类产品需要预约上门安装。

这篇 RAGFlow 官方实践文章的方案，是用工作流编排加大模型，把用户问题先做意图分类，再分流到三个客服流程：

1. 产品功能对比；
2. 产品使用指南问答；
3. 上门安装预约信息收集。

编排后的工作流如下：

![图 2：完整客服工作流](images/02-1-779c331885831a1505700ddbabb733fd.PNG)

这个案例的核心不是“让一个 Agent 什么都干”。它更像一个工程化客服流水线：用 `Categorize` 做入口分流，用 `Retrieval` 取知识库材料，用专门的 `Agent` 生成对应答复，最后统一交给 `Message` 返回结果。这个设计更适合客服，因为客服最重要的是稳定、快、可控。

## 1. 准备数据集

### 1.1 创建数据集

示例数据集可从 Hugging Face 下载：`InfiniFlow/Ecommerce-Customer-Service-Workflow`。

![图 3：官方示例数据集](images/03-createdatasets-785f6edd83b5af967230d240fc84e89e.png)

在 RAGFlow 中创建两个知识库：

- `Product Information`：产品信息，用于产品型号、规格和功能对比；
- `User Guide`：用户指南，用于安装、使用、维护和故障排查问答。

然后把对应数据集文档上传到这两个知识库。

### 1.2 解析文档

对于 `Product Information` 和 `User Guide` 这两个知识库，文章选择的是 `Manual` chunking。

![图 4：选择 Manual chunking](images/04-2-3c257b1c60951c35bcb62495b5b0ed9e.PNG)

原因很实际：产品手册通常图文混排，结构复杂，信息密度高。如果只按文本长度切分，很容易把一段说明和对应图片拆开，检索出来的上下文就残了。

RAGFlow 在这里假设文档有层级结构，并使用“最小标题”作为切分单位。这样每个 chunk 尽量保留一个小节里的文字和配图，检索时能拿到更完整的说明。

切分后的用户手册预览如下：

![图 5：用户手册切分预览](images/05-3-748661a1f21a372bafbdc05770d1bc5a.png)

工程上看，这一步是整个方案的地基。客服问答不是只靠 Prompt 变聪明，知识库切分一旦把说明书拆碎，后面的 Agent 只能在坏上下文里猜。

## 2. 构建工作流

### 2.1 创建应用

创建应用后，RAGFlow 会在画布上自动生成 `Begin` 组件。

![图 6：Begin 组件](images/06-1-24759098862a63d926cbbff7d0d18300.jpg)

可以在 `Begin` 组件中配置客服开场白，例如：

```text
Hi! I'm your assistant.
```

![图 7：配置开场白](images/07-4-a934bd0e6db3ba5dd465580100d67064.png)

### 2.2 添加 Categorize 组件

`Categorize` 组件负责意图识别。它会调用大语言模型，根据分类名称、分类描述和示例，把用户输入路由到合适的处理分支。

![图 8：Categorize 组件](images/08-5-e6606e3eb39f725ac5ee06ebe8f36518.png)

这一步的价值很明确：不要让一个通用 Agent 在运行时临时规划所有事情。客服场景里的任务类型相对固定，先分流，再进入专门流程，通常比全交给 Agent 更快、更稳定，也更容易排查问题。

### 2.3 构建“产品功能对比”流程

产品功能对比分支的结构是：

1. `Retrieval` 组件连接 `Product Information` 知识库；
2. 根据用户问题检索相关产品信息；
3. 把检索结果传给 `Feature Comparison Agent`；
4. Agent 生成结构化对比答复。

![图 9：产品功能对比分支](images/09-6-8dea7141c411aeecd4430c759bf725b9.png)

先添加一个名为 `Feature Comparison Knowledge Base` 的 `Retrieval` 组件，并绑定 `Product Information` 知识库。

![图 10：配置 Feature Comparison Knowledge Base](images/10-7-67c9d876eb2081c06596b538fc14263e.png)

然后在 `Retrieval` 后面添加 `Agent` 组件，命名为 `Feature Comparison Agent`。

原文给出的 System Prompt 如下，建议保留这种约束方式：角色清楚、目标清楚、输出要求清楚。

```text
## Role  
You are a product specification comparison assistant.  
## Goal  
Help the user compare two or more products based on their features and specifications. Provide clear, accurate, and concise comparisons to assist the user in making an informed decision.  
---  
## Instructions  
- Start by confirming the product models or options the user wants to compare.  
- If the user has not specified the models, politely ask for them.  
- Present the comparison in a structured way (e.g., bullet points or a table format if supported).  
- Highlight key differences such as size, capacity, performance, energy efficiency, and price if available.  
- Maintain a neutral and professional tone without suggesting unnecessary upselling.  
---
```

User Prompt 配置如下：

```text
User's query is /(Begin Input) sys.query   
  
Schema is /(Feature Comparison Knowledge Base) formalized_content
```

这里有两个关键输入：

- `/(Begin Input) sys.query`：用户原始问题；
- `/(Feature Comparison Knowledge Base) formalized_content`：产品信息知识库检索出的结构化内容。

配置完成后的 Agent 如下：

![图 11：Feature Comparison Agent 配置结果](images/11-8-8af39f9b308da4a392308ded2a4f3479.png)

工程学习点：这个 Agent 不负责检索，也不负责判断用户意图。它只拿“用户问题 + 产品信息上下文”做对比答复。职责边界越清楚，输出越容易稳定。

### 2.4 构建“产品使用指南”流程

产品使用指南分支的结构和上一节类似，只是知识库换成 `User Guide`，Agent 的任务从“比较产品”变成“指导用户操作”。

![图 12：产品使用指南分支](images/12-9-6f1dd2765a9fa64b4b00d4774a2202b1.png)

先添加一个名为 `Usage Guide Knowledge Base` 的 `Retrieval` 组件，并绑定 `User Guide` 知识库。

![图 13：配置 Usage Guide Knowledge Base](images/13-10-ab7aca5218811a68c33f359583e7b40f.png)

然后在 `Retrieval` 后添加 `Agent` 组件，命名为 `Usage Guide Agent`。

原文给出的 System Prompt 如下：

```text
## Role  
You are a product usage guide assistant.  
## Goal  
Provide clear, step-by-step instructions to help the user set up, operate, and maintain their product. Answer questions about functions, settings, and troubleshooting.  
---  
## Instructions  
- If the user asks about setup, provide easy-to-follow installation or configuration steps.  
- If the user asks about a feature, explain its purpose and how to activate it.  
- For troubleshooting, suggest common solutions first, then guide through advanced checks if needed.  
- Keep the response simple, clear, and actionable for a non-technical user.  
---
```

User Prompt 配置如下：

```text
User's query is /(Begin Input) sys.query   
  
Schema is / (Usage Guide Knowledge Base) formalized_content
```

配置完成后的 Agent 如下：

![图 14：Usage Guide Agent 配置结果](images/14-12-5d825a21aa6f1659e185b98ba676fefc.png)

工程学习点：使用指南类回答要避免大段泛泛解释。Prompt 里明确要求 step-by-step、simple、clear、actionable，这是客服产品里更实用的输出约束。

### 2.5 构建“安装预约”助手

安装预约分支不需要知识库检索，重点是多轮对话收集信息。文章要求 Agent 收集三项关键信息：

1. 联系电话；
2. 期望安装时间；
3. 安装地址。

创建一个名为 `Installation Booking Agent` 的 Agent 组件，并配置 System Prompt：

```text
# Role  
You are an Installation Booking Assistant.  
## Goal  
Collect the following three pieces of information from the user   
1. Contact Number    
2. Preferred Installation Time    
3. Installation Address    
Once all three are collected, confirm the information and inform the user that a technician will contact them later by phone.  
## Instructions  
1. **Check if all three details** (Contact Number, Preferred Installation Time, Installation Address) have been provided.  
2. **If some details are missing**, acknowledge the ones provided and only ask for the missing information.  
3. Do **not repeat** the full request once some details are already known.  
4. Once all three details are collected, summarize and confirm them with the user.
```

User Prompt 配置如下：

```text
User's query is /(Begin Input) sys.query
```

配置完成后的 Agent 如下：

![图 15：Installation Booking Agent 配置结果](images/15-14-d585bb03421aa50fe0126315c7262a46.png)

如果业务需要真正登记用户信息，可以在这个 Agent 后面接一个 `HTTP Request` 组件，把收集到的信息写入 Google Sheets、Notion 或企业自己的工单系统。文章只说明这个扩展方向，没有展开实现细节。

![图 16：可选 HTTP Request 扩展](images/16-15-f68768593ca28b5df257c905c74703a4.png)

工程上这一步要小心。电话号码、地址、预约时间都属于敏感业务数据，真正落库或调用外部系统前，至少要做字段校验、用户确认和失败重试。别让 Agent 自己“差不多理解了”就直接写生产系统。

### 2.6 添加回复消息组件

三个分支最终共用一个 `Message` 组件。它接收各个 Agent 的输出，并把处理后的结果展示给用户。

![图 17：统一 Message 组件](images/17-17-7bce84da2f8ff4efad8b0a9f1f782d4a.png)

这个设计很朴素，但好用。入口用 `Categorize` 分流，出口用 `Message` 统一返回，中间每条分支只处理自己的任务。流程可读性比一个大 Agent 自己规划所有步骤强得多。

### 2.7 保存并测试

保存工作流后，按下面路径测试：

```text
Save -> Run -> View Execution Result
```

当用户询问产品型号和功能差异时，系统能返回产品对比结果：

![图 18：产品功能对比测试结果](images/18-18-277206e585a8e9257bf55a46de58e1f4.png)

当用户询问使用方法时，系统能返回对应操作指导：

![图 19：使用指南测试结果](images/19-19-399796e7a1fbcd5e5ed83382a622479b.png)

当用户预约安装时，系统能收集并确认必要信息：

![图 20：安装预约测试结果](images/20-20-ba0a95f26685de5453a3626769eb3ae4.png)

这三个测试覆盖了这个工作流的主要路径：知识库检索型回答、说明书指导型回答、多轮信息收集型回答。

## Summary

文章最后有一个关键判断：这个用例当然也可以用更完整的 Agent workflow 实现，而且 Agent 在复杂问题上更灵活。但 Agent 往往会主动规划和反思，带来明显的响应延迟。对于电商售后客服这种任务边界相对清楚、响应速度要求高的场景，全靠 Agent 未必划算。

RAGFlow 也提供过 Deep Research 多 Agent 框架，相关模板可以在模板库中找到。

![图 21：模板库中的相关工作流](images/21-21-27f2cbec898c99199f40770bf0c3e9f4.png)

这篇文章的客服工作流只覆盖了电商中的一部分场景。类似方法还可以扩展到用户评论分析、个性化邮件营销、售后工单归类、退换货咨询等任务。

## 工程学习笔记

这篇案例最值得学的不是某个 Prompt，而是工作流边界：

1. **先分类，再处理**：客服场景里的任务类型通常稳定，`Categorize` 比让 Agent 自己猜流程更实用。
2. **知识库分开建**：产品规格和用户手册不是同一种材料，分成 `Product Information` 和 `User Guide` 更利于检索和调试。
3. **Agent 职责要窄**：对比 Agent 只做对比，指南 Agent 只做操作指导，预约 Agent 只收集字段。不要让一个节点承担所有业务。
4. **Prompt 要约束输出行为**：比如“如果型号未指定就追问”“优先常见故障排查”“缺什么只问什么”，这些比泛泛地说“请专业回答”有用。
5. **对外写入要谨慎**：HTTP Request 接工单、表格或 CRM 是真实生产能力，但必须加确认、校验和错误处理。
6. **不要迷信多 Agent**：客服不是论文 demo。用户要的是快、准、稳定。任务简单时，工作流编排通常比复杂 Agent 更合适。

核心判断很简单：这个案例值得作为 RAGFlow 工作流入门样板。它没有搞复杂的多 Agent 炫技，而是把客服问题拆成稳定的分支，再在每个分支里用检索和专用 Agent 解决具体问题。这是好品味。
