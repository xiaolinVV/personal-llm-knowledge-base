---
title: "Implementing Text2SQL with RAGFlow"
source_url: "https://ragflow.io/blog/implementing-text2sql-with-ragflow"
canonical_url: "https://ragflow.io/blog/implementing-text2sql-with-ragflow"
published: "2024-09-24T00:00:00.000Z"
fetched_at: "2026-05-24T03:36:53.094305+00:00"
image_count: 10
---

> Source: [Implementing Text2SQL with RAGFlow](https://ragflow.io/blog/implementing-text2sql-with-ragflow)
>
> 本文件是为本仓库学习实践保存的本地归档版；图片已改写为本地相对路径。

# Implementing Text2SQL with RAGFlow

Sep 24, 2024 · 5 min read

[RAGFlow](https://github.com/infiniflow/ragflow) introduces the Text2SQL feature in response to community demand. Traditional Text2SQL requires model fine-tuning, which can significantly increase deployment and maintenance costs when used in enterprise settings alongside RAG or Agent components. RAGFlow’s RAG-based Text2SQL leverages the existing (connected) large language model (LLM), enabling seamless integration with other RAG/Agent components without the need for additional fine-tuned models.

![Figure 1](images/01-station-a92e7bed192fa8144999da5fdc0c15ec.jpg)

The following pipeline explains how to implement Text2SQL capabilities based on RAG:

![Figure 2](images/02-text2sql-77424b18f5c0e9bd41816d7ec3eb79b8.png)

General speaking, you need to prepare a knowledge base for generating Text2SQL prompts, which contains various examples of natural language being converted to SQL statements. A user query is first sent to this knowledge base to retrieve similar examples. The retrieved examples are then concatenated into prompts for the LLM to generate the final SQL statement. The generated SQL is used directly to query the database. If the returned result is incorrect or if, even worse, nothing is retrieved, the generated SQL will be considered incorrect, and the LLM will be called again to regenerate a SQL statement until the predefined upper limit is reached.

Therefore, Text2SQL relies on multiple rounds of orchestration. RAGFlow encapsulates this Text2SQL feature into a convenient, built-in Agent component. In upcoming releases, we plan to adjust this workflow. The goal is to enable users to manually add or update text2SQL examples in the knowledge base, as indicated by the dashed arrow above.

## A Text2SQL demonstration

![Figure 3](images/03-dialogue-b91ce899b0d24687a40ae031975db675.gif)

## Using Text2SQL in RAGFlow

Following is a guide on how to use Text2SQL in RAGFlow:

### 1. Create an agent from template

![Figure 4](images/04-create_from_template-ec16788828f57985b3f2fb7eb21db841.png)

![Figure 5](images/05-choose_template-30c2ea5909ee9b2be040d7b750d97538.png)

### 2. Configure knowledge bases

In the provided **DB Assistant** template, RAGFlow uses three types of knowledge bases to ensure the performance of Text2SQL:

* The **DDL** knowledge base
* The **Q->SQL** knowledge base
* The **Database description** knowledge base

![Figure 6](images/06-agent_template-3679c191bfe410e1c0759bea6ee6b55e.png)

The **DDL** knowledge base: An LLM requires accurate DDL (Data Definition Language) data to generate SQL statements, such as table structures and field information. The DDL knowledge base holds the correct DDL data for effective database querying. The recommended configurations for parsing the DDL knowledge base are as follows:

![Figure 7](images/07-ddl_kb-b2dd896117576630f2312bed0c27d55d.png)

Example: <https://huggingface.co/datasets/InfiniFlow/text2sql/tree/main>

The **Q->SQL** knowledge base: During the Text2SQL process, providing the LLM with samples of natural languages and their corresponding SQL statement pairs can enhance the quality of generated SQL statements. The Q->SQL knowledge base stores such pairs. The recommended configurations for parsing the Q->SQL knowledge base are as follows:

![Figure 8](images/08-q2sql_kb-29007b17b69290fce8513822eebd80d2.png)

Example: <https://huggingface.co/datasets/InfiniFlow/text2sql/tree/main>

The **DB Description** knowledge base: This knowledge base contains accurate information about the queried database, including but not limited to the meanings of database tables and the significance of different fields within those tables. With detailed descriptions from the database, the large language model can more accurately convert user questions into SQL statements. It is recommended to configure the DB Description knowledge base parsing settings as follows:

![Figure 9](images/09-db_description_kb-a287958398fb2c016059db462fa1a0d0.png)

Example: <https://huggingface.co/datasets/InfiniFlow/text2sql/tree/main>

### 3. Configure the database

1. Configure the required parameters for the database in the **Execute SQL** component, including:
   * Database type (currently supports MySQL, PostgresDB, and MariaDB)
   * Database name
   * Database username
   * Database IP address
   * Database port number
   * Database password

![Figure 10](images/10-configure_db-78bb8566bc711c39d5e58d00e904efda.png)

2. After completing the configuration, click the **Test** button to check if the connection is successful.
3. Configure the **Loop** parameter:

Text2SQL in RAGFlow features automatic reflection capabilities. If the generated SQL is deemed capable of querying correctly, the results will be returned directly. However, if the query fails, RAGFlow’s Text2SQL will automatically correct the SQL statement based on the error information returned from the database and retry the query. This process — query failure, correction of the SQL statement, and retry — will continue iterating until it reaches the maximum limit set by the Loop parameter. If this maximum is reached, the Text2SQL process will terminate, prompting the user to optimize their question or knowledge base data before attempting again.

4. Configure **TopN**:
   *This parameter limits the number of records returned in a query, as queries often involve records.*

### 4. Try out Text2SQL

Click **Run** to execute the operation.

## Troubleshooting

### `Database Connection Failed`

Failed to connect to the database. To solve this issue:

1. Click the **Execute SQL** component to ensure all parameters are correctly set.
2. Double check if the machine deploying RAGFlow can connect to the database using the provided information.
3. Click **Test** to check if the database connection is successfully established.

### `SQL statement not found!`

The user query cannot be converted into a SQL statement, primarily due to insufficient or incomplete knowledge bases. It’s recommended to expand the three mentioned knowledge bases.

### `No record in the database!`

The SQL query failed to retrieve any records from the table, either because the filtering condition is excessively restrictive or because the table itself contains no data.

### `Maximum loop time exceeds. Can’t query the correct data via SQL statement.`

The generated SQL statement cannot accurately query the database. Please check the following:

* Ensure the database contains the relevant data.
* Verify that the user question is appropriate.
* Confirm that the SQL statements generated by the **Generate SQL Statement LLM** and **Fix SQL Statement LLM** components are correct.
