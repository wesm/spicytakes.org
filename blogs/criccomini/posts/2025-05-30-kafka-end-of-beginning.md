---
title: "Kafka: The End of the Beginning"
subtitle: "A decade of focus on adoption has paid off. Now it's time to innovate."
date: 2025-05-30T10:04:16+00:00
url: https://materializedview.io/p/kafka-end-of-beginning
slug: kafka-end-of-beginning
word_count: 1050
---


You’ve probably noticed fewer posts recently. I am spending time working on the batch processing chapter inDesigning Data-Intensive Applications (2nd edition). It’s striking how much batch processing has changed since the book was written. The first edition was very focused on MapReduce. A lot has changed over the past 10-15 years: cloud data warehouses, data lakes, lakehouses, data catalogs, new storage formats,Spark,DuckDB,DataFusion, DataFrames, composable data systems, and more.


The pace of change in the batch processing ecosystem stands in stark contrast to its streaming counterpart.Apache Kafkaremains the near-universal solution for streaming data, whileApache Flinkremains the dominant stream processing system. Both projects were started well over 10 years ago. Flink 1.0 was released in 2016, while Kafka 0.9 (widely adopted in production) was released in 2015. EvenDebeziumstarted around 10 years ago; we adopted 0.2 at WePay in 2016.


Undeniably, there has been some innovation. The separation of control, data, and compute planes has led to object store-backed streaming systems likeWarpStream﹩,Bufstream, andRedpanda. The object store transition also led to streaming lakehouse integrations likeTableflow. AndFrank McSherryet al.’s work on timely and differential dataflow is nothing short of is brilliant.

[Everything You Need to Know About Incremental View Maintenance](https://materializedview.io/p/everything-to-know-incremental-view-maintenance)
[Chris](https://substack.com/profile/69592459-chris)
·
April 18, 2025

Incremental view maintenance has been a hot topic lately. Materialize has been around for a while, but newcomers like PostgreSQL’s (semi-working) pg_ivm extension, Feldera, Epsio, Bytewax, and many others are starting to make noise. In the data warehousing space,

[Read full story](https://materializedview.io/p/everything-to-know-incremental-view-maintenance)

Yetthe architecturethatConfluentwas founded on—an enterprise service bus built on Apache Kafka—remains largely the same as it was 10 years ago. Moreover, the actual technologies we’re using are the same. Much of the story of the past 10 years has been about adoption rather than innovation. We’re still using Kafka (or at least its protocol), we’re still using Flink, and we’re still using Debezium.


I’ve been thinking about this stagnation for a while. I don’t believe we’ve solved everything. It’s still very difficult to write and deploy stream processing jobs, for example; it honestly feels likeit’s gotten worse, not better. I’d like to believe that these challenges are not fundamental—that there are better ways.


This malaise seems to be growing.Yaroslav Tkachenkoposted a summaryof last week’sCurrent 2025 conferencein London. The post is worth a read, but his comment at the top of the post mirrored my own view:


> Finally, I feel like the data streaming industry is still in a tough spot. The growth is slow, and the sales cycles are long. One person I spoke with said that “80% of the companies in the Expo hall will be dead in two years”. I don’t want to believe them, but it might be true.


I was speaking with someone just yesterday that said something similar: it’s the same people, same companies, and same technology. There are no new ideas and no new users. This person said they would not attend future Current conferences; it wasn’t worth it; they didn’t learn anything new.


Yaroslav’s post also says that Redpanda was banned from the conference. I don’t know the details, nor do I really care. But if true, it’s hard not to read this as an indication of scarcity and fear, not one of abundance.


It’s worth reflecting onApache Hadoop. Hadoop began atYahoo!in 2006. It took about 10 years for companies such asHortonworksandClouderato drive adoption through the enterprise. By 2016, it was widespread, but dated. This is when dataflow engines and cloud data warehouses began to replace Hadoop. Confluent was founded in 2014. Eleven years later, it feels like we might be at a similar turning point with Kafka; it’s widely adopted, but dated.


Yet, I don’t see the challengers that Hadoop saw in 2016. I suspect this is because Kafka’s protocol has become the de facto standard.HDFS,including its protocol, was largely replaced by object stores like S3. Kafka, on the other hand, managed to adopt object stores while keeping its protocol and client rebalancing architecture intact.


A de facto standard protocol is great for enterprises; they don’t need to migrate and vendors are all forced to compete on a commoditized storage layer. But what happens when the protocol needs to change? Entrenched vendors aren’t going to ask their customers to migrate.


Concepts like partitions and leadership are baked into Kafka’s protocol (especially its clients). Broker awareness of time—fundamental to stream processing—is largely absent. Kafka is not designed for millions (or billions) of streams. Gunnar Morling, of Debezium fame, has an excellent post where he asks,“What if We Could Rebuild Kafka From Scratch?”


![](https://substackcdn.com/image/fetch/$s_!4KNP!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc6cd122e-a795-4a0a-be6e-767187883a20_1388x468.png)

*View Post*


One bright spot isS2.Shikharand his team seem to be rethinking what a modern, cloud-native ecosystem could look like. Notably, of all the modern streaming solutions—Redpanda, AutoMQ, WarpStream, Confluent Freight, and Bufstream—S2 stands alone as the only system that doesn’t (yet) use Kafka’s protocol; they are unconstrained.


While writing my incremental view maintenance (IVM) post, I wondered what timestamps in Kafka might look like. A month later, S2announced their take. In, “What if streams had the primacy of objects?,” they discuss supporting per-user streams. This is the fresh thinking we need. Unfortunately, adoption is a real challenge. Kafka’s protocol network effects are strong.


Meanwhile, the stream processing side of the house seems somehow both worse and better. I am no fan of Flink, but it has won the stream processing race (outside ofGoogle Cloud, which hasDataflow). Unspoken amongst vendors, the true winner is really just regular old Kafka consumers and producers.


I do see some glimmers of hope. Compact libraries that incorporate differential dataflow, such asD2﹩, are appearing. AndFelderaseems like a genuinely better computation layer than Flink. Such systems might become the next Spark orSnowflakeof the streaming ecosystem (and batch ecosystem, in Feldera’s case).


The next decade of stream processing could look like the last decade of batch processing: one of growth and innovation as we transition out of legacy on-prem architectures, protocols, and systems into a truly cloud-native streaming era. I hope so; it would be great for everyone.


---


#### Book


Support this newsletter by purchasingThe Missing README: A Guide for the New Software Engineerfor yourself or gifting it to someone.


![](https://substackcdn.com/image/fetch/$s_!CI0B!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fde442631-41a6-4119-a99a-62957cd53edb_870x978.png)


Buy Now


---


#### Disclaimer


I occasionally invest in infrastructure startups. Companies that I’ve invested in are marked with a ﹩ in this newsletter. See myLinkedIn profileandMaterialized View Capitalfor a complete list.
