---
title: "Data Engineering, the future of Data Warehousing?"
date: 2018-03-08
url: https://www.ssp.sh/blog/data-engineering-the-future-of-data-warehousing/
slug: data-engineering-the-future-of-data-warehousing
word_count: 2671
---

![Data Engineering, the future of Data Warehousing?](https://www.ssp.sh/blog/data-engineering-the-future-of-data-warehousing/images/Data-Engineering-e1520539250268.jpg)

Contents

Today, there are 6,500 people on LinkedIn who call themselves data engineers according to [stitchdata.com](https://www.stitchdata.com/resources/reports/the-state-of-data-engineering/). In San Francisco alone, there are 6,600 job listings for this same title. The number of data engineers has doubled in the past year, but engineering leaders still find themselves faced with a significant shortage of data engineering talent. So is it really the future of data warehousing? What is data engineering? These questions and much more I want to answer in this blog post.


In [unicorn](https://en.wikipedia.org/wiki/Unicorn_(finance)) companies like Facebook, Google, Apple where data is the fuel for the company, mostly in America, is where data engineers are largely used. In Europe, the job title does not completely exist besides the startup mecca Berlin, Munich, etc. They are called or included in jobs like software engineer, big data engineer, business analyst, data analyst, data scientist and also the business intelligence engineer. Myself, I started as a business intelligence engineer and using more and more time on the engineering rather the business part, that’s why I am starting this blog from the data warehousing angle.


## What is a Data Warehouse?


What is data warehousing or what is a business intelligence engineer doing, and why are they using a data warehouse?


To use the analogy to a physical retail-type warehouse, **you want to sell very structured products in the most efficient way to your customers**. In a data warehouse (DWH) you have typically structured data and optimised them for business users to query. If you dig a little deeper, you offload data from the trucks in the back of the physical shop, before it gets sorted and structured into the warehouse for the customers to buy. In a DWH you basically do the same, just with data. As you see in the DWH architecture below, the offloading area in the back of the store is your [stage area](https://en.wikipedia.org/wiki/Staging_(data)) where you store the source data from your operational systems or external data.


![/blog/data-engineering-the-future-of-data-warehousing/images/DataWarehouse_Wiki_Architecture.jpg](https://www.ssp.sh/blog/data-engineering-the-future-of-data-warehousing/images/DataWarehouse_Wiki_Architecture.jpg)

*A traditional Data Warehouse architecture byWikipedia*


The physical warehouse where the customers buying the articles is in a DWH normally the so-called [data mart](https://en.wikipedia.org/wiki/Data_mart). The data processed between each layer seen in the architecture above is called [ETL (Extract Transform Load)](https://en.wikipedia.org/wiki/Extract,_transform,_load). This is not to confuse with [ELT (Extract Load Transform)](https://en.wikipedia.org/wiki/Extract,_load,_transform) which is the common mythology data lakes (more in my recent [post](https://www.ssp.sh/blog/data-warehouse-vs-data-lake-etl-vs-elt/)). In a DWH you always transform to get data as clean and structured as possible.


### Why having a Data Warehouse?


Besides the obvious reasons of a shop explained above, a data warehouse gives you big advantages:

- In theory: **Integration** and **transformation** of raw data of an organisation **from multiple** sources (mostly very structured like SAP, CRM, Excel, etc.) into meaningful and **useful information, historical stored**.
- In practice: Similar **a cockpit in an aeroplane** - All Measures and [KPI’](https://en.wikipedia.org/wiki/Performance_indicator)s are at one place in order to steer the plane and take the right decisions
- It allows businesses to make **better decisions** by accessing the data well structured
- The visual products from business intelligence based on top of a data warehouses are largely:


## What is Data Engineering?


Data engineering is the less famous sibling of data science. Data science is growing like no tomorrow and so does data engineer, but much less heard. Compared to existing roles it would be a **software engineering plus business intelligence engineer including big data abilities** as the Hadoop ecosystem, streaming and computation at scale. Business creates more reporting artefacts themselves but with more data that needs to be collected, cleaned and updated near real-time and complexity is expanding every day. With that said more programmatic skills are needed similar to software engineering. **The emerging language at the moment is Python** (more in the chapter [below](https://www.ssp.sh/blog/data-engineering-the-future-of-data-warehousing#ThetoollanguagePython)) while used in engineering with tools alike Apache Airflow as well as data science with powerful libraries. Where today as a BI-engineer you use [SQL](https://en.wikipedia.org/wiki/SQL) for almost everything except when using external data from an FTP-server for example. You would use bash and PowerShell in the nightly batch jobs. But this is no longer sufficient and because it gets a full-time job to develop and maintain all these requirement and rules (called pipelines), the data engineering is needed.


## The role of a data engineer


In order to get high quality and **frequently updated data sets**, it is important to distinguish between data pipelines that are **done and cleaned** by data engineers and all the others that are mostly exploratory. We at Airbus use a folder that is called “cleaned” and all data sets produced there are constantly updated, documented and of the highest quality. Based on these data sets you create your own. We use the data lake solution [Palantir Foundry](https://en.wikipedia.org/wiki/Palantir_Technologies) (brand name of Airbus: [Skywise](http://www.airbus.com/newsroom/press-releases/en/2017/06/airbus-launches-new-open-aviation-data-platform--skywise--to-sup.html)) which provides you with a map where you see the [data lineage](https://en.wikipedia.org/wiki/Data_lineage) easily. **Documentation and metadata to each data set are crucial** as otherwise, you lose the overview of your data, which is also one main task of a data engineer.


### Services that a data engineer provides


Another important task or **service which a data engineer provides is automation** that data scientists or data analysts do manually. A good overview what task this includes are provided by [Maxime Beauchemin](https://medium.com/@maximebeauchemin), the founder of [Apache Airflow](https://airflow.apache.org/), a tool that helps a data engineer to lift the majority of tasked mentioned:

- “**data ingestion**: services and tooling around “scraping” databases, **loading logs, fetching data from external stores or APIs**, …
- **metric computation**: frameworks to compute and summarise engagement, **growth or segmentation related metrics**
- **anomaly detection**: automating data consumption to **alert people anomalous events occur** or when trends are changing significantly
- **metadata management**: tooling around allowing generation and consumption of metadata, making it easy to find information in and around the data warehouse
- **experimentation: A/B testing** and experimentation frameworks is often a critical piece of company’s analytics with a significant data engineering component to it
- **instrumentation**: **analytics starts with logging events** and attributes related to those events, data engineers have vested interests in making sure that high-quality data is captured upstream
- **dependencies**: **pipelines that are specialized in understand series of actions** in time, allowing analysts to understand user behaviours"


> While the nature of the workflows that can be automated differs depending on the environment, the need to automate them is common across the board. By Maxime Beauchemin


## When is a data engineer needed?


I believe, that **not every company is in need of data engineers**. His skills are mostly required if the company either:

- has already a product that is fully web-based and therefore data-driven or
- the need or desire to analyse lots of data (Volume) from any kind of sources (Variety) and fast (Velocity) to get the insights (Value and Veracity) (see more about the [five V’s of Big Data](https://miuc.org/vs-big-data/))


## Data engineer job description and skills


If English is the language of business, SQL is the language of data and Python the language of engineering. While technology disappears often, SQL is still here. This means you need a reliable understanding of:

- **SQL to a high level of complexity**
- **Data modelling techniques:** [ERD](https://en.wikipedia.org/wiki/Entity%E2%80%93relationship_model)s and dimensional modelling
- Solid [ETL](https://en.wikipedia.org/wiki/Extract,_transform,_load) **understanding**
- Architectural projections: needs to have a **high-level understanding of most of the tools, platforms, libraries and other resources** at its disposal
- able to connect the dots from source to destination with any **programming language** that does the job best. (Probably Python at the moment)


[Stitchdata.com](https://www.stitchdata.com/resources/reports/the-state-of-data-engineering/) anticipated that as company size increased, so would the focus on scaling-related skill. However, that’s not the story the data told. Instead, data engineers at **larger companies tend to be more focused on “enterprise” skills like ETL, BI, and data warehousing, whereas data engineers at smaller companies focus more on core technologies**:


![/blog/data-engineering-the-future-of-data-warehousing/images/Skill_Differences_of_DataEngineers.jpg](https://www.ssp.sh/blog/data-engineering-the-future-of-data-warehousing/images/Skill_Differences_of_DataEngineers.jpg)

*Skill differences of data engineers across company sizes*


## The tool language, Python


### The growth of major programming languages


Programming languages have always come and gone, but in the last couple of years, Python rises on top of the popularity. The question is why. One valid reason for sure is because of the rise of the data engineers but also the use of libraries for data science and data analytics.


![/blog/data-engineering-the-future-of-data-warehousing/images/Python_The_rise_of_major_programming_languages.jpg](https://www.ssp.sh/blog/data-engineering-the-future-of-data-warehousing/images/Python_The_rise_of_major_programming_languages.jpg)

*Trends programming languages on StackOverflow*


According to the [Codeacademy](http://codecademy.com) and their source data from [Stack Overflow](https://stackoverflow.blog/2017/09/06/incredible-growth-python/), they say it’s connected to the rise of data science. This and [machine learning](https://en.wikipedia.org/wiki/Machine_learning) were the biggest trends in tech 2017. Additionally, Python has become a go-to language for data analysis. With data-focused libraries like pandas, NumPy, and matplotlib, anyone familiar with Python’s syntax and rules can deploy it as a powerful tool to process, manipulate, and visualise data.


Related to the rise of data science and data engineering, it’s clear to me that Python is here to stay and it’s becoming the **Swiss Army Knife of programming languages**.


### Python for data engineers


But for what can you use Python in data engineering. For example, **you use it for data wrangling** (reshaping, aggregating, joining disparate sources, etc.) which mostly done with the library [Pandas](https://en.wikipedia.org/wiki/Pandas_(software)), small-scale ETL, API interaction (our presentation usually happens in Tableau which has Python APIs) and automation with [Apache Airflow](https://airflow.apache.org/), which is also natively in Python.


“*Apache Airflow has several building blocks that allow Data Engineers to easily piece together pipelines to and from different sources. Because it is written in Python, Data Engineers find it easy to create ETL pipelines by just extending classes of Airflow’s DAG and Operator objects. And this allows us to write our own Python code to create any ETL we wish, with the structure given by Airflow. Airflow uses several packages mentioned all ready to do the job: [boto](http://boto.cloudhackers.com/en/latest/) for S3 handling, pandas for obvious advantages with data frames, psycopg2 for popular integrations with Postgres and Redshift, and several more.*” said by [David Dalisay](https://www.quora.com/profile/David-Dalisay).


## Facebook data engineer


According to a job description as a [data engineer](https://www.facebook.com/careers/jobs/) at Facebook in Menlo Park in Seattle, he needs to have the following qualification and responsibilities.


**Minimum Qualifications**

- 2+ years of Java and/or Python development experience
- 2+ years of SQL (Oracle, Vertica, Hive, etc.) experience
- 2+ years of LAMP stack development experience
- 2+ years of experience in custom or structured (i.e. Informatica/Talend/Pentaho) ETL design, implementation and maintenance
- Experience working with either a MapReduce or an MPP system on any size/scale.


**Responsibilities**

- Build data expertise and own data quality for the awesome pipelines you build
- Architect, build and launch new data models that provide intuitive analytics to your customers
- Design, build and launch extremely efficient & reliable data pipelines to move data (both large and small amounts) to our ridiculously large Data Warehouse
- Design and develop new systems and tools to enable folks to consume and understand data faster
- Use your expert coding skills across a number of languages from Python, Java and PHP
- You have developed applications within the LAMP Stack environment
- Work across multiple teams in high visibility roles and own the solution end-to-end


![/blog/data-engineering-the-future-of-data-warehousing/images/DataEngineer_Persona.jpg](https://www.ssp.sh/blog/data-engineering-the-future-of-data-warehousing/images/DataEngineer_Persona.jpg)

*A picture of such a persona could look like (quora.com)*


## Data Engineer Salary


The salary of a data engineer is hard to say as it is very new, especially in Switzerland where the following salary-report is from. But on the following table you see all the jobs that are related or close by (unfortunately only in German, sorry for that) and their salary for a full year ins Swiss Francs (CHF) created by [Robert Half.ch](https://www.roberthalf.ch/de/gehalt):


![/blog/data-engineering-the-future-of-data-warehousing/images/DataEngineer_SalaryReport_RobertHalf.jpg](https://www.ssp.sh/blog/data-engineering-the-future-of-data-warehousing/images/DataEngineer_SalaryReport_RobertHalf.jpg)

*Salaray Overview in Switzerland*


## Business Intelligence Engineer vs Data Engineer


As already mentioned in further up, the data engineer has the skillset of a business intelligence engineer plus also solid programming and big data skills. I believe BI-engineers will transit over to a data engineer anyway, depending on the size of a company. But why? What is changing/has changed?


### What has changed


As the power of computers and especially the speed of the internet is growing, more data can be collected and needs to be analysed. Therefore many parameters around the data warehouse environment have or will change. Below the points that I see with most influence:

- Computer get faster and **reports can be built directly on source data**, no persistent layer needed for performance optimisation, a semantic layer is enough
- **Business has not the time to wait for ETL** to be finished during the night, data needs to show immediately (almost real-time)
- Structure needs to put in place after you collect data ([ELT instead of ETL](https://www.ssp.sh/blog/data-warehouse-vs-data-lake-etl-vs-elt/)).
- Easy collaboration and exchange of data is needed
- **Governance getting more important as more data is stored** in order to have the full overview of the data, timeframe and quality
- New trends, tools, technologies and competitors are arising all the time, companies must be on top of that


#### ETL is changing


Furthermore the way we do ETL is changing as well, as [Maxime Beauchemin](https://medium.com/@maximebeauchemin), data engineer at Airbnb quotes: “*Product know-how on **platforms like Informatica, IBM Datastage, Cognos, AbInitio or Microsoft SSIS isn’t common amongst modern data engineers**, and being replaced by more generic software engineering skills along with understanding of programmatic or configuration driven platforms like Airflow, Oozie, Azkabhan or Luigi. It’s also fairly common for engineers to develop and manage their own job orchestrator/scheduler.*” He is also saying that **code is the best abstraction there is for software** rather than using drag and drop tools (ETL-tools). Most important what I see as well, that the **transformation logic is of a higher need and shouldn’t be locked away exclusively for BI developers**.


#### Data Modelling is changing


As you can’t change ETL without modelling differently, also this is changing:

- **Further** [denormalisation](https://en.wikipedia.org/wiki/Denormalization) for performance gains is mostly compensated with faster databases engines or cloud solutions.
- **Maintaining** [surrogate keys](http://www.kimballgroup.com/1998/05/surrogate-keys/) in dimensions can be tricky and not human-friendly as we prefer business keys.
- With the popularity of document storage and cheap blobs in cloud storage, it is becoming easier to create and develop database **schemas dynamically** without writing [DML-statements](https://en.wikipedia.org/wiki/Data_manipulation_language).
- Systematically **snapshoting** dimension compared to handle complex and maybe contra-intuitive [slowly changing dimension (SCD)](https://en.wikipedia.org/wiki/Slowly_changing_dimension) is a way to **simplify track changes** in a DWH. Is it also easy and relatively cheap to denormalise dimension’s attribute directly on the fact table to keep important information at the moment of the transaction.
- [Conformed dimensions](http://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/conformed-dimension/) and **conformance** as in general is extremely important in nowadays data warehouse and data environments. But **to be more collaborative and work on same objects it is a necessary trade-off to loosen it up**.
- Not only more working on the same project within data warehousing, also more people from business and other departments **getting more data-savvy than ever before**. In that sense data needs to get more real-time rather than batch processing and precompute calculations, this can be done more ad-hoc with new fast technologies like Spark that **ran complex jobs ad-hoc** and on-demand.


#### Education is changing


Facebook, Airbnb and other companies taking it a step into so-called “Data Camps or Data University” to educate internal employees in respect of data to get more data savvy.


## Conclusion


So after all, is the data engineer the new business intelligence engineer? I would say in the long run yes. I imagine that data warehouses - in any way - will always be a need for the business, where the data is fully structured and easily accessible. But how we build DWHs or a similar type, will change and therefore more engineering and data engineers, are needed.


---


```
Republished on LinkedIn and Hacker Noon.
```


## Comments


### Comment by Global Tech Council on 2021-01-02 11:16


Thanks for the detailed blog. The blog consists of informational content about the topic. I really appreciate the blog post of posting such and valuable content.

[Discuss on Bluesky](https://bsky.app/search?q=domain%3A%20https://www.ssp.sh/blog/data-engineering-the-future-of-data-warehousing/)
|
[Pay what you like](https://ko-fi.com/sspaeti)
|
[Business-Intelligence](https://www.ssp.sh/tags/business-intelligence/)
[Big Data](https://www.ssp.sh/tags/big-data/)
[Data Engineer](https://www.ssp.sh/tags/data-engineer/)
[Data Science](https://www.ssp.sh/tags/data-science/)
[ELT](https://www.ssp.sh/tags/elt/)
[ETL](https://www.ssp.sh/tags/etl/)
[Python](https://www.ssp.sh/tags/python/)
