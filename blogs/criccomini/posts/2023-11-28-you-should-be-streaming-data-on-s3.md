---
title: "You Should Be Streaming Data on S3, Neon DB Is a Masterpiece, a Reactive Edge DB, and more..."
subtitle: "Streaming on S3 is finally here; Jack Vanlightly does a Neon tech teardown; and SKDB is the coolest database you don't know about."
date: 2023-11-28T11:08:27+00:00
url: https://materializedview.io/p/you-should-be-streaming-data-on-s3
slug: you-should-be-streaming-data-on-s3
word_count: 475
---


## You Should Be Streaming Data on S3


More and more people are buying into the idea that S3 is a good storage layer for streaming.


![](https://substackcdn.com/image/fetch/$s_!-NQH!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F90b2e5a9-0ec6-486a-b573-babdb6562476_690x436.png)


The three projectsYingjunmentions show three different architectures.

- S3 as source of truth:WarpStream[$] is a stateless Kafka protocol-compatible system where S3 acts as the source of truth for all data.
- Tiered storage:AutoMQimplements Kafka’sRemoteStorageinterfaces to provide tiered storage on S3. Unlike WarpStream, AutoMQ still has Kafka brokers that store a small amount of data on EBS.RedPandaalso supports tiered storagewith a Kafka-compatible API.


![](https://substackcdn.com/image/fetch/$s_!Wvrb!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F00d175dc-ced8-4b24-978b-7aa14e272de6_694x331.png)

- Streaming data lakes:Paimonis not a Kafka-compatible messaging system. Instead, Paimon is a streaming data lake (similar toHudi). Data isingested via engineslike Flink, Spark, or Hive (only Flink and Spark support streaming writes).


And Kafkafinally has tiered storagein 3.6.0 (as an early-access feature). I had assumed this was already available, but it turns out Confluentwas keeping it as a paid feature.


## Neon DB Is a Masterpiece


Jack Vanlightlyhas been on a tear withserverless postslately. Hislatest postis aNeonarchitecture teardown. I recommend reading bothJack’s postand the AWS’sAurora paperthat Neon is based on.


Neon takes PostgreSQL and replaces its storage layer with remote storage interfaces. The two components of the remote storage are a remote WAL and a page service that sits atop a BLOB store like S3.


Neon is such an elegant project. Some notes:

- Neon usesQEMUinstead of microVMs for live migration.
- Neon’s Postgres has been patched to allow WAL and page service calls to go over network. These changes are not yet upstream.
- Designers chosePaxosnotRAFTbecause it worked nicely with their service design (clients, safekeepers, and pageservers).


I hadn’t come across QEMU before (orDRDB, which Jack also mentions). Neon chose QEMU—a full VM—overFirecrackerbecause they wantedlive migration. Firecracker and gvisor both only support snapshot and restore.


## Project Highlight: SKDB


SKDBis a new kind of database: a reactive edge database that supports materialized views, table subscriptions, and diff’ing. Unlike SQLite and libsql, SKDB is rebuilt from the ground up to support such use cases.


> SKDB is inspired by SQLite and supports the same subset of SQL (including transactions). What sets it apart is that it is also highly concurrent. SKDB supports processing complex queries from multiple simultaneous readers/writers without stalling other database users.


The project is quite young—a proof-of-concept—but it has on some really interesting building blocks: SkipStore and Skiplang. Stay tuned to learn more in my upcoming podcast interview withJulien Verlaguet, the CEO ofSkipLabs.


## More Awesome Infrastructure


Keep up with new infrastructure projects as they’re added toawesome-infra. New submissions are welcome!

- OneTable- OneTable is an open source project that provides omni-directional interoperability between lakehouse table formats such asApache Hudi,Apache Iceberg, andDelta Lake.


---


Share


---


I occasionally invest in infrastructure startups. Companies that I’ve invested in are marked with a [$] in this newsletter. See myLinkedIn profilefor a complete list.
