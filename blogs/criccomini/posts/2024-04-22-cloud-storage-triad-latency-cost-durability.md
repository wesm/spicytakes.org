---
title: "The Cloud Storage Triad: Latency, Cost, Durability"
subtitle: "A theorem for primary persistence on object stores."
date: 2024-04-22T17:23:50+00:00
url: https://materializedview.io/p/cloud-storage-triad-latency-cost-durability
slug: cloud-storage-triad-latency-cost-durability
word_count: 853
---


I believe thatthe future of database persistence is object storage—S3, Google Cloud Storage, and so on. New systems likeNeon,WarpStream[$], andTurbopufferpersist data in object storage to offer infinite retention, durability, replication,data warehouse integration, and so on.


Object stores present some challenges, though. Historically, such systems have been higher latency, have lacked atomic writes, and have billed a lot for API requests. For these reasons, many systems write to a cache in front of the object store. Data is then flushed to object storage asynchronously.


Write caches come with their own set of challenges. If durability and consistency are important, caches must be replicated and serve consistent reads. Consensus protocols enter the picture. Neon, for example, uses their own brand ofPaxoswithSafekeepers and Pageserver.


I don’t think we’ll need these write caches in the future. Object storage is changing fast. Latency on S3 has improved dramatically withS3 Express.Google cloud storageis going tooffer similar latencies soon. As for atomic writes, nearly every object store except S3 already offerscompare-and-swap(CAS),called preconditions. I believe S3 Express will adopt pre-conditions soon. And systems likeTigrisalready offer both preconditions and low-latency reads and writes.


Given these trends, it’s reasonable to expect object stores to converge on low latency reads and writes with atomicity. Such systems would allow us to move write ahead logs into the object storage layer and eliminate write caches.


I recently began hacking on a project to test this theory out. The project—dubbedSlateDB—is a cloud-nativelog-structured merge tree(LSM) embedded key-value database. My goal is to answer the question: what does an LSM tree look like if all writes are persisted directly to object storage? I don’t think evenRocksDB-clouddoes this; they have a pluggable WALthat can write to disk, Kafka, or Kinesis.


Recall that an LSM tree normally has an in-memory sorted list of key-value pairs called aMemTable. Writes are inserted into this MemTable. To keep writes durable, writes are also sent to awrite-ahead log(WAL). When MemTables get large, they’re frozen (made immutable) and flushed to disk assorted-string tables(SSTs).


The most naive implementation of a cloud-native LSM might simply send all WAL writes directly to object storage. This works and is reasonably low latency with S3 Express. Unfortunately, it’s expensive when you have a lot of writes.PUTs are $0.0025 per-1000 requests. A high-volume service that sustains 10,000 writes per-second would cost 2.5c per-second, or $65,000 per-month.


Object storage pricing isn’t changing anytime soon. If cost remains fixed and SlateDB is constrained to object storage, there’s no choice but to batch writes. Batching decouples the client write-rate from the PUT calls sent to object storage. SlateDB can be configured to send writes to object storage every N milliseconds. All writes accrued during that window are sent as a single PUT. A 10ms window means a maximum of 100 writes per-second are sent to object storage. A 100 write-per-second upper-bound implies a maximum cost of $0.00025 per-second, or $650 per-month—much more reasonable.WarpStream[$] works this way (agents default to 50ms windows), as doesTurbopuffer(which defaults to a 100ms window).


Batched writes leave clients with a decision: they can either wait for the batch to complete or they can let writes happen asynchronously. If a client waits for a successful batch write, their latency goes up. If the client chooses not to wait, their latency drops but they lose durability.


This triad of latency, cost, and durability presents an easy mental model; something I’m facetiously calling the latency, cost, durability (LCD) theorem. The LCD theorem holds high API costs fixed, and forces clients to choose between money, durability, and latency.


Clients that want low latency and high durability have to pay. Clients that care less about latency or durability can lower cost at the expense of latency (waiting for writes to finish) or durability (treating writes as asynchronous).


![](https://substackcdn.com/image/fetch/$s_!8OCq!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6b72175a-1a47-4530-8a27-14d43d402d21_520x279.png)

*View Post*


LCD-style systems have a rather elegant design. Clients can pick batch windows and maximum batch sizes to control latency—similar toApache Kafke’slinger.msandbatch.sizesettings. And a simple async/await or future-based write API allows clients to choose whether to wait for writes to successfully persist to object storage or not.


![](https://substackcdn.com/image/fetch/$s_!rjgc!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4b864e89-4aaa-442e-9650-b86bdc36d6bd_688x288.png)

*View Post*


I’m still experimenting with SlateDB, but I think it could be a very useful library (Yes, it’s written in Rust). The library isn’t yet open source (it doesn’t have compaction and reads only exist in a PR). I would love to get some more contributors, though.Shoot me a DMif you want to help! It’s already surfaced a number of interesting questions:

- Can we move the control plane into object storage (using pre-conditions)?
- Can we achieve multi-region durability on S3 Express using quorum bucket writes?
- Which compaction strategies work well for object storage (tieredlooks promising)?
- Can we flush MemTables directly to level-0 SSTs, thereby eliminating the WAL all together?


I plan to answer these questions in future posts.


---


Share


---


#### Book


Support this newsletter by purchasingThe Missing README: A Guide for the New Software Engineerfor yourself or gifting it to someone.


![](https://substackcdn.com/image/fetch/$s_!CI0B!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fde442631-41a6-4119-a99a-62957cd53edb_870x978.png)


Buy Now


---


#### Disclaimer


I occasionally invest in infrastructure startups. Companies that I’ve invested in are marked with a [$] in this newsletter. See myLinkedIn profilefor a complete list.
