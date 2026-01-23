---
title: "Data Warehouse vs Data Lake | ETL vs ELT10-26"
date: 2017-10-26
url: https://www.ssp.sh/blog/data-warehouse-vs-data-lake-etl-vs-elt/
slug: data-warehouse-vs-data-lake-etl-vs-elt
word_count: 1960
---

![Data Warehouse vs Data Lake | ETL vs ELT](https://www.ssp.sh/blog/data-warehouse-vs-data-lake-etl-vs-elt/images/Woman-with-Lake-Backgroud-1024x683.jpg)

Contents

There is a bit of a confusion between Data Warehouse vs Data Lake or ETL vs ELT. I hear that Data Warehouses are not used anymore, that they are replaced by Data Lakes altogether, but is that true? And why do we need Data Warehouses anyway? I will go into that as well as the definitions of both pluses explain the differences between them.


## Data Warehouse vsÂ Data Lake


### Data Warehouse definition


A Data Warehouse, in short DWH and also known as anÂ Enterprise Data WarehouseÂ (EDW), is the traditional way of collecting data as we doÂ [since 31 years](https://www.ssp.sh/blog/data-warehouse-automation-dwa/). The DWH serves the purpose of being the data integration from many different sources, the single point of truth and the data management meaning cleaning, historize and data joined together. It provides greater executive insight into corporate performance with management Dashboards, Reports or Ad-Hoc Analyses.


Various types ofÂ business data are analysedÂ with Data Warehouses. The need for it often becomes evident when analytic requirements run afoul of the ongoing performance of operational databases. Running a complex query on a database requires the database to enter a temporarily fixed state. This is often untenable for transactional databases. A data warehouse is employed to do the analytic work, leaving the transactional database free to focus on transactions.


The other characteristics are the ability to analyse data from multiple origins (e.g. your Google Analytics with your CRM data), and that is highly transformed and structured due to theÂ ETL (Extract Transform Load) process.


### Data Lake definition


A Data Lake is a store full of unstructured and structured data, stored as-is, without a specific purpose in mind, that can be built on multiple technologies such as Hadoop, NoSQL, Amazon Simple Storage Service, a relational database, or various combinations and different formats (e.g. Excel, CSV, Text, Logs, etc.).


According to [Hortonworks Data Lake Whitepaper](http://hortonworks.com/wp-content/uploads/2014/05/TeradataHortonworks_Datalake_White-Paper_20140410.pdf), the data lake arose because new types of data needed to be captured and exploited by the enterprise. As this data became increasingly available, early adopters discovered that they could extract insight through new applications built to serve the business. The data lake supports the following capabilities:

- To capture and store raw data at scale for a low cost
- To store many types of data in the same repository
- To perform transformations on the data
- To define the structure of the data at the time, it is used, referred to as schema on reading
- To perform new types of data processing
- To perform single subject analytics based on particular use cases


### Differences between Data Warehouse and Data Lake


I like the definition and comparison byÂ James Dixon, founder and CTO of Pentaho:


> If you think of a **DWH** as a store of bottled water â **cleansed and packaged and structured for easy consumption** â the **data lake** is a **large body of water in a more natural state**. The contents of the data lake stream in from a source to fill the lake and various users of the lake can come to examine, dive in, or take samples.


### Different analogies


As you can see on the picture below, both Technologies are created for different purposes:


### When to use what?


As mentioned in the introduction, companies are **shifting** **from the Data Warehouse to the Data Lake**, although it’s two different things, it still can make sense. Especially when you want real-time data, as the Data Warehouse typically works in batch processes, the Data Lake works near real timeÂ and handling Big Data. It’s made for huge data and stores them unstructured easy and fast. So when should I use what?

- **The Data Warehouse**Â is designed for *slowly changing data*:
- **The Data Lakes** on the other side is designed for *quickly changing data*


### Modern Data and Analytics Environment


It is common, especially in mid or large size organisation to have both environments. The image below illustrates how you would integrate itÂ with an Enterprise Data Warehouse and a Data Lake:


![/blog/data-warehouse-vs-data-lake-etl-vs-elt/images/Modern-Data-Analytics-Environment.jpg](https://www.ssp.sh/blog/data-warehouse-vs-data-lake-etl-vs-elt/images/Modern-Data-Analytics-Environment.jpg)

*Image fromHow Iâve Learned to Stop Worrying and Love the Data Lake*


## ETL vs ELT


ETLÂ (Extract Transform and Load) and ELT (Extract Load and Transform) is what has described above. **ETL is what happens within a Data Warehouse and ELT within a Data Lake**.


ETL is the most common method used when transferring data from a source system to a **Data Warehouse**. In that process, you load data to your stage-layer of your DWH, [clean](https://en.wikipedia.org/wiki/Data_cleansing) and transform it to the [Dimensional Model](https://en.wikipedia.org/wiki/Dimensional_modeling) (Facts and Dimensions) and at the end, you load it to a final Data Mart or a Cube for further Data Visualisations.


If you want to use ELT, that’s when you want to build a **Data Lake**. You extract data, mostly done by physical files, load it into your Data Lake in your Cloud Storage and only then start transforming and cleaning the data. The natural process is that you begin exploring and analysing your data and find out, that the data is dirty and then you begin cleaning it.


## Big Data


How is [Big Data](https://en.wikipedia.org/wiki/Big_data) connected to this topic? Big Data is more or less gathering massive amounts of data (several million rows per second) from devices like IoT (Internet of Things), different data points from each smartphone, etc. With specific Big Data infrastructure and algorithms (e.g. map-reduce) you collect the data and store it into the Data Lake. Big data is greatest used with a Data Lakes.


As a new technology arises an old one gets replaced, that’s maybe why**Â many technologists and thought leaders are declaring the Data Warehouse is dead.**Â They say it’s no longer relevant **in the age of Big Data**. But why? The question is, are youÂ still have a traditional Data Warehouse with an ETL tool, are you 100% happy with it? There is a great chance that you are not.Â Because of a significant amount of coding required in traditional ETL tools,Â your ETL tool was probably outdated before you were ready to deploy it.


But these prognosticators are mistaken. **Big data can extend and enrich a Data Warehouse, but cannot replace it**. It is not a Data Warehouses that are dead, but the traditional way of designing and building them. A better and new approach is using Data Warehouse Automation (DWA) Tools that automates the recurring parts of developing a Data Warehouse to [cut down time development time by 40-60%](https://www.ssp.sh/blog/why-data-warehouse-automation-is-not-more-popular/#Speed). Find more information in the [DWA Blog post series](https://www.ssp.sh/blog/data-warehouse-automation-dwa/) or directly [why we should use DWA tools](https://www.ssp.sh/blog/why-automate-what-does-dwa-for-us/).


## Data Vault


Another way of adapting to Big Data and fast-changingÂ data connection points is theÂ [Data Vault](https://danlinstedt.com/solutions-2/data-vault-basics/) modelling and methodology which enables you a more dynamic and flexible way to implement additions to your Data Warehouse. Lately, **there has been an interesting move to use a Data Vault as a governed Data Lake**, because it addresses the elements of the problems we identified within Data Warehousing:

- It adapts to a changing business environment
- It supports huge data sets
- It simplifies the Data Warehouse design complexities
- It increases usability by business users because it models after the business domain
- It allows for new data sources to add without impacting the existing design


This technological advancement is already proving to be highly effective and efficient. Easy to design, build, populate, and change. New Data Warehouses should be created with this methodology, also a point where [Data Warehouse Automation](https://www.ssp.sh/blog/why-automate-what-does-dwa-for-us/) helps you.


## Conclusion: Will a Data Lake replace the Data Warehouse?


I don’t think so. As elaborated thoroughly above, it will still need both over a long period. Both are designed for distinctive purposes and have different advantages. And I believe we should be careful with Data Lakes as more data is always better but can also lead to more chaotic data stores where nobody knows the what’s in there and it takes everyone a lot of time just to get the needed data.


In my opinion, it makes sense to have both environments to be flexible for fast changes and analysis within the Data Lake. But still be able to make very well structured Analytics with Dashboards and Reports for the operational business user. That’s why I would suggest importing patterns and essential analysis you found in the Data Lake back to your Data Warehouse to make it easily accessible for everyone in a standard way and tools users know.


Thanks for reading that far. Please feel free to add comments or anything you don’t agree, I’m always open to discussions and recommendations :-).


---


```
Republished onÂ LinkedIn and Hacker Noon.
```


## Comments


### Comment by Amira Isbel on 2018-01-15 15:28


perfect article , thank you


### Comment by sspaeti on 2018-01-19 19:43


Thanks for reading and the feedback Amira


### Comment by Somesh C on 2018-03-15 15:52


I was looking for a quick primer and kind of T shaped article on EDW vs Data lake and got on to this page. Wonderfully written article succinct and to the point.


### Comment by sspaeti on 2018-03-15 17:47


Hi Somesh, thank you so much for your comment. I’m happy you find the post useful


### Comment by Gaja Krishna Vaidyanatha on 2018-03-20 03:46


Hi Simon,


Here is another perspective on the subject of ETL vs ELT:


The use of ELT is not just for big-data stores. ELT is relevant even for relational data when you are attempting to build a data-integration hub/platform from multiple system-of-record (SOR) databases. ELT is the boon you are looking for when you don’t want to âleave any data on the table’ and bring everything into the data integration hub. This is great because, ELT obviates the need for an physical enterprise data model, which mandates standards of object definition and naming.


The fundamental problem with ETL is that any data that does not conform to the transformation rules, will never make it into the data integration hub. With ELT, you bring all of your data in (yes mostly relational) and then transform your data, which then helps you understand side-by-side, the reasons why some of your data does not make the âtransformation cut’. And in doing ELT, one can always run transformation multiple times, after the relevant data cleansing and fixing has been undertaken.


So where I come from, ETL is now ELT or even SLT (Stream, Load & Transform). It is important to note here that T in the context of ELT and SLT is to the power of n. Meaning, it can, will and should happen many times. As the business changes, you want your data integration hub to also change with it. âT to the power of n’ helps us support just that. You may wish to look at my LinkedIn posting about architecting âmeaningful data lakes’ here - [[https://www.linkedin.com/feed/update/urn:li:activity:6343284661518733312](https://www.linkedin.com/feed/update/urn:li:activity:6343284661518733312)](https://www.linkedin.com/feed/update/urn:li:activity:6343284661518733312). Hope that adds another perspective to what you are discussing ð


Cheers,


Gaja


### Comment by Umair Ahmed Shaikh on 2020-01-01 08:26


Its a good article explaining the key differences and use cases of each and when to use what. I agree with you that Data Lakes aren’t going to replace the traditional DWHs but instead, they will supplement the existing information powerhouse for advanced use cases. From a user standpoint, I think we have different users for DWHs and Data Lakes. Traditional report users like business managers will rely on DWHs for historical analysis whereas they will go to Data Scientists who will actually run the predictive models and extract the required information from Data Lakes on behalf of them.

[Discuss on Bluesky](https://bsky.app/search?q=domain%3A%20https://www.ssp.sh/blog/data-warehouse-vs-data-lake-etl-vs-elt/)
|
[Pay what you like](https://ko-fi.com/sspaeti)
|
[Business-Intelligence](https://www.ssp.sh/tags/business-intelligence/)
[Big Data](https://www.ssp.sh/tags/big-data/)
[Data Lake](https://www.ssp.sh/tags/data-lake/)
[Data Vault](https://www.ssp.sh/tags/data-vault/)
[Data-Warehouse](https://www.ssp.sh/tags/data-warehouse/)
[ETL](https://www.ssp.sh/tags/etl/)
[ELT](https://www.ssp.sh/tags/elt/)
