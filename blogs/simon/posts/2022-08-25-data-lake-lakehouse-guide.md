---
title: "Data Lake / Lakehouse Guide: Powered by Data Lake Table Formats (Delta Lake, Iceberg, Hudi)08-25"
date: 2022-08-25
url: https://www.ssp.sh/blog/data-lake-lakehouse-guide/
slug: data-lake-lakehouse-guide
word_count: 3594
---

![Data Lake / Lakehouse Guide: Powered by Data Lake Table Formats (Delta Lake, Iceberg, Hudi)](https://www.ssp.sh/blog/data-lake-lakehouse-guide/data-lake-lakehouse-feature.jpeg)

Contents
Image by
[Rachel Claire](https://www.pexels.com/@rachel-claire/)
on
[Pexels](https://www.pexels.com/photo/building-on-lakeshore-7276967/)

Ever wanted or been asked to build an open-sourceÂ [Data Lake](https://glossary.airbyte.com/term/data-lake)Â offloading data for analytics? Asked yourself what components and features would that include. Didn’t know the difference between aÂ [Data Lakehouse](https://glossary.airbyte.com/term/data-lakehouse)Â and aÂ [Data Warehouse](https://glossary.airbyte.com/term/data-warehouse)? Or you just wanted to govern your hundreds to thousands of files and have more database-like features but don’t know how?


This articleÂ **explains the data lake power and which technologies can build one to avoid creating a**Â [**Data Swamp**](https://glossary.airbyte.com/term/data-swamp)Â **with no structure and orphaned files**. And discuss the analytical capabilities of data lakes and how to make them. We will go through when you’d not use a data lake and what alternatives are there.


With Databricks open-sourced the fullÂ [Delta Lake](https://glossary.airbyte.com/term/delta-lake)Â 2.0, including premium features, and Snowflake announcing an integrated Iceberg Table,Â **the market is hot right now**.


## Whatâs a Data Lake and Why Do You Need One?


A data lake is a storage system with an underlyingÂ [Data Lake File Format](https://glossary.airbyte.com/term/data-lake-file-format)Â and its differentÂ [Data Lake Table Formats](https://glossary.airbyte.com/term/data-lake-table-format)Â thatÂ **store vast amounts of unstructured and semi-structured data**, stored as-is, without a specific purpose. Its the primary destination for growing volumes and varieties of exploratory and operational data next to data warehouse destinations. A wide range of technical and non-technical data consumers can access that data for analytic use cases and machine learning models, including business intelligence and reporting.


A data lake also removes the need to go through a proprietary format that traditional BI tools had done to transform the data. You load data into the lake, and old bottlenecks where data teams spend their time building and maintaining complex ETL pipelines are gone, and waiting weeks for data access requests are skipped.


With a data lake, dataÂ **becomes increasingly available, and early adopters discovered that they could extract insight through new applications built to serve the business**.Â **The data lake supports capturing and storing raw data at scale for a low cost with many different types of data**. An accessible way to perform a transformation on top, even when not yet precise which analytics are needed at the end âmainly quickly iterate on the transformations and explore business value ad-hoc.


A data lake ([initial Data Lake paper from 2014](http://hortonworks.com/wp-content/uploads/2014/05/TeradataHortonworks_Datalake_White-Paper_20140410.pdf)) can be built on multiple technologies such as Hadoop, NoSQL, Amazon Simple Storage Service, a relational database, or various combinations and different formats (e.g., Excel, CSV, Text, Logs,Â [Apache Parquet](https://glossary.airbyte.com/term/apache-parquet),Â [Apache Arrow](https://glossary.airbyte.com/term/apache-arrow),Â [Apache Avro](https://glossary.airbyte.com/term/apache-avro), more on that later). Every data lake starts with a simple storage provider, a data lake file format and then extends crucial database-like features with data lake table formats that we explore later in this article.


## Whatâs the Differences between a Data Lake, Data Warehouse, and Data Lakehouse


So whatâs the difference from a data lake to data lakehouse then? AÂ **data lakehouse is a combination of a data lake and a data warehouse if you will**Â (and there are many opinions in-between). A data lakehouse has an open data management architecture that combines the flexibility, cost-efficiency, and scale of data lakes. Same as a data lake, it also has database features provided by data lake table formats ([Delta Lake](https://glossary.airbyte.com/term/delta-lake),Â [Apache Iceberg](https://glossary.airbyte.com/term/apache-iceberg)Â &Â [Hudi](https://glossary.airbyte.com/term/apache-hudi)).Â


A data lakehouse has additionalÂ [Data Governance](https://glossary.airbyte.com/term/data-governance)Â compared to a data lake. It includes cluster-computing frameworks and a SQL query engine. More features rich lakehouses also supportÂ [Data Cataloging](https://glossary.airbyte.com/term/data-catalog)Â andÂ [State-of-Art Orchestration](https://airbyte.com/blog/data-orchestration-trends).


[
](https://future.com/emerging-architectures-modern-data-infrastructure/)


Overviewing Data Lake vs. Lakehouse (See the Full Architecture onÂ [Emerging Architectures for Modern Data Infrastructure](https://future.com/emerging-architectures-modern-data-infrastructure/)).


InÂ [Emerging Architectures for Modern Data Infrastructure](https://future.com/emerging-architectures-modern-data-infrastructure/), they say there is growing recognition for the data lakehouse architecture and have seen it by the adoption of prominent vendors (including AWS, Databricks, Google Cloud, Starburst, and Dremio) and data warehouse pioneers. The fundamental value of the lakehouse is to pair a robustÂ [storage layer](https://glossary.airbyte.com/term/storage-layer-object-store)Â with an array of powerful data processing engines like Spark, Presto, Apache Druid/Clickhouse, and Python libraries.


To close the cycle byÂ [comparing](https://youtu.be/MnP86QiWA3o)Â theÂ **data lakehouse to a data warehouse**, we can say: A lakehouse is more open (open-formats) and more difficult as more DIY and patching different tools together, supporting more ML/DS/AI use cases whereas a data warehouse is more closed (mostly closed-source), build for BI, fully managed, and more expensive to scale.Â

Definition Data Lakehouse
The term “data lakehouse” was initially described by Jeremy Engle onÂ
[these slides](https://www.slideshare.net/awschicago/jeremy-engles-slides-from-redshift-big-data-meetup-on-july-13-2017)
Â in July 2017. The big push came later when Databricks published theirÂ
[whitepaper CIDR](http://cidrdb.org/cidr2021/papers/cidr2021_paper17.pdf)
Â in 2021. Fun fact: they call it “lakehouse” without the data. I also see some differences between then and now. The initial data lakehouse is more related to data warehouse than today, with theÂ
[Data Lake Table Format](https://glossary.airbyte.com/term/data-lake-table-format)
Â having database features on top of distributed files differently.

## Components of a Data Lake


There are three major components of a data lake that we are going to discuss here. First is the layer where data is stored physically. Next, we have a data lake file format that mainly compresses the data for either row or column-oriented writing or querying. Lastly, the data lake table formats sit on top of these file formats to provide robust features.

Evolution of Data Lakes: A brief history of data lake and its evolution
- **1. Hadoop &**Â [**Hive**](https://glossary.airbyte.com/term/apache-hive): A First-Generation data lake table format withÂ [MapReduce](https://glossary.airbyte.com/term/map-reduce). Already enabled SQL expressions.
- **2. AWS S3**: The Next Generation of a simple data lake storage. No function but immensely less maintenance and an excellent programmatic API interface
- **3. Data Lake File Format:**Â Suitable file formats for the cloud that have column-oriented, well-compressed, and optimized for Analytics. File formats such as Apache Parquet, ORC, and Apache Avro.
- **4. Data Lake Table Format:**Â Delta Lake, Apache Iceberg, and Hudi with full-fledged database-like features.


### Storage Layer / Object Store (AWS S3, Azure Blob Storage, Google Cloud Storage)


Starting with the storage layer, we have the object storage services from the three big cloud providers, AWS S3, Azure Blob Storage, and Google Cloud Storage. The web user interface is easy to use.Â **Its features are very basic, where, in fact, these object stores store distributed files exceptionally well.**Â They are also highly configurable, with solid security and reliability built-in.Â


As a successor of Hadoop, they are well suited for unstructured and semi-structured data in the cloud. AWS S3 is the de facto standard for uploading files in any format to the cloud.Â


### Data Lake File Formats (Apache Parquet, Avro, ORC)


Data lake file formats are the new CSVs on the cloud. They are more column-oriented and compress large files with added features. The main players here are Apache Parquet, Apache Avro, and Apache Arrow. Itâs the physical store with the actual files distributed around different buckets on your storage layer.


Data lake file format helps store data, sharing and exchanging data between systems and processing frameworks. These file formats have additional features such as split ability and schema evolution. These are a team and programming language agnostic.


Comparison of Data Lake File Formats (Inspired byÂ [Nexla: Introduction to Big Data Formats](https://www.nexla.com/resource/introduction-big-data-formats-understanding-avro-parquet-orc/))


When choosing which data lake file format is up to you, Apache Parquet seems to have the momentum. Avro is great as it has a sophisticated schema description language to describe the data structure and supports Schema Evolution. But let’s check switch one layer above and see which data lake table formats use which file formats.

Schema Evolution
Schema Evolution is less critical as data lake table formats in the next chapter also support these.

### Data Lake Table Formats


Data lake table formats are very attractive as they are the database on data lakes. Same as a table, oneÂ **data lake table format bundles distributed files into one table that is otherwise hard to manage**. You can think of it as an abstraction layer between your physical data files and how they are structured to form a table.


Imagine inserting into hundreds of files at once. They are the key and usual relay on one of the above, open-source data lake file formats that optimize columnar storage and are highly compressed. Data lake table formats allow youÂ **to efficiently query your data directly out of your data lake.**Â No initial transformation is needed.


The data lake table formats are the engine of the data lake file format. The file formats are good at storing big data in a compressed way and returning it for column-oriented analytical queries. But they lack additional features such as ACID transactions and support of standard ANSI SQL on a table everyone knows and loves from relational databases. With data lake table formats and its open-source solutions, we get these wanted basic features precisely, but also much more, as seen in the next chapter.

Questions to ask before adopting a data lake table format
- Which format has the most advanced and stable features I need?
- Which format enables me to use SQL to access my data easily?
- Which format has the momentum and good community support?
- Which format gives the most robust version-control tools?


#### Features of a Data Lake Table Formats


How to add database features to S3 with data lake table format features that all three significant Formats are sharing. As well, the feature help, for example, to follow the GDPR policies, track, and audit, plus delete requested deletion.


**Why are all these features essential**? Imagine you need to store your analytics data on S3 in parquet files. You’d need to cluster all files, keep a record of schemata, read and update all files simultaneously, find a way to backup and roll back in case you made a mistake, write heavy functions that mimic updates or delete statements, and so on. You see where I’m going with this. These are the start of why these data lake table formats started to emerge. Because everyone needed them and created a standard, they were published as open-source.Â


##### DML and SQL Support: Select, Inserts, Upserts, Deletes


Providing merge, update, and delete directly on your distributed files. Some also support Scala/Java and Python APIs in addition to SQL.


##### Backward compatible with Schema Evolution and Enforcement


AutomaticÂ [Schema Evolution](https://glossary.airbyte.com/term/schema-evolution)Â is a crucial feature in data lake table formats as changing formats is still a pain in today’s data engineer work. Schema Evolution means adding new columns without breaking anything or even enlarging some types. You can even rename or reorder columns, although that might break backward compatibilities. Still, we can change one table, and theÂ **table format takes care of switching it on all distributed files**. Best of all does not require e rewrite of your table and underlying files.


##### ACID Transactions, Rollback, Concurrency Control


AnÂ [ACID Transaction](https://glossary.airbyte.com/term/acid-transactions)Â secures that either all changes are successfully committed or rollbacked. It makes sure you never end in an inconsistent state. There is different concurrency control that, for example, guarantees consistency between reads and writes. Each data lake table format has other implementations and features here. Read more on the respective table format.


##### Time Travel, Audit History with Transaction Log and Rollback


WithÂ **time travel**, the data lake table format versions the big data you store in your data lake. You can access any historical version of that data, simplifying data management with easy-to-audit, rollback data in case of accidental bad writes or deletes, and reproduce experiments and reports. Time travel enables reproducible queries as you can query two different versions simultaneously.


All the versions being snapshotted with a time travel feature it simplifies implementing otherwise complex methodologies such asÂ [Slowly Changing Dimension](https://glossary.airbyte.com/term/slowly-changing-dimension-scd)Â (Type 2). You can even extract changes as you usually do withÂ [Change Data Capture (CDC)](https://airbyte.com/blog/change-data-capture-definition-methods-and-benefits)Â (if you do it often enough not to lose the intermediate modifications).


TheÂ [**transaction log**](https://glossary.airbyte.com/term/data-lake-transaction-log)Â is the ordered record of every transaction since its inception. A transaction log is a common component used through many of its above-mentioned features, including ACID transactions, scalable metadata handling, and time travel. For example, Delta LakeÂ [creates a single folder called `_delta_log`](https://airbyte.com/tutorials/load-data-into-delta-lake-on-databricks-lakehouse#step-5).


**Scalable metadata handling:**Â These tables handle large amounts and many files and their metadata at scale by automatically checkpointing and summarizing them.


##### Partitioning


Partitioning andÂ [Partitioning Evolution](https://www.dremio.com/subsurface/comparison-of-data-lake-table-formats-iceberg-hudi-and-delta-lake/#toc_item_Partition%20Evolution)Â handle tedious and error-prone tasks of producing partition values for rows in a table and automatically skips unnecessary partitions and files. No extra filters are needed for fast queries, and the table layout can be updated as data changes.


##### File Sizing, Data Clustering with Compaction


Data can be compacted withÂ [OPTIMIZE](https://docs.delta.io/latest/optimizations-oss.html#optimize-performance-with-file-management)Â in Delta Lake and deletion of the old version by setting a retention date withÂ [VACUUM](https://docs.delta.io/latest/delta-utility.html#remove-files-no-longer-referenced-by-a-delta-table)Â (other data lake table formats have similar functions). TheÂ **data compaction**Â is supported out-of-the-box, and you can choose from different rewrite strategies, such as bin-packing or sorting, to optimize file layout and size. Optimize is especially effective in solving the small-file problem where you ingest tiny files over time, but querying thousands of small files is slow. Optimization can refragment the files into bigger ones, which boosts performance in many ways.


##### Unified batch and streaming source and sink


**Unified batch and streaming**Â mean theÂ [Lambda Architecture](https://glossary.airbyte.com/term/lambda-architecture)Â is obsolete. No need to differentiate your data architecture in batch and streamingâthey end both in the same tables with less complexity and more speed.


It does not matter if you’re reading from a stream or batch. Out-of-the-box MERGE statements are suitable for streaming cases where changes apply to distributed files. These data lake table formats support both a single API and target sink. You can see that well explained atÂ [Beyond Lambda: Introducing Delta Architecture](https://youtu.be/FePv0lro0z8)Â or with someÂ [code examples](https://docs.delta.io/latest/delta-streaming.html#delta-table-as-a-sink&language-python).


##### Data Sharing


A new exciting and needed feature to minimize data duplications isÂ **data sharing**. In the Delta world, it’s calledÂ [Delta Sharing](https://www.databricks.com/blog/2021/05/26/introducing-delta-sharing-an-open-protocol-for-secure-data-sharing.html). SnowflakeÂ [announced](https://www.snowflake.com/blog/iceberg-tables-powering-open-standards-with-snowflake-innovations/)Â that they would also have this feature in the Iceberg tables. These are proprietary features inside Databricks and Snowflake, as I understand.


Although, the open-sourceÂ [Delta Sharing Protocol](https://github.com/delta-io/delta-sharing)Â for secure data sharing makes it simple to share data with other organizations regardless of which computing platforms they use.


##### Change Data Feed (CDF)


[Change Data Feed (CDF)](https://docs.delta.io/latest/delta-change-data-feed.html#change-data-feed)Â feature allows tables to track row-level changes between versions of a table. When enabled, the runtime records “change events” for all the data written into the table. CDF includes the row data and metadata indicating whether the specified row was inserted, deleted, or updated. Super helpful to set upÂ [CDC](https://airbyte.com/blog/change-data-capture-definition-methods-and-benefits).


#### Data Lake Table Formats (Delta, Iceberg, Hudi)


Now we have the most notable features of open-source data lake table formats, let’s check the three most prominent products mentioned already a couple of times: Delta Lake, Apache Iceberg, and Apache Hudi.


GitHub Stars evolution onÂ [GitHub Star History](https://star-history.com/#delta-io/delta&apache/iceberg&apache/hudi&Date)


##### Delta Lake


Delta Lake is an open-source project created by Databricks and kindly open-sourced with itsÂ [first public GitHub Commit](https://github.com/delta-io/delta/commit/14cb4e0267cc188e0fdd47e5b4f0235baf87874e)Â on 2019-04-22. Recently announcedÂ [Delta Lake 2.0](https://www.databricks.com/blog/2022/06/30/open-sourcing-all-of-delta-lake.html).


ð¤¹ð¼ Example ofÂ [Creating a Table in Delta Lake](https://docs.delta.io/latest/delta-batch.html)Â with Spark SQL



| `1
2
3
4
5
6
7
8
9
` | `
--creating
CREATE TABLE default.people10m (id INT, firstName STRING, gender STRING ) USING DELTA PARTITIONED BY (gender)
LOCATION 's3a://my-bucket/delta/people10m'
--writing 
INSERT INTO default.people10m VALUES (1, 'Bruno', 'M'), (2, 'Adele', 'F');
INSERT INTO default.people10m SELECT * FROM source
--reading 
SELECT COUNT(*) > 0 AS 'Partition exists' FROM default.people10m WHERE gender = "M"
` |



##### Apache Iceberg


Apache Iceberg wasÂ [initially developed](https://github.com/Netflix/iceberg)Â at Netflix to solve long-standing issues using huge, petabyte-scale tables. It was open-sourced in 2018 as an Apache Incubator project and graduated from the incubator on the 19th of May 2020. TheirÂ [first public commit](https://github.com/apache/iceberg/commit/a5eb3f6ba171ecfc517a4f09ae9654e7d8ae0291)Â was 2017-12-19âmore insights about the story onÂ [A Short Introduction to Apache Iceberg](https://medium.com/expedia-group-tech/a-short-introduction-to-apache-iceberg-d34f628b6799).


ð¤¹ð¼ Example ofÂ [Creating a Table in Apache Iceberg](https://iceberg.apache.org/docs/latest/getting-started/)Â with Spark SQL



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
` | `
--creating
CREATE TABLE local.db.table (id bigint, data string, category string) 
USING iceberg
LOCATION 's3://my-bucket/iceberg/table/'
PARTITIONED BY (category)
--writing 
INSERT INTO local.db.table VALUES (1, 'a'), (2, 'b'), (3, 'c');
INSERT INTO local.db.table SELECT id, data FROM source WHERE length(data) = 1;
--reading 
SELECT count(1) as count, category FROM local.db.table GROUP BY category
` |



##### Apache Hudi


Apache Hudi was originally developed at Uber in 2016 (code-named and pronounced “Hoodie”), open-sourced end of 2016 ([first commit](https://github.com/apache/hudi/commit/0512da094bad2f3bcd2ddddc29e8abfec175dcfe)Â in 2016-12-16), and submitted to the Apache Incubator in January 2019. More about the back story onÂ [The Apache Software Foundation Announces ApacheÂ® Hudiâ¢ as a Top-Level Project](https://www.globenewswire.com/news-release/2020/06/04/2043732/0/en/The-Apache-Software-Foundation-Announces-Apache-Hudi-as-a-Top-Level-Project.html).


ð¤¹ð¼ Example ofÂ [Creating a Table in Apache Hudi](https://hudi.apache.org/docs/quick-start-guide/)Â with Spark SQL



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
` | `
--creating
create table if not exists hudi_table (id int,  name string,  price double)
using hudi options ( type = 'cow' )
partitioned by (name)
location 's3://my-bucket//hudi/hudi_table';
--writing (dynamic partition)
insert into hudi_table partition (name) select 1, 'a1', 20;
--reading
select count(*) from hudi_table
` |



#### Data Lake Table Format Comparison: Delta Lake vs Apache Hudi vs Apache Iceberg


Delta Lake has the most stars on GitHub and is probably the most mature since the release of Delta Lake 2.0. Apache Iceberg and Hudi have much more diverse GitHub contributors than Delta, which is around 80% from Databricks.Â


Hudi has been open-source the longest and has the most features. Iceberg and Delta have great momentum with the recent announcements, Hudi provides the most conveniences for the streaming processes, and Iceberg supports most integrations with data lake file formats (Parquet, Avro, ORC)Â


A comprehensive overview of read/write features fromÂ [Onehouse.ai:](https://www.onehouse.ai/blog/apache-hudi-vs-delta-lake-vs-apache-iceberg-lakehouse-feature-comparison)


[
](https://www.onehouse.ai/blog/apache-hudi-vs-delta-lake-vs-apache-iceberg-lakehouse-feature-comparison)


A comprehensive overview of Data Lake Table Formats Read/Write Features byÂ [Onehouse.ai](https://www.onehouse.ai/blog/apache-hudi-vs-delta-lake-vs-apache-iceberg-lakehouse-feature-comparison)Â (reduced to rows with differences only)


And data lake table services comparison byÂ [Onehouse.ai:](https://www.onehouse.ai/blog/apache-hudi-vs-delta-lake-vs-apache-iceberg-lakehouse-feature-comparison)

[
](https://www.onehouse.ai/blog/apache-hudi-vs-delta-lake-vs-apache-iceberg-lakehouse-feature-comparison)


A comprehensive overview of Data Lake Table Formats Services byÂ [Onehouse.ai](https://www.onehouse.ai/blog/apache-hudi-vs-delta-lake-vs-apache-iceberg-lakehouse-feature-comparison)Â (reduced to rows with differences only)


Please check the full articleÂ [Apache Hudi vs. Delta Lake vs. Apache Iceberg](https://www.onehouse.ai/blog/apache-hudi-vs-delta-lake-vs-apache-iceberg-lakehouse-feature-comparison)Â for fantastic and detailed feature comparison, including illustrations of table services and supported platforms and ecosystems. Two other excellent ones areÂ [Comparison of Data Lake Table Formats](https://www.dremio.com/subsurface/comparison-of-data-lake-table-formats-iceberg-hudi-and-delta-lake/)Â by Dremio andÂ [Hudi, Iceberg and Delta Lake: Data Lake Table Formats Compared](https://lakefs.io/hudi-iceberg-and-delta-lake-data-lake-table-formats-compared/)Â by LakeFS.


ð InterestingÂ [comment](https://www.linkedin.com/feed/update/urn:li:activity:6966046844137213952/)Â around Hudi Versioning where Hudi supports different source systems and how itâs based on commits and can be maintained for individual source systems.Â


## Data Lake Trends in the Market


The market of open-source data lake table formats is hot with the recent announcements at theÂ [Snowflake Summit](https://www.snowflake.com/blog/four-customer-takeaways-from-summit-2022/)Â andÂ [Data & AI Summit](https://www.databricks.com/blog/2022/07/25/recap-of-databricks-lakehouse-platform-announcements-at-data-and-ai-summit-2022.html). Snowflake and Databricks announced a significant step with the Apache Iceberg Tables ([Explainer Video](https://www.youtube.com/watch?v=Kz5cWY_vRwU)), combining the capabilities of open-source Apache Iceberg with Apache Parquet. And Databricks with open-sourcing all of Delta Lake, including previous premium features such asÂ [OPTIMIZE](https://docs.delta.io/latest/optimizations-oss.html#compaction-bin-packing)Â andÂ [Z-ORDER](https://docs.delta.io/latest/optimizations-oss.html#z-ordering-multi-dimensional-clustering)Â withÂ [Delta Lake 2.0](https://www.databricks.com/blog/2022/06/30/open-sourcing-all-of-delta-lake.html).


Other market trends are further commercializing the data lake table formats, such asÂ [Onehouse for Apache Hudi](https://venturebeat.com/big-data/onehouse-brings-a-fully-managed-lakehouse-to-apache-hudi/)Â and bothÂ [Starburst](https://www.techtarget.com/searchdatamanagement/news/252509796/Starburst-Enterprise-brings-Apache-Iceberg-to-data-lakehouse)Â andÂ [Dremio](https://www.dremio.com/blog/announcing-dml-support-for-apache-iceberg/)Â coming out with their Apache Iceberg offerings. In April, Google announcedÂ [BigLake](https://cloud.google.com/biglake)Â andÂ [Iceberg support](https://www.datanami.com/2022/04/06/google-cloud-opens-door-to-the-lakehouse-with-biglake/)Â earlier this year, but it also supported Hudi and Delta now.


There is a big run for data lake table formats; every big vendor is either having one themself or searching for the perfect open-source one. By now, you should also understand why. Good for us is that all of these technologies are getting built on open-source data lake file formats (Apache Parquet, ORC, Avro), which is excellent news for us all.


For Example, All Features Are Open-Sourced with Delta Lake 2.0


## How to Turn Your Data Lake into a Lakehouse


An essential part of a data lake and lakehouse isÂ **data governance**. Governance is mainly around data quality, observability, monitoring, and security. Without it, you’ll directly move towards a Data Swamp.Â


Data Governance is a big thing at larger companies. In that case, the lakehouse implementations and features are helping here. These focus on reliability and strong governance and have more integrated features. But much data governance also sets the right processes and access rights in place. Let cross-functional teams work together with data quickly and in a transparent way.


To summarize essential parts so far, extending from the simple S3 storage to a full-fledged data lakehouse, you can follow these steps:

1. Choose the suitable data lake file format
2. Combine the above with the data lake table format you want to use that supports your use-case best
3. Choose a cloud provider and storage layer you want to store the actual files inÂ
4. Build some data governance on top of your lakehouse and inside your organization.
5. Load your data into the data lake or lakehouse

Alternatives
Alternatives or when not to use a data lake or lakehouse: If you need a database. Donât useÂ
[JSON instead of a Postgres-DB](https://www.linkedin.com/feed/update/urn:li:activity:6958408364246605825/?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A6958408364246605825%2C6958686136378486784%29)
. You can leverageÂ
[Data Virtualizations](https://glossary.airbyte.com/term/data-virtualization)
Â technologies when you need a quick and fast way of querying multiple data sources without moving data.

## Wrapping Up


In this article, we learned the difference between a data lake and a data lakehouse. What the market is doing in 2022 and how to turn the data lake into a data lakehouse. The three levels of it with the storage layer, the data lake file format, and the data lake table formats are on top with powerful features, which open-source table formats are out there with Apache Hudi, Iceberg, and Delta Lake.Â


---


```
Originally published at Airbyte.com
```

[Discuss on Bluesky](https://bsky.app/search?q=domain%3A%20https://www.ssp.sh/blog/data-lake-lakehouse-guide/)
|
[Pay what you like](https://ko-fi.com/sspaeti)
|
[Data Lake](https://www.ssp.sh/tags/data-lake/)
[Lakehouse](https://www.ssp.sh/tags/lakehouse/)
[Apache Hudi](https://www.ssp.sh/tags/apache-hudi/)
[Delta Lake](https://www.ssp.sh/tags/delta-lake/)
[Apache Iceberg](https://www.ssp.sh/tags/apache-iceberg/)
[Open Table Format](https://www.ssp.sh/tags/open-table-format/)
