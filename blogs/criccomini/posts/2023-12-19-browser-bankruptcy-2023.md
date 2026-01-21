---
title: "Browser Bankruptcy 2023: Consensus, Durable Execution, Streaming, HTAP, TSDBs, and more..."
subtitle: "Everything in my tabs as I close out the year. Catch you in '24!"
date: 2023-12-19T11:13:19+00:00
url: https://materializedview.io/p/browser-bankruptcy-2023
slug: browser-bankruptcy-2023
word_count: 706
---


I started this blog onOctober 31, 2023. It’ll be 2 months old as we start the new year. It’s been fun to write and I plan to keep it going in the new year. If you haven’t yet read my most popular post, it’s a good place to start:

[Durable Execution: Justifying the Bubble](https://materializedview.io/p/durable-execution-justifying-the-bubble)
[Chris Riccomini](https://substack.com/profile/69592459-chris-riccomini)
·
November 13, 2023

There’s been a surge in durable execution frameworks over the past 6 to 12 months. Temporal has been the go-to for a while but many new projects and companies are emerging. Let’s look at why, and what needs to change. Durable execution explained Temporal’s

[Read full story](https://materializedview.io/p/durable-execution-justifying-the-bubble)

Rather than a recap or predictions post, I thought it’d be fun to share what I’ve got in my browser tabs—stuff I haven’t been able to get to yet. I hope you find a link or two that pique your interest.


---


## Consensus


Viewstamped Replicationsucked me back into consensus protocols this year.

- The Leadership Myth in Replicated Databases
- Nezha: Deployable and High-Performance Consensus Using Synchronized Clocks
- Building a Large-scale Distributed Storage System Based on Raft


## Workflows, FaaS, durable execution


Durable executionblew up this year.

- Singularity: Planet-Scale, Preemptive and Elastic Scheduling of AI Workloads
- A FaaS File System for Serverless Computing
- Lifting the veil on Meta’s microservice architecture: Analyses of topology and request workflows
- Towards Modern Development of Cloud Applications
- Alluxio: A Virtual Distributed File System


## Streaming


The trend toward S3 persistence for streaming (withWarpStream[$]) captured my interest.

- Kora: A Cloud-Native Event Streaming Platform For Kafka
- Clonos: Consistent Causal Recovery for Highly-Available Streaming Dataflows
- Streaming from Apache Iceberg - Building Low-Latency and Cost-Effective Data Pipelines
- DBSP: Automatic Incremental View Maintenance for Rich Query Languages


## HTAP/multi-model databases


As IdugmoreintoS3 persistence, I found plenty of other exemplary systems (e.g.Neon,Turbopuffer,Quickwit). I’ve been thinking lately about what it means to have all our data directly on S3. Does it makehybrid transaction/analytical processing(HTAP) andmulti-model databaseseasier to build or more likely to be successful?

- Running OLAP and OLTP Workloads on the Same Cluster with Workload Prioritization
- Introducing Compute-Compute Separation for Real-Time Analytics
- The Beauty of HTAP: Defining a Modern Data Architecture with TiDB
- Cloud-Native Transactions and Analytics in SingleStore
- Why I left IBM to work on CockroachDB


## Embedded databases


Litestream,LiteFS,libsql,Turso, andSKDBhave me pulling at the embedded (and edge) DB thread.

- Stop Building Databases
- Building data-centric apps with a reactive relational database
- Parallel Python within the same process or hacking around the cursed GIL with a hand-rolled library loader
- Embedded databases (1): The harmony of DuckDB, KùzuDB and LanceDB
- TreeLine: An Update-In-Place Key-Value Store for Modern Storage
- What Modern NVMe Storage Can Do, And How To Exploit It: High-Performance I/O for High-Performance Storage Engines


## Time-series databases


SomePrometheus (and frostdb) spelunkingled me toInfluxDB’snew(ish)IOx storage engine, which usesDatafusionandParquet.

- Intro to InfluxDB IOx
- Welcome to InfluxDB IOx: InfluxData’s New Storage Engine


## PosgreSQL


PostgreSQLand its extensions continue to be a pragmatic solution to, well, everything.

- Introducing pgroll: zero-downtime, reversible, schema migrations for Postgres
- The Great Re-shard: adding Postgres capacity (again) with zero downtime


## Analytics


Analytics Twitter continues to be very—obnoxiously—loud.

- Capturing Data Evolution in a Service-Oriented Architecture
- Why we develop on data locally and how to finally stop (Part 1)
- Riverbed: Optimizing Data Access at Airbnb’s Scale
- A Deep Dive into Common Open Formats for Analytical DBMSs
- Lakehouse: A New Generation of Open Platforms that Unify Data Warehousing and Advanced Analytics
- Lineage Stash: Fault Tolerance Off the Critical Path
- Don’t Hold My Data Hostage – A Case For Client Protocol Redesign
- The Story of AWS Glue
- What if an SQL Statement Returned a Database?
- Procella: Unifying serving and analytical data at YouTube
- The Composable Data Management System Manifesto


---


Share


---


You can support me by purchasingThe Missing README: A Guide for the New Software Engineerfor yourself or gifting it to new software engineers that you know.


Buy Now


---


I occasionally invest in infrastructure startups. Companies that I’ve invested in are marked with a [$] in this newsletter. See myLinkedIn profilefor a complete list.
