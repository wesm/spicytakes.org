---
title: "From Samza to Flink: A Decade of Stream Processing"
subtitle: "Why Samza failed, how it led to Kafka Streams and Kafka Connect, and why I'm skeptical of Apache Flink."
date: 2024-02-20T11:24:15+00:00
url: https://materializedview.io/p/from-samza-to-flink-a-decade-of-stream
slug: from-samza-to-flink-a-decade-of-stream
word_count: 2118
---


I am investor inResponsive, a managed stateful Kafka Streams provider. The history and lessons in this post influenced my decision to invest in Responsive, and my excitement in their product.


---


I startedApache Samzatwelve years ago during my tenure at LinkedIn. Samza was a stream processing framework built forApache Kafka. The team grew to include all-stars likeMartin Kleppmann,Chinmay Soman,Jakob Homan,Yi Pan, and many other talented engineers. Together, we added support forstateful processing,batch processing,SQL,YARN,standalone deployment, and many other features you see in modern stream processing systems. I learned a lot building Samza. In this post, I want to review Samza’s history, look at lessons learned, and talk about how these lessons affect my thinking onApache Flink.


## A Brief History of Samza


Before Samza, developers at LinkedIn used microservices to send and receive Kafka messages. Common patterns began to emerge. Some microservices existed only to consume and produce messages; they never received RPC calls. Others would consume messages and accumulate state—counting events, grouping messages, buffering, and so on. Still others had complex partitioning logic that required them to take control of Kafka’sconsumer rebalancing protocol. Some would trigger RPC calls to other microservices as events arrived in Kafka topics. We decided that we could help developers by providing them a tool to process Kafka streams—a stream processing framework.


I began working on Samza in 2012 under the tutelage ofJay Kreps. At the time, the most popular streaming system wasApache Storm. Storm’s architecture presented several challenges that we wanted to fix with Samza:

1. Storm included a transport layer: ZeroMQ. ZeroMQ was a thin wrapper around TCP/IP. This seemed dubious to us. Why use ZeroMQ when we had Kafka? ZeroMQ wasslightlylower latency, but you lose a lot when you implement your own transport layer. You have toimplement transactions, partitioning, buffering, ingest connectors, egress connectors, and a lot more. Kafka handles all of this.
2. Storm included its own orchestration layer. Deployments required ZooKeeper, job trackers, and task managers. (I’m forgetting the actual names, but you get the idea.) Again, this seemed duplicative. We were already running Hadoop at the time, and Hadoop 2.0 shipped withYARN, a new general-purpose scheduler and orchestrator.
3. Storm didn’t manage state. State is the hardest part of stream processing. Most of what you want to do with streaming involves accumulating state across multiple events. This is true for counting, summing, grouping, joining, buffering, and a lot more. To get accurate counts, you need to keep your state in sync with the point you’ve read up to in the stream (otherwise you double-count). Storm didn’t help with this.


Samza fixed the transport layer problem (1) by using Kafka for all message passing. We fixed the orchestration problem by using YARN (2).


Jay had a novel technique for managing state (3). He wanted to colocate the statein Kafka, a radical idea at the time. Samza would record state changes as messages in Kafka, and use that as the source of truth. A localLevelDBcache would be kept to do point lookups (it was quickly switched toRocksDB). We were planning to make Kafka transactional (it wasn’t at the time), so we knew we would be able to use Kafka transactions to keep our state in sync with input and output messages.


All of this was pluggable, too. Though Kafka was the first-class transport layer, we supported other implementations. The same was true for the state store and orchestration layer.


## Lessons Learned


We went on a talking spree after we open sourced Samza. We did presentations at Netflix, Hortonworks, QCon, and others. MyQCon SF 2013 talkis worth watching if you want to learn about the state of the art at the time.


Companies began to adopt Samza. Ex-LinkedIn developers brought Samza to Uber. Slack picked Samza up. Expedia used it. But growth was slow. Some of our architectural decisions were causing problems. I wrote an email to the dev@ list entitled,Thoughts and obesrvations (sic) on Samzain June of 2015. The email listed three headwinds:

- Samza is dependent upon a dynamic deployment system (YARN, Mesos).
- Samza is too pluggable.
- Samza's SystemConsumer/SystemProducer and Kafka's consumer APIs are trying to solve a lot of the same problems.


The post goes into a lot of detail about each point. The deployment problem was particularly acute.


> Samza strongly depends on the use of a dynamic deployment scheduler such as YARN, Mesos, etc. When we initially built Samza, we bet that there would be one or two winners in this area, and we could support them, and the rest would go away. In reality, there are many variations. Furthermore, many people still prefer to just start their processors like normal Java processes, and use traditional deployment scripts such as Fabric, Chef, Ansible, etc. Forcing a deployment system on users makes the Samza start-up process really painful for first time users.


Our belief that there would be a single winner was right, but it would take years for Kubernetes to come out on top.


Samza had pluggable configs, metrics, orchestrators, consumers, producers, serializers, storage engines, and partitioning strategies. Literally every part was pluggable. This was great for LinkedIn because we had proprietary implementations for many of these layers. For open source users it was a rats nest of configuration. Try as we might, the onboarding experience was rough.


And, though we’d decided to leverage Kafka for Samza’s transport layer, we still had a pluggable interface. This allowed us to support other systems likeHDFSandKinesis, but it also created a leaky abstraction. Many functions in Samza’s consumer and producer APIs only worked with Kafka.


These challenges led us to propose the following changes:


> 1. Make Samza standalone the *only* way to run Samza processors, and eliminate all direct support for YARN, Mesos, etc.2. Make a definitive call to support only Kafka as the stream processing layer.3. Eliminate Samza's metrics, logging, serialization, and config systems, and simply use Kafka's instead.


Astute readers will note that this is effectively Kafka Streams. Jay and Ewen Cheslack-Posava (Confluent’s founding engineer) followed on witha proposal to create copycat, an Kafka-based ETL system:


> So the thought experiment was, given that Samza was basically already totally Kafka specific, what if you just embraced that and turned it into something less like a heavyweight framework and more like a third Kafka client--a kind of "producing consumer" with state management facilities. Basically a library. Instead of a complex stream processing framework this would actually be a very simple thing, not much more complicated to use or operate than a Kafka consumer. As Chris said we thought about it a lot of what Samza (and the other stream processing systems were doing) seemed like kind of a hangover from MapReduce.Of course you need to ingest/output data to and from the stream processing. But when we actually looked into how that would work, Samza isn't really an ideal data ingestion framework for a bunch of reasons. To really do that right you need a pretty different internal data model and set of apis. So what if you split them and had an api for Kafka ingress/egress (copycat AKAKIP-26) and a separate api for Kafka transformation (Samza).


To anyone familiar with the Kafka ecosystem, this is obviously describing Kafka Connect.


The proposal to simplify Samza was met with skepticism among the broader Samza community, and the discussion eventually died. Samza would remain as it was. Confluent would go on to create Kafka Streams and Kafka Connect on their own.


## Unpacking Use Cases


When I look back at these emails, I see us wrestling with different use cases. There are at least three popular use cases for stream processing:

1. Production features
2. Analytical queries
3. Extract, transform, load (ETL)


Production stream processing jobs create features for products, or to detect anomalies in production workload. Examples include Yelps realtimebot detection,advertising event processing at Uber, andso on.


Analytical use cases refer to SQL queries on streams. If a human is running an ad-hoc query, it’s probably an analytical use case. Examples include operational queries, data science, analytics engineering, and so on.


Extract, transform, load(ETL) stream processors are similar to standard batch ETL, except done in realtime.Change data capture(CDC) is used to get data into a streaming system. Once extracted, streams need to be transformed to filter out sensitive data, join tables, and the like. Transformation logic benefits from SQL as well. Once transformed, data is loaded into downstream systems using a sink connector.


These use cases all have different—often contradictory—requirements; something we missed when building Samza.


Developers prefer to deploy their production stream processing jobs the same way as the rest of their production code. They want their usual CI/CD pipeline, containers, and orchestrators. They want to write code, not SQL, and they want easily testable APIs. Transactionality and operability are important.


Analytical use cases are the polar opposite. Users want to write SQL and don’t want to think about deployment. Queries are often shorter lived than production jobs. Users care less about transactionality. And users often want to query batch data as well.They want a streaming database.


ETL’s defining characteristic is pluggability. Extracting and loading data requires integration with other systems—both batch and realtime—to move data in and out. A common data model to describe data in various systems is also helpful.


Samza’s architecture could service all of these use cases, but none of them well. Flexibility came at the cost of complexity and a poor user experience. Worse still, the more we tried to fix things (by addingstandalone deploymentorSQL) the more complex Samza became.


This tension is what led to our proposal. We preferred smaller, purpose-built systems rather than one giant monolithic platform. Smaller systems are easier to deploy and maintain. You can add the features you need and ditch the ones you don’t.


In hind sight, I think we proposed the wrong use case. Samza’s architecture, with its pluggability and orchestration, was much better suited for SQL and ETL use cases.Kafka Connectlooks much more like Samza than Kafka Streams does.


## 10 Years Later


The split between one giant platform and many smaller systems lives on. The giant platform is now Flink. The smaller systems are Kafka Streams, Kafka Connect, andksqlDB(in Confluent’s ecosystem). I still prefer our smaller, purpose-built approach.


The smaller systems are not without their warts, of course. Kafka Streams’s storage layer struggles with large state; you need to run hot standbys or face disastrously long recovery times (somethingResponsive[$]has fixed). Kafka Connect is still painful to self-host. ksqlDB is a failure. But these are not problems inherent to a federated architecture; these are implementation issues of aging software. Kafka Streams and Connect are nearly a decade old. And because the smaller systems are split by use case, you can throw one out without ditching the others. Don’t like ksqlDB? Swap it forMaterializeorRisingWave. Don’t like Kafka Connect? GrabAirbyteorFivetran.


I still believe Kafka Streams is a great solution for production workloads. It’s missing some of Flink’s whiz-bang features likebatch queriesand pipeline shuffles, but I love its deployment simplicity (Flink’s standalone provider still requiresZooKeeper for HA—yuck). Kafka Streams is a library meant for one thing: production streaming workloads.BytewaxandFaustare similarly appealing. Flink fans will say, “But it can’t do…” To which I respond, “Yes, that’s the point.”


As for Flink, I have to ask, what is Flink for? The answer seems to be, “It’s for everything!” And so I see many of the same problems Samza had. Flink has layered on feature after feature to appease its users. They’ve added astandalone orchestrator,Kubernetes support,SQL,state checkpointing,savepoints, and even afull-blown data lake platform. It’s just too much. As with Samza, this comes at the cost of simplicity. Privately, Flink developers admit to me that eventheythink it’s too complicated.


It’s true that Flink hasseen adoptionfrom big names like Uber, Yelp, Pinterest, and Netflix. I can’t deny that.But so has Kafka Streams. Flink is just buzzier. You could interpretConfluent’s Immerok acquisitionas a capitulation to monolithic platform architecture. Or you could interpret it as a sign that customers with deep pockets fell into the one-platform trap and now have to pay someone for help.


Ultimately, the question of federated or centralized management isaphilosophicalone. The answer is, “It depends.” If you’ve got a big budget to burn on a centralized streaming platform, knock yourself out with Flink. If you’ve got hundreds of engineers running ETL, analytic, and production streaming jobs, you’ll probably earn your money back.


But there are many users out there that need production stream processors, yet are happy with their batch-based ETL pipelines. Many companies have no production streaming jobs, but need realtime data integration. Many analytics engineers want to query streaming databases like Materialize, not a streaming platform. For such users, separate systems seem like the better choice.
