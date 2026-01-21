---
title: "Search on PostgreSQL, Building Extensions, and pg_analytics with Philippe Noël"
subtitle: "Philippe Noël is CEO and co-founder of ParadeDB. In this post, Philippe and I discuss ParadeDB, the experience of building as a PostgreSQL extension, pg_duckdb, pg_lakehouse, and more ..."
date: 2024-09-03T10:18:55+00:00
url: https://materializedview.io/p/search-on-postgresql-building-extensions
slug: search-on-postgresql-building-extensions
word_count: 1695
---


Philippe Noëlis the CEO and co-founder ofParadeDB. ParadeDB is a collection of extensions to makePostgreSQLwork for search and analytics use cases. Their first extension,pg_search, addedBM25for relevance scoring (the standard in the industry). They followed that work with the hit extensionspg_analyticsandpg_lakehouse, which add support for columnar queries and datalake integration.


Before ParadeDB, Noël was the co-founder ofWhist, a cloud-hybrid browser that accelerated web applications.


---


C.R.: You and I have been talking for the past year, give or take. I'm excited to finally have you on Materialized View. Let's start with the basics. What is ParadeDB and how did it come to exist?


P.N.: Hey Chris! I've been a reader since day 1 and am excited to be a part of it.


ParadeDBis aElasticsearchalternative forPostgres. We build the core feature set of Elasticsearch (the data store), full-text search and fast analytics, in Postgres via Postgres extensions. The idea is that with ParadeDB, Postgres users can avoid needing to ETL data to Elasticsearch or similar tools in order to power user-facing search and analytics, and can instead stay within Postgres and keep their infrastructure simple. ParadeDB is an open-source project and is compatible with any existing Postgres deployment, including on managed Postgres services like AWSRDS, etc.


We came up with the idea while operating Postgres+Elasticsearch ourselves as part of a previous project, Retake. We were frustrated with needing to maintain an Elasticsearch cluster and an ETL pipeline, and by the lack of real-time and transactional guarantees in our search workload. We then went around asking our friends and fellowYCbatchmates, and realized that this frustration was shared by a large number of them. Realizing the gap between people's love for Postgres and hate for Elastic convinced us to launch into this and thus ParadeDB was born.


C.R.: The overlap between search and analytics is something I’ve written about recently in my 15 Years of Realtime OLAP series (part 1andpart 2). These use cases are distinct, but they have remarkably similar infrastructure. Faceted search has always looked a lot like columnar aggregation to me, for example. And both have shifted from batch to realtime ingest.


How do you think about these use cases? ParadeDB has pg_search, pg_lakehouse, and pg_analytics extensions. You seem to be suggesting that they don’t warrant different infrastructure (i.e. Elastic), but you’ve implemented different extensions for each.


P.N.: We think of these use cases from the perspective of the customer. While it is true that they are distinct, they are fundamentally the same: enable users to filter data to derive insights/take actions. Every major customer who comes to us for full-text search is also interested in faceted search, which as you point out is very similar to columnar aggregations. In fact, our faceted search uses a custom columnar implementation built byTantivy.


These customers typically build products that contain both user-facing search and live dashboards. You can get very far powering real-time dashboards with faceted search, but sometimes you need to fetch data that's stored in object storage, or you need to perform aggregations over the JOINed tables, which inverted indexes aren't as optimal for.


We believe customers should pick a product by thinking about their business need(s) rather than about the infrastructure of the product itself. ParadeDBpg_searchdeliversBM25full-text search and faceted search in Postgres. We've also builtpg_analyticsto offer on-disk columnar analytics in Postgres, and finallypg_lakehouseto offer analytics in Postgres over data in object storage like AWSS3. We're now combining pg_lakehouse and pg_analytics into a single extension, pg_analytics, which will offer both capability in a single extension to streamline development and adoption.


The use case is fundamentally the same: Customers want to offer user-facing search and analytics. They build their backend on top of Postgres, and ParadeDB enables them to offer these features on top of Postgres, no matter where their data lives.


C.R.: That last comment—building on PostgreSQL—seems to be the real differentiator for ParadeDB. PostgreSQL has been experiencing a real renaissance lately. Why do you think that is, and how has your experience been working with it?


P.N.: In my view Postgres isn't having a renaissance but is rather "coming of age". The last 30 years of smart design decisions have slowly made it the best open-source RDBMS. It's extremely reliable and very extensible, which is a really big deal.


The development of Postgres is open-source (not backed by any single company) and moves slowly. Maintainers are very opinionated and getting any patch in core is a serious task. This is good, as it guarantees quality. However, it means development is slow and Postgres could be left behind faster-moving database projects. pgvector was able to be developed very quickly as it sits outside of core, as an extension. Extensions enable Postgres to stay current with innovations in the data space while also maintaining extreme care to keep core as small and robust as possible. Every now and then, some extensions become so ubiquitous that it’s merged into core, like pg_stat_statement. The clear separation of work granted by extensions allow Postgres to uniquely accomplish the best of both worlds: Stay relevant while being rock-solid.


Working with Postgres has been wonderful. The extension ecosystem and API is very mature. Thanks toEric Ridge(ZomboDB)'spgrxproject, we can build our extensions inRustand benefit from the entire Rust open-source data community, without which ParadeDB couldn't exist. Oftentimes we find ourselves reading Postgres source and mailing lists, which is dense but the quality of code in core Postgres is quite amazing. Hacking on Postgres is really hard.Robert Haaswrotea big postabout it, for the curious. It's hard to find developers who know Postgres core, though. We didn't before we started. We're hiring, so if a reader is looking to get into Postgres internalscome say hi!


C.R.: You mentioned that you’re combining pg_analytics and pg_lakehouse.HydraandMotherDuckrecently announcedpg_duckdbalongsideDuckDB Labs,Neon, andMicrosoft. The Postgres analytics ecosystem seems really hot and really fast changing right now.


How is pg_duckdb different from what ParadeDB is doing, why are you combining your two analytics extensions, and how do you see things shaking out in this space?


P.N.: Analytics in Postgres should be a single extension, whether it's pulling data from object storage or from Postgres tables. That is the reason we’re consolidating pg_analytics and pg_lakehouse.


pg_duckdb is a cool project! I'm very excited to see it come to life. I had previously talked with DuckDB Labs and MotherDuck about donating our analytics work to DuckDB Labs to be the foundation of pg_duckdb, but others seem to have beaten us to it. I'm excited and cautiously optimistic it will flourish. If it does, it would be very good for everyone in Postgres, including for ParadeDB.


Building analytics in Postgres is really hard. Doing it properly is much harder than what ParadeDB could do today. My hope is that many companies work on pg_duckdb so it becomes a good foundation that we can rebase pg_analytics on top of. The vision is for many Postgres companies to build on top of pg_duckdb to easily create an analytics-in-Postgres extension for their platform.


For now, though, pg_duckdb is still very early. It also appears to be more DuckDB-centric than Postgres-centric, which concerns me. I am worried that MotherDuck, who seems to be the primary company driving this, does not care enough about Postgres to really make the project what it needs to be. Hopefully Neon gets involved, as they are one of the few players who have the Postgres expertise to really build it correctly. It's too early to tell, but we are following along.


On our side, ParadeDB is building an Elasticsearch alternative. We have plenty to do with search and already have a strong analytics offering with faceted search and our existing pg_analytics extension. If pg_duckdb evolves in the right direction, we'll be very eager to adopt it and to contribute to it. Fingers crossed!


C.R. On the Elasticsearch front, what challenges have you found in implementing search in Postgres, and what does the roadmap look like for pg_search?


P.N.: ParadeDB pg_search is built on top of aLucene-inspired library called Tantivy. Tantivy stores data in its own file format. Because Tantivy uses its own  format, we do not store data inside Postgres block storage (yet!). This means we have had to implement various of Postgres' native functionalities, like backup, WALs, etc. manually on top of this new storage. This is a lot of work, and we’re continuously improving upon it.


Today, pg_search is built via a multithreaded Postgres background writer and dynamic functions via the Postgres `CALL` API. It's quite uncommon, but very elegant. This enables us to play inline with Postgres as much as possible and has made our work integrating Tantivy much cleaner.


Roadmap-wise, we're working on features like:

- BM25 indexes over partitioned tables
- BM25 indexes over JOINed tables (highly requested, but very difficult)
- Full transaction isolation for faceted search


Eventually, we're also planning to integrate withCitusto offer a horizontally-scalable version of ParadeDB.


C.R.: Partnering withCitusis an interesting twist. ParadeDB’s extensions are licensed under theAGPL. I knowyou’ve written about your license choicein the past. You also don’t have a cloud offering right now. What’s your strategy for bringing ParadeDB to market?


P.N.: Today, we sell commercial licenses of ParadeDB containing a few enterprise-relevant features on top of our open-source offerings. Our customers self-host ParadeDB clusters from those licenses.


We're working on a bring-your-own-cloud (BYOC) solution to make this process smoother, and are going to announce partnerships with Postgres platform providers to power a ParadeDB Cloud.


C.R.: Wonderful. There’s plenty more to say, but I’ll save that for a future interview! Let’s call it here. Any parting thoughts?


P.N.: For anyone interested in our project, you can find (and star, hihi) our repo here:https://github.com/paradedb/paradedb. We welcome community contributions and are hiring for an early engineer role. If working on search and analytics in Postgres interests you, shoot me a note.


Thanks for having me, Chris! 🙂


---


Share


---


#### Book


Support this newsletter by purchasingThe Missing README: A Guide for the New Software Engineerfor yourself or gifting it to someone.


![](https://substackcdn.com/image/fetch/$s_!CI0B!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fde442631-41a6-4119-a99a-62957cd53edb_870x978.png)


Buy Now


---


#### Disclaimer


I occasionally invest in infrastructure startups. Companies that I’ve invested in are marked with a ﹩ in this newsletter. See myLinkedIn profilefor a complete list.
