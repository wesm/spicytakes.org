---
title: "The Open Lakehouse Stack: DuckDB and the Rise of Table Formats06-16"
date: 2025-06-16
url: https://www.ssp.sh/blog/open-table-lakehouse-with-duckdb/
slug: open-table-lakehouse-with-duckdb
word_count: 4764
---

![The Open Lakehouse Stack: DuckDB and the Rise of Table Formats](https://www.ssp.sh/blog/open-table-lakehouse-with-duckdb/featured-image.png)

Contents
This article was written as part of
[my services](https://www.ssp.sh/services)

Wouldn’t it be great to build a data warehouse on top of affordable storage and scattered files? SSDs and fast storage are expensive, but storing data in a data lake on S3 or R2 is significantly cheaper, allowing you to save a greater amount of essential data. However, the downside is that it quickly becomes messy or unorganized, lacking clear governance and rules.


That’s where databases shine, right? They offer numerous helpful features and a SQL interface for interaction. It’s fast and convenient, except that we need to define all schemas and structures before storing (remember the ELT vs. ETL debate, where we have schema on read vs schema on write).


Data lakes with affordable storage and an open table format (Iceberg, Delta, Hudi, Lance) are here to provide database-like features on top of distributed files. They have SQL interfaces, versioning, ACID Transactions, and many more database-like featuresâas we’ll demonstrate with live examples using DuckDB and MotherDuck to query Iceberg tables directly from S3. Additionally, AI-powered workflows such as MCP and Claude explore how lightweight catalogs can make data more accessible than ever before.


So, is that the future of databases or data warehouses, rebuilding database features on cheap storage? It might be. It’s something Databricks, with its Lakehouse architecture, has been promoting for a while. With the further unification of open table formats around Iceberg and the addition of managed Iceberg services by AWS, Cloudflare, and other hyperscalers, this promise is being fulfilled more than ever. Especially with the newer open catalogs such as Unity Catalog, Apache Polaris, and Glue Catalog, we also try to achieve better uniformity and integration through a set of defined APIs to manage access, permissions, or lists of tables in your lake.


This article focuses on why open table formats are all the rage and how they, in combination with DuckDB and MotherDuck, can help us in creating analytical insights.


## What is an Open Table Format?


I have [written extensively](https://www.rilldata.com/blog/the-open-table-format-revolution-why-hyperscalers-are-betting-on-managed-iceberg) about open table formats; therefore, I’ll keep this brief. The most succinct definition I can condense it to:


> Open Table Format bundles distributed files into manageable tables with database-like features. Newer features enhance and facilitate access and data governance, similar to a lakehouse. Consider them an abstraction layer that structures your physical data files into coherent tables.


The primary use cases and benefits include managing large volumes of files in an affordable store for a data lake or enhancing data governance. In both scenarios, table formats can be extremely helpful due to their features.


Unlike data warehouses, where you achieve fast performance by storing hot data on high-performance devices such as SSDs, you store it on inexpensive storage. As DWHs maintain statistics, build efficient access methods such as indexes, and co-optimize, with an open table format you don’t have these options, but features like [Z-ORDER](https://delta.io/blog/2023-06-03-delta-lake-z-order/) and others are attempting this on non-SSDs.


The latest prominent open-source table formats are [Iceberg](https://github.com/apache/iceberg), [Delta Lake](https://github.com/delta-io/delta), [Hudi](https://github.com/apache/hudi), [Paimon](https://github.com/apache/paimon/) and [Lance](https://github.com/lancedb/lance).


### Feature Comparison of Data Lake Table Formats


A quick feature comparison of Apache Iceberg versus other table formats (Delta Lake, Apache Hudi, and Lance) as Databricks bought Tabular, the company behind Apache Iceberg, and is most likely consolidating around Iceberg/Delta:



| Feature Group | Apache Iceberg Advantages | Competition Comparison |
| **Fundamental Capabilities** | â Complete ACID, schema evolution, time travel | Most competitors match basics, Lance has limitations in ACID/schema |
| **Advanced Data Management** | â Hidden partitioning with evolution
â Both CoW and MoR | Delta/Hudi use standard partitioning
All support CoW/MoR except Lance |
| **Performance Features** | â Column statistics for skipping
â Z-order, bin-packing | Similar capabilities across Delta/Hudi, Lance has basic data skipping |
| **Ecosystem & Governance** | â Widest integration
â Apache Software Foundation | Delta: Databricks-focused, Linux Foundation
Hudi: ASF/Uber
Lance: Arrow-focused, newer |



The difference between the open table formats is that **Iceberg and Delta Lake** share many similar capabilities as mature table formats, with Iceberg having stronger hidden partitioning and broader file format support. **Apache Hudi** differentiates itself with native primary key support, making it particularly well-suited for **update-heavy** workloads and **real-time** data ingestion. **Lance**, as the newcomer, focuses explicitly on **ML workloads** with random access performance and built-in vector search capabilities. However, it lacks some of the mature data lake features of the other formats. **Apache Paimon** is emerging as a format specifically optimized for **real-time lakehouse** architecture, combining streaming capabilities with traditional lake format features.


Additionally, the formats try to converge in features, with projects like **[Apache XTable](https://xtable.apache.org/)** (formerly OneTable) and [Universal Format (UniForm)](https://docs.delta.io/latest/delta-uniform.html) working to provide interoperability between Iceberg, Delta, and Hudi formats.

Newcomer
Another, more AI-focused and closed-source option to keep an eye on is
[Bauplan](https://www.bauplanlabs.com/)
.

## Fitting into the Bigger Data Architecture?


But how do open table formats fit into the current data architecture landscape, you might ask?


### Four Foundational Layers + Compute: Open Data Platform Architecture Built on Open Standards and Formats


Generally, data architecture and its data platform, which utilize open table formats and other open-source software, are typically organized into four layers, plus underlying components such as a compute engine, data governance, and automation. The platform begins with the lowest layer, the storage layer, and progresses to the top catalog layer. This is how I see the open platform architecture as of today:

1. **Storage**: The distributed storage where data resides (AWS S3, Cloudflare R2, Azure Blob, MinIO).
2. **File Format**: Optimizes data for analytics using compressed columnar formats like Parquet, ORC, Avro, and DuckDB.
3. **Open Table Format**: Bundles distributed files into manageable database-like tables. Apache Iceberg is becoming the industry standard, with Delta Lake and Apache Hudi also available.
4. **Catalog Layer**: Unifies access and permission rights across your data assets. Solutions include Iceberg Catalog, Polaris Catalog, Unity Catalog, and Glue Catalog. Note that these are not the same as [data catalogs](https://github.com/opendatadiscovery/awesome-data-catalogs).


The data architecture for such a platform can look like this:


![/blog/open-table-lakehouse-with-duckdb/open-data-stack-architecture-v5.jpg](https://www.ssp.sh/blog/open-table-lakehouse-with-duckdb/open-data-stack-architecture-v5.jpg)

*Open Data Platform Architecture based on Open Table Format & on Open Standards | Image by the Author, based onThe Open Table Format Revolution*


The Open Data Stack Architecture consists of four essential layers with interchangeable compute engines serving as the connecting force.


An Open Data Platform architecture combines different layers that are integrated and executed by the compute engine. The **compute layer** is responsible for creating files on S3, creating an Iceberg table, or managing the request for the number of tables sent to the catalog via API. Additionally, it can be replaced with any other engine, making the [open](https://www.ssp.sh/brain/openness) platform, with its [open standards](https://www.ssp.sh/brain/open-standards/), so powerful: [Open Standards over Silos](https://voltrondata.com/codex/open-standards).


#### Undercurrents of the Open Data Platform Architecture


Undercurrent (for lack of a better name) and glue components encompass **compute engines**, data governance and lineage, and operational automation. The compute engine is a critical component, as interchangeable engines (such as Spark, DuckDB, Snowflake, etc.) allow you to process and query data without being locked into any vendor’s ecosystem.


A less obvious but essential undercurrent is **data governance & lineage**; it represents the critical **metadata management** that tracks data origins, transformations, and usage across the stack. This is often overlooked in architectural diagrams but is essential for ensuring the compliance, security, and trustworthiness of the data architecture. And the third is the **automated maintenance operations layer**, which captures automated processes like compaction, snapshot management, and unreferenced file removal that are essential for operational efficiency but frequently omitted from high-level architecture discussions.


## Open Table Catalogs: Avoiding Vendor Lock-in at the Metadata Layer


These are key for unified access and where Hyperscalers battle for their catalog and metastore.


We have several closed and open-source catalogs that are competing at this time, and the question is, can we build one that doesn’t lock us into a single vendor?


The battle has shifted from data processing engines and table formats to the catalog layer. Unlike traditional metastores tightly coupled to specific engines, the new generation of catalogs aims to work across multiple compute platforms. However, as the compatibility matrix below shows, vendor lock-in at the catalog level remains a significant challenge.


As of today, we have mainly these different catalog options - **Open Source Catalogs:**

- **[Apache Polaris Catalog](https://github.com/apache/polaris)**: Fully open source, designed for broad compatibility with Iceberg clients
- **[Iceberg Catalog](https://github.com/apache/iceberg/blob/main/open-api/rest-catalog-open-api.yaml)**: Open source REST API definition as part of Apache Iceberg
- **[Unity Catalog](https://github.com/unitycatalog/unitycatalog) (Databricks)**: Advanced governance features, strong integration with Databricks ecosystem


And **Vendor-Managed Catalogs:**

- **[AWS Glue Catalog](https://docs.aws.amazon.com/prescriptive-guidance/latest/serverless-etl-aws-glue/aws-glue-data-catalog.html)**: Deep AWS integration, serverless metadata management
- **[Snowflake Horizon Catalog](https://www.snowflake.com/en/product/features/horizon/)**: Native Snowflake integration with governance capabilities
- **[BigQuery Metastore](https://cloud.google.com/bigquery/docs/about-bqms)**: Google Cloud native, designed for multi-engine support


If we check the three major open table formats, we see that Unity Catalog supports Delta Lake and also [implements the Iceberg REST Catalog API interface](https://www.databricks.com/blog/open-sourcing-unity-catalog), which is now available rather than just planned. The Iceberg catalog is indeed supported across major platforms where Iceberg is used, including [Snowflake (through Snowflake Open Catalog)](https://docs.snowflake.com/en/release-notes/2024/other/2024-10-18-snowflake-open-catalog-ga) and [AWS (through AWS Glue Data Catalog)](https://aws.amazon.com/blogs/big-data/use-apache-iceberg-in-your-data-lake-with-amazon-s3-aws-glue-and-snowflake/).


### How This Architecture Extends the Lakehouse Concept


The open data platform architecture, with its open table formats, represents the next evolution of or extends the Lakehouse core principle. But what is the difference between this and the [Databricks Lakehouse](https://www.databricks.com/product/data-lakehouse) architecture? Are they the same?


The [2021 Lakehouse](https://www.cidrdb.org/cidr2021/papers/cidr2021_paper17.pdf) illustration combines aspects of data lakes and warehouses with components like BI, streaming analytics, data science, and machine learning on top of a lake:


[

](https://www.ssp.sh/blog/open-table-lakehouse-with-duckdb/lakehouse-compare.webp)Evolution of data platform architectures to today’s two-tier model (a-b) and the new Lakehouse model (c) | Image from [Whitepaper](https://www.cidrdb.org/cidr2021/papers/cidr2021_paper17.pdf)


With these **components of a lakehouse**, such as *[(transactional) metadata](https://www.databricks.com/blog/2019/08/21/diving-into-delta-lake-unpacking-the-transaction-log.html), caching, and indexing layer*:


[

](https://www.ssp.sh/blog/open-table-lakehouse-with-duckdb/lakehouse.webp)Evolution of data platform architectures to today’s two-tier model (a-b) and the new Lakehouse model (c) | Image from [Whitepaper](https://www.cidrdb.org/cidr2021/papers/cidr2021_paper17.pdf)


Lakehouse was open, but the data catalog initially was not open source. As you have to rely heavily on the metadata, you are not vendor-locked; however, it’s challenging to run on your own.


As elaborated above, there are various open-source catalogs, and none are easy to run on your own, as they require some compute engine and deep integration into the platform. The open data platform is yet to be implemented end-to-end, and catalogs are not as unified as the table formats were. So we’ll need to wait before choosing one of the OSS options.


The key is that open data platform architectures are more modular, open, and composable, as each layer is interchangeable, such as the compute engine, table, and file format. In an ideal world, the access layer would be through a standardized REST catalog.


## Reading Iceberg Tables with DuckDB and MotherDuck Directly


How does MotherDuck or DuckDB handle reading table formats? For example, how do we read data from an Iceberg table stored in a data lake on S3/R2?


Let’s make a quick example.


#### Reading Open Table Formats with DuckDB/MotherDuck


We can read the Iceberg tables directly from an object store, such as S3.  Here, I am reading data on my local DuckDB instance from S3 directly:



| ` 1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
` | `â¯ duckdb
D install iceberg;
D load iceberg;
D install https;
D load https;
D .timer on
D SUMMARIZE FROM iceberg_scan('s3://us-prd-motherduck-open-datasets/iceberg/tpcds/iceberg/default.db/call_center',allow_moved_paths = true);
RESULT HERE
âââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
â 31 rows                         12 columns (10 shown) â
âââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
Run Time (s): real 5.093 user 0.073381 sys 0.025548
` |



You can avoid some of the network latency from your local machine to wherever your S3 sits by using MotherDuck; in this case, both are on AWS, so it’s much faster:



| ` 1
 2
 3
 4
 5
 6
 7
 8
 9
10
` | `â¯ duckdb
D attach ':md';
D CREATE OR REPLACE TABLE my_db.tpcds_call_center AS FROM iceberg_scan('s3://us-prd-motherduck-open-datasets/iceberg/tpcds/iceberg/default.db/call_center',allow_moved_paths = true);
Run Time (s): real 4.190 user 0.074477 sys 0.025936
D SUMMARIZE FROM my_db.tpcds_call_center;
RESULT HERE
âââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
â 31 rows                         12 columns (10 shown) â
âââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
Run Time (s): real 0.146 user 0.015458 sys 0.001614
` |



You see, it took `real 0.146` instead of `real 5.093` as before. Remember that I’m located in Europe, so the first query had to go all the way around the world, whereas the second is in the same country. Jacob [demonstrates more examples](https://www.youtube.com/watch?v=FMVgwGh8RQA), like using dbt or materializing an Iceberg table into [Google Sheets](https://duckdb.org/community_extensions/extensions/gsheets.html).


This **keeps the Iceberg tables as a single source of truth** in the data lake, while still allowing for complex analytics with plain SQL.


This tremendously simplifies the work we have to do on the data engineering side; we can **avoid creating denormalization pipelines** and **data duplication** solely for reporting purposes.


## DuckDB as Lightweight Data Lake Access Layer


The next question is: how to read from the catalog layer? Or how to use DuckDB as a lightweight catalog?


### DuckDB, the Reader Tool


One example is DuckDB, a provider of a **lightweight, SQL compute engine** to access and create an interface to data lakes, minimizing download sizes and leveraging object storage for data serving. This is especially useful for sharing open datasets.


Two examples and key insights from both [Tobias’s blog](https://tobilg.com/using-duckdb-databases-as-lightweight-data-lake-access-layer) and [Mehdi’s approach](https://motherduck.com/blog/from-data-lake-to-lakehouse-duckdb-portable-catalog/) are the use of DuckDB VIEWs as a lightweight catalog. The approach works by creating views in a small DuckDB database that points to remote data on cloud storage. For example, you might create a database with views referring to Parquet files on S3:



| `1
2
3
` | `-- Create views pointing to remote data sources
CREATE VIEW agency AS SELECT * FROM read_parquet('https://data.openrailway.dev/providers/gtfs-de/full/agency.parquet');
CREATE VIEW areas AS SELECT * FROM read_parquet('https://data.openrailway.dev/providers/gtfs-de/full/areas.parquet');
` |



You can then save this database locally and attach it at any time, even copy it around, as the resulting database file is typically under 300 KB in size, since it only contains view definitions, not actual data.


You can then upload this file to object storage and share it with users, who can attach it and immediately query the data.


For example, the full database from the above Openrailway data can be attached by simply:



| ` 1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
` | `â¯ duckdb
v1.2.2 7c039464e4
Enter ".help" for usage hints.
Connected to a transient in-memory database.
Use ".open FILENAME" to reopen on a persistent database.
D -- Run this snippet to attach database
D ATTACH 'md:_share/openrailway-lightweight-catalog/d0928dbb-b573-4bce-8dfa-bed62d2ca641' as railway;
100% ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
D use railway;
D select count(*) from routes;
ââââââââââââââââ
â count_star() â
â    int64     â
ââââââââââââââââ¤
â    25178     â
ââââââââââââââââ
` |



This approach makes DuckDB an excellent access layer for data lakes where querying a 32-million-record file takes less than 0.4 seconds. The small database serves as a catalog or entry point, while the actual data is stored in cloud storage. DuckDB intelligently retrieves only the data required via HTTP range requests.


If you use DuckDB as a lightweight catalog, DuckDB excels by:

1. **Providing a unified SQL interface** to multiple data sources and formats
2. **Creating abstraction layers** through views that shield users from complexity
3. **Supporting diverse data formats**, including Parquet, CSV, Iceberg, and others
4. **Enabling cross-format queries** that can join data from various sources


This combines the affordable storage of data lakes with the convenience of SQL querying, all without complex infrastructure.

Bonus: AI Use-Case with MCP: SQL and DuckDB/MotherDuck
Not fully related to open table formats, but as an addition to explore Iceberg tables with MCP-backed capabilities inside Claude, accessing autonomous MotherDuck database and firing queries to validate assumptions and returning a better answer to the prompt at hand, I attached a fun bonus chapter in
**Appendix A**
that goes into details.

## Next Up, Write to a Data Lake


We’ve seen how open table formats, such as Iceberg, Delta, and Hudi, provide powerful database-like features on top of affordable object storage. The Open Data Platform architecture, with its four interchangeable layersâfrom object storage to catalogâcreates a truly composable data ecosystem where each component can be swapped out without vendor lock-in. This modular approach enables us to develop advanced analytics capabilities while retaining data in its native format on affordable storage rather than relying on expensive, proprietary systems.


It is powerful to read directly from open table formats, such as Iceberg, using DuckDB. This approach embodies the principle of **Open Standards over Silos** - instead of loading data into proprietary formats of cloud vendors and getting locked in, we work directly with open standards.


On the other hand, comparing the open data platform to a closed data platform or data warehouse also has its disadvantages. Besides the added complexity and manual data governance that you need to implement, the separation of compute and storage introduces additional latency, which will impact query response times. That’s where an open data stack probably will never compete with a closed ecosystem.


But beyond reading the Iceberg table format from distributed object storage, wouldn’t it be great to write aggregates and insights to an Iceberg table too? That’s where the real power of composable data platforms becomes fully apparent; by reading and materializing on top of Iceberg, we’re getting closer to a fully interoperable data ecosystem. Writing, updating, and managing these tables with the same flexibility and without vendor lock-in?



| `1
2
3
` | `-- Imagine being able to do something like this
CREATE OR REPLACE ICEBERG TABLE my_iceberg_table 
AS SELECT * FROM my_transformed_data;
` |



In the next part, we will focus on writing to a data lake. We’ll explore how to create, update, and manage Iceberg tables directly, completing the circle of a truly open, composable data platform that maintains the single source of truth in your data lake while allowing complex analytics through SQL.


## Appendix


### Appendix A: Bonus: AI Use-Case with MCP: SQL and DuckDB/MotherDuck


With MotherDuck you can create simple to complex data analytical notebooks and performant SQL queries that scale up with your data. It’s even more helpful when you have AI agents with MCP helping you with the SQL writing or producing valuable output analytics for users.


Below is a fun example of how to use AI in SQL or directly in your IDE with MCP.


#### Write SQL with AI


For example, you can [write SQL with AI](https://motherduck.com/docs/key-tasks/writing-sql-with-ai/). If we use our call center table that we created with the `CREATE OR REPLACE TABLE` command on database `my_db` above, we can do something like this:



| `1
2
3
4
5
6
7
8
` | `D use my_db;
D CALL prompt_sql('what are the top managers of my call center?');
ââââââââââââââââââââââââââ
â         query          â
â        varchar         â
ââââââââââââââââââââââââââ¤
â SELECT cc_manager, COUNT(*) AS call_center_count FROM tpcds_call_center GROUP BY cc_manager ORDER BY call_center_count DESC;\n 
ââââââââââââââââââââââââââ
` |



If we run this AI-generated query, we can see that it actually does what we asked for:



| ` 1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
` | `D SELECT cc_manager, COUNT(*) AS call_center_count FROM tpcds_call_center GROUP BY cc_manager ORDER BY call_center_count DESC;
âââââââââââââââââââââ¬ââââââââââââââââââââ
â    cc_manager     â call_center_count â
â      varchar      â       int64       â
âââââââââââââââââââââ¼ââââââââââââââââââââ¤
â Larry Mccray      â                 3 â
â Travis Wilson     â                 3 â
â Wayne Ray         â                 2 â
â Gregory Altman    â                 2 â
â Jason Brito       â                 2 â
â Miguel Bird       â                 2 â
â Jack Little       â                 1 â
â Clyde Scott       â                 1 â
â Ronnie Trinidad   â                 1 â
â Rene Sampson      â                 1 â
â Roderick Walls    â                 1 â
â Charles Hinkle    â                 1 â
â Ryan Burchett     â                 1 â
â Andrew West       â                 1 â
â David Brown       â                 1 â
â Felipe Perkins    â                 1 â
â Bob Belcher       â                 1 â
â Timothy Bourgeois â                 1 â
â Dion Speer        â                 1 â
â Mark Hightower    â                 1 â
â Richard James     â                 1 â
â Alden Snyder      â                 1 â
âââââââââââââââââââââ´ââââââââââââââââââââ¤
â 22 rows                     2 columns â
âââââââââââââââââââââââââââââââââââââââââ
` |



We retrieve the top managers of the call center from our **distributed Iceberg table on S3**. Beautiful, isn’t it?


#### Reading Iceberg Tables with MCP


[Model Context Protocol (MCP)](https://github.com/modelcontextprotocol) is the language protocol between an AI and an IDE. There’s a lot of use cases tossed around lately, and we will also have a quick look at how we can use MCP to read Iceberg tables from an S3.

Quick Recap and MotherDuck's DuckDB MCP
MotherDuck’s DuckDB MCP Server implements a protocol to allow AI assistants likeÂ
[Claude](https://claude.ai/)
, or AI IDEs likeÂ
[Cursor](https://www.cursor.com/)
Â to directly interact with your local DuckDB or MotherDuck cloud databases. It enables conversational SQL analytics without complex setup, letting you analyze your data through natural language conversations.

Following the [initial setup](https://motherduck.com/docs/key-tasks/use-md-with-ai/) with setting up a MotherDuck token and MCP-compatible client. I used Claude Desktop and set up `claude_desktop_config.json`, and I can now ask questions; Claude can then run actual queries against my databases to figure things out.


Let’s try the same example above again with `what are the top managers of my call center?`. First, we need to activate it - if everything is correct, as in stated here, you should see this MCP MotherDuck popping up:


[

](https://www.ssp.sh/blog/open-table-lakehouse-with-duckdb/mcp1.webp)MotherDuck MCP in Claude Desktop


Second, we can ask the same question - notice that I added the name of the database but not the table itself:


[

](https://www.ssp.sh/blog/open-table-lakehouse-with-duckdb/mcp2.webp)MotherDuck MCP in Claude Desktop


We can see that Claude figured out a way to answer my question. It autonomously ran four queries. As you can see also, it’s a different result than we had before. Let’s see which query it ran:


It ran these queries autonomously:



| ` 1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
` | `1. `query`: `SHOW TABLES FROM my_db;`
2. `query`: `SHOW TABLES;`
3. `query`: ` DESCRIBE tpcds_call_center;
4. {
  `query`: `
SELECT 
    cc_name AS call_center_name,
    cc_manager AS manager,
    cc_market_manager AS market_manager,
    cc_employees AS employees
FROM 
    tpcds_call_center
ORDER BY 
    cc_employees DESC;
`
}
` |



What is interesting is that the result this time is different than the first one. If we look at the data with this query `SELECT cc_name AS call_center_name, cc_manager AS manager, cc_market_manager AS market_manager, cc_employees AS employees FROM tpcds_call_center ORDER BY 1, 2, 3 DESC;`:



| ` 1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
` | `âââââââââââââââââââââââ¬ââââââââââââââââââââ¬ââââââââââââââââââââ¬ââââââââââââ
â  call_center_name   â      manager      â  market_manager   â employees â
â       varchar       â      varchar      â      varchar      â   int32   â
âââââââââââââââââââââââ¼ââââââââââââââââââââ¼ââââââââââââââââââââ¼ââââââââââââ¤
â California          â Wayne Ray         â Evan Saldana      â     44682 â
â California          â Wayne Ray         â Daniel Weller     â     22266 â
â California_1        â Jason Brito       â Earl Wolf         â     48033 â
â California_1        â Jason Brito       â Earl Wolf         â     48033 â
â Hawaii/Alaska       â Gregory Altman    â James Mcdonald    â     17687 â
â Hawaii/Alaska       â Gregory Altman    â James Mcdonald    â     17687 â
â Hawaii/Alaska       â Ronnie Trinidad   â Mark Camp         â     55979 â
â Hawaii/Alaska_1     â Travis Wilson     â Peter Hernandez   â     38400 â
â Hawaii/Alaska_1     â Travis Wilson     â Peter Hernandez   â     69020 â
â Hawaii/Alaska_1     â Travis Wilson     â Kevin Damico      â     38877 â
â Mid Atlantic        â Felipe Perkins    â Julius Durham     â     19074 â
â Mid Atlantic        â Mark Hightower    â Julius Durham     â     19074 â
â Mid Atlantic_1      â Charles Hinkle    â Nicolas Smith     â      9026 â
â Mid Atlantic_1      â Clyde Scott       â Ronald Somerville â      9026 â
â Mid Atlantic_2      â Dion Speer        â Gerald Ross       â     67578 â
â Mid Atlantic_2      â Rene Sampson      â Gerald Ross       â     67578 â
â NY Metro            â Bob Belcher       â Julius Tran       â      2935 â
â NY Metro_1          â Jack Little       â Frank Schwartz    â      5832 â
â NY Metro_2          â Richard James     â John Melendez     â     19270 â
â North Midwest       â Larry Mccray      â Matthew Clifton   â     10137 â
â North Midwest       â Larry Mccray      â Gary Colburn      â     34898 â
â North Midwest       â Larry Mccray      â Gary Colburn      â     30618 â
â North Midwest_1     â Miguel Bird       â Paul Mccarty      â     63392 â
â North Midwest_1     â Miguel Bird       â Charles Corbett   â     63392 â
â North Midwest_1     â Timothy Bourgeois â Kim Wilson        â     59506 â
â North Midwest_2     â Andrew West       â Tom Root          â     41932 â
â North Midwest_2     â David Brown       â Luis Gault        â     41932 â
â North Midwest_2     â Ryan Burchett     â Michael Hardy     â     41932 â
â Pacific Northwest   â Alden Snyder      â Frederick Weaver  â      6280 â
â Pacific Northwest_1 â Roderick Walls    â Mark Jimenez      â     62343 â
âââââââââââââââââââââââ´ââââââââââââââââââââ´ââââââââââââââââââââ´ââââââââââââ¤
â 30 rows                                                       4 columns â
âââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
` |



We see that the first iteration with the function `prompt_sql()` counted the rows by managers and market_managers with a `GROUP BY` and the second with MCP printed the data raw (as it only 30 rows) and interpreted the result.


If we analyze even more, manually, we see that the entries in this table actually protocols the history with [SCD2](https://en.wikipedia.org/wiki/Slowly_changing_dimension#Type_2:_add_new_row) and only one row is currently valid. For example, for `Larry Mccray`, the last row has `cc_rec_start_date=2002-01-01` and `cc_rec_end_date=NULL`, meaning only that the last row with `employees=30618` is correct:



| `1
2
3
4
5
6
7
` | `âââââââââââââââââââââââ¬ââââââââââââââââââââ¬ââââââââââââââââââââ¬ââââââââââââ¬ââââââââââââââââââââ¬ââââââââââââââââââââ¬ââââââââââââââââââ¬...â
â  call_center_name   â      manager      â  market_manager   â employees â cc_call_center_sk â cc_rec_start_date â cc_rec_end_date â...â
â       varchar       â      varchar      â      varchar      â   int32   â       int32       â       date        â      date       â...â
âââââââââââââââââââââââ¼ââââââââââââââââââââ¼ââââââââââââââââââââ¼ââââââââââââ¼ââââââââââââââââââââ¼ââââââââââââââââââââ¼ââââââââââââââââââ¼...â¤
â North Midwest       â Larry Mccray      â Matthew Clifton   â     10137 â                 4 â 1998-01-01        â 2000-01-01      â...â
â North Midwest       â Larry Mccray      â Gary Colburn      â     34898 â                 5 â 2000-01-02        â 2001-12-31      â...â
â North Midwest       â Larry Mccray      â Gary Colburn      â     30618 â                 6 â 2002-01-01        â NULL            â...â
` |


My Next Project
Another use case is to help us
[write data pipelines](https://www.youtube.com/watch?v=yG1mv8ZRxcU)
. Instead of guessing the schema or the file types, MCP can directly query the INFORMATION_SCHEMA or request other information from the database interactively.

#### Takeaways from GenAI


So what do we learn? No matter how good GenAI or GenBI is, humans are still irreplaceable in interpreting the results and understanding the domain. However, aside from that, you could also consider providing a better prompt or exploring further with `SUMMARIZE` and verifying if it’s SCD2 (in fact, I did this; see image 1 at the end below for the outcome).


It also shows that the English language is not always precise enough. That’s why SQL is sometimes better to use or to explain to an LLM, so we communicate exactly what we want.


In any case, I hope you can see that both of these AI-powered options are tremendously helpful and a productivity boost for analysts and others. We might even see a decline in dashboard use per se, as self-service analytics is now possible for the first time via chat with the analytics backend.


This means users can ask via chat prompts, and the MCP with a real connection to the database can query and refine its way through the questions. With Claude, you get to see what it is doing. Pretty exciting, right?


One key element here is **speed**. Why speed? Because we can’t wait one minute to get a simple query back, certainly not for customer-facing analytics.  That’s where OLAP systems, such as DuckDB databases, locally or on MotherDuck, shine with their instant query response. Even more so with the recent MotherDuck feature [Instant SQL](https://motherduck.com/blog/introducing-instant-sql/), which returns ad-hoc queries as you type them.

Good to know
While the MCP can connect to MotherDuck, you can also use it without any connection to the Cloud for pure DuckDB actions. Find out more about connecting toÂ
[local DuckDB here](https://github.com/motherduckdb/mcp-server-motherduck?tab=readme-ov-file#connect-to-local-duckdb)
.
Troubleshooting
In case you get the error when starting up Claude that says
and in the debug log with
you find
, please recreate a new token on the MotherDuck UI. Mine was from last year and therefore threw this error.

Image 1: Updated MCP query and now the answer is correct ð.


[

](https://www.ssp.sh/blog/open-table-lakehouse-with-duckdb/mcp4.webp)MotherDuck MCP in Claude Desktop with the Answer


---


```
Full article published at MotherDuck.com - written as part of my services
```

[Discuss on Bluesky](https://bsky.app/search?q=domain%3A%20https://www.ssp.sh/blog/open-table-lakehouse-with-duckdb/)
|
[Logs](https://www.ssp.sh/tags/logs/)
[Motherduck](https://www.ssp.sh/tags/motherduck/)
[Duckdb](https://www.ssp.sh/tags/duckdb/)
[SQL](https://www.ssp.sh/tags/sql/)
[Open Table Format](https://www.ssp.sh/tags/open-table-format/)
[Lakehouse](https://www.ssp.sh/tags/lakehouse/)
[Services](https://www.ssp.sh/tags/services/)
