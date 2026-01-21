---
title: "Arrow and Velox Play Nice, Databases Get Edgy, a UUID Shootout, and More..."
subtitle: "Arrow adds formats to work with Velox; The world of edge databases is buzzing with activity; I explore various UUID implementations; and more..."
date: 2024-02-26T11:12:25+00:00
url: https://materializedview.io/p/arrow-and-velox-play-nice
slug: arrow-and-velox-play-nice
word_count: 921
---


## Apache Arrow Adds Velox Data Structures


Arrowadded three new formats: StringView, ListView, and Run-End-Encoding (REE). These formats improve interoperability with Velox.


Veloxis an execution engine from Meta. An execution engine is the lower part of a query engine that translates an execution plan into actual tasks for a runtime (like Spark or Flink). Meta has been updating all of their internal systems to use Velox.


> Velox is currently in different stages of integration in more than 10 of Meta’s data systems. We have observed3-10x efficiency improvementsin integrations with well-known systems in the industry like Apache Spark and Presto.


Apparently, Velox has its own in-memory format:Velox Vectors. The format is similar toApache Arrow. Arrow is far-and-away the winner in this space, so Meta is trying to interoperate. But they wanted Arrow to add a few new formats.


The post is a solid read. The StringView format is particularly interesting. Arrow normally serializes a column of string data as contiguous strings followed by offsets (memory locations). The new StringView format has a level of indirection:


![](https://substackcdn.com/image/fetch/$s_!xsep!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb37daa2d-bab9-4754-89d3-724586ceacca_1023x326.png)

*Aligning Velox and Apache Arrow: Towards composable data management*


Theviewblock contains the length of the string followed by 12 bytes. Smaller strings can be directly encoded into the view layer. This improves memory locality and allows for some other optimizations.


I really like Arrow and its subprojects: DataFusion, Ballista, and Comet. I believe they will be as impactful as Hadoop was a decade ago; something I’ve written about inDatabases Are Falling Apart: Database Disassembly and Its Implications.


It’s unsurprising to see Arrow and Velox converging. Frankly, I see little reason to use Velox. DataFusion is a superset of Velox’s functionality. It’s about to graduate as a top-level Apache project and has a lot of momentum. The space where Velox seems most useful is if you’ve already got a query engine and just want to replace the execution engine. This is Meta’s use case. They (and others like Intel) are going through and replacing Presto and Spark’s execution engines. Though, this is also something DataFusion supports. In fact, Comet is just this—Apple updated Spark to use DataFusion.


![](https://substackcdn.com/image/fetch/$s_!Dhbf!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb60a5f41-196c-4ea2-918b-4655c42c620c_693x376.png)

*Tweet*


We’ll see how this all shakes out.


If you’re interested in more about composable databases check out Episode 175 ofThe Data Stack Show.Pedro Pedreira, the author of the Meta’s Arrow post, joined Ryan Blue, Wes McKinney, Kostas Pardalis, and me to talk about composable data systems.

[The Data Stack Show175: The Parts, Pieces, and Future of Composable Data Systems, Featuring Wes McKinney, Pedro Pedreira, Chris Riccomini, and Ryan BlueThis week on The Data Stack Show, Eric and Kostas chat with a panel of experts as Wes McKinnyey (Cofounder, Voltron), Ryan Blue (Co-Founder and CEO, Tabular), Chris Riccomini (Seed Investor, Various Startups), Pedro Pedreira (Software Engineer, Meta), all share their thoughts around the topic of composable data stacks. During the conversation, the group…Listen now2 years ago](https://datastackshow.substack.com/p/175-the-parts-pieces-and-future-of?utm_source=substack&utm_campaign=post_embed&utm_medium=web)

## Edge Databases Are A Thing™


There’s been a lot of activity in the edge database world recently.


My friend and former manager,Chris Conrad, joinedDittoas their VP of engineering. I was only vaguely aware of Ditto, so I’ve been reading theirplatform documentation. The product is intriguing. Ditto is an edge syncing platform that includes both client-side and cloud storage. Unlike other edge databases, Ditto also comes with a resilient network library that uses Bluetooth Low Energy (BLE), peer-to-peer wi-fi, and local area network (LAN) to handle spotty internet. This architecture works well for edge hardware with spotty internet like theairline and payment industries. Oh, andthey’re hiring!


Julien VerlaguetpostedTurning Firebase into a Local First, Reactive Experience. The post shows how to integrateSKDBwithFirebase. Italked to Juliena month ago, right before he launched SKDB. They look to be progressing quickly.


Finally,ElectricSQLmanaged toship PostgreSQL to the browser(Githubhere). This isreallyinteresting. I’ve been reading overElectricSQL’s architecture, and one of the uglier warts is that they sync between PostgreSQL (server side) and SQLite (client side). Schemas must be translated between the two systems and SQLite has arather odd type system. ElectricSQL with PostgreSQL on both the client and server simplifies a lot.


![Image](https://substackcdn.com/image/fetch/$s_!6kYa!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F339f927c-fdd2-4040-ac95-4a31fba56da9_1376x846.jpeg)

*ElectricSQL’s Tweet*


## UUID Shootout


Jeremy Schneiderposted a funUUID Benchmark Warthat compares different storage strategies on PostgreSQL. The post measures UUID performance and size in text, uuid, and uuidv7 against classic `bigint` primary keys. Take a peak at the post to see how they stack up.


UUIDs are near and dear to my heart. One of the first services I wrote at WePay was an SFTP service to sync data between our object store and bank SFTP servers. The service used UUIDs as its primary keys. I decided to storeUUID v4as BINARY(16) types in MySQL. This ended up being a bad idea for a variety of reasons; it caused performance andextract, transform, load(ETL) problems.


Algorithmic improvements, native database support, and best practices have come a long way. Jeremy’s post leads to many neat UUID implementations:

- Universally Unique Lexicographically Sortable Identifiers(ULIDs)
- Snowflake ID
- UUID v7
- NewID


All of these have one trait in common: they’re lexicographically sortable. Many databases use a B-tree variant to index keys. Random IDs can cause problems, asBuildkite explains:


> Non-time-ordered UUIDs values generated in succession are not sequential. The randomly generated values will not be clustered to each other in a database index, and thus inserts will be performed at random locations. This random insertion can negatively affect the performance on common index data structures such as B-tree and its variants.


I’m excited about UUID v7. There’s anIETF spec for it, and PostgreSQL isincluding it in PostgreSQL 17.
