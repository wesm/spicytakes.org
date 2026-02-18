---
title: "Data Modeling Guide for Real-Time Analytics with ClickHouse"
date: 2025-09-05
url: https://www.ssp.sh/blog/practical-data-modeling-clickhouse/
slug: practical-data-modeling-clickhouse
word_count: 4978
---

![Data Modeling Guide for Real-Time Analytics with ClickHouse](https://www.ssp.sh/blog/practical-data-modeling-clickhouse/featured-image.png)

Contents
ð¶
Featured on Hacker News.
[Read the comments](https://news.ycombinator.com/item?id=45137927)
This article was written as part of
[my services](https://www.ssp.sh/services)

Querying billions of weather records and getting results in under 200 milliseconds isn’t theory; it’s what real-time analytics solutions provide. Processing streaming IoT data from thousands of sensors while delivering real-time dashboards with no lag is what certain business domains need. That’s what you’ll learn at the end of this guide through building a ClickHouse-modeled analytics use case.


You’ll learn how to land data in ClickHouse that is optimized for real-time data applications, going from basic ingestion to advanced techniques like statistical sampling, pre-aggregation strategies, and multi-level optimization. I’ve included battle-tested practices from Rill’s years of implementing real-time analytics for customers processing everything from financial transactions and programmatic advertising to IoT telemetry.


This article is for data engineers and practitioners who want to build analytics that deliver sub-second query responses, and who want to unlock ClickHouse’s full potential for real-time analytics demands. By the end, you’ll have a playbook for ClickHouse data modeling plus a working example that ingests NOAA weather data from S3 and visualizes it with a single configuration file.

Why ClickHouse

If you haven’t heard of ClickHouse or are wondering why it’s becoming the go-to choice for real-time analytics, here’s what sets it apart from traditional data warehouses.


ClickHouse achieves blazingly fast analytical performance through column-oriented storage that reads only relevant data, advanced compression (LZ4/ZSTD), and vectorized query execution that maximizes CPU capabilities. Its sparse primary indexing with data skipping eliminates irrelevant data blocks, while the C++ implementation avoids JVM overhead for bare-metal performance.


These innovations enable sub-second query responses on billions of rows, performance that would take minutes or hours in traditional data warehouses. Storage efficiency has a direct impact on both cost and speed at scale, making ClickHouse the ideal foundation for the real-time analytics modeling strategies covered in this article.


## Data Flow for Real-time Analytics


Before we see a concrete example of modeling data with ClickHouse, specifically for real-time and online analytical processing (OLAP) cubes, it’s important to **understand the flow of data**, its trade-offs, and payoffs. Where Does Data Come From, and Where Does It Go?


### Data Flow is Knowing the Requirements


Data flows from sources to analytics. In the simplest terms, we have sources of data, a transformation with aggregations, and the visualization. Most often, the data should travel from source to visualization as quickly as possible and respond fast to queries.


Most data flow modeling is handled in the transformation phase. Connecting to a source, whether it is an S3 or R2 bucket, a relational database like Postgres or others, or visualization on an analytical tool. We need to **aggregate and combine the data** to extract business insights out of masses of information to answer the questions our business needs to answer.


Obviously data modeling can get much more involved—looking at modeling open data stack, or looking at [The State of Data Engineering](https://dedp.online/part-1/1-introduction/history-and-state-of-data-engineering.html) and its [challenges](https://dedp.online/part-1/1-introduction/challenges-in-data-engineering.html). However, modeling data has nothing to do with choosing tools in the first place. If we have the best tools but a bad data flow, it’s not worth much.


The below illustration shows where the modeling part actually happens:


[

](https://www.ssp.sh/blog/practical-data-modeling-clickhouse/data-modeling.png)From the book [Data Modeling with Snowflake](https://www.amazon.com/dp/1837634459) by Serge Gershkovich | Like seeing a forest for the trees, ubiquitous modeling allows us to see the business for the data.


Most often, modeling is more about offline, off-computer, and real conversations with the business people involved than figuring it out ourselves. We have to answer the questions “What’s needed on a dashboard?” “Which numbers are even possible with the data at hand?” and “How can we get them, join and aggregate them with other data from the company to get the best possible insights?”

Shifting Left: Another form of modeling

[Shifting Left](https://www.ssp.sh/blog/shifting-left/) is another important concept related to data modeling. It means that the better we model and structure data at the source (left side of the data pipeline), the more efficient and accurate our analytics become downstream (right side). When raw data is properly typed, deduplicated, and structured early in the pipeline, we avoid expensive transformations later and reduce the risk of data quality issues propagating through our entire analytics stack. This is especially critical for real-time systems where you can’t afford lengthy batch cleanup processes.


### Real-Time Analytics: A Tradeoff


Real-time analytics specifics are always a tradeoff between **data freshness and accuracy**.


The moment the data is loaded, it is outdated. But to avoid pulling the latest all the time, we need to make sure the data is consistent across tables, meaning related data is pulled too when we refresh, so that it’s cohesive and accurate.


In the end, you need a set of metrics that are business critical for your organization. Some businesses like IoT and e-commerce don’t need all data, but specific data such as IP or location to identify quickly where users come from. Use cases like this especially need and benefit from low-latency query responses. Data needs to load near real-time and needs to deliver fast, flexible access to core analytics.


### The Payoff of Great Data Flow


The payoffs of modeling are higher performance, insights on consistent data, and lower cost as we do not need to query production with a reduced aggregated data set and without the need for heavy overnight ETL jobs. We need less storage for aggregated data and get even faster query responses.


Imagine a fast river that flows constantly with great volume. This is what good data will look like when new data is coming in steady and accurate.


Let’s see that in action with ClickHouse real-time modeling.


## ClickHouse Modeling Strategies: From Theory to Practice


Now that we understand the data flow requirements for real-time analytics such as fast ingestion, efficient transformation, and sub-second query responses, let’s explore how ClickHouse specifically addresses these challenges through its modeling approaches.


Remember our data flow: `Sources â Transformation & Aggregation â ClickHouse â Visualization`. The key insight is that ClickHouse doesn’t only serve as storage but can handle much of the transformation and aggregation work directly, eliminating traditional ETL bottlenecks.


ClickHouse offers several strategies to optimize this flow, each addressing different aspects of the freshness-accuracy tradeoff we discussed:


**For Minimizing Query-Time Complexity:**

- [**Denormalizing data**](https://clickhouse.com/docs/data-modeling/denormalization): Move joins from query time to insert time by flattening related tables into a single structure (One Big Table, approach). This trades some storage efficiency for dramatic query performance gains. Especially recommended for tables that change infrequently and not for high-cardinality or many-to-many relationships.
- [**Dictionaries**](https://clickhouse.com/docs/dictionary): Handle dimension lookups through in-memory key-value structures, perfect for enriching streaming data with relatively static reference information.


**For Real-Time Aggregation:**

- [**Incremental Materialized Views**](https://clickhouse.com/docs/materialized-view/incremental-materialized-view): Shift computational cost from query time to insert time, computing aggregates as data arrives rather than when users request it. Most suitable for real-time aggregations and transformations, especially for single-table aggregations or simple enrichments with static dimension tables.
- [**Refreshable Materialized Views**](https://clickhouse.com/docs/materialized-view/refreshable-materialized-view): Handle complex multi-table joins and transformations on a scheduled basis, suitable when real-time freshness isn’t critical. They are also useful for batch denormalization and building view dependencies (like DAGs) and can be scheduled with [dbt](https://clickhouse.com/docs/integrations/dbt), Airflow, and other data orchestrators. Refreshable MVs are similar to materialized views in traditional OLTP databases.


The fundamental principle underlying all these approaches is **minimizing joins at query time**. In traditional OLAP cubes, much of this complexity is handled by pre-built logical modeling layers. ClickHouse takes a different approach where you explicitly choose where in the pipeline to handle complexity based on your specific performance and freshness requirements.


### Modeling Data with ClickHouse


An interesting new dimension is modeling multi-dimensional cubes. What’s the difference, you might ask? Besides the difference between traditional OLAP cubes and modern OLAP cubes, which first stores measures and joins within the cube and pre-processes, whereas [modern real-time databases](https://www.ssp.sh/blog/scaling-beyond-postgres/) systems like ClickHouse, Pinot, Druid, and StarRocks do not. This is at first glance a disadvantage, but on the other hand an advantage, that we can change our queries at query time without re-processing needed.


What else do we need to know about *OLAP data modeling*? We need to understand that OLAP cubes store data in a **column-oriented (or columnar)** way. This is important to the ClickHouse architecture. Unlike traditional row-oriented databases that store all values in a row together, ClickHouse stores all values that belong to a single column together. This also influences how we model our data and enables fast analytical queries based on a few columns out of potentially hundreds. ClickHouse only needs to read the data files for those specific columns, drastically reducing disk I/O compared to reading entire rows.


Usually when we model a multi-dimensional cube, we deal with facts and dimensions. The queries are optimized for **sub-second** response times and the users might be our clients or business users; there might only be one visualization layer in between such as a BI tool or Excel. This means it’s mission-critical.


In ClickHouse and in general with cubes, we are working with dimensions, measures, and operators that operate on time aggregations and dimensions. You want rollups and drill-downs along multiple axes, with subtotals and potentially pivots.


SQL can sometimes be hard work to get right as we constantly pivot along different dimensions, and there are joins involved, different granularity, and all of a sudden, you accidentally duplicate your counting by adding a wrong dimension.


So how do we effectively model ClickHouse to get real-time data from start to end with no more than needed effort?


In the following example, we’ll see several of these strategies in action: denormalization through data transformation during ingestion, partitioning for query optimization, and incremental processing for real-time updates.

Traditional Cubes

There’s no logical modeling layer like in [SQL Server Analysis Services (SSAS)](https://learn.microsoft.com/en-us/analysis-services/ssas-overview?view=sql-analysis-services-2025), meaning we need to model our data outside of ClickHouse to create pre-defined optimized tables to query with the methods explained above such as materialized views, small lookup tables, or denormalized tables.


## Demo: Using S3 -> ClickHouse -> Rill


But we can design and model the data flow easily to source data from an S3/R2 bucket, load from Kafka, or other streaming data sources.


Let’s have a look at a practical example where we ingest data from S3, using ClickHouse as the engine to do transformation and aggregation, ingesting the data [incrementally](https://docs.rilldata.com/build/advanced-models/incremental-models) with the built-in refresh by ClickHouse, and visualizing with Rill.


![/blog/practical-data-modeling-clickhouse/rill-dashboard.webp](https://www.ssp.sh/blog/practical-data-modeling-clickhouse/rill-dashboard.webp)

*Dashboard overview in Rill*


Watch the short video for the interactive version - below we are going to explain each config step by step.

Demo used in this chapter available on GitHub

Find everything shown in this demo at [clickhouse-modeling-rill-example](https://github.com/sspaeti/clickhouse-modeling-rill-example).


### Ingest and Transformation


This example represents an end-to-end data project, loading [NOAA weather data](https://commoncrawl.org/blog/index-to-warc-files-and-urls-in-columnar-format) that gets updated from S3 via ClickHouse and visualized in Rill. All within a single YAML shown here (expand to see the full code):



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
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
` | `type: model
materialize: true
incremental: true

# Do an incremental refresh every hour.
refresh:
  cron: "0 * * * *"

# Use SQL partitions to define year-based partitions for NOAA data
# This demonstrates ClickHouse's S3 capabilities with yearly partitioning
partitions:
  sql: SELECT generate_series AS year FROM generate_series(2024, 2025)
  #grabbing all files
  #glob: s3://noaa-ghcn-pds/csv.gz/*.csv.gz 

# Load and transform NOAA weather data with proper column names and types
# This showcases ClickHouse's data transformation capabilities
sql: >
  SELECT
      '{{ .partition.year }}' AS __partition,
      now() AS __load_time,
      -- Transform raw CSV columns to proper NOAA weather schema
      COALESCE(c1, 'UNKNOWN') AS station_id,
      COALESCE(toDate(toString(c2)), toDate('1900-01-01')) AS measurement_date,
      COALESCE(c3, 'UNKNOWN') AS measurement_type, -- TMIN, TMAX, PRCP, SNOW, etc.
      toFloat32(c4) / 10.0 AS measurement_value, -- Convert from tenths
      c5 AS measurement_flag,
      c6 AS quality_flag,
      c7 AS source_flag,
      c8 AS observation_time,
      -- Add derived fields for analytics
      toYear(toDate(toString(c2))) AS measurement_year,
      toMonth(toDate(toString(c2))) AS measurement_month,
      toDayOfYear(toDate(toString(c2))) AS measurement_day_of_year,
      -- Temperature conversions for common analysis
      CASE 
        WHEN c3 = 'TMIN' THEN toFloat32(c4) / 10.0
        ELSE NULL 
      END AS temp_min_celsius,
      CASE 
        WHEN c3 = 'TMAX' THEN toFloat32(c4) / 10.0  
        ELSE NULL
      END AS temp_max_celsius,
      CASE 
        WHEN c3 = 'PRCP' THEN toFloat32(c4) / 10.0
        ELSE NULL
      END AS precipitation_mm
  FROM s3(
      's3://noaa-ghcn-pds/csv.gz/by_year/{{ .partition.year }}.csv.gz',
      'CSV'
  )

# Insert the results into a partitioned table that uses the MergeTree engine.
# Optimized for time-series weather data analytics
output:
  incremental_strategy: partition_overwrite
  partition_by: __partition
  engine: MergeTree
  # Optimize ordering for typical weather queries: by date, station, measurement type
  # Using COALESCE ensures non-nullable columns in sorting key
  order_by: (measurement_date, station_id, measurement_type)
  # Primary key for fast weather station and date lookups
  primary_key: (measurement_date, station_id)
  # TTL for data retention (optional - uncomment if needed)
  # ttl: measurement_date + INTERVAL 10 YEAR
` |



*Source code and full project can be found on GitHub at [clickhouse-modeling-rill-example](https://github.com/sspaeti/clickhouse-modeling-rill-example)*


So what happens here?


This YAML configuration demonstrates how ClickHouse can serve as both your data transformation engine and storage layer, eliminating the need for traditional ETL tools.


**Data ingestion and transformation in one step:** The `sql` section directly reads compressed CSV files from S3 using ClickHouse’s native `s3()` function. Rather than requiring a separate ETL process to extract, clean, and load the data, ClickHouse performs all transformations during the ingestion process itself. The query handles data type conversions (like converting temperature readings from tenths to actual values with `toFloat32(c4) / 10.0`), creates derived fields for analytics (such as extracting year, month, and day components), and applies data quality measures using `COALESCE` to handle null values.


**MergeTree is your built-in ETL engine:** The `engine: MergeTree` specification transforms ClickHouse into what you can think of as “local ETL without the need for an ETL tool.” MergeTree engines are specifically designed for high data ingest rates and massive data volumes. When new data arrives, ClickHouse creates table parts that are automatically merged by background processes, maintaining optimal query performance without manual intervention. This means your data pipeline becomes very lightweight and self-managing – new weather data gets ingested, transformed, and optimized automatically based on defined cron triggers.


**Multi-level optimization strategy:** This example demonstrates ClickHouse’s ability to optimize at multiple levels simultaneously. At the **query level**, the `order_by: (measurement_date, station_id, measurement_type)` ensures that data is physically sorted for optimal access patterns typical in weather analytics. This is very important to your end query and how your response will perform. At the **storage level**, the `partition_by: __partition` creates year-based partitions that enable ClickHouse to skip entire data segments when querying specific time ranges. The **incremental strategy** with `partition_overwrite` means only changed partitions are reprocessed, not the entire dataset.


**Real-time processing without complexity:** The `refresh: cron: "0 * * * *"` configuration creates an automated pipeline that updates hourly without requiring external orchestration tools like Airflow or Dagster. ClickHouse handles the scheduling, dependency management, and incremental processing internally.


Further optimizations are [*TTL* (time-to-live)](https://clickhouse.com/docs/use-cases/observability/clickstack/ttl), which deletes data after a defined retention period such as `hour + INTERVAL 90 DAY DELETE`, or we can apply further [table features](https://clickhouse.com/docs/operations/settings/merge-tree-settings) such as:



| `1
2
3
4
5
6
7
8
` | `# Additional optimizations for data lifecycle and projection management
table_settings: >
    # Handle projections during deduplication: 'rebuild' recreates projections after merge
    deduplicate_merge_projection_mode = 'rebuild',
    # Speed up TTL-based data compression merges (0 = immediate, default: 4 hours)
    merge_with_recompression_ttl_timeout = 0,
    # Speed up TTL-based data deletion merges (0 = immediate, default: 4 hours)  
    merge_with_ttl_timeout = 0
` |



These settings optimize both deduplication behavior with projections and accelerate automatic data lifecycle management through more frequent TTL merges, ensuring expired data is cleaned up promptly rather than waiting for the default 4-hour intervals.

Native Deduplication Features

ClickHouse provides built-in **[insert deduplication](https://clickhouse.com/docs/guides/developer/deduplicating-inserts-on-retries#query-level-insert-deduplication)** for retry scenarios by creating unique `block_id` hashes for each inserted block. Duplicate blocks are skipped automatically.


**Key settings** are `insert_deduplicate=1` enables block-level deduplication (default for replicated tables) and `insert_deduplication_token` provides custom deduplication keys for explicit control. This is block-level deduplication at insert time, unlike ReplacingMergeTree’s row-level deduplication during merges. For more details, see the [deduplication token documentation](https://clickhouse.com/docs/operations/settings/settings#insert_deduplication_token).


### Visualizing in Rill


The above YAML is the source `noaa-weather.yaml` and when you start rill after cloning the example above with:



| `1
` | `rill start git@github.com:sspaeti/clickhouse-modeling-rill-example.git
` |



You can click on the source, and the data will be automatically loaded from the S3 source, and the above-defined transformations and conversions will be made:


![/blog/practical-data-modeling-clickhouse/rill-source.webp](https://www.ssp.sh/blog/practical-data-modeling-clickhouse/rill-source.webp)

*Source-View in Rill ingesting 58 million rows*


### What Did We Learn so Far?


To recap this example, ClickHouse offers a fundamentally different approach compared to other [real-time databases](https://www.ssp.sh/blog/scaling-beyond-postgres/) like Druid, where most heavy lifting must be done **ahead of ingestion** using Spark or other compute engines. With ClickHouse, the engine itself handles complex aggregations and optimizations at ingestion time, during query execution, and even post-ingestion.

Rill does all the orchestration

Interestingly, Rill automatically spawns up ClickHouse and orchestrates the incremental loads and ingests data. If you will, Rill is doing orchestration work.



| `1
2
3
` | `>  â¯ ps aux | grep clickhouse
sspaeti  1406478  0.1  0.4 477508 136528 pts/28  Sl+  22:42   0:00 clickhouse-watchdog                                 server --config-file /tmp/rill-modeling/clickhouse-modeling-rill-example/tmp/default/clickhouse/default/config.xml
sspaeti  1406566 54.8  3.2 12216304 899476 pts/28 Sl+ 22:42   1:12 /home/sspaeti/.rill/clickhouse/25.2.2.39/clickhouse server --config-file /tmp/rill-modeling/clickhouse-modeling-rill-example/tmp/default/clickhouse/default/config.xml
` |



ClickHouse provides multiple levels of optimization that can be applied independently or combined:


**Query-Level Optimizations:**

1. Simple **GROUP BY** aggregations that process data from milliseconds to hours on the fly.
2. Data **partitioning:** Data is organized into directories based on partition keys for parallel processing.
3. **Filter and partition pushdown:** ClickHouse’s optimizer pushes filters closer to the data source and skips irrelevant partitions, dramatically reducing I/O.


**Storage-Level Pre-Aggregation Optimizations:**

4. **Incremental materialized views** shift computation cost from query time to insert time for faster SELECT queries.

5. **AggregatingMergeTree** stores partial aggregation states directly in the table engine, merging rows with the same primary key into single rows containing combined aggregate states—enabling orders of magnitude data reduction and sub-second query performance.


This flexibility allows you to choose the right optimization strategy based on your specific use case, query patterns, and performance requirements.

Example of running ClickHouse locally with the StackOverflow dataset, 22 million rows

Querying stackoverflow data in ClickHouse locally | [X Post](https://x.com/sspaeti/status/1957804415508746476)

Alternative for more Powerful and managed Ingestion: ClickPipes

**[ClickPipes](https://clickhouse.com/cloud/clickpipes)** is ClickHouse Cloud’s managed integration platform that makes ingesting data from diverse sources as simple as clicking a few buttons, providing a scalable, serverless ingestion experience with high throughput and low latency. Beyond object storage, ClickPipes supports Kafka/Confluent, database CDC from MySQL and Postgres, and streaming platforms like Kinesis and Event Hubs.


The platform includes fully managed operations with built-in error handling, automatic retries, schema evolution, and monitoring through dedicated error tables, plus enterprise features like API/Terraform integration and Prometheus metrics). For object storage specifically, ClickPipes supports `continuous ingestion` with configurable polling where new files must be lexically ordered (e.g., `file1`, `file2`, `file3`) for proper ingestion sequencing.


## Applicable Tips & Tricks


In this chapter we look at practical strategies for data modeling with ClickHouse with practical tips and tricks for real-time analytics.


### Deduplication Strategies


**Why it matters**: Real-time data streams often contain duplicate records due to network retries, system failures, or multiple data sources. Without deduplication, your analytics might show inflated metrics and incorrect insights.


**How to implement**: ClickHouse offers several deduplication approaches:

- **[ReplacingMergeTree](https://clickhouse.com/docs/engines/table-engines/mergetree-family/replacingmergetree)**: Automatically deduplicates rows based on the sorting key during background merges.
- **Refreshable Materialized Views**: Use `GROUP BY` with `argMax()` to keep the latest version of each record.
- **Custom Deduplication Logic**: Implement application-level deduplication before insertion.


**Best Practice**: For high-throughput real-time scenarios, use ReplacingMergeTree with a proper sorting key that includes your natural deduplication fields (e.g., `user_id`, `event_id`, `timestamp`).


### Performance Optimization


ClickHouse is all about performance and speed out of the gate. But here are some tips and practical examples to optimize even more.


#### Partitioning Strategy


**Why it matters**: Proper partitioning enables [query pruning](https://www.postgresql.org/docs/current/ddl-partitioning.html#DDL-PARTITIONING-OVERVIEW) and parallel processing, dramatically reducing query times from minutes to seconds.


**How to implement**:

- Partition by time (daily/monthly) for time-series data.
- Use secondary partitioning for high-cardinality dimensions. This means adding additional partition keys beyond just time to handle columns with many distinct values (`region` in the example below).
- Design partitions to match your most common query patterns.



| `1
2
3
4
` | `-- Advanced: Combine with AggregatingMergeTree for maximum efficiency
PARTITION BY (toYYYYMM(timestamp), region)
ORDER BY (user_id, timestamp)
ENGINE = AggregatingMergeTree()
` |



#### Predicate Pushdown Optimization


**Why it matters**: Moving filters closer to the data source reduces the amount of data processed at each query stage.


**How to implement**:

- Structure your `WHERE` clauses to match your sorting key order.
- Use low-cardinality columns early in filtering.
- Leverage ClickHouse’s automatic index usage for range queries with [sparse index](https://clickhouse.com/docs/primary-indexes).
- **Advanced tip**: Combine with materialized views to push aggregations to insert time, not just filters to data source.


#### Pre-Aggregation with AggregatingMergeTree


**When to use**: High-volume time-series data where the same aggregation queries run frequently.


**Implementation**: Use `-State` functions during INSERT and `-Merge` functions during SELECT to work with pre-computed aggregate states rather than raw data. [More Information](https://clickhouse.com/docs/engines/table-engines/mergetree-family/aggregatingmergetree#select-and-insert)


### Storage Efficiency


Data modeling has a real impact on cost when done correctly. Here are some strategies to reduce storage, therefore save cost, and speed up query responses by an order of magnitude.


#### Data Sketches for Approximation


**Why it matters**: Exact distinct counts and percentiles on billions of rows are very expensive and time-consuming. [Data sketches](https://datasketches.apache.org/) use clever algorithms to deliver 99%+ accuracy for 1% of the cost and storage.


**How to implement**:



| `1
2
3
4
5
6
7
` | `-- Challenge: Count unique users from 1B+ events without storing all IDs - from: https://datasketches.apache.org/docs/Background/TheChallenge.html
SELECT 
    uniqHLL12(user_id) as approx_unique_users,  -- Uses ~1.5KB vs 8GB+
    quantile(0.95)(response_time_ms) as p95_response_time,  -- 95th percentile approximation
    countDistinct(session_id) as approx_unique_sessions  -- Approximate distinct sessions
FROM events 
WHERE date >= '2024-01-01'
` |



**Impact**: The above example has an accuracy of 99%+ and a memory footprint of <2KB with a speedboost of 100x by reducing storage.


#### Rollup to Optimal Time Granularity


**Why it matters**: Storing every millisecond-level event creates significant storage overhead. Most business analytics work at hourly or daily granularity.


**How to implement**:

- Aggregate raw events to hourly summaries using materialized views or SQL aggregations.
- Keep detailed data for recent periods (last 30 days) and aggregated monthly data for historical analysis, for example.
- Use different retention policies per granularity level.


### Sampling Strategies


Sampling is a statistical way to reduce data without compromising on getting the right insights.


#### Statistical Sampling for Large Datasets


**Why it matters**: When dealing with billions of events, sometimes a representative sample provides sufficient accuracy for analytics while dramatically reducing processing time and storage costs.


**How to implement**:



| `1
2
3
4
5
6
7
8
9
` | `-- Random sampling: Take 1% of all events
SELECT * FROM events 
WHERE cityHash64(user_id) % 100 = 0

-- Time-based sampling: Higher resolution for recent data
SELECT * FROM events 
WHERE 
  timestamp >= now() - INTERVAL 7 DAY  -- Keep all recent data
  OR cityHash64(event_id) % 100 = 0    -- Sample older data
` |



**Best Practice**: Use [stratified sampling](https://en.wikipedia.org/wiki/Stratified_sampling) when you need to maintain proportional representation across important business dimensions (customer segments, product categories, geographic regions). Use consistent hash functions to ensure reproducible samples.


**Impact**: Can reduce data volumes by 90-99% while maintaining statistical significance for trend analysis and aggregate metrics.


### Schema Management


#### Table Projections for Query Optimization


[Table projections](https://clickhouse.com/docs/sql-reference/statements/alter/projection) are ClickHouse’s native feature for pre-computed, physically stored copies of your table data with different sort orders or pre-aggregations. Think “same table, multiple indexes on steroids”.


**Why it matters**: Different queries need different sort orders or aggregations. Projections let you maintain multiple optimized access patterns without duplicating tables, and the query optimizer automatically picks the projection with the least data to scan.



| `1
2
3
4
5
6
7
8
9
` | `-- ClickHouse: Create projection optimized for user-based queries
ALTER TABLE events_obt ADD PROJECTION user_timeline
(SELECT user_id, timestamp, event_type ORDER BY user_id, timestamp);

-- ClickHouse: Pre-aggregated projection for analytics
ALTER TABLE events_obt ADD PROJECTION daily_stats  
(SELECT toDate(timestamp) as date, event_type, count() 
 GROUP BY date, event_type ORDER BY date);
 
` |


dbt + ClickHouse Approach

Use dbt to create a denormalized One Big Table (OBT) in ClickHouse, then leverage ClickHouse projections for different query patterns instead of maintaining separate OLAP cubes.


#### Schema Evolution Best Practices


**Why it matters**: Real-time systems need to handle schema changes without breaking existing queries or requiring full data reloads.


**How to implement**:

- Use nullable columns for new fields to maintain backward compatibility.
- Implement “latest state” modeling for slowly changing dimensions.
- Leverage ClickHouse’s automatic schema detection for JSON fields.
- **Snapshot approach**: Daily/weekly full snapshots of dimensional data.


### Time Series Optimization


When working with time series, dates are an important part of how we query and store data.


#### Always Store in UTC


**Why it matters**: Mixed timezones in analytical data lead to incorrect aggregations and confusing results when data spans multiple regions.


**How to implement**:

- Convert all timestamps to UTC at ingestion time.
- Store the original timezone as a separate column if needed for display.
- Use ClickHouse’s timezone functions for display conversion only.



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
` | `-- Convert and store in UTC, keep original timezone for reference
INSERT INTO events 
SELECT 
    toDateTime(local_timestamp, source_timezone) as timestamp_utc, -- Store in UTC (the key storage column)
    -- Display examples in different timezones
    toTimeZone(toDateTime(local_timestamp, source_timezone), 'Europe/London') as london_time,
    toTimeZone(toDateTime(local_timestamp, source_timezone), source_timezone) as original_local_time,
    
    -- other fields
FROM source_table;
` |


Some of the Limitations of ClickHouse

Besides all the strengths, some limitations can’t be neglected. For example, it’s more difficult to do updates and deletes ([Mutations](https://clickhouse.com/docs/sql-reference/statements/alter)). Joins are limited in performance and functionality and there’s no full ACID transactions support. There’s also no notion of foreign keys. This means referential integrity is left to the user to manage at an application level. Read more about this on [ClickHouse Architecture 101](https://www.chaosgenius.io/blog/clickhouse-architecture/) as well.


## Choosing the Right ClickHouse Modeling Strategy


After exploring ClickHouse’s capabilities for real-time analytics, the key question becomes: How do you choose the right modeling approach for your specific use case? As always, the answer depends on your data volume, latency requirements, complexity needs, and team capabilities. But we can say that ClickHouse lets us handle powerful use cases without the need for expensive ETL pipelines or an additional semantic layer.


For straightforward real-time scenarios, ClickHouse’s native features shine. You can [deduplicate within ClickHouse](https://clickhouse.com/docs/guides/developer/deduplication) to land consistent data in your cube, and use the [FINAL modifier](https://clickhouse.com/docs/sql-reference/statements/select/from#final-modifier) to let ClickHouse fully merge data before returning results. This performs all data transformations that happen during merges for the given table engine, eliminating the complexity of external processing.


**The ETL Pipeline Approach**

However, for more complex data projects, you can always handle execution through **[external ETL](https://clickhouse.com/docs/data-modeling/denormalization#orchestrating-and-scheduling-denormalization)** performed outside of ClickHouse using tools like dbt, Airflow, Dagster, Kestra, Flink, BladePipe, or dlt. These tools can orchestrate batch or streaming transformations before loading data into ClickHouse, which is especially useful for complex pipelines or when you want to manage schema evolution, data quality, or referential integrity outside the database. The [ClickHouse integration for dbt](https://clickhouse.com/docs/integrations/dbt) ensures this is performed atomically with a new version of the target table created and then atomically swapped with the version receiving queries via the [EXCHANGE](https://clickhouse.com/docs/sql-reference/statements/exchange) command.


Modeling outside of ClickHouse is a common approach with more complex landscapes, but if we want real-time analytics, batch ETL can break the flow of continuously updated streams. That’s why this shouldn’t be the first choice if you want real-time data, quickly updated.


**The BI Approach**  There’s also a tradeoff with storing metrics within the OLAP cube versus outside of it. Because SQL aggregations and measures can be queried on the fly but can’t be stored within ClickHouse easily, data modeling often happens outside ClickHouse or gets stored within BI tools. The **advantage** is you can change metrics at any time without running an ETL pipeline. The **downside** is you can’t easily store or manage them except in your UI, whether it’s a web app with an [OLAP-ORM](https://clickhouse.com/blog/moosestack-does-olap-need-an-orm), notebooks, or Business Intelligence tools.


This is one reason why Rill [pairs so well](https://docs.rilldata.com/guides/rill-clickhouse/) with ClickHouse—it has a full-blown metrics layer built-in with all its capabilities out of the box. You can store metrics declaratively based on YAML, version control them, and update them in a governed way. For example, put them in a git repository and let users collaborate on these metrics, which then get blazingly fast query returns on ClickHouse. Rill gives you **another layer of data modeling** while using ClickHouse as a sub-second response query engine.


Ultimately, the choice between native ClickHouse modeling, external ETL pipelines, or BI tool integration comes down to balancing three key factors: data freshness requirements, transformation complexity, and team capabilities. ClickHouse’s native approach eliminates traditional ETL overhead for most real-time use cases, but the flexibility to layer additional tools when needed ensures your analytics architecture can evolve with your business requirements.


---


To get started, check out the [practical example](https://github.com/sspaeti/clickhouse-modeling-rill-example) that demonstrates ClickHouse ETL with NOAA weather data, or explore ClickHouse’s comprehensive [Schema Design](https://clickhouse.com/docs/data-modeling/schema-design) documentation, which guides you through all the steps including querying large datasets like StackOverflow’s 60+ million records locally within seconds.


---


```
Full article published at Rilldata.com - written as part of my services
```

[Discuss on Bluesky](https://bsky.app/search?q=domain%3A%20https://www.ssp.sh/blog/practical-data-modeling-clickhouse/)
|
[Clickhouse](https://www.ssp.sh/tags/clickhouse/)
[Real-Time Analytics](https://www.ssp.sh/tags/real-time-analytics/)
[Data Modeling](https://www.ssp.sh/tags/data-modeling/)
[Olap](https://www.ssp.sh/tags/olap/)
[S3](https://www.ssp.sh/tags/s3/)
[Rill](https://www.ssp.sh/tags/rill/)
[ETL](https://www.ssp.sh/tags/etl/)
[Partitioning](https://www.ssp.sh/tags/partitioning/)
[Aggregation](https://www.ssp.sh/tags/aggregation/)
[Dashboard](https://www.ssp.sh/tags/dashboard/)
[Services](https://www.ssp.sh/tags/services/)
