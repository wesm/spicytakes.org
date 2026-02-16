---
title: "Open-Source Data Warehousing â Druid, Apache Airflow & Superset"
date: 2018-11-29
url: https://www.ssp.sh/blog/open-source-data-warehousing-druid-airflow-superset/
slug: open-source-data-warehousing-druid-airflow-superset
word_count: 1262
---

![Open-Source Data Warehousing â Druid, Apache Airflow & Superset](https://www.ssp.sh/blog/open-source-data-warehousing-druid-airflow-superset/images/Druid_Airflow_Superset.png)

Contents

These days, everyone talks about open-source. However, this is still not common in the Data Warehouse (DWH) field. Why is this?


In my recent blog, I researched [OLAP technologies](https://www.ssp.sh/blog/olap-whats-coming-next/), for this post I chose some open-source technologies and used them together to build a full data architecture for a Data Warehouse system.


I went with [Apache Druid](http://www.druid.io) for data storage, [Apache Superset](https://superset.incubator.apache.org/) for querying and [Apache Airflow](https://airflow.apache.org/) as a task orchestrator.


## Druid - the data store


Druid is an **open-source**, **column-oriented**, **distributed data store** written in Java. It’s designed to **quickly ingest** massive quantities of event data, and **provide low-latency queries** on top of the data.


![/blog/open-source-data-warehousing-druid-airflow-superset/images/Druid-what-is-it.png](https://www.ssp.sh/blog/open-source-data-warehousing-druid-airflow-superset/images/Druid-what-is-it.png)

*Whatdruid.iois*


### Why Druid?


Druid has many **key features**, including sub-second **OLAP queries, real-time streaming ingestion, scalability, and cost-effectiveness**.


With theÂ [comparison of modern OLAP Technologies](https://www.ssp.sh/blog/olap-whats-coming-next/#comparison-modern-olap-technologies)Â in mind, I chose Druid over ClickHouse, Pinot and Apache Kylin. Recently,Â [Microsoft announced they will add Druid](https://azure.microsoft.com/en-us/blog/azure-hdinsight-brings-next-generation-hadoop-3-0-and-enterprise-security-to-the-cloud/?source=post_page---------------------------)Â to their Azure HDInsight 4.0.


### Why not Druid?


Carter Shanklin wroteÂ [a detailed post about Druidâs limitations](https://blog.cloudera.com/apache-hive-druid-part-1-3/)Â at Horthonwork.com. The main issue is with its support for SQL joins, and advanced SQL capabilities.


### The Architecture of Druid


Druid is scalable due to its cluster architecture. You have three different node types â **the Middle-Manager-Node, the Historical Node and the Broker**.


The great thing is that you can add as many nodes as you want in the specific area that fits best for you. If you have many queries to run, you can add more Brokers. Or, if a lot of data needs to be batch-ingested, you would add middle managers and so on.


A simple architecture is shown below. You can read more about Druidâs designÂ [here](http://druid.io/docs/latest/design/?source=post_page---------------------------).


![/blog/open-source-data-warehousing-druid-airflow-superset/images/Druid-Architecture.png](https://www.ssp.sh/blog/open-source-data-warehousing-druid-airflow-superset/images/Druid-Architecture.png)

*Druid Architecture from AirBnB posted onMedium*


## Apache Superset â the UI


The easiest way to query against Druid is through a lightweight, open-source tool calledÂ [Apache Superset](https://superset.incubator.apache.org/?source=post_page---------------------------). It is easy to use and has all common chart types like Bubble Chart, Word Count, Heatmaps, Boxplot andÂ [many more](https://superset.incubator.apache.org/gallery.html?source=post_page---------------------------).


Druid provides a Rest-API, and in the newest version also a SQL Query API. This makes it easy to use with any tool, whether it is standard SQL, any existing BI-tool or a custom application.


## Apache Airflow - the Orchestrator


As mentioned inÂ [Orchestrators â Scheduling and monitor workflows](https://www.ssp.sh/blog/olap-whats-coming-next/?source=post_page---------------------------#Orchestrators), this is one of the most critical decisions.


In the past, ETL tools like Microsoft SQL Server Integration Services (SSIS) and others were widely used. They were where your data transformation, cleaning and normalisation took place.


In more modern architectures, these tools arenât enough anymore. Moreover, code and data transformation logic are much more valuable to other data-savvy people in the company.


I highly recommend you read a blog post fromÂ [Maxime Beauchemin](https://medium.com/@maximebeauchemin?source=post_page---------------------------)Â aboutÂ [Functional Data Engineering â a modern paradigm for batch data processing](https://medium.com/@maximebeauchemin/functional-data-engineering-a-modern-paradigm-for-batch-data-processing-2327ec32c42a?source=post_page---------------------------). This goes much deeper into how modern data pipelines should be.


### Why using Airflow?


[Apache Airflow](https://airflow.apache.org/?source=post_page---------------------------)Â is a very popular tool for this task orchestration. Airflow is written in Python. Tasks are written as Directed Acyclic Graphs ([DAGs](https://en.wikipedia.org/wiki/Directed_acyclic_graph?source=post_page---------------------------)). These are also written in Python.


Instead of encapsulating your critical transformation logic somewhere in a tool, you place it where it belongs to inside the Orchestrator.


Another advantage is using plain Python. There is no need to encapsulate other dependencies or requirements, like fetching from an FTP, copying data from A to B, writing a batch-file. You do that and everything else in the same place.


### Features of Airflow


Moreover, you get a fully functional overview of all current tasks in one place.


![](https://www.ssp.sh/blog/open-source-data-warehousing-druid-airflow-superset/images/airflow.gif)

*Functionalities of Apache Airflow*


More relevant features of Airflow are that you write workflows as if you are writing programs. External jobs like Databricks, Spark, etc. are no problems.


Job testing goes through Airflow itself. That includes passing parameters to other jobs downstream or verifying what is running on Airflow and seeing the actual code. The log files and other meta-data are accessible through the web GUI.


(Re)run only on parts of the workflow and dependent tasks is a crucial feature which comes out of the box when you create your workflows with Airflow. The jobs/tasks are run in a context, the scheduler passes in the necessary details plus the work gets distributed across your cluster at the task level, not at the DAG level.


For many more feature visit theÂ [full list](https://gtoonstra.github.io/etl-with-airflow/great.html?source=post_page---------------------------).


## ETL with Apache Airflow


If you want to start with Apache Airflow as your new ETL-tool, please start with thisÂ [ETL best practices with Airflow](https://gtoonstra.github.io/etl-with-airflow/)Â shared with you. It has examples simple [ETL](https://gtoonstra.github.io/etl-with-airflow/etlexample.html)-examples, with plain SQL, with [HIVE](https://gtoonstra.github.io/etl-with-airflow/hiveexample.html), withÂ [Data Vault](https://gtoonstra.github.io/etl-with-airflow/datavault.html),Â [Data Vault 2](https://gtoonstra.github.io/etl-with-airflow/datavault2.html),Â [Data Vault with Big Data processes](https://gtoonstra.github.io/etl-with-airflow/datavault-bigdata.html). It gives you an excellent overview of what’s possible and also how you would approach it.


At the same time, there is a Docker container that you can use, meaning you don’t even have to set-up any infrastructure, pull the container from [here](https://gtoonstra.github.io/etl-with-airflow/etlexample.html#run-airflow-from-docker).


For the GitHub-repo follow the link onÂ [etl-with-airflow](https://github.com/gtoonstra/etl-with-airflow).


## Conclusion


If youâre searching for open-source data architecture, you cannot ignore Druid for speedy OLAP responses, Apache Airflow as an orchestrator that keeps your data lineage and schedules in line, plus an easy to use dashboard tool like Apache Superset.


My experience so far is that Druid is bloody fast and a perfect fit forÂ [OLAP cube replacements](https://medium.com/@sspaeti/olap-whats-coming-next-be01c1567b87?source=post_page---------------------------)Â in a traditional way, but still needs a more relaxed startup to install clusters, ingest data, view logs etc. If you need that, have a look atÂ [Impy](https://imply.io/?source=post_page---------------------------)Â which was created by the founders of Druid. It creates all the services around Druid that you need. Unfortunately, though, itâs not open-source.


Apache Airflow and its features as an orchestrator are something which has not happened much yet in traditional Business Intelligence environments. I believe this change comes very naturally when you start using open-source and more new technologies.


And Apache Superset is an easy and fast way to be up and running and showing data from Druid. There for better tools like Tableau, etc., but not for free. Thatâs why Superset fits well in the ecosystem if youâre already using the above open-source technologies. But as an enterprise company, you might want to spend some money in that category because that is what the users can see at the end of the day.


Related Links:

- [Understanding Apache Airflowâs keyÂ concepts](https://medium.com/@dustinstansbury/understanding-apache-airflows-key-concepts-a96efed52b1a)
- [How Druid enables analytics at Airbnb](https://medium.com/airbnb-engineering/druid-airbnb-data-platform-601c312f2a4c)
- [Google launches Cloud Composer, a new workflow automation tool for developers](https://techcrunch.com/2018/05/01/google-launches-cloud-composer-a-new-workflow-automation-tool-for-developers/)
- [A fully managed workflow orchestration service built on Apache Airflow](https://cloud.google.com/composer/)
- [Integrating Apache Airflow and Databricks: Building ETL pipelines with Apache Spark](https://databricks.com/blog/2016/12/08/integrating-apache-airflow-databricks-building-etl-pipelines-apache-spark.html)
- [ETL with Apache Airflow](https://gtoonstra.github.io/etl-with-airflow/)
- [What is Data Engineering and the future of Data Warehousing](https://www.ssp.sh/blog/data-engineering-the-future-of-data-warehousing/)
- [Imply - Managed Druid platform (closed-source)](https://imply.io/)
- [Ultra-fast OLAP Analytics with Apache Hive and Druid](https://de.hortonworks.com/blog/apache-hive-druid-part-1-3/)

/wp:core-embed/twitter

---


```
Republished on LinkedIn, freeCodeCamp and Medium.
```


## Comments


### Comment by Kaibo Hao on 2019-02-25 09:01


This is a great article for the combination of the 3 open source projects. This is what I am looking for. Thanks for your help. : )


### Comment by Simon on 2019-02-27 19:58


Thank you Kabio Hao, I’m glad it helped you. Let me know what you think in case you going to use it as well.


### Comment by dougfoo on 2020-08-29 07:53


Love the articles on how to assemble the # of options out there today. How is Presto used in the arch here?

[Discuss on Bluesky](https://bsky.app/search?q=domain%3A%20https://www.ssp.sh/blog/open-source-data-warehousing-druid-airflow-superset/)
|
[Pay what you like](https://ko-fi.com/sspaeti)
|
[Airflow](https://www.ssp.sh/tags/airflow/)
[Big Data](https://www.ssp.sh/tags/big-data/)
[Druid](https://www.ssp.sh/tags/druid/)
[Olap](https://www.ssp.sh/tags/olap/)
[Superset](https://www.ssp.sh/tags/superset/)
