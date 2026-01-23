---
title: "Building an Analytics API with GraphQL: The Next Level of Data Engineering?01-22"
date: 2022-01-22
url: https://www.ssp.sh/blog/analytics-api-with-graphql-the-next-level-of-data-engineering/
slug: analytics-api-with-graphql-the-next-level-of-data-engineering
word_count: 3671
---

![Building an Analytics API with GraphQL: The Next Level of Data Engineering?](https://www.ssp.sh/blog/analytics-api-with-graphql-the-next-level-of-data-engineering/header_pyramid_stairs.jpeg)

Contents
Image by
[Mohammad Bagher Adib Behrooz](https://unsplash.com/@adibbehrooz)
on
[Unsplash](https://unsplash.com/photos/XHI-S_xWK28)

Why GraphQL for data engineers, you might ask? GraphQL solved the problem of providing a distinct interface for each client by unifying it to a single API for all clients such as web, mobile, web apps. The same challenge we’re now facing in the data world, where we integrate multiple clients with numerous backend systems.


So what is GraphQL? In the world of microservices and web apps, GraphQL is a popular query language and serves as a data layer. It is essentially SQL on steroids for APIs. In this article, we go through how to combine the data from all services into a single, unified API.


## Why GraphQL for Data Engineers?


### What is GraphQL?


Let’s start with GraphQL. It was developed internally by Facebook in 2012 before being publicly released in 2015. Essentially to serve their mobile app better, all APIs were optimised for the web with bigger clients and faster data connections. Instead of duplicating all their existing API endpoints for mobile, they soon figured they required another solution. And this solution was called GraphQL. If you want to know more about how it started, I recommend watching the Netflix-like [documentary](https://youtu.be/783ccP__No8).


**Essentially, GraphQL is SQL on steroids for APIs**. The best part, it is based on the same technology as REST with GET or POST requests. But instead of having multiple *dumb* endpoints, you have a single *intelligent* endpoint that can take in complex queries. Assume you have hundreds of API endpoints for all your use cases. GraphQL lets you combine them but selects only columns (`SELECT columns FROM ...`) and rows (`WHERE ...`) you need. These options lead to fewer API calls and less data load as you can combine several REST calls into one. That also empowers frontend developers as they depend less on backend developers.


### The (query) interface


Below illustrates how a simple query looks with GitHub [public GraphQL endpoint](https://docs.github.com/en/graphql/overview/explorer). You can try the below query yourself.



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
` | `query {
  repository(owner: "ssp-data", name: "practical-data-engineering") {
    name
    description
    owner {
      login
    }
    homepageUrl
    visibility
    createdAt
  }
}
` |



The response looks like this:



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
` | `{
  "data": {
    "repository": {
      "name": "practical-data-engineering",
      "description": "Real estate dagster pipeline",
      "owner": {
        "login": "ssp-data"
      },
      "homepageUrl": "https://www.sspaeti.com/blog/data-engineering-project-in-twenty-minutes/",
      "visibility": "PUBLIC",
      "createdAt": "2020-11-18T21:15:37Z"
    }
  }
}
` |



### Why is GraphQL such a great fit?


Most discussions of GraphQL focus on data fetching, but any **complete data platform needs a way to modify server-side data** as well. That’s where built-in `mutation`’s come into play, and we use them to our advantage in the Analytics API later on. Find more information under [Queries and Mutations](https://graphql.org/learn/queries/).


Maintenance is simple. Instead of adding complexity by creating more endpoints, GraphQL essentially is one single endpoint `/graphql` (can be named as you want). It also adds to its **extendability and maintainability**.


**Type validations** built-in with the [GraphQL schema language](https://graphql.org/learn/schema/) to prevalidate GraphQL queries. These allow the servers and clients to effectively inform developers when there is an invalid query **without relying on runtime checks**.


**Self-documented!** As you build your interface with columns and types, you document the code, which becomes automatically available to the client through introspection with tools like GraphQL. **That is a huge time saver for the developers building the API and those using it**.


A big one is your **API schema decouples from your database schemas**. For example, you use [AWS Lambda](https://aws.amazon.com/lambda/) functions today to query [Google Big Query](https://cloud.google.com/bigquery) in your backend, and you want or must change to something else such as [Apache Druid](https://www.ssp.sh/blog/open-source-data-warehousing-druid-airflow-superset/#druid---the-data-store). You can switch that without interfering with the users as GraphQL acts as your semantic layer. Imagine the contrary where you tightly integrated your web app with the API of Big Query. It would take a lot of effort to migrate and rewrite all the frontend code.


💡 Good to know: Besides query and mutation, the operation **`subscription` is handy to update downstream events and prevent polling**. The server will push the changes to all the subscribers. It’s convenient for event-based or real-time applications. Subscriptions themselves can be `update`, `delete` or `insert` that GraphQL uses [Websockets](https://en.wikipedia.org/wiki/WebSocket) to keep an open connection between server and client.


Another winning aspect is the **standardised specification form. At any rate, being a specification means great tooling, easier usage**, and more comprehensive interoperability among services are all much simpler to achieve. I think that alone makes GraphQL hard to avoid.


### What GraphQL is not


It’s not a full-blown solution that provides you with all the necessary services. It is one part of a framework that delivers the proper boundaries and tools to implement the suitable logic for your business that you would otherwise have to build anyway. But without the hassle of creating your query interface, permissions, validations, etc. and glue everything together.


It is not [YAML](https://blog.stackpath.com/yaml/), not JSON, very close though, but it is its format as seen above in the [interface part](https://www.ssp.sh/blog/graphql-the-next-level-of-data-engineering/#the-query-interface)). You find other potential problems in the article [REST vs GraphQL APIs, the Good, the Bad, and the Ugly](https://www.moesif.com/blog/technical/graphql/REST-vs-GraphQL-APIs-the-good-the-bad-the-ugly/#problems-with-graphql).


## What is an Analytics API?


Now, as we’ve seen what GraphQL can do, we talk about **building an API that leads to the next level of data engineering,** which I call *Analytics API* in this article. The API will empower all stakeholders to use **one single source of accessing analytics data** in a consistent and decoupled semantic way (and if you know a better name, please let me know!).


![/blog/analytics-api-with-graphql-the-next-level-of-data-engineering/graphql-data-api-data-engineering.jpg](https://www.ssp.sh/blog/analytics-api-with-graphql-the-next-level-of-data-engineering/graphql-data-api-data-engineering.jpg)

*The Analytics API architecture with the single endpoint with GraphQL | Image by the Author*


The Analytics API consists of five main components where GraphQL is the natural fit for the gateway API and the query interface. Besides that, the SQL Connector connects legacy or traditional BI systems that talk SQL natively. The metrics or business logic, also called [Metrics Store](https://cube.dev/blog/introducing-cube-sql/) or [Headless BI](https://basecase.vc/blog/headless-bi) stored in a Metrics Store. Suppose you’re in a large organisation with a lot of variety. In that case, it’s helpful to have a data catalog that helps discover your data and add owners, comments, ratings and others to the datasets to navigate between them. The orchestrator updates your content in the data stores consistently and reliably. More about each component a bit later.


## How data teams struggle to build an Analytics API


Cloud architecture is more complex than ever, especially with the latest explosion of tools and technology. Today every data team want data to be readily available to decision-makers in the company. Whether a Data Analyst, Product Manager, Data Scientist, Business or Data Analyst approaches them, it’s hard to provide a single interface to abstract all heterogeneous data stores away and let them query all the data. On top of that, new principles and architecture are picking up old ideas, for example, decentralised data products in [Data Mesh](https://cnr.sh/essays/what-the-heck-data-mesh) and a centralised cloud data warehouse.


[Xavier Gumara Rigol from Adevinta](https://medium.com/adevinta-tech-blog/building-a-data-mesh-to-support-an-ecosystem-of-data-products-at-adevinta-4c057d06824d) says that each dataset should have at least two interfaces with **SQL as fast access and programmatic access via notebooks** if more complex processing is needed.


On the other hand, if you have a single Postgres database or any other simplified architecture, it probably doesn’t make sense to build and route it through an Analytics API. Let’s have a look at different data teams nowadays and with what they struggle today:

- **Machine Learning folks** want an API to experiment with particular data within a Jupyter Notebook.
- **Business Intelligence users** need to report how the company is doing with their dashboard tool of choice. They need a SQL Connector. Response time must be within seconds as they want to slice and dice in real-time and demo the numbers in meetings. If possible company-wide KPI’s are already precalculated and ready to use.
- **Power-users** want to update and fix some incorrect data. They need an interface or clear documentation of how to do that. And more importantly, whether they are doing it on a data lake, an [OLAP](https://www.ssp.sh/blog/olap-whats-coming-next/) cube, configs, etc., shouldn’t matter.
- **Internal applications and pipelines** that apply the product logic with different requirements include ingesting new data, fixing invalidate states, automatic maintenance such as compacting massive data sources or implementing complex business logic.
- **External customers** want to extract data for their data warehouse.
- **Managers** want to see the overall numbers at a glance.


As these stakeholders have different use-cases and skills, it is tough to support them all. With a standardised GraphQL interface validated on the spot and documented build-in, we have the best approach today. It is also a chance to **make updates consistent and save**, instead of getting direct access to people 🚒.


**Authorisation and authentication** are noteworthy instead of creating new groups and users in every system. It’s essential to implement that once. But that is very hard if you do not have such an API. Of course, you could integrate your identity and access management solution, but baked-in in the central API and with GraphQL is a pragmatic and elegant way.


## Components of an Analytics API


Let’s now look into each component in more detail and what they effectively do.


### API and Query Engine


The first component of the Analytics API is the interface and Query Engine. This interface is the single GraphQL endpoint that all tools access. Call it a proxy, router or gateway, which forwards every `query`, `mutation` or `subscription` to the correct service or pipeline.


The query engine helps if you have central calculated measures or any data stores that do not speak SQL, you translate the GraphQL query to that specific query language. A critical separation from the SQL Connector uses advanced and more general patterns to query data. E.g. instead of `SELECT COUNT(DISTINCT userid) AS distinct_users FROM customers` we would be more generalised with:



| `1
2
3
` | `SELECT {{ metrics.distinct_users }} FROM {{ datasources.customers }}
--or
SELECT * FROM {{ metrics.metric('customer', by='day', dims=['country', 'year']) }}
` |



For that, we need an intermediate layer to translate the generic query to an actual SQL-Query, the Query Engine.


I hope you notice the benefits and the **small [revolution](https://www.linkedin.com/feed/update/urn:li:activity:6885632330640171008/) for all business intelligence engineers here. We have one definition instead of writing long and complex queries for all data stores with slightly different syntax**. And rather than defining the metrics such as `distinctUsers` in various places, we store it once and apply it to all systems. No need to worry if you got the latest version or if anyone changed the calculation. More on how you store one metric definition centrally in the next chapter.


> We're seeing more abstractions emerging in the transform layer. The metrics layer (popularised by [Airbnb's Minerva](https://medium.com/airbnb-engineering/how-airbnb-achieved-metric-consistency-at-scale-f23cc53dea70), [Transform.co](https://transform.co/), and [Metriql](https://metriql.com/)), feature engineering frameworks (closer to MLops), A/B testing frameworks, and a cambrian explosion of homegrown computation frameworks of all shapes and flavours. Call this "data middleware", "parametric pipelining" or "computation framework", but this area is starting to take shape. From [How the Modern Data Stack is Reshaping Data Engineering](https://preset.io/blog/reshaping-data-engineering/)


As seen on the Analytics API image above, it integrates through GraphQL with the other components to either read data from the metrics and data catalog store or trigger an update through the orchestration. There is no integral tool besides the Headless BI tools, which implements only certain parts. In [The Recent Hype Around Headless BI](https://www.ssp.sh/blog/graphql-the-next-level-of-data-engineering/#the-recent-hype-around-headless-bi) chapter, you can find more about them.


### Metrics Store | Headless BI


The Headless BI part, or Metrics Store as I refer to in this article, is the essential place for all your [metrics](https://support.google.com/analytics/answer/1033861?hl=en). Metrics such as calculated measures, dimensions, etc., that you typically know from your business intelligence tools such as Tableau, Power BI, Superset, Looker. **These tools all have their metric store and, most times, their language to describe aggregated calculations or dimensions**. Most famous here is [LookML](https://docs.looker.com/data-modeling/learning-lookml/what-is-lookml) from Looker. The difference here is that we separate that part of all BI tools and centralise them. It allows us to define them once in a structured and source controlled way instead of inside a proprietary tool.


> **See it as certain business logic, critical code or metadata implemented once centrally following the [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) principles**. Let's say you use Apache Druid, and you might have complex calculated measures, which you'd like to query with BI tools, as an ML-Engineer or any customer. Instead of recreating them adding formatting options, units, descriptions in each tool, you store them central in the Analytics API. Also, with the help of the metrics store.


The communication between the different components within the Analytics API is returning the queries from the Query Engine via GraphQL, querying or updating the metadata store and data API configs when needed via direct query and executing requests from the orchestration.


Currently, most tools and people use the **popular templating solution with [Jinja and SQL](https://multithreaded.stitchfix.com/blog/2017/07/06/one-weird-trick/)** and integrate them in the chosen BI tool of the company. But as the Jinja SQL logic is hard to re-use across different database engines and gets messy quickly if you start nesting these queries, metrics stores become popular.


As you can understand by now, the Metrics Store is one big part of an Analytics API, and the critical component as analytics queries and the metrics are almost synonyms. Also, with **the growing popularity of Analytics Engineers, their domain knowledge mainly defines and creates the transformation of such metrics**.


On top of it, I would see **additional services integrated similar to the [Confluent Schema Registry](https://docs.confluent.io/platform/current/schema-registry/index.html) for Kafka**, such as comparing different versions of metrics definition and schemas of data stores. These will reduce errors to integrate your data pipelines and application logic with the ever-evolving schema of tables and views in your data stores. And allows features with adding new metrics and dimensions consistently.


#### The Recent Hype Around Headless BI


If you follow the data space, you have noticed the **hype around metadata with terms called the Metrics Store or Headless BI. Interesting open-source and closed-source companies and tools starting around it include [Cube.js](https://cube.dev/blog/introducing-cube-sql/), [Metriql](https://metriql.com/), [Supergrain](https://www.supergrain.com/), [Transform.co](https://transform.co/) or the [Minerva API](https://medium.com/airbnb-engineering/how-airbnb-enables-consistent-data-consumption-at-scale-1c0b6a8b9206) by AirBnB**. You’ll also see that they are using or beginning to use GraphQL for many reasons mentioned.


The latest announcement happened at the keynote of [dbt’s](https://www.getdbt.com/) public conference [Coalesce](https://coalesce.getdbt.com/) from [Drew Banin](https://twitter.com/drewbanin) about the “[The Metric System](https://youtu.be/MdSMSbQxnO0)”. He talks about where we came from with measurement 5000 years ago and is a must-watch if you haven’t seen it already. If you want to know more details, follow the started [Github Issue](https://github.com/dbt-labs/dbt-core/issues/4071) with many information and exciting thoughts.


### Data Catalog


Data increased 40x over the last ten years according to the United Nations Economic Commission for Europe (UNECE) in 2003 (much higher today). It’s hard to keep this amount organised over time. A data [Data Catalog Service](https://www.ssp.sh/blog/business-intelligence-meets-data-engineering/#8220use-data-catalogs-to-have-a-central-metadata-store8221) solves the problem of handling the fast-growing data.


The solution doesn’t lie in the data but instead in keeping track of metadata and presenting them efficiently. Data Catalog and Discovery tools like [Amundsen](https://amundsen.io/) achieve that by showing us what data sets are available and which years who created it, metadata of how many rows, min/max entries. It incorporates a rating system where users can give feedback about a data set to give you a feeling for the data quality and how valid it is to use that data set. **It is Google Search but for metadata with a handy interface for your metrics store**.


Depending on which tool you choose or build, you interface with the metrics store and other components such as orchestrator or web apps. Optimal solution if that component has a GraphQL interface itself. The user will use the web interface of such a tool, and other parts of the Analytics API will become the programmable interface through GraphQL and REST. For example, the orchestration tool will query the latest db-schema or a list of lasted data sources.


### Orchestration


The orchestration part is where most of the business logic and transformation land at the end. **Instead of building everything into the Query Engine directly on GraphQL, it’s better to use a proper tool to re-use code and integrate it better**.


I see [Dagster](http://dagster.io) as the modern business rule engine where you express the logic in python code, which makes it testable and scalable compared to [no-code/less-code approaches](https://www.linkedin.com/feed/update/urn:li:activity:6857348322504540160/). Dagster offers tons of tools such as [resources](https://docs.dagster.io/concepts/resources) to capture the re-usable code, such as connecting to Druid, creating a delta table, and starting a spark job, all of which are used in the pipelines. Another building block in the Analytics API is an [Op](https://docs.dagster.io/concepts/ops-jobs-graphs/ops#ops), which condenses your business logic as functional tasks within a [data pipeline](https://docs.dagster.io/concepts/ops-jobs-graphs/jobs-graphs). It is well defined with typed inputs and outputs and uses context such as the above resources, making it easy to run a spark job as part of an op.


The integrations within the Analytics API is with GraphQL as Dagster has one built-in. Dagster uses this interface to query all sorts of metadata, start pipelines/sensors (mutation), or subscribe to specific info. Side-note: This does not come out of thin air, as the founder of Dagster [Nick Schrock](https://twitter.com/schrockn) is the Co-Founder of GraphQL 😉. Instead of running and using the [Dagster UI](https://docs.dagster.io/concepts/dagit/dagit), we use that interface for developers and abstract it away with the Analytics API.


### SQL Connector


**SQL is the data language besides python, as elaborated in earlier [articles](https://www.ssp.sh/blog/business-intelligence-meets-data-engineering/#8220use-notebooks-to-open-up-the-data-silos8221). That’s why we need to provide an interface for that as well.** The SQL Connector integrates all BI, SQL speaking or legacy tools. For example, the connector mainly implements an ODBC or JDBC driver with Avatica built on [Apache Calcite](https://calcite.apache.org/avatica) used by Apache Druid. With that, have a way to interface with ANSI SQL, including all our metrics and dimensions in the metrics store with no additional effort on the accessing side if the tools talk SQL.


## Challenges of building an Analytics API


While writing this article, I often found myself in conflict with existing architecture and existing tools. This chapter is not meant to be complete in any way. It indicates the challenge of building such a central interface and lets us learn from their advantages and disadvantages.

- **Microservices with OpenAPI Specification:** With the easiness of deploying apps, we get lots of bi-directional communication between the different APIs and services. With [OpenAPI Specification (earlier known as Swagger)](https://swagger.io/specification/), you can use tools to generate the documentation, client code, and testing.
- **[ROAPI](https://github.com/roapi/roapi)**: Another fascinating one, it automatically spins up read-only APIs for static datasets without requiring you to write a single line of code. It builds on top of [Apache Arrow](https://arrow.apache.org/) and [Datafusion](https://github.com/apache/arrow-datafusion).
- **Cloud Data Warehouse approach:** Kind of a monolithic architecture if you use one primary cloud data warehouse. It gives you a single API, and you access the data with plain SQL. It has the known disadvantages of tightly integrating into your web app.
- **[No Code / Less Code Platforms](https://www.linkedin.com/feed/update/urn:li:activity:6857348322504540160/)**: Same goes for when you buy into one [Closed-Source Vendor Platform](https://www.ssp.sh/blog/business-intelligence-meets-data-engineering/#8220use-closed-source-if-you-dont-have-the-developers-or-the-time8221) such as [Ascend.io](https://www.ascend.io/) or similar.
- **[Lakehouse Architecture](http://cidrdb.org/cidr2021/papers/cidr2021_paper17.pdf) by Databricks:** The Lakehouse shows that everything is heading to more minor moving parts with consolidating the data interfaces to a bare minimum or one single interface. The CEO Ali Ghodsi said recently: “Despite how far we came with all data tools and frameworks, people are still running around and matching up correct numbers, and fighting who’s once are correct”. It indicates that the Metrics Store and central Analytics API are needed.
- **[Data Virtualisation](https://www.ssp.sh/blog/olap-whats-coming-next/#data-virtualisations)**: Another way to centralise and connect all moving parts is with Data Virtualisation. **You don’t move and copy data around and pre-aggregate**, but you have a semantic middle layer to create your business models (like cubes). These tools, e.g. [Dremio](https://www.dremio.com/) or [others](https://www.ssp.sh/blog/olap-whats-coming-next/#data-virtualisations), use Apache Arrow technology, which will cache and optimise a lot in-memory for you to have fast response times.


![/blog/analytics-api-with-graphql-the-next-level-of-data-engineering/apache-arrow.png](https://www.ssp.sh/blog/analytics-api-with-graphql-the-next-level-of-data-engineering/apache-arrow.png)

*How Apache Arrow works here is demonstrated byJulien Le Dem,Spark Summit*

- **Serverless Functions:** Less an architecture, but for smaller objectives, you could use serverless functions (without an infrastructure) to run your glue code, for example, in [AWS Lambda](https://aws.amazon.com/lambda/), to mention one. Your function can react to events that support highly event-driven use-cases.
- [Data Warehouse Automation](https://www.ssp.sh/blog/data-warehouse-automation-dwa/)**: Another way of solving it is to invest in automation. Instead of buying your data warehouse, you could build it with tools such [TimeXTener, WhereScape, BiGenius](https://www.ssp.sh/blog/what-dwa-tools-are-on-the-market/) and [many more](https://dwa.guide/dwa-tools/). Instead of integrating all with a single interface, you’d work agile and integrate all into your data warehouse. More about that


## Conclusion


As we have seen, GraphQL is a powerful tool for data engineering and building an Analytics API. We learnt what an Analytics API is for and how data teams struggle to develop one for today complex cloud architectures, primarily to serve various stakeholders and other business departments. The components of an Analytics API with the Query Engine, Metrics Store, a Data Catalog, an orchestration tool and a SQL connector. And at the end, we looked at other solutions and challenges, in general, we have today.


This article means not to be the silver bullet solution in any way. Much more, I hope it helps you develop the best solution for your own. I’m sure there will be a lot going on in the next couple of months and years in this specific topic, and I’m looking forward to seeing the ecosystem around Analytics API and GraphQL involved. I’m also interested in the naming for such solutions as *Analytics API* is not yet the final name, in my opinion.


That’s it for now. I’m looking forward to your suggestions and critics. Let me know how you solved the problem of building an Analytics API and your thoughts on this one?


---


```
Republished on Towards Data Science
```

[Discuss on Bluesky](https://bsky.app/search?q=domain%3A%20https://www.ssp.sh/blog/analytics-api-with-graphql-the-next-level-of-data-engineering/)
|
[Pay what you like](https://ko-fi.com/sspaeti)
|
[Analytics Api](https://www.ssp.sh/tags/analytics-api/)
[Data Architecture](https://www.ssp.sh/tags/data-architecture/)
[Headless Bi](https://www.ssp.sh/tags/headless-bi/)
[Metricsstore](https://www.ssp.sh/tags/metricsstore/)
[Graphql](https://www.ssp.sh/tags/graphql/)
