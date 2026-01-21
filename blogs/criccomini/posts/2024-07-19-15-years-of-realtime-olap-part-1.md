---
title: "15 Years of Realtime OLAP (Part 1)"
subtitle: "A brief history of Avatara, Apache Pinot, and Apache Druid."
date: 2024-07-19T19:33:33+00:00
url: https://materializedview.io/p/15-years-of-realtime-olap-part-1
slug: 15-years-of-realtime-olap-part-1
word_count: 1212
---


Materialized View has crossed 3,000 subscribers! Growth continues to be up and to the right. I can’t say thank you enough, but… thank you.


In other news,Gablehas taken ownership ofRecap. I open sourced Recap as an open sourceportable data catalog18 months ago. Since then, it’s grown into afull-blown type systemthat reads and models schemas across data warehouses, streaming systems, and web service APIs. Exactly the kind of thing that’s useful if you’re working ondata contracttools, which Gable is! I’m happy to see it continue to grow and evolve. I’ll still be around to review PRs, too.


---


ClickHousehas been coming up in a lot of conversations. I planned to write about it this week, but found myself writing about the history of realtimeonline analytical processing(OLAP) instead. I’ll get back to ClickHouse in a forthcoming post, but I first want to motivate some of its use cases. You’ll have to indulge me with this.


My first brush with realtime OLAP came 15 years ago atLinkedIn. We had a product calledWho’s Viewed My Profile(WVMP). At the time, WVMP showed users a time-sorted list of users that had viewed their profile. It was a classic vanity metric. Naturally, the product was popular and drove considerable subscriber revenue.


We decided our users wanted a better experience. Profile viewers had a lot of rich data—companies, schools, regions, and so on. Product and design mocked up a WVMP dashboard that showed profile views over time. Today’s WVMP product still contains the original chart:


![](https://substackcdn.com/image/fetch/$s_!ku6K!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0bc7ef79-f6a1-4942-8aff-188a8b858457_795x417.png)

*Who’s Viewed My Profile*


Such charts are commonplace in the business analytics domains. Internal stakeholders—product managers, analysts, data scientists, and engineers—write queries and build dashboards exactly like the charts show in WVMP. This query pattern is often called online analytical processing (OLAP). IBM hasa decent definition:


> OLAP, or online analytical processing, is technology for performing high-speed complex queries or multidimensional analysis on large volumes of data in adata warehouse,data lakeor other data repository.


OLAP developed many fancy concepts—cubes, dimensions, measures, and so on. But it’s really just SELECT COUNT(*) FROM … GROUP BY queries. Data warehouses likeSnowflake,BigQuery,Vertica,Teradata, andRedshiftare all OLAP systems.


But Who’s Viewed My Profile had several differentiating characteristics:

1. Reports were shown to external users.
2. Users were allowed to pivot and filter the data.
3. Reports showed intra-day data.


Data warehouses are built to handle queries on large data sets but with slower response times (seconds to minutes). WVMP requires millisecond response times since end-users are waiting for the page to load. Our warehouse didn’t have the response times we needed. Nor did it have the required data freshness. Data was loaded daily in a batch process; it didn’t have intra-day data. Furthermore, our data warehouse was isolated from our production environment—we couldn’t even query it from the web services that were handling WVMP requests.


LinkedIn’s primary production data store wasOracle. We could have built WVMP on top of Oracle. The database probably could have sustained the load, but the hardware and operational effort needed to house and serve the data was substantial.


One of the few alternatives we had wasVoldemort, a key-value store. Voldemort is a key-value store that serves reads with single-millisecond latency and integrates with Hadoop (our data warehouse at the time) through abuild and push job.


We decided to periodically calculate WVMP statistics in our data warehouse (Apache Hadoop), push the data to Voldemort, and serve the aggregates from there. This is amaterialized view(the inspiration for this newsletter’s name!). We built a system calledAvatarato manage the computation, data push, and serving.


Avatara met our needs. GET requests to Voldemortare very fast. Our design was not without its challenges, however. Users were limited to pivots that we had already calculated; they could not group or filter profile views by dimensions we hadn’t pre-computed. A single profile view resulted in one write (or increment) for each combination of dimensions—high write amplification. Pre-materializing all the data also took a lot of storage space. And pre-computing the data in Hadoop meant our data was always a few hours stale. Eventually, we used Kafka events to update Voldemort counts in realtime, but the write amplification and rigid query challenges remained.


Avatara caught the eye ofEric Tschetter, another engineer at LinkedIn. Eric was on an adjacent team and gave us a lot of feedback on our project. His gears were turning, and he eventually went on to become the founding engineer and VP of engineering atMetaMarkets. There, he worked withFangjin Yangand others to createApache Druid.


Druid aimed to fix Avatara’s problems by foregoing pre-materialization. Instead, Druid would use acolumnar storage formatas many classic OLAP stores did. The problem with columnar storage is that you need to write out chunks of rows rather than a single row at a time; something I discuss inNimble and Lance: The Parquet Killers.


Druid had a clever solution to the batch-write problem: store recently ingested in-memory as well. Data in memory was asynchronously flushed to columnar file segments. Queries could then read recent data from memory and older data from columnar files on disk (or object storage).


This design solved a lot of problems. Data could be ingested through Kafka topics in realtime because writes simply went to memory. Ingested data was immediately available for reads. Users could query the data however they liked because there was no pre-materialization. Storage space was also reduced. And there were decades of research in columnar systems to draw from.


Meanwhile, a few years after Avatara was launched, another engineer namedKishore GopalakrishnacreatedApache Pinot﹩. (At the time, Druid was either not open source, or was released under a restrictiveGPL license.) Kishore and his team set out to build a system that could service low latency user-facing queries like Avatara, but do so without restricting users to pre-computed query patterns. They wanted to solve the same problems as Druid.


As with Druid, Pinot used columnar storage and in-memory buffering. But they also included a new feature:star-tree indexes. Star-trees give operators a knob to tune, trading off space for query latency. Though data was stored in columnar files as with Druid, for very fast (single-digit millisecond) reads, data could be partially pre-materialized. Pinot became widely adopted within LinkedIn and Uber for internal business intelligence, user-facing analytics features, log analytics, metrics, and more.


While Kishore and his team worked on Pinot, I began work onApache Samza. In 2015, I left LinkedIn to join WePay. Upon joining, I bumped into my second realtime OLAP use case while helping our risk and fraud team.


My next few posts will cover WePay’s fraud query patterns and how these two experiences inform my broader understanding of realtime OLAP. With that out of the way, we can then explore ClickHouse.


NOTE: There are also a bunch of papers and technologies from other companies, particularly Google. I’m probably missing a lot of backstory here. This is just my experience with the space. Shoot me a direct message or email if you feel I’ve missed anything.


---


Share


---


#### Book


Support this newsletter by purchasingThe Missing README: A Guide for the New Software Engineerfor yourself or gifting it to someone.


![](https://substackcdn.com/image/fetch/$s_!CI0B!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fde442631-41a6-4119-a99a-62957cd53edb_870x978.png)


Buy Now


---


#### Disclaimer


I occasionally invest in infrastructure startups. Companies that I’ve invested in are marked with a ﹩ in this newsletter. See myLinkedIn profilefor a complete list.
