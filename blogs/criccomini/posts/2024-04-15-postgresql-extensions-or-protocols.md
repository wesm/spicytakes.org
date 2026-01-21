---
title: "PostgreSQL Extensions or Protocols: Architecture Roulette"
subtitle: "Should new infrastructure use PostgreSQL as a query engine, or aim for protocol compatibility instead?"
date: 2024-04-15T10:16:30+00:00
url: https://materializedview.io/p/postgresql-extensions-or-protocols
slug: postgresql-extensions-or-protocols
word_count: 1105
---


PostgreSQLhas a lot of momentum right now. Nearly every startup I talk to is using PostgreSQL or a PostgreSQL-compatible database. Most database vendors offer some form of PostgreSQL compatibility throughextensions,protocol compatibility, orPostgreSQL SQL dialectsupport.


A big part of PostgreSQL’s success is its extension ecosystem. Users no longer need to adoptElasticsearchfor search,Pineconefor vector search,Neo4Jfor graph operations, andSnowflakefor online analytical processing (OLAP). Instead, users are opting for PostgreSQL extensions likepg_bm25,pgvector,postgis,pg_analytics,hydra_columnar, and so on. The operational footprint is smaller, users have to deal with fewer (if any) vendors, and PostgreSQL’s architecture is tried-and-true.


Two architectures are emerging. The first embraces PostgreSQL as a query engine to build extensions for. Vendors such asHydra,Tembo,ParadeDB, andNeonuse this approach. The other approach uses PostgreSQL’s protocols and/or SQL dialect, but builds a new query engine and storage layer from ground up.CedarDB,Yugabyte,CockroachDB,Spanner, andAuroraDBrepresent the latter approach.


Adopting PostgreSQL as your query engine confers many advantages. You get a lot from PostgreSQL: its excellentwrite-ahead log(WAL), its parser frontend, its network layer, and so on. Infrastructure developers are free to focus only on the area of the system that differentiates their project. Neon, for example, has chosen to focus heavily on thestorage layerto provide bottomless storage. InPostgres is eating the database world,Ruohang Fengwrites:


> PostgreSQL is already a near-perfect database kernel for the vast majority of scenarios, making the idea of a kernel “bottleneck” absurd. Forks of PostgreSQL and MySQL that tout kernel modifications as selling points are essentially going nowhere.This is similar to the situation with the Linux OS kernel today; despite the plethora of Linux distros, everyone opts for the same kernel. Forking the Linux kernel is seen as creating unnecessary difficulties, and the industry frowns upon it.Accordingly, the main conflict is no longer the database kernel itself but two directions— databaseextensionsandservices! The former pertains to internal extensibility, while the latter relates to external composability. Much like the OS ecosystem, the competitive landscape will concentrate ondatabase distributions. In the database domain, only those distributions centered around extensions and services stand a chance for ultimate success.Kernel remains lukewarm, with MariaDB, the fork of MySQL’s parent, nearing delisting, while AWS, profiting from offering services and extensions on top of the free kernel, thrives. Investment has flowed into numerous PG ecosystem extensions and service distributions: Citus, TimescaleDB, Hydra, PostgresML, ParadeDB, FerretDB, StackGres, Aiven, Neon, Supabase, Tembo, PostgresAI, and our own PG distro — —Pigsty.


Feng’s kernel analogy is interesting, as is his comparison between Linux and PostgreSQL distributions. But I think the post misses the significance of PostgreSQL’s protocol being an easy integration point. The question is not whether to package or fork PostgreSQL, but whether to extend PostgreSQL using the extensions API or the protocol.


I disagree with Feng’s statement that, “PostgreSQL is already a near-perfect database kernel for the vast majority of scenarios, making the idea of a kernel “bottleneck” absurd.” Tying yourself to PostgreSQL is always going to be more limiting than building your own database. You’re limited by what PostgreSQL can offer you.  The more control you want, the more PostgreSQL is going to feel like a straight jacket. One of Feng’s own examples—Neon—has had to fork PostgreSQLto support a remote write-ahead log (something they hope to merge upstream).


And building your own database doesn’t sound as crazy as it used to. Query engine components likeDataFusion,Substrait, andVeloxare maturing. Storage formats likeParquetand storage layers likeRocksDBare well known. As I wrote about inDatabases Are Falling Apart: Database Disassembly and Its Implications, databases are easier than ever to build. Using these systems while maintaining protocol and dialect compatibility with PostgreSQL seems to get you the best of both worlds.


Deployment complexity is still important, though. Extensions are easier to adopt than a new system (with a caveat that I’ll get to in a moment). New infrastructure must justify its upfront adoption cost. Not only must new systems be PostgreSQL compatible, but they must be easier to run and offer more functionality than the PostgreSQL extensions they’re competing with.


Vendors will follow the standard playbook to make their systems easier to run: serverless SaaS,bring your own cloud(BYOC),virtual private clouds(VPCs), bring your own object store, and so on.


When it comes to functionality, I believe new databases will need to bemulti-model, something I wrote about in,Databases Are Commodities. Now What?Multi-model databases amortize the adoption cost across multiple use cases. Users may choose to keep PostgreSQL as theironline transaction processing(OLTP) system but adopt a single multi-model system for search, GIS, graph, and caching use cases. Multi-model system can take over OLTP workload as users get comfortable with them.SingleStoreDBandCedarDBexemplify this approach.


Further pushing users away from extensions is the caveat I alluded to above. The big three cloud providers have limited extension support. Amazon’s Aurora PostgreSQL has anextensive but not exhaustivelist of supported extensions. The same is true forGoogle Cloud’s AlloyDB. If you want to use an extension that’s not on the list, you’re out of luck. This is an opportunity for third-party providers like Tembo and Neon, and also for multi-model databases that offer missing functionality.


There’s no clear winner between the two architectures. I suspect that both types of systems will exist; indeed, they already do. My gut says that PostgreSQL’s protocol, not its query engine, will be its most defining characteristic. But I also think there’s room in the market for multi-model PostgreSQL vendor distributions.


---


Share


---


#### Jobs

- Eventual[$] - Eventual Computing is a startup from some of the folks that work onDaft. The team isis hiringafull stack engineer,open-source product growth engineer, and adistributed query engine engineer. Code Rust, write a distributed query engine, what's not to like?
- Stealth [$] - A stealth seed-funded startup that I invested in is looking for a founding staff software engineer.  You’ll work closely with the founders and be responsible for creating the technical roadmap, architecting/designing a complex query engine, and building out the initial platform that re-imagines how data pipelines are built and managed. Work with exciting technologies likeVelox,DataFusion,Firecracker, etc. The role is Bay Area based.Message meif you’re interested.
- Ditto- InEdge Databases Are a Thing, I mentioned that my friend (and former manager),Chris Conrad, joined Ditto as their VP of engineering. Their product is an interesting mix of CRDT, networking, database, and systems programming. The teamis now hiring for a bunch of rolesincluding a seniorRust engineer, seniorC++ engineer. andSite Reliability Engineer.


---


#### Book


Support this newsletter by purchasingThe Missing README: A Guide for the New Software Engineerfor yourself or gifting it to someone.


![](https://substackcdn.com/image/fetch/$s_!CI0B!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fde442631-41a6-4119-a99a-62957cd53edb_870x978.png)


Buy Now


---


#### Disclaimer


I occasionally invest in infrastructure startups. Companies that I’ve invested in are marked with a [$] in this newsletter. See myLinkedIn profilefor a complete list.
