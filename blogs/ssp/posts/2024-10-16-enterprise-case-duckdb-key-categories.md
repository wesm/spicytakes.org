---
title: "The Enterprise Case for DuckDB: 5 Key Categories and Why Use It"
date: 2024-10-16
url: https://www.ssp.sh/blog/enterprise-case-duckdb-key-categories/
slug: enterprise-case-duckdb-key-categories
word_count: 3060
---

![The Enterprise Case for DuckDB: 5 Key Categories and Why Use It](https://www.ssp.sh/blog/enterprise-case-duckdb-key-categories/featured-image.png)

Contents
This article was written as part of
[my services](https://www.ssp.sh/services)

DuckDB has a significant share1Â and is frequently featured in the latest data engineering news. However, it’s still in its early adopter phase and has yet to be adopted by larger enterprises. Sure, all data creators and startups have used and potentially grown to love DuckDB, but is it also suitable for enterprises?


What about scaling out and sharing it with others in the organization? Isn’t it only a database file? And why would anyone in a large enterprise adopt DuckDB? In this article, we’ll discuss five key use cases, categorize them, and highlight the unique advantages of an enterprise using DuckDB.


## What is DuckDB?


If you haven’t heard of DuckDB or cannot allocate its application, the simple matrix below as anÂ **analytical**Â andÂ **embedded database**Â might help.



|  | *Transactional* | *Analytical* |
| *Embedded* | SQLite | **DuckDB** |
| *Stand-alone* | Oracle, MS SQL, Postgres, MySQL | Cloud DWHs: BigQuery, Snowflake, Redshift
Modern OLAP: Druid, ClickHouse, Pinot, Starrocks |



Table Matrix inspired byÂ [Oliver Molander in Better Programming](https://betterprogramming.pub/duckdb-whats-the-hype-about-5d46aaa73196)


Think of it as SQLite for analytics workloads but with a fast columnar-**vectorized**Â query execution engine. This is the opposite of a row-oriented relational database where you select all data in a row or nothing.


In simple terms, DuckDB is an in-process SQL OLAP database management system with extensive support for SQL. Each database is a single file, though it doesn’t have to be. DuckDB is simple to install, as it’s a single binary of around ~20 MB. According toÂ [Compiled and Vectorized Queries](https://www.vldb.org/pvldb/vol11/p2209-kersten.pdf), vectorized databases like DuckDB achieve high performance by processing data in batches, amortizing interpretation overhead, and enabling efficient use of CPU caches and SIMD instructions.


Similar to traditional OLAP Cubes (SSAS, SAP BW) or modern OLAP Systems (ClickHouse, Druid, Pinot, Starrocks), it only contains a single or no file when used with theÂ **zero-copy layer**. One use case of DuckDB could be to read a bunch of CSVs or Parquets, transform it, and store it somewhere else and have used it only as a compute engine.


It can handle large amounts of data locally. It’s a much smaller and lighter version of modern OLAP systems. Some even sayÂ [Big Data Is Dead](https://motherduck.com/blog/big-data-is-dead/)Â ð. What is big, anyway? According toÂ [Redshift Files](https://motherduck.com/blog/redshift-files-hunt-for-big-data/), anything over 10 TB.


DuckDB is designed to work as an embedded library, eliminating the network latency you usually get when talking to a database. The latest trend, using it inside the browser to save the roundtrips, isÂ [WASM](https://en.wikipedia.org/wiki/WebAssembly).


In summary, it boils down to an innovative in-process analytical database management system that combinesÂ **simplicity, portability, and high performance**. It solves the need for efficient data analysis on local machines without the complexity of traditional database setups and is highly developer-friendly. But what are these flexible and portable use cases?


## When: Typical Use Cases for DuckDB


That sounds good, but when do you use DuckDB?


I’m glad you asked. This is not all that simple to explain and can be confusing. DuckDB is highly flexible in that there is no one-size-fits-all category. Although DuckDB fits into the analytical and stand-alone square, it has the capabilities of other boxes and many beyond.


The questions are usually:

- Is DuckDB like Snowflake? Not really.
- Is DuckDB like PostgreSQL? No, no, cousins, maybe?
- Is DuckDB like Pandas? It’s complicated.
- Is DuckDB like SQLite? Yes, no!
- Is DuckDB like Apache Spark? Interesting.


Here are five key categories that highlight DuckDB’s use cases:


The table below highlights DuckDB’s versatility and examines each category in more detail to better understand its composition and what interesting use cases for large enterprises can be.



| **Category** | **Description** |
| **Fast (Browser-based) Analytics & Dashboarding - Interactive Data Apps** | - Enables ultra-fast analytical use cases on local machines (e.g., analyzing 1.5 billion rows of taxi data on a laptop)  
- Enables fast and responsive data visualization and exploration used in tools like MotherDuck, Rill Developer, Evidence, and Observable Framework  
- Brings data to users, reducing latency enabling high-performance queries, and running a full-blown analytics engine within a browser using WebAssembly (WASM)  
- Works even on Android phones, providing local file system access |
| **Data Pipeline Compute & Data Wrangling and Preprocessing - On-Demand Pipeline Compute Engine** | - Single binary with no dependencies, suitable for use in AWS Lambda  
- Faster startup times compared to traditional databases  
- Strong data wrangling and preprocessing capabilities for transformation before importing to a data warehouse or OLAP system  
- Flexible extension mechanism for custom data types, functions, and file formats  
- Enables integration with existing data ecosystems and tools |
| **Single File Analytical DB & Local Development and Testing - Lightweight SQL Analytics Solution** | - Local DB, Small Data Stack and simplifying deployment, maintenance, and integration compared to traditional DBMS  
- Strong DuckDB file format: Handles bulk updates and schema changes (e.g., adding columns) in a columnar style and supports transactional changes without losing performance  
- Run tests with dbt or SQLGlot models locally on DuckDB for testing before running in production with cloud data warehouses or data diffs: performing quick comparisons  
- Saving compute & infrastructure costs with optimized performance and enabling local development and testing  
Free and open-source, reducing licensing costs for enterprises |
| **Fast Universal Data Processor - Zero-Copy SQL Connector** | - Acts as an SQL data virtualization wrapper on top of Parquet, CSV, and JSON files in S3 or Postgres DB using a zero-copy mechanism  
- Used for lazy & efficient aggregation, data exploration, and wrangling in memory with common formats (CSV, JSON, Parquet, etc.). Results can be stored as Parquet files back to the data lake or cloud warehouse  
- Acts as a query engine planner (such as notebooks with Python), and allows for the materialization and composition of SQL queries  
- Handles data type parsing, delimiters, and column names under the hood  
- Query interface on top of your data lake file formats or table formats  
- Highly portable across operating systems and CPU architectures  
- Suitable for diverse enterprise environments, from edge devices to large servers  
- Provides APIs for multiple programming languages, facilitating integration |
| **Secure and Compliant Data Processing - Secure Enterprise Data Handler** | - Embedded operation keeps data within the process, enhancing security  
- Open-source nature allows for code audits and compliance checks  
- MIT License provides flexibility for enterprise use and modification  
- Supports transactional guarantees (ACID properties) for data integrity |



In summary, we have these five prominent use cases with the featured characteristics of each category respectively.

- **Interactive Data Apps**Â - Embeddable
- **On-Demand Pipeline Compute Engine**Â - High-performance SQL workflows
- **Lightweight SQL Analytics Solution**Â â Single-node compute engine
- **Secure Enterprise Data Handler**Â - Enhanced security
- **Zero-Copy SQL Connector**Â - Federated query engine


This goes along with theÂ [recent DuckDB survey](https://duckdb.org/2024/10/04/duckdb-user-survey-analysis.html)Â with 500+ community users which says:

- Users often run DuckDB on laptops, but servers are also very popular.
- The most popular clients are theÂ **Python API**Â and the CLI client.
- Most users don’t have huge data sets, but they greatly appreciate high performance.
- Parquet is the most used file format, CSV second and JSON third.
- Users would like performance optimizations related to time series and partitioned data.
- DuckDB is popular among data engineers, analysts, scientists, and software engineers.


They like the high performance, file format support, and ease of use. These fit nicely in our determined categories, such as extensible analytics, zero-copy SQL connector, or interactive. However, only a few use the enhanced security capability it provides as a single binary or see the cost benefits as a significant argument.


Not many other databases can handle such a broad range of use cases, so it’s hard to explain DuckDB to someone new. I’m sure you’ve encountered many of the above cases and maybe even use them daily. Let’s explore just two of these categories to understand their benefits with concrete examples.


### Simple Data Pipeline Engine


As data engineers, we must quickly explore andÂ **wrangle**Â the data. Whether data wrangling on our laptops, pre-processing, or computing as part of a data pipeline, we typically fix some timestamps, correct spelling errors, and aggregate some metrics for a management report. That means we get some CSVs, Excels, or JSONs and put them into a dashboard.


As easy as this sounds, loading CSVs and precisely correcting data types isÂ *still*Â not a solved problem in 2024. It still involves a lot of manual steps, and as we depend on upstream data, it may fail with newer/changed data.


DuckDB helps us here tremendously. It has some of the fastest and most convenient data readers. For example, reading a CSV is as simple as:



| `1
2
3
4
5
` | `SELECT *  
FROM read_csv('flights.csv',
		  delim   = '|',
		  header  = true,
		  columns = { 'FlightDate': 'DATE', 'UniqueCarrier': 'VARCHAR'});
` |



Or read all parquet files with a pattern `SELECT * FROM 'test/*.parquet';`, or read directly from S3:



| `1
2
3
4
5
6
7
` | `CREATE SECRET my_secret (
    TYPE S3,
    KEY_ID 'my_secret_key',
    SECRET 'my_secret_value',
    REGION 'my_region'
);
SELECT * FROM "s3://some-bucket/that/requires/authentication.parquet";
` |



Or an example with Python:



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
` | `from duckdb.experimental.spark.sql import SparkSession as session
from duckdb.experimental.spark.sql.functions import lit, col
import pandas as pd

spark = session.builder.getOrCreate()

pandas_df = pd.DataFrame({
    'age': [34, 45, 23, 56],
    'name': ['Joan', 'Peter', 'John', 'Bob']
})

df = spark.createDataFrame(pandas_df)
df = df.withColumn(
    'location', lit('Seattle')
)
res = df.select(
    col('age'),
    col('location')
).collect()
` |



DuckDB abstracts away most of the tedious process. And we can as also write data directly to Postgres:



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
v1.1.1 af39bd0dcf
Enter ".help" for usage hints.
D INSTALL postgres;
D LOAD postgres;

D ATTACH 'dbname=my-db user=postgres password=postgres host=host.docker.internal port=5444' AS pg_db (TYPE postgres);
D select count(*) from dm.source_table;
ââââââââââââââââ
â count_star() â
â    int64     â
ââââââââââââââââ¤
â      3584412 â
ââââââââââââââââ
D CREATE TABLE pg_db.target_table AS SELECT * FROM dm.source_table;
100% ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
` |



This is just the beginning. With its advanced SQL support, ACID compliance, and integration of all significant data engineering and data science tools, DuckDB is highly feature-rich. Think of it as the Swiss army knife of data engineers. With extensions, you can flexibly expand on these features, evenÂ [build your own](https://github.com/duckdb/community-extensions).

Federated Query, zero-copy and powerful High-Performance SQL Workflows

To name a few, it integrates natively with Delta Lake, PRQL, Pandas, Numpy, and Polars and is interoperable between different data frames and file and table formats. All of it is open-source and released under the MIT License, which makes it freely available and open for enterprises to use.


![test](federated-query.webp)

*Illustration of how DuckDB serves as a zero-copy layer between your data | Image fromDuckDB Beyond the Hype - by Alireza Sadeghi.*

Querying Analytics Data from Postgres
It became even more accessible to perform analytics queries on Postgres withÂ
[pg_duckdb](https://github.com/duckdb/pg_duckdb)
. Turning a relational database into an analytical one is also calledÂ
[HTAP (Hybrid Transaction and Analytics Processing databases)](https://en.wikipedia.org/wiki/Hybrid_transactional/analytical_processing)
.

### Interactive Data Apps (Embedded)


Here’s another example of interactively reading a 513 MB parquet file with ~20 mio rows (`fhvhv_tripdata_2023-05.parquet`) joined with Taxi Zones (`taxi_zone_lookup.csv`).


![](https://www.ssp.sh/blog/enterprise-case-duckdb-key-categories/rill-example.gif)

*Rill Example with NYC dataset*


Rill utilizes DuckDB’s speed and exploration on the fly, showcasing its ability to handle already “big” data sets such as theÂ [NYC dataset](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page). Find more examples later.


## Why DuckDB in an Enterprise?


Can a larger enterprise with thousands of employees also benefit from DuckDB? Don’t enterprises typically use larger, distributed cloud solutions? Yes, but maybe not all the time.


In an enterprise, you usually build dashboards, requiring (sub-) second response times; these are typicalÂ **analytical OLAP workloads**. OLAP systems typically cost developers time and computer resources (especially RAM).


Various systems used across the organization spread heterogeneous data sources throughout different regions, countries, or departments. They might be decentralized, with a small Excel here, another access there, or huge BigQuery solutions there. One thing all of these need isÂ **testing and fixing data**.


TheÂ **computational**Â cost of such tests is usually expensive as the same queries are run repeatedly. A single-node orÂ [Single-Compute Lakehouse](https://dipankar-tnt.medium.com/hudi-rs-with-duckdb-polars-daft-datafusion-single-node-lakehouse-347ee1a45371)Â like DuckDB can save us a lot of time and cloud costs. Running these tests simply on a cheap machine can alsoÂ **save a lot of money**.


It’s simple because there’s no need for Docker or any long-running process; it’s just a simple binary with one line to install. Also, remove compute for countless hours of development and testing that you can outsource from the cloud to a tool running locally or within your pipeline, allowing efficient data transformation before even importing to the data warehouses or OLAP cube.


**Simplify**. Replace Apache Spark with DuckDB where possible. Spark is a complex setup, even more so for tuning and debugging. A quick setup can also improve decision-making speed, as it doesn’t need a huge buy-in from upper management, and you can quickly create a POC with little time/money. It also eases deployment in cloud environments (e.g., AWS Lambda or MotherDuck) and enhances data preprocessing workflows.


Besides saving cloud upfront costs and compute resources, simplifying theÂ **data infrastructure**Â stack can save time and capital. If the simplified architecture does not offer enough features for production, for example, it at least boosts development investments, testing data models before production, and gaining insights and understanding of your business.


This is supported by the zero-copy SQL Connector that delivers fast universal data processing and acts like an SQL wrapper on various file formats and databases. Like data virtualization solutions, but within a single binary. A quick exploration of your data lakes and cloud warehouse, identifying new data science or ML use cases, for example, allÂ **without data movement**Â (quick, cheap, and fast).


Another less-known advantage isÂ **security**. As DuckDB can be embedded into data operations, all compute is done within the existing process. Think of an Airflow task that runs on Kubernetes; there is no need for additional compliance. That helps your enterprise with the ever-growing data protection regulations. You could even process sensitive data without copying or moving data elsewhere.


### DuckDB vs. Common Enterprise Analytics Solutions


An everyday use case involves using a prominent cloud provider such as Amazon, Microsoft, or Google, which offers many tools.


The common data solutions these days:

- Enterprise BI tools2Â (e.g., Tableau, Power BI) with various deployment options (cloud, on-premises, or hybrid), often integrated with cloud platforms (e.g., Microsoft Fabric, SAP HANA)
- Closed-source data platforms (e.g., Ascend.io, Palantir Foundry, Keboola)
- Open data stacks / Modern data stacks with open-source tools


DuckDB can serve as a powerful complementary tool in these data solutions, enhancing their capabilities and addressing some limitations you might face in the above scenarios.

- **With enterprise BI tools:**Â DuckDB is a high-performance local or embedded processing engine that complements both cloud and on-premises deployments. It can enhance data preparation and exploration speed, potentially reducing the load on primary data sources and improving interactive analytics performance.
- **Alongside closed-source platforms:**Â DuckDB provides a flexible, open-source alternative for specific analytical tasks, potentially lowering costs and reducing vendor lock-in.
- **In open data stacks:**Â DuckDB shines as a lightweight yet powerful component, excelling in data wrangling, ETL processes, and ad-hoc analysis without complexity.


By leveraging DuckDB as a complementary tool, enterprises can address limitations in their current setups while maintaining flexibility and potentially reducing costs, regardless of their chosen deployment model.


However, it can enable newer data architecture, which is only possible now with the 1.5-tier architecture.


### New 1.5-Tier Architecture


The 1.5 data architecture,Â [introduced](https://www.cidrdb.org/cidr2024/papers/p46-atwal.pdf)Â by MotherDuck, is a newer architecture than the more commonly known three-tier architecture or other multi-tier architecture. Compared to the more classical tier architecture, this requiresÂ **fewer intermediate operations**Â between the presentation, the data app, and the underlying database or data tier.


The same DuckDB engine runs in the user’s web browser and the cloud. Developers can move the data closer to the application or user, making the analytical experience magnitudes faster as you save the roundtrips from the client to the server and do not move data over the network. This type of architecture is only possible with MotherDuck[2](https://motherduck.com/blog/duckdb-enterprise-5-key-categories/#fn2)Â .


![/blog/enterprise-case-duckdb-key-categories/1-5-architecture-motherduck.webp](1-5-architecture-motherduck.webp)

*Illustration 1.5 Tier Architecture with MotherDuck*


Advantages of 1.5 tier architecture over 3 tier:

- Avoid potential cloud compute
- Improve UX (mostly speed with less network traffic and latency)
- Simpler setup to populate new data


Compared to a classical data app architecture, usually theÂ [3-Tier Architecture](https://en.wikipedia.org/wiki/Multitier_architecture#Three-tier_architecture), it has three main layers: 1. Presentation Layer, 2. Application and 3. Data Tier. This looks something like:


![/blog/enterprise-case-duckdb-key-categories/1-5-architecture.webp](1-5-architecture.webp)

*Classical Data App Architecture (three tier)*


## What’s Next


DuckDB stands out as a fast, user-friendly, and increasingly powerful database thatâs reshaping analytics across various domains. Originally viewed as a niche solution, DuckDBâs unique speed, simplicity, and hybrid architectureâespecially with innovations like MotherDuckâare pushing it into the spotlight as the Swiss army knife for data engineers, scientists, and analysts alike.


DuckDB offers significant benefits for enterprises: reduced infrastructure costs, simpler deployment, and the ability to run complex analytics directly on local machines or embedded in applications. Its high performance, particularly in handling large data sets without network latency, makes it a compelling alternative for organizations seeking faster insights without the overhead of traditional cloud-based or distributed systems.


InÂ **[Part II](https://www.ssp.sh/blog/duckdb-in-production/)**, weâll exploreÂ **15+ Companies Using DuckDB in Production: A Comprehensive Guide**Â across industries, showcasing how companies leverage DuckDB to tackle their most complex data challenges.


---


```
Full article published at MotherDuck.com - written as part of my services
```


---

1. Started in 2018 and released 1.0 in June 2024. It has 6 million Python client downloads per month, and the website hits 600k unique website visitors, among other numbers, growing fast. [https://duckdbstats.com/](https://duckdbstats.com/) ↩︎
2. Note that these Enterprise BI tools cannot work with vanilla DuckDB and will be hard to implement as a persistence layer (and compute) is required. MotherDuck supports it out of the box. ↩︎

[Discuss on Bluesky](https://bsky.app/search?q=domain%3A%20https://www.ssp.sh/blog/enterprise-case-duckdb-key-categories/)
|
[Duckdb](https://www.ssp.sh/tags/duckdb/)
[Olap](https://www.ssp.sh/tags/olap/)
[Motherduck](https://www.ssp.sh/tags/motherduck/)
[Services](https://www.ssp.sh/tags/services/)
