---
title: "Beyond Basic ETL: Enterprise Data Capabilities Without the Complexity"
date: 2025-10-13
url: https://www.ssp.sh/blog/beyond-basic-etl/
slug: beyond-basic-etl
word_count: 3031
---

![Beyond Basic ETL: Enterprise Data Capabilities Without the Complexity](https://www.ssp.sh/blog/beyond-basic-etl/featured-image.png)

Contents
This article was written as part of
[my services](https://www.ssp.sh/services)

Most data teams spend 80% of their time wrestling with infrastructureâwriting custom UPSERT logic, building incremental loading from scratch, or debugging why their Airflow DAGs failed again at 2 AM. Meanwhile, the business is still waiting for those critical data insights.


This article is a follow-up to [Part 1](https://www.ssp.sh/blog/declarative-data-stack-enterprise/), where we explored declarative data stacks. Here, we dive into the specific capabilities that let you skip most of the engineering challenges and focus on delivering business value. You’ll discover how to extract and load data from multiple sources with built-in quality controls, configure complex write strategies like SCD2 and UPSERT with simple configuration changes, and transform data using SQL that transpiles seamlessly across BigQuery, Snowflake, Databricks, and DuckDB. We’ll also explore how to generate production-ready orchestration workflows without writing custom code, all while testing locally before deploying to production.


By the end, you’ll see how declarative approaches can eliminate custom development while giving you enterprise features that usually require dedicated platform teams, from automated data quality validation to intelligent dependency management across multiple execution engines.


*In Part 3, we’ll explore advanced use cases and unique features that make Starlake particularly powerful for complex data scenarios.*


## Why Declarative Data Stacks Go Beyond the Modern Data Stack


Let’s quickly recap why you’d want a [declarative data stack](https://www.rilldata.com/blog/the-rise-of-the-declarative-data-stack). The modern data stack is only a definition and not something that exists physically. But generally, it’s defined as a modular stack where you can flexibly exchange certain data tools and combine them, leading to integration into an end-to-end data platform.


This is also where most of the frustration comes fromâsome of them do not work well together, and it’s a lot of work with constant changes on each of the tools while you try to build. Though the code and license to use the tools cost nothing, it’s expensive to set up yourself if you don’t have the expertise.


This is where a declarative stack comes in handy. It’s a pre-built framework to **stitch together the best-in-class tools**. It’s opinionated toward tools that work well together, but that comes with a big efficiency gain. Plus, you can get started in minutes, as everything is declarative.


Starlake, for example, allows you to configure your stack with only configurations. It’s as if it came from one vendor or platform, and you have a **unified configuration layer** to set up and configure your data stack despite using various tools from the data stack behind the scenes.


### The Configuration-First Approach to Data Platform Building


A declarative data stack lets you focus on the business challenges and use automation with orchestration and other complex topics that are usually added as an afterthought from day one. Because Starlake is open-source and uses the so-called Modern Data Stack, there’s no vendor lock-in.


Starlake uses **external engines** to run its compute. With SQL transpilers and support for multiple engines, you can easily switch your compute while having the same business logic and integration from Starlake. Plus, you get **instant scaling** through having external engines.


Where declarative data stacks shine is when complexity grows. With a predefined setup that’s built and used in some of the biggest companies in France and elsewhere, you are prepared for that growth. Starlake was built from the ground up to fix this with declarative configurations. Instead of glue code, type-safe definitions, built-in orchestration integration, and full cloud flexibility, all open-source.


If you want to know more about Starlake’s open-source declarative data platform and why you might consider it for an enterprise use case, I suggest checking out [Part 1](https://www.ssp.sh/blog/declarative-data-stack-enterprise/) first. Otherwise, let’s explore Starlake in action before we focus on the key features that make it very interesting for data engineers later in this article.


## Complete ETL and Data Engineering Capabilities


In this chapter, we cover capabilities that every data engineer needs for a successful analytics solution: solving the fundamental data engineering jobs and delivering analytics results with capabilities that come out of the box with Starlake, supporting beyond basic ETL.

*Illustration of Starlake with its modular structure from extract, load and transform, connected by orchestration.*


Illustration of Starlake with its modular structure from extract, load and transform, connected by orchestration.


Powerful features include:

- No-Code Data Ingestion: Connect to any data source through simple YAML configurations without writing custom extraction code.
- Data Governance and Quality at every step: Built-in validation rules and lineage tracking ensure data reliability from ingestion to analytics.
- Automated Workflow Orchestration: Dependencies and scheduling are handled automatically based on your declarative configurations.


In the next chapters, we go through them step by step and elaborate on how a declarative data stack like Starlake works and the capabilities it offers.


### Extract & Load: From Source to Warehouse


**Extracting** is the direct way to load from your source databases. The extraction lets you extract tables in one shot and incrementally from a database as a set of files.


**Load**, on the other hand, is when you [load from local files or files](https://www.youtube.com/watch?v=m490VNeASC0) on S3/R2, for example. This is loading your Parquet, CSV, or JSON files.


#### Supported Data Sources


Starlake supports a comprehensive range of data sources:



| Category | Data Sources |
| **File Formats** | **Structured:** CSV, TSV, PSV (with multi-char separators)
**Semi-structured:** JSON, XML, YAML
**Binary:** Parquet, Avro, ORC
**Compressed:** ZIP, GZIP, BZIP2
**Other:** Fixed-width position files, Excel spreadsheets |
| **Cloud Storage** | Amazon S3, Google Cloud Storage, Azure Blob Storage, Local filesystem |
| **Databases & Warehouses** | Snowflake, BigQuery, Redshift, Databricks, PostgreSQL, MySQL, Oracle, SQL Server, DuckDB/Ducklake, any JDBC Databases |
| **Streaming & Events** | Apache Kafka, Amazon Kinesis, Google Pub/Sub, Azure Event Hubs |



For some warehouses or cloud providers, deep integration exists. For example, with Snowflake through Snowflake’s Native App capability, you simply install: `install starlake -> native app` and get all the features inside Snowflake. This allows you to avoid sharing your Snowflake credentials with an external SaaS platform and avoid data exfiltration, as well as use your Snowflake compute credits to run Starlake and have a unified bill.


You can use markup on top of Snowflake and avoid DevOps. With Starlake as a native app, it means no security headaches, credentials are never shared, and no data is exfiltrated. Everything is SQL, and the data is secure in Snowflake. You save a lot of time by not needing to do this work.

Organized by Domain

In Starlake, the data is organized by domains. A domain is a database schema also called a dataset on BigQuery.


#### Built-in Quality Features


The loading capabilities go beyond moving files. For example, we can set data types and their format at the beginning when we load, which applies them for everyone at the very beginning of loading. We can set attributes and [write strategies](https://docs.starlake.ai/guides/load/write-strategies)

such as `APPEND`, `OVERWRITE`, `UPSERT_BY_KEY`, `UPSERT_BY_TIMESTAMP`, `DELETE_THEN_INSERT`, `SCD2`, or even `ADAPTIVE`. These are all very powerful on their own, as typically you’d need to write your own extensive custom code, especially for incremental, [Slowly Changing Dimension (Type 2)](https://www.ssp.sh/brain/slowly-changing-dimension-type-2/), or UPSERTs. Having these integrated and switching quickly by just changing the *writing strategy* is handy and significant.


![/blog/beyond-basic-etl/starlake-write-strategy.png](https://www.ssp.sh/blog/beyond-basic-etl/starlake-write-strategy.png)

*Example of how to load data and its configurations in Starlake GUI*

Dedup Strategy for Better Data Quality

Write Strategies help you always make sure users won’t see duplicated rows where specified. For example, you can specify that a customer data table should be deduped, and Starlake makes sure to upsert the data accordingly.


**[Type Validations](https://docs.starlake.ai/guides/load/validate)** and **[expectations](https://docs.starlake.ai/guides/load/expectations)** are two features to improve data quality out of the box. It validates the types of the data you are loading by specifying the schema, and with expectations, allows you to test if the resulting table contains the expected data.


**[Transform on Load](https://docs.starlake.ai/guides/load/transformj)** to quickly add columns you need but are not provided by the source database, such as load-time or locally formatted timestamp.


For `BigQuery` and `Databricks`, there is a feature that supports their user-defined **[clustering and partitioning](https://docs.starlake.ai/guides/load/sink)** to improve the performance of queries on large datasets.


**[Access Control](https://docs.starlake.ai/guides/load/security)** with ACL or row-level security for Snowflake, BigQuery or Spark is built in. This is pretty cool.


![/blog/beyond-basic-etl/starlake-acl.png](https://www.ssp.sh/blog/beyond-basic-etl/starlake-acl.png)

*Starlake GUI to configure ACLs.*


All of these configurations have one place to configure all your data needs, and they will be propagated downstream to all your consumers.


Other powerful and advanced enterprise features that you’d spend much time and effort to build otherwise are:



| **No-Code Data Ingestion** | **Cloud-Native Integration** | **Security & Governance** |
| Real-time streaming via Kafka | Native AWS, GCP, Azure support |  |
| Built-in error handling & recovery | Cloud-agnostic deployment | Column-level encryption |
| Alerting, Freshness, Schedule | Serverless execution | Data masking & anonymization |
|  | Multi-cloud data sync | Audit logging & compliance |
|  |  | GDPR & CCPA support |



Beyond core data processing, Starlake excels in development workflow and platform integration:



| **CI/CD Integration** | **Version Control & Testing** | **Platform Integrations** |
| Git-based version control | Automated testing with DuckDB | GitHub Actions |
| Pipeline validation workflows | Infrastructure as Code support | GitLab CI |
|  |  | Azure DevOps |
|  |  | Jenkins |



#### Data Modeling and Schema Definition


We can also define foreign keys and primary keys in the load menu. This helps us model the data when we combine different sources and create new tables, or if the data source does not have any proper relations set.


![/blog/beyond-basic-etl/starlake-attribute.png](https://www.ssp.sh/blog/beyond-basic-etl/starlake-attribute.png)

*Starlake worksheet data transformation example.*


### Transform: Integrate Business Logic Simplified


Transforms are the critical business logic. We define them mostly in SQL and Python, and custom transformations are also possible. We can define them in the worksheet.


![/blog/beyond-basic-etl/starlake-worksheet.png](https://www.ssp.sh/blog/beyond-basic-etl/starlake-worksheet.png)

*Starlake worksheet data transformation example.*


We can then **preview** our transformation to check if we have the right granularity or result. But beyond that, we can **[transpile into other SQL](https://labs.starlake.ai/)** dialects if we want to test our DuckDB SQL on our Spark or BigQuery cluster. This allows us to test the SQL on top of an in-memory DuckDB database without hitting the data warehouse, inducing more interactivity and less cost.


If you click on preview, it will show transpiled code for the current configured engine that’s going to be run. Or we can just check the **lineage** for that aggregation.


![/blog/beyond-basic-etl/starlake-result.png](https://www.ssp.sh/blog/beyond-basic-etl/starlake-result.png)

*Preview our data aggregationâor hit transpiled or lineage to see more detailed information.*


These transformations can be stacked upon each other, building your data application with newly created data models and powerful aggregations. Check out a demo [here](https://www.youtube.com/watch?v=B6xEomPtvCY).


![/blog/beyond-basic-etl/starlake-lineage.png](https://www.ssp.sh/blog/beyond-basic-etl/starlake-lineage.png)

*An example of column-level lineage with its dependencies and an overview of your data assets in the web UI. Hovering with the mouse will reveal the transformation applied (seeSUM()above).*

Lineage from plain SQL

Thanks to its deep integration with open-source projects like JSQLParser and JSQLTranspiler (both funded by Starlake), the platform can automatically infer data lineage directly from your SQL statements. This enables Starlake to generate orchestrator DAGs and manage dependencies without requiring manual Jinja references or explicit dependency declarations. As a result, orchestration order and lineage tracking are handled by the platform, freeing developers from boilerplate and reducing the risk of errors.


This also makes it easy to copy and share queries with other team members, streamlining collaboration and reducing friction in your workflow.


### Tests: Ensuring Data Quality at Scale


The next step is to test, orchestrate, and deploy. Testing is most important in data engineering and data analytics platforms because if we have false key performance indicators (KPI) or get inconsistent data, business consumers of the data won’t trust the data anymore.


That’s where extensive tests such as **[unit tests](https://docs.starlake.ai/guides/unit-tests/concepts)** and full tasks for loading or transformation come in. These tests check the correctness of the data transformations, the data loading process, and the data quality.


**[Type validation](https://docs.starlake.ai/guides/load/validate)** is built-in and done with DuckDB. For example, you can get quite creative to define your types and have them validated ahead of runtime through a test dataset.


When you have rejected rows during a production run, these can be written to specific **rejected tables** with rows that invalidated the definition, including a [report summary](https://docs.starlake.ai/guides/unit-tests/load-tests#example-load--summary-report). This allows only valid data in the system and provides an elegant way to send a report based on the rejected table to the domain owner with invalid data for further analysis.


The best part is that Starlake allows you to test load tasks locally (using DuckDB) before deploying to production. This helps you save many development cycles as we can avoid running a long-running task at night only to find a typo in the morning.


### Orchestrate: Automated Workflow Management


[Orchestration](https://docs.starlake.ai/guides/orchestrate/tutorial) is for scheduling the transformations on a regular schedule using your orchestration tool of choice. For example, Dagster, Airflow, or Snowflake Tasks are integrated.


Starlake doesn’t have its own orchestrator but uses major open-source ones. It natively integrates with Dagster or Airflow, or you can use Snowflake Tasks (Snowflake’s native orchestrator), to run compute. The motto is to always use the cloud orchestrator that already exists or is in use.


#### No-Code DAG Generation with Templates


Furthermore, Starlake supports [templating](https://docs.starlake.ai/guides/orchestrate/customization) for customizing the DAG generation using Jinja2 and Python. This helps load similar tasks with the same template, helping to maintain consistency across a large codebase.


DAG generation relies on command line tools, configurations, templates, and the starlake-orchestration framework to manage dependencies. Templates for data loading and transformation can be customized with runtime parameters using Python variables like `jobs` and `user_defined_macros`. Dependencies between tasks can be managed either inline (generating all dependencies) or through external state changes using Airflow datasets or Dagster Assets.


The best part is that users can schedule advanced schedules **with code-free templating**, also called no-codeâyou just select one of the predefined/custom orchestrator templates and let Starlake generate and deploy your DAGs on your selected orchestrator. See some examples in [Orchestration Tutorial](https://docs.starlake.ai/guides/orchestrate/tutorial).


Furthermore, you get intelligent and visual dependency management with parallel execution when needed, and automated error handling and recovery. It’s a key component of Starlake, as it not only defines the data stack via flexible configurations but can also run it with whatever **execution engine** your data organization uses.


#### Multi-Engine Flexibility and Cross-Platform Support


In fact, Starlake supports [multi-engines and works across different ones](https://docs.starlake.ai/#multi-engine--cross-engine).


What does that mean? This concept is what differentiates it from normal data stacks that can run only a proprietary engine. This way you have a well-defined configuration for your data stack and business logic, but with the flexibility to exchange to newer or faster engines.


![/blog/beyond-basic-etl/multi-cross-engine.png](https://www.ssp.sh/blog/beyond-basic-etl/multi-cross-engine.png)

*Cross-engine support to use any compute you want. As you can see in the image, you could use Snowflake or hook it up to Excel.*


Further, you are not vendor-locked inâyou can use different engines when needed or can change if you have to because of an organizational decision. By default, Starlake lets you specify your default engine for your entire project while also giving you the flexibility to override it on a per-model basis.


Let’s say you need the native warehouse engine in production for speed and security reasons, while leveraging DuckDB in the development environment or using Spark to process thousands of XML files in the test environment. Starlake is also **cross-engine capable**, enabling transformations that query one data warehouse and write results to another. This is especially useful for export tasks to formats like CSV, Parquet, or Excel, as well as for integrations with external analytical or operational databases.


### Deploy: From Development to Production


The last step is deploying your project. Maybe you run it locally with Docker and want to run it on Kubernetes or Starlake Cloud. For that, you can simply copy the configurations and be up to speed. That’s the beauty of being declarative.


### Visualize: Connecting to Your Analytics Stack


Visualization is usually not covered by a declarative data stack, but you can plug in any notebook, data apps, or business intelligence tools to use your created data marts or data artifacts.


Every data analytics project needs a visualization tool. Starlake leaves this open, so you could use any you want.


## Key Takeaways and What’s Next


So whether you’re a business user, data analyst, or data engineer, Starlake, with its declarative approach and low-code interface, makes it easy for everyone to create a sophisticated data platform with minimal configuration and all the bells and whistles included.


It allows efficient data transformation with the engine of your choice, supporting SQL and Python defined in YAML. It provides automatic handling of advanced write methodologies such as incremental and SCD2, built-in support for complex data types and error handling, and everything is version-controllable with simple YAML. Best of all, Starlake is fully open-source.


I believe the future is declarative data engineering, and Starlake can play a big part in this. Some also talk about the move [From Data Engineer to YAML Engineer](https://juhache.substack.com/p/from-data-engineer-to-yaml-engineer) and explain how declarative stacks free up engineers to focus on higher-value work.


In Part 3, we’ll discuss use cases such as transpiling SQL between dialects and data quality and validation with expectations in action. We’ll demonstrate the built-in, declarative security features and showcase DAG generation using templates that integrate with Airflow, Dagster, and Snowflake tasks out of the box, including column-level lineage support. We’ll also analyze how the end goal of moving toward English engineering through LLMs could lookâa road to self-service data platforms with a declarative backbone.


I hope you enjoyed this. Please let me know in the comments or write me if you have any feedback or experiences with declarative data stacks.


---


Want to get started with Starlake? Check out the [GitHub repo](https://github.com/starlake-ai/starlake/) or get started with a demo on [demo.starlake.ai](https://demo.starlake.ai/). Again, Starlake is fully open-sourceânot only its engine but also SQL transpilers and used toolsâbut you can also use its cloud hosting to get started immediately. If you use VS Code, check out [the extension](https://www.youtube.com/watch?v=8EL9-UiW6zs) for this too.


---


```
Full article published at Starlake.ai - written as part of my services
```

[Discuss on Bluesky](https://bsky.app/search?q=domain%3A%20https://www.ssp.sh/blog/beyond-basic-etl/)
|
[Declarative Data Stack](https://www.ssp.sh/tags/declarative-data-stack/)
[Starlake](https://www.ssp.sh/tags/starlake/)
[Orchestration](https://www.ssp.sh/tags/orchestration/)
[Yaml](https://www.ssp.sh/tags/yaml/)
[Orchestration](https://www.ssp.sh/tags/orchestration/)
[Data Governance](https://www.ssp.sh/tags/data-governance/)
[Services](https://www.ssp.sh/tags/services/)
