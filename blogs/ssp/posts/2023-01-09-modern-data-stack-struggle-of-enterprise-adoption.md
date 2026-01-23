---
title: "Modern Data Stack: The Struggle of Enterprise Adoption01-09"
date: 2023-01-09
url: https://www.ssp.sh/blog/modern-data-stack-struggle-of-enterprise-adoption/
slug: modern-data-stack-struggle-of-enterprise-adoption
word_count: 3118
---

![Modern Data Stack: The Struggle of Enterprise Adoption](https://www.ssp.sh/blog/modern-data-stack-struggle-of-enterprise-adoption/images/mds-enterprise-struggle-feature.jpg)

Contents

In part I,Â [The Open Data Stack Distilled into Four Core Tools](https://www.sspaeti.com/blog/open-data-stack-core-tools/), we discussed how to quickly set up a data stack, tackling end-to-end data analytics challenges. As a manager or developer working with data at a mid- to large-sized enterprise, you might ask why arenât we using any of these tools.Â


In this article, we dive into what mid-to-large-sized companies are using instead, the struggle of setting up aÂ [Modern Data Stack (MDS)](https://glossary.airbyte.com/term/modern-data-stack/)Â for an enterprise size, and the opportunities of a free-of-charge and open-source MDS. We will also highlight its downside: the addedÂ [complexity](https://roundup.getdbt.com/p/complexity-the-new-analytics-frontier)Â of using dedicated tools along each phase of theÂ [Data Engineering Lifecycle](https://glossary.airbyte.com/term/data-engineering-lifecycle).


## The Struggle of Building the Enterprise Data Stack


No matter what, building an enterprise-sized data stack is no piece of cake. Usually, in larger companies, everything is more complex. You have more people (possibly independent teams working with the same data), the whole setup is vastly more intertwined, and the code and programming language are enormous across the organization. There’s a lot of management with different opinions and strategies, and data engineering tools areÂ [changing faster](https://mattturck.com/data2021/)Â than any other domain.


Usually, the struggle starts with a management strategy to be aÂ **more data-driven**Â and self-serving organization. The struggle expands around eliminating data silos (Excel is your enemy), creating more transparency, faster decision cycles that are based on facts, and empowering people from the business to be more data savvy.

Top-Level Management Support
No matter which direction you go, it’s more important than ever to have top-level management support for your data strategy, executed from the bottom upâuse-case driven, starting with one department at a time.

## What Are Medium to Large-Sized Enterprises Doing Today?


Let’s paint a picture of how a typical environment could look in a mid-to-large-sized enterprise that wants to have a data-driven strategy. Most commonly, there are large ERP, CRM, and other internal systems that hold most of the business data. The beginning of the data journey is primarily standard among the more prominent companies, such as correlating the demand with orders and processes from the ERP with the customer from the CRM, connecting it with the user data from your website(s) with Google Analytics.


The sales team is building different platforms, including many financial business rules resulting in a pixel-perfect report sent out by e-mail. The product team pulls all data into an MS Excel sheet, adding custom transformation directly there. Marketing uses the third tool and cleans data with their custom web app. Usually, you have more internal data locked into a legacy software or format.


Working with data within a big organization is complicated and unpredictable. On the surface, it might not look that challenging. But everyone in the domain knows that all the different solutions, custom scripts, and code add technical debt, especially if the people who built it leave.


The options such enterprises often choose from to solve a more common data architecture are:

- Setting up a new team to either:
- customize and extend existing products and workflows, or
- go all in with a service from one of the bigÂ [cloud providers](https://glossary.airbyte.com/term/cloud-provider)
- [â](https://glossary.airbyte.com/term/cloud-provider)Hire a consultancy firm that knows the latest trendsâand can take responsibility if things are not working out ð


### Technology Adoption Lifecycle: The Chasm


If we look back at theÂ [Chasm](https://en.wikipedia.org/wiki/Crossing_the_Chasm), it’s clear that the Modern Data Stack is in its veryÂ *early market*Â withÂ *innovators*Â andÂ *early adopters*. Most of the Modern Data Stack tools are brand new; if lucky, you will find version 1.0. We can understand why mid-to-large enterprises have yet to pick up on the latest open-source data tools.Â


![/blog/modern-data-stack-struggle-of-enterprise-adoption/images/chasm.jpg](https://www.ssp.sh/blog/modern-data-stack-struggle-of-enterprise-adoption/images/chasm.jpg)

*Overview of the technology adoption lifecycle called the Chasm*


We see a similar picture when we look atÂ [Google Trends](https://trends.google.com/trends/explore?date=today%205-y&q=%22modern%20data%20stack%22)Â queries where the term “Modern Data Stack” is seldom searched outside of the US and Â«Data TwitterÂ»âwhich is mainly San Francisco if you search in the US only.Â


![/blog/modern-data-stack-struggle-of-enterprise-adoption/images/google-trend-mds.jpg](https://www.ssp.sh/blog/modern-data-stack-struggle-of-enterprise-adoption/images/google-trend-mds.jpg)

*Google Trends Search on Modern Data Stack*


Large enterprises typically ignore the trends until they are unavoidable, which theÂ [Enterprise IT Adoption Cycle](https://enterpriseitadoption.com/)Â dramatically illustrates. It’s okay, though, as these enterprises predominantly suffer from many legacies and migrations projects already; we will get into that later.


### Pre-Modern Data Stack


While working at larger enterprises, interacting with the business people who need to get the job done, I often heard questions like “[Why can’t we just write a script for this](https://airbyte.com/blog/etl-framework-vs-etl-script)?â and âDoes our existing tool (fill in the name) support that already?â I’m generalizing here on purpose, as each enterprise is different and all of them have a department or a couple of people playing with the latest stack.


All of this was pre-Modern Data Stack. My colleagues and I have essentially re-implemented the MDS repeatedly at each company in one way or another. The story generally went:

- **Extracting:**Â âWrite some script to extract data from X.â
- **Visualizing: âLetâs buy an all-in-one BI tool.â**
- **Scheduling**: “Now we need a daily cron.”
- **Monitoring**: “Why didn’t we know the script broke?”
- **Configuration**: “We need to reuse this code but slightly differently.”
- **Incremental Sync**: “We only need the new data.”
- **Schema Change**: “Now we have to rewrite this.”
- **Adding new sources**: “OK, new script…”
- **Testing + Auth + Pagination**: “Why didn’t we know the script broke?”
- **Scaling**: “How do we scale up and down this workload?”


These scripts above wereÂ **written in custom code**Â dedicated to one companyâsometimes for one department only.Â


Alternatively, buying an all-in-one enterprise data platform that uses no-code services gets you started with anÂ **out-of-the-box toolbox**Â for data integration, transformation, orchestration, and visualization right away. These tough decisions usually require several months of evaluation to be sure to invest in the right tool, as prices vary and are not cheap. Your final choices have long-term consequences, as you lock the company into that proprietary tool.


Today you get the full data stack for free, open-sourced on GitHub as illustrated inÂ [Part I](https://www.ssp.sh/blog/open-data-stack-core-tools/). It’s aÂ **game-changer**Â and is one reason that small companies can outperform large enterprises regularly with strong data-driven strategies and the latest technology from the Modern Data Stack.


**ðï¸ Traditional Data Stack vs. Modern Data Stack**Â


An overview of the data flow pre-MDS withÂ [ETL](https://glossary.airbyte.com/term/etl)Â and in modern data stack with the shift to centralize data before transforming the data withÂ [ELT](https://glossary.airbyte.com/term/elt).Â


![/blog/modern-data-stack-struggle-of-enterprise-adoption/images/tds-to-mds.jpg](https://www.ssp.sh/blog/modern-data-stack-struggle-of-enterprise-adoption/images/tds-to-mds.jpg)

*Traditional Data Stack (TDS) with ETL vs. Modern Data Stack with ELT byÂAlexandre Beauvois.*


Think of the above purple boxes on the left as different teams within the department. None of these were terrible ideas; itâs just the best way there was without investing in expensive SAP or similar solutions.


### Europe is different from the US market


I’m generalizing here, but Iâd like to share some high-level observations from working most of my life in European enterprises with 100-100,000 employees.Â

- European companies are optimizing for costs and privacy at a very high level.
- Their tech stack is commonly much less technical, and if so, consultants are a widely used medium.


The US market, with lots of startups, less regulation, and more openness to publicly sharing private data, uses the Modern Data Stack extensively. In contrast, Europe has stricter rules and is exceptionally aware of the security and ownership of its data and where it’s stored. Especially with the latestÂ [**GDPR regulations**](https://airbyte.com/blog/etlt-gdpr-compliance), data teams must support a way out for the customer who wants to delete their data and needs more precautions to store it in the first place.


Why is this even relevant? It has influenced how tools get picked. As seen above, most open data stack tools have been developed by fast-growing US startups. Unlike these startups, a bank in Switzerland or a publicly held company must comply with many laws. They needed to be careful and, for a long time, couldn’t invest in any cloud solutions, as there was no data center in Switzerland, for example. This is changing rapidly, but some big banks are still searching forÂ [Mainframe System Engineer](https://www.linkedin.com/jobs/view/3362554786)Â programming within programming languages such asÂ [COBOL](https://en.wikipedia.org/wiki/COBOL).


#### Legacy and Migrations


A big part of a large enterprise is also legacy and migration projects. The reasons are simple: enterprises exist longer and employ more employees than smaller ones. They go through different areas of data engineering and will most certainly have legacy code, tools, and frameworks that have been built by people who are no longer with the company.


With the above-discussed custom, scripts developed and maintained over the years also manifest in many legacy codes. But there is not only legacy code; there is also legacy hardware. Think of the above banks still running the oldÂ [IBM Mainframe](https://www.ibm.com/topics/mainframe)Â dependent on COBOL, Fortran, or some other ancientÂ [programming language](https://glossary.airbyte.com/term/programming-languages)Â which, according to Credit Suisse, is “still core of our Swiss Banking platform.” You can also check the changesÂ [in salaries between 2021 and 2022](https://survey.stackoverflow.co/2022/#section-top-paying-technologies-change-in-salaries-between-2021-and-2022), and you’ll see a similar picture with COBOL, Delphi, and IBM DB2.


The Seattle Data Guy also rightfullyÂ [points out](https://seattledataguy.substack.com/p/realities-of-being-a-data-engineer)Â that data engineers regularly face migration projects. Some of the types of migrations he mentions are operational system migrations (CRM, ERP), hardware migrations (newer, faster servers), cloud migrations (on-premise to the cloud), analytics migrations (differentÂ [data warehouses](https://glossary.airbyte.com/term/data-warehouse)Â orÂ [BI Tools](https://glossary.airbyte.com/term/business-intelligence-tools)), and data migrations (switch database or schema designs).


## Enterprise Data Platforms


Ultimately, every company needs a data platform for managing its data. So where do mid-to-large sized enterprises start? Not with an open-source Modern Data Stack, as people are used to working with more monolithic approaches with Oracle and Microsoft Servers. Therefore, the easiest and probably the best transition is to use services provided by your cloud provider of choice. These essentially are the MDS stack tools,Â *operated*Â by Amazon, Microsoft, and Googleâand most of the time, they have renamed the product as well (e.g.,Â [Google Cloud Composer](https://cloud.google.com/composer/docs/concepts/overview)Â is a managedÂ [Apache Airflow](https://glossary.airbyte.com/term/apache-airflow)).


Think of big vendors such as SAP, Oracle, and Microsoft, which were the main drivers a couple of years ago. Today there are more data platforms to choose from than ever. The bigÂ [cloud providers](https://glossary.airbyte.com/term/cloud-provider)Â are the best known: Amazon Web Services (AWS), Google Cloud, Microsoft Azure, Databricks, and Snowflake, where you find any service you need or find in open-source. Other less known are dedicated enterprise data platforms such as Ascend, Palantir Foundry, Kuwala, Keboola, Nexla, and Rivery, among many more. Also, solutions underÂ [Customer Data Platform](https://glossary.airbyte.com/term/cdp-customer-data-platform)Â (CDP) are essentially data platforms. Their feature set is vastly different, and each of them has their strengths and weaknesses.


ðÂ **Metadata in Enterprise Data Platforms**


The advantage that enterprise data platforms have is the metadata. As they act end to end, they have much-needed metadata to work in aÂ [declarative](https://glossary.airbyte.com/term/declarative)Â manner where you define what you want to achieve, and the platform figures out the how. The Modern Data Stack is one tool of many and missing the much-needed metadata to act autonomously. Moreover, the MDS had to workÂ [imperatively](https://glossary.airbyte.com/term/imperative/). But with tools such asÂ [Dagster](https://glossary.airbyte.com/term/dagster)Â and other tool integrations, this advantage slowly but surely merges more into the MDS, making it more powerful with the declarative approach.


â¹ï¸Â **Alternative: The Modern Data Stack Cloud**


Besides the all-in-one data platform, the modern data stack provider offers mainly a cloud option and different deployment options. Besides the prominent cloud provider running the MDS stack on their cloud, each MDS tool has its cloud product, e.g.,Â [Airbyte Cloud](https://cloud.airbyte.io/),Â [Airflow Cloud (Astronomer)](https://www.astronomer.io/),Â [Dagster Cloud](http://dagster.io/cloud), etc. These usually offer three different deployment methods:

- On-Prem / Self-managed (Free open-source option)
- Cloud First (Managed open-source version)
- Enterprise / Hybrid (Bring your compute platform, and the control plane of each cloud does not see your code orÂ [PII](https://en.wikipedia.org/wiki/Personal_data)Â data. Enterprise / Hybrid maximizes flexibility andÂ **security**Â while offloading the vast majority of the operational burden to the cloud provider)


### No-code vs. code solutions


These big vendors and their enterprise data platforms are essentially big no-code or less-code solutions. Itâs important to know the difference between no-code and code solutions. For example, no-code is excellent forÂ **lowering technical barriers**Â and enabling more users to perform data engineering. But these tools come with significant drawbacks:

- You are building knowledge in a proprietary tool rather than something generic and easily transferable (e.g., coding inÂ [Python](https://glossary.airbyte.com/term/python)).
- It’s powerful for a simple pipeline, but when it starts to get complex, it’s difficult to extend and maintain.
- It’s not easy/impossible to follow best practices of software engineering like testing or versioning.
- Licensing is usually rather expensive.


On the other hand, code-first solutions are hard to get started; you need highly skilled software engineers, but you getÂ **sustainable, long-term**Â **solutions**Â that are open without vendor lock.


## Opportunities for Enterprises with the MDS Stack


Now let’s discuss opportunities that the MDS stack delivers for enterprises.

- **Getting started**: Think about all the gains you can realize from existing solutions that could allow non-data engineers to start getting insight in a few hours or days.
- **Data privacy & legal**: MDS lowers the legal risks, giving more flexibility on where to run with open code. This means itâs easier to comply with changing data regulations.
- **Modularity & extensibility**: You can choose dedicated specialized tools for each use case without cost.
- **Technological advantage**: You are using the latest technology and gaining benefits over competitors who remain less data-driven.


It is strongly recommended to have highly technical people who useÂ [DevOps](https://glossary.airbyte.com/term/dev-ops)Â to set up the Modern Data Stack, especially on a scale or in an enterprise where many use it with something likeÂ [Kubernetes](https://glossary.airbyte.com/term/kubernetes).


#### Modularity: Supporting the Data Engineering Lifecycle


Whether you choose an enterprise data platform or the open-source route with the Modern Data Stack, your selection must solve theÂ [Data Engineering Lifecycle](https://glossary.airbyte.com/term/data-engineering-lifecycle). Each of these blocks needs to be implemented in one way or another to output insights valuable to the data consumers.


![/blog/modern-data-stack-struggle-of-enterprise-adoption/images/data-engineering-lifecycle.png](https://www.ssp.sh/blog/modern-data-stack-struggle-of-enterprise-adoption/images/data-engineering-lifecycle.png)

*The data engineering lifecycle |Fundamentals of Data Engineering*


### When not to use an MDS Stack


The advantage of modularity is undoubtedly also a disadvantage to the point that failures can pop up at each integration of another tool. Always keep in mind this quote fromÂ [Data Platforms: The Past](https://medium.com/alexandre-beauvois/modern-data-stack-as-a-service-1-3-1a1813c38633):

Complexity
Integrating good tools doesn’t mean you’ll get a good stack and expected results. It’s still a complex thing.

On the other hand, if you choose wisely, you can end up much better than a custom monolith that lost its maintainer.


**Costs**Â are another consideration, but can be hard to predict. As you run many independent tools, it’s harder to forecast the costs and to balance than to have one tool solution that does it for you.


The core of each MDS tool needs to be built forÂ **enterprise scale**Â and is added as an afterthought. You need to prove the solution first before you scale. I’m confident that the scale can’t be fixed, but that is something to keep in mind when testing the MDS tool.


**Adopting**Â MDS is slower than just plugging a credit card into an enterprise data platform and getting started. With such platforms, you do not need to consider deploying, upgrading, security, or other concerns. These things are hard. Therefore, you will need a dedicated data team and DevOps people.


In the end, it’s always aÂ **tradeoff**Â between fully on-premise and hosting all your tools yourself vs. everything managed on SaaS:Â


![/blog/modern-data-stack-struggle-of-enterprise-adoption/images/mdsaas.jpg](https://www.ssp.sh/blog/modern-data-stack-struggle-of-enterprise-adoption/images/mdsaas.jpg)

*FromÂData Platforms: The Past - The Evolution of Data Platforms*


## The Core Open (Modern) Data Stack


There are always more tools you can add to your Modern Data Stack! You can use the data engineering lifecycle as a reference for the building blocks to add. But in general, the core four you need are data ingestion, transformation, orchestration, and analytics.Â


Unfortunately, the fast phase will continue for a while. Sure, there are thousands of tools, and it’s impossible to keep updated with them, but you only need a few. Take Airbyte, dbt, a visualization tool, and Dagster, and youâll be up and running within hoursâwith a battle-tested, open-source high-impact tool at your fingertips. I illustrated these tools and how to set them up in Part I:Â [The Open Data Stack Distilled into Four Core Tools](https://airbyte.com/blog/modern-open-data-stack-four-core-tools). Check it out to get started with the analytics journey today.


Another consideration is naming. Even though the term Modern Data Stack hasn’t spread much, there is already the dislike of “modern,” which has no tangible value. Alternative names for “Modern Data Stack” that I saw areÂ [new generation open-source data stack](https://blog.devgenius.io/modern-data-stack-demo-5d75dcdfba50)Â (ngods), DataStack 2.0, and the Boring Data Stack. While starting an open-sourceÂ [Project](https://github.com/airbytehq/open-data-stack/), I foundÂ [Open Data Stack](https://www.ssp.sh/brain/open-data-stack/)Â to be the perfect nomenclature, emphasizing theÂ **value open-source**Â tools provide. âOpenâ also speaks toÂ **open standards**âdesperately needed in data engineering.Â


No matter the name, the essence of open source, extensible, and free-to-use will not change.

GitHub Project
Check out theÂ
[open-data-stack](https://github.com/airbytehq/open-data-stack/)
Â example project we just started (weâll be adding to it as part of thisÂ
[series](https://airbyte.com/blog/building-airbytes-data-stack)
).

## ð® The Next Step of the Modern Data Stack is Open Data Stack


Most of us live in a bubble with the latest trends of big tech data-driven companies ([FANG](https://en.wikipedia.org/wiki/Big_Tech#FANG,_FAANG,_MAGMA_or_MAMAA)). If you follow the space closely, you see indications that people are overwhelmed with too many tools in the MDS stack, which is no surprise as our industry is growing like no other.


Another sign showsÂ [DuckDB](https://glossary.airbyte.com/term/duckdb/)Â hype; people like the simplicity of itâ removing instead of adding to the data stack. ManyÂ [use cases](https://glossary.airbyte.com/term/duckdb/#use-cases)Â are possible, and everyone is looking to simplify things. In the end, simplification also means fewer moving parts and fewer errors.Â


At the same time, the Modern Data Stack will not go anywhere, except it will most likely be renamed to something else. It’s still evolving, as many large European enterprises learned from their past with vendor lock-in and closed-source and are ready to leave that behind.


Enterprises still have legacy code that will use old programming languages for a while. So these are still slowly adoptingÂ [Open Data Stack](https://www.ssp.sh/brain/open-data-stack/)Â over the next decade. Again, integrating good tools from the data stack doesn’t mean you’ll get a good stack per se. It helps to choose wisely. Ask yourself: “Do we have the capacity and knowledge to own and manage the data stack ourselves?”Â


If you want to try it yourself, follow along with ourÂ [open-data-stack](https://github.com/airbytehq/open-data-stack/)Â project on GitHub, where you will see the core Open Data Stack tools in action.


Either way, I look forward to hearing from you!


---


```
Originally published at Airbyte.com
```

[Discuss on Bluesky](https://bsky.app/search?q=domain%3A%20https://www.ssp.sh/blog/modern-data-stack-struggle-of-enterprise-adoption/)
|
[Pay what you like](https://ko-fi.com/sspaeti)
|
[Modern Data Stack](https://www.ssp.sh/tags/modern-data-stack/)
[Enterprise Data Platform](https://www.ssp.sh/tags/enterprise-data-platform/)
[Open Data Stack](https://www.ssp.sh/tags/open-data-stack/)
