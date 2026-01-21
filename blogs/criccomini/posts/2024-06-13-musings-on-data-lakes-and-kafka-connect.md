---
title: "Musings on Data Lakes and Kafka Connect"
subtitle: "ParadeDB launches pg_lakehouse, I explore how best to serve data from data lakes, and Kafka Connect needs some fixing."
date: 2024-06-13T18:25:32+00:00
url: https://materializedview.io/p/musings-on-data-lakes-and-kafka-connect
slug: musings-on-data-lakes-and-kafka-connect
word_count: 915
---


## ParadeDB Releases pg_lakehouse


It’s official:ParadeDBreleasedpg_lakehouse(Hackernewsusersfound the code in May). pg_lakehouse is an extension that converts PostgreSQL into a query engine for data lakes and lakehouses. Developers can easily query their data lake fromPostgreSQLwithout a bulky query engine likeTrino,Presto, orApache Spark.


PostgreSQL is a mature database with many tools and features; building on it has many benefits. PostgreSQL has roles and privileges for security, something I’ve complained thatDuckDB lacked. And PostgreSQL comes with a shared cache that pg_lakehouse could take advantage of. And if pg_lakehouse supported writes, it could be used to ingest data into lakehouses. Another wild idea is to embed pg_lakehouse insidepgliteto directly query data lakes from the client (likeDuckDB).


pg_lakehouses is built on top ofApache OpenDALandApache DataFusion. I’ve written about the importance of DataFusion before, but Apache OpenDAL is just as notable. I’ve been followingXuanwo, OpenDAL’s creator, for some time. I’m very impressed with the work he’s doing (especially on Apache Iceberg’s Rust client, which sorely needs better non-Java clients). pg_lakehouse is proof thatcomposable data systemsare not only possible, but are already here.


## Serving Lakehouse Data In Production


Continuing with the lakehouse theme, I’vebeen thinkingabout how to best serve data lake and lakehouse data back to production. This was a common use case at LinkedIn. We pre-computed data in Hadoop and then pushed the data toVoldemortusing abuild and push job.


Systems have changed but the pattern remains the same. Data is computed in acloud data warehouse(CDW) likeSnowflakeorBigQuery, a data lake, or data lakehouse. Manyanalytics engineersare eager to contribute to product development. The most natural pipeline to get their data back into production is from the data warehouse or lake.


Reverse ETL, pushing data from the DWH to external SaaS applications, is a similar pattern. But I’m interested in exposing the analytics engineer’s data back into productionwithinthe organization, not across external SaaS apps. What I want is a cache that sits in front of warehouse data and exposes it through a low-latency API. Production services can then read the data. Analytics engineers can recompute data to push new changes to production transparently.


There are many ways to build this pipeline. A reader likeROAPIcan expose warehouse data to production applications. Low latency databases likeStarRocksorSingleStorethat can read data lake data. Data can also be streamed from a data lake back into production with a system like LinkedIn’sVenice.


I really like the simplicity of the first approach—a caching service that fronts the lakehosue. Like pg_lakehouse, ROAPI uses Apache DataFusion to expose “slow moving data” via SQL, GraphQL, and REST APIs. Plunk it down in front of your Deltalake or Parquet files and it’ll serve them right up.


Unfortunately, ROAPI doesn’t have a caching layer. I have to believe that the author (QP Hou) is trying to keep it simple. But a cache would make it useful when developers wish to serve Parquet data from object storage for low-latency queries (i.e. user-facing features). Even better, a partitioned cache using something likerendezvous hashingwould allow ROAPI to create a cache across multiple instances.


This is where systems likeRockset,SingleStore,Apache Doris, andStarRocksexcel. Like ROAPI, developers can mount object storage data into their query engine. Unlike ROAPI, though, these databases ingest or cache the data, which makes them suitable for low latency production workloads. The don’t seem to offer GraphQL and REST APIs the way ROAPI does, unfortunately.


## Improving Kafka Connect


There’s been a lot of chatter aboutBento,Benthos(a.k.a.Redpanda Connect), andKafka Connectlately. I mentioned theRedpandadrama inmy previous post.Jay Kreps, the CEO of Confluent, posted a thread encouraging developers to centralize around an open platform like Kafka connect.


I like this sentiment, but Kafka Connect is anaging platform. Developers have been talking about how to improve it.Chris Egerton, my former teammate at WePay, has (jokingly?) proposed forking it to build a bridge without Kafka.


![](https://substackcdn.com/image/fetch/$s_!w_cO!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe51bff1f-bafd-4d91-8a70-e7064437b85d_1372x246.png)

*View Post*


This idea sounds a lot like Bento and Redpanda Connect to me. A few years ago,Gunnar Morling, an engineer at Decodable, wrotea great postproposing Kafka Connect with Kubernetes instead of its built-in scheduler and orchestrator.Ryanne Dolanwrote about similar ideas inControl Planes and the Death of the Cluster.


> Consider the example of runningKafka Connect at Twitter Scale. We had to dumb-down Connect's cluster management features and bypass the HTTP API in order to achieve our goals. Instead of sending HTTP requests to the Connect API, we loaded YAML directly from within the workers. We couldn't put different types of workloads together onto the same cluster, since they'd compete for resources in unpredictable ways. So we had dedicated clusters for each type of workload. The workloads within each cluster were so similar that we had cluster-level defaults. A new workload came down to: pick the right cluster and add a couple lines of YAML. The "Connect-as-a-Service" part of Connect was completely absent.


We had an eerily similar experience running Kafka Connect at WePay.


![](https://substackcdn.com/image/fetch/$s_!PNqN!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb72aab4c-8b10-4b61-8183-ab69788e4f26_1370x366.png)

*View Post*


I haven’t kept up with the Kafka Connect community, so I don’t know if they’re planning to address issues like connector isolation, scheduler complexity and so on. I do think it’s healthy for competitors like Bento and Redpanda Connect to present alternatives. I hope things stabilize; we could use a healthy, easy to use connector framework.


---


#### Book


Support this newsletter by purchasingThe Missing README: A Guide for the New Software Engineerfor yourself or gifting it to someone.


![](https://substackcdn.com/image/fetch/$s_!CI0B!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fde442631-41a6-4119-a99a-62957cd53edb_870x978.png)


Buy Now


---


#### Disclaimer


I occasionally invest in infrastructure startups. Companies that I’ve invested in are marked with a [$] in this newsletter. See myLinkedIn profilefor a complete list.
