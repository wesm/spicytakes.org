---
title: "OLAP, whatâs coming next?11-23"
date: 2018-11-23
url: https://www.ssp.sh/blog/olap-whats-coming-next/
slug: olap-whats-coming-next
word_count: 1976
---

![OLAP, whatâs coming next?](https://www.ssp.sh/blog/olap-whats-coming-next/images/cube_k_flach.jpg)

Contents

Are you on the lookout for a replacement for the Microsoft Analysis Cubes, are you looking for a big data OLAP system that scales ad libitum, do you want to have your analytics updated even real-time? In this blog, I want to show you possible solutions that are ready for the future and fits into existing data architecture.


## What is OLAP?


OLAP is an acronym for **Online Analytical Processing**. OLAP performs multidimensional analysis of business data and provides the capability for complex calculations, trend analysis, and sophisticated data modelling. An **[OLAP cube](https://en.wikipedia.org/wiki/OLAP_cube)** is a multidimensional database that is optimised for data warehouse and online analytical processing (OLAP) applications. An OLAP cube is a method of storing data in a multidimensional form, generally for reporting purposes. In OLAP cubes, data (measures) are categorised by dimensions. In order to manage and perform processes with an OLAP cube, Microsoft developed a query language, known as multidimensional expressions ([MDX](https://docs.microsoft.com/en-us/sql/analysis-services/multidimensional-models/mdx/mdx-query-fundamentals-analysis-services?view=sql-server-2017)), in the late 1990s.  Many other vendors of multidimensional databases have adopted MDX for querying data, but with this specific language, management of the cube requires personnel with the skill set.


## Why replace OLAP-Cubes?


As my job as a business intelligence specialist and data engineer, I was always using OLAP-Technologies for quick ad-hoc analysis with tools like Tableau, TARGIT, Power BI, Excel, etc. As the Microsoft BI stack is still used widely around in small to large companies, the technology for it is mostly SQL Server Analysis Services (SSAS) or Microsoft Cubes. **These are a compelling and fast way to aggregate and pre-calculate all of your corporate-related data and makes it available to your operational business users.** Nevertheless, these cubes are getting more and more to their limits as you might have experienced that in your own company. There are several problems I see or encountered:

- The multi-dimensional model of Analysis Services **are not supported in the Azure Cloud** and also does not look like it will soon (there is the tabular model of Microsoft cubes, but they still got some following limitations).
- **There is a limit to the size of data** it can process fast. It was developed a long time ago it is not optimised for the vast amount of data nowadays.
- Does not fit in the open-source and big data ecosystem due to:
- The **query language [MDX](https://en.wikipedia.org/wiki/MultiDimensional_eXpressions) is considerably hard to understand** and difficult to write more complex queries.


Therefore I was researching for alternatives on the world wide web. But before I go into more dept what I found, I want that you look at the architecture as a whole. **One reason is that nowadays are countless persons wish to make use of data, that’s why you might want to make it available to all of them** or at least have a more open architecture. In my opinion, Data Lake is the buzzword for it where everyone easily can access data instead of BI-Specialists only or worse, infrastructure guys having access to the FTP-Server.


To illustrate this I like the architecture from [DWBI1](https://dwbi1.wordpress.com/2018/09/06/modern-data-warehousing/), which shows the architecture as generic as possible:


[

](https://www.ssp.sh/blog/olap-whats-coming-next/images/bluegranite-diagram.jpg)Generic big data architecture


What you also see is the difference between corporate data that traditionally go into the Data Warehouse (DWH) and the real-time streaming data like social media, IoT that goes into the data lake. **As Data Lakes makes it easier to access data for data-savvy persons**, you should always keep in mind where you put which data. If you want to know more about that topic, read my other blog post about [DataWarehouse vs Data Lake](https://www.ssp.sh/blog/data-warehouse-vs-data-lake-etl-vs-elt/).


Back to the OLAP Cubes which would be on top of the Data Warehouse in the architecture above as *In-Memory-Models* or *Semantic Layer.* **You understand OLAP is still used for essential tasks as Data Exploration, Analytics and Self-Service BI**. I would say that Data Lakes are having not enough speed for any of these needs where speed and fast response time is critical in most organisations. On the other hand, Data Lakes are very beneficial for Data Scientists because they are interested in all the data without seconds query-response time. Therefore a Data Scientist can explore, analyse and run the machine learning models on top of the Data Lake very convenient.

**But what is coming up next now after, e.g. Microsoft Analysis Services?** In the following chapter, I show you the possible different technologies to replace it with a modern, scalable and fast replacements.


## List of Cube-Replacements


Because **you can make a one-to-one replacement, having a faster cloud-backend, virtualise a semantic layer or use a service cloud provider** I categorised the different technologies in the following groups.


### OLAP-Technologies

- [Apache Druid](https://en.wikipedia.org/wiki/Druid_%28open-source_data_store%29)
- [Click House](https://en.wikipedia.org/wiki/ClickHouse)
- [Pinot](https://github.com/linkedin/pinot/wiki)
- [Apache Kylin](https://en.wikipedia.org/wiki/Apache_Kylin)


With **OLAP-Technologies** you replace your cubes one to one with another technology. Therefore you don’t change anything on your current architecture but replace your cubes with a modern big data optimised technology which **focus on fastest query response time**. See the Appendix for a [comparison between modern OLAP Technologies](https://www.ssp.sh/blog/olap-whats-coming-next#Comparison_modern_OLAP_Technologies).


### Cloud Data Warehouses

- [Snowflake](https://www.snowflake.com/) (first fully cloud-based DWH, optimised for DWH and Analytics)
- [Google BigQuery](https://cloud.google.com/bigquery/)
- [Amazon Redshift](https://aws.amazon.com/redshift/)
- [Azure SQL Data Warehouse](https://azure.microsoft.com/en-us/services/sql-data-warehouse/)


Another approach is that you change your on-premise Data Warehouse to a **Cloud Data Warehouse** to get more scalability, more speed and better availability. This option is best suited for you if you do not necessarily need the fastest response time and you do not have tera- or petabytes of data. **The idea is to speed up your DWH and skip the layer of cubes. This way you save much time in development, processing and maintaining of cubes.** On the other hand, you lose in query latency while you create your dashboards. If you mainly have reports anyway, which can run beforehand, then this is perfect for you.


### Data Virtualisations

- [Dremio ](https://www.dremio.com/)â [Apache Arrow](https://arrow.apache.org/) in-memory Technology
- [Cisco Data Virtualisation](https://www.cisco.com/c/en/us/products/analytics-automation-software/data-virtualization/index.html) (previously called Composite Software)
- [Denodo Platform for Data Virtualisation](https://www.denodo.com/)
- [Informatica Data Virtualisation](https://www.informatica.com/products/data-integration/real-time-integration/data-virtualization.html)
- [IBM Big SQL](https://www.ibm.com/us-en/marketplace/big-sql)
- [Incorta](https://incorta.com/)


You may have many source system from different technologies, but all of them are rather fast in response time, and you don’t run a lot of operational applications, you might consider **Data Virtualisation**. In that way, **you don’t move and copy data around and pre-aggregate**, but you have a semantic middle layer where you create your business models (like cubes), and only if you query this data virtualisation layer it queries the data source. If you use, e.g. Dremio, there you use [Apache Arrow](https://arrow.apache.org/) technology which will cache and optimise a lot in-memory for you that you have as well astonishing fast response times.


### Serviced Cloud and Analytics

- [Looker](http://looker.com/) ([Use-case](https://inside.getyourguide.com/blog/2017/10/18/implementing-looker-at-getyourguide) where they replaced MS Analysis Cube with Looker)
- [Sisense](https://www.sisense.com/) ([ElastiCubes ](https://documentation.sisense.com/latest/managing-data/ElastiCubes.htm)Technology)
- [panoply.io](http://panoply.io/)


Last option is to buy a **Service Cloud Storage or Analytics** vendors like Looker, Sisense or Panoply. These are very easy to use and create implicit cubes for you, meaning you just join your data together in your semantic layer of the respective tool and all the rest is handled by the tool, including the reporting and dashboard tools. In this way your more depended on the individual vendor, it might also be more expensive (prices are always very in transparent and hard to get), but **you are very fast up and running**.


## Additional featured Tools


If you go one step further, let’s say you choose one of the above technologies, you will most probably run into the need to handle intermediate levels in between. For example to prepare, wrangle, clean, copy, etc. the data from one to another system or another format especially if your working with unstructured data as these need to be mingled in a structured way at the end in one or the other way. To keep the overview and handle all these challenging tasks, you need an **Orchestrator** and some **cloud-computing frameworks** which I will explain in the two following chapters to complete the full architecture.


## Orchestrators

- [Apache Airflow](https://airflow.apache.org/) (created in Airbnb)
- [Luigi](https://github.com/spotify/luigi) (created in Spotify)
- [Azkaban](https://azkaban.github.io/) (created in LinkedIn)
- [Apache Oozie](http://oozie.apache.org/) (for Hadoop systems)


After you choose your group and even your technology you want to go for, you want to have an Orchestrator. **This is one of the most critical tasks** that gets forgotten most of the time.


### What is a Orchestrator?


An orchestrator is a scheduling and monitor workflows tool. For the different technologies and different file format working together, you need some orchestrator and processing engine that prepares, moves and wrangle the data correctly and to the right place.


### Why would you need this?


As companies grow, their workflows become more complex, comprising of many processes with intricate dependencies that require increased monitoring, troubleshooting, and maintenance. **Without a clear sense of data lineage, accountability issues can arise, and operational metadata can be lost**. This is where these tools come into play with their [directed acyclic graphs (DAGs)](https://en.wikipedia.org/wiki/Directed_acyclic_graph), data pipelines, and workflow managers.


Complex workflows can be represented through DAGs. DAGs are graphs where information must travel between the vertices in a specific direction, but there is no way for information to travel through the graph in a loop that circles back to the starting point. **The building blocks of DAGs are data pipelines or following processes where the output from one process becomes the input for the next**. Building these pipelines can be tricky, but luckily there are several open-source workflow managers available, allowing programmers to focus on individual tasks and dependencies:


## Cluster-computing frameworks

- [Apache Spark](https://en.wikipedia.org/wiki/Apache_Spark) (â [Databricks ](https://databricks.com/)/ [Azure Databricks](https://azure.microsoft.com/en-us/services/databricks/) )
- [Apache Flink](https://flink.apache.org/) (main difference to Spark is that Flink was built from the ground up as a streaming product. Spark added Streaming onto their product later)
- [Dask](https://dask.org/) (distributed Python with API compatibility for pandas, numpy and scikit-learn).


To complete the list, we also need to address the computing frameworks mostly know for example Spark. Spark or Cluster-computing frameworks are **unified analytics engines for large-scale data processing which means you can wrangle, transform, clean, etc. your data at a large scale with a lot of parallelisation**. This can also be used and started within the above-mentioned orchestrator-tools.


## Conclusion


There is not only the right technology to choose it’s also critical to define your requirements and goals correctly that you want to achieve with your data ecosystem. Based on these definitions you are selecting the technology in the right category either a one-to-one OLAP replacement, a faster Cloud Data Warehouse backend, virtualised semantic layer or you use a Serviced Cloud Provider.


If you include the featured tools from the very beginning like the orchestrator or cloud-computing framework, then for sure you will have the perfect fit for your use-case that also survives the very near future.


Related Links:

- [Replace SSAS Cubes with Looker at GetYourGuide](https://inside.getyourguide.com/blog/2017/10/18/implementing-looker-at-getyourguide)
- [How Apache Druid enables analytics at Airbnb](https://medium.com/airbnb-engineering/druid-airbnb-data-platform-601c312f2a4c)
- [SQL Server 2019 including Big Data Clusters](https://www.jamesserra.com/archive/2018/10/sql-server-2019-big-data-clusters/)
- [Data Engineering, the future of Data Warehousing?](https://www.ssp.sh/blog/data-engineering-the-future-of-data-warehousing/)


## Appendix


### Comparison modern OLAP Technologies


---


```
Republished on LinkedIn and Medium.
```


## Comments


### Comment by Hugo Delgadinho on 2019-08-05 15:40


Thank you for your post, you gave an modern approach to replace Olap cubes but I think we can see this old features but with a modern vision, as explained in this article [[https://www.imaginarycloud.com/blog/oltp-vs-olap/](https://www.imaginarycloud.com/blog/oltp-vs-olap/)](https://www.imaginarycloud.com/blog/oltp-vs-olap/) .


### Comment by Wade on 2019-09-21 22:55


You left out tabular analysis services which is really good.


### Comment by Simon on 2019-09-23 11:45


Hi Wade, thanks for commenting. But actually under Why replace OLAP-Cubes, I stated that Tabular Cubes has similar problems or limitations as the Multidimensional. Search for âTabularâ and you’ll find it :-).

[Discuss on Bluesky](https://bsky.app/search?q=domain%3A%20https://www.ssp.sh/blog/olap-whats-coming-next/)
|
[Pay what you like](https://ko-fi.com/sspaeti)
|
[Big Data](https://www.ssp.sh/tags/big-data/)
[Cloud Data Warehouse](https://www.ssp.sh/tags/cloud-data-warehouse/)
[Cluster Computing](https://www.ssp.sh/tags/cluster-computing/)
[Data Architecture](https://www.ssp.sh/tags/data-architecture/)
[Data Science](https://www.ssp.sh/tags/data-science/)
[Data Pipelines](https://www.ssp.sh/tags/data-pipelines/)
[Olap](https://www.ssp.sh/tags/olap/)
