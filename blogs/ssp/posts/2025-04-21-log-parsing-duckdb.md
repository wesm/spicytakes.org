---
title: "The Data Engineer's Guide to Efficient Log Parsing with DuckDB/MotherDuck"
date: 2025-04-21
url: https://www.ssp.sh/blog/log-parsing-duckdb/
slug: log-parsing-duckdb
word_count: 5411
---

![The Data Engineer's Guide to Efficient Log Parsing with DuckDB/MotherDuck](https://www.ssp.sh/blog/log-parsing-duckdb/featured-image.png)

Contents
This article was written as part of
[my services](https://www.ssp.sh/services)

As data engineers, we spend countless hours combing through logs - tracking pipeline states, monitoring Spark cluster performance, reviewing SQL queries, investigating errors, and validating data quality. TheseÂ **logs are the lifeblood of our data platforms**, but parsing and analyzing them efficiently remains a persistent challenge. This comprehensive guide explores whyÂ **data stacks are fundamentally built on logs**Â and why skilled log analysis is critical for the data engineer’s success.


Throughout this article, we’ll categorize the various log types and formats you’ll encounter in your daily work, compare popular analysis tools, and most importantly, demonstrate practical, code-driven examples of parsing complex logs using DuckDB. You’ll see how DuckDB’s super fast parsers and flexible SQL syntax make it an ideal tool for log analysis across various formats including JSON, CSV, and syslog files.


For those working with larger datasets, we’ll also show how to analyze massive JSON log datasets at scale with MotherDuck, providing optimized query patterns for common log analysis scenarios. Whether you’re troubleshooting pipeline failures, monitoring system health, or extracting insights from operational metadata, this guide will help you transform log analysis from a tedious chore into a powerful competitive advantage for your data team.


## Understanding Log Types and Their Purpose in Data Engineering


The questions would be, “**What are we using logs for?**”, “What information is there?”, and “What are these logs specifically for?” for data engineering workloads.


### Categories of logs (application logs, system logs, etc.)


There are various logs. To better understand them, we need to know who is producing them. Let’s look at theÂ **categories**Â of logs and the file formats they are usually in.


From a high-level perspective, we have different domains like application logs, system logs, error logs, and transaction logs:Â


![/blog/log-parsing-duckdb/different-categories.png](https://www.ssp.sh/blog/log-parsing-duckdb/different-categories.png)

*Different categories of LogFiles | Image fromÂWhat is a Log File?*


As a data engineer, you’ll typically need to analyzeÂ **several types of logs**Â to monitor, troubleshoot, and optimize data pipelines and systems.


Besides there being many more logs (like Security, Perimeter Device, Windows or Endpoint Log and many more), these are the major logs you’ll encounter most of the time:

- Operational Logs:
- Data Management Logs:
- Security and Access Logs:


#### Different Types of Metadata


On a high level, we have different types of Metadata: social, technical, business, and operational. What we, as data engineers, mostly deal with are operational logs like job schedules, run times, data quality issues, and, most critically, error logs.


![/blog/log-parsing-duckdb/different-types-metadata.png](https://www.ssp.sh/blog/log-parsing-duckdb/different-types-metadata.png)

*Different types of metadata | Image byÂEckerson Group on LinkedIn*


These operational data logs are called pipeline and execution metadata logs. They have certain formats and types (technical aspect), contain business terms in some cases, and have some social and business impact on the people and the organization.

A new emerging term: Meta Grid
There is also a newer term called Meta Grid, see the bookÂ
[Fundamentals of Metadata Management](https://www.oreilly.com/library/view/fundamentals-of-metadata/9781098162818/)
Â by Ole Olesen-Bagneux that talks about metadata in a deeper way andÂ
[compares it to data mesh and microservices architectures](https://olesenbagneux.medium.com/the-meta-grid-is-the-third-wave-of-data-decentralization-b18827711cec)
.

Let’s now look at how these logs appear and what formats they use.


### Data Types and Formats of Data Logs


What information does a log typically hold? Log files hold various data types, but two are always present: timestamp and someÂ **log, error or message**.


Further columns could include a user, event type (like a specific action or occurrence that triggered it), or running application (e.g., started within Airflow). Others include system errors and any metadata that helps debug the errors.


These logs come in all shapes, styles, and formats. Most common areÂ **structured logs**Â for metadata as JSON or key-value pairs andÂ **plaintext-based logs**Â for execution sequences often in syslog-like formats. The JSON format has the advantage of a flexible schema, meaning columns can change each time, and the producers don’t need to think about types or fit into a pre-defined structureâleaving that job to the analyst later.


A range of different log formats is shown below.


#### Structured Formats

- JSON: Most common. JSON provides a hierarchical structure with nested objects and arrays, making it ideal for complex logging needs while remaining machine-parsable.



| `1
2
3
4
5
6
7
8
9
` | `{
"timestamp": "2024-11-19T08:15:12Z",
"level": "INFO",
"service": "data-pipeline",
"message": "ETL job completed",
"job_id": "12345",
"records_processed": 10000,
"duration_ms": 45000
}
` |


- **CSV/TSV**: Used for logging tabular data. This format is compact and easily imported into spreadsheet software or databases, though it lacks descriptive field names unless headers are included.



| `1
` | `2024-11-19 08:15:12,INFO,data-pipeline,ETL job completed,12345,10000,45000
` |


- **Key-Value Pairs**: Common in many logging systems. This format offers a good balance between human readability and machine parseability while remaining flat and avoiding the overhead of more structured formats.



| `1
` | `timestamp=2024-11-19T08:15:12Z level=INFO service=data-pipeline message="ETL job completed" job_id=12345 records_processed=10000 duration_ms=45000
` |



#### Semi-structured Formats

- **[Syslog Format](https://en.wikipedia.org/wiki/Syslog)**: A standardized format that includesÂ a priority field, a header with information like timestamps and hostnames, and the actual message content.Â This format allows for centralized logging and easy analysis of logs across different systems and applications.



| `1
` | `Nov 19 08:15:12 dataserver01 data-pipeline[12345]: ETL job completed successfully
` |



#### Common Event Format (CEF)

- **CEF**:  Used in security and event management systems. This vendor-neutral format was developed by ArcSight and has become widely adopted for security event interchange between different security products and security information and event management (SIEM) systems.



| `1
` | `CEF:0|Vendor|Product|Version|Signature ID|Name|Severity|Extension
` |



#### `.log`Â File


The .log-file is a common file extension used for logging data, butÂ **not a format itself**. TheÂ `.log`Â extension indicates that the file contains log information, while the actual content could be any of the previously mentioned formats.


## Why Data Stacks Are Built on Logs


As data engineers, we have to deal with all of these various log types and formats because our data pipelines touch the full lifecycle of a business. From reading from many different source systems with potential network latencies or issues, to loading large tables that need more performance, to the whole ETL process where we transform data and need to make sure we don’t compromise granularity or aggregated KPIs with duplications or incorrect SQL statements.


Data stacks and dataÂ **platforms are essentially built around logs**. We can’t debug the data stack; the logs are our way to find the error later on. Software engineers can debug more easily, as they are in control of what the user can and can’t do. But data is different, constantly changing and flowing from A to B. We have external producers that we can’t influence, and the business and requirements are changing too.


On the consumer side, we have the visualization tools that need to be fast and nice looking. We have security, data management, DevOps on how we deploy it, the modeling and architecture part, and applying software engineering best practices along with versioning, CI/CD, and code deployments. All of this happens under the umbrella of data pipelines and is part of theÂ [Data Engineering Lifecycle](https://www.oreilly.com/library/view/fundamentals-of-data/9781098108298/ch02.html). On each level, we can have different data logs, performance and monitoring logs, data quality checks, and result sets of running pipelines with their sub-tasks.


That’s why our data stacks run on metadata, and they are as important today as they were two decades ago. However, with more sophisticated tools, we can now analyze and present them more efficiently.

Data Orchestration Trends Relating to Logs
In theÂ
[Data Orchestration Trends: The Shift From Data Pipelines to Data Products](https://airbyte.com/blog/data-orchestration-trends)
, I highlighted how the trends of pipelines shifted more towards declarative and data products, which also influences our logging. With a code-first approach (
**Data-as-Code**
) to data, we can implement reactive logic to logs in a declarative manner. More concretely, we can define annotations of a data pipeline that only runs if a log hasÂ
Â written in the log. This is possible with non-declarative and UI-first solutions too, but it is more natural for the code-first solution.

### Log Analysis Use Cases and When to Use Log Files


What are we doing when we analyze logs? Data engineers typically focus on several key use cases:


**Debugging**Â is the most common use case. As we can’t simply use a debugger with complex data pipelines, we mustÂ **log our way through problems**. Good logs shouldÂ **identify**Â errors clearly. Since we work with complex business logic most of the time, on top of the technical stack, this requires significant expertise from data engineers and is where we can spend much of our time. But the better the logs, the less we need to search, and the more we can focus our time on fixing the bugs.


**Tracing**Â helps pinpoint the origin of errors in pipelines with many sub-tasks, whileÂ **performance analysis**Â uses logs from BI tools or orchestrators like dbt to identify bottlenecks.


**Error pattern analysis**Â examines changes over time to prevent recurring issues.


ForÂ **monitoring**, we often load logs into tools likeÂ [DataDog](https://www.datadoghq.com/),Â [Datafold](https://www.datafold.com/),Â [ELK Stack](https://www.elastic.co/elastic-stack), orÂ [InfluxDB](https://www.influxdata.com/use-cases/monitoring/), standardize metrics withÂ [Prometheus](https://prometheus.io/), and visualize usingÂ [Grafana](https://grafana.com/). For more, see the next chapter.


### Tools and Solutions for Effective Log Analysis


The tools we use to analyze the logs have changed over time and have become more numerous but also better in quality. Traditionally, we had to do all the log reporting manually. More recently, however, we have monitoring and observability tools with dedicated log analyzer capabilities included. These vary in their specific use cases, but all of them analyze some kind of log.


Here’s an overview of some of the different tools, categorized in these two domains: log and monitoring/observability, and the degree of automation and manual effort required. You also see the green mark if the tool is open-source or not.


![/blog/log-parsing-duckdb/log-parsing-observability-monitoring.webp](https://www.ssp.sh/blog/log-parsing-duckdb/log-parsing-observability-monitoring.webp)

*Cluster of log parsing and monitoring/observability tools categorized into the degree of automation | Image by the author*


These tools fall into several categories:

- **Auto-profiling solutions**Â like Bigeye, Monte Carlo, and Metaplane offer automated monitoring with unique features ranging from ML-driven alerts to enterprise data lake integrations
- **Pipeline testing tools**Â such as Great Expectations, Soda, and dbt tests provide granular validation within data workflows
- **Infrastructure monitoring platforms**Â including DataDog and New Relic focus on system health and resource utilization
- **Hybrid solutions**Â like Databand and Unravel unify infrastructure monitoring with data-specific observability

Side-Note: Kafka Event-Driven Use-Cases
While event streaming platforms like Kafka also use logs, this article focuses on pipeline error and trace logs rather than event-driven architectures. For Kafka analysis, tools likeÂ
[kwack](https://github.com/rayokota/kwack)
Â andÂ
[sql-flow](https://github.com/turbolytics/sql-flow)
Â provide specialized capabilities.

### DuckDB as the Ultimate Log Parser?


But how about using DuckDB as a log parser? Let’s imagine we have all the logs parked on an S3 storage or somewhere in our data warehouse. DuckDB is a very efficient tool for quickly analyzing the overall status.


Whereas the above tools are doing real-time monitoring mostly, analyzing what is happening every second and minute, DuckDB can be used to have analytics for theÂ **overall state**. We can have advanced log analysis techniques such as:

- Time-series analysis of log data
- Combining logs from multiple sources
- Creating dashboards and monitoring systems


DuckDB is theÂ **ultimate log parser**. It can run with zero-copy, meaning you don’t need to install or insert logs into DuckDB, but you can read from your data lake in S3, from your Snowflake Warehouse, and from your servers via HTTPS server, all within a single binary.


DuckDB has one of the fastest JSON and CSV parsers. This comes in very handy, as we learned that most logs are in these exact formats. The ability to query multiple file formats with consistent SQL syntax and the local processing capabilities that reduce network overhead are just two other big advantages that make DuckDB a great tool for log parsing.


With the extension of MotherDuck, we can simply scale the log analysis in case DuckDB can’t handle it, when we want to share quick analytics with a notebook, or when we want to share the data as a shared DuckDB database. You can scale up your parser without making the code more complex, just using a different engine with the same syntax and understanding as DuckDB itself.


## Practical Log Analytics: Analyzing Logs with DuckDB and MotherDuck


Below, we have a look at two datasets: the first one with various formats and the second real-life JSON from Bluesky to benchmark larger log analytics.


### Parsing Various Log Formats with DuckDB


Before we go any further, let’s analyze some logs to get a better understanding of what logs are and how they can look. The idea is to analyze completely different log files to understand how to parse them all with DuckDB using various strategies.

Data Sets Used in This
The data sets used in this part are from two open data sets ofÂ
[Loghub](https://github.com/logpai/loghub)
Â that provides a large collection of system logs and datasets for log analytics. See download links below.

## Practical Log Analytics: Analyzing Logs with DuckDB and MotherDuck


Below, we have a look at two datasets: the first one with various formats and the second real-life JSON from Bluesky to benchmark larger log analytics.


### Parsing Various Log Formats with DuckDB


Before we go any further, let’s analyze some logs to get a better understanding of what logs are and how they can look. The idea is to analyze completely different log files to understand how to parse them all with DuckDB using various strategies.

Data Sets Used in This
The data sets used in this part are from two open data sets of
[Loghub](https://github.com/logpai/loghub)
that provides a large collection of system logs and datasets for log analytics. See download links below.

#### Parsing one big Apache Logs: From Unstructured Text to Actionable Insights


In this first example, we analyze one large log file with 56,481 lines and 4.90MB called `Apache.log` (it is compressed in `.gz`). The size is small, but the log is semi-structured like this, where we have the timestamp, error type, and message. There are also outliers we need to deal with:



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
` | `[Fri Jun 10 11:32:39 2005] [notice] mod_security/1.9dev2 configured
[Fri Jun 10 11:32:39 2005] [notice] Apache/2.0.49 (Fedora) configured -- resuming normal operations
[Fri Jun 10 11:32:39 2005] [notice] jk2_init() Found child 2337 in scoreboard slot 1
[Fri Jun 10 11:32:39 2005] [notice] jk2_init() Found child 2338 in scoreboard slot 2
[Fri Jun 10 11:32:39 2005] [notice] jk2_init() Found child 2339 in scoreboard slot 3
[Fri Jun 10 11:32:39 2005] [notice] jk2_init() Found child 2342 in scoreboard slot 6
[Fri Jun 10 11:32:39 2005] [notice] jk2_init() Found child 2343 in scoreboard slot 7
script not found or unable to stat
[Fri Jun 10 11:32:39 2005] [notice] jk2_init() Found child 2340 in scoreboard slot 4
[Fri Jun 10 11:32:39 2005] [notice] jk2_init() Found child 2341 in scoreboard slot 5
` |



Remember, this is a good opportunity to use an LLM. If you give it the schema description with the first 100 lines, it can do an excellent job of helping us create complex RegExp patterns to parse otherwise randomly looking log files such as the `Apache.log` above. That is exactly what I used initially to generate this:



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
` | `SELECT 
    regexp_extract(line, '\[(.*?)\]', 1) AS timestamp,
    regexp_extract(line, '\[error\]', 0) IS NOT NULL AS is_error,
    regexp_extract(line, '\[client (.*?)\]', 1) AS client_ip,
    regexp_extract(line, '\](.*)', 1) AS message
FROM read_csv('https://zenodo.org/records/8196385/files/Apache.tar.gz?download=1', 
    auto_detect=FALSE, 
    header=FALSE, 
    columns={'line':'VARCHAR'},
    delim='\t', -- Set explicit tab delimiter
    strict_mode=FALSE) -- Disable strict mode to handle multi-column content
LIMIT 5;
` |



If we run, we can check if the RegExp works, and can confirm with the result looking like this:



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
` | `ââââââââââââââââââââââââââââ¬âââââââââââ¬ââââââââââââ¬ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
â        timestamp         â is_error â client_ip â                              message                              â
â         varchar          â boolean  â  varchar  â                              varchar                              â
ââââââââââââââââââââââââââââ¼âââââââââââ¼ââââââââââââ¼ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ¤
â Thu Jun 09 06:07:04 2005 â true     â           â  [notice] LDAP: Built with OpenLDAP LDAP SDK                      â
â Thu Jun 09 06:07:04 2005 â true     â           â  [notice] LDAP: SSL support unavailable                           â
â Thu Jun 09 06:07:04 2005 â true     â           â  [notice] suEXEC mechanism enabled (wrapper: /usr/sbin/suexec)    â
â Thu Jun 09 06:07:05 2005 â true     â           â  [notice] Digest: generating secret for digest authentication ... â
â Thu Jun 09 06:07:05 2005 â true     â           â  [notice] Digest: done                                            â
ââââââââââââââââââââââââââââ´âââââââââââ´ââââââââââââ´ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
` |



Let’s now **count the errors by client IP** (when available) to get some insights. To do that, we create a table based on the above query to reuse and simplify the following query:



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
` | `CREATE OR REPLACE TABLE apache_errors AS
SELECT 
    regexp_extract(line, '\[(.*?)\]', 1) AS timestamp,
    regexp_extract(line, '\[error\]', 0) IS NOT NULL AS is_error,
    regexp_extract(line, '\[client (.*?)\]', 1) AS client_ip,
    regexp_extract(line, '\](.*)', 1) AS message
FROM read_csv('https://zenodo.org/records/8196385/files/Apache.tar.gz?download=1', 
    auto_detect=FALSE, 
    header=FALSE, 
    columns={'line':'VARCHAR'},
    delim='\t', -- Set explicit tab delimiter
    strict_mode=FALSE); -- Disable strict mode to handle multi-column content
` |



Then we can query the IP with the most errors:



| `1
2
3
4
5
6
7
8
` | `SELECT 
    client_ip, 
    COUNT(*) AS error_count 
FROM apache_errors 
WHERE is_error AND client_ip IS NOT NULL
GROUP BY client_ip 
ORDER BY error_count DESC 
LIMIT 10;
` |



The result in a couple of seconds:



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
` | `âââââââââââââââââââ¬ââââââââââââââ
â    client_ip    â error_count â
â     varchar     â    int64    â
âââââââââââââââââââ¼ââââââââââââââ¤
â                 â       25367 â
â 218.144.240.75  â        1002 â
â 210.245.233.251 â         624 â
â 211.99.203.228  â         440 â
â 80.55.121.106   â         322 â
â 61.152.90.96    â         315 â
â 212.45.53.176   â         299 â
â 82.177.96.6     â         289 â
â 64.6.73.199     â         276 â
â 81.114.87.11    â         274 â
âââââââââââââââââââ´ââââââââââââââ¤
â 10 rows             2 columns â
âââââââââââââââââââââââââââââââââ
` |



#### Handling Big Data Logs: HDFS Example


Another example is the [HDFS Logs](https://zenodo.org/records/8196385/files/HDFS_v1.zip?download=1) that are available on this same [GitHub repo](https://github.com/logpai/loghub). Let’s look at how DuckDB can handle HDFS logs, which are common in big data environments.


This dataset is 1.47GB in size and has 11,175,629 lines, but we only look at the one HDFS.log that has more than 11 million rows. If you want to follow along, download the file and unzip it. I unzipped it on `~/data/HDFS_v1`.


Let’s now create a table again to simplify our querying:



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
` | `CREATE OR REPLACE TABLE hdfs_logs AS
SELECT 
    SUBSTR(line, 1, 6) AS date,
    SUBSTR(line, 8, 6) AS time,
    regexp_extract(line, 'INFO (.*?): ', 1) AS component,
    regexp_extract(line, 'INFO .*?: (.*)', 1) AS message,
    CASE 
        WHEN line LIKE '%blk_%' THEN regexp_extract(line, 'blk_([-0-9]+)', 1)
        ELSE NULL 
    END AS block_id
FROM read_csv('~/data/HDFS_v1/HDFS.log', 
    auto_detect=FALSE, 
    header=FALSE, 
    columns={'line':'VARCHAR'},
    delim='\t', -- Set explicit tab delimiter
    strict_mode=FALSE); -- Disable strict mode
` |



If we check, we see that we have 11.18 million logsâquerying this directly takes about 3 seconds on my MacBook M1.



| `1
2
3
4
5
6
7
8
` | `select count(*) from hdfs_logs;
âââââââââââââââââââ
â  count_star()   â
â      int64      â
âââââââââââââââââââ¤
â    11175629     â
â (11.18 million) â
âââââââââââââââââââ
` |



If we plan to query that data often, we could create a `TABLE` again, as shown above. Another interesting query is to analyze block operations in these HDFS logs with this analytical query over our logs:



| `1
2
3
4
5
6
7
` | `SELECT 
    component,
    COUNT(*) AS operation_count
FROM hdfs_logs 
WHERE block_id IS NOT NULL
GROUP BY component
ORDER BY operation_count DESC;
` |



The result looks something like this - it reveals the distribution of block operations across different HDFS components, with the NameSystem managing the most operations while DataNode components handle various aspects of data transfer and storage:



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
` | `ââââââââââââââââââââââââââââââââ¬ââââââââââââââââââ
â          component           â operation_count â
â           varchar            â      int64      â
ââââââââââââââââââââââââââââââââ¼ââââââââââââââââââ¤
â dfs.FSNamesystem             â         3699270 â
â dfs.DataNode$PacketResponder â         3413350 â
â dfs.DataNode$DataXceiver     â         2162471 â
â dfs.FSDataset                â         1402052 â
â                              â          362793 â
â dfs.DataBlockScanner         â          120036 â
â dfs.DataNode                 â            7002 â
â dfs.DataNode$DataTransfer    â            6937 â
â dfs.DataNode$BlockReceiver   â            1718 â
ââââââââââââââââââââââââââââââââ´ââââââââââââââââââ
` |



Or we identify potential failures with this query:



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
` | `SELECT 
    block_id,
    COUNT(*) AS log_entries,
    STRING_AGG(DISTINCT component, ', ') AS components
FROM hdfs_logs
WHERE block_id IS NOT NULL
GROUP BY block_id
HAVING COUNT(*) > 10
ORDER BY log_entries DESC
LIMIT 5;
` |



The result looks something like this:



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
` | `ââââââââââââââââââââââââ¬ââââââââââââââ¬âââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
â       block_id       â log_entries â                                                           components                                                           â
â       varchar        â    int64    â                                                            varchar                                                             â
ââââââââââââââââââââââââ¼ââââââââââââââ¼âââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ¤
â -4145674605155741075 â         298 â dfs.DataNode$DataXceiver, dfs.FSNamesystem, dfs.DataNode$DataTransfer, , dfs.DataNode, dfs.FSDataset, dfs.DataNode$PacketResâ¦  â
â -2891794341254261063 â         284 â dfs.DataNode, dfs.DataNode$DataTransfer, dfs.DataNode$DataXceiver, dfs.DataNode$PacketResponder, dfs.FSDataset, dfs.FSNamesyâ¦  â
â 2813981518546746323  â         280 â dfs.DataNode$DataTransfer, dfs.FSNamesystem, dfs.DataNode$DataXceiver, dfs.DataNode$PacketResponder, dfs.FSDataset, dfs.Dataâ¦  â
â -2825351351457839825 â         278 â dfs.DataNode$PacketResponder, dfs.FSNamesystem, dfs.DataNode$DataXceiver, dfs.DataNode$DataTransfer, dfs.FSDataset, dfs.Dataâ¦  â
â 9014620365357651780  â         277 â dfs.DataNode$DataTransfer, dfs.FSNamesystem, dfs.DataNode$PacketResponder, dfs.DataNode, dfs.DataNode$DataXceiver, dfs.FSDatâ¦  â
ââââââââââââââââââââââââ´ââââââââââââââ´âââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
` |



You can see, with some simple queries, you can either run the query directly on your files, or if you have many files, it’s recommended to just create a table, or even unnest some JSON structure to improve query performance. More on this later.


### JSON Log Analytics with Bluesky Data: Scale-Up If Needed


As DuckDB is an analytics tool, besides just parsing logs, we can also create analytics dashboards. In this demo, we do two use cases: first, analyzing the logs directly sitting on S3, with no normalization or unnesting beforehand, once with DuckDB and once with MotherDuck.


Then we unnest JSON files and store them as struct or flat tables, and see how this affects the speed. For more complex log analysis, let’s examine JSON-formatted logs from Bluesky (real-world data), and see some benchmarks when it would make sense to use MotherDuck.

Data Sets
These data sets are from
[JSONBench](https://github.com/ClickHouse/JSONBench)
, a benchmark for data analytics on JSON with Bluesky JSON dataset provided in different sizes.

We can query the data like this quite easily:



| `1
2
3
4
5
6
7
8
9
` | `SUMMARIZE
SELECT 
    did,
    time_us,
    kind,
    commit->>'operation' AS operation,
    commit->>'collection' AS collection,
    commit->'record' AS record
  FROM read_json('https://clickhouse-public-datasets.s3.amazonaws.com/bluesky/file_0001.json.gz');
` |



The result comes back in 5-10 seconds for one single file:



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
` | `âââââââââââââââ¬ââââââââââââââ¬âââââââââââââââââââââââ¬...â¬âââââââââââââââââââ¬ââââââââââ¬ââââââââââââââââââ
â column_name â column_type â         min          â...â       q75        â  count  â null_percentage â
â   varchar   â   varchar   â       varchar        â...â     varchar      â  int64  â  decimal(9,2)   â
âââââââââââââââ¼ââââââââââââââ¼âââââââââââââââââââââââ¼...â¼âââââââââââââââââââ¼ââââââââââ¼ââââââââââââââââââ¤
â did         â VARCHAR     â did:plc:222i7vqbnnâ¦  â...â NULL             â 1000000 â            0.00 â
â time_us     â BIGINT      â 1732206349000167     â...â 1732206949533320 â 1000000 â            0.00 â
â kind        â VARCHAR     â commit               â...â NULL             â 1000000 â            0.00 â
â commit_json â JSON        â {"rev":"22222267axâ¦  â...â NULL             â 1000000 â            0.53 â
â operation   â VARCHAR     â create               â...â NULL             â 1000000 â            0.53 â
â collection  â VARCHAR     â app.bsky.actor.proâ¦  â...â NULL             â 1000000 â            0.53 â
â record      â JSON        â null                 â...â NULL             â 1000000 â            0.53 â
âââââââââââââââ´ââââââââââââââ´âââââââââââââââââââââââ´...â´âââââââââââââââââââ´ââââââââââ´ââââââââââââââââââ
` |



So we can imagine that loading all of the 100 million rows (100 files) or even the full dataset of 1000 million rows would need some different mechanism. But for loading the 100 million rows and 12 GB worth of data,  it can’t run on my Macbook M1 Max anymore.


I tried downloading the 100 million locally and running the query for all or some of the files. But it didn’t finish in a useful time. You can see, that DuckDB uses most of your resources, specifically the CPU (shown in `btop`):


![/blog/log-parsing-duckdb/btop.webp](https://www.ssp.sh/blog/log-parsing-duckdb/btop.webp)

*Btopactivity monitoring*


And in MacOS activity monitor with full CPU usage too:


[

](https://www.ssp.sh/blog/log-parsing-duckdb/macos-activiy.webp)MacOS Activity Monitoring


Here is the syntax to load partially (a couple of files) or load them all:



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
` | `...
  FROM read_json(
  ['s3://clickhouse-public-datasets/bluesky/file_001*.json.gz'
  ,'s3://clickhouse-public-datasets/bluesky/file_002*.json.gz'
  , 's3://clickhouse-public-datasets/bluesky/file_003*.json.gz'
  ], ignore_errors=true);


--OR
...
FROM read_json('s3://clickhouse-public-datasets/bluesky/file_*.json.gz', ignore_errors=true);
` |



#### Scaling Beyond Local Resources with MotherDuck


For this job, I used [MotherDuck](https://app.motherduck.com/). It scales nicely without requiring syntax changes or purchasing a new laptop ð. Plus, I can [share the data set](https://motherduck.com/docs/key-tasks/sharing-data/sharing-overview/) or the [collaborative notebook](https://motherduck.com/docs/getting-started/motherduck-quick-tour/). We can use MotherDuck to parse logs at scale.


Let’s check if the data is queryable directly via S3:



| `1
2
3
4
5
6
7
8
` | `select count(*) from read_json('https://clickhouse-public-datasets.s3.amazonaws.com/bluesky/file_0001.json.gz');
ââââââââââââââââââ
â  count_star()  â
â     int64      â
ââââââââââââââââââ¤
â    1000000     â
â (1.00 million) â
ââââââââââââââââââ
` |



##### Performance Optimization: Pre-Materializing JSON Data


This works, but is still quite slow (`29.7s`) as we need to download the larger Bluesky data over the network. And if we want to do some analytical queries and GROUP BY on top of it, we need to have a different strategy. That’s where materialization into a simple table comes into play. And because we work with JSON data, if we flatten and unnest the JSON, we can do even faster analytics queries.


This is good practice and will always speed up drastically on DuckDB locally and on MotherDuck. For example, we can do this:



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
` | `CREATE OR REPLACE TABLE bluesky_events
  AS
SELECT 
    did,
    time_us,
    kind,
    
    -- Extract fields using json_extract functions
    json_extract_string(commit, '$.rev') AS rev,
    json_extract_string(commit, '$.operation') AS operation,
    json_extract_string(commit, '$.collection') AS collection,
    json_extract_string(commit, '$.rkey') AS rkey,
    json_extract_string(commit, '$.cid') AS cid,
    
    -- Extract record fields
    json_extract_string(commit, '$.record.$type') AS record_type,
    json_extract_string(commit, '$.record.createdAt') AS created_at,
    json_extract_string(commit, '$.record.text') AS text,
    
    -- Extract array fields
    json_extract(commit, '$.record.langs') AS langs,
    
    -- Extract nested reply fields
    json_extract_string(commit, '$.record.reply.parent.cid') AS reply_parent_cid,
    json_extract_string(commit, '$.record.reply.parent.uri') AS reply_parent_uri,
    json_extract_string(commit, '$.record.reply.root.cid') AS reply_root_cid,
    json_extract_string(commit, '$.record.reply.root.uri') AS reply_root_uri

  FROM read_json(
  ['s3://clickhouse-public-datasets/bluesky/file_001*.json.gz'
  ,'s3://clickhouse-public-datasets/bluesky/file_002*.json.gz'
  , 's3://clickhouse-public-datasets/bluesky/file_003*.json.gz'
  ], ignore_errors=true);
 ;
` |



This query took `8m 5s` to create on MotherDuck as it had to load the full data from S3 to MotherDuck. Once we have it in, it’s fast. This is always a tradeoff - when you just want a live view without materializing, you can also filter more narrowly and run it directly without the table created first.

How to use Wildcards
Instead of loading all data with
, I used the above list notation to read the
.

##### Practical Analytics: Real-world Query Example


Let’s now analyze analytics queries like event types with:



| `1
2
3
4
5
6
7
` | `SELECT 
    record_type,
    operation,
    COUNT(*) AS event_count
FROM bluesky_events
GROUP BY record_type, operation
ORDER BY event_count DESC;
` |



The result looks something like this:



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
` | `ââââââââââââââââââââââââââââââ¬ââââââââââââ¬ââââââââââââââ
â        record_type         â operation â event_count â
â          varchar           â  varchar  â    int64    â
ââââââââââââââââââââââââââââââ¼ââââââââââââ¼ââââââââââââââ¤
â app.bsky.feed.like         â create    â    13532563 â
â app.bsky.graph.follow      â create    â    10414588 â
â app.bsky.feed.post         â create    â     2450948 â
â app.bsky.feed.repost       â create    â     1645272 â
.....
â app.bsky.feed.post         â update    â         248 â
â app.bsky.feed.postgate     â update    â         105 â
â app.top8.theme             â update    â          29 â
â app.bsky.labeler.service   â update    â           9 â
â app.bsky.labeler.service   â create    â           3 â
ââââââââââââââââââââââââââââââ´ââââââââââââ´ââââââââââââââ¤
â 25 rows                                    3 columns â
ââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
` |



And time-based analysis (events per hour) queries, or basically any query:



| `1
2
3
4
5
6
7
` | `SELECT
    DATE_TRUNC('hour', to_timestamp(time_us/1000)) AS hour,  -- Using to_timestamp instead
    collection,
    COUNT(*) AS event_count
FROM bluesky_events
GROUP BY hour, collection
ORDER BY hour, event_count DESC;
` |



The result:



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
` | `ââââââââââââââââââââââââââââ¬âââââââââââââââââââââââââââââ¬ââââââââââââââ
â           hour           â         collection         â event_count â
â timestamp with time zone â          varchar           â    int64    â
ââââââââââââââââââââââââââââ¼âââââââââââââââââââââââââââââ¼ââââââââââââââ¤
â 56861-06-07 16:00:00+02  â app.bsky.feed.like         â        1366 â
â 56861-06-07 16:00:00+02  â app.bsky.graph.follow      â        1240 â
â 56861-06-07 16:00:00+02  â app.bsky.feed.post         â         276 â
â 56861-06-07 16:00:00+02  â app.bsky.feed.repost       â         174 â
â 56861-06-07 16:00:00+02  â app.bsky.graph.listitem    â          59 â
â 56861-06-07 16:00:00+02  â app.bsky.graph.block       â          53 â
â 56861-06-07 16:00:00+02  â app.bsky.actor.profile     â          29 â
â            Â·             â          Â·                 â           Â· â
â            Â·             â          Â·                 â           Â· â
â            Â·             â          Â·                 â           Â· â
â 56861-06-17 02:00:00+02  â app.bsky.graph.follow      â         486 â
â 56861-06-17 02:00:00+02  â app.bsky.feed.like         â         486 â
ââââââââââââââââââââââââââââ´âââââââââââââââââââââââââââââ´ââââââââââââââ¤
â 2724 rows (40 shown)                                      3 columns â
âââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
` |



Or find the **most active users**:



| `1
2
3
4
5
6
7
8
` | `SELECT 
    did AS user_id,
    COUNT(*) AS activity_count,
    COUNT(DISTINCT collection) AS different_activity_types
FROM bluesky_events
GROUP BY did
ORDER BY activity_count DESC
LIMIT 10;
` |



Here’s the user identified:



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
` | `ââââââââââââââââââââââââââââââââââââ¬âââââââââââââââââ¬âââââââââââââââââââââââââââ
â             user_id              â activity_count â different_activity_types â
â             varchar              â     int64      â          int64           â
ââââââââââââââââââââââââââââââââââââ¼âââââââââââââââââ¼âââââââââââââââââââââââââââ¤
â did:plc:kxrsbasaua66cvheddlg5cq2 â           5515 â                        3 â
â did:plc:vrjvfu27gudvy2wpasotmyf7 â           5127 â                        4 â
â did:plc:kaqlgcnwgnzlztbcuywzpaih â           5073 â                        3 â
â did:plc:zhxv5pxpmojhnvaqy4mwailv â           5018 â                        5 â
â did:plc:znqs6r4ode6z4clxboqy5ook â           4940 â                        6 â
â did:plc:tqyrs5zpxrp27ksol4tkkxht â           4025 â                        2 â
â did:plc:6ip7eipm6r6dhsevpr2vc5tm â           3720 â                        5 â
â did:plc:ijooriel775q4lsseuro6agf â           3379 â                        7 â
â did:plc:r5qc6mzxyetxgnvgvrvkobe2 â           3267 â                        2 â
â did:plc:42benzd2u5sgxxdanweszno3 â           3188 â                        3 â
ââââââââââââââââââââââââââââââââââââ´âââââââââââââââââ´âââââââââââââââââââââââââââ¤
â 10 rows                                                            3 columns â
ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
` |



That’s it; these are some tricks and examples of how to analyze logs, from simple logs to large JSON data sets. Please go ahead and try it yourself with your own data logs, or follow along with the GitHub repos shared in this article.

Other Handy Trick
Unnest to speed up, see example query snippet:
[Unnest JSON Array into Rows (pseudo-json_each)](https://duckdbsnippets.com/snippets/13/unnest-json-array-into-rows-pseudojsoneach)
. Find many more on
[SQL, Python & More for DuckDB | DuckDB Snippets](https://duckdbsnippets.com/)
.

## What Did We Learn?


In wrapping up, we saw that logs are not as simple as we think and that data engineering platforms are fundamentally built on logs. We can use DuckDB for parsing logs and MotherDuck for parsing logs at scale with collaboration and sharing features.


Log files provide crucial visibility into every aspect of our data stack. From application errors to performance metrics, from transaction records to security events, these logs form the digital breadcrumbs that allow us to trace, troubleshoot, and optimize our data platforms.


The power of DuckDB as a log parser lies in its flexibility and performance. We’ve seen how it effortlessly handles different log formatsâfrom simple text files to complex JSON structuresâwithout requiring data to be pre-loaded into a database. The ability to query logs directly where they sit, whether on S3, in Snowflake or on local storage, makes DuckDB an incredibly powerful tool for ad hoc analysis.


For larger-scale log analysis, MotherDuck extends these capabilities, allowing teams to collaboratively analyze massive log datasets without being constrained by local hardware limitations. The ability to seamlessly scale from local analysis to cloud-based processing with the same familiar syntax makes this combination particularly powerful for data teams of all sizes.


We’ve learned that effective log analysis is not only about which tools to use, but about understanding the structure and purpose of different log types, knowing when to materialize or unnest data for performance, and being able to craft queries that extract meaningful insights from what might otherwise be overwhelming volumes of information.


Knowing how to analyze logs straightforwardly and efficiently is a competitive advantage in today’s data-driven world. It allows data engineers to spend less time troubleshooting and more time building reliable data platforms that drive business value.


---


```
Full article published at MotherDuck.com - written as part of my services
```

[Discuss on Bluesky](https://bsky.app/search?q=domain%3A%20https://www.ssp.sh/blog/log-parsing-duckdb/)
|
[Logs](https://www.ssp.sh/tags/logs/)
[Motherduck](https://www.ssp.sh/tags/motherduck/)
[Duckdb](https://www.ssp.sh/tags/duckdb/)
[Log Analysis](https://www.ssp.sh/tags/log-analysis/)
[JSON Parsing](https://www.ssp.sh/tags/json-parsing/)
[SQL](https://www.ssp.sh/tags/sql/)
[Data Observability](https://www.ssp.sh/tags/data-observability/)
[Data Pipelines](https://www.ssp.sh/tags/data-pipelines/)
[Services](https://www.ssp.sh/tags/services/)
