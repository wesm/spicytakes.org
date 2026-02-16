---
title: "Scaling Beyond Postgres: How to Choose a Real-Time Analytical Database"
date: 2025-03-11
url: https://www.ssp.sh/blog/scaling-beyond-postgres/
slug: scaling-beyond-postgres
word_count: 4307
---

![Scaling Beyond Postgres: How to Choose a Real-Time Analytical Database](https://www.ssp.sh/blog/scaling-beyond-postgres/featured-image.png)

Contents
This article was written as part of
[my services](https://www.ssp.sh/services)

Many data engineers and analysts start their journey with Postgres. Postgres is powerful, reliable, and flexible enough to handle both transactional and basic analytical workloads. It’s the Swiss Army knife of databases, and for many applications, it’s more than sufficient.


But data volumes grow, analytical demands become more complex, and Postgres stops being enough. Therefore, you’ve probably come across terms like OLAP (Online Analytical Processing) systems, data warehouses, and, more recently, real-time analytical databases. The lines between these solutionsâcloud data warehouses like Redshift, BigQuery, or Snowflake, OLAP cubes, and real-time streaming databasesâhave increasingly blurred.


The question becomes: When would you need to move beyond Postgres? When does scaling your PostgreSQL instance no longer make sense compared to a specialized cloud data warehouse? Or is there an even better solution for low-latency dashboards or customer-facing analytics apps? Can’t we just use a fast database?


This article will explore how real-time analytical databases address critical analytical requirements. We will explore the differences between cloud data warehouses like Snowflake and BigQuery, legacy OLAP databases like Vertica, and a new class of real-time analytical databases like ClickHouse and StarRocks that combine elements of both of these categories. We will also examine the categories of today’s analytics solutions and how to choose the right one. Finally, we will discuss the history of analytical databases and how to choose a migration path to such a database.


## The Limitations of Postgres for Analytics


Postgres has become the go-to database these days. Some say [Postgres is eating the database world](https://medium.com/@fengruohang/postgres-is-eating-the-database-world-157c204dcfc4), and they’re not wrong. However, the limitations of Postgres become apparent when you start focusing on analytics. Complex queries over large tables can result in slow response times. While Postgres works fine for ETL processes and backend operations, it struggles with serving customer-facing dashboards that require consistent, fast performance.


There have been various efforts to enhance Postgres’s analytical capabilities, including extensions like [CitusDB](https://github.com/paradedb/pg_analytics), [Swarm64 DA](https://dbdb.io/db/swarm64), [TimeScale](https://www.timescale.com/), and others. Despite these innovations, Postgres remains fundamentally an OLTP (Online Transaction Processing) databaseâoptimized for transactions, not analyticsâand trying to make it perform like an analytical database has diminishing returns.


These limitations explain why organizations eventually need purpose-built solutions optimized for analytical queries. The typical first step beyond Postgres is adopting a cloud data warehouse.


## Scaling Beyond Postgres to Cloud Data Warehouses


When people or companies start with their analytics, they usually start with a cloud data warehouse or a SaaS solution that handles all the compute and storage. If you are more adventurous, you can build one yourself with a [Lakehouse](https://www.databricks.com/blog/2020/01/30/what-is-a-data-lakehouse.html) (extension to Data Lake). Or, if you have the team and the skills, you can make one based on what the [open-source data engineering landscape](https://mad.firstmark.com/) provides us.


Either way, you have requirements such as business-facing BI dashboards, reports, or a data app that shows all measures and insights of your data platform that serves business people. The next step is typically to improve speed. Dashboards get bigger, and users query non-optimized data that is either too slow to calculate (sometimes needs ETL-load overnight) or filtering/clicking around is too laggy (above 1 second).


If you go with a cloud data warehouse vendor, the next level is cost. It doesn’t matter if it’s Google BigQuery, Snowflake, Azure Fabric, Oracle, or any other; the price will be high due to each query, no matter if production or development is running on expensive cloud compute. Additionally, you get locked in with that vendor. However, you get a lot of simplicity with simpler architecture and peace of mind. Some complexity, such as running on Kubernetes and orchestration, is abstracted with a custom service within that vendor’s platform. This abstraction is super convenient if that service delivers high-quality development or customer service and solves your requirements. Quite the opposite if that is not the case.


As always, this heavily depends on the majority and level of functionality you need, and it is not easy to make a choice.


### Cloud Data Warehouses Are Built for Scale, Not Speed


Cloud data warehouses are built – like physical warehouses in the real world – to enable storage and retrieval at massive scales with efficiency. However, in order to achieve these efficiencies, they rely on an architecture that separates storage and compute, introducing seconds of incompressible latency for every query. This performance hit is often unsuitable for many analytical applications (such as exploratory dashboards).


In addition to this performance gap, cloud data warehouses can also lead to higher costs. With Snowflake, you pay-per-query, which becomes expensive quickly, especially if your analytical applications are gaining traction and growing into more departments. Budgeting or predicting costs becomes more complex. This **cost-performance dilemma** is an important consideration.


This rising cost for analytics applications is one reason cloud data warehouses are getting bad press and losing ground. But what else should we use? What are the alternatives?


What if we pre-aggregate data so that queries get cheaper? We don’t pay the actual computing of running the query, but “only” the cache to keep the aggregations in memory. What if we could leverage column-oriented designs better to profit from fast filters and drilling down? Aren’t we coming full circle and talking about OLAP systems and data marts from the 1990s? Let’s see if we can answer these questions.


## The Evolution of Analytical Systems


Let’s look at where we come from and why history has chosen analytical systems such as OLAP cubes and cloud data warehouses.


### OLAP Pioneers


Early in my career, I was working with OLAP cubes in Oracle and SAP. But the one that didn’t fade was SQL Server Analysis Services (SSAS) from Microsoft. During my consultancy, SSAS was used by every client. It was the magic ingredient to create extremely fast and responsive dashboards; we could hide complex calculations inside the cube and pre-calculate them.


Additionally, **Microsoft built an Excel connection**. The integration meant that the biggest BI tool, Microsoft Excel, could query the same data from the pre-aggregated and well-defined KPIs within seconds. Users didn’t need to recreate the business calculations repeatedly in their siloed Excel sheets; instead, they could do it centrally once. Everyone benefited from that.


Obviously, there were downsides. With SSAS cubes, it was the bottleneck of a central BI team. Changes to SSAS cubes were not made in minutes; it took a long time to change, test, and redeploy in most cases. However, to a large extent, the speed advantages outweighed the downsides.


To this day, SSAS, mostly tabular on Azure cloud, is used to power complex and heavy Power BI dashboards. But many new modern OLAP systems have started to grow, too. They were open-source and code first, compared to the SSAS, which is visual only, making it hard to collaborate, automate, or generate new cubes or metrics.


OLAP cubes were **revolutionary** due to their pre-calculated aggregations and slice-and-dice capabilities on the fly. However, the mentioned limitations, such as rigid schema and long processing times, eventually led to their decline.


### A Brief History of OLAP and Related Analytics


A short evolution of OLAP systems shows that shortly after Edgar F. Codd coined the term OLAP, the first MOLAP systems (Essbase) were created. In 1998, with the first release of Microsoft OLAP Services with SQL Server 7.0, OLAP was known more widely and, later, in the early 2000s, used across businesses around the world. SSAS revolutionized business intelligence by making multidimensional analysis accessible to a broader audience. Its **integration with Excel**, the world’s most widely used analytical tool, was particularly transformative.


In 2005, the open-source C-Store project was announced by Michael Stonebraker’s team at MIT with columnar rather than row-based storage. It spawned the creation of Vertica and kicked off a wave of both open-source and commercial analytical database designs that would eventually transform the OLAP landscape.


Vectorized query execution, pioneered by systems like MonetDB and later adopted by ClickHouse (created in 2010), processed data in column “chunks” rather than individual values. This approach took full advantage of CPU cache hierarchies, pipelining, and SIMD instructions, delivering order-of-magnitude performance improvements. In 2012, Apache Druid was created at Metamarkets, and in 2013, Apache Pinot was developed at LinkedIn. In 2016, ClickHouse became open-source, and in 2017, Apache Doris became open-source by Baidu. Around 2018, StarRocks was forked based on Doris.


These major releases led to today’s growth of cloud data warehouses and **hybrid** OLAP warehouse systems, especially with the decoupling of storage and compute becoming standard.


Looking at the key elements of such analytical systems, we see that storage innovation, query processing, scalability, and aggregation methods are playing a big part here:


![/blog/scaling-beyond-postgres/mermaid-characteristics.jpg](https://www.ssp.sh/blog/scaling-beyond-postgres/mermaid-characteristics.jpg)

*Characteristics of an Analytical System*

Did we've Come Full Circle?

While the technical evolution of analytical systems appears to be a linear progression, it is cyclical, addressing the same fundamental challenge: **balancing performance with flexibility**.


Early OLAP systems achieved incredible speed through pre-aggregation but sacrificed flexibility. Modern systems return to OLAP principles with dynamic rather than static aggregation, enabled by hardware advances that early OLAP architects could only dream of.


## Two Categories of Analytical Databases: Warehouses and Real-Time DBs


Let’s now focus on today, examine the different categories of analytical databases, and see if we can find differences between cloud data warehouses and OLAP cubes.


Mike Driscoll said in our discussion: “All of these databases belong in the **category of analytical databases**âthey all leverage column-oriented designs and are fast for aggregations and filters, and are considered OLAP databases”.


Mike further shared that the significant difference between these analytical databases is the trade-off between **cost** (dollars-per-TB-stored) and **performance** (seconds-per-TB-scanned). I agree, and this is what we’ve seen happening lately. On one side, cloud data warehouses like Snowflake use **decoupled cloud storage + compute architectures**, offering lower cost but with lower performance.


Cloud data warehouses introduce higher latencies per query since there’s no guarantee that the data is in memory; it may need to be fetched from or scanned from its internal storage, or even slower, from a data lake in the form of object storage. Notably, none of these offerings are open source; they are pure software as a service (SaaS).


Conversely, real-time analytical databases like ClickHouse, Pinot, Druid, and DuckDB **achieve higher performance by co-locating compute and storage**1. These systems keep frequently accessed data and aggregations in memory, enabling extremely fast query performance, similar to what the initial OLAP solutions such as SSAS and others did best initially.


These discoveries lead us to **two main categories** of analytical databases:

1. Cloud data warehouses (Snowflake, Redshift, BigQuery, Azure Fabric, Firebolt)
2. Real-time analytical databases (ClickHouse, Pinot, Druid, DuckDB, Starrocks, Doris, Kylin).


If we categorize real-time analytical databases further, there might be a trade-off between **scale vs. complexity**.


Pinot and Druid are highly scalable and designed from the ground up as **distributed systems**. ClickHouse was initially architected as a **single-node system** but has since added support for horizontal scaling in its OSS and commercial cloud offering. DuckDB is intentionally **non-distributed** and has a **single-node architecture** (though MotherDuck is working on a more scalable, distributed cloud version).


At the end of the day, engineers need to choose an analytics database technology based on trade-offs across cost, performance, scale, and complexityâwhich ultimately only our business use cases can determine. Let’s explore related technologies and how to choose the right one for our needs next.

Cloud Data Warehouses or Cloud Data Platforms?
Snowflake, Fabric and BigQuery call themselves data platforms nowadays. They do more than just data warehousing. But it’s where they started and probably where they still mostly fall into.

### Related Categories (Streaming, Vector, Federation)


There are several related technologies that we exclude for the comparison in this article, but are nonetheless essential to mention.


There are many **streaming** technologies out there. In a sense, real-time analytical databases combine streaming and cloud data warehouses that update and handle events. Estuary [categorized](https://estuary.dev/blog/the-real-time-data-landscape-2025/) into different buckets such as capture, transport, operation, and analytics on one axis, and open-source, hybrid, and managed (closed-source) on the other:


![/blog/scaling-beyond-postgres/landscape_2025_streaming.jpeg](https://www.ssp.sh/blog/scaling-beyond-postgres/landscape_2025_streaming.jpeg)

*Streaming Data Landscape | Image byEstuary*


This overview is interesting, as we have mixed technologies - some that do only the discussed compute, others that do compute + storage, and some that are mixed. Let’s explore further how we can choose the right path for our needs.


However, two more related categories are doing similar things to what is discussed here. The first category is **vector databases** such as Pinecone, Qdrant, Chroma, and Weaviate, which are powerful backend databases for Large Language Models (LLMs). These are mostly a mix of compute and storage but are optimized for AI. They provide a simple and straightforward way for AI engineers to store and query their rehashed data.


The second category is **federation** solutions such as Dremio, Trino, and Apache Arrow. It’s a middle ground between cloud DWHs and real-time analytical databases, where we virtually join different data sources as a logical entity **without the need to move and copy** data around or pre-aggregate, though there are caches, too.

Combining Streaming and Batch is Not New
This reminded me of Delta Lake Tables, or
[Open Table Formats](https://www.startdataengineering.com/post/what_why_table_format/)
when we tried to use them as a sink for both stream and batch jobsâunifying batch and streaming sources and eliminating the need for a
[Kappa Architecture](https://hazelcast.com/foundations/software-architecture/kappa-architecture/)
. This is important to remember with additional features such as built-in CDC, streaming capabilities, and sharing features. More of this is well explained in
[Beyond Lambda: Introducing Delta Architecture](https://youtu.be/FePv0lro0z8)
or through
[code examples](https://docs.delta.io/latest/delta-streaming.html#delta-table-as-a-sink&language-python)
.
Single-Node Processors
Also related, check out single-node processors such as Polars, Pandas, Apache Arrow, DataFusion and DuckDB.

### The Real-Time Analytical Databases


So, what are real-time analytical databases?


Real-time databases allow us to have extremely fast response times, which is needed for time-critical analytics. They may additionally enable real-time updates through direct streaming ingestion, similar to streaming solutions. They allow a lower-cost approach in terms of cost-per-query if you have an analytical, query-heavy workload.


Real-time analytical databases use modern OLAP technologies to combine the best of traditional OLAP systems with modern analytical capabilities. Some of the benefits of real-time analytical databases:

- **Sub-second query response times** enable interactive dashboards and analytics experiences
- **Columnar storage optimization** dramatically speeds up aggregations and filtering by reading only the needed columns, reducing I/O bottlenecks.
- **Vectorized processing** leverages modern CPU capabilities to process data in chunks rather than row-by-row, delivering performance gains.
- **Cost efficiency** is achieved through co-located compute and storage architecture that eliminates expensive data movement between layers. Co-located compute also allows direct access to data without network transfer delays, reducing query latency.
- **Real-time data ingestion** supports streaming and batch processing, enabling fast insights from fresh data without separate pipelines.
- **Lower operational costs** for query-heavy analytical workloads as pre-calculated and not charged for each query.
- **More flexibility** by relaxing some of the constraints of traditional OLAP databases, for instance by enabling JOIN and UPSERT operations.
- **Open-source foundations** provide vendor independence and community-driven innovation, reducing lock-in risks compared to proprietary solutions.


Real-time databases serve analytical data in sub-seconds but have an additional overhead and some disadvantages; let’s look at how to choose the right tool for the right job.


## When to Choose a Real-Time Analytical Database?


So, how do you ensure the best choice for you?


Choosing the approach and solutions to replace a cloud data warehouse for low-latency analytics solutions requires careful consideration of specific needs, constraints, and objectives. Let’s explore how to make this decision strategically.


![/blog/scaling-beyond-postgres/scale-and-speed-2.jpg](https://www.ssp.sh/blog/scaling-beyond-postgres/scale-and-speed-2.jpg)

*Decision Quadrants for Choosing a Analytical Databases*


For example, if you need a lot of joins or cleansing of your data (e.g., complex data pipelines), an OLAP cube isn’t optimized for joins. Pre-joining or cleansing the data beforehand is something that cloud data warehouses are much more suitable for.


Also, adding a real-time analytical database alongside an existing cloud data warehouse might be more complex and costly initially. Still, it is worth investing in this additional layer if customer-serving analytics handles all required queries in **sub-seconds** compared to multiple seconds or minutes.


But could we eliminate our cloud data warehouse entirely? What if, instead of a cloud data warehouse, we used a low-cost data lake for slower reporting and used only a real-time analytical database for serving applications? What is the ROI of potentially migrating away from a cloud data warehouse?


### Real-Time Analytical Database Selection Guide


The above quadrants show us a high-level overview of what we’ve discussed here and serve as a guide to help you choose the right analytical solution. With the decision tree below, we can address the most important questions and evaluate which database is the best fit for our needs.


![/blog/scaling-beyond-postgres/mermaid-decision-tree.png](https://www.ssp.sh/blog/scaling-beyond-postgres/mermaid-decision-tree.png)

*Decision Tree to choose the right analytical DB*

Categories are not strictly defined
The lines between categories are blurred. OLAP systems now add warehouse features, while data warehouses add OLAP-like capabilities. This convergence reflects an underlying fact that the business needs to constantlyâdeliver accurate insights quickly and cost-effectively.

#### Hybrid Approaches


Many modern architectures combine multiple approaches to leverage their respective strengths.


For example, **Data Warehouse + OLAP** pairs warehouse capabilities for complex transformations and joins with OLAP for serving analytical queries, which is ideal when you need both complex data manipulation and fast query responses. The **Data Lake + OLAP** pattern stores raw data in a lake while materializing aggregates in an OLAP engine, which is best suited when data volume is high but query patterns are predictable. Finally, **Federation + Materialization** allows querying data in place when possible while materializing frequently accessed paths, which is particularly effective when data is distributed across multiple systems.


### Understanding When to Use Real-Time Analytical Databases


Three key reasons one would choose a real-time OLAP solution are stated below.

1. **You need sub-second queries** - If your use case demands response times under 1-2 seconds:
2. **You’re running query-heavy workloads** - When query volume is high:
3. **You want zero-disk architecture benefits** - Real-time analytical databases systems can:

Zero-Disk vs. Zero-ETL
If you are confused about zero-ETL or wonder if they are related, these address different challenges. “Zero-disk” uses cloud object storage instead of dedicated disks, while “zero-ETL” eliminates traditional data movement pipelines. Real-time analytical databases often use zero-disk for cost optimization, while zero-ETL focuses on federation capabilities.

### Real-Time Analytical Database Comparison and Features


If we compare the four of the real-time analytical databases and rate them according to their feature, that could look like this:



| Attribute | ClickHouse | StarRocks | Druid | Pinot |
| Query Performance | â­â­â­â­ | â­â­ | â­â­ | â­â­â­ |
| Scalability | â­â­â­ | â­â­â­ | â­â­â­â­ | â­â­â­ |
| Developer Experience | â­â­â­â­ | â­â­ | â­ | â­â­ |
| SQL Support | â­â­â­ | â­â­â­â­ | â­ | â­â­ |
| Data Lake Support | â­â­â­â­ | â­â­ | â­â­ | â­â­ |
| Streaming Support | â­â­ | â­ | â­â­â­ | â­â­â­â­ |
| Community Strength | â­â­â­â­ | â­â­â­ | â­ | â­â­ |



Takeaways from this comparison are:

1. **ClickHouse** excels in SQL capabilities and vectorized processing, with strong columnar storage optimization. It was initially designed as a single-node system but has since added horizontal scaling support.
2. **StarRocks** offers excellent scalability with low operational complexity, balancing performance and management overhead well.
3. **Druid** and **Pinot** were built from the ground up as distributed systems, with Pinot particularly strong in streaming ingestion (developed at LinkedIn).
4. All four systems provide sub-second query response times, though they achieve this through slightly different architectural approaches.


Find more insight into GitHub activity and community building in [State of Open Source Real-Time OLAP Systems 2025](https://practicaldataengineering.substack.com/p/state-of-open-source-read-time-olap-2025).


### Additional Characteristics and Consideration


Furthermore, we can look at data characteristics, query patterns, technical constraints, or ergonomic factors we may have.


Check volume and growth rate, how frequently (batch vs streaming) data is updated, and structure and complexity called **data characteristics**. Analyze your **query patterns**. Do you have many predefined vs ad-hoc queries and complex joins? And how many concurrent queries need to run? These determine the acceptable response time.


Do you have **technical constraints**? For example, do you have the team expertise? Do you need to be on-prem or on the cloud? What integrations do you need with other tools from your data stack? Consider security and compliance.


Developer-friendliness or **ergonomic factors** play another role. Can you quickly deploy and integrate into your DevOps tooling? How predictable are costs? And what is the business impact if insights are delayed?


## Migration Strategy


Let’s say you have a cloud data warehouse and have discovered, with the above guide, that a real-time analytical database would suit your needs better.


### Migration Guide


There are many migration guides. For example, the [ClickHouse guide](https://clickhouse.com/docs/integrations/migration/overview) offers paths to migrate from DBMS, ETL/ELT tools, object storage, or the cloud data warehouse Redshift.


Migrating to real-time analytical databases requires thoughtful schema optimization - denormalize where appropriate, choose sort keys based on query patterns, and use compact data types to improve compression and performance.


Your migration approach depends mainly on your infrastructure constraints and data volume. PUSH methods using ETL tools like Airbyte and dlt offer transformation capabilities, and PULL methods enable direct database connections. Meanwhile, PIVOT approaches using cloud storage work best for large-scale migrations with parallel processing.


For a successful transition, implement a phased migration starting with a single data mart while running systems in parallel to validate query results and performance. Establish proper monitoring, backup procedures, and scaling strategies for your new environment. Consider operational factors like data freshness requirements and query patterns to ensure your real-time analytical database delivers the expected improvements.

Common Pitfalls and How to Avoid Them

Underestimating **schema optimization** is perhaps the most common mistake. While most real-time analytical databases can handle any schema, performance varies dramatically with proper design. Start by profiling your existing queries to identify access patterns before migration.


Another frequent pitfall is attempting to **migrate all** workloads simultaneously; instead, prioritize use cases where real-time performance delivers immediate value. Be cautious about replicating your warehouse’s data modeling patterns, as real-time analytical databases often perform best with different joins, aggregations, and partitioning approaches.


Finally, don’t neglect data validation. Implement reconciliation processes to **verify data consistency** between systems during parallel operation phases.


### ROI and Cost Considerations


Real-time analytical databases deliver ROI through multiple avenuesâdirect cost savings on query-heavy workloads, substantial performance improvements with sub-second query times, and increased business agility by encouraging more data exploration without penalty.


Organizations often report reductions in their analytics spending after migration, particularly those with high query volumes or dashboards that previously required expensive compute resources. Track metrics like dashboard load times, user engagement with analytical tools, and the business impact of **faster decision-making** to quantify your migration’s value.


Real-time analytical databases often use a resource-based pricing model with more predictable costs. This shift can reduce expenses for analytical workloads since you’re not paying for each operation, though initial infrastructure setup may require investment.


The engineering trade-offs include potentially higher complexity in deployment and maintenance. Still, reduced query expenses and performance gains can typically offset these costs. Plus, the real-time analytical databases have better and better onboarding scripts and documentation.


A good exercise is to conduct a three-month total cost comparison between your current warehouse and the proposed real-time analytical database to establish a clear financial baseline for your migration decision, including the benefits you’ll gain from either solution.


## Looking Ahead: The Future of Analytical Systems


While Postgres remains an excellent starting point for many organizations and continues to evolve with extensions like pg_analytics, the future belongs to purpose-built analytical systems that deliver the holy trinity of database needs: consistency, scalability, and cost-efficiency.


The evolution I predicted in my 2018 article on [OLAP and what’s coming next](https://www.ssp.sh/blog/olap-whats-coming-next/) has largely materialized, with the categories remaining relevant today. What’s changed is how these systems have matured and converged. Cloud data warehouses have expanded into comprehensive data platforms, while real-time analytical databases have incorporated more warehouse-like featuresâdriven by the universal need for faster insights at manageable costs.


Today’s landscape shows two parallel trends:

1. **Scaling down**: Single-node engines like Polars, DuckDB, and [ClickHouse-Local](https://clickhouse.com/docs/operations/utilities/clickhouse-local)/[chDB](https://clickhouse.com/docs/chdb) bring real-time analytics capabilities to local environments, democratizing access to powerful analytical tools.
2. **Scaling up**: Real-time analytical databases continue to improve their distributed architectures, making complex analytical systems more accessible to organizations without specialized expertise.


SQL remains the universal language, and its widespread adoption has enabled real-time analytical databases to flourish, while innovations like code-first applications and [GenBI](https://www.rilldata.com/blog/bi-as-code-and-the-new-era-of-genbi) are lowering the barrier for non-technical users to participate in data-driven decision-making.


Deployment will also be key to this. With serverless being omnipresent, can we quickly deploy a serverless real-time analytical database? Maybe not as soon as a relational database, but we’re getting there.


It is exciting to see how real-time analytical databases are promising. They can unify the architecture of databases and real-time architecture into one, allowing business insights and KPIs to be explored instantly without the need for pipelines and duplicated storage that characterized earlier generations of data systems.


As organizations outgrow Postgres for their analytical needs, they now have a spectrum of options that weren’t available just a few years agoâfrom cloud data warehouses to real-time analytical databases, each with its strengths and tradeoffs. The key is understanding your specific requirements and choosing the right tool that balances performance, cost, and complexity for your unique analytical journey.


---


```
Full article published at Rilldata.com - written as part of my services
```


---

1. It should be noted that ClickHouse Cloud has made headway in building a decoupled compute and storage architecture, similar to Snowflake, enabling separate compute workloads to operate on shared storage. [https://clickhouse.com/blog/introducing-warehouses-compute-compute-separation-in-clickhouse-cloud](https://clickhouse.com/blog/introducing-warehouses-compute-compute-separation-in-clickhouse-cloud) ↩︎

[Discuss on Bluesky](https://bsky.app/search?q=domain%3A%20https://www.ssp.sh/blog/scaling-beyond-postgres/)
|
[Postgres](https://www.ssp.sh/tags/postgres/)
[Rill](https://www.ssp.sh/tags/rill/)
[Business-Intelligence](https://www.ssp.sh/tags/business-intelligence/)
[Olap](https://www.ssp.sh/tags/olap/)
[Clickhouse](https://www.ssp.sh/tags/clickhouse/)
[Real-Time](https://www.ssp.sh/tags/real-time/)
[Data-Warehouse](https://www.ssp.sh/tags/data-warehouse/)
[Cloud Data Warehouse](https://www.ssp.sh/tags/cloud-data-warehouse/)
[Druid](https://www.ssp.sh/tags/druid/)
[Services](https://www.ssp.sh/tags/services/)
