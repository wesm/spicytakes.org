---
title: "The Open Table Format Revolution: Why Hyperscalers Are Betting on Managed Iceberg"
date: 2025-05-20
url: https://www.ssp.sh/blog/open-table-format-revolution/
slug: open-table-format-revolution
word_count: 5761
---

![The Open Table Format Revolution: Why Hyperscalers Are Betting on Managed Iceberg](https://www.ssp.sh/blog/open-table-format-revolution/featured-image.png)

Contents
This article was written as part of
[my services](https://www.ssp.sh/services)

Wondering why open table formats are suddenly booming? Why is AWS investing heavily in making Iceberg tables on S3, and why did Databricks pay a reported $2B to acquire Tabular? The answers might change how we think about data architecture. Historically, object storage like Amazon S3 or R2 was used as inexpensive, scalable storage for unstructured files, while structured data typically went to data warehouses. But open table formats are changing this paradigm by allowing database-like features on top of distributed files, making data storage both cost-effective and powerful.


Data lake table formats essentially allow you to store all your data cost-effectively while reaping the benefits of a warehouse or database. This is the premise of a Lakehouse architecture. The key advantage is flexibility: Iceberg tables are queryable by any SQL-supporting engine, allowing data pipelines to utilize DuckDB, Snowflake, Spark, or any other preferred engine.


The ICE Stack (Interoperable, Composable, and Efficient) is revolutionizing the way we design data architectures. With Cloudflare R2’s zero egress fees and AWS S3 Tables’ integrated optimization features, we’re seeing truly open data platforms where storage and compute are finally decoupled. But there’s more at stake: Is AWS S3 Tables using the standard Iceberg REST API, or creating proprietary extensions? And can Hyperscalers’ managed services outperform other implementations by speed and cost?


In this article, we’ll explore the four layers of the ICE Stack, from storage to catalogs, and why managed Iceberg powered by Hyperscalers might represent the post-Modern Data Stack future where data independence truly matters.


Let’s find out.


## Primer on ICE Stack Architecture: The Foundational Layers


To analyze the space, let’s explore what components the managed Iceberg is built on and where we’re coming from. To refer to the managed Iceberg table and all its requirements for managing it in the cloud on a Hyperscaler or locally, I call it the “ICE stack”. As we can’t **run a table format without an object store or compute**, we won’t analyze Iceberg table formats in isolation but the whole (ICE) stack.


### The Foundation of an ICE Stack


Let’s define what the ICE Stack with its open table format is and what components are involved.


![/blog/open-table-format-revolution/iceberg-stack-diagram.png](https://www.ssp.sh/blog/open-table-format-revolution/iceberg-stack-diagram.png)

*ICE Stack Components*


In short, open table formats like [Iceberg](https://github.com/apache/iceberg), [Delta Lake](https://github.com/delta-io/delta), [Hudi](https://github.com/apache/hudi), and [Lance](https://github.com/lancedb/lance) are a crucial part of building a data warehouse on top of files, also called a Lakehouse. The managed Iceberg tables provide mainly four key layers:

1. **Catalog**: Unify access and permission rights (â ï¸ not the same as [data catalogs](https://github.com/opendatadiscovery/awesome-data-catalogs)) plus listing existing tables and providing access to them using SQL. They may or may not be open, for example, Polaris vs. Horizon or Unity vs. Glue catalog.
2. **Open Table Format**: Bundle distributed files into manageable tables
3. **File Format**: Compress and optimize data for analytics like Apache Parquet, OCR, Apache Avro, etc.
4. **Object Store**: This is the storage layer that stores distributed files exceptionally well.


As we need a **compute engine** to process (aggregate, transform, create tables) and update our managed tables. That’s why Hyperscalers are offering these managed solutions, as these computations are usually time-intensive or involve heavy loads, where the cloud can help ease management and improve speed.


As everything is in an open format, and no lock-in is possible, it’s easy to switch and exchange an engine from Spark to BigQuery, or anything else that can handle table formats, or distributed files on an object store, which is almost any tool in the space.


### The ICE Stack


So what exactly is “The ICE Stack”? You can think of the entire concept of a managed Iceberg table as the foundation behind the ICE Stack, which is very similar to a **[Data Lakehouse](https://www.databricks.com/glossary/data-lakehouse)** architecture. The lakehouse attempts to unify the four layers into a single, cohesive layer. Alternatively, it can be explained as a data warehouse that’s not based on a database but rather on distributed files.


I-C-E stands for **I**nteroperable, **C**omposable, and **E**fficient.


**Interoperable** (SQL) query engines enable you to exchange data between DuckDB, Trino, or Spark SQL without modifying your data or data stack. **Composable** means you can combine different vendors as part of your data stack. E.g., you can use AWS S3, Cloudflare R2, or even [MinIO](https://min.io/) as your storage layer, but use any different engine to run your table format (Athena, Snowflake, Databricks) and again another to run your catalog. **Efficient** means that, because market forces are at play, vendors cannot overcharge, as developers can easily swap out technologies (such as S3 for R2) and negotiate better deals.


This is a significant shift from earlier eras of enterprise data infrastructure, where customers chose and were locked into major vendors like SAP, Oracle, or even IBM Mainframes (and some are still dealing with these consequences).

Related Concepts and Discussions
Sometimes you also hear the term
**Composable Data Stacks**
as Wes McKinney talked about in
[The Road to Composable Data Systems](https://wesmckinney.com/blog/looking-back-15-years/)
. In 2023 and before, we had discussions on
[Bundling vs Unbundling](https://blog.fal.ai/the-unbundling-of-airflow-2/)
. Julien Hurault and others talk about
[Multi-Engine Data Stacks](https://juhache.substack.com/p/multi-engine-data-stack-v1)
, and
[Declarative Data Stack](https://www.rilldata.com/blog/the-rise-of-the-declarative-data-stack)
are related too, as most of the ICE stack is created declaratively, or should be.

### Why ICE Stack?


The ICE Stack is a table format-enabled data stack. Building on top of a cheap storage layer and distributed files.


Why would you choose the ICE Stack, or managed Iceberg to begin with when you can just use BigQuery, Databricks or Snowflake? That’s a good question, and the short answer comes down to mainly **cost** and **no vendor lock-in**.


An ICE Stack shifts from *where the data is stored* (database/cloud data warehouse, Oracle, Teradata) to a data stack and data platform. Instead of proprietary, mostly expensive file storage, the data is at the core of the ICE Stack. It’s [open](https://www.ssp.sh/brain/openness), for everyone to explore and use, and standardized around the table format of Iceberg with a clear [set of APIs](https://github.com/apache/iceberg/blob/main/open-api/rest-catalog-open-api.yaml), defined as open source.


This also has its downsides: data governance is more complex. Performance is typically slower as the files are distributed and potentially not in the same location. The compute might be geographically located somewhere totally different. It’s challenging to achieve a unified interface.


That’s why catalogs have gained popularity lately. Catalogs like Iceberg Catalog, [Unity Catalog](https://github.com/unitycatalog/unitycatalog), [Apache Polaris Catalog](https://github.com/apache/polaris) and others, try to create this **control plane** to unify access and permission rights.


If we dig one level deeper into the question I got from [Andrew](https://bsky.app/profile/therriault.bsky.social/post/3lo6v3j64t22b):


> Why do we need all these new options? What problem do they solve that wasn't adequately solved by Parquet [..]?


#### Strategic Advantages


Besides the cheaper cost and no vendor lock-in, we need to look beyond the table format alone and consider the overall solution of managed Iceberg tables, or its lakehouse-like architecture. With the managed approach, you get an open, interoperable, composable and efficient data platform to store vast and various amounts of data. But Iceberg is only a storage format with Apache Parquet and a transaction log, so what are the advantages?


The strategic edge for going with an ICE Data stack includes:

- **Convergence on open standards**: The industry is moving toward interoperability and open standards based on table formats and table format catalogs
- **Recognition of Iceberg’s importance**: As evidenced by Databricks’ $2B acquisition of Tabular, Databricks’ efforts to manage Iceberg tables as part of their platform, and Amazon AWS and Cloudflare integrating these as services
- **Cost efficiency emphasis**: Particularly with Cloudflare’s zero egress model, and many more to come by other vendors, it’s challenging traditional cloud economics


To summarize, an ICE Stack compared to a vendor cloud data platform is incredibly cheap, offers polyglot and hot-swappable compute engines, has no vendor lock-in, and features interoperable query engines which makes it super flexible. You store data once, run compute anywhere and scale flexibly with Hyperscalers’ cloud platforms only when needed.


## Why Managed Iceberg, and Some Trends


You might think or ask yourself, why [Iceberg](https://github.com/apache/iceberg/), why not [Delta Lake](https://github.com/delta-io/delta) or [Apache Hudi](https://github.com/apache/hudi)? Let’s analyze this, and explore the features and history behind it a bit more.


### Trends: Why Managed Iceberg, and not Delta, or Hudi?


With the acquisition of [Tabular](https://www.tabular.io/) by Databricks, and even more so, with the recent “Managed Iceberg” announcements (more on that later) that Databricks made to host Iceberg tables on Databricks, it’s clear that open table formats are consolidating into Apache Iceberg table format. The features themselves have become interchangeable between the formats for a while now, and multiple conversion tools like [Apache XTable](https://github.com/apache/incubator-xtable) or [Delta Universal Format (UniForm)](https://docs.delta.io/latest/delta-uniform.html) have been developed to facilitate conversions between them.


Before that, we can examine which Hyperscaler uses which table format. We noticed that Microsoft Fabric has adopted Delta Lake, Snowflake has integrated Iceberg Tables, which are essentially Apache Iceberg tables (although they weren’t as open initially), and Hudi is primarily developed and maintained by [Onehouse](https://www.onehouse.ai/), as it was initially created at Uber.


We got further reinforcement with the recent [announcement](https://aws.amazon.com/blogs/aws/new-amazon-s3-tables-storage-optimized-for-analytics-workloads/) of **Amazon S3 Tables**, which is based on Apache Iceberg. Or [Cloudflare R2](https://www.cloudflare.com/developer-platform/products/r2/), a catalog for managed Iceberg tables with zero egress fees.


As table formats such as Iceberg are a key part of a data platform, it’s good to know that it’s now standardizing around one, Apache Iceberg, and the existing Delta Lake ecosystem will be merged as Databricks, the owner of both and with lots of Delta Lake customers, needs a straight path forward.

When not to use Apache Iceberg
A year ago, I’d say you’d choose the format that best fits your platform and environment. Nowadays, you’d select Iceberg unless you have dedicated use cases where one format is optimized for a specific purpose, such as Apache Hudi for a heavy streaming approach. However, aside from that, we can safely say that the ecosystem will standardize around Apache Iceberg sooner rather than later.

#### *Not* A Proprietary Format


One of the most significant advantages, if not the biggest, is the [openness](https://www.ssp.sh/brain/openness) to our own data. An organization now has access to its data and everyone can read or scan it with a clearly defined open-source definition. There’s no proprietary software needed to read it.


This is key and opens up many of the discussed benefits and reasons why you’d want an ICE stack. They are unlike proprietary formats in data warehouses, where it’s difficult to extract your data. Instead, you can easily move the data to a different cloud provider, build services like semantic layers on top, or perform any other action, as the data itself is open and standardized through the table format.


![/blog/open-table-format-revolution/closed-vs-open-source-architecture.png](https://www.ssp.sh/blog/open-table-format-revolution/closed-vs-open-source-architecture.png)

*Closed vs. Open Source Architecture Components*


Another benefit is that since a company’s **data** is typically one of its most valuable assets, it’s now easier than ever to own your data. Because the data is in an open format, even at the underlying file format level (usually Apache Parquet), it’s easy to read with almost all modern engines, in an efficient and open manner.


Open formats also allow new possibilities for **sharing data, instead of copying** data from one platform to another. You could potentially expose APIs. Since it’s an open format, others can integrate these APIs and standardizations and read the data without copying. This is essentially what AWS S3 Tables has done with the [S3 Table API](https://docs.aws.amazon.com/AmazonS3/latest/API/API_Operations_Amazon_S3_Tables.html) now that it’s managed and hosted on Amazon.


#### No Compute Vendor Lock-In


We also need to talk about the compute as this is where the money lies in an open table format.


Because storage is very affordable, most money is made when you aggregate or query the data stored in the affordable storage. This is called the compute or engine that queries or transforms the data: on AWS you can use multiple engines like Spark, Glue, Athena. That’s why it’s so interesting for Snowflake, Microsoft with Fabric, Databricks and others to support and **offer these services**.


As the ICE Stack architecture with managed Iceberg reduces vendor lock-in, the outcome might be that instead of migrating data to another Hyperscaler, everyone migrates compute engines more frequently. As the data itself doesn’t move because it stays in open table formats, we can now easily choose and pick the best engine for every job.


With the vendor data lock-in removed, any vendor offering data computation has the advantage that fewer data platforms get locked into being strictly a “Snowflake, Databricks, BigQuery, or AWS shop”. Moving data compute between vendors previously required translating and often significantly refactoring the code to execute on a different engine. But today you have a **unified engine** that works on any platform, like Orchestration, Spark, Ibis, ClickHouse or a Kubernetes resource/job on Airflow.


### The Evolution of Managed Iceberg Tables


Before we proceed, let’s briefly review our current position. We can examine the evolution from initial file formats to today’s table formats, catalogs, and managed services provided by Hyperscalers.


We have come a long way as the illustration below shows. From Hadoop with the [Hive Metastore (HMS)](https://hive.apache.org/), to file formats like ORC to Parquet, to table formats in 2016. Later we got Delta UniForm  and XTable to convert between different table formats, and today we have unified table formats with Iceberg and managed Iceberg tables and catalogs on AWS, Cloudflare and others.


![/blog/open-table-format-revolution/evolution-open-table-formats.png](https://www.ssp.sh/blog/open-table-format-revolution/evolution-open-table-formats.png)

*Managed Iceberg Ecosystem*


The above-mentioned terms are not all open table formats, but they’re related in terms of what led to them (file formats) and where we are heading (catalogs, lakehouse). For example, Hive Metastore (HMS) is a central repository that stores metadata for Hive, similar to an Iceberg catalog. Parquet is a file format primarily used as the underlying file format for table formats. And Polaris is a catalog compatible with Iceberg.


## Features of Managed Iceberg


As we transition into a new **Post Modern Data Stack** as some might want to call it, the question is what’s next and what features does managed Iceberg deliver to us?


Most people are talking about Iceberg as the center of it. I’d agree, and not only today, but already back in 2019 when I first used Delta Lake, the open format by Databricks, it was clear to me that this is huge.


Back then, we had the main features of an open table format, including database-like features on top of distributed files. Today, we have newer features that enhance and facilitate access and data governance. In both scenarios, there is a massive benefit if you need or have a lot of files in your data lake and you’d like to make better sense of them, or you want to improve [Data Governance](https://en.wikipedia.org/wiki/Data_governance). In both scenarios, table formats can be extremely helpful due to their features.


### Main Features


The main feature, without going into each of them, as this has been explained in many places, is the ability to run SQL queries on top of distributed files.


When you want to aggregate over thousands of files and calculate the `SUM()` or `AVG()` of your sales, or just a simple `COUNT(*)`, you can do that by simply querying `SELECT COUNT(*) FROM iceberg_table`, without having to know where the files are stored or how many of them exist.


By having a table format in place such as Iceberg, you also have a **validated and guaranteed** schema, also called **schema enforcement**.


Besides SELECT statements, we can do UPSERTs (update and insert), but also [DDL](https://en.wikipedia.org/wiki/Data_governance) commands like `ALTER, DROP, CREATE`, etc. are possible. We can rename a table or truncate it by simply using SQL statements we’re familiar with.


We get **Time Travel** as we have **ACID Transactions** that either succeed or fail for the full transaction. With each successful transaction, we get a new version, and we can query old versions for each table—therefore traveling back in time. This is not a backup but can give us peace of mind in case we mess up a UPSERT statement. This is only available for as long as the *retention interval* is set. In Delta, this is set to 7 days by default.


### Newest Features: Unity and Cataloging


The more interesting ones that were introduced lately are catalog and unifying features around Unity Catalog and Iceberg Catalog.


These allow you to search for your data assets as part of your data lake. Similar to what `INFORMATION_SCHEMA` does in a database, you can query your table format catalog to see what assets are available.


With the release and [announcement](https://youtu.be/x-pAS9KqTC0?si=grZXiUCdNwFetrlE&t=244) of Databricks managed Iceberg, it’s clear they’re integrating the ecosystem around Iceberg and Delta to **avoid siloed data and siloed catalogs**.


## Iceberg Catalog Features


### Cataloging Features: What is an Iceberg Catalog?


So, what is an Iceberg Catalog, what is its connection to Iceberg tables, and why would we need one?


First, what is an Iceberg or any other Catalog? It’s tricky because it’s not the same as the standard data catalogs that come with features such as searching for datasets, defining owners, commenting on and documenting the different data assets.


Instead, it’s like an index or “catalog” of tables in your data asset. A little like the INFORMATION_SCHEMA that most relational databases support where you query like `SELECT * FROM INFORMATION_SCHEMA.tables;`, or the Hive Metastore (HMS). These are **singular indexes for what tables you have in your data lake**. And they provide everyone SQL access to them and a [REST OpenAPI specification](https://github.com/apache/iceberg/blob/main/open-api/rest-catalog-open-api.yaml).


The actual metadata, including which files and physical paths belong to this table, the number of rows, and the columns, is stored in the transaction log called the **manifest**.


### Other Catalogs Overview


There are other catalogs besides the Iceberg catalog such as Unity Catalog, Polaris Catalog, and [Glue Catalog](https://docs.aws.amazon.com/prescriptive-guidance/latest/serverless-etl-aws-glue/aws-glue-data-catalog.html). The challenge here is to avoid **catalog silos**, particularly true for Iceberg as this table format requires a catalog (Delta, for example, does not).


![/blog/open-table-format-revolution/silo-catalog.png](https://www.ssp.sh/blog/open-table-format-revolution/silo-catalog.png)

*Green = full support, yellow = some support and red = no access | Image fromThe Whys of Managed Iceberg with Databricks*


Important here again are the **engines**. As mentioned before, the table formats only add a definition and a transaction log in addition to the Apache Parquet file, but you can’t create or update a table without a respective engine. The Databricks vision for the unification of catalogs is around **Unity Catalog** as you can see on their overview:


![/blog/open-table-format-revolution/unity-catalog.png](https://www.ssp.sh/blog/open-table-format-revolution/unity-catalog.png)

*Unity Catalog ecosystem |  Image fromThe Whys of Managed Iceberg with Databricks*


Key features they plan include pre-optimization (automated maintenance), implementation of Iceberg REST catalog spec for interoperability, federation capabilities to connect with other catalogs, and integration with Databricks’ performance features like liquid clustering.


They hinted in the YouTube discussion that, ultimately, they are moving in the direction of a **Lakehouse Catalog** where format interoperability across Delta and Iceberg will have *consistent data and delete files* in Iceberg v3 with deletion vectors, variant types, geographic types, and row-level tracking.


**Other questions are**

Is Apache Iceberg the same as an Iceberg Table? Why does Snowflake not call them Apache Iceberg Tables? And how do they compare to AWS managed S3 Iceberg Tables?


### Cloudflare Managed Iceberg Catalog with Zero Egress on R2


Interesting is the newly [announced](https://developers.cloudflare.com/r2/data-catalog/) managed Iceberg Catalog by Cloudflare. Cloudflare R2 Data Catalog offers managed Iceberg tables with **zero egress fees**. The R2 Data Catalog is an open and beta managed Apache Iceberg catalog built directly into your Cloudflare R2 bucket.


With zero egress fees, we can store Iceberg tables on R2 and let others query them for free. Cloudflare has also integrated the Iceberg Catalog, which provides an endpoint for querying to retrieve a list of your tables and the current state of your data lake, using only R2 and no additional requirements. The Iceberg catalog [serves as a pointer](https://blog.cloudflare.com/r2-data-catalog-public-beta/) to the manifest files.


Although they sell it as managed Iceberg, it’s more a managed Iceberg catalog, as the compute or the warehouse is not part of it as you can see in [their example](https://blog.cloudflare.com/r2-data-catalog-public-beta/#create-your-first-iceberg-table-on-r2), where you’d need to configure a warehouse engine (like [PyIceberg](https://py.iceberg.apache.org/), [Snowflake](https://www.snowflake.com/), and [Spark](https://spark.apache.org/)) as part of your pipeline python code.


## What about AWS S3 Tables?


Where does the AWS S3 (Iceberg) Table fit into all of this?


AWS took it one step further than Cloudflare R2; they also provide the compute as part of their cloud offering. That means you can have a fully managed Iceberg table inside AWS, and can choose not from one, but multiple engines. According to the [Official Amazon Docs](https://aws.amazon.com/s3/features/tables/), AWS S3 Tables deliver a 3x faster query performance compared to unmanaged Iceberg tables. The important part is that the Iceberg transaction metadata is also managed.


The new table buckets introduced to S3, compared to the standard object buckets, include a client library used by query engines to navigate and update the Iceberg metadata of tables in your table bucket. This library, in conjunction with updated S3 APIs for table operations, allows multiple clients to safely **read and write data to your tables**.


According to the [user guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables.html), the AWS S3 table is essentially a new **bucket type** called *table bucket*, which stores the Iceberg tables as sub-resources. They allow you to query the tables with query engines that support Iceberg, such as **Amazon Athena, Amazon Redshift, and Apache Spark** as the compute.


The hierarchy goes from `Account -> Catalog -> Database -> Table`:



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
` | `AWS Account
ââââ AWS Glue Data Catalog
    ââââ s3tablescatalog (Account level container)
        ââââ Catalog 1 (Table bucket A)
        â   ââââ Database 1 (Namespace A)
        â       ââââ Table A
        â       ââââ Table B
        â       ââââ Table C
        â   ââââ Database 2 (Namespace B)
        ââââ Catalog 2 (Table bucket B)
            ââââ Database 3 (Namespace C)
             ââââ Tables...
` |



What does that mean? On paper, it’s managed Iceberg tables with faster query performance, integrated features such as [compaction](https://aws.amazon.com/blogs/storage/how-amazon-s3-tables-use-compaction-to-improve-query-performance-by-up-to-3-times/) and others out of the box.

Features that AWS Managed Iceberg Tables Offers

According to [New Amazon S3 Tables: Storage optimized for analytics workloads | AWS News Blog](https://aws.amazon.com/blogs/aws/new-amazon-s3-tables-storage-optimized-for-analytics-workloads/), managed AWS Iceberg Tables have these features:


**Table Maintenance**

Table buckets take care of some important maintenance duties that would be your responsibility if you were creating and managing your own Iceberg tables. To relieve you of these duties so that you can spend more time on your table, the following maintenance operations are performed automatically:


**Compaction** – This process combines multiple small table objects into a larger object to improve query performance, in pursuit of a target file size that can be configured to be between 64 MiB and 512 MiB. The new object is rewritten as a new snapshot. This is referred to [Small File Problem](https://www.cloudera.com/blog/technical/the-small-files-problem.html).


**Snapshot Management** – This process expires and ultimately removes table snapshots, with configuration options for the minimum number of snapshots to retain and the maximum age of a snapshot to retain. Expired snapshots are marked as non-current, then later deleted after a specified number of days.


**Unreferenced File Removal** – This process removes and deletes objects that are not referenced by any table snapshots.


### Open or Proprietary API?


The key question is, as some have mentioned, whether the API for reading and writing tables is the [open source API](https://github.com/apache/iceberg/blob/main/open-api/rest-catalog-open-api.yaml) that is on GitHub, or if it’s proprietary. According to Daniel, **the [AWS S3 Table API](https://docs.aws.amazon.com/AmazonS3/latest/API/API_Operations_Amazon_S3_Tables.html) is a proprietary one**, not following the Iceberg standard.


While the managed Iceberg with all the additional services is most welcome, the proprietary API is not. This means that you can no longer access the underlying file format (Parquet files and transaction log folder) directly; instead, you must use their API. Others mentioned that not only is the API proprietary but also that the catalog was essentially created as proprietary and as a non-standard option that confuses users and makes integration difficult. This issue has apparently been addressed recently by releasing the [Iceberg REST endpoint](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-integrating-open-source.html) embedded in the service.


According to the [documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-integrating-open-source.html), this allows us to connect with the Iceberg REST client to the Amazon S3 Tables Iceberg REST endpoint and make REST API calls to create, update, or query tables in S3 table buckets.


The endpoint implements a set of standardized Iceberg REST APIs specified in the official [Apache Iceberg REST Catalog Open API specification](https://github.com/apache/iceberg/blob/main/open-api/rest-catalog-open-api.yaml) . The endpoint works by translating Iceberg REST API operations into corresponding S3 Tables operations.


There are still many open issues, like AWS Glue integration and IAM permissions via LakeFormation as Tobias Müller [points out](https://www.linkedin.com/feed/update/urn:li:activity:7315771851077484545?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A7315771851077484545%2C7316066746702913537%29&*dashCommentUrn*=urn%3Ali%3Afsd_comment%3A%287316066746702913537%2Curn%3Ali%3Aactivity%3A7315771851077484545%29). But it’s definitely a good start for working with Iceberg and table formats if you are on AWS.


But as all of this is very early, much can change and align over time.


And on the other hand, as Iceberg is just Parquet with a transaction log, you can still store that on your own with full authority and control, improving read and access speed with [MinIO](https://min.io/), [Zenko](https://github.com/scality/Zenko), and other self-hosted S3 providers. This depends on how much you benefit from the managed services and integration that Amazon provides in S3 Tables. It’s certainly beneficial for the ecosystem that we have managed services available when needed and to better integrate them into our data architecture.


### Example with Athena as Compute


To demonstrate how a managed Iceberg table or AWS S3 table works, here is a brief demo. This demo utilizes AWS Athena as the compute engine to create and execute SQL statements. Without a compute, we couldn’t create the folder and the Parquet files. Alternatives could be Spark, Glue, or EMR.


Creating an Iceberg table with Athena:


[

](https://www.ssp.sh/blog/open-table-format-revolution/aws-s3-athena.png)Creating Iceberg Table with Athena | Image from the YouTube Demo on [Understanding Amazon S3 Tables](https://www.youtube.com/watch?v=e1ypMWSHgsM)


You can see on the next slide that when you actually create the table, it’s no different than creating any other database table with a CREATE statement, but with the addition of `TBLPROPERTIES ('table_type' = 'iceberg')` as you can see below:


![/blog/open-table-format-revolution/aws-s3-editor.png](https://www.ssp.sh/blog/open-table-format-revolution/aws-s3-editor.png)

*Creating Iceberg Table with Athena | Image from the YouTube Demo onUnderstanding Amazon S3 Tables*


You also specify the data catalog as this is a requirement by Iceberg and the database. This helps us then using the catalog, to query all existing tables on our data lake called database.


### Using DuckDB to Read the Iceberg Table


DuckDB recently [announced](https://duckdb.org/2025/03/14/preview-amazon-s3-tables.html) native Iceberg support as well, supporting Apache Iceberg REST Catalogs, enabling seamless connections to Amazon S3 Tables (and [SageMaker Lakehouse](https://aws.amazon.com/sagemaker/lakehouse/)).


With DuckDB, you can then attach the catalog with the right secret and query the tables you created in that catalog as seen below:



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
` | `CREATE SECRET (
  TYPE S3,
  PROVIDER credential_chain
);

ATTACH '059904129044:s3tablescatalog/demo-table-bucket' AS glue_test (TYPE ICEBERG)

--existing tables in this catalog
SHOW ALL TABLES;

--query a Iceberg table
Select * from glue_test.pidaydemo.tripdatatable limit 1000;
` |



The extension also supports Iceberg’s schema evolution, allowing users to follow changes in the table’s schema.


## Commentary of Data Engineers in the Field


Interesting also to get the insights of data engineers who voiced their opinion on LinkedIn or other places, which I’d like to include below to give different perspectives of the current ecosystem on the managed Iceberg ecosystem, particularly regarding AWS S3 Tables and Cloudflare R2 Data Catalog.


**Daniel Beach** cautions that AWS S3 Tables may not be as “**open**” as they appear. He points out that they’re designed primarily for exclusive use with AWS products like Glue, Athena, and EMR, with limited support for query engines outside of Apache Spark. Daniel emphasizes that S3 Tables represent a proprietary API for reading and writing tables—not files—and that integrations require adoption of this **proprietary API** through a [third-party connector](https://github.com/awslabs/s3-tables-catalog/tree/main), potentially making it an expensive path to building a lakehouse architecture.


**Roy Hasson** initially criticized AWS S3 Tables for creating their own catalog rather than following standard options, noting this would confuse users and complicate integration. However, in his [LinkedIn post](https://www.linkedin.com/posts/royhasson_when-s3-tables-were-announced-i-was-quick-activity-7315771851077484545-T4ef), he later acknowledged that AWS addressed his concerns by releasing an Iceberg **REST endpoint embedded** in the service. Roy now believes this represents “true customer obsession” and a major step forward for making Iceberg tables simpler to use within the AWS ecosystem, though he notes there are still limitations to overcome.


**Tobias Müller** highlights practical hurdles when working with S3 Tables in his [LinkedIn comment](https://www.linkedin.com/feed/update/urn:li:activity:7315771851077484545?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A7315771851077484545%2C7316066746702913537%29), including the lack of **CloudFormation IaC** support for Namespaces and actual S3 Tables. He also questions the necessity of integrating **IAM permissions** via LakeFormation and using resource links between S3 Tables catalog and the “normal” Glue catalog, suggesting these implementations may not feel meaningful or straightforward for developers. Müller is also working on a detailed blog post about [cost-efficient event ingestion into Iceberg S3 Tables on AWS](https://tobilg.com/cost-efficient-event-ingestion-into-iceberg-s3-tables-on-aws).


**Amit Gilad** provides benchmark data comparing compaction performance in his [LinkedIn post](https://www.linkedin.com/posts/amit-gilad-45763433_apacheiceberg-dataengineering-awss3tables-activity-7322597968879017986-yY8u), demonstrating that **custom Rust-based** compaction significantly outperforms both Apache Spark and AWS S3 Tables in terms of speed and cost. According to his tests on a 200GB compressed dataset, custom binpack compaction completed in just 221 seconds at a cost of $0.21, while Spark took 1,612 seconds ($1.54) and S3 Tables reportedly cost around $10. He notes that sort-based compaction using Rust was more than twice as fast as Apache Spark while remaining cost-effective.


**Christophe Blefari** cautions in his [LinkedIn post](https://www.linkedin.com/posts/christopheblefari_apache-iceberg-was-everywhere-at-data-council-activity-7322484732422729728-uc50) that while Iceberg is trending, it was “developed by **Big techs** for big techs,” and most data teams might not need it. He highlights two major challenges: performance issues with S3 buckets handling the write workloads that Iceberg demands (particularly for transactions), and the necessity of running **automatic file compaction** to avoid the small file problem that Iceberg doesn’t handle well.


[**r/dataengineering Reddit**](https://sh.reddit.com/r/dataengineering/comments/1k9bg5q/cloudflares_range_of_products_for_data_engineering/) show enthusiasm for Cloudflare’s R2 Data Catalog, with users praising how it allows developers to use R2 object storage as a **data lakehouse using Apache Iceberg**. Users appreciate that it makes data engineering more accessible to beginners without requiring extensive configuration or causing budget concerns, though they note that query processing engines must still run outside Cloudflare’s infrastructure. For more information, see the [R2 Data Catalog documentation](https://developers.cloudflare.com/r2/data-catalog/) and this article on [Cloudflare R2 + Apache Iceberg + R2 Data Catalog + Daft](https://dataengineeringcentral.substack.com/p/cloudflare-r2-apache-iceberg-r2-data)


**Mike Driscoll** describes Apache Iceberg as a “**game changer**” in his [LinkedIn post](https://www.linkedin.com/posts/medriscoll_cloudflare-today-announced-apache-iceberg-activity-7316176096310317056-3WFT) because it provides a way to store tables directly on object storage, combining the query-ability of a database with the cost efficiency of object storage. He highlights that Iceberg tables can be queried by **any database**, allowing users to create pipelines that write tables with one tool and query them with another. Mike notes that Cloudflare’s support for Iceberg on R2 with no egress fees creates “a path to run a large-scale, globally replicated database at incredibly low cost,” explaining why Databricks reportedly paid $2B to acquire Tabular, the company founded by Iceberg’s creators.


## Running Analytics on top of Iceberg Tables


The ICE stack’s open nature has enabled an ecosystem of specialized analytics platforms. ClickHouse, known for its high-performance columnar architecture, has established itself as a [powerful option](https://clickhouse.com/blog/exploring-global-internet-speeds-with-apache-iceberg-clickhouse) for running analytics on Iceberg tables. It provides [dedicated table functions](https://clickhouse.com/docs/engines/table-engines/integrations/iceberg) and engines for Iceberg, supporting key features such as schema evolution, partition pruning, and time travel.


Similarly, MotherDuck, a cloud analytics platform built on DuckDB, offers [capabilities](https://motherduck.com/docs/integrations/file-formats/apache-iceberg/) to query Iceberg data through functions such as `iceberg_scan` and `iceberg_metadata`. These specialized analytics platforms aren’t hyperscalers themselves, but they demonstrate how the ICE stack enables freedom of tool choice, allowing organizations to select the right analytics engine for specific workloads while maintaining a single source of truth in their Iceberg tables.


If you need to visualize Iceberg Table format, you can use Rill by simply installing it with `curl https://rill.sh | sh & rill start`, and use the DuckDB connector to add a source:


![/blog/open-table-format-revolution/rill-iceberg-connection.png](https://www.ssp.sh/blog/open-table-format-revolution/rill-iceberg-connection.png)

*Dashboard on top of Iceberg Table in Rill*


Note that you configure the used **connector**, in this case, DuckDB, with specific options such as AWS secrets or installing extensions. My `duckdb.yaml` looks as follows:



| `1
2
3
4
5
6
` | `type: connector
driver: duckdb
boot_queries: |
  INSTALL ICEBERG;
  LOAD ICEBERG;
  SET unsafe_enable_version_guessing = true;
` |



Here, I connect a local Iceberg table I created based on the NYC dataset with [PyIceberg](https://py.iceberg.apache.org/#connecting-to-a-catalog). We can proceed by having Rill quickly AI-generate an initial dashboard and fine-tune it to our liking. This is excellent news, as we can now build a complete BI analytics solution using affordable object storage.


Learn more about Rill and its operational and fast features on [Rill Docs](https://docs.rilldata.com/) or the [Rill Website](https://www.rilldata.com/).


## Beyond Format Wars and the Unified ICE Stack Future


The ICE Stack and managed Iceberg tables represent an upcoming change in data architecture, where format wars matter less than interoperability through standardized APIs. With major Hyperscaler like AWS, Databricks, and Cloudflare offering managed Iceberg solutions, we’re seeing an apparent industry convergence toward open standards. Cost efficiency has become a key differentiator, particularly in operations such as compaction, while catalog federation and unified governance are emerging as crucial capabilities for the lakehouse architecture.


What makes this shift particularly compelling is how managed Iceberg tables deliver database-like experiences while maintaining the flexibility of distributed files. Services like AWS S3 Tables and Cloudflare R2 Data Catalog abstract away complexity through managed services, offering the governance and performance of databases with the affordability of object storage. This explains why Databricks reportedly paid $2 billion to acquire Tabular, the company behind Iceberg—they recognized the strategic importance of standardizing around Iceberg rather than their proprietary Delta Lake format.


Looking ahead, the industry is moving toward a future with truly interoperable query engines and polyglot architectures, where potential AI query planners can identify the best compute for each run. Ryan Blue, Iceberg’s creator, has already hinted at upcoming features, including new type support and a vision where formats like Iceberg and Delta might converge. With Neon’s [acquisition](https://neon.tech/blog/neon-and-databricks) by Databricks and zero egress costs becoming the new data gravity, the innovation continues to evolve.


The true power of this open approach lies in its flexibility—data remains in open formats, engines become interchangeable, and organizations maintain ownership of their most valuable asset: their data. With managed Iceberg tables, we gain the cost efficiency of object storage combined with the query-ability of databases, creating a path to run large-scale, globally replicated databases at remarkably low costs while maintaining the freedom to choose the best tools for each specific workload.


---


```
Full article published at Rilldata.com - written as part of my services
```

[Discuss on Bluesky](https://bsky.app/search?q=domain%3A%20https://www.ssp.sh/blog/open-table-format-revolution/)
|
[Rill](https://www.ssp.sh/tags/rill/)
[Business-Intelligence](https://www.ssp.sh/tags/business-intelligence/)
[Data-Warehouse](https://www.ssp.sh/tags/data-warehouse/)
[Cloud Data Warehouse](https://www.ssp.sh/tags/cloud-data-warehouse/)
[Data Architecture](https://www.ssp.sh/tags/data-architecture/)
[Modern Data Stack](https://www.ssp.sh/tags/modern-data-stack/)
[Yaml](https://www.ssp.sh/tags/yaml/)
[Open Table Format](https://www.ssp.sh/tags/open-table-format/)
[Services](https://www.ssp.sh/tags/services/)
