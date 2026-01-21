---
title: "Antithesis in the Wild, Polar Signals Traces Calls, GCS Express, and More..."
subtitle: "Deterministic simulation testing for the masses; Polar signals unifies distributed call tracing and profiling; Google Cloud Storage is going to get 100x faster; and more..."
date: 2024-03-12T10:08:20+00:00
url: https://materializedview.io/p/antithesis-in-the-wild
slug: antithesis-in-the-wild
word_count: 1045
---


## Antithesis in the Wild


I’ve been meaning to write aboutAntithesissince it launched publicly a couple of weeks ago. To understand Antithesis, you must be familiar with deterministic simulation testing: the idea that you build your software and tests so that they are completely deterministic. Given an input it will always produce the same output.


Once software is deterministic it’s much easier to test. And a test that fails once will always fail—no more flaky tests! You can also simulate disk failures, network partitions, and so on. I wrote a lot more about the subject here:

[Viewstamped Replication in Go, Deterministic Testing at Dropbox, FoundationDB's Simulation, and more...Chris Riccomini·November 9, 2023Read full story](https://materializedview.io/p/viewstamped-replication-deterministic-simulation)

The challenge with deterministic simulation testing is that it only works for software that’s been written in a deterministic way. Threads, event loops, network, disk, random number generators, and many other components all introduce non-determinism. Writing deterministic code takes practice; you have to wrap every non-deterministic interface in a wrapper that you can control.


Antithesis solved this problem by writing a customhypervisorthat emulates an entire machine. Software no longer needs to be deterministic in order to do deterministic simulation testing. Old software can reap the benefits without a full rewrite and new software can be written without having to wrap every non-deterministic interface.


When failures happen, Antithesis can play back every instruction—not just the application instructions, but all of the operating system ones as well. The result is a fully deterministic machine that can inject faults and reproduce failures whether code is non-deterministic or not.


![](https://substackcdn.com/image/fetch/$s_!WRut!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbdb95d8a-1b9b-48b1-b329-ddff5e709736_692x489.png)

*View Tweet*


TigerBeetle[$] is one of many companies now using or evaluating Antithesis.Joran(CEO of TigerBeetle) and his team have been evangelizing deterministic simulation testing for a long time. Still, I’ve been surprised by how quickly Antithesis is being adopted. Nearly every database company I talk with is using or evaluating it.


The only complaint I’ve heard so far is the price tag, which can be hefty. Theirpricing pageoffers per-core options, but you’ll likely need professional services to get it working.


Out of curiosity, I asked Joran if he would still write TigerBeetle as a non-deterministic system now that Antithesis exists. He wrotea very thoughtful answer,as didDominik Tornow(CEO ofResonate).


## Polar Signals Trace IDs


Polar Signalsupdated Parcato support distributed call tracesfor profiling data.Parcais a profiling tool that provides application CPU profiles. Unlike other profiling tools, Parca profile can span multiple processes and even the operating system (OS) itself. It uses an eBPF filter to achieve this, something that I discuss with in detail on the Materialized View Podcast:

[Parca, Polar Signals, and FrostDB with Frederic BranczykChris Riccomini·January 8, 2024Read full story](https://materializedview.io/p/parca-polar-signals-frostdb-frederic-branczyk)

Prior to the latest release, Parca could only profile call stacks in a single machine. Now call trace IDs can be used to profile calls across multiple machines.


> …with Parca Agent's system-wide profiling approach, this enables an entirely new use-case of viewing all CPU time used by an entire request throughout all services!


This is a big deal. A frontend call might result in hundreds of downstream microservice calls, each of which can result in still more calls. Developers use distributed call tracing to figure out which microservices are causing the most latency for the frontend call. Once the bottleneck is found, a different set of tools—profilers—is used to figure outwhythe service is slow.


We spent a lot of time at LinkedIn buildingReal-time distributed tracing for website performance and efficiency optimizations. Parca and Polar Signals now unify these two operations in one system.


![](https://substackcdn.com/image/fetch/$s_!fg4X!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff75f1602-64d9-43d3-8d57-662e3021f4c0_534x92.png)

*View Post*


## Google Cloud Storage Express


Shikhar Bhushanfoundan interesting postfrom Google Cloud Storage’s (GCS) Director of Engineering. It looks like Google was caught off guard byAWS’s S3 Express One Zone. The post says GCS is looking to improve latencies by 1-2 orders of magnitude. That would put it in line with Express.


![](https://substackcdn.com/image/fetch/$s_!Aule!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fab68d955-d0e8-4689-9e2f-f7112f1c75d9_551x425.png)


This development is unsurprising; I’ve already saidI expect to see more products like it. In fact, I’m betting that we see multi-region, low-latency object stores withoptimistic concurrency control(OCC) in the next 18-24 months. In fact,Tigrisalreadydoesthis.


An object store with such characteristics will completely change how we build data systems. Low latency object stores enable key-value (KV) and OLTP databases. Multi-region will allow write-ahead logs (WALs) to be written durably straight to object stores. Finally, optimistic concurrency control will remove the need for complex control planes. The hard parts of distributed data infrastructure will be managed by the object store.


## Project Highlight: CozoDB


I had a fun chat withJames Arthur, the CEO ofElectricSQL[$] this week. He’s a wealth of information onConflict-free replicated data types(CRDT) and databases. I plan to do an interview with him in the coming weeks. In the meantime, he pointed me atCozoDB. The Github repository describes Cozo as:


> A transactional, relational-graph-vector database that uses Datalog for query. The hippocampus for AI!


There’s a lot going on in that sentence. And it doesn’t even mention that Cozo is embedded, as well!


The combination of graph and vector is an fascinating to me. Graphs can be though of as nearest-neighbor search where edges define explicit links to nearest neighbors. Conversely, nearest neighbor search can be thought of as graph traversal, where nearest neighbors define implicit edges in the graph. A system that combines these two structures seems very smart.


Datalogmakes sense as a query language for such a database; it more easily represents graph traversal queries, which are often recursive. Many graph databases already use non-SQL dialects likeCypher,SPARQL, orGremlin. I don’t seen Datalog as a barrier for adoption given such diverse query languages.


Cozo’s storage layer is also notable. Cozo is embedded, but the storage layer is pluggable. Some storage engines—SQLite,RocksDB, andSLED—are also embedded. But Cozo also supports aTiKVstorage backend. A TiKV-based backend could not only larger datasets, but also data portability. Distributed clients could all read and write from the same TiKV store. I would be curious about durability and consistency semantics in such a case; it’s something I didn’t dig into.


---


Share


---


Support this newsletter by purchasingThe Missing README: A Guide for the New Software Engineerfor yourself or gifting it to someone.


![](https://substackcdn.com/image/fetch/$s_!CI0B!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fde442631-41a6-4119-a99a-62957cd53edb_870x978.png)


Buy Now


---


I occasionally invest in infrastructure startups. Companies that I’ve invested in are marked with a [$] in this newsletter. See myLinkedIn profilefor a complete list.
