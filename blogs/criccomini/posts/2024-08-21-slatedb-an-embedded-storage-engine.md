---
title: "SlateDB: An Embedded Storage Engine Built on Object Storage"
subtitle: "We open sourced SlateDB a week ago. Let's look at where we're at and where we're headed."
date: 2024-08-21T14:11:43+00:00
url: https://materializedview.io/p/slatedb-an-embedded-storage-engine
slug: slatedb-an-embedded-storage-engine
word_count: 537
---


Apologies to those who follow me on Twitter and LinkedIn—this is probably old news to you—but I’m going to talk aboutSlateDBthis week.


For thosenotfollowing me, SlateDB is a cloud-native embedded storage engine built as alog-structured merge-tree(LSM tree) on object storage. That’s a lot in one sentence, so let’s unpack it. The cloud-native and object storage parts refer to the fact that SlateDB writesallits data to object storage (S3, GCS, and the like). SlateDB is a embedded, so it’s a library that runs in your process. It’s a storage engine that exposes a key-value API similar to RocskDB. And like RocksDB, it’s built as an LSM tree.


Object storage allows SlateDB to provide bottomless storage capacity, high durability, and easy replication. The trade-off is that object storage has a higher latency and higher API cost than local disk. I’ve written extensively about these tradeoffs before.

[The Cloud Storage Triad: Latency, Cost, DurabilityChris Riccomini·April 22, 2024Read full story](https://materializedview.io/p/cloud-storage-triad-latency-cost-durability)

In fact, my cloud storage triad post was the genesis of SlateDB. The tail end of the post pitches the idea and asks for contributors to help me work on it.


Shortly after the post,Rohan Desai(cofounder atResponsive),Vignesh Chandramohan(manager at Azure Streaming),Paul Butler(CEO atJam Socket), and several others all got in touch. We have been working together for the past 4 months to get SlateDB ready to open up. Last week, we got there.


We built SlateDB because we felt an open source LSM on object storage would be useful for stateful stream processing, serverless functions, durable execution, andmore. We had a lot of inspiration. Companies likeWarpStream﹩ andTurbopuffersetzero disk architectureon the map. And open source projects likeTonboandMonotoneare blossoming. But we couldn’t find an LSM that was purpose-built for object storage (see our FAQ for discussion onRocksDB-cloud,RocksDB on EBS, andRocksDB on EFS). So we built it.


In the past week, we’ve been overwhelmed with the positive feedback, questions, contributions, and new users showing up on Github and Discord. We’ve hit 327 stars as of this writing (pleasestar us on our Github repository!).


![](https://substackcdn.com/image/fetch/$s_!C0YM!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd460cdbf-9856-4be3-bbef-fb17fb75e6b7_1400x958.png)

*Star History*


Several people have asked me if I (or anyone else) has commercial plans for SlateDB. I can only speak for myself: I am explicitlynotgoing to do anything with SlateDB other than help make it a successful open source project. I am not going to start a company around it or try and monetize it in any way. To that end, we’ve chosen the permissiveApache 2.0license, and I’m hoping we can get it intoCNCF; we’ve submitted a sandbox application.


We’ve also got a lot of work to do on the project itself. We’re working hard to addon-diskandin-memorycaches to speed up reads. There’sa lot more to doon compaction. And we haven’t yet implementedsnapshots,garbage collection, transactions, andrange queries—all must-have’s. We’ve also got some clever ideas up our sleeves, includingwritable snapshot clones, remote compaction, and a lot more. If this sounds like fun, we’d love to have your contributions.Our Github issueshave “help wanted” and “good first issue” labels to get you started.


If you want to learn more, check outslatedb.io(especially thearchitecture pageanddesign documents). You can alsoregister for P99 CONF(it’s free and virtual). Rohan and I signed up to do a talk there. We’ll be discussing SlateDB’s history, architecture, performance, learnings, and more.
