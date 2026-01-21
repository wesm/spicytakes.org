---
title: "Databases Are Falling Apart: Database Disassembly and Its Implications"
subtitle: "Why are engineers taking databases apart and putting them back together, again?"
date: 2024-01-29T11:47:02+00:00
url: https://materializedview.io/p/databases-are-falling-apart
slug: databases-are-falling-apart
word_count: 1731
---


A recent trend in the database world is to break databases into their constituent components. Each component is provided on its own so infrastructure engineers can integrate them into databases.


Most databases have the same parts: a query parser, logical and physical planner, optimizer, write ahead log, client connection protocol, and so on. Each database usually implements their own version of these components.(Excepting storage engines likeMySQL’sMyISAM/InnoDB, orRocksDB’s widespread use.)


Monolithic databases make sense. Each layer integrates with the layers above and below it; to abstract these layers is hard. Pluggable layers require a flexible API and support for different—often antithetical—use cases.


Yet most of these layers end up looking pretty much the same. A specific database might spend the majority of itsinnovation tokensin just one layer; say, the optimizer. But developers have historically had to re-implement each layer because there were limited off-the-shelf components. New open source projects are now building these components.


In this post, I discuss the history of database disassembly, the industry’s current state, where we’re heading, and the implications of this trend. I find it instructive to look at disassembly through the lens of twoelephant-themedprojects:Apache HadoopandPostgreSQL. Though Hadoop and PostgreSQL are from different parts of the data stack, both have influenced modern disassembly efforts. Let’s start with Hadoop.


## Hadoop’s Influence on Disassembly


Eighteen years ago, Hadoop broke the data warehouse into compute, data, and control planes—a paradigm that persists to this day.


Compute planes are responsible for running calculations; initiallyMapReduce. The data plane is responsible for providing storage; initiallyHDFS. Control planes are responsible for coordinating the deployment and execution of the compute; initially Hadoop’sJobTracker, thenYARN.


Separate planes—often on separate computers—create a boundary where protocols and APIs could develop. Such developments are a prerequisite for a disassembled database.


The next step happened with storage formats. Hadoop users very quickly found they needed to write their data to HDFS in a file format. Users often started with CSV but quickly found that text parsing was slow. Early attempts to optimize storage formats led to Twitter’sElephant Birdand LinkedIn’sVoldemort storage format. Subsequently,Apache Avro,Apache ORC, andApache Parquetreceived widespread adoption, with Parquet ultimately winning (for now, anyway).


Further disassembly was spawned byApache HiveandApache Pig, which built atop MapReduce. These were query engines that converted text-based queries (SQL orPig Latin) into MapReduce jobs to be run on Hadoop.


We’re now starting to see the contours of a disassembled database: a query engine (Hive/Pig) with a parser, a query plan, and an optimizer, which sits atop a query runtime (MapReduce). The query runtime reads from a data plane (HDFS) in an optimized storage format (Parquet).


This architecture is where we find ourselves today. Hive and Pig have been replaced byPresto,Apache Spark, andTrino. HDFS has been replaced by cloud object stores likeS3andGCS. Parquet lives on, though it’s used withApache IcebergorDelta Lakenow. YARN is still in widespread use, butKubernetesand itsoperatorsnow dominate the control plane. Yet the architecture endures.


## Disassembling the Query Engine


Current query engines like Trino are built as a fully integrated query engines with a parser, logical/physical query plan, optimizer, execution engine, and runtime. Engineers are now ripping these apart.


![](https://substackcdn.com/image/fetch/$s_!X-BQ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd345ed72-6cd4-423f-8fa4-f8ee7468c974_757x342.png)

*Fromvelox-lib.io*


Language front ends parse text (SQL) and convert them into anintermediate representation(IR) such as aconcrete syntax tree(CST),abstract syntax tree(AST), orlogical or physical query plans. These intermediate representations make it easier for code to work with the queries than directly operating on the text.


Once the query engine has an intermediate representation, an optimizer replaces nodes in the IR with more optimal ones. Trino’s optimizer, for example, might decide that ahash-joinis an optimal strategy.


After a query plan is optimized, it’s handed to the execution engine. Engines convert plans into tasks (like MapReduce tasks). Tasks are then executed by the execution runtime (MapReduce,Flink, Spark, and so on).


In practice, these layers are fuzzy. Optimization might happen at other layers, engines and runtimes might be combined, or perhaps a query engine has only one query plan or another. Still, the model above is a useful starting point.


Developers are now building composable libraries for each layer of the query engine. All query engines that integrate these libraries will benefit from the same set of optimization and feature work. And new databases can be quickly assembled to address new use cases as they arise; vector search being one recent example.


New open source projects now exist at every layer. SQL still dominates the frontend (despitethehate), butMalloy,PRQL, andSaneQLare projects worth looking at.Substraithas sprung up to provide an intermediate representation, andCMU-DB’soptdproject is a composable optimizer. Further down the stack,Metahas open sourcedVelox, an execution engine that’s now integrated intoPrestoandSpark. The runtime layer is by far the most mature, with options like Spark and Flink.


And then there’sApache Arrow’sDataFusionsubproject (soon to be a top-level Apache project). Unlike the projects above, which focus on a single layer, DataFusion does everything. You can use it as an integrated query engine like Trino orDuckDB, or you can use it as a library for any one of the layers above. It’s a complete database toolkit.


![](https://substackcdn.com/image/fetch/$s_!sikK!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4c3c19cc-d989-4530-be61-8e1a3d2108ff_695x454.png)

*twitter.com/andygrove_io/status/1745295329468047461*


It’s no surprise that many new databases are using DataFusion; it’s flexible and—I’m told—very easy to integrate. Adopters includeGlareDB,Lance,ROAPI,Cube,InfluxDB, anddozens of others.


## What about PostgreSQL?


While Hadoop has driven disassembly in data warehousing, PostgreSQL has done the same forrelational databases(RDBMSs) andhybrid transactional/analytical processing(HTAP). Its robust storage layer,extension API, simple architecture, andopen source Berkeley development modelmake it a shoo-in for disassembly.


PostgreSQL add-on projects run the gamut from SQL extensions to custom replication and storage schemes. Its protocolandsyntaxarealsowidelyadopted, but it’s PostgreSQL’s storage layer—its data plane—that’s most significant to this discussion.


PostgreSQL’s storage layer is much more robust than Hadoop’s; it includes awrite-ahead log(WAL), avacuumprocess, andtransactional guarantees. These features are helpful when building production databases that act as the source of truth for data (as opposed to data warehouses).


Many extensions add custom formats and indexes to PostgreSQL’s storage layer that are optimized forvector search,text search,graph queries,geospatialqueries,online analytical processing(OLAP) queries, anda lot more.


Developers are treating PostgreSQL almost like DuckDB—an integrated query engine with a pluggable storage layer. Except, unlike DuckDB, PostgreSQL’s storage layer is far more mature (DuckDB deliberatelydoesn’t even document their storage format). Extensions automatically inherit all of the transactional goodness that PostgreSQL provides.


Projects likeNeonhave taken the storage layer a step further by ripping apart PostgreSQL’s internals. They’vemodified PostgreSQLto make PG’swrite-ahead log(WAL) pluggable. Neon provides a remote implementation that uses theirPaxos-based WALwith tiered object storage.


![Neon architecture diagram](https://substackcdn.com/image/fetch/$s_!sAWL!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0283edb8-f6e8-4613-b161-c1e5411aa9bd_1920x1080.png)

*Neon’sarchitectural overview*


Neon’s architecture isexemplary. I believe this is the most significant part of PG’s disassembly, and will be influential. Much like query engines, we’ll see projects that will provide read and write-through caches,consensus-based WALsandkey-value stores, andtiered object storage. I’m not alone inthisbelief.Is Scalable OLTP in the Cloud a Solved Problem?describes exactly how this will look.


## The Implications of Disassembly


Disassembly will impact the entire data ecosystem, from data warehouses to OLTP, HTAP,multi-model databases, and even streaming.


Data warehouse will become increasingly undifferentiated and commoditized.Jordan Tigani,MotherDuck’sCEO, recently wrotePerf is not enough. Jordan claims that database performance will converge over time; databases will compete on features and developer experience. I believe this commoditization will happen with features, too. The projects in the previous section commoditize performance, but they also make it easier to add, copy, or share new features. CMU-DB’sMeta Velox presentationreflects on this, too:


![](https://substackcdn.com/image/fetch/$s_!gqpI!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3540a44d-2206-425f-806d-22a86cae927a_829x440.png)


Meanwhile, new components in the storage layer will enable OLTP systems to finally achieve the dream: low cost, low latency, high throughput, multi-region, fully transactional databases. Current NewSQL systems tick only a subset of those boxes. Asdistributed WAL + S3 architecturegets commoditized (thanks to the projects listed in the previous section), costs should plummet. Neon is a my favorite example;TiKV’sS3 integrationis another.


The final shoe to drop will be when OLAP data warehouses and OLTP databases are unified into HTAP and multi-model systems. As OLTP systems integrate with object stores, two new architectures surface:

1. OLTP systems can persist data in both row-based and columnar formats.
2. Separate OLTP and OLAP systems can interface via loosely coupled standards in the object store.


Both of these make it cheap and simple to service both row-based production queries and also column-based warehouse queries. The first architecture lends itself to integrated systems that service both OLTP and OLAP workloads.Thomas Neumannet al’sHyPerproject is one example of this trend. SingleStore is another;Cloud-Native Transactions and Analytics in SingleStoreis an excellent read.


The second architecture would see a plethora of query engines for different workloads. Each query engine would run off the same shared storage using storage formats optimized for their use cases. Loosely coupled systems will depend on open formats like Parquet, Iceberg, and Delta Lake to make integration possible.


A world centered around object stores is a serious threat toApache Kafka. Kafka’s primary use case is data integration—moving data between systems. But if all of your data is on an object store from start (OLTP) to finish (OLAP, search, graph, etc.) what use have you for Kafka? Streaming systems will continue to be useful for sub-second use cases, but that’s a smaller market than data integration.


To continue to be relevant in data integration, Kafka should morph into a realtime ingestion system for object stores. This will require first-class integration with table formats like Apache Iceberg and Delta Lake.KIP-1009hints at this with Kafka and Parquet integration (though, I believe there are better designs).WarpStream[$] is a trail blazer in this space,Confluent’sKorais trending this way, and Kafkafinallysupports tiered object storage.


I’ve come this far without mentioningSQLite, the most successful database of all. SQLite, too, is being disassembled, and it’s having a significant impact on edge databases. Object storage, local storage, and caches are really just storage tiers. Developers are extending this tiering into the client side with SQLite andConflict-Free Replicated Data Types(CRDT). Others are starting from scratch, leveraging libraries like DataFusion.Fly(viaLitestreamandLiteFS),SQLite Cloud,Turso,SKDB, andDittoare but a few of the many projects that are making edge databases workable.


All of this change is going to take time, but the future looks bright. A world with purpose-built, low latency, high thoughput, multi-region, multi-model, transactional databases is coming; it’s just a matter of time. This is great news.


---


Share


---


Support this newsletter by purchasingThe Missing README: A Guide for the New Software Engineerfor yourself or gifting it to someone.


![](https://substackcdn.com/image/fetch/$s_!CI0B!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fde442631-41a6-4119-a99a-62957cd53edb_870x978.png)


Buy Now


---


I occasionally invest in infrastructure startups. Companies that I’ve invested in are marked with a [$] in this newsletter. See myLinkedIn profilefor a complete list.
