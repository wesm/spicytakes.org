---
title: "The Open Data Stack Distilled into Four Core Tools"
date: 2023-01-03
url: https://www.ssp.sh/blog/open-data-stack-core-tools/
slug: open-data-stack-core-tools
word_count: 2111
---

![The Open Data Stack Distilled into Four Core Tools](https://www.ssp.sh/blog/open-data-stack-core-tools/mds-core-stack.jpg)

Contents

In this article, we are going to explore core open-source tools that are needed for any company to become data-driven. We’ll cover integration, transformation, orchestration, analytics, and ML tools as a starter guide to the latest open data stack.


Let’s start with the Modern Data Stack. Have you heard of it or where the term came from? Here’s the definition from our [Data Glossary](https://glossary.airbyte.com/term/modern-data-stack/):


> The Modern Data Stack (MDS) is a heap of open-source tools to achieve end-to-end analytics from ingestion to [transformation](https://glossary.airbyte.com/term/data-transformation/) to ML over to a columnar data warehouse or lake solution with an analytics BI dashboard backend. This stack is extendable, like lego blocks. Usually, it consists of **data integration, a transformation tool, an [Orchestrator](https://glossary.airbyte.com/term/data-orchestrator/), and a [Business Intelligence Tool](https://glossary.airbyte.com/term/business-intelligence-tools/)**. With growing data, you might add [Data Quality](https://glossary.airbyte.com/term/data-quality/) and observability tools, [, [Semantic Layers](https://glossary.airbyte.com/term/semantic-layer/), and more.](https://glossary.airbyte.com/term/data-catalog/)


So what is the [Open Data Stack](https://www.ssp.sh/brain/open-data-stack/)? The Open Data Stack is a better term for the Modern Data Stack, but focusing on solutions built on open source and open standards covering the data engineering lifecycle. It still has the same goal as the Modern Data Stack, but tools integrate better due to the openness and, therefore, more usable data practitioners use them.


The word *open* is vital here and often overlooked. It means the tool or framework is either open source or complies to open standards. For example, [Dremio](https://www.dremio.com/), a data lakehouse platform, is closed source but based on open standards like [Apache Iceberg](https://glossary.airbyte.com/term/apache-iceberg) and [Apache Arrow](https://glossary.airbyte.com/term/apache-arrow), eliminating vendor lock-in for bigger organizations.

Disclaimer
The core tools I present here are my personal favorites. But since there are over 100 tools to choose from, I want to offer a beginner’s guide if you haven’t had an opportunity to study the field closely.

## The Open Data Stack


Before we introduce individual tools, let’s consider why you might want to use an open data stack—one that is maintained by everyone using it. With the open data stack, companies can reuse existing battle-tested solutions and build on top of them instead of having to reinvent the wheel by re-implementing key components from the [Data Engineering Lifecycle](https://glossary.airbyte.com/term/data-engineering-lifecycle) for each component of the data stack.


In the past, without these tools available, the story usually went something like this:

- **Extracting:** “Write some script to extract data from X.”
- **Visualizing:** “Let’s buy an all-in-one BI tool.”
- **Scheduling**: “Now we need a daily cron.”
- **Monitoring**: “Why didn’t we know the script broke?”
- **Configuration**: “We need to reuse this code but slightly differently.”
- **Incremental Sync**: “We only need the new data.”
- **Schema Change**: “Now we have to rewrite this.”
- **Adding new sources**: “OK, new script…”
- **Testing + Auth + Pagination**: “Why didn’t we know the script broke?”
- **Scaling**: “How do we scale up and down this workload?”


These scripts above were **written in** [**custom code**](https://airbyte.com/blog/etl-framework-vs-etl-script) dedicated to one company—sometimes one department only. Let’s find out how we profit from the open data stack to have a data stack up and running quickly to solve challenges such as those above.


**Excluded**

I am ignoring the rest of the lifecycle that comes with this scenario, such as security, deployment, maintenance, data management, and defining software engineering best practices. I’m also leaving storage out, as it is interchangeable with most of the standard [Storage Layers](https://glossary.airbyte.com/term/storage-layer-object-store/); I also wrote in-depth about them in the [Data Lake and Lakehouse Guide](https://airbyte.com/blog/data-lake-lakehouse-guide-powered-by-table-formats-delta-lake-iceberg-hudi).


## Integration with Airbyte


The first task is [Data Integration](https://airbyte.com/blog/data-integration). Integration is needed when your organization collects large amounts of data in various systems such as databases, CRM systems, application servers, and so on. Accessing and analyzing data that is spread across multiple systems can be a challenge. To address this challenge, data integration can be used to create a unified view of your organization’s data.


At a high level, data integration is the process of combining data from disparate source systems into a single unified view. This can be accomplished via manual integration, data virtualization, application integration, or by moving data from multiple sources into a unified destination.Â


[Airbyte](http://airbyte.com/) will likely be the number one choice for this job. Let me explain what Airbyte brings to the table with its premier offering: the first tool you should use in the data engineering lifecycle for data integration.


### Why Airbyte?


Airbyte unifies all your integration data pipelines and replicates your data pre-built and custom connectors. Some key features are reliability, extensibility, integrations, and transparency.


Airbyte offers a big **community** that updates connectors when source APIs and schemas change, allowing data teams to focus on insights and innovation instead of ETL. With **open source**, you can edit pre-built connectors and build new ones in [hours](https://docs.airbyte.com/connector-development/config-based/low-code-cdk-overview/). No more need for separate systems; Airbyte handles it all–database included–and **integrates** with most orchestrators.Â


The value comes from 300+ out-of-the-box connectors to address the **long tail** of connectors. All are open source, easily customizable, and support your language of choice (since connectors run as Docker containers). Options to schedule full-refresh, incremental, and log-based CDC replications across all your configured destinations save you time, and you can reduce sync times and overhead with state-of-the-art [Change Data Capture](https://airbyte.com/blog/change-data-capture-definition-methods-and-benefits) with [Debezium](https://debezium.io/) integration.


### How to get started with Airbyte


It’s super simple: you type two lines of code in your terminal and get an up-and-running Airbyte UI (more on [docs](https://docs.airbyte.com/quickstart/deploy-airbyte)):



| `1
2
` | `git clone https://github.com/airbytehq/airbyte.git
cd airbyte && docker-compose up
` |



![/blog/open-data-stack-core-tools/images/airbyte-ui.jpg](https://www.ssp.sh/blog/open-data-stack-core-tools/images/airbyte-ui.jpg)

*A freshly installed Airbye with its beautiful UI. You can also play around on theÂdemo instance.*


## Data Transformation (SQL) with dbt


The next step is [data transformation](https://glossary.airbyte.com/term/data-transformation). Data transformation is the process of converting data from one format to another. Reasons for doing this could be to optimize the data for a different use case than it was originally intended or to meet the requirements for storing data in a different system. Data transformation may involve steps such as cleansing, normalizing, [structuring](https://glossary.airbyte.com/term/structured-data), validation, sorting, joining, or [enriching](https://glossary.airbyte.com/term/data-enrichment) data. In essence, the key business logic is saved in the transformation layer.


Let’s explore why the number one choice and the **king of** [**SQL**](https://glossary.airbyte.com/term/sql) is [dbt](https://www.getdbt.com/).


### Why dbt?


Every data project starts with some SQL queries. The default should be to use dbt, which immediately forces you to use the best software engineering practices and added features that SQL does not support. Essential elements are documentation generation, reusability of the different SQL statements, testing, source code versioning, added functionality to plain SQL with [Jinja Templates,](https://glossary.airbyte.com/term/jinja-template) and (newly added) even [Python](https://glossary.airbyte.com/term/python) support.


dbt avoids writing boilerplate [DML](https://docs.getdbt.com/terms/dml) and [DDL](https://docs.getdbt.com/terms/ddl) by managing transactions, dropping tables, and managing schema changes. Write **business logic** with just a SQL select statement or a Python DataFrame that returns the dataset you need, and dbt takes care of [materialization](https://docs.getdbt.com/terms/materialization).


dbt produces valuable metadata to find long-running queries and has built-in support for standard transformation models such as full or incremental load.


### How to get started with dbt


dbt is a command line interface (CLI) tool that needs to be installed first. Choose your [preferred way](https://docs.getdbt.com/docs/get-started/installation) of installation. To initialize, you can run the command to set up an empty project: `dbt init my-open-data-stack-project`.


Next, you can start setting up your SQL statement into [macros](https://docs.getdbt.com/docs/build/jinja-macros) and [models](https://docs.getdbt.com/docs/build/sql-models), where the macros are your SQL statements with extended Jinja macros and the models are your physical elements you want to have in your destination defined as a table view (see image below; you can specify this in `dbt_project.yml`).


![/blog/open-data-stack-core-tools/images/dbt-cli.jpg](https://www.ssp.sh/blog/open-data-stack-core-tools/images/dbt-cli.jpg)

*An example of dbt CLI in action when generating the tables and views withdbt run*

Reference to Project
You can find the above-illustrated project with different components (e.g., macros, models, profiles…) at our open-data-stack project underÂ
[transformation_dbt](https://github.com/airbytehq/open-data-stack/tree/main/transformation_dbt)
 on GitHub.

There is so much more that makes dbt so powerful. Please follow up on the [dbt developer hub](https://docs.getdbt.com/) and play around with the [open-data-stack project](https://github.com/airbytehq/open-data-stack/tree/main/transformation_dbt).


## Analytics and Data Visualization (SQL) with Metabase


When data is extracted and transformed, it’s time to visualize and get the value from all your hard work. Visuals are done through [Analytics](https://glossary.airbyte.com/term/analytics) and [Business Intelligence](https://glossary.airbyte.com/term/business-intelligence) and one of their [Tools](https://glossary.airbyte.com/term/business-intelligence-tools). The BI tool might be the most crucial tool for data engineers, as it’s the visualization everyone sees–and has an opinion on!


Analytics is the systematic computational analysis of data and statistics. It is used to discover, interpret, and communicate meaningful patterns in data. It also entails applying data patterns toward effective **decision-making**.

Which BI tool
In this category, I like pretty much all the available tools. If you implement strongÂ
[data engineering fundamentals](https://glossary.airbyte.com/term/data-engineering)
 andÂ
[data modeling](https://glossary.airbyte.com/term/data-modeling)
, you choose the BI tool,Â
[notebook](https://glossary.airbyte.com/term/notebooks)
, and build your data app. It’s amazing how many BI tools get built almost daily, withÂ
[Rill Data](https://www.rilldata.com/)
 being an interesting one to look out for.

### Why Metabase?


Out of the many choices available, I chose [Metabase](https://www.metabase.com/) for its simplicity and ease of setup for non-engineers.


Metabase lets you ask questions about your data and displays answers in formats that make sense, whether a bar chart or a detailed table. You can save your questions and group questions into friendly dashboards. Metabase also simplifies sharing dashboards across teams and enables self-serving to a certain extent.


### How to get started with Metabase


To start, you must download the metabase.jar [here](https://www.metabase.com/start/oss/jar). When done, you simply run:



| `1
` | `java -jar metabase.jar
` |



![/blog/open-data-stack-core-tools/images/metabase-example.jpg](https://www.ssp.sh/blog/open-data-stack-core-tools/images/metabase-example.jpg)

*Example Dashboard in Metabase*


Now you can start connecting your data sources and creating dashboards.


## Data Orchestration (Python) with Dagster


The last core data stack tool is the [orchestrator](https://glossary.airbyte.com/term/data-orchestrator). It’s used quickly as a data orchestrator to model dependencies between tasks in complex heterogeneous cloud environments end-to-end. It is integrated with above-mentioned open data stack tools. They are especially effective if you have some glue code that needs to be run on a certain cadence, triggered by an event, or if you run an ML model on top of your data.


Another crucial part of the orchestration is applying [Functional Data Engineering](https://glossary.airbyte.com/term/functional-data-engineering). The functional approach brings clarity to “pure” functions and removes side effects. They can be written, tested, reasoned about, and debugged in isolation without understanding the external context or history of events surrounding their execution. As data pipelines quickly grow in complexity and data teams grow in numbers, using methodologies that provide clarity isn’t a luxury–it’s a necessity.


### Why Dagster?


[Dagster](http://dagster.io/) is a framework that forces me to write functional Python code. Like dbt, it enforces best practices such as writing declarative, abstracted, idempotent, and type-checked functions to catch errors early. Dagster also includes simple unit testing and handy features to make pipelines solid, testable, and maintainable. It also has a deep integration with Airbyte, allowing [data integration as code](https://airbyte.com/tutorials/configure-airbyte-with-python-dagster). Read more on the latest [data orchestration trends](https://airbyte.com/blog/data-orchestration-trends).


### How to get started with Dagster


To get started easily, you can scaffold an example project `assets_modern_data_stack` which includes a data pipeline with Airbyte, dbt and some ML code in Python.



| `1
2
3
` | `pip install dagster dagit && dagster project from-example --name open-data-stack-project --example assets_modern_data_stack
cd open-data-stack-project && pip install -e ".[dev]"
dagit
` |



![/blog/open-data-stack-core-tools/images/dagster-ui.jpg](https://www.ssp.sh/blog/open-data-stack-core-tools/images/dagster-ui.jpg)

*Example open-data-stack pipeline in Dagster when running above three lines of code*


## Additional Components of the Open Data Stack


The tools I’ve mentioned so far represent what I would call the core of the open data stack if you want to work with data end to end. The beauty of the data stack is that you can now add specific use cases with other tools and frameworks. I’m adding some here for inspiration:

- [Semantic Layer / Metric Layer](https://www.ssp.sh/blog/rise-of-semantic-layer-metrics/)
- [Data Quality and Data Observability](https://airbyte.com/blog/data-quality-issues)
- [Reverse ETL](https://airbyte.com/blog/reverse-etl)
- [Data Catalogs](https://glossary.airbyte.com/term/data-catalog)
- And many more


### What’s Next?


So far, we’ve reviewed the difference between the modern data stack and the open data stack. We’ve discussed its superpower and why you’d want to use it. We also discussed core open-source tools as part of the available data stack.Â


To see these four core tools in action, read our tutorial on [Configure Airbyte Connections with Python (Dagster)](https://airbyte.com/tutorials/configure-airbyte-with-python-dagster), which scrapes GitHub repositories and integrates with Airbyte, creates SQL views with dbt, orchestrates with Dagster, and visualizes a dashboard Metabase.


We *didn’t* discuss **enterprise data platforms** or so-called **no-code solutions**. The next blog post discusses [The Struggle of Enterprise Adoption](https://www.ssp.sh/blog/modern-data-stack-struggle-of-enterprise-adoption/) with the open data stack. Particular focus will center on mid- and large-sized enterprises that want to adapt to the new data stack.


---


```
Originally published at Airbyte.com
```

[Discuss on Bluesky](https://bsky.app/search?q=domain%3A%20https://www.ssp.sh/blog/open-data-stack-core-tools/)
|
[Pay what you like](https://ko-fi.com/sspaeti)
|
[Open Data Stack](https://www.ssp.sh/tags/open-data-stack/)
[Modern Data Stack](https://www.ssp.sh/tags/modern-data-stack/)
