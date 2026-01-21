---
title: "Epsio, IVMs, and Differential Dataflow With Gilad Kleinman"
subtitle: "Gilad Kleinman, CEO of Epsio, talks with me about incremental view maintenance (IVM). We discuss use cases, the history of IVM, how Epsio is different, and where the field is headed."
date: 2025-02-11T17:03:20+00:00
url: https://materializedview.io/p/epsio-ivms-differential-dataflow
slug: epsio-ivms-differential-dataflow
word_count: 1874
---


I’m planning to spend some time with differential data flow, timely dataflow, and incremental materialized views. As a first step, I talked withGilad Kleinman, co-founder and CEO ofEpsio. Epsio is an incremental view stream processor that feeds off a database’s replication feed and writes materialized data back to the DB.


Before co-founding Epsio, Gilad worked as a product manager forAxis Securityand was an R&D team lead forIsraeli Military Intelligence.


---


C.R.: Let's start with the basics to get everyone on the same page. Can you give me a brief definition of what streaming SQL is and what it's useful for?


G.K: Unlike "traditional" SQL that processes a dataset at a specific point in time, streaming SQL refers to constantly processing a stream of changes and understanding how a given change in the underlying data affected the previously outputted result—without ever re-processing the entire dataset.


For example, if you are running a query that calculates the count of items in a warehouse per category, a streaming SQL engine will output the initial result of that query and just do "plus one" to the relevant category whenever an item gets added and "minus one" when an item gets removed. Although this specific example is a fairly easy one to imagine, the same concept could be applied to much more complex queries containing many joins, subqueries, window functions, and so on.


In scenarios where an application runs a predefined set of queries on a dataset (e.g. in-app analytics, data modeling, reporting, etc.), streaming SQL can help you get faster and cheaper results by orders of magnitude compared to reprocessing the entire dataset each time you run the query.


C.R.: There are so many streaming SQL offerings out there:Materialize,Flink SQL,Feldera,RisingWave, and others. I tend to split solutions into one of two categories: streaming databases (RisingWave, Materialize) and stream processing systems (Flink SQL,kSQL). Does this match your mental model? And what differentiates Epsio from these systems?


G.K.: This model makes a lot of sense. Stream processing systems like Flink SQL and kSQL focus on outputting changes in query results to downstream systems (e.g., Kafka), leaving users responsible for consuming and processing these changes later. On the other hand, streaming databases go a step further by materializing up-to-date query results based on the stream of changes and serving them directly to clients, much like traditional databases. Unlike stream processing systems, streaming databases often allow users to connect via SQL clients (usually PostgreSQL) to interact with the data, run ad hoc queries, create indexes, and perform other typical database operations.


At Epsio, we’re huge fans of PostgreSQL and MySQL. Our goal is to bring the benefits of streaming databases to the existing PostgreSQL/MySQL deployments that organizations already use and love. Epsio achieves this by natively consuming the CDC stream from these databases and updating result tables directly within the original database. With this architecture, creating a new “streaming query” is as simple as calling a stored procedure in your current PostgreSQL/MySQL instance and querying the resulting table—essentially transforming your existing database into a streaming database.


Since Epsio's results sit within the original database, organizations get the best of both worlds — a robust streaming SQL engine, with all the amazing features MySQL/PostgreSQL already have to offer (diverse indexing options, table partitioning, constraints, etc.) and without needing to migrate to a new database.


C.R.: Streaming SQL without having to add a new database is very appealing. Though, it sounds like Epsio still needs to run as a separate process on a separate machine. How would you compare your solution to PostgreSQL’spg_ivmextension?


G.K.: When we originally built Epsio, we started out by building it as a PostgreSQL extension (similar to pg_ivm). Pretty quickly, we changed the architecture to what we currently offer based on pretty strong feedback we got from initial users/customers.


Other than the fact most managed database offerings (RDS,Cloud SQL, and so on) don't allow users to install unauthorized extensions, adopting new database technologies is a pretty scary endeavor. We found that asking companies to install a new extension (that could potentially crash) on their production database was a pretty big ask to make. By sitting "behind" the existing database, reading CDC logs, and writing back results to the original database, users can integrate Epsio without worrying about affecting anything other than the results tables it needs to maintain. We even actively recommend not giving Epsio permissions to anything other than that.


Additionally, in a world where PostgreSQL and MySQL doesn't scale out elegantly, we found that being able to offload some computations to a separate instance using Epsio was actually a benefit to many customers who were already reaching the limits of what a single PostgreSQL or MySQL instance could do.


Regarding pg_ivm — other than the mentioned points above regarding being an extension, I believe it is currently still a bit of a "batch processor in disguise" and not ripe yet for real-world use cases. Doing streaming SQL at scale for real-world use cases is no easy task, and I believe the way pg_ivm stores data (PG tables vs. storage engine built for streaming), passes data between nodes ("static rows" and not "changes in data" that can be consolidated), and executes queries (still missing support for basic operators like OUTER JOIN) just isn't enough yet for the use cases we see companies needing.


C.R.: The isolation Epsio offers by running on a separate instance is compelling. Ultimately, though, it has to write back into the database. In my experience, it’s possible for stream processing systems to overwhelm OLTP systems that they write into.


One example would be an Epsio instance that is offline for an extended period of time, then comes back and has to catch up by reading all of the CDC logs it missed. In such a scenario, I could imagine Epsio inserting data very frequently for a burst of time. How does Epsio prevent such issues?


G.K.: One of the exciting things in streaming SQL technologies is the concept of consolidations. To avoid redundant calculations/writes back to the DB, consumed changes are "consolidated" internally before writing back to database. This means that, for example, if you have 1M changes that affect a specific COUNT aggregations you have, instead of updating the result COUNT 1M times, all the changes will be consolidated into a single UPDATE to reflect the latest count after processing all the changes. Another example is if a row gets updated 100 times — the changes will be "consolidated" into a single update of the last value of the row.


Additionally, since the engine ensures that the outputted results are transactionally correct (i.e., a single transaction in the PostgreSQL/MySQL base tables is never split across multiple transactions updating the results table), Epsio actually only uses up to a single connection per results table to update results, significantly limiting the amount of stress a single view can generate in the database (since both PostgreSQL and MySQL don't use more than one core per INSERT/DELETE operation).


Having said all the above, every piece of software has its edge cases. If you have hundreds of large views that need to be fully rewritten after a long downtime, it might still be smart to limit the number of connections the `epsio_user` (the user with limited permissions created for Epsio to have access to the database) can create on the database!


C.R.: There seem to be a few different ways to implement incremental materialized views. Companies likeMaterializeandFelderausetimely dataflow,differential dataflow, andDBSP. Can you give me a 10,000 foot view of these approaches, and which you chose for Epsio?


G.K.: Sure! So basically, both timely/differential dataflow and DBSP are pretty awesome new theories/frameworks/libraries that allow you to create incremental materialized views with a handful of benefits that the more "legacy" (e.g.,Flink) stream processors don't offer:

- Being highly parallel while promising high consistency - Both differential and DBSP allow you to process in parallel a stream of changes, while always ensuring the result is consistent (for example, if a user adds $100 to their bank balance and then withdraws $90 — their bank balance would never reflect the withdrawal before the addition).
- Supporting "iterative" syntax - Both differential and DBSP support "iterative" syntax, meaning they can efficiently handle recursive queries or computations that depend on previous results.


Apart from the above benefits, they offer a new (and very elegant!) way to look at changes in data and process them much more efficiently compared to more "old-school" ways.


Although not directly based on differential dataflow/DBSP, Epsio's approach is probably more similar to the differential dataflow approach, although not completely similar (we are disk-based and have approached a couple of things differently given the use case Epsio is trying to optimize for).


C.R.: Users sometimes have a hard time understanding whereincremental view maintenance(IVM) fits into their stack. I most often see it used for fraud detection, where fraud detection models need up to date information. What other use cases and verticals do you see it being adopted in? What problems can you solve with it that users might not be aware of?


G.K.: Since the "Streaming SQL" world evolved out of the streaming world, most people initially associate it with "streaming" use cases like fraud /anomaly detection, notification, and so on. However, we've seen a pretty big shift in the last couple of years from those use cases to more SQL-related use cases.


Such use cases, which run complex and non-ad hoc queries on changing datasets, are common in areas like:

- Customer facing analytics (e.g. dashboards)
- Data transformations an enrichments (e.g. incremental DBT)
- Real time reporting


In classic "streaming" use cases, the main benefit of IVM was the ease of writing SQL rather than writing custom code. In the use cases above, the benefits are more about query performance and cost—how easy it is to deliver performant, cost-effective queries. No matter how fast or efficient a traditional database is, if you are running a heavy query and most of the dataset hasn’t changed since the last run, there is a lot of wasted compute. This translates into either higher cost, higher latency, or both.


We've seen companies make customer-facing analytics 100x faster, drop infrastructure costs by an order of magnitude, and turn reports that took hours to execute into ones that complete in under a second.


C.R.: Thanks for taking the time to talk with me. Let’s wrap things up. Where do you see IVM headed in the next few years. Any other parting thoughts? Where can readers get in touch with you?


G.K.: Happy to!


Regarding the upcoming years in IVMs, I think exciting times are coming. Whether it's in the use cases we earlier discussed or new use cases that emerge as IVM technologies evolve (like what the folks at ReadySet are working on with database caching), I believe IVMs offer a pretty fundamental change in how organizations can work with their data (i.e., building data structures around specific queries vs. trying to store data to be "generically" fast for any query) and that we're going to see them much more widely used!


For anybody interested in learning more aboutEpsio, you can head over to our website atepsio.ioor just ping us atcontact@epsio.io. We’re always happy to chat!
