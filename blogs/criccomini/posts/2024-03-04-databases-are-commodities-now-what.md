---
title: "Databases Are Commodities. Now What?"
subtitle: "How will vendors differentiate when databases are commoditized? I've got three ideas."
date: 2024-03-04T11:04:20+00:00
url: https://materializedview.io/p/databases-are-commodities-now-what
slug: databases-are-commodities-now-what
word_count: 870
---


Databases are becoming commoditized.Jordan Tigani(CEO ofMotherDuck) has written thatperformance is no longer a competitive advantage. My previous post,Databases Are Falling Apart, shows that query engines are becoming commoditized. PostgreSQL’s protocol and dialect are the new lingua franca for database front ends. Object stores like S3 and RocksDB are used for storage, and formats like Parquet are widely adopted.


If every database is a PostgreSQL-compatible frontend built atop the same set of open source components, how are these databases going to compete? I can think of at least three ways: build a platform, build for a vertical, or build amulti-modelsystem.


![](https://substackcdn.com/image/fetch/$s_!Ql73!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcbf693ca-b61d-4471-8b68-011c32ac2652_1376x500.png)

*View Tweet*


## Database Platforms


To run a database in production, you need more than the database itself. Developers must manage schema migrations, snapshots, indexes, query optimization, access controls, connection pools, and so on. A database platform should include such features.


There is room to innovate, too. New ideas likebranchingandtime travelshould also be added. Branching allows you to test schema changes, to manage data migrations, and to test more easily. Time travel eases recovery and makes debugging easier. Tighter integration withobject–relational mappings(ORMs) is another area to explore (seeDatabases Should Speak Substraitfor more on this).


Data integration features that simplifyextract, transform, load(ETL) andchange data capture(CDC) are also valuable. Databases should support PostgreSQL’s (or MySQL’s)streaming replication protocol. This would allow plug-and-play change data capture with existing systems likeDebezium. Simple transformations could be pushed into the database—personal identifiable information(PII) redaction is a big deal. Perhaps even built-insupport for outboxes(dare I say, triggers?).


Though I’m speaking mostly aboutonline transaction processing(OLTP), many of these features apply toedgeandonline analytical processing(OLAP) databases as well. These databases have even more room for platform features, too. Edge databases must solve conflict resolution, data syncing, and hardware challenges. OLAP databases have a whole suite of machine learning and data visualization tools to integrate with.


In totality, database platforms are a compelling product. Even if every platform uses the same database, there is ample space to compete on the surrounding ecosystem.


## Databases For Verticals


Databases can also be built for specific business verticals—finance, retail, manufacturing, public sector, and so on. Verticalized (or domain-specific) databases can address very specific needs. Two examples areNile[$] andTigerBeetle[$].


Nile is a PostgreSQL-compatible database that’s built forsoftware as a service(SaaS) providers. A SaaS provider is a company that, itself, sells SaaS.Stripe,DoorDash, andConfluentare all SaaS companies. Providers have customers. Each customer usually has its own independent dataset. Nile bakes the concept of a customer (called atenant) into the database itself.Any table with a tenant_id columnautomatically gets magical features like data isolation, data portability, and so on.


TigerBeetle, meanwhile, is a database built for the financial industry. It has focusedveryheavilyon durability and consistency—two things required by finance. They also have abuilt-in data modelto define credits and debits. The data model, alone, is an invaluable feature. We spent many hours and made many mistakes at WePay—my previous company—trying to do what TigerBeetle does.


I suspect databases like these will be built to provide purpose-built features and data models for most industries.


## Multi-Model And HTAP Databases


Multi-model databasesare one of my hobby horses. They extend workloads beyond traditionalhybrid transactional/analytical processing(HTAP) to include graph, search, and caching operations.SingleStoreandCedarDBare two examples.


Multi-model databases fundamentally change application architectures for the better. A world with a bunch of purpose-built PostgreSQL compatible databases is only incrementally better. Developers must still adopt a different database and vendor for each access pattern—OLTP, OLAP, search, graph, caching, and so on. There are still7±2systems I’ve got to deal with. Multi-model databases reduce this by folding multiple access patterns into a fewer systems. Fewer vendors, fewer systems, less complexity, less cost.


Many developers are skeptical of HTAP databases; the industry is littered with failures. Multi-model systems look even more challenging; they try to collapse yet more access patterns. This is a feature, not a bug, though. There’s no winner for this type of database yet, so there’s room to compete. And users do want this, they just can’t get it (yet).


Recent technology advances make me optimistic. Decomposable data systems likeDataFusion,Velox, andSubstraitare making databases easier to build. And object stores are getting really good—S3 Expressis just a first step towardlow latency, low cost, multi-region object stores. Dual writes to different storage formats and separate query engines on shared storage are feasible. Such an architecture could enable loosely coupled multi-model systems.


## All Together, Now


Database platforms, vertical databases, and multi-model systems can each stand on their own as valuable products. Yet, even more value could be unlocked by adopting more than one of these strategies. Vertical database should, for example, become platforms as well—Nile already supports schema migrations and incremental rollouts. The same goes for multi-model databases. And there’s room for multi-model databases for verticals like finance—OLAP and graph traversal feature heavily here.


I was worried that database commoditization might leave the space dull. After thinking through these opportunities, I’m excited. So is Jordan.


![](https://substackcdn.com/image/fetch/$s_!AhMU!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1361cf2b-06e4-4a18-a90a-e355cbb5befb_1378x350.png)

*View Tweet*


---


Share


---


Support this newsletter by purchasingThe Missing README: A Guide for the New Software Engineerfor yourself or gifting it to someone.


![](https://substackcdn.com/image/fetch/$s_!CI0B!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fde442631-41a6-4119-a99a-62957cd53edb_870x978.png)


Buy Now


---


I occasionally invest in infrastructure startups. Companies that I’ve invested in are marked with a [$] in this newsletter. See myLinkedIn profilefor a complete list.
