---
title: "Internal vs. External Storage? What's the Limit of External Tables"
date: 2026-05-14
url: https://www.ssp.sh/blog/modern-external-tables-and-evolution/
slug: modern-external-tables-and-evolution
word_count: 5273
---

![Internal vs. External Storage? What's the Limit of External Tables](https://www.ssp.sh/blog/modern-external-tables-and-evolution/featured-image.png)

Contents
This article was written as part of
[my services](https://www.ssp.sh/services)

When I started my career as a data warehouse engineer and business intelligence engineer in 2003, external tables with materialized views were the standard. We used external tables to integrate CSV files and other data not already in Oracle databases. Oracle External Tables have existed since 2001, and that’s where I first used them. If the Lindy Effect continues to hold, we’ll use external tables even longer. But why have they survived for so long?


The core question is: “When should you store data internally in your warehouse versus externally in object storage?”. Hot data queried frequently goes inside. Cold archival data stays external, where it’s cheaper but slower. Interestingly, Databricks and BigQuery recently added external table features, but why? Not because they’re trendy, but because the economics still work.


This article offers an inside look at external tables, their 25-year history, how they evolved from CSV parsers to ACID lakehouse tables, and whether you need to know about them today.


## What Are External Tables?


So what are external tables, and why have we been using them for so long? Why don’t we just use the internal storage of a database?


In Oracle, where I first used them in 2008, they allowed you — and still do — to access data in external tables. External tables are defined as **tables that do not reside in the database**, and can be in any format for which an access driver1 is provided. All of this is provided via [DDL](https://en.wikipedia.org/wiki/Data_definition_language) (Data Definition Language) of the database, describing an external table with all its columns, data types, etc., exposing the data as if it were residing in a regular database table.


The external data can be queried in parallel and **queried directly using SQL**. Essentially, it’s read-only access to data stored outside of our database, making it available in a tabular, easy-to-work-with format to interact with existing tooling and language. In 2008, this was through procedural language such as PL-SQL in Oracle or T-SQL on MSSQL.


Today, external tables have evolved. The biggest change is that they can read more formats including semi-structured data such as Parquet, JSON, Avro, and ORC. While CSV was readable in 2008, the difference today is the columnar formats and nested formats that enable faster analytics. These are available for downstream processes and dashboards, but mostly accessed through SQL queries in one form or another.


A modern definition by [BigLake](https://research.google/pubs/biglake-bigquerys-evolution-toward-a-multi-cloud-lakehouse/), an evolution of BigQuery toward a multi-cloud lakehouse that tries to solve key customer requirements around the unification of data lake and enterprise data warehousing workloads, [introducing](https://docs.cloud.google.com/bigquery/docs/external-tables) external tables in 2015 as part of it2:


> External tables are stored outside of BigQuery storage and refer to data that’s stored outside of BigQuery. [..] Google Non-BigLake external tables let you query structured data in external data stores. To query a non-BigLake external table, you must have permissions to both the external table and the external data source.


Snowflake [defines](https://docs.snowflake.com/en/sql-reference/sql/create-external-table) them as:


> […]  When queried, an external table reads data from a set of one or more files in a specified external stage, and then outputs the data in a single VARIANT column. Additional columns can be defined, with each column definition consisting of a name, data type, and optionally whether the column requires a value (NOT NULL) or has any referential integrity constraints.


External tables were [added in 2021](https://www.snowflake.com/en/blog/external-tables-are-now-generally-available-on-snowflake/), and Snowflake described their benefits as follows:


> External Tables Address Key Data Lake Challenges:
> To **augment an existing data lake**. [..] augment their existing data lake, rather than replace it. The External Tables feature enables that use case. Customers can use external tables to query the data in their data lake without ingesting it into Snowflake. (side note: MVs3)
> Ad-hoc analytics. Customers often use external tables to **run ad-hoc queries directly on raw data before ingesting the data** into Snowflake. Ad-hoc queries help them evaluate data sets and determine further actions.


### Just a Pointer (Symlink)?


A simple analogy is a **symlink in Linux**, where you point from your current directory to another directory without moving data. You just add a pointer. If you read that file from that symlink, all it does is read it from the location the symlink points to.


An external table is the same, just a **pointer** to external data, bringing that data into the current data warehouse or cloud solution, hence the word external. You define the source format such as XML, CSV, etc., and define their structure, and then you can query that at any time. It’s similar to a SQL View in that sense, but pointing to non-internal data.


Running `DROP TABLE` and deleting an external table is metadata-based only. No data is removed, only the table definition from the internal data catalog. The same is true with a symlink. Almost any relational database today has support for it, even if it’s not called an external table. Everyone occasionally needs to read data outside of its warehouse or database.


## Recap in the History of External Tables


Looking back at the history and evolution of external tables, we can quickly see that there’s a long history and they’ve been a **recurring pattern** across every generation of database technology since the early 2000s, and arguably longer if you count IBM’s federated database concepts from the late 1990s.


### The Origin Story: ISO in 2001


The history starts with [ISO/IEC 9075-9](https://www.iso.org/standard/31370.html), published in 2001. Part 9 of the SQL standard defined foreign-data wrappers and datalink types for managing external data from within SQL. The work was completed in late 2000 and published alongside SQL:1999, with full integration in SQL:2003 (it was later [updated in 2023](https://www.iso.org/standard/84804.html)).


It was the initial definition and extensions to database language SQL to support management of external data **through the use of foreign-data wrappers and datalink types**.


My first encounter was with Oracle external tables, but according to [Wikipedia](https://en.wikipedia.org/wiki/Open_Database_Connectivity) there were earlier implementations, such as **Microsoft Access linked tables (~1992)**. Microsoft Access linked tables (~1992) were the earliest consumer-facing implementation where users could link dBASE, Paradox, text files, and ODBC sources as if they were Access tables. **ODBC 1.0 (1992)** itself established the first standard for heterogeneous data access across databases, though it didn’t create table abstractions.


Further, **[IBM’s DB2 DataJoiner](https://www.mcpressonline.com/analytics-cognitive/db2/the-as400-and-ibms-db2-datajoiner) (~1995)** was more ambitious with a middleware product enabling SQL queries across Oracle, Sybase, SQL Server, Informix, Teradata, and even VSAM files through a unified interface. With **SQL Server 7.0’s Linked Servers (1998)** we got federated querying to Microsoft’s ecosystem via **OLE DB**, supporting cross-database joins with four-part naming conventions.


Most of these implementations shared a common limitation that Oracle ([9i Release 1 - 9.0.1](https://oracle-base.com/articles/9i/sql-new-features-9i) in 2001) solved: they focused on querying *other databases* or required middleware. Oracle’s abstraction treated local flat files as first-class read-only table objects using the familiar `CREATE TABLE ... ORGANIZATION EXTERNAL` DDL syntax, providing a simple way to define external files as part of normal table creation and allowing ORACLE_LOADER access to query flat files (CSV, fixed-width, delimited) through DBAs.


It was an early way of separating declaration from compute (the Oracle loaders).


## Why External Tables? What Are Their Benefits?


But why use external tables? What makes them so useful that they persisted? Why have they **survived so long**, and why are they getting added to Databricks and other major platforms?


For that, we need to look at external tables’ benefits. The first reason is that external tables can simplify data access to **avoid developing ETL pipelines**, moving data out of the source, and re-ingesting it in our data warehouse. They make external data accessible easily, defined in a tabular form by a database schema with column types. Typical cloud data warehouses like Snowflake and Azure use them to link existing data from object storage easily without moving data. This makes the object storage files accessible for almost any downstream tool or query language in a simple and cost-effective way.


Other ways of using them are to store some data on **cheaper storage** (e.g., object storage over data warehouse storage) and only link them in. It’s slower to fetch, but more affordable to keep. If you have large data sets, cost savings can be immense as this article [shows](https://medium.com/@abhidutty/optimize-data-storage-costs-by-70-using-databricks-snowflake-aws-s3-332f44949e93), bringing down Snowflake internal storage cost from ~$23/TB/month to S3 infrequent access with ~$12.50/TB or S3 Glacier Deep Archive with only ~$1/TB.


Another handy side effect as the consumer of external table data is that the **data is always up to date**, because no refresh or update is needed. It goes without saying that this has its own downsides and can be a problem for the owner of the data if it’s used in production and the ETL process reads large amounts of data through external tables. This will affect upstream apps running or owning this data.


That’s why many use external tables in combination with materialized views (MVs) to truncate and recreate a daily snapshot (or similar) during off-peak (mostly nights) of this data, avoiding affecting production data and even optimizing query performance with added indices for downstream queries.


### When Internal and When External Data? What’s the Limit of External?


The tradeoffs come down to how often the data is queried, e.g. the hot versus cold question.


The tradeoffs and considerations you should make when wanting to use them come down to the decision of how often the data is queried. The table below shows it in more detail:



| Dimension | **Internal Storage** | **External Tables** |
| Temperature | **Hot**: recent data, lasts weeks to months | **Cold**: archival or infrequently touched |
| Typical use case | Dashboards, frequent queries, sub-second latency | Archival, ad-hoc exploration, augmenting a data lake |
| Query speed | Fast, optimized for repeated access | Slower (a 1.3×–1.7× tax in the below dashboard benchmark) |
| Storage cost | Higher (warehouse-managed, ~$23/TB on Snowflake capacity) | Lower: up to ca. 20× cheaper on S3 Glacier Deep Archive (~$1/TB) |
| Data freshness | Can go stale between ETL refreshes | Always up to date, no refresh needed |
| Setup effort | Requires ETL pipelines, scripts or re-ingestion | Simple DDL-only definition, data stays in place |
| Scaling concern | Disk grows faster than compute needs | Heavy reads can affect upstream apps owning the source files |
| Operational overhead | Predictable, managed by the warehouse | Small-file problem and manifest management for tiny or streaming datasets |



In the era of data lake and lakehouse architectures, this is an important consideration. VSCO [says](https://eng.vsco.co/querying-s3-data-with-redshift-spectrum/): “disk space was growing more quickly than our compute needs,” which is what triggered the adoption of external tables.


If you look at your use case, if you need to do analytics across various sources with joins and augmentation of your data at an enterprise, you probably want to focus on loading data into your database or data warehouse, an architectural pattern that has survived more than 30 years. But if you have data that is external and small but you want to join it with existing data, or you always need fresh data and can live with a slower response time (maybe because it runs during the night), you might use external tables.


In any case, external tables are a good approach to keep in mind and a valuable [toolkit](https://motherduck.com/blog/data-engineering-toolkit-essential-tools/) to have.


### They Work Well with Existing Tech and Common Patterns


Obviously, today’s external tables are not the same as the earliest ones in Microsoft Access, but the principle of accessing data outside your system is still the same. Nowadays we have more support, new formats besides CSV and JSON. We can do Parquet or open table formats.


As mentioned, they work well with related long-lasting data warehouse patterns and applications such as materialized views and stored procedures. The recurring pattern is to access external data with your data management system, similar to the pattern of materialized views that refresh complex SQL statements and make them fast, and stored procedures that run glue code within your database.


Moreover, there are temporary tables that are similar but only available during a transaction or session. They all work in the same Lindy effect, e.g., Databricks just [announced Temporary table support](https://www.databricks.com/blog/introducing-temporary-tables-databricks-sql) recently on December 9th, 2025, or Databricks SQL Stored Procedure a [little earlier](https://www.databricks.com/blog/introducing-sql-stored-procedures-databricks), August 14th, 2025, for reusing existing SQL statements.


Again and again, **everything that is old will be new again**. Exactly what the Lindy Effect is all about. We can clearly say that the Lindy effect over the last 33 years applies here. The longer something is in place, the more likely it is to be around for at least that long.

External vs. Temporary Table

In contrast: temp table = session-scoped, writable, fast, invisible to others, auto-dropped. External table = persistent metadata, read-only, infinite size, visible to all, optimized for cost.


A common chain in practice is going from: `external table → temp/transient table → permanent managed table`.


### How a Classical External Table Works


To understand how traditional external tables work, let’s first look at Oracle, which has built an extensive syntax around them and where they still work this way today.


First, we can create a place for external data called `DIRECTORIES`, which is simply a pointer or alias to a file system location where external files already exist:



| `1
2
` | `CREATE OR REPLACE DIRECTORY admin_dat_dir
    AS '/flatfiles/data';
` |



This directory can point to local file systems, NFS mounts, or even cloud object storage today (with the `ORACLE_BIGDATA` driver for S3, OCI, Azure). The `DIRECTORIES` don’t require moving data, though you could prepare those files via ETL pipelines or third-party tools, or they can be generated directly by applications.


We can now create an external table based on this directory, e.g., log files, bad data that we store externally, JSON files, and make data accessible inside the [INFORMATION_SCHEMA](https://en.wikipedia.org/wiki/Information_schema) and with plain SQL, as if it were internal.


Creating an external table:



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
` | `CREATE TABLE admin_ext_employees
                   (employee_id       NUMBER(4), 
                    first_name        VARCHAR2(20),
                    last_name         VARCHAR2(25), 
                    job_id            VARCHAR2(10),
                    manager_id        NUMBER(4),
                    hire_date         DATE,
                    salary            NUMBER(8,2),
                    commission_pct    NUMBER(2,2),
                    department_id     NUMBER(4),
                    email             VARCHAR2(25) 
                   ) 
     ORGANIZATION EXTERNAL 
     ( 
       TYPE ORACLE_LOADER 
       DEFAULT DIRECTORY admin_dat_dir  --notice this dir with above
       ACCESS PARAMETERS 
       ( 
         records delimited by newline 
         badfile admin_bad_dir:'empxt%a_%p.bad' 
         logfile admin_log_dir:'empxt%a_%p.log' 
         fields terminated by ',' 
         missing field values are null 
         ( employee_id, first_name, last_name, job_id, manager_id, 
           hire_date char date_format date mask "dd-mon-yyyy", 
           salary, commission_pct, department_id, email 
         ) 
       ) 
       LOCATION ('empxt1.dat', 'empxt2.dat') 
     ) 
     PARALLEL 
     REJECT LIMIT UNLIMITED; 
` |



The first and most important choice is `TYPE`, which determines the access driver and what kind of files you can read: `ORACLE_LOADER` for plain text files like CSV or logs (read-only), `ORACLE_DATAPUMP` for Oracle binary dump files, `ORACLE_BIGDATA` for cloud object stores like S3 or OCI in formats like Parquet or Avro, and `ORACLE_HIVE` for Hadoop/Hive data. The `DEFAULT DIRECTORY` points to a server-side path alias, and `LOCATION` names the actual file(s), with wildcard support (`*.dat`) so you can load a whole batch at once.


The `ACCESS PARAMETERS` block is where you control parsing: row and field delimiters, null handling, custom date format masks, and where to write bad rows (`badfile`) and parse logs (`logfile`). On top of that, `PARALLEL` lets Oracle split file reading across multiple processes for large files, and `REJECT LIMIT` controls fault tolerance. Set it to `UNLIMITED` to skip bad rows silently, or `0` to fail immediately on the first error.


You see lots of built-in features that we can use compared to building a full-fledged data pipeline. Instead of exporting and importing CSVs from the source databases or developing a complex CDC pipeline that traditionally looked something like: `source OLTP --> CSVs --> IDW (reports on yesterday) -> ingest into DWH for long-term analytics`, we can just define a table based on external data and access it as part of our pipeline.

The INFORMATION_SCHEMA analogy

You are probably familiar with the INFORMATION_SCHEMA of a database. It’s the **internal data catalog** that most databases provide and it contains a **list of all tables and all metadata** such as columns, data types, etc. The neat thing is that external tables will show up as internal tables once defined.


## What’s the Modern Version of External Tables Today?


To preface: the previous Oracle example shows the `CREATE EXTERNAL TABLE` syntax, and a first-class DDL object in the data catalog. What follows in this chapter is the next evolution, where external tables are not necessarily created with DDL, but in another way, achieving the same outcome of querying data in place without loading it. Let’s see what these are.


### Integrated into Warehouses


Most modern warehouses - Snowflake, Redshift Spectrum, BigQuery, Athena, Synapse - come with a simplified version of `CREATE EXTERNAL TABLE`. Compared to the Oracle example, the schema is usually inferred from the file format (especially Parquet), S3 or another object store is the default backing location, and the parsing ceremony disappears. The pseudo-code looks roughly like this across engines:



| `1
2
3
4
5
6
` | `-- Pseudo-code: modern external table over Parquet on S3
CREATE EXTERNAL TABLE sales
WITH (
  LOCATION = 's3://my-bucket/sales/',
  FORMAT = 'PARQUET'
);
` |



Object storage like S3, GCS, and Azure Blob has become the first-class citizen for external data. From here, the ecosystem layers on: dbt wraps this in YAML, DuckDB skips the DDL entirely in favor of schema-on-read, and open table formats add transactional guarantees on top.


### External Tables with dbt?


On top of this base SQL form, dbt adds a YAML layer and can be used with its own package called [`dbt-external-tables`](https://github.com/dbt-labs/dbt-external-tables). It’s one of the most-used dbt packages, though it seems less actively maintained now.


The external table is defined via YAML, and there are lots of options to set, with the most important being `external` and its `location`, but also defining `columns` in different ways such as inference or the `meta` tag:



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
38
39
40
` | `version: 2

sources:
  - name: snowplow
    tables:
      - name: event
        description: >
            This source table is actually a set of files in external storage.
            The dbt-external-tables package provides handy macros for getting
            those files queryable, just in time for modeling.
                            
        external:
          location:         # required: S3 file path, GCS file path, Snowflake stage, Synapse data source
          ...               # database-specific properties of external table
          partitions:       # optional
            - name: collector_date
              data_type: date
              ...           # database-specific properties

        # Specify ALL column names + datatypes.
        # Column order must match for CSVs, column names must match for other formats.
        # Some databases support schema inference.

        columns:
          - name: app_id
            data_type: varchar(255)
            description: "Application ID"
          - name: platform
            data_type: varchar(255)
            description: "Platform"
          ...

        # Use `meta` to pass custom column properties (e.g. alias, expression)
        columns:
          - name: raw_timestamp
            data_type: timestamp
            config:
              meta:
                alias: event_timestamp       # rename the column in the external table
                expression: TO_TIMESTAMP(...) # custom SQL expression instead of default value extraction
` |



This is a nice improvement over the ODBC GUI interface. It’s not exactly an apples-to-apples comparison as dbt itself is not a database, but with its supported destinations such as Redshift (Spectrum), Snowflake, BigQuery, Spark, Synapse, and Azure SQL, you see that it will persist in these destinations, mostly data warehouses.


### DuckDB with dbt


If you use dbt, you can also use DuckDB with dbt via [dbt-duckdb](https://github.com/duckdb/dbt-duckdb), which is more up-to-date. But DuckDB is not an external table, right?


Yes, DuckDB doesn’t have `CREATE EXTERNAL TABLE` syntax [yet](https://github.com/duckdb/duckdb/discussions/14422), mostly because it is an in-memory database, but you can achieve the same functionality through other means. DuckDB can not only be used as a database but also as a zero-copy SQL connector (see all categories at [5 Key Categories](https://www.ssp.sh/blog/enterprise-case-duckdb-key-categories/)). We can just point it to an external source, as shown above with dbt. The difference is that DuckDB is both a database and a compute engine, making ad-hoc reads possible directly without a DDL definition, similar to an external table with Oracle loaders. With dbt, we can nicely declare this in dbt configs.


With DuckDB, you can query “external data” extremely fast over HTTPS or locally in formats such as Parquet, CSV, and [many more](https://duckdb.org/docs/current/data/data_sources), so the need for formal external tables is reduced since DuckDB does **schema on read**.


If you want to define the database schema ahead of time, we’d use external tables to do that and effectively have **schema on write** (though we don’t write, just define the DDL table structure and data types), which is more of the classical ETL approach.


Here’s an example with `external_location` to read external data with dbt:



| `1
2
3
4
5
6
` | `sources:
  - name: external_source
    config:
      external_location: "s3://my-bucket/my-sources/{name}.parquet"
    tables:
      - name: source1
` |



Read more at [Fully Local Data Transformation with dbt and DuckDB](https://duckdb.org/2025/04/04/dbt-duckdb).


Other options are with database views that are supported in DuckDB with **`CREATE VIEW` over `read_parquet()`**. You can ship a .duckdb file to clients with pre-defined views over S3 data, so clients don’t need to know about the underlying data, Hive partitioning, or even glob patterns — very similar to what a formal `CREATE EXTERNAL TABLE` would do.



| `1
2
` | `CREATE VIEW events AS
  SELECT * FROM read_parquet('s3://lake/events/*.parquet', hive_partitioning=true);
` |



Or similarly use `ATTACH` to directly point to Postgres, MySQL, SQLite, S3, and others:



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
` | `-- Postgres (binary wire protocol, predicate + projection pushdown, read+write)
INSTALL postgres; LOAD postgres;
ATTACH 'dbname=postgres user=postgres host=127.0.0.1' AS pg (TYPE postgres);
ATTACH 'postgresql://user@host/db' AS pg (TYPE postgres, READ_ONLY);

-- MySQL (via MariaDB Connector/C; Postgres-style keyvalue string even for MySQL — easy trap)
INSTALL mysql; LOAD mysql;
ATTACH 'host=localhost user=root port=0 database=mysql' AS mdb (TYPE mysql);

-- SQLite (file opens directly; multi-reader single-writer by SQLite file locks)
INSTALL sqlite; LOAD sqlite;
ATTACH 'sakila.db' (TYPE sqlite);

-- Generic remote DuckDB file
ATTACH 's3://duckdb-blobs/databases/stations.duckdb' AS stations_db;
` |



### Open Table Formats and Lakehouse Architecture


That begs the question of whether [Open Table Formats](https://motherduck.com/blog/open-lakehouse-stack-duckdb-table-formats/) are the next evolution and modern way of external tables. These table formats allow almost any SQL compute engine to use them as external tables, and read, compute, and aggregate as a database would.


If we look at what table formats consist of, they’re built on object storage, with a file format like Parquet, and then we have a manifest file that contains a list of files that **unifies multiple single files into a “single” table**, looking from the outside.


So again, the manifest file is our pointer or fancier symlink, but it lives next to the data, unlike external tables. There’s much more going on in table formats, but if we have a **data lake with open table format tables**, we can see how we define tables in DDL and the **pointers are to different files** (Parquet, ORC, Avro), in most cases Parquet.


More broadly, we can say external tables decouple storage from compute. Open table formats decouple the table itself (schema, history, transactions, statistics) from any single engine.


### Lakehouse and Connecting to DuckLake


One step further is obviously a lakehouse architecture, with the shift from *format-agnostic file reading* to *governed, transactional, multi-engine open table formats*.


If you extend the external table idea to a [lakehouse architecture](https://motherduck.com/blog/from-data-lake-to-lakehouse-duckdb-portable-catalog/), these external tables with open table formats provide essentially what databases provide with ACID guarantees, time travel, schema evolution, partition evolution, and fine-grained access control, but for files.


But with the difference that data stays in open Parquet file format on customer-owned cloud storage. The external table, once a humble workaround for avoiding data loads, has become the architectural foundation of the data lakehouse if you like this analogy.


With [DuckLake](https://ducklake.select/), we have the next evolution just around the corner, bringing back exactly that missing database, especially to handle all the metadata of such a lakehouse and all its files. This means having durable and consistent database storage for our [manifest files](https://iceberg.apache.org/spec/#manifests).


#### Open Data Catalog to Complete the Picture: The ODBC Glue


With all these evolutions, we’ve come far. When adding an [Open Data Catalog](https://www.ssp.sh/brain/open-table-format-catalogs), we are exactly where we started: having an INFORMATION_SCHEMA, a dictionary with all our tables, in this case the open table format tables.


It’s the **glue that ODBC provided when connecting a BI tool to the underlying database**. Now you’d like to have an open data catalog that, in the best-case scenario, gives you all the tables and ways to connect.


But then again, the syntax of `EXTERNAL TABLES` still gets added, and [ADBC](https://arrow.apache.org/docs/format/ADBC.html) and DuckDB are doing a great job of using external data without needing a data lake and its technology stack altogether. For example, DuckDB has support for [ODBC](https://duckdb.org/docs/current/core_extensions/odbc/overview), [ADBC](https://duckdb.org/docs/current/clients/adbc) and even [JDBC](https://duckdb.org/docs/current/clients/java). That matters especially for 3rd-party tools: ADBC streams Apache Arrow end-to-end instead of serializing row-by-row, so BI tools and notebooks can pull millions of rows directly from external Parquet tables at speeds that previously required keeping data “hot” in a cloud data warehouse. 🙂

ADBC, what is that?

ODBC is 30+ years old, and we have a newer, faster version of it, called [ADBC](https://arrow.apache.org/docs/format/ADBC.html). It’s a faster way to connect to other databases with a columnar-oriented API instead of **row-by-row serialization**, heavily making use of Apache Arrow.


While ADBC is newer, it tries to support the same drivers as ODBC, but faster and easier to install. E.g., it has a handy [dbc](https://github.com/columnar-tech/dbc) CLI to install it on almost any programming language, so no more manual and error-prone Windows GUI ODBC downloading of drivers and definitions needed, just one CLI command.

Using MotherDuck

If you want a data warehouse that just works, integrates well with DuckDB, and has support for DuckLake, you can always use managed MotherDuck. You can build a classical data warehouse with plain SQL, you can read external data easily with DuckDB or dbt-duckdb, or [integrate with DuckLake](https://motherduck.com/blog/announcing-ducklake-1-0-on-motherduck/).


It works great [with agents](https://motherduck.com/blog/motherduck-agent-skills/). Check out MotherDuck’s [agent-skills](https://github.com/motherduckdb/agent-skills/) for opinionated AI skills for building applications with MotherDuck. And [visualize with Dives](https://motherduck.com/product/dives/) with one prompt.


## Which Is Faster? A Quick Benchmark


To put numbers behind the hot/cold decision, I ran a simple benchmark on the TPC-H SF=1 `lineitem` table (6M rows, ~150 MB), stored four ways: inside a DuckDB file (internal), as raw Parquet, as an Iceberg table, and as a DuckLake table. Full code: [`bench2.py`](https://github.com/sspaeti/external-table-benchmark/blob/main/bench2.py) and [`metadata_bench.py`](https://github.com/sspaeti/external-table-benchmark/blob/main/metadata_bench.py).


**Dashboard workload (hot path)**: 3 queries × 10 repeats:



| Backend | Tier | Median | p95 | vs internal |
| Internal (DuckDB) | hot | 23.8 ms | 235 ms | **1.0×** |
| DuckLake | cold | 45.1 ms | 269 ms | 1.3× |
| External Parquet | cold | 41.3 ms | 271 ms | 1.4× |
| External Iceberg | cold | 56.1 ms | 377 ms | 1.7× |



Internal is fastest; external pays a 1.3×–1.7× tax. But for **cold/archival queries** (one-off, no warmup), all four backends answered in under 150 ms. The speed difference effectively vanishes for data you query once a week.


**Storage cost** is where external tables shine. Columnar Parquet is ~40% smaller than native DuckDB format. Ten TB of archive data costs roughly ~$125/month on S3 Infrequent Access or ~$10/month on Glacier Deep Archive, versus ~$230/month inside Snowflake on capacity pricing. This is the economic case external tables were invented for, and it still holds.


**Metadata workload** is where DuckLake stands out. Fifty single-row inserts showed DuckLake creating **zero data files** (rows inlined in the catalog) versus Iceberg’s **352 files** (201 data + 151 metadata). That’s the “small file problem” made concrete: at one write per second, Iceberg creates ~86,400 files per day needing compaction. DuckLake creates zero until you checkpoint. DuckDB Labs’ own benchmarks report up to [926× faster queries](https://ducklake.select/2026/04/02/data-inlining-in-ducklake/) on streaming workloads.


## So Should You Use External Tables?


So after all this, should you use external tables today? After seeing how sticky they’ve been since Oracle 9i in 2001, how they keep getting re-added to newer tools (Snowflake in 2021, Databricks Unity Catalog, BigLake in 2022), and how their core benefit is. Accessing data where it lives without moving it, via a simple DDL statement, has only grown more valuable as formats have evolved from CSV to Parquet, JSON, Avro, and now open table formats. I’d say yes. But choose wisely based on your data’s temperature: use internal storage for hot data, such as dashboards and frequently used queries.


Use external tables for cold data, archival workloads, and ad-hoc exploration, where that gap vanishes, and storage costs plummet (up to 20× cheaper on Glacier Deep Archive vs. warehouse-managed storage). And if you already use dbt, DuckDB, or a lakehouse stack, the modern versions are right there. Where they’re the *wrong* choice is the inverse: transactional workloads, queries that need sub-second latency on every run, or data so small that the operational overhead of an external stage outweighs the benefit of not loading it.


The evolution is worth naming explicitly: “read CSVs on disk” → “read Parquet on HDFS” → “read Parquet on S3 via a metastore” → “read Iceberg/Delta tables with ACID on S3” → “the Iceberg table *is* the warehouse table”. Each step kept the core idea (data stays where it lives, metadata describes it, SQL queries it) and added database semantics back in. With open data catalogs, the warehouse becomes a **stateless rental over a bucket you own**, and external tables are increasingly managed. DuckLake demonstrates this best: when the catalog has SQL-DB-like guarantees, the distinction between “external” and “internal” dissolves. The metadata benchmark made this concrete by reading a single indexed row rather than walking a manifest tree.


The **database semantics are returning** with DuckLake, managed Iceberg, and predictive optimization, all of which reintroduce RDBMS-style guarantees to the lake. The cycle from “external table for cheap storage” to “external table as a full ACID database on S3” took 25 years, completing the journey back to database principles while maintaining the separation of storage and compute. You can say **the modern external table isn’t external anymore**. DuckDB reads them directly, and DuckLake handles the metadata that multifile lakehouse architectures would otherwise drown in. The lesson from history is that whenever someone tries to replace it, the pattern is that reading data in place always beats moving it. And the Lindy Effect suggests that if external tables have lasted 25 years and get re-added, they’ll persist another 25. They’re probably not going anywhere. 🙂


---


```
Full article published at MotherDuck.com - written as part of my services
```


---

1. A so-called loader that lets you access the data via a driver: see the ORACLE_LOADER Access Driver example: [https://docs.oracle.com/en/database/oracle/oracle-database/12.2/sutil/oracle_loader-access-driver.html](https://docs.oracle.com/en/database/oracle/oracle-database/12.2/sutil/oracle_loader-access-driver.html) ↩︎
2. Also see the latest release notes of BigQuery from April 2026; lots of it has to do with “external catalogs” and also BigQuery Apache Iceberg external tables now support Iceberg version 3: [https://docs.cloud.google.com/bigquery/docs/release-notes#April_21_2026](https://docs.cloud.google.com/bigquery/docs/release-notes#April_21_2026) ↩︎
3. Customers can also choose to create materialized views on external tables to speed up the query performance significantly. ↩︎

[Discuss on Bluesky](https://bsky.app/search?q=domain%3A%20https://www.ssp.sh/blog/modern-external-tables-and-evolution/)
|
[External-Tables](https://www.ssp.sh/tags/external-tables/)
[Oracle](https://www.ssp.sh/tags/oracle/)
[Ducklake](https://www.ssp.sh/tags/ducklake/)
[Duckdb](https://www.ssp.sh/tags/duckdb/)
[Lakehouse](https://www.ssp.sh/tags/lakehouse/)
[Open Table Format](https://www.ssp.sh/tags/open-table-format/)
[Data Warehouse](https://www.ssp.sh/tags/data-warehouse/)
[Object-Storage](https://www.ssp.sh/tags/object-storage/)
[Cloud Data Warehouse](https://www.ssp.sh/tags/cloud-data-warehouse/)
[Dbt](https://www.ssp.sh/tags/dbt/)
[Motherduck](https://www.ssp.sh/tags/motherduck/)
[Services](https://www.ssp.sh/tags/services/)
