---
title: "Small Batch, Artisanal ETL is Back"
subtitle: "Batch ETL is back, and we're brining everyone this time!"
date: 2024-10-10T09:59:35+00:00
url: https://materializedview.io/p/small-batch-artisanal-etl-is-back
slug: small-batch-artisanal-etl-is-back
word_count: 714
---


I joinedThe Geek Narratorto talk aboutSlateDBlast week. This is the most complete description of what SlateDB is, why we built it, and how it works (at least until ourP99 CONFtalk later this month). Check out the video below for the full interview:


Speaking of P99 CONF, I did a littlespeaker spotlightwith them last week. I talk about the projects I’m working on and which talks I’m most excited about at P99 CONF.


---


In 2019, I gave aQContalk entitledThe Future of Data Engineering. It discussed the evolution of our data pipeline atWePayover the years. The talk presents a series of steps that most organizations go through when building pipelines:

- Stage 0: None
- Stage 1: Batch
- Stage 2: Realtime
- Stage 3: Integration
- Stage 4: Automation
- Stage 5: Decentralization


I won’t discuss each one of these (seethe videoor readthe blog), but one point I make in the talk is that it’s reasonable, if not suggested, to take your time with this evolution. It’s possible you won’t even need the latter stages. In fact, WePay had a batch data pipeline—stage 2—running onAirflownearly the entire time I was there. It ran at 15m intervals and it was remarkably effective.


These days, the ETL ecosystem is very diverse. An enterprise can still stand up an ETL pipeline like WePay’s using Airflow,Prefect, orDagster. Or an enterprise might choose to adopt a data integration platform such asAirbyte,Fivetran, orKafka Connect. Many cloud providers offer one-click integration between their cloud SQL services and their data warehouses as well.


For many smaller organizations, these tools are overkill. Though I don’t fully agree withMotherDuck’sBig Data is Deadthesis, they’re right that a lot of organizations just have a few terabytes of data. Developers are thinking: if I can get by with a small query engine (DuckDB), maybe I can get by with a small ETL tool.


Pipeline ownership has shifted as well. WePay had a team of data engineers to manage our data pipelines. These days, we’re asking ML, AI, analytics, and product engineers to build data pipelines. These users are used to interacting with data in a different way. They like to transform data in batch through SQL and Python with tools likedbt,Jupyter notebooks, andPandas data frames. They want an ETL tool that integrates with this flow.


The closest thing that I’ve come across so far isdata load tool (dlt). As the name suggests, dlt is philosophically similar to dbt;it’s trying to give these new users a tool that fits into their flow, but that incorporates software development life cycle (SDLC) best practices. Unlike dbt, which focuses more on transformations, dlt offers sources and sinks and a simple API to work with:


> The proliferation of Python libraries such as Pandas, Jupyter notebooks, NumPy or PyTorch revolutionised the ML/AI space by allowing millions of practitioners to actively build the ecosystem.We aim to bring such revolution to the data space. dlt is a pip-installable, minimalistic library that anyone writing Python code can use. dlt enables those people to create new datasets and move them to tools they use - be it other Python projects or engines or tooling from the Modern Data Stack.


dlt fits nicely into many so-calledmodern data stack (MDS)tools out there, but also runs on its own. It’s a nice stepping stone from step 1 to step 2 in my stage-list, above.


There are challenges to this approach. If everyone is managing their own data pipelines, there will duplication. There is also likely to be inefficiency as engineers opt for simpler solutions rather than cheaper ones. Moreover, the pipelines could become a tangled mess with no clear ownership as employees come and go. These challenges are probably familiar to anyone working with dbt in a large organization.


But I think dlt has recognized something: data consumers want control of their data pipelines. I’m excited to see where this goes. There’s a lot of work to be done to get this right.


---


#### Book


Support this newsletter by purchasingThe Missing README: A Guide for the New Software Engineerfor yourself or gifting it to someone.


![](https://substackcdn.com/image/fetch/$s_!CI0B!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fde442631-41a6-4119-a99a-62957cd53edb_870x978.png)


Buy Now


---


#### Disclaimer


I occasionally invest in infrastructure startups. Companies that I’ve invested in are marked with a ﹩ in this newsletter. See myLinkedIn profileandMaterialized View Capitalfor a complete list.
