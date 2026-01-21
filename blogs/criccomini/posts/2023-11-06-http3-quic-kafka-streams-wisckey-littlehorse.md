---
title: "HTTP/3 is QUIC, Autoscaling Kafka Streams, Sipping WiscKey, and more..."
subtitle: "An overview of QUIC, Kafka Streams gets a Kubernetes autoscaler, WiscKey optimizes LSMs for SSDs, and I highlight a durable execution framework called LittleHorse."
date: 2023-11-06T11:00:40+00:00
url: https://materializedview.io/p/http3-quic-kafka-streams-wisckey-littlehorse
slug: http3-quic-kafka-streams-wisckey-littlehorse
word_count: 778
---


## HTTP/3 From A To Z


I confess I knew nothing aboutQUIC. Thanks toRobin Marx’s excellent write-up,HTTP/3 From A to Z, now I do. HTTP/3 is really just HTTP/2 + QUIC (with a few minor tweaks to HTTP/2).


> The main features we’re excited about for HTTP/3 (faster connection set-up, less HoL blocking, connection migration, and so on) are really all coming from QUIC.


QUIC is a new protocol built on top of UDP. It’s meant to address some of the issues with TCP.


> We’ve reimagined and implemented a much more advanced version of TCP and called it QUIC. And because we want to make QUIC easier to deploy, we run it over UDP.


There are four improvements over TCP:

- Security:TLS is built into QUIC (I’m not sure how I feel about the protocol breaking layers of separation here.)
- Multiplexing:You can send multiple independent byte streams (files) over one connection in tandem (multiplexed).
- Multi-connection:Clients have connection IDs that allow them to migrate connections between networks (between local wifi and 4G/LTE, for example).
- Extensibility:The protocol uses packet frames to make it extensible. A single packet can have many frames of different types (ack, new_connection_id, stream, datagram, etc).


There’s a lot more in the post and there aretwomoreposts in the series. Check ‘em out if you’re into this.


## Autoscaling Kafka Streams


Responsive [$]built an autoscaler for Kafka Streamsthat scales up and down based on resource utilization. And because they’veseparated state from compute, you can scale down to save cash without having to re-hydrate RocksDB when you scale up (a time-consuming operation).


I worked on a stream processing system calledApache Samzaat LinkedIn. Two things always annoyed me about the way I implemented job sizing in Samza:

1. Jobs were defined by physical requirements (memory, cpu, disk, network).
2. Resource requirements were static.


Both are undesirable because it’s hard for application developers to guess physical requirements and because resource requirements change over time.


Responsive’s autoscaler lets you define min/max messages per thread, thread (CPU) saturation, and expected latency (how long before a new message is processed). They call these “diagnosers” and you can combine them to have multiple rules for a stream job. Seethe postfor more detail.


## Paper Highlight: WiscKey


Alex Feinbergand I were talking about serverless storage this week.RocksDB cloudcame up, and he sent me a link toWiscKey: Separating Keys from Values in SSD-conscious Storage. WiscKey tries to optimizelog structured merge(LSM) tree-based key-value stores forsolid state drives(SSDs). Traditionallog structured merge(LSM) storage systems are optimized for spinning disks. SSDs have different characteristics:

1. Random reads aren’t as expensive with SSDs.
2. SSDs have more parallelism.
3. SSDs wear out after many writes.


WiscKey tweaks the LSM design to take advantage of these properties by splitting up key and value storage. Keys are kept as an LSM-tree while values are written to a simple append-only log. Splitting keys and values reduces write amplification and works best for “large” values (> 1kb). But two problems are created:

1. Range queries result in random reads on values (since values aren’t sorted)
2. Consistency issue since keys and values are written separately.


Both are addressed in the paper.


Since 2016, WiscKey’s architecture has been widely adopted for LSM stores.Dgraph’s [$]BadgerDB,PingCAP’sTitan, andRocksDB’sBlobDBare all examples.


## Project Highlight: LittleHorse


LittleHorseis adurable execution framework(DEF). The project brands itself as “workflow-driven microservices”. I think of it as a mashup between three different framework styles:

1. Airflow/Prefect/Dagster-style workflows
2. Durable execution frameworks
3. Traditional business process modeling and automation


Unlike batch systems like Airflow, LittleHorse is meant for realtime use cases. Yet workflow declarations look like old-school Airflow or Prefect definitions. And LittleHorse has built-in support foruser tasks, which call out to actual humans for input—something usually found inBPMN-style solutions likeCamundaandZeebe(thanks toDmitriy Ryaboyfor pointing this out).


Under the hood, LittleHorse is written in Java and usesKafkaStreamsto provide transactionality and state management. It has SDKs for Java, Go, and Python. There’s a cloud-version coming soon, which I expect to be acontrol plane.


I plan to write more on durable execution frameworks in the near future, but I couldn’t resist highlightingLittleHorsebecause it looks so different from the other DEFs out there.


## More Awesome Infrastructure


Keep up with new projects as they’re added to theawesome-infraGithub repo.


Arroyois a distributed stream processing engine, designed to make it easy for anyone to build correct, efficient, and reliable real-time data pipelines with SQL or Rust.


Quickwitis a cloud-native distributed search engine designed to execute powerful search and analytics queries directly on cloud storage.


---


I occasionally invest in infrastructure startups. Companies that I’ve invested in are marked with a [$] in this newsletter. See myLinkedIn profilefor a complete list.
