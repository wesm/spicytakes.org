---
title: "ElectricSQL, PGLite, CRDTs, and Elixir with James Arthur"
subtitle: "James Arthur, the CEO of ElectricSQL, joins me to talk about their new database. We dig into its architecture, his thoughts on edge database use cases, PGLite, why they chose Elixir, and a lot more..."
date: 2024-03-18T10:22:09+00:00
url: https://materializedview.io/p/electricsql-pglite-crdts-and-elixir
slug: electricsql-pglite-crdts-and-elixir
word_count: 2550
---


I recently had the chance to interviewJames Arthur. James is the CEO and co-founder ofElectricSQL[$], a reactive, realtime, local-first sync database and replication system for PostgreSQL.


Prior to ElectricSQL, James co-founded thePost Urbanventure builder and was co-founder and CTO of synthetic data companyHazy. James's projects have won aTED Prizeand the$1M Microsoft Innovate.AIPrize for the best startup in Europe.


---


C.R.: There is a lot of activity in the edge database world these days. Different projects are targeting different use cases.


Databases like SKDB seem to be going after reactive front ends (at least initially). Such databases require client-side installation (WASM), conflict resolution (CRDT), and a reactive architecture that minimizes computation when updates occur.


Others like Ditto are going after IoT. Their product offering includes not only an embeddable, client side database, but also a mesh network layer. The whole idea is to make it easy to run their edge database on hardware with spotty internet connections (airlines and payment systems, right now).


Still others seem to be thinking more about geolocation, edge caching, and minimizing latency for applications.


Where do you see ElectricSQL fitting in? Which use cases are you thinking about?


J.A.: ElectricSQL is an open source platform for building local-first software. What we really target is the state transfer layer: how you move data across the public Internet between the frontend and the backend.


When you sit down to make an app, one of the first decisions you make is how to do state transfer—REST, GraphQL, LiveView? So much of web and mobile development is about ferrying data back and forth and coding across the network that the choice tends to dominate the architecture of your app and the code you have to write. All that boilerplate for serialization, authorization, validation, hydration, caching, state management, reactivity, etc.


What we're trying to do with Electric is eliminate those layers. So you just have your data and your components. Everything is live, reactive, instant and always on. In your app code you just declare what data you want where and we take care of making it so.


There are a bunch of sweet spot use cases for local-first. Building the next Linear or Figma. On-site collaboration software. Mobility, retail, construction, etc. However, we don't really want to pigeon hole it at this point. We see local-first as the best way of building pretty muchallsoftware in the future. We're working to make Electric the best way of building local-first on top of Postgres.


---


Housekeeping: I’ve had mixed feedback on the podcast format for interviews. I’m trying the written interview format with this post. Please let me know which you prefer.

Loading...

---


C.R.: "We see local-first as the best way of building pretty much all software in the future," is a bold statement. One of my gripes with local-first software is that the semantics can be tricky. Transactionality guarantees, consistency, durability, and conflict resolution are really tough not only to build, but for developers to reason about.


In my experience, developer ergonomics are key to a database's success. Can you give a rundown of ElectricSQL's architecture, and how you solve for the consistency and durability guarantees that engineers are used to getting from their databases?


J.A.: Yup, the thing with local-first is you have not only local/offline writes but also multi-user collaboration. This means you can have multiple people editing the same data at the same time -- without being able to coordinate with each other.


In the past, this has led toconflicts, which require some resolution strategy and torollbacks, where local writes end up being rejected later on. A classic example is one user enrolling in a tournament whilst another user concurrently deletes the same tournament. Both writes can be valid locally but when they sync you can't accommodate both of them without breaking referential integrity.


In contrast, Electric provides both a conflict-freeanda rollback-free programming model. Technically, we provide Transactional Causal Consistency with CRDTs (TCC+). This includesHighly Available Transactions, which are not ACID but do guarantee atomic "all or nothing" application of writes wrapped in a transaction. The CRDTs provide automated conflict resolution. And we layer on additional"Rich-CRDT" techniquesto maintain guarantees like referential integrity.


Importantly, we also hold onto the principle of Finality of Local Writes. This means that writes made to the local embedded database in the client are not subject to being rejected by the server (unless they're malicious). This gets rid of rollbacks and tentativity, which is a key advance in simplifying the local-first programming model and finally making it viable and sane enough for mainstream application development.


The result for a developer is that you can write to the local database just as you would a normal backend database. You don't need to code conflict handlers and you don't need to code rollback handlers—or in fact any code related to syncing data or handling the network.


Now, thereisa trade-off and that is that, with CRDTs, your writes are always subject to concurrent merge semantics. So whilst with finality of local writes your local writes are never rejected, actually the guarantee is slightly softer: local writes are guaranteed to be factored into the CRDT merge history but they may well be "trumped" by other logically concurrent updates.


The worry here is that data is then "moving around" underneath you. However, in practice, in a multi-user system, writes can be trumped by subsequent updates from other users anyway. So as long as you switch to live, reactive data bindings and use Rich-CRDTs to maintain database invariants (rather than relying on serializable database access) then the model becomes very compelling.


C.R.: Most of what we’re talking about here is about resolving conflicts with the data itself. Another area of complexity that comes to mind is schema management. One of the nice things about having the layers you mentioned—REST, GraphQL, and so on—is that they provide clear boundaries between components.


A common issue I see inchange data capture(CDC) is that internal database schemas get treated as APIs for other services. Sharing database schemas across components creates a lot problems—versioning, compatibility, transformation, access control, schema migration, and so on. I wrote about this inYes, Change Data Capture Still Breaks Database Encapsulation. It sounds like ElectricSQL’s would create similar issues; how are you dealing with these?


J.A.: Yes, these issues are very real. Schema evolution is complex and coupling is a key concern / trade off.


Practically, Electric propagates changes to (the “electrified” subset, ie the opted-in subset) of the Postgres schema out to clients. So you manage your schema using your standard PG migrations tooling, such asEctoorPrisma. We then stream DDL changes out to clients over the replication stream (with the same transactional causal consistency guarantees — because the schema change is a causal dependency of a write made using it, you always see the schema change before you see the write).


The challenge is that clients can go offline and write data using their current schema, whilst the rest of the system moves on to using a new version of the schema. Because we provide finality of local writes, we have to accept these “stale” writes.


The enabling simplification that allows us to do so is to only support additive migrations (of the electrified subset of the schema). So you can add columns and tables and relax constraints. But you can’t remove columns and tables or make constraints stricter.


This means that stale writes are always supported because they are always made using a still-valid subset of the evolved schema. Which is elegant but does come at a price — the limitations on how you evolve your schema. Plus we only support forward migrations, no rollbacks.


There is a solution to this, which is to support bi-directional lenses for non-additive migrations. Ink & Switch did some great work showing how this is possible with theirCambriaproject. Lenses provide transformation functions to map one schema to another. Which, interestingly, is conceptually similar to the kind of adapter functions you might maintain to support multiple versioned endpoints in a REST API.


In GraphQL, you can solve the same problem with your resolver layer, which de-couples the graph schema from the underlying database schema. This is powerful and it is an abstraction layer we lose with Electric. One that’s particularly important with larger, real world applications.


So, we are explicitly tighter coupling. However,  whilst the software architecture orthodoxy emphasizes the cons of tight coupling, there genuinely are both pros and cons here.


The delight and the promise of local-first is to be able to reduce the complexity of the development stack to just your data and your components. By removing all the abstraction layers, development can be highly productive.


If you can solve the schema evolution challenge, for example using primitives like lenses, schema adapters and virtual tables, etc. Then you can make the stack so much leaner and more productive without suffering the downsides of the tighter coupling.


Of course you can also run GraphQL on Electric — resolve your queries from local SQLite. So if you want looser coupling between your component bindings and your local DB schema you can have that out of the box today.


And it’s not just GraphQL. You also have databases likeCozoDBin the client, for example. Cozo provides both graph and vector data in the client on top of SQLite. So you can craft higher order data models and looser coupling on relational as an underlying storage layer if you want to.


C.R.: You mentioned Ecto, a data mapping toolkit written in Elixir. Your comment hints at one of the more interesting characteristics of ElectricSQL’s architecture—its sync service is written in Elixir.


As I understand it, ElectricSQL has three components: a PostgreSQL extension, an Elixir sync service, and a client-side library. The client-side library contains an embedded database—SQLite—and a web-socket client to keep the database in sync.


Elixir is a fairly rare language to find in production—Discord is the largest user that comes to mind. I’m curious why you picked Elixir and what benefits and challenges you’ve experienced with it. Are the PostgreSQL extension and client-side library written in Elixir as well?


J.A.: We love the ergonomics of Elixir and we lean a lot on the underlying BEAM runtime (the Erlang VM) for fault tolerance and concurrency.


TheBEAMwas designed to run high uptime, fault tolerant distributed systems. It naturally supports lots of concurrent connections (as you can see from some of the systems built on it, like Discord and WhatsApp). For us, it's a very natural choice for the sync layer, which we run as a separate process in front of your database. We can then scale out to thousands of concurrent clients, without having the database become a bottleneck to the sync throughput.


Elixir being a functional language also helps keep complexity down. We use a lot of the concurrency and stream processing primitives that come with the language to construct our replication pipelines and route data efficiently and resiliently.


On the client side, we provide a Typescript library. This is developed in Typescript -- we don't compile from Elixir. There is some scope to move parts of the library to Rust or Elixir and compile down to different targets like WASM for portability but we haven't got there yet.


Then for Postgres, we don't actually install anything. We wanted to maximize compatibility with standard open source Postgres. So rather than integrating as an extension, we just connect over a DATABASE_URL. We need logical replication enabled and certain user permissions and everything just works. Which means you don't need to install any potentially dangerous code and you don't need anything whitelisted by your Postgres host.


C.R.: In the vein of my previous schema question, bridging schemas between PostgreSQL and SQLite is likely challenging. I spent some timeexploring SQLite’s type system, and it’s… unique.


You recently publishedPGLite, an embeddable PostgreSQLweb assembly(WASM) binary. Will ElectricSQL eventually replace SQLite with PGLite on the client-side, thereby unifying client and server data models. What are the challenges you’ve seen with SQLite and what are your plans with PGLite?


J.A.: Yes, we've started with SQLite as our client database. It's low footprint, high performance and well supported, with some great projects likewa-sqliteandop-sqliteimproving support in the browser and Javascript-based mobile apps.


It does introduce an impedance between the Postgres data model in the cloud and the SQLite data model in the client. We handle mapping between the two and for simpler SQL it's fine—the mapping just works and SQLite has great query support in the client. However, this approach doesn't support more complex requirements, like functions, triggers, extensions, etc. For example, mapping extensions likepgvectorfor embeddings orPostGISfor geo data to their SQLite equivalents is pretty difficult and becomes quite complex and quite fragile quite quickly.


So PGLite is intended as an alternative client side database for applications that want to sync a Postgres data model with more advanced features. The mouthwatering prospect is being able to compile the same extensions on the server and client. Like using pgvector and being able to do hybrid vector-relational sync on and off the local device, all from the same core data model without any siloes. Or PostGIS for geo-based partial replication.


We will most likely continue to support SQLite though. It's really fast and has a lower footprint. So having both options will allow developers to choose what to optimize for.


On the topic, there are also other cool use cases for PGLite. For example using it as a development database, where you can skip all the OS-level package management and just `npm install` Postgres. Also syncing in data from scale-to-zero cloud hosts likeNeon, and/or using Electric's partial replication to provision subsets of data into edge workers, like fromSupabaseinto aCloudflare Worker.


So I think PGLite will have a life of its own beyond Electric but the combination of PGLite + Electric sync is pretty sweet.


C.R. Wonderful. I appreciate you taking the time to talk with me. I’ll give you the final word.Where can people go to get started with ElectricSQL? Do you have any other parting thoughts?


J.A.: Likewise, I really appreciate the opportunity to chat! If you're interested in Electric, you can head over to the website atelectric-sql.com, join the Discord community atdiscord.electric-sql.com, or check us out on GitHub atgithub.com/electric-sql.


As a parting thought, if you're building consumer, prosumer, or SaaS software and you're not building local-first, ask yourself how your product is going to compare to a product that is. Do you want your product to feel old and laggy like Jira or super snappy and modern, like Linear and Superhuman? It's clear to me which pattern the next generation of category defining software is going to be built on.


You can also dive into the wider local-first community atlofi.software, which has links to lots of other projects and references, including theoriginal local-first manifesto. Lastly, I believe there are still a few tickets available for the first ever Local-first Conf in Berlin later this year:localfirstconf.com


Hope to see you there :)


---


Share


---


Support this newsletter by purchasingThe Missing README: A Guide for the New Software Engineerfor yourself or gifting it to someone.


![](https://substackcdn.com/image/fetch/$s_!CI0B!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fde442631-41a6-4119-a99a-62957cd53edb_870x978.png)


Buy Now


---


I occasionally invest in infrastructure startups. Companies that I’ve invested in are marked with a [$] in this newsletter. See myLinkedIn profilefor a complete list.
