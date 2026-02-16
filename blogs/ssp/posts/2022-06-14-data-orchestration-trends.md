---
title: "Data Orchestration Trends: The Shift From Data Pipelines to Data Products"
date: 2022-06-14
url: https://www.ssp.sh/blog/data-orchestration-trends/
slug: data-orchestration-trends
word_count: 3560
---

![Data Orchestration Trends: The Shift From Data Pipelines to Data Products](https://www.ssp.sh/blog/data-orchestration-trends/featured-image.jpg)

Contents

Data consumers, such as data analysts, and business users, care mostly about the production of data assets. On the other hand, data engineers have historically focused on modeling the dependencies between tasks (instead of data assets) with an orchestrator tool. How can we reconcile both worlds?


This article reviews open-source data orchestration tools (Airflow, Prefect, Dagster) and discusses how data orchestration tools introduce data assets as first-class objects. We also cover why a declarative approach with higher-level abstractions helps with faster developer cycles, stability, and a better understanding of whatâs going on pre-runtime. We explore five different abstractions (jobs, tasks, resources, triggers, and data products) and see if it all helps to build a Data Mesh.


## What Is a Data Orchestrator?


A Data OrchestratorÂ **models dependencies between different tasks in**Â [**heterogeneous environments**](https://mattturck.com/data2021/)Â **end-to-end**. It handles integrations with legacy systems, cloud-based tools,Â [data lakes](https://airbyte.com/glossary/data-lake), andÂ [data warehouses](https://airbyte.com/glossary/data-warehouse). ItÂ **invokes**Â [**computation**](https://en.wikipedia.org/wiki/Orchestration_%28computing%29), such as wrangling your business logic in SQL and Python and applying ML modelsÂ **at the right time based on a time-based trigger or by custom-defined logic**.


WhatÂ **makes an orchestrator an expert**Â is that it lets you findÂ *when*Â things are happening (monitoring with lots of metadata),Â *what*Â is going wrong andÂ *how*Â to fix the wrong state with integrated features such as backfills.


When discussing complex open-source cloud environments, itâsÂ **crucial to integrate**Â and orchestrate various tools from theÂ [Modern Data Stack (MDS)](https://airbyte.com/glossary/modern-data-stack)Â andÂ **automate**Â them as much as possible as companies grow their need for orchestration. With ELT getting more popular, data orchestration is less about data integration but more aboutÂ [wrangling data](https://en.wikipedia.org/wiki/Data_wrangling)with assuring quality and usefulness. Previously, it was common among data engineers to implement allÂ [ETL parts in the orchestrator, typically with Airflow](https://airbyte.com/blog/airflow-etl-pipelines). On top, monitoring, troubleshooting, and maintenance become more apparent, and the needÂ **for a**Â [**Directed Acyclic Graph (DAG)**](http://www.airbyte.com/glossary/dag-directed-acyclic-graph)Â **of all your tasks arises. DAGs allow us to describe more complex workflows safely**.


In the end, an orchestratorÂ **must activate Business Intelligence, Analytics, and Machine Learning**. These are company-accessible dashboards/reports, machine learning models, or self-serve BI environments where users can create and pull their data. It is also where the shift happens from data pipelines to what the user is interested in, the Data Asset or Data Product, to use the jargon ofÂ [Data Mesh](http://www.airbyte.com/glossary/data-mesh).

Orchestration synonym for data orchestration
I will use orchestration as a synonym for data orchestration, as all we talk about in this article is data. As well, I useÂ
[Data Assets](http://www.airbyte.com/glossary/data-asset)
Â interchangeably withÂ
[Data Products](http://www.airbyte.com/glossary/data-product)
.

## Alternatives to Data Orchestration


By now, we have a pretty good understanding of data orchestration. Letâs discussÂ **the main alternative to data orchestration. Itâs called choreography,**Â and as opposed to orchestration, it does not take care of the whole process. Instead, it sends and communicates events to a specific message storage. Choreography is similar to a microservice, where each application only knows how to do its core function.


As always, both have their advantages and disadvantages. For example, inÂ **the orchestration part, you have a unified view-the control plane**-where choreography is loosely coupled, and the shared-nothing pipelines can be very hard to manage. On the other hand,Â **a choreographic architecture is easier to scale**, althoughÂ [Kubernetes](http://www.airbyte.com/glossary/kubernetes)Â can also help to scale the orchestration part.


## The Shift From a Data Pipeline to a Data Product


In the era of big data, we have managed to compute massive amounts of data with high-scale computation and storage and efficiently query data sets of arbitrarily large size. But as a side effect, data teams are growing fast, and so do new data sources daily, creating more complex data environments. Although each data project starts simple, below is an example illustrating a typical data architecture among data engineers.


![/blog/data-orchestration-trends/data-orchestration_typical-cloud-data-project.png](https://www.ssp.sh/blog/data-orchestration-trends/data-orchestration_typical-cloud-data-project.png)

*An example of a typical cloud data project that needs data orchestration*


The questions are not anymore how we can transform data overnight or create a DAG with a modern data orchestrator, but how we get an overview of all data crunched and stored. How do we do that shift?


There are several trends to support this:

- Think aboutÂ **data as a product**Â withÂ **data-aware**Â pipelines that know about the inner life of a task
- Shift toÂ **declarative**Â pipeline orchestration
- UseÂ **abstractions**Â to reuse code between complex cloud environments
- Make Python a first-class citizen with aÂ [functional data engineering](http://airbyte.com/glossary/functional-data-engineering)Â approach andÂ [idempotent](https://airbyte.com/glossary/idempotency)Â functions.


Applying this will help you get the Data Product Graph view we are all longing for. Letâs have a look at each of these trends.


### Data Products Are the Output of Modern Orchestration


One solution to achieve the shift is to focus on the data assets and products with excellent tooling byÂ [fading the technology layer to the background](https://petrjanda.substack.com/p/a-path-towards-a-data-platform-that)Â and giving access to the data products to data consumers. WithÂ [Data Mesh](https://cnr.sh/essays/what-the-heck-data-mesh)Â popularizedÂ *Data as a Product*, we will next see how can we apply this change to data orchestrators. Seeing the data as the use-case, the data product each data consumer wants has a clearly defined owner and maintainer.


In the end,Â **all data must come from somewhere and go somewhere**. Modern data orchestrators are the layer that interconnects all those tools, data, practitioners, and stakeholders.


> A data asset is typically a database table, a machine learning model, or a report â a persistent object that captures some understanding of the world. Creating and maintaining data assets is the reason we go through all the trouble of building data pipelines. Sandy Ryza onÂ [Introducing Software-Defined Assets](https://dagster.io/blog/software-defined-assets)


But how do we achieve such a shift to data products? We can use a declarative approach and abstractions that we know ahead ofÂ *runtime*. This way, we can declare and interact with them the same way we do with tasks and pipelines. We can show theÂ [Data Lineage](http://www.airbyte.com/glossary/data-lineage)Â of upstream assets â not tasks or pipelines. The actual data asset makes it easy to understand for anyone, for example, if a business logic changes or new data of an upstream asset arrives.


Achieving this shift from a pipeline to a business logic-centric data product view is a challenging engineering problem with data ingesting from dozens of external data sources, SaaS apps, APIs, and operation systems. At Airbyte, we know that pain firsthand and built all of theseÂ [connectors](https://airbyte.com/connectors)Â to mitigate theÂ [E(xtract) and L(oad)](https://airbyte.com/blog/data-integration)Â and difficultÂ [Change Data Capture (CDC)](https://airbyte.com/blog/change-data-capture-definition-methods-and-benefits)Â part.

Data product not live inside orchestrator
The data product does not need to live inside the orchestration tool. The orchestrator manages only the dependencies and business logic. These assets are primarily tables, files, and dashboards that live somewhere in a data warehouse, data lake, or BI tool.
Handy side-effect
A handy side-effect if you use mostly one orchestrator is that you can have a data product catalog inside the orchestrator. It gives you valuable information about when this particular data product was updated last, by who, and which upstream assets have changed. This information probably goes into a so-calledÂ
[Data Catalog](http://www.airbyte.com/glossary/data-catalog)
Â in the long run.

### Declarative Pipelines Are Taking Over Imperative Pipelines


Similar to howÂ [DevOps](http://www.airbyte.com/glossary/dev-ops)Â changed how software gets deployed with Kubernetes and descriptiveÂ [YAML](http://www.airbyte.com/glossary/yaml), the exact same should happen with data pipelines for faster developer cycles, better stability, and a better understanding of whatâs going on pre-runtime.


In short, anÂ **imperative**Â pipeline tellsÂ *how*Â to proceed at each step in a procedural manner. In contrast, aÂ **declarative**Â pipeline does not tell the order it needs to be executed but instead allows each step/task to find the best time and way to run. The how should be taken care of by the tool, framework, or platform running on. For example, update an asset when upstream data has changed. Both approaches result in the same output. However, the declarative approach benefits fromÂ **leveraging compile-time query planners**Â andÂ **considering runtime statistics**Â to choose the best way to compute and find patterns to reduce the amount of transformed data.


![/blog/data-orchestration-trends/data-orchestration_declarative-vs-imperative.png](https://www.ssp.sh/blog/data-orchestration-trends/data-orchestration_declarative-vs-imperative.png)

*Declarative vs. Imperative Overview*


Declarative approaches appeal because they make systems easier to debug and automate. Itâs done by explicitly showing intention and offering a simple way to manage and apply changes. By explicitly declaring how the pipeline should look, for example,Â **defining the data products that should exist**, it becomes much easier to discover when it does not look like that, reason about why, and reconcile. Itâs the foundation layer for your entire platformâs lineage, observability, and data quality monitoring.


### Abstractions: Jobs, Tasks, Resources, Triggers


Why abstractions, and how do they help us define Data Products? Because of higher-level abstractions, we are more explicit and declarative.


Lots of the ability to manage data products comes fromÂ **Python being a first-class citizen**Â in the modern data stack. InÂ [The Rise of the Data Engineer](https://medium.com/free-code-camp/the-rise-of-the-data-engineer-91be18f1e603), Maxime said code, in our case, a dedicated function is theÂ **best higher-level abstraction for defining a software**Â construct (automation, testability, well-defined practices, and openness). It declares upstream dependency in-line in a Pythonic open API, with abstracted authorship on top of assets with a Python function.


So what abstractions do we have as of today? For example, letâs take theÂ **resource**Â abstraction ([Dagster](https://docs.dagster.io/concepts/resources),Â [Prefect](https://docs.prefect.io/core/idioms/resource-manager.html), referred to as an operator inÂ [Airflow](https://airflow.apache.org/docs/apache-airflow/stable/concepts/operators.html)). You abstract complex environments and connections away with a simple construct like that. You have the immediate benefits of defining that once and using it in every task or pipeline with `context.resources.pyspark`, e.g., for Spark using Dagster. Through that, the code is battle-tested and used the same everywhere. As itâs a concrete construct, you can unit test the heck out of it-which is a tricky thing otherwise. Think of databricks notebooks. The hassle of which secrets, hostname, and configs (e.g., a Spark cluster hasÂ [thousands](https://spark.apache.org/docs/latest/configuration.html)Â of them) are done once, and you do not need to think about it when creating transformations.



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
` | `def spark_session_from_config(spark_conf=None):
    spark_conf = check.opt_dict_param(spark_conf, "spark_conf")
    builder = SparkSession.builder
    flat = flatten_dict(spark_conf)
    for key, value in flat:
        builder = builder.config(key, value)

    return builder.getOrCreate()

class PySparkResource:
    def __init__(self, spark_conf):
        self._spark_session = spark_session_from_config(spark_conf)

    @property
    def spark_session(self):
        return self._spark_session

    @property
    def spark_context(self):
        return self.spark_session.sparkContext


@resource({"spark_conf": spark_config()})
def pyspark_resource(init_context):
    """This resource provides access to a PySpark SparkSession for executing PySpark code within Dagster.
    """
    return PySparkResource(init_context.resource_config["spark_conf"])

#
# Example: How to use the resource within a task (op) with context.resources.pyspark.*
#
@op(required_resource_keys={"pyspark"})
def reading_json(context):
    spark_session = context.resources.pyspark.spark_session
    dataframe = spark_session.read.json("examples/src/main/resources/people.json")

my_pyspark_resource = pyspark_resource.configured(
    {"spark_conf": {"spark.executor.memory": "2g"}}
)

@job(resource_defs={"pyspark": my_pyspark_resource})
def my_spark_job():
    reading_json()
` |



An example of defining a resource once and re-use everywhere (tasks, pipelines, assets) with `context.resources.pyspark.*` (source onÂ [GitHub](https://github.com/dagster-io/dagster/blob/7207a6e2dc3fd3a6e9705ca361b9f5a18204c1e3/python_modules/libraries/dagster-pyspark/dagster_pyspark/resources.py#L33))


Another abstraction isÂ **tasks**Â ([Airflow](https://airflow.apache.org/docs/apache-airflow/stable/concepts/tasks.html),Â [Dagster](https://docs.dagster.io/concepts/ops-jobs-graphs/ops),Â [Prefect](https://docs.prefect.io/core/concepts/tasks.html)) that let you build pipelines likeÂ [Lego](https://www.lego.com/)Â blocks. Everyone creates tasks, and you choose the one you need to make yourÂ **DAG**. Data engineers could write stable, high-quality battle-tested tasks, and analytics or machine learning engineers could use them, which is a dream for reusability and following the DRY principle.


**Triggers**Â ([Prefect](https://docs.prefect.io/core/concepts/tasks.html#triggers),Â [Dagster](https://docs.dagster.io/concepts/partitions-schedules-sensors/schedules),Â [Airflow](https://airflow.apache.org/docs/apache-airflow/stable/concepts/scheduler.html)) are another one. They can be time, typical cron example `0 8 * * *` for a daily schedule at 8 AM or event-based such as a new file to an S3-folder, new data arrived at the API. More abstractions we will not go into areÂ **config systems**,Â **data types, IO management, and repositories**. These can add to each part of the above abstraction.


Abstractions let you use data pipelinesÂ **as a microservice on steroids**. Why? Because microservices are excellent in scaling but not as good in aligning among different code services. A modern data orchestrator has everything handled around the above reusable abstractions. You can see each task or microservice as a single pipeline with its sole purpose-everything defined in aÂ [functional data engineering](http://www.airbyte.com/glossary/functional-data-engineering)Â way. You do not need to start from zero when you start a new microservice or pipeline in the orchestration case.


There is one more key abstraction,Â **data products**Â ([Dagster](https://docs.dagster.io/concepts/assets/software-defined-assets)) or data assets that are newer and not get generalized among all orchestrators. We will discuss this abstraction in more detail next.


### Data-Aware Orchestration


To get to anÂ **operational control plane**, we need to come to a state of declarative data orchestration that knows exactly about each data product and its metadata. Instead of siloed data withÂ [unbundling](https://blog.fal.ai/the-unbundling-of-airflow-2/), we need to support the Modern Data Stack tools and orchestrate them in a unified way.


Letâs look at how a data-aware pipeline manifests in a real-live use case. WithinÂ [Dagster](http://dagster.io/), you see the non-data aware pipeline on the left vs. the data-aware data-asset driven pipeline on the right.


![/blog/data-orchestration-trends/data-orchestration_normal-data-pipeline-vs-data-product-view.png](https://www.ssp.sh/blog/data-orchestration-trends/data-orchestration_normal-data-pipeline-vs-data-product-view.png)

*Normal data pipeline on the left, data product view on the right. Notice that from one block on the left, we get 2 Airbyte data assets and 3 dbt models on the right. Note: These two graphs co-exist and can be toggled.*


Normal data pipeline on the left, data product view on the right. Notice that from one block on the left, we get 2 Airbyte data assets and 3 dbt models on the right. Note: These two graphs co-exist and can be toggled.


On the right, you see the data products `orders, daily_order_summary, and predicted_orders` defined ahead of any run. No need to execute anything first.Â **We want these artifacts to be available**Â andÂ [programmatically define them](https://dagster.io/blog/software-defined-assets).


One step more of a data-aware pipeline is integrating the MDS tools with metadata, such as the SQL statement out of the dbt model or the database schema from the dbt table, or information about an Airbyte sync. Below is the dbt example with Dagster.


![/blog/data-orchestration-trends/data-orchestration_integrated-modern-data-stack-metadata.png](https://www.ssp.sh/blog/data-orchestration-trends/data-orchestration_integrated-modern-data-stack-metadata.png)

*Data-Aware pipeline with integrated Metadata from the Modern Data Stack tools*


### The Missing Data Mesh Layer: The Data Product Graph


To conclude this chapter, we can say that everything we talked about in this chapter will essentially lead to theÂ *Data Product Graph,*Â which contains all relevant information for an Analyst or Business User to see the upstream dependency and core business logic. If you will, it bundles some of the modern data tools into a unified data product graph. Itâs a shift to a new way of organizing data and heterogeneous sources. To extend, it allows the user to self-serve as we once dreamt of in the Business Intelligence world.


![/blog/data-orchestration-trends/data-orchestration_illustration-data-product-graph.png](https://www.ssp.sh/blog/data-orchestration-trends/data-orchestration_illustration-data-product-graph.png)

*Illustration of a Data Product Graph*

Most common Data Mesh failure
According to theÂ
[Data Mesh Paper](https://martinfowler.com/articles/data-monolith-to-mesh.html)
: The most common failures of the past for building an intelligence platform are first-generation proprietary enterprise data warehouse and business intelligence solutions with lots of technical debt in unmaintainable ETL jobs and reports. And second-generation big data ecosystems with data lakes (swamps?) with long-running batch jobs operated by a central team specialized in data engineering. As I do not agree with everything said in the paper, I believe two of the reasons for the above failures are missing abstractions and tools that support the data products.

Next, letâs look at modern open-source orchestrators and when to use them.


## Modern Data Orchestrator Tools


As a modern Data Orchestrator, we call one with the above-mentioned higher-level abstractions, data assets, and additional data-aware features on top of task orchestration.


### Where Do We Come From: The Evolution of Data Pipeline Orchestration


Traditionally, orchestrators focused mainly on tasks and operations to reliable schedule and workflow computation in the correct sequence. The best example is the first orchestrator out there,Â [cron](https://en.wikipedia.org/wiki/Cron). Opposite to crontabs, modern tools need to integrate with the Modern Data Stack.


To understand the complete picture, letâs explore where we came from before Airflow and other bespoken orchestrators these days.

1. In 1987, it started with theÂ **mother of all scheduling**Â tools,Â [(Vixie) cron](https://en.wikipedia.org/wiki/Cron)
2. to moreÂ **graphical drag-and-drop**Â ETL tools around 2000 such asÂ [Oracle OWB](https://en.wikipedia.org/wiki/Oracle_Warehouse_Builder),Â [SQL Server Integration Services](https://docs.microsoft.com/en-us/sql/integration-services/sql-server-integration-services?view=sql-server-ver15),Â [Informatica](https://www.informatica.com/)
3. toÂ **simple orchestrators**Â around 2014 withÂ [Apache Airflow](https://airflow.apache.org/),Â [Luigi](https://github.com/spotify/luigi),Â [Oozie](https://oozie.apache.org/)
4. toÂ **modern orchestrators**Â around 2019 such asÂ [Prefect](https://www.prefect.io/),Â [Kedro](https://github.com/quantumblacklabs/kedro),Â [Dagster](https://github.com/dagster-io/dagster/), orÂ [Temporal](https://github.com/temporalio/temporal)


If you are curious and want to see the complete list of tools and frameworks, I suggest you check out theÂ [Awesome Pipeline List](https://github.com/pditommaso/awesome-pipeline#pipeline-frameworks--libraries)Â on GitHub.

Closed-Source Solutions
Besides the above open-sourced, we have closed-source, mostly low-code or no-code solutions involving scheduling, such asÂ
[Databricks](https://databricks.com/)
Â with the acquisitions ofÂ
[bamboolib](https://bamboolib.8080labs.com/)
,Â
[Ascent.io](http://ascent.io/)
,Â
[Palantir Foundry](https://www.palantir.com/palantir-foundry/)
, and many more.

### Data Orchestration Platform: Unbundling vs. Bundling


Do we think of data orchestrators as data orchestration platforms that bundle different tools, or should they be unbundled? For example,Â [in The Unbundling of Airflow](https://blog.fal.ai/the-unbundling-of-airflow-2/), Gorkem explains the open-source ecosystem:


> We have seen the same story over and over again. Products start small, in time, add adjacent verticals and functionality to their offerings, and become a platform. Once theseÂ **platforms**Â become big enough, people begin to figure out how to serve better-neglected verticals or abstract out functionality to break it down into purpose-built chunks, and the unbundling starts.


Furthermore, the Airflow DAG is being split from end-to-end data pipelines to ingestion tools (Airbyte, Fivetran, Meltano), transformational tools (dbt), reverse ETL tools (Census, Hightouch), and metrics layers (Transform), ML-focused systems (Continual), just to name a few. Dagster immediately stated a post aboutÂ [Rebundling the Data Platform](https://dagster.io/blog/rebundling-the-data-platform)Â slouching toward this âunbundledâ world that moves from imperative tasks to declarative data assets. These can be seen asÂ **orchestrator platforms providing some of the data catalog and data lineage toolâs responsibilities**.


## What Are Trendy Open-Source Data Orchestration Tools


As weâve laid out where we come from with orchestration and what the evolutions were, what is the current trend? Letâs dig deeper into some data orchestrators that support that future. Also, letâs see when youâd use each orchestrator.


The evolution shows that the most stable and widely used orchestrator is Apache Airflow. Itâs the base of many prominent tech companies. As it was the first of its kind with Luigi and Oozie, it grew with some of the core philosophies built-in from the very beginning. One is a pure schedule, not knowledgeable about the inner life of a task. It wasnât designed to interact with inputs and outputs of data (oldÂ [XComs](https://airflow.apache.org/docs/apache-airflow/stable/concepts/xcoms.html)Â debate). In Airflow 2.0, the new featureÂ [TaskFlow](https://airflow.apache.org/docs/apache-airflow/stable/concepts/taskflow.html)Â provides a better developer experience to pass data from one task to another but still relies on XCom. When orchestrating data pipelines with Airflow is still recommended to use intermediary storage to pass data between different tasks. Thatâs why I call Airflow a simple orchestrator in this article, and we mainly focus on the âmodernâ data orchestrator such as Prefect and Dagster.


I will leave Kedro aside as the momentum is on the other two, and it focuses mostly on data science.Â **Temporal**Â is another fascinating orchestrator. At Airbyte, we internallyÂ [use the Temporal Java SDK](https://airbyte.com/blog/scale-workflow-orchestration-with-temporal)Â to orchestrate ETL jobs. Temporal focuses on real-time application orchestration instead of heterogeneously complex cloud environments. As of today, Temporal lets you write workflows in Java, Go, TypeScript and PHP, and provides no Python support.


As seen in the abstraction chapter above, modern orchestrators already support vast abstractions: the two most prominent ones and some suggestions on when to use them below.


**Prefect**Â if you need a fast and dynamic modern orchestration with a straightforward way to scale out. They recently revamped the prefect core asÂ [Prefect 2.0](https://www.prefect.io/blog/introducing-prefect-2-0/)Â with a new second-generation orchestration engine calledÂ [Orion](https://www.prefect.io/blog/announcing-prefect-orion/). It has several abstractions that make it a swiss army knife for general task management.


**Dagster**Â when you foresee higher-level data engineering problems. Dagster has more abstractions as they grew from first principles with a holistic view in mind from theÂ [very beginning](https://dagster.io/blog/introducing-dagster). They focus heavily on data integrity, testing, idempotency, data assets, etc.

Dagster vs. Airflow
A good sense of what has changed between simple to modern orchestrators, you can find the difference inÂ
[Dagster vs. Airflow](https://dagster.io/blog/dagster-airflow)
.
History of Dataflow Automation
A good read about how Prefect sees theÂ
[History of Dataflow Automation](https://www.prefect.io/guide/blog/a-brief-history-of-dataflow-automation)
.
dbt adding Python
Interesting that dbt, as the mother of SQL transformation, also putsÂ
[Python](https://github.com/dbt-labs/dbt-core/discussions/5261)
Â on theirÂ
[Roadmap](https://github.com/dbt-labs/dbt-core/blob/main/docs/roadmap/2022-05-dbt-a-core-story.md)
Â (besides others such as their ownÂ
[Metrics Layer](https://docs.getdbt.com/docs/dbt-cloud/using-dbt-cloud/cloud-metrics-layer)
). EngagingÂ
[discussions](https://github.com/dbt-labs/dbt-core/discussions/5073)
Â are ongoing about integrating with external tools such as Dagster and Prefect.

### Data Orchestration Examples


Here are some hands-on examples that help you get started with the world of data-aware orchestrators.


ThisÂ [Demo](https://youtu.be/oOOuQQsnPTM)Â shows the Airbyte integration with dbt in one declarative data asset pipeline, including the rich metadata such as db-schema from Airbyte and other valuable metadata. Check out theÂ [Tutorial](https://airbyte.com/tutorials/orchestrate-data-ingestion-and-transformation-pipelines)Â andÂ [Code](https://github.com/dagster-io/dagster/tree/aa6d4ba20a3caaa5b15fbe8015186dc9327f3248/examples/modern_data_stack_assets)Â on GitHub.


The same goes for integrating prefect, dbt, and Airbyte-theÂ [Demo](https://youtu.be/uDqe1x_MhVg)Â on YouTube, aÂ [Tutorial](https://airbyte.com/tutorials/elt-pipeline-prefect-airbyte-dbt), and theÂ [Code](https://github.com/desertaxle/airbyte-prefect-recipe/blob/master/prefect/flow.py)Â on GitHub.


## Conclusion and Outlook


I hope you better understand the importance of focusing on the data products instead of data pipelines and why it is better to write declarative code so that data pipelines can update themselves when upstream data assets change. We also covered reasons for using abstractions in the complex big open-source data world and how to make pipelines more data-aware to align with the mission of the data mesh.


I am looking forward to debating it with you.


---


```
Originally published at Airbyte.com
```

[Discuss on Bluesky](https://bsky.app/search?q=domain%3A%20https://www.ssp.sh/blog/data-orchestration-trends/)
|
[Pay what you like](https://ko-fi.com/sspaeti)
|
[Orchestration](https://www.ssp.sh/tags/orchestration/)
[Data Pipelines](https://www.ssp.sh/tags/data-pipelines/)
[Python](https://www.ssp.sh/tags/python/)
[Dagster](https://www.ssp.sh/tags/dagster/)
[Airflow](https://www.ssp.sh/tags/airflow/)
[Prefect](https://www.ssp.sh/tags/prefect/)
[Open-Source](https://www.ssp.sh/tags/open-source/)
[ETL](https://www.ssp.sh/tags/etl/)
