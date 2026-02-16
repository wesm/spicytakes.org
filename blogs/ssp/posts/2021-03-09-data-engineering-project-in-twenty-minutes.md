---
title: "Building a Data Engineering Project in 20 Minutes"
date: 2021-03-09
url: https://www.ssp.sh/blog/data-engineering-project-in-twenty-minutes/
slug: data-engineering-project-in-twenty-minutes
word_count: 4522
---

![Building a Data Engineering Project in 20 Minutes](https://www.ssp.sh/blog/data-engineering-project-in-twenty-minutes/images/open-source-logos.png)

Contents
Project Updates on 2024-03-17

After three years, recognizing the evolving landscape of data engineering tools and the ongoing relevance of this project, I’ve made several updates to [Practical Data Engineering](https://github.com/ssp-data/practical-data-engineering/). Key changes include updating components like Dagster and Delta Lake, removing Spark in favor of using Delta-rs directly, to streamline local development and simplify the architecture. For those interested in the original architecture, the [v1 branch](https://github.com/ssp-data/practical-data-engineering/tree/v1) preserves the initial setup.


I also added a quick [YouTube Video](https://youtu.be/FfDOsgg2EEQ) that shows you how to install and run.


This post focuses on practical data pipelines with examples from web-scraping real-estates, uploading them to S3 with [MinIO](https://min.io/), [Spark](https://spark.apache.org/) and [Delta Lake](https://delta.io/), adding some Data Science magic with [Jupyter Notebooks](https://jupyter.org/), ingesting into Data Warehouse [Apache Druid](https://druid.apache.org/), visualising dashboards with [Superset](https://superset.apache.org/) and managing everything with [Dagster](https://dagster.io/).


The goal is to touch on the common data engineering challenges and using promising new technologies, tools or frameworks, which most of them I wrote about in [Business Intelligence meets Data Engineering with Emerging Technologies](https://www.ssp.sh/blog/business-intelligence-meets-data-engineering/). As well everything runs on Kubernetes in a scalable fashion but as well locally with Kubernetes on [Docker Desktop](https://www.docker.com/products/docker-desktop).


The source-code you can find on [practical-data-engineering](https://github.com/ssp-data/practical-data-engineering) for the data pipeline or in [data-engineering-devops](https://github.com/ssp-data/data-engineering-devops) with all it’s details to set things up. Although not all is finished, you can observe the current status of the project on [real-estate-project](https://github.com/orgs/ssp-data/projects/1).


## What are we building, and why?


A data application that will collect real-estates coupled with Google maps way calculation but potential other macro or microeconomics like taxes, the population of city, schools, public transportation. Enriched with machine learning correlations to know factors that influence the price the most.


Why this project? When I started in 2018, I wanted to find the next best flat to rent but there was no sophisticated real-estate-portal out there in Switzerland. I found this very entertaining post about [Datamining a Flat in Munich](https://funnybretzel.com/datamining-a-flat-in-munich/) and wanted to code my own. Presently there are tons of services like [PriceHubble](https://www.pricehubble.com/en/) in Switzerland or [Zillow](https://www.zillow.com/) in the US, but still, it’s worthwhile to optimise for finding your dream apartment or house. On top of it, it is a genuine example that includes enough data engineering challenges.


Starting with web scraping gives you the power to treat every website as a database. We download the latest properties or those who have changed with a change data capture (CDC) mechanism. Zipping and uploading them to S3. With a Delta Lake table, we merge new changes with [schema evolution](https://databricks.com/blog/2019/09/24/diving-into-delta-lake-schema-enforcement-evolution.html). From there we add some machine learning and data science magic with Jupyter notebooks. Ingest it into the Druid data warehouse. Presenting the data in a business intelligence dashboarding manner. All of it is tied together with a well-suited orchestrator. And of course, everything is running cloud-agnostic anywhere, with [Kubernetes](https://kubernetes.io/). A gist of how the pipeline will look like as of today you see below.


![/blog/data-engineering-project-in-twenty-minutes/images/Dagster-Practical-Data-Engineering-Pipeline.png](https://www.ssp.sh/blog/data-engineering-project-in-twenty-minutes/images/Dagster-Practical-Data-Engineering-Pipeline.png)

*Dagster UI â Practical Data Engineering Pipeline*


## 💡 What will you learn?


Below I noted the key learnings which are integrated into a full-fledged data engineering project to illustrate the how part in the most hands-on way. Hopefully, you’ll find something interesting for you!

- **Scraping with Beautiful Soup**: How to get value out from a website with basic Python skills.
- **Change Data Capture (CDC) with Scraping**: Using a fingerprint to verify against the data lake if a property needs to be downloaded or not.
- **How to use an S3-Gateway / Object Storage**: Placing an S3 API in front of your object storage in the so-called âgateway-modeâ to stay cloud-agnostic. This allows you to change the object-store from Amazon S3 to Azure blob storage or Google cloud storage with ease.
- **UPSERTs and ACID Transactions**: Besides schema evolution mentioned above, Delta Lake also provides merge, update and delete directly on your distributed files.
- **Automatic Schema Evolution**: With the growing popularity of data lakes and [ELT](https://www.ssp.sh/blog/data-warehouse-vs-data-lake-etl-vs-elt/#ETL_vs_ELT), data engineers are left with lots of data but no schemas. To integrate schema and especially schema changes, automatic schema evolution is important.
- **Integrating Jupyter Notebooks - the right way**: Notebooks hold important data transformations, calculations or machine learning models yet it’s always hard to copy the living code in your data pipelines. We will integrate notebooks as a step of our pipeline with Dagster.
- **Learning about Apache Druid**: Druid is one of the fastest Data Warehouse / OLAP Solutions. It’s optimized for fast real-time ingestion and immutable data. On the downside, it’s hard to set up, luckily, below you see how to do exactly that.
- **Open-Source dashboarding with Apache Superset**: How to use Superset with its many out-of-box connections. On top, it’s free of charge compared to Tableau, Looker and others.
- **DevOps with Kubernetes**: How to run Kubernetes locally and install all of the tools here. If you haven’t used Kubernetes, don’t worry, examples and local set-up with Kubernetes for Docker are included.
- **Introduction to features of Dagster**: Showing how all of the data engineering parts can be tided together with one open-sourced tool called Dagster ([alternative to Airflow](https://qr.ae/pNrIPi)).
- And many more which I won’t mention but you’ll hopefully see along the way.


## Hands-On with Tech, Tools and Frameworks


In an earlier post about [Open-Source Data Warehousing](https://www.ssp.sh/blog/open-source-data-warehousing-druid-airflow-superset/), I focused explicitly on Apache Druid, Airflow and Superset. This post is all about using data engineering in a practical example. To give you an overview of what we use, I extended the tech, tools and frameworks I used in these blog post on top of the newer Databricks [Lakehouse Paradigm](http://cidrdb.org/cidr2021/papers/cidr2021_paper17.pdf).


![/blog/data-engineering-project-in-twenty-minutes/images/lakehouse-open-sourced.png](https://www.ssp.sh/blog/data-engineering-project-in-twenty-minutes/images/lakehouse-open-sourced.png)

*Databricks Lakehouse Paradigm with used Open-Source Technologies added*


Below you’ll find different chapters for different topics. I included at least one practical example with some hands-on code but kept it minimalistic as the source code is all open in the above-mentioned [repositories](http://code.sspaeti.com).Â Some chapters include extra information or architectural reasoning of why I believed a certain tool or method is especially suited for the use-case. But let’s get started with scraping data implemented with Python.


### Getting the Data â Scraping

Disclaimer
Everything shown here is demonstrated for learning purposes only. Before you begin, make sure you donât violate the copyright of any website and always
[be friendly](https://www.zyte.com/learn/web-scraping-best-practices)
when scraping.

The internet has an infinite amount of information, thatâs why scraping is valuable to know even though less know for data engineers. As a first step, we are getting the properties from a real-estate portal. In my case, I chose a Swiss portal, but you can choose anyone from your country. There are two main Python libraries to achieve this, [Scrapy](https://scrapy.org/) and [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/). I used the latter for its simplicity.


My initial goal was to scrape some properties from the web-page by determining how many search page result I get and scrape through each property from each page. While testing around with BeautifulSoup and [IPython](https://ipython.readthedocs.io/en/stable/)âââIPython is an excellent way to initially test your codeâââand asking my way through StackOverflow. I found that certain websites provide open APIs which you find in the documentation of their website or with the interactive developer tools (F12) explained below. This will save you from scraping everything manually and therefore also producing less traffic on the site of the provider.

How to check open APIs

If you want to check if another website has an open API, you can search for an HTTP request by simply clicking F12 and switching to the network tab to check requests that your browser send when clicking on a property.


![/blog/data-engineering-project-in-twenty-minutes/images/web-scraping-api_anomised.png](images/web-scraping-api_anomised.png)

*An example with Webbrowser Brave (Chrome like)*


To get started with web-scraping, it helps when you know some [basic HTML](https://www.w3schools.com/html/html_basic.asp). To get an overview of the site you would like to scrape your data from, use the above interactive developer tools. You can now inspect in which `<table>`, `<div>` or `id`, `class` or `href` your information is found. Most websites with valuable data have ever-changing idâs or classes, which makes it a bit harder to just grab the specific data you need.


Letâs say we want to buy a house in Bern, the capital of Switzerland. We can e.g. use this URL with this search term: [[https://www.immoscout24.ch/en/house/buy/city-bern?r=7↦=1](https://www.immoscout24.ch/en/house/buy/city-bern?r=7&map=1)](https://www.immoscout24.ch/en/house/buy/city-bern?r=7&map=1). R, in this case, is the radius around Bern and map=1 mean we only want properties with a price tag. As mentioned we need to find out how many pages of result we have. We can see this information is at the very bottom. A hacky example that worked for me is I searched all buttons on the page and chose the one smaller and equal three which equals me as the last page number two as of today.Â An example code to scrape how many pages of search results we have:



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
` | `from bs4 import BeautifulSoup
import requests

url = 'https://www.immoscout24.ch/en/house/buy/city-bern?r=7&map=1'

html = requests.get(url)
soup = BeautifulSoup(html.text, "html.parser")
buttons = soup.findAll('button')

p = []
for item in buttons:
    if len(item.text) <= 3 & len(item.text) != 0:
        print(item)
        p.append(item.text)
if p:
    lastPage = int(p.pop())
else:
    lastPage = 1

print(lastPage)

## -- Output --
<button aria-disabled="true" aria-pressed="true" class="bkivry-0 as6woy-0 c2ol4x-0 hXMMbP" disabled="" type="button">1</button>
<button aria-disabled="true" class="bkivry-0 as6woy-0 c2ol4x-0 hXMMbP" disabled="" type="button">2</button>
2
` |



To get to a list of property IDs I assembled a search-link for each search where I grabbed links that stared with “en/d”Â and had a number in it. Some sample code below:



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
` | `import re
url = 'https://www.immoscout24.ch/en/house/buy/city-bern?pn=1&r=7&se=16&map=1'

ids = []
html = requests.get(url)
soup = BeautifulSoup(html.text, "html.parser")
links = soup.findAll('a', href=True)
hrefs = [item['href'] for item in links]
hrefs_filtered = [href for href in hrefs if href.startswith('/en/d')]
ids += [re.findall('\d+', item)[0] for item in hrefs_filtered]

print(ids)

## -- Output --
['6331937', '6330580', '6329423', '6298722', '6261621', '6311343', '6318070', '6313553', '6317089', '6306531', '6305793', '6296041', '6294327', '6284892', '6283242', '6282624', '6274328', '6251376', '6237199', '6237144', '6231495', '6224144', '6223578', '6209944']
` |



Complete code above you can find on GitHub on [solids_scraping.py](https://github.com/ssp-data/practical-data-engineering/blob/v1/src/pipelines/real-estate/realestate/common/solids_scraping.py) in functions called `list_props_immo24`Â and `cache_properies_from_rest_api`.


### Storing on S3-MinIO


With an object storage, you provide one single API without lock you in into a cloud vendor and you can always access the same URL/API within your application or pipelines. I use [MinIO](http://min.io) but there are several [others](https://en.wikipedia.org/wiki/Amazon_S3#Notable_users). They normally run on Kubernetes, are open-source and may also boost performance. Plus if you haven't access to your own S3 e.g. locally or on your servers, you can simply create one in three lines of code: 


`1
2
3
4
5
6
7
8
9
`

`wget https://dl.min.io/server/minio/release/linux-amd64/minio
chmod +x minio
./minio server /data
# â Output â
Endpoint: http://192.168.2.128:9000 http://127.0.0.1:9000
AccessKey: your-key
SecretKey: your-secret
Browser Access:
http://192.168.2.128:9000 http://127.0.0.1:9000
`

You can access the endpoint `127.0.0.1:9000` programmatically with its key/secrets. On top, you get a full-blown UI as you can see below.


![/blog/data-engineering-project-in-twenty-minutes/images/2021-01-14_22-14-24.png](https://www.ssp.sh/blog/data-engineering-project-in-twenty-minutes/images/2021-01-14_22-14-24.png)

*Local Minio UI*


### Change Data Capture (CDC)


CDC is a powerful tool and especially in cloud environments with event-driven architectures. I used it to minimize the downloads of already downloaded properties. Besides existing open-source CDC solutions like [Debezium](https://debezium.io/), I implemented my own simple logic to detect the changes. Also because I have no access to the source-[OLTP](https://en.wikipedia.org/wiki/Online_transaction_processing) database where the properties are stored which you'd need.


I accomplish the CDC by creating two functions. The first one lists all properties to certain search criteria and the second one compares these properties with existing once. How am I doing that? Primarily, I create a [fingerprint](https://en.wikipedia.org/wiki/Fingerprint_(computing)) from each property that will tell me if the one is new or already exstinging. You might ask why I'm not using the unique property-ID? The reasons are I didn't just want to check if I have the property or not. As mentioned in the intro I also wanted to check if the seller lowered the price over time to be able to notify when the seller can't get rid of his house or flat. My fingerprint combines the property-ID and the selling price (called `normalized_price`in my data). One more benefit if more columns getting relevant, I could just add them to the fingerprint and my CDC mechanism would be extended without changing any other code.


To have the relevant selling price for each property-ID I will scrape them separately from the website same as the IDs themselves. You can check that code in [solid_scraping.py](https://github.com/ssp-data/practical-data-engineering/blob/v1/src/pipelines/real-estate/realestate/common/solids_scraping.py#L121). The function is called `list_props_immo24` which returns all properties as a data frame for my search criteria.


The logic for CDC happens in `get_changed_or_new_properties` in [solids_spark_delta.py](https://github.com/ssp-data/practical-data-engineering/blob/v1/src/pipelines/real-estate/realestate/common/solids_spark_delta.py) where I compare the existing once in my delta table with the new coming from list function above. As Delta Lake supports an SQL-API I can use plain SQL to compare the two with this simple SELECT-Statement:


`1
2
3
4
5
6
`

`SELECT p.id, p.fingerprint, p.is_prefix, p.rentOrBuy, p.city, p.propertyType, p.radius, p.last_normalized_price
  FROM pd_properties p
  LEFT OUTER JOIN pd_existing_props e
    ON p.id = e.propertyDetails_id
 WHERE p.fingerprint != e.fingerprint
	OR e.fingerprint IS NULL
`

Adding Database features to S3 â Delta Lake & Spark

**To get database alike features on top of your S3 files, you simply need to create a [Delta Lake](https://delta.io/) table**. For example, to add a dynamic schema to not break ingestions into a data lake or data pipelines downstream is quite a challenge. Delta is doing that and automatically add new columns incrementally in an [optimistic concurrent way](https://docs.databricks.com/delta/concurrency-control.html#optimistic-concurrency-control). As data in a data lake ist mostly distributed files, this is quite hard if you were to do that yourself. But as Delta already enforce schema and stores this information in the [transaction log](https://databricks.com/blog/2019/08/21/diving-into-delta-lake-unpacking-the-transaction-log.html) it makes sense to handle this with Delta. In my data sets with 60+ dynamic and changing columns, I made use of this feature extensively.
  

    How to create or read a Delta table then? It can be easily done with providing the format `delta` opposed to `parquet` or other formats you'd know:
  


`1
2
3
4
5
6
`

`#create delta table
data = spark.range(0, 5)
data.write.format("delta").save("/tmp/delta-table")
#reading it
df = spark.read.format(âdeltaâ).load(â/tmp/delta-tableâ)
df.show()
`

 
    Another feature of Delta is the automatic snapshotting mechanism with [time-travel](https://databricks.com/blog/2019/02/04/introducing-delta-time-travel-for-large-scale-data-lakes.html) that lets you check older versions of a table. This can become very handy for dimension-tables to protocol history e.g. addresses. This way you can skip a rather complex [SCD2](https://www.kimballgroup.com/2008/09/slowly-changing-dimensions-part-2/) logic. Just make sure to set your [retention threshold](https://docs.delta.io/latest/delta-utility.html#vacuum) high enough before you using [vacuum](https://docs.delta.io/latest/delta-utility.html#remove-files-no-longer-referenced-by-a-delta-table) (deletion of older data).
  


`1
2
3
`

`#Read older versions of data using time travel
df = spark.read.format(âdeltaâ).option(âversionAsOfâ, 0).load(â/tmp/delta-tableâ)
df.show()
`

 
    Also handy is it does not matter if you're reading from a stream or batch. Delta support both in a single API and target sink. You can see that well explained at [Beyond Lambda: Introducing Delta Architecture](https://youtu.be/FePv0lro0z8) or with some [code examples](https://docs.delta.io/latest/delta-streaming.html#delta-table-as-a-sink&language-python). Often used MERGE-statement in SQL can be applied on your distributed files as well with Delta including schema evolution and ACID transaction:
  


`1
2
3
4
5
6
7
8
`

`--A simple example:
MERGE INTO events
USING updates
   ON events.eventId = updates.eventId
 WHEN MATCHED THEN
	  UDATE SET events.data = updates.data
 WHEN NOT MATCHED THEN
 	  INSERT (date, eventId, data) VALUES (date, eventId, data)
`

 
    Further motivation why I'm using Delta for my project:
  


      using SQL on top of my distributed files
    

      simply merge my new properties into my data lake, no need to manually identify data changes
    

      working with JSONs and each has a totally different schema, I don't need to worry about that with schema evolution
    

      I get a full-blown transaction log to see what went on
    

      everything is well compressed and in columnar format stored ready for analytics query with open-source [Apache Parquet](https://parquet.apache.org/) files
    

      I have rich APIs in different languages with Scala, Java, Python and SQL
    

      with deletes integrated I'm prepared for [GDPR](https://en.wikipedia.org/wiki/General_Data_Protection_Regulation) requirements
    

      I can always travel back in time to see how the selling price of my properties has risen over time
    

      no need to worry about size and speed as everything is scalable with Spark, even the metadata.
    

      future proof with unified batch and streaming source and sink - no need for a [lambda architecture](https://en.wikipedia.org/wiki/Lambda_architecture) where batch and streaming is handled separately
    

      everything is open-source, the data format with Apache Parquet and [Delta Lake](https://github.com/delta-io/delta) itself
    


    To add to the popularity of SQL, I added a Dagster generic solid that can pass any SQL statement along and it will use spark to run on top of my Delta Lake tables. The solid is called `_sql_solid` (original coming from Dagster [airline-demo](https://docs.dagster.io/examples/airline_demo)). The full integrated example in [solids_spark_delta.py](https://github.com/ssp-data/practical-data-engineering/blob/v1/src/pipelines/real-estate/realestate/common/solids_spark_delta.py) or below an extract of how I can pass along the merge within Dagster.
  


` 1
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
`

`merge_property_delta = sql_solid(
    name="merge_property_delta",
    sql_statement="""
    MERGE INTO {{ target_delta_table }} trg
    USING input_dataframe AS src
       ON trg.propertyDetails_id = src.propertyDetails_id
     WHEN MATCHED THEN
          UPDATE SET *
     WHEN NOT MATCHED THEN
          INSERT *
    """,
    materialization_strategy="delta_table",
    input_defs=[
        InputDefinition("target_delta_table", DeltaCoordinate),
        InputDefinition("input_dataframe", DataFrame),
    ],
)
`

Machine Learning part â Jupyter Notebook

    I'm not a data scientist, still, I wanted to have some insights and fun with my data as well. That's why initially copied one or two Notebook from [Kaggle](https://www.kaggle.com/) to play around with. In my project, I wanted to integrate them into my pipeline.
  

[

](https://www.ssp.sh/blog/data-engineering-project-in-twenty-minutes/images/scatterplot_fun.png)Scatterplots from different attributes of real-estates associated with the selling Price


    Why bother with Jupyter notebooks? Because you most probably have skilled people who are creating the most advanced notebooks with real insight from your data. But unfortunately, these notebooks need to run manually and are not integrated into the data pipelines. There are two options in my opinion. Either you can test and approve notebooks, integrate them into your pipeline, this is basically to copy your python code over into your pipelines. This obviously is a lot of work and does not support changes from the data scientists in the notebooks as these need to be copied over again. So what else could we do?
  

    Good thing there is [Papermill](https://github.com/nteract/papermill) that lets you run jupyter notebooks directly. And even better, Dagster integrated Papermill into [dagstmill](https://docs.dagster.io/overview/packages/dagstermill) which lets you place one notebook as part of your existing data pipeline. On top of that, you have visibility within Dagster's UI, which lets you open the notebook directly. As well you can interact with the input and output of the notebook or use the output further downstream in your pipeline.
  
16/ By integrating it into Dagster, it is accessible and understandable with our tools: [pic.twitter.com/qUuGFDDktZ](https://t.co/qUuGFDDktZ)— Nick Schrock (@schrockn) [August 11, 2020](https://twitter.com/schrockn/status/1293240737027375105?ref_src=twsrc%5Etfw)


    My part of the integration, you can find in `data_exploration`in [solid_jupyter.py](https://github.com/ssp-data/practical-data-engineering/blob/v1/src/pipelines/real-estate/realestate/common/solids_jupyter.py).
  
Ingesting Data Warehouse for low latency â Apache Druid

    Most business intelligence solutions include a fast responsive [OLAP](https://www.ssp.sh/blog/olap-whats-coming-next/#What_is_OLAP) solution often done with cubes. For example, in Microsoft SQL Server you have [Analysis Services](https://en.wikipedia.org/wiki/Microsoft_Analysis_Services). But what should you use if you want an open-source product which is able to handle big data with no problems? One excellent choice is [Apache Druid](https://druid.apache.org/), but if you want to know more details or find other ways for you, check out my blog post about [OLAP, and what's next](https://www.ssp.sh/blog/olap-whats-coming-next/).
  

    Druid is a beast to set up, but luckily in my [data-engineering-devops](https://github.com/ssp-data/data-engineering-devops/tree/main/src/druid) infrastructure project, you find how to set it up on Kubernetes, or locally on your laptop with [Docker Desktop](https://www.docker.com/products/docker-desktop) which provides a native Kubernetes. Also, check out the original [helm chart](https://github.com/helm/charts/tree/master/incubator/druid) coming from Druid.


` 1
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
`

`#create namespace
kubectl create namespace druid
kubectl get namespaces

#PersistentVolumes (pv) and PersistenVolumeClaims (pvc)
#get context:
kubectl config current-context
#use above context and set namespace to druid:
kubectl config set-context docker-desktop --namespace=druid

#create perstisten volumes
cd $git/data-engineering-devops/src/druid
kubectl apply -f  manifests/base/persistentVolume/volumes.yaml

#druid deployment
cd $git/data-engineering-devops/src/druid
kubectl apply -k manifests/overlays/dev/localhost/sspaeti
kubectl delete -k manifests/overlays/dev/localhost/sspaeti

#Port-forwarding to access druid-UI
kubectl get pod
kubectl port-forward druid-router-86798c8b4c-vjvxj 8888:8888
`

 
    For the project part, I set it up and ingested some properties, but that was more to test the set-up locally. As speed is not a major requirement for me right now, and Druid eats a lot of resources and hard to run locally, I'm focusing on the Delta Lake to be the single source of thought for my queries.
  
The UI with Dashboards and more â Apache Superset

[

](https://www.ssp.sh/blog/data-engineering-project-in-twenty-minutes/images/apache_superset_scale.png)Scale data access across any data architecture


    No project isn't complete without a nice UI that visualises your insights. For its [open-source purposes](https://preset.io/blog/future-of-business-intelligence/) and features, I use Apache Superset for some time now. Lately, Superset announces version 1.0 and it is among the [top 200 projects](https://gitstar-ranking.com/repositories?page=2) on GitHub. The founder [Maxime Beauchemin](https://medium.com/@maximebeauchemin) and his company [Preset](https://preset.io/) are building more and more amazing features, one being to [create your own plugins](https://preset.io/blog/2020-07-02-hello-world/)Â easily.
  

    Superset can easily connect to Druid natively, or it can query a data lake with Delta Lake tables, plus it can handle almost any kind of SQL based database. The [dockerfile](https://github.com/ssp-data/data-engineering-devops/tree/main/src/superset) I use is the original with adding `pydruid`for querying Druid. Functionalities as exploring, dashboarding views and how to investigate your data you see below:
  

[

](https://www.ssp.sh/blog/data-engineering-project-in-twenty-minutes/images/superset-view.png)Apache Superset Dashboard Functionality

Orchestrating everything together â Dagster

    Ultimately, the part that glues everything together, the orchestrator. Today there is quite an [extended list](https://github.com/pditommaso/awesome-pipeline#pipeline-frameworks--libraries) of orchestrator out there. I tried to highlight the most suitable  [alternatives to Apache Airflow](https://qr.ae/pNrIPi) and went with [Dagster](https://dagster.io/) for the coming reasons below.
  




    Data pipelines start simple and straight-forward, **but often they end up vastly heterogeneous with various APIs, Spark, cloud data warehouse, and multi-cloud-providers**. Above a real-live example from [GoodEggs](https://www.goodeggs.com/) which includes [mode](https://mode.com/), [networkx](https://networkx.org/), [stitch](https://www.stitchdata.com/), SQL, Jupyter-notebooks, Slack-connector, [cronitor](https://cronitor.io/), and many more. This is a complex data pipeline but it is still fairly common to have such an amount of diverse technologies.
  

    Why I'm saying all that? Because this is one place where Dagster shines. **It's built with a high-level abstraction in mind**, not just as an executor. Even more, you can use different executor e.g. Airflow, Celery, Dask or Dagster itself, no lock-in here. Dagster lets you focus on building your data pipelines. It is made for data-flows and with it to pass data between the [solids](https://docs.dagster.io/overview/solids-pipelines/solids) (their name of tasks). The integration with [modes](https://docs.dagster.io/overview/modes-resources-presets/modes-resources) lets you switch from dev to test and production with one click and different resources on each mode. Let's say you won't have a [snowflake-db](https://www.snowflake.com/) locally available, so you could just mock it or use a simple Postgres locally for testing but with no changing of your data-pipeline code.
  

**You have an elegant way of separating business logic in [solids](https://docs.dagster.io/overview/solids-pipelines/solids) and technical code within [resources](https://docs.dagster.io/overview/modes-resources-presets/modes-resources)**. Resources are also commonly available in solids and are written once. Meaning your Spark connect, your Snowflake create a table, your rest-call to a certain service, these all can be written once in a resource and all users have it available in every solid.
  

**Dagster provides a beautiful feature-rich UI called Dagit. It includes state-of-the-art [GraphQL](https://graphql.org/) Interfaces for fetching status, starting, stopping pipelines** and many more. As shown in the machine learning part, it closes the boundaries to the machine learning team with the integration of Jupyter notebooks. It's all free and [open-source](https://github.com/dagster-io/dagster) and the team is extremely responsive on both [Slack](https://dagster-slackin.herokuapp.com/) and [GitHub](https://github.com/dagster-io/dagster/).
  

    What about testing? Testing data is very hard and nothing compared to software testing as data is and even tools and framework is dynamic and can change every output of your transformation, as well the size of data changes in dev, test, and production. Dagster's abstraction supports testing profoundly. [Type checks](https://docs.dagster.io/tutorial/types#dagster-types) and [assertions](https://docs.dagster.io/tutorial/types#expectations) about your data are included. ButÂ I'd suggest using the first-class [integration](https://dagster.io/blog/great-expectations-for-dagster) of [Great Expectation](https://greatexpectations.io/).
  
Happy to announce @dagsterio's newest integration with  [@expectgreatdata](https://twitter.com/expectgreatdata?ref_src=twsrc%5Etfw), the open source data quality framework. See here how richly display the test results right in our tools. We deeply integrate with tools and don't just call them opaquely. Fun to work with [@AbeGong](https://twitter.com/AbeGong?ref_src=twsrc%5Etfw) and team! [https://t.co/NKRcUMY1yX](https://t.co/NKRcUMY1yX) [pic.twitter.com/tQ6qQ9D45F](https://t.co/tQ6qQ9D45F)— Nick Schrock (@schrockn) [September 10, 2020](https://twitter.com/schrockn/status/1304094805153083392?ref_src=twsrc%5Etfw)

On top of that, **Dagster embraces the [functional programming paradigm](https://en.wikipedia.org/wiki/Functional_programming)**. By simply writing Dagster pipelines, you are writing **functional solids that are declarative, abstracted, [idempotent](https://www.ssp.sh/blog/business-intelligence-meets-data-engineering/#%E2%80%9CLoad_incremental_and_Idempotency_%E2%80%9D), type-checked to catch errors early**. Dagster also includes simple [unit-testing](https://docs.dagster.io/examples/pipeline_unittesting) and handy feature toÂ [make pipelines and solid testable and maintainable](https://docs.dagster.io/tutorial/testable#testing-solids-and-pipelines).
All of my examples are implemented with Dagster. Just clone my repo, install Dagster and start Dagit from [src/pipelines/real-estate](https://github.com/ssp-data/practical-data-engineering/tree/v1/src/pipelines/real-estate). I’m trying to build an [awesome-dagster](https://github.com/ssp-data/awesome-dagster) with common code-blocks as solids, resources and more to be re-used by everyone. Feel free to contribute if you have nice components to add.
DevOps engine â Kubernetes
And finally, the engine everything runs on locally and [cloud-agnostic](https://looker.com/definitions/cloud-agnostic#:~:text=Cloud%2Dagnostic%20platforms%20are%20environments,different%20features%20and%20price%20structures.) in the cloud is [Kubernetes](https://kubernetes.io/). Quoted from an earlier [post](https://www.ssp.sh/blog/business-intelligence-meets-data-engineering) in chapter [Use a container-orchestration system](https://www.ssp.sh/blog/business-intelligence-meets-data-engineering/#%E2%80%9CUse_a_containerorchestration_system_%E2%80%9D):
**[Kubernetes](https://stackoverflow.blog/2020/05/29/why-kubernetes-getting-so-popular/)Â has become the de-facto standard** for your cloud-native apps to (auto-)Â [scale-out](https://stackoverflow.com/a/11715598/5246670) and to deploy your open-source zoo fast, cloud-provider-independent. No lock-in here. You could use [open-shift](https://www.openshift.com/)Â orÂ [OKD](https://www.okd.io/). With the latest version, theyÂ added theÂ [OperatorHub](https://operatorhub.io/) where you can install as of today 182 items with just a few clicks. [â¦] Some more reasons for Kubernetes are the **move from infrastructure as code** towards **infrastructure as data**, specifically asÂ [YAML](https://en.wikipedia.org/wiki/YAML). [â¦] Developers quickly write applications that run across multiple operating environments. Costs can be reduced by scaling down [â¦]
To get hands-on with Kubernetes you can install [Docker Desktop](https://www.docker.com/products/docker-desktop) with Kubernetes included. All of [my examples](http://code.sspaeti.com) are build on top of it and run on any cloud as well as locally.Â For a more sophisticated set-up in terms of Apache Spark, I suggest reading the blog post from [Data Mechanics](https://www.datamechanics.co/) about [Setting up, Managing & Monitoring Spark on Kubernetes](https://www.datamechanics.co/blog-post/setting-up-managing-monitoring-spark-on-kubernetes). If your more of a video guy, [An introduction to Apache Spark on Kubernetes](https://youtu.be/qcvNZvFZIP4?t=31) contains the same content but adds still even on top of it.
Conclusion
We have seen that in order to apply hands-on data engineering methodologies to a real-estate project, you need to know a good amount of the latest big data tools and frameworks. As well as data architecture to assess how these fit together and can be utilised for specific use-cases. I hope I could give you some inspiration and ways to create your own data engineering project. From scraping the web to storing the data in an S3 object store, adding database features onto it, using machine learning capabilities with Jupyter notebooks, ingesting it into a data warehouse, visualise the data with a nice dashboard, connecting everything together with an orchestrator and running it cloud-agnostic.
If you want to test your knowledge, start the [Pokemon or Big Data](https://pixelastic.github.io/pokemonorbigdata/) quiz, you will see it’s not that easy ð. If you like more [Open-Source Data Engineering Projects](https://www.ssp.sh/brain/open-source-data-engineering-projects/), I curate a list I constantly update.
Thatâs it for now. If you like the content and want to follow along, make sure you subscribe to my [newsletter](https://subscribe.ssp.sh/), check my [code](http://code.sspaeti.com) on GitHub or visit me on [LinkedIn](https://www.linkedin.com/in/sspaeti/), or [Twitter](https://twitter.com/sspaeti/) for genuine news about the data ecosystem.

*Republished on [Medium](https://sspaeti.medium.com/building-a-data-engineering-project-in-20-minutes-85c37cad4d87).*

[Discuss on Bluesky](https://bsky.app/search?q=domain%3A%20https://www.ssp.sh/blog/data-engineering-project-in-twenty-minutes/)
|
[Pay what you like](https://ko-fi.com/sspaeti)
|
[Druid](https://www.ssp.sh/tags/druid/)
[Dagster](https://www.ssp.sh/tags/dagster/)
[Delta Lake](https://www.ssp.sh/tags/delta-lake/)
[Data Lake](https://www.ssp.sh/tags/data-lake/)
[Devops](https://www.ssp.sh/tags/devops/)
[Jupyter](https://www.ssp.sh/tags/jupyter/)
[Kubernetes](https://www.ssp.sh/tags/kubernetes/)
[Minio](https://www.ssp.sh/tags/minio/)
[Notebooks](https://www.ssp.sh/tags/notebooks/)
[Spark](https://www.ssp.sh/tags/spark/)
[Superset](https://www.ssp.sh/tags/superset/)
[Open Table Format](https://www.ssp.sh/tags/open-table-format/)
