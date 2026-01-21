---
title: "S3 Key-Value Stores, Production Flink Usage, Titan is Terraform for Data, and more..."
subtitle: "Flink's production usage is actually very diverse, we need more transactional key-value stores built on BLOB stores, and dbt meets Terraform with the Titan project."
date: 2023-11-16T11:38:34+00:00
url: https://materializedview.io/p/flink-usage-kv-store-on-s3-terraform-for-data
slug: flink-usage-kv-store-on-s3-terraform-for-data
word_count: 870
---


## Transactional Key-Value Stores on S3


OLTP databases likeNeonandPingCAP’sTiDBcan use S3 as their primary data store. An architecture with a BLOB store as primary storage has many benefits but also presents challenges.Davis Treybigsummarizes the challenges well inS3 as a universal infrastructure backend.


I’ve seen different approaches to these challenges:

1. A key-value-based API layer that implements a consensus protocol and write-ahead log on top of S3 (using local disks for caching). (c.f.TiKV)
2. A WAL-based API. (c.f.The Disaggregated Write-Ahead Log)
3. Read-through caches. (c.f.WarpStream’s [$] distributed mmap)
4. Write-back caches. (c.f.Neon Safekeepers)


The KV-based approach is particularly popular with OLTP systems likeFoundationDBandTiDB, which are built on top of a transactional key-value store. PingCAP talks about their migration in,How PingCAP transformed TiDB into a serverless DBaaS using Amazon S3 and Amazon EBS.


> PingCAP made an improvement to the design and introduced Amazon S3 as a separate storage medium layer. In the new design, TiDB stores most of its data on Amazon S3 while putting Write-Ahead Logs (WALs) on EC2 instance store which provides the lowest latency


I have heard of companies building internal OLTP databases onTiKV. I had hopedRocksDB cloudwould work as well, but I don’t believe it provides the ACID characteristics that OLTP databases need. I’d love to be corrected on this.


We need more open source transactional key-value stores on S3 with a variety of consensus protocols, APIs, and features. Serverless databases could use these stores a building block.


## Production Flink Usage


I got curious aboutFlink’s production usage this week. I expected Flink usage to mostly beanalytics engineeringuse cases and SQL. My hypothesis was born of the deluge ofFlink SQLandchange data capture (CDC)content lately.


![](https://substackcdn.com/image/fetch/$s_!KHnL!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F16f783cf-2d6c-4030-bcdc-16ca3e5b4c90_690x191.png)


To my surprise, Flink’s usage is quite diverse!flink-at-scaleandFlink Forward’sconference programboth have production use cases for ads, realtime pricing, security, and a lot more. Some notable uses:

- Real-Time Exactly-Once Ad Event Processing with Apache Flink, Kafka, and Pinot(Uber)
- Realtime Bot Detection with Flink(Yelp)
- Keeping Redditors safe in real-time with Flink Stateful Functions(Reddit)


## mmap Isn’t So Bad After All?


RavenDB’s CEO,Oren Eini, wrote anexcellent rebuttalto themmap critiqueI shared in myBuffer Pool Refresherpost a few weeks ago. The rebuttal is expertly written.


Oren’s central point is that mmap alternatives are difficult.


> When building a database, using mmap has the following advantages, the OS will take care of:Reading the data from diskConcurrency between different threads reading the same dataCaching and buffer managementEviction of pages from memoryPlaying nice with other processes in the machineTracking dirty pages and writing to disk*… If you aren’t using mmap, on the other hand, youstill need to handle all those issues.


It’s great to see such a well written and fair response. It’s also nice to contrast pragmatic and academic perspectives.


## Project Highlight: Titan


MeetTitan, a project fromTJ Murphy. Think of Titan as a mashup ofdbtandTerraform.


![](https://substackcdn.com/image/fetch/$s_!7UKE!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1d172df9-7e36-456d-a128-aab4f224ea9a_691x328.png)


Terraform works for basic provisioning in the data ecosystem: S3 buckets, BigQuery datasets, Kafka topics, access-control lists (ACLs). For more complex use cases (especially in the data warehouse), data engineers are forced into dbt, Python scripts, templating languages, and custom tools. Other data warehouse users—analytics engineers—often lack Terraform experience.


Tobi Mao(author ofsqlglotandsqlmesh) explains why Terraform-like systems are useful for data in,Why Data Teams Are Adopting Declarative Pipelines. Titan bridges this gap. Here’s an example code-as-config example from theREADME.md:


![](https://substackcdn.com/image/fetch/$s_!UlOs!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F22259719-f5a8-4f56-b8d3-1bc9aebc7c8b_721x592.png)


## More Awesome Infrastructure


Keep up with new projects as they’re added to theawesome-infraGithub repo. New projects and startups welcome! SeeCONTRIBUTING.mdand thePR template.


Major durable execution drop in awesome-infra aftermy last post.

- Temporal- Temporal is a microservice orchestration platform which enables developers to build scalable applications without sacrificing productivity or reliability.
- Azure Durable Functions- Durable Functions is an extension of Azure Functions that lets you write stateful functions in a serverless compute environment.
- Conductor- Conductor is a microservices orchestration engine from Netflix.
- Convex- Convex is a full cloud backend designed to replace your database, server functions, backend functionality, and the interface all the way out to your application.
- coroutine- A durable coroutine compiler and runtime library for Go.
- durabletask-go- The Durable Task Framework is a lightweight, embeddable engine for writing durable, fault-tolerant business logic (orchestrations) as ordinary code.
- Flawless- Flawless is an execution engine for durable computation.
- Infinitic- Infinitic is a general-purpose framework built on Pulsar to reliably orchestrate microservices, manage distributed transactions, operates data pipelines, builds user-facing automation, etc.
- Inngest- Inngest is the developer platform for easily building reliable workflows with zero infrastructure.
- Laravel Workflow- Durable workflow engine that allows users to track job status, orchestrate microservices and write long running persistent distributed workflows in PHP powered by Laravel Queues.
- LittleHorse- LittleHorse is a high-performance microservice orchestration engine that allows developers to build scalable, maintainable, and observable applications.
- Rama- Rama is a new programming platform that combines databases and stream processing with fault-tolerant computation.
- Resonate- Resonate is a lightweight durable execution engine made to help you keep your promises.
- Restate- Write RPC and event handlers, and Restate makes them reliable by adding durability to invocations, promises, communication and state.


---


I occasionally invest in infrastructure startups. Companies that I’ve invested in are marked with a [$] in this newsletter. See myLinkedIn profilefor a complete list.
