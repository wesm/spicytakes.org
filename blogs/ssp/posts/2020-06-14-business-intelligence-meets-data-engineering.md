---
title: "Business Intelligence meets Data Engineering with Emerging Technologies"
date: 2020-06-14
url: https://www.ssp.sh/blog/business-intelligence-meets-data-engineering/
slug: business-intelligence-meets-data-engineering
word_count: 4160
---

![Business Intelligence meets Data Engineering with Emerging Technologies](https://www.ssp.sh/blog/business-intelligence-meets-data-engineering/images/shutterstock_abstract_data_engineering_kk-1024x601.jpg)

Contents

Today we have more requirements with ever-growing tools and framework, complex cloud architectures, and with data stack that is changing rapidly. I hear claims: “Business Intelligence (BI) takes too long to integrate new data”, or “understanding how the numbers match up is very hard and needs lots of analysis”. The goal of this article is to make business intelligence easier, faster and more accessible with techniques from the sphere of data engineering.


In an [earlier post](https://www.ssp.sh/blog/data-engineering-the-future-of-data-warehousing/), I pointed out what data engineering is and why it’s the successor of business intelligence and data warehousing. When a data engineer is needed and what he is doing. The data engineers tooling language python and what has changed in ETL. In this post, I will focus on challenges in BI, and how to solve them with data engineering.


## The Goal of Business Intelligence


But first, let’s talk a second about “what should BI do for us?”


In my terms, BI should produce a simple overview of your business, boost efficiency, and automate repetitive tasks across your organisation. In more detail:

- **Roll-up capability** - (data) visualisation over the most important [KPIs](https://en.wikipedia.org/wiki/Performance_indicator) (aggregations) - alike a cockpit in an airplane which gives you most important information at one glance.
- **Drill-down possibilities** - from the above high-level overview drill-down into the very details to figure out why something is not performing as planned. **Slice-and-dice or pivoting** your data from different angles.
- **Single source of truth** - instead of multiple spreadsheets or other tools with different numbers, the process is automated and done for all unified. Employees can talk about the business-problems instead of the various numbers everyone has. Reporting, budgeting, forecasting are automatically updated and consistent, accurate and in a timely manner.
- **Empower users**: With so-called [self-service BI](https://www.sisense.com/glossary/self-service-bi/), every user can analyse their data instead of only BI or IT persons.


## Problems of Business Intelligence


On the other hand, BI has some substantial problems with speed and transparency. I tried to summarise the issues I learned or heard people telling over my career as a BI engineer and specialist working with Oracle and SQL Server:

- **It takes too long to integrate additional sources,** and BI engineers are **overloaded** with work.
- **The transparency** is a problem for other users than BI engineers. Only they can see inside the transformation logic mostly hidden in proprietary ETL tools.
- Business people or managers are **dependent on BI engineers**. There is no easy way to access the ETL or getting any real-time data.
- The BI department **makes it more complicated than it requires to be**. The impression was always it shouldn’t be as complex. For us, it is clear with all the transformations, business logic cleaning, star schema transformation, performance tuning, working with big data, and the list goes on and on. But for non-BI’lers, this is hard to understand.
- **Difficulties to handle ([semi](https://en.wikipedia.org/wiki/Semi-structured_data)-) [unstructured](https://en.wikipedia.org/wiki/Unstructured_data) data formats** like JSON, images, audio, video, e-mails, documents, etc.
- **General data availability only once a day** (traditionally). We get everything in real-time in our private lives, everyone demands the same from modern BI systems.


This list is not complete by any means. Also, can any point be mitigated with special solutions (e.g. cloud-solutions with [SnowflakeDB](https://www.snowflake.com/) with [Variant](https://docs.snowflake.com/en/sql-reference/data-types-semistructured.html#variant) data-type for semi-structured data) or different approaches ([data vault](http://danlinstedt.com/solutions-2/data-vault-basics/) for fast integration). However, stereotypes are deeply preserved and from what I hear, still around.


## 🔗 Data Engineering Approaches


Because I encountered these bottlenecks myself, and more frequently lately, I asked myself: “How can we:

- Make BI *easier*?
- Transparent for everyone?
- Effortless to change or add new data or transformations but still have some governance and testing?
- Fast in ad-hoc queries to explore and slice-and-dice your data?
- Have more frequent data loads?
- Simplify following the transformations for all data-savvy people and not exclusive for involved BI engineers?
- Extend additional machine learning capabilities smoothly?


I’m aware that nowadays a lot is going on, especially in around open-source tools and framework, data ops and deployments with container-orchestration systems and the like.


Nevertheless, I tried to collect some approaches that helped me make this complex construct more open and ease the overall experience. Some will present itself more complicated in the short term, but significantly leaner and less complex over time. You can apply each of them separately, yet the more you use, the more apparent the flow as a whole will be.


### “Use a data lake.“


Let’s start with the first: Use a data lake or [lakehouse](https://databricks.com/blog/2020/01/30/what-is-a-data-lakehouse.html) instead of a data warehouse (DWH). **This gives you speed, ability to have (semi-) unstructured data** and define schema later during transformation (ELT rather than ETL). As well it will provide you with **high** **transparency** as data gets stored into a data lake open for everyone to access or analyse. It’s easy to **add new columns or share your data with co-workers**. You can use wide distributed computation like [Spark SQL](https://databricks.com/glossary/what-is-spark-sql) or [Presto](https://prestodb.io/) to explore, join and transform your data instantly with ad-hoc queries.


The data availability is fast, no batch needed every night as data gets deposited into the lake as a first step. It may not be clean yet, but you can directly start exploring and add transformations to do so. A common approach is to add a data lake in front of the data warehouse. This way, you have the benefit of both, instant data in the lake but also structured and cleansed at the end of the data warehouse.


A practical overview which illustrates the components involved well is the evolution from a data warehouse over the data lake to a lakehouse. The most important part to notice is the ETL which is also the central component of data engineering overall. You see that it moved from hidden behind the [data marts](https://en.wikipedia.org/wiki/Data_mart) to the data lake architecture to **the primary transformation layer in one unified block.**


![/blog/business-intelligence-meets-data-engineering/images/data-lakehouse-1.png](https://www.ssp.sh/blog/business-intelligence-meets-data-engineering/images/data-lakehouse-1.png)

*What is a LakehousebyDatabricks*


Further data architectures that manifest the components in different angels you can find in my [LinkedIn post](https://www.linkedin.com/posts/sspaeti-com_four-different-data-architectures-activity-6660097384279744512--5e1) or, for more information about a data warehouse and its comparison to a data lake, check out my [earlier blog post](https://www.ssp.sh/blog/data-warehouse-vs-data-lake-etl-vs-elt/).


### “Use transactional processing.”


To support various features of a relational database in a data lake, you need transactional processing. Luckily **[Delta Lake](https://delta.io)** is here to rescue you. **Delta has many awesome features like ACID transactions, [time-travel](https://databricks.com/blog/2019/02/04/introducing-delta-time-travel-for-large-scale-data-lakes.html), keeping a [transaction log](https://databricks.com/blog/2019/08/21/diving-into-delta-lake-unpacking-the-transaction-log.html), SQL API to write native SQL** **as insert, update, delete and even merge statements, open-format ([Apache Parquet](https://parquet.apache.org/)), unified batch and streaming source and sink (no [lambda architecture](https://en.wikipedia.org/wiki/Lambda_architecture) needed anymore), [schema evolution](https://databricks.com/blog/2019/09/24/diving-into-delta-lake-schema-enforcement-evolution.html), [optimistic concurrency](https://docs.databricks.com/delta/concurrency-control.html)**. The full list and more information on [delta.io](https://delta.io/). Also, check out and excellent customer example with Apple about [threat detection at scale](https://databricks.com/session/keynote-from-apple).


![/blog/business-intelligence-meets-data-engineering/images/a-screenshot-of-a-social-media-post-description-a.png](https://www.ssp.sh/blog/business-intelligence-meets-data-engineering/images/a-screenshot-of-a-social-media-post-description-a.png)

*Key features of delta lake by June 2020 (delta.io)*


As in data lakes, we commonly have distributed files, it’s hard to get them structured and arranged. Especially if you want to insert, update or delete rows. Delta has **different APIs, besides scala and python, it also gives you SQL API** (from Spark 3.0 on or in [databricks](https://databricks.com/)), where you can easily write an *update* or even *merge* statements on your distributed files. As it’s powered by Spark, you can do this entirely at scale.


Behind the scene is raw **[Apache Parquet](https://parquet.apache.org/), optimised columnar storage and highly compressed.** This allows you **to query your data directly out of your data lake efficiently.** No initial transformation needed there.


With **slowly changing dimension (SCD) still being a thing in some cases, **Delta has time-travel** to solve this. It’s similar to snapshotting what we did back in earlier days. But this time though with fairly cheap blob storage compared to SSDs where instead of a daily or monthly snapshots, Delta stores every batch of changes as a separate version. This gives you the power to travel back in time to older versions in case you mistakenly deleted something or if you need analytics to be pointed to specific versions. This is for as long as the retention time is set.


These changes and snapshots are stored in a **transaction log maintained by Delta**. Beside time-travel, this is a **kind of change data capture (CDC) with all tracked changes per table**. You see which files have been affected, what operation, who did and more, and that for each transaction. This is stored in a JSON format separately. And transaction data can get big as well, Delta creates a checkpoint file every ten commits and with the entire state of the table at a point in time – in Parquet format which is fast and simple for Spark to read.


### “Use less of surrogate keys, instead go back to business keys that everyone understands.”


In data warehouses, it is a common practice to use [surrogate keys](https://en.wikipedia.org/wiki/Surrogate_key) to address a row by a single artificial key. When this makes sense to support the [dimensional model](https://data-warehouses.net/glossary/dimensionalmodel.html) and to be sure that a row key has a unique ID, in data lakes you don’t do that, to begin with. I’d argue to minimise as much as possible as **it makes data reading more complex in terms of understanding and communication**. Surrogate keys are random Ids which gives no meaning to anybody (that’s why also mostly used or seen in the background).


In distributed systems by contract, it’s not as practical anymore to have unique keys over your full data set as data getting bigger. Especially with parallelism, it’s hard to parallelise and still have uniqueness. Better to use [hash keys](https://danlinstedt.com/allposts/datavaultcat/dv2-keys-pros-cons/) to mitigate that problem. The downside, they are even longer and less readable. So why not going back to the [business key](https://en.wikipedia.org/wiki/Natural_key) (BK, also called natural key) that your source system already generated for you? **Business keys are already understood by everyone, to some degree unique (as created as a sequence in the source-system), holding the same value for the life of the data set, can be tracked and compared therefor all the way back**.


Of course, there are [great reasons](https://danlinstedt.com/allposts/datavaultcat/dv2-keys-pros-cons/) for surrogate keys. They give us big advantages in some ways but to what cost? We need to put a lot of work to ensure the correct granularity of facts and that dimensions get merged and cleaned together with a unique ID as the representer of one row. But again, in data lakes, we have fewer rules, and it’s less rigid. We can, for example, have duplicates in the first place, and only clean and erase them later on.


This topic also very much goes hand by hand with the question if “Kimball still relevant in the modern data warehouse?” and “[Normalisation](https://en.wikipedia.org/wiki/Database_normalization) and its normal forms?”. As for the latter, it’s not as important anymore in terms of storage as it getting cheaper with blobs and similar storages, but still valid for analytics purposes. For more details and insights, I encourage you to check out the [blog post](https://www.advancinganalytics.co.uk/blog/2019/6/17/is-kimball-still-relevant-in-the-modern-data-warehouse) by Simon Whiteley about this very topic.


### “Use notebooks to open up the data silos.”


With **notebooks** ([jupyter](https://jupyter.org/), [zeppelin](https://zeppelin.apache.org/), [databricks](https://docs.databricks.com/notebooks/index.html)) **everyone has access to the data, can explore and write analytics with all the advanced statistical and data science libraries**. It’s straightforward to set-up, no need to install a local environment or [IDE](https://en.wikipedia.org/wiki/Integrated_development_environment), it works with your browser of choice. You can spread your visualisations by quickly sharing a link. You can also work together in the same notebook. With integrated markdowns, you explain the whole story and thought-process behind the numbers to people naturally.


**The** **downside of notebooks is that your code will be duplicated and scattered around the place**. A little bit like everyone having their own Excels, everyone will start their own notebooks (but of course different data-wise, as the data is stored centrally). I suggest you set strict and clear rules or governance around the notebooks and starting to integrating stable notebooks into your common data pipelines.


For a fast and smooth transition, you should have a look at [papermill](https://github.com/nteract/papermill) which allows you to parameterise, execute and analyse notebooks. Even **a step further is to use [dagster](https://dagster.io/) and either use the notebooks as a step of your pipeline** (dagster integrates with papermill) **or incorporate it into your pipeline fully** with dedicated [solids](https://docs.dagster.io/concepts/solids-pipelines/solids). This way, you avoid code duplication and reusing solids.


### “Use python (and SQL if possible).”


**Python is the [tooling language](https://www.ssp.sh/blog/data-engineering-the-future-of-data-warehousing/#The_tool_language_Python) of data engineers these days**. Sure there is [golang](https://golang.org/), [javascript](https://en.wikipedia.org/wiki/JavaScript), [scala](https://www.scala-lang.org/) and other popular languages, but python is still hard to beat when it comes to simplicity and multi-purpose capabilities (data science, web and others). SQL is getting again more traction, which is hugely welcome. Still, SQL will never be able to do what [object-oriented programming](https://en.wikipedia.org/wiki/Object-oriented_language) languages are doing, that’s why I think python is here for many years to stay in building data pipelines.


Therefor **use frameworks or tools that are written in python to code your pipelines**. Notebooks are already supporting SQL and python, but they don’t support organisation or orchestration. Better to use tools like the [hugely popular](https://qr.ae/TWhzLf) and well know [Apache Airflow](https://airflow.apache.org/). There are new kids in the blocks (as always), which are promising, one being the above-mentioned dagster. More in my little Quora answer on [What are common alternatives to Airflow](https://qr.ae/pNrIPi) if you are interested.


### “Use open-source tools.”


**Open-source is available free for everyone, no licences involved and easy to start right away**. There is no vendor-lock-in which requires sorrow discussions throughout the team(s) before buying-in a closed-source project or product.


On the other hand, one open-source tool rarely comes along solo, which can be or get exhausting to fit and evaluate all your favourite tools and applications from the open-source zoo. Also, you need to follow-up on never-ending versions or bug-fixes that might come out and valuable to you. The idea here is you know which tools to use maybe through some suggestions of other companies or some good consultancies. And **be open to trying out along the way as you are not locked-in, you can always replace or adapt later on**. The learning process can be as valuable as choosing the right tool in the first place.


![/blog/business-intelligence-meets-data-engineering/images/Matt_Turck_FirstMark_Big_Data_Landscape_2018_Final.png](https://www.ssp.sh/blog/business-intelligence-meets-data-engineering/images/Matt_Turck_FirstMark_Big_Data_Landscape_2018_Final.png)

*Big Data and AI Landscape for 2018 byMatt Turcktaken fromGreat Power, Great Responsibility*


**You can also opt for a middle approach, something like [Databricks](https://databricks.com/)** for Spark and machine learning capabilities. You are up-and-running in an instant and lock yourself in just halfway. With Spark and notebooks under the hood with both open-sourced technologies, you can switch to your cluster by any time. You lose premium features and speed, which you can also buy and add again later on.


**A practical example I put together in an [earlier post](https://www.ssp.sh/blog/open-source-data-warehousing-druid-airflow-superset/) where I use the open-source technologies for building a complete data warehouse**. That time back in 2018 without Delta Lake and other tools mentioned above as they weren’t released that time. I used [Apache Airflow](https://airflow.apache.org/), [Apache Druid](https://druid.apache.org/) and [Apache Superset](https://superset.incubator.apache.org/).


### “Load incremental and Idempotency.”


Compared to the nightly loads of traditional data warehouses, we need to load **incrementally. This makes your data more modular and manageable**, especially when you have a [star schema](https://en.wikipedia.org/wiki/Star_schema). Fact tables can only be appended and dimensions only need to scan the newest transactions instead of the entire fact table.


With the incremental approach, you **switch from batch to event-driven**. Your updates and inserts are independent, and you get autonomous batches. If you succeed in switching, you get a near real-time analytics solution which you can scale and parallelise those batches.


Another approach is enforcing [idempotency](https://en.wikipedia.org/wiki/Idempotence) which is vital for the operability of pipelines and helps mainly in two ways. It **guarantees that you can re-run your pipeline and it will produce the same result every time**. On the other hand data scientist and analytics, people rely on point-in-time snapshots and perform historical analysis. Meaning your data should not be mutable as time progress. Otherwise, we would get different results as time goes on. That’s why pipelines should be build to reproduce the same output when running with the same (business) logic and time interval. This is called idempotency and used in [functional programming](https://medium.com/@maximebeauchemin/functional-data-engineering-a-modern-paradigm-for-batch-data-processing-2327ec32c42a), which was the role model for idempotency.


**A nice side effect of event-driven and incremental loading is that you can eliminate the [lambda architecture](https://en.wikipedia.org/wiki/Lambda_architecture).** **One single data flow for batch and stream** left which is perfectly in-line with **Delta Lake**. Well suited and a good fit for that purpose is [Spark Structured Streaming](https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html) with the integrated option [micro-batching](https://databricks.com/blog/2018/03/20/low-latency-continuous-processing-mode-in-structured-streaming-in-apache-spark-2-3-0.html). That way you benefit from both worlds, as you stream and can set the latency to 0, but you can also reduce speed in processing. For example when you have a batch per hour to mitigate the overhead for looking up dimensions or specifically aggregations, which you need to perform otherwise for each stream (which might take time as well).


### “Don’t do structure changes (ALTER) in traditional DDL manner.”


Everyone working with data knows how painful it is to change (ALTER) a data type or rename a column. There is a whole chain of dependencies and its a lot of work without real value or impact. With the above incremental and idempotency pattern, you get this for free. This means that your changes are instead of renaming or changing business logic for a field, **better be adding new fields and change your pipeline and analytics later on** **without breaking anything**.


With the use of Delta Lake, you also get [schema evolution](https://databricks.com/blog/2019/09/24/diving-into-delta-lake-schema-enforcement-evolution.html) and [optimistic concurrency](https://docs.databricks.com/delta/concurrency-control.html) which both helps you with this pain. As the first one automatically updates schema changes without breaking things. And the second will make sure that two or more users can update the same dataset without failing as long as not the same column and the corresponding data will be changed simultaneously.


### “Use a container-orchestration system.”


[Kubernetes](https://stackoverflow.blog/2020/05/29/why-kubernetes-getting-so-popular/) has become the de-facto standard for your cloud-native apps to (auto-) [scale-out](https://stackoverflow.com/a/11715598/5246670) (horizontal instead of vertical) and to deploy your open-source zoo fast, cloud-provider-independent. No lock-in here as well. You could use [open-shift](https://www.openshift.com/) or [OKD](https://www.okd.io/). With the latest version, they **added the [OperatorHub](https://operatorhub.io/) where you can install as of today 133 items with just a few clicks**. Databases and machine learning application that are otherwise complex to install is very much made simple.


Some more reasons for Kubernetes are the **move from infrastructure as code towards infrastructure as data, specifically as [YAML](https://en.wikipedia.org/wiki/YAML)**. All the resources in Kubernetes that include Pods, Configurations, Deployments, Volumes, etc., can simply be expressed in a YAML file. **Developers quickly write applications that run across multiple operating environments**. Costs can be reduced by scaling down (even to zero with, e.g. [Knative](https://medium.com/knative/knative-v0-3-autoscaling-a-love-story-d6954279a67a)) and also by using plain python or other programming languages instead of paying for a service on Azure, AWS, Google Cloud. Its management makes it easy through its modularity and abstraction, also with the use of Containers ([Docker](https://en.wikipedia.org/wiki/Docker_%28software%29) or [Rocket](https://coreos.com/rkt/)), and you can monitor all your applications in one place.


### “Use declarative pipelining instead of imperative.”


As with Kubernetes YAML-files, you start working descriptive, meaning you define *what* should do rather than *how*. For the same, we should aim in data pipelines to eliminate as much from the how (the glues) in our DAGs and only declare the what. The tool, frameworks and platforms should take care of the how.


[Sean Knapp](https://www.linkedin.com/in/seanknapp), the founder of the unified data-pipeline solution [ascend.io](https://www.ascend.io/) quotes: “Declarative programming is a paradigm that expresses the logic of a computation without describing its control flow… [in an] attempt to minimize or eliminate side effects by describing what the program must accomplish.” Check out more details in his impressive presentation on [Intelligent Orchestration: Data’s missing link](https://www.datacouncil.ai/hubfs/Data%20Council/slides/nyc19/Sean-Knapp-Ascend%20-%20Intelligent%20Orchestration%20-%20Data%20Council%20NY%202019.pdf).


![/blog/business-intelligence-meets-data-engineering/images/a-screenshot-of-a-cell-phone-description-automati.png](https://www.ssp.sh/blog/business-intelligence-meets-data-engineering/images/a-screenshot-of-a-cell-phone-description-automati.png)

*Declarative vs Imperative bySean Knapp&Ascend.iotaken fromIntelligent Orchestration*


This might be obvious, yet it’s hard to implement. That’s why [ascends.io](https://www.ascend.io/) offers a superior all-in-one platform where you can do this. It sorts out all how’s for you and you focus on the what.


If it so happens that you aren’t having a platform like this, you might need an architecture that supports towards it. It’s not something that comes naturally I would say, you need to build around this paradigm. But the rewards might be worth with faster cycles and more problem-solving approaches.


#### The evolution of Pipeline Orchestration


A quick overview from where we are coming from in types of orchestration and pipeline tools:

1. From the mother of all scheduling tool [cron](https://en.wikipedia.org/wiki/Cron) to more
2. to more Graphical ETL tools like [Oracle OWB](https://en.wikipedia.org/wiki/Oracle_Warehouse_Builder), [SQL Server Integration Services](https://docs.microsoft.com/en-us/sql/integration-services/sql-server-integration-services?view=sql-server-ver15), [Informatica](https://www.informatica.com/) to more
3. code centric tools like [Airflow](https://airflow.apache.org/), [Luigi](https://github.com/spotify/luigi), [Oozie](https://oozie.apache.org/)
4. to python frameworks like [Prefect](https://www.prefect.io/), [Kedro](https://github.com/quantumblacklabs/kedro), [Dagster](https://github.com/dagster-io/dagster/) or even fully SQL framework [dbt](https://www.getdbt.com/)
5. to declarative pipelines fully managed into [Ascent.io](https://www.ascend.io/), [Palantir Foundry](https://www.palantir.com/palantir-foundry/) and other data lake solutions


**There is a ton of tools and framework out there if your interested check out the [Awesome Pipeline List](https://github.com/pditommaso/awesome-pipeline#pipeline-frameworks--libraries)**. If your interested in some alternatives to Apache Airflow that is the most popular at the moment, in my opinion, check out [common alternatives to Airflow](https://qr.ae/pNrIPi).


### “Use data catalogs to have a central metadata store.”


[Data catalogs](http://cidrdb.org/cidr2017/papers/p111-hellerstein-cidr17.pdf) are a centralised store where all your metadata data about your data lies. Nowadays synonym with metadata store, data discovery or similar. This is vital as with data lakes and other data stores **you want to keep an overview and the ability to search for your data**.


A perfect example is provided by [Lyft](https://www.lyft.com/). They implemented an application on top of a data catalog called [Amundsen](https://github.com/lyft/amundsen). Amundsen does not only shows what data sets are available but also which years who created it. Furthermore, metadata of how many rows, min/max entries, etc. about a table is shown if the connected database is supported. It incorporates even a [rating](https://eng.lyft.com/amundsen-lyfts-data-discovery-metadata-engine-62d27254fbb9) system where users can give feedback about a data set to give you a feeling for the data quality and how valid it is to use that very data set.


On top, Amundsen connects data sets with dashboards and notebooks to show in which of these has been a particular data set been used. This avoids duplicated work, and you find your answers to your data questions in no time.Â


![/blog/business-intelligence-meets-data-engineering/images/Amundsen.png](https://www.ssp.sh/blog/business-intelligence-meets-data-engineering/images/Amundsen.png)

*An example of Ammundsen back on Apr 2, 2019, posted onLyft’s data discovery & metadata engineby Mark Grover*


### “Use closed-source if you don’t have the developers or the time.”


As not everything mentioned above is built in one day and might not be all that mild without the necessary teams or financials, I also include the closed source [platform as a service (PaaS)](https://en.wikipedia.org/wiki/Platform_as_a_service) solutions that will cost you but gives all the advantages out-of-the-box and immediately. Two solutions I used myself are the mentioned [Ascend.io](https://www.ascend.io/) or [Palantir Foundry](https://www.palantir.com/palantir-foundry/). There are for sure more, if you know any genuine ones, let me know.


For more specific solutions, I see the following:

- If you use [**OLAP**](https://en.wikipedia.org/wiki/Online_analytical_processing) (slice and dice ad-hoc queries), choose a managed [Druid](https://druid.apache.org/) cluster from [Imply.io](https://imply.io/).
- If you need a **Cloud Data Warehouse**, choose [Snowflake DB](https://www.snowflake.com/product/).
- If you have already many different systems, and you want to bring them together, chose **Data Virtualisation** solution [Dremio](https://www.dremio.com/) which uses [Apache Arrow](https://arrow.apache.org/) for the power.
- If you mainly want to focus on **dashboards and reports**, choose a [Looker](https://looker.com/) or [Sisense](https://www.sisense.com/), which gives you a hosted cube kind of solution.


See also a more complete list with some more alternatives for cube-replacements in my [earlier post](https://www.ssp.sh/blog/olap-whats-coming-next/#List_of_Cube-Replacements) (although not fully up-to-date anymore as of Nov 2018).


## Conclusion


We have seen that the goal of business intelligence is to produce an overview of business and organisation-wide, and the most challenging problems to create data warehouses that are transparent, handles unstructured data formats or real-time data availability. And then how we solve them with twelve emerging data engineering technologies and approaches.


I hope these approaches are helpful and will solve some of your challenges with your BI system. Or otherwise, help you with data architecture or reduce some complexity on the way. To do all of it it’s quite a job. However, if you start and picking the most relevant for you, I guess you are on the right path forward. And possibly the most advantage, your architecture will be future-proof and prepared for big data and cloud-native solutions.


If you don’t have the time nor resources, you could pick a closed-source platform as a service that just works as we saw in the last approach, that’s also fine. That will cost you more in the long run, but you are up-and-running instantly.


To see the tools in action, check-out my hands-on post [Building a Data Engineering Project in 20 Minutes](https://www.ssp.sh/blog/data-engineering-project-in-twenty-minutes/). That’s it for now. Let me know your thoughts on this, what are your go-to tools and frameworks to solve some of the challenges? I’d appreciate your comments.


---


```
Republished on LinkedIn & Towards Data Science.
```

[Discuss on Bluesky](https://bsky.app/search?q=domain%3A%20https://www.ssp.sh/blog/business-intelligence-meets-data-engineering/)
|
[Pay what you like](https://ko-fi.com/sspaeti)
|
[Big Data](https://www.ssp.sh/tags/big-data/)
[Data Lake](https://www.ssp.sh/tags/data-lake/)
[Open Table Format](https://www.ssp.sh/tags/open-table-format/)
[Data Pipelines](https://www.ssp.sh/tags/data-pipelines/)
[Data-Warehouse](https://www.ssp.sh/tags/data-warehouse/)
[Delta Lake](https://www.ssp.sh/tags/delta-lake/)
[Kubernetes](https://www.ssp.sh/tags/kubernetes/)
[Open-Source](https://www.ssp.sh/tags/open-source/)
[Python](https://www.ssp.sh/tags/python/)
[Business-Intelligence](https://www.ssp.sh/tags/business-intelligence/)
