---
title: "Ce n'est pas un Kafka: Kafka is a Protocol"
subtitle: "Apache Kafka is an aging open source project. It's time to accept that Kafka's protocol is what matters."
date: 2024-03-25T10:50:20+00:00
url: https://materializedview.io/p/ce-nest-pas-un-kafka
slug: ce-nest-pas-un-kafka
word_count: 661
---


Confluentannounced TableflowatKafka Summitthis past week.TableflowintegratesConfluent Cloudwith open table formats likeApache Iceberg. Confluent’s Kafka can now write to tiered storage (object stores likeS3) usingParquetfiles andIcebergmetadata. I have been preaching about this idea for a while.


![](https://substackcdn.com/image/fetch/$s_!lALo!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F24c4c1f5-c6da-456d-90c1-82f9eada3ed9_1384x1084.png)


Jack Vanlightlydescribes Confluent Cloud’s (Kora’s) implementation:


> Firstly, we can replace the native tiered storage format with Parquet files and Iceberg metadata directly. This creates a zero-copy storage representation of a stream as a single coherent dataset across Kora brokers and object storage. The Kora storage engine handles this Iceberg/Parquet storage tiering, object storage file compaction, retention, storage optimization, and schema evolution between Kafka topic schemas and Iceberg tables.


This feature, along with other developments, has really driven home how varied Kafka implementations have become. Kafka is now a protocol, not an Apache project. The Apache project is just one (aging) implementation.


Confluent, themselves,think about Kafka this way:


> Just like theApache Kafka API has evolved to be the de facto open standard for data streaming, we’re seeing Apache Iceberg evolve into the de facto open-table standard for large-scale datasets stored in lakehouses.


Confluent Cloud’s feature set has so diverged from Apache Kafka that it’s nearly unrecognizable. Confluent has offered tiered storage since at leastJanuary, 2020. Meanwhile, Apache Kafkajust got tiered storage in 3.6.0, released in October, 2023. It’s not even ready for production yet—still early access.


And now Confluent Cloud is offering Parquet and Iceberg integration.KIP-1008is trying to add similar support for the Apache project. But the design needs a lot of work and the discussion hasdied. It’s unlikely Apache users will get this feature anytime soon.


Looking beyond Confluent, the ecosystem is still more diverse.WarpStream[$] has built a truly serverless implementation of Kafka using only object stores for persistence.Redpandahas had a C++-based Kafka implementation for years; they’re now trying tomorph into a serverless platform.AutoMQforked Kafka to add tiered storage.S2is on the cusp of launching itswrite-ahead log(WAL) with Kafka protocol compatibility. EvenStreamNativehasembraced the Kafka protocolon top ofApache Pulsar.


The evolution of popular open source infrastructure into a protocol is not unique to Apache Kafka.Redis’sprotocol is widely adopted, as isPostgreSQL’s(something I wrote about inDatabases are Commodities. Now What?). Even closed source systems like S3 have seen their protocols adopted as the de facto standard. Successful infrastructure is destined to be a protocol.


![](https://substackcdn.com/image/fetch/$s_!Klaq!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd7baee23-37ef-4313-b2ea-c79786e75587_683x168.png)


I’m OK with this. Though I’m no longer a CFLT shareholder, I recognize the need to make money. The Apache process, too, can be slow. Businesses sometimes need to move faster. And congregating around the protocol means vendors can try different things—different manifestations of the platonic ideal that is the protocol spec.


Frankly, I don’t see a pure open source business—a laHortonworks—as a viable model. I am not alone in this; several open source developers have recently confided in me the same feeling. A post for another day.


All of this begs the question: what responsibility—if any—do companies have to their open source roots, or to the protocol itself? I don’t have a good answer. What I can offer is that clear communication is important.


Many companies find this uncomfortable. They worry—rightly so—that they’ll alienate users and suffer brand damage if they explicitly abandon their open source roots. Touching the proverbial open source third rail, so to speak. So they opt for strategic ambiguity.


Users are going to have to get comfortable inferring a company’s intentions based on their actions. In the case of Confluent and Kafka, it’s pretty clear that we have graduated from an Apache project to an open protocol. I’m excited about this (of course, I have a vested interest). The products we’re getting—Confluent Cloud, WarpStream [$], Redpanda, S2, and AutoMQ—are genuine improvements with (hopefully) sustainable business models.


---


Share


---


Support this newsletter by purchasingThe Missing README: A Guide for the New Software Engineerfor yourself or gifting it to someone.


![](https://substackcdn.com/image/fetch/$s_!CI0B!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fde442631-41a6-4119-a99a-62957cd53edb_870x978.png)


Buy Now


---


I occasionally invest in infrastructure startups. Companies that I’ve invested in are marked with a [$] in this newsletter. See myLinkedIn profilefor a complete list.
