---
title: "Everything You Need to Know About Incremental View Maintenance"
subtitle: "An overview of incremental view maintenance, why it’s useful, and how it's implemented."
date: 2025-04-18T18:28:00+00:00
url: https://materializedview.io/p/everything-to-know-incremental-view-maintenance
slug: everything-to-know-incremental-view-maintenance
word_count: 2426
---


Incremental view maintenance has been a hot topic lately.Materializehas been around for a while, but newcomers like PostgreSQL’s (semi-working)pg_ivmextension,Feldera,Epsio,Bytewax, and many others are starting to make noise. In the data warehousing space,Clickhousesupports IVMsanddbtnow hasincremental models(though, still batch-based). On the front-end, sync engines look increasingly like IVM engines;ZeroandElectricSQL﹩ come to mind.Sam Willis(of ElectricSQL)teasedthe idea of IVM on ElectricSQL and has implementedD2TS, a differential dataflow engine in TypeScript.


This post will provide a high-level overview of what incremental view maintenance is, why it’s useful, and how it can be implemented. We’ll then look briefly at three (relatively) recent research papers:timely dataflow,differential dataflow, andDBSP; these influential papers have influenced many (but not all) of the products listed above.


## What is IVM?


(If you already know what an IVM is, you can skip this section.)


To understand incremental view maintenance, we must first understand views. In this context, a view is a projection of data in a specific way. Pivot tables are a view: you have a spreadsheet with data, and you create a pivot table to filter and aggregate the data from the source spreadsheet. Similarly, a table in a database can be thought of as a spreadsheet, and a database view can be thought of as a pivot table. Views in databases are defined using SQL, rather than the UIs you’re used to in Excel and Google Sheets.


Continuing with our pivot table analogy, when a user updates data in their spreadsheet, the pivot table needs to be updated to reflect changes in its filters and aggregates. The same thing applies for database tables and views.


There are many approaches to view updates. The simplest way is to re-execute the query every time the view is accessed. In Excel, this would mean every time the pivot table is viewed, it must re-run its query on the source data; the same applies for database views.


Refreshing a view on every query can be slow and costly for large datasets, though. A spreadsheet with millions of rows might halt a user’s progress for several seconds. A database with billions (or trillions) of rows might block things for much longer. An alternative is to use materialized views. A materialized view is a cached result of the view. Rather than re-computing views on every read, they are refreshed periodically. Once the computation is complete, the new version of the view is used.


This approach—periodically reprocessing the entire dataset—trades data freshness for lower read latency. Queries on views will be faster since their data has already been computed, but the data will reflect an older version of the data from when it was last refreshed. Reprocessing the entire dataset can also be wasteful. A change to a single row in the source data requires reprocessing all the source data to generate the new materialized view.SELECT COUNT(*)has to recount every row to discover that only one new row was inserted.


Incremental view maintenance addresses these problems. Rather than reprocessing the entire dataset every time a change occurs, IVM reprocesses only the view data affected by the change (the delta). This approach dramatically decreases the cost of maintaining the materialized view. The DBSP paper illustrates this well:


> Informally, QΔ built by our algorithm, is faster than Q by a factor of O(|DB|/|ΔDB|). In practice this may be an improvement of several orders of magnitude. For our example above |DB|≅10⁹ and |ΔDB|≅10², this can make QΔ10 million timesfaster!


Cheap updates allow us to refresh materialized views more frequently. In doing so, we can keep materialized views more up to date with their source data, thereby reducing data latency. Best of all, read latency can remain largely unaffected since readers continue to query pre-computed data.


## How do IVM engines work?


Now that we understand what IVM is, let’s discuss how they have historically worked. There are two things to consider:

- When do incremental updates occur?
- How do we know what data needs to be updated?


The answer to the first question is fairly straightforward. Incremental materialized views are computations like any other; they can run on a fixed schedule, on an ad-hoc basis, or with a trigger. In practice, the last option—a trigger—is usually used to watch for newly changed data. In a data warehouse, Airflow’striggers and sensorsdetect changes. Similarly, developers can write triggers in OLTP databases to update views whenever source tables are mutated. OLTP databases that have built-in IVM support also usually update views as source data changes. Stream processors follow the same pattern: state is updated as new events arrive.


The second question—knowing what data needs to be updated—is trickier. The most intuitive approach is to write code or ad-hoc queries to react to triggers and update data. For example, we might have anorderstable and acustomer_order_totalsview. We can thenwrite a triggerto updatecustomer_order_totalswhenever data is inserted intoorder.


```
CREATE OR REPLACE FUNCTION orders_insert_trigger_fn()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO customer_order_totals (customer_id, total_amount)
    VALUES (NEW.customer_id, NEW.amount)
    ON CONFLICT (customer_id)
    DO UPDATE SET total_amount = customer_order_totals.total_amount + EXCLUDED.total_amount;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;
```


Triggers and ad-hoc code work for simple cases. But complex incremental queries that use joins, window functions, or recursive algorithms are very difficult to write by hand. A more systematic approach is needed.


The systematic approach many databases have relied on uses bag algebra (relational algebra). Users start by defining an incrementally maintained materialized view as a SQL query. The database then translates the SQL query into relational algebra operations such as select, project, union, intersect, join, difference, and so on. Once in relation algebra form, there is a bunch of math that shows inserts and deletes (called deltas) from source tables can be fed into the relational expression to compute the difference that must be applied to the materialized view. PostgreSQL’sincremental view maintenancewiki is a good starting point if you want to learn more.


Problem solved, right? Developers can continue to define materialized views in standard SQL, and databases can use fancy math to operate on just the deltas rather than recomputing everything. Unfortunately, not. It turns out, the bag algebra approach does not work well for complex and computationally expensive queries, especially with recursive or nested structures. While we’ve increased our expressiveness and ease of use, our IVM is no longer as cheap as before.


## A Modern Approach


This leads us to the papers three papers I mentioned at the beginning of this post:Naiad: a timely dataflow system,Differential dataflow,DBSP: Incremental Computation on Streams and Its Applications to Databases. These papers collectively present a different way to build an IVM engine that is:

- Fast enough to update materialized views on every data change
- Expressive enough that developers can use query languages such as SQL orDatalogto define views
- Flexible enough to be used with stream processors as well as databases


Frank McSherry, one of the foremost contributors to this space, describes these new innovations as a set of tools with different levels of flexibility and opinions. The lowest level, and most flexible, is timely dataflow. Differential dataflow is built on top of timely dataflow, and enforces some requirements on the user in order to calculate incremental updates. DBSP enforces still more requirements on the user in exchange for a simpler implementation. Let’s look at how these three systems build off one another.


### Timely Dataflow


Timely dataflow provides a model of time that makes it easier to do IVM computation without sacrificing expressiveness. Time is modeled as a vector that includes both an epoch as well as a loop counter.


![](https://substackcdn.com/image/fetch/$s_!pDIf!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9a4a87c3-2104-4916-9aad-2bd3130bfbf4_780x182.png)

*Section 2.1 inNaiad: a timely dataflow system*


As the name implies, loop counters keep track of what iteration a specific event is on. I won’t go into detail on why this is important (see the paper), but it means timely dataflow can support deeply nested loops very easily. Graph processing algorithms, in particular, benefit from this. Indeed, the paper spends a large amount of time talking about this use case.


The next innovation in timely dataflow is how it handles time. Traditionally, time updates (“punctuations”) are sent as special events or metadata in the data stream; this forces time to cascade sequentially through a dataflow. A task receives a new time update, and forwards that outputs downstream. Such an approach can cause bottlenecks.


Timely dataflow uses out-of-band watermark broadcasts. This sounds fancy, but it just means time is tracked outside of data streams—the data and control planes are separate. Timely dataflow has every task tell every other task in the dataflow how far it’s processed outside of the data streams. Armed with this information, tasks can get a global view of time and determine when they can make forward progress. Tasks in the same dataflow can even be processing different points in time, or multiple points in time. The takeaway is that the computation can happen concurrently (and thus faster) than the bag algebra approach.1


Practically speaking, the API for timely dataflow is fairly simple. It has four methods: SendBy, NotifyAt, OnRecv, OnNotify. The send/recv methods are to send and receive events, and the notify methods are for advancing time. I mention this because I like to think of timely dataflow a lot like Hadoop’s Map/Reduce: a powerful, but low-level framework for data processing.


### Differential Dataflow


Differential dataflow introduces “differential computation”:


> The novelty of differential computation is twofold: first, the state of the computation varies according to a partially ordered set of versions rather than a totally ordered sequence of versions as is standard for incremental computation; and second, the set of updates required to reconstruct the state at any given version is retained in an indexed data-structure, whereas incremental systems typically consolidate each update in sequence into the “current” version of the state and then discard the update.


The paper is very technical (I don’t understand the math in it). The gist is that it keeps track of multiple versions of data states, arranged in a partial order, rather than just a linear sequence (see the paper for examples). Timely dataflow timestamps are used to track the order. The arrangement allows the system to selectively reuse prior computations, significantly reducing the amount of work when the data is updated.


Once differential computation is defined, the paper shows (in section 4.3) that standard SQL-like operators can be built above the computation engine. The result is that developers can express incremental views using high-level query languages like SQL or Datalog. The engine handles joins, aggregations, and even recursive computations efficiently. This automation significantly simplifies building and maintaining IVM systems, especially for complex scenarios such as graph analytics or deeply nested computations. Continuing with the Hadoop ecosystem metaphor, you might describe this as thePigorCascadinglayer.


### DBSP


I had to take one electrical engineering class in college. I remember being blown away when I learned that any circuit could be expressed using nothing butNAND gates(not-and’s). This property is known asfunctional completeness, a property that it shares with NOR gates.


> …any other logic function (AND, OR, etc.) can be implemented using only NAND gates. An entire processor can be created using NAND gates alone.


I raise this idea because DBSP is based ondigital signal processing(DSP). The authors realized that incremental view maintenance looks somewhat similar to differentiation and integration in DSP. And much like the NAND gate phenomenon I learned about in college, the DBSP paper presents four operators (lift, delay, and two operators for recursive programs) that are the foundation for all relational operations in SQL. To get a flavor, here’s how the lift operator is depicted:


![](https://substackcdn.com/image/fetch/$s_!lQVb!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9e4ddf5a-c7ce-44ba-ba99-249bb0705a8f_914x78.png)


This is simply a map operator. The delay operator is also simple. It’s represented in the paper asz⁻¹, and it delays output by one step.


![](https://substackcdn.com/image/fetch/$s_!QuLT!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F453f29e1-33de-4a78-9d8b-1766d5e6c435_824x90.png)


Using circuit design and relational algebra, the paper is able to show that arbitrary SQL queries can be translated into DBSP circuits. Once converted into a DBSP circuit, the paper then shows that the circuit can be converted to an incremental DBSP circuit. This is a really powerful idea. DBSP can convert any batch-based SQL to an incremental query.


![](https://substackcdn.com/image/fetch/$s_!mOZT!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdaf3ccef-9bd3-4cb6-a3a0-bf86d67fd2e9_1860x1214.png)


DBSP does make some tradeoffs when compared to differential dataflow. It simplifies the programming model by constraining how time and state management occur. This simplification limits some of the concurrency gains we see in timely and differential dataflow. In exchange for this, DBSP offers a simpler, more accessible framework for typical database and stream processing workloads.


## Putting it all Together


Ultimately, the progression from timely dataflow to differential dataflow and then to DBSP shows a clear trajectory: moving from highly flexible, low-level frameworks toward more structured, to easier-to-use incremental computation systems.


The ideas pioneered by these three papers underlie many of the recent incremental view maintenance implementations. Materialize leverages differential dataflow directly, while newer entrants like Feldera are built on DBSP. Even frontend tools are shifting toward differential-like incremental maintenance paradigms, demonstrating the broad applicability and utility of this research.


Yet, IVM engines still have a long way to go. IVM in stream processors is still a work in progress. Many databases have missing or incomplete IVM implementations. A PostgreSQL implementation would be a very big deal. PerhapsParadeDBwill build this next?Nikhil Benesch, former CTO of Materialize, apparently contemplated this early on:


Differential dataflow is just really complicated. A few years ago,Jamie Brandonasked,Why isn't differential dataflow more popular?His post is worth reading. The firstHackernews responsehas a ring of truth to it:


> Indirectly answering the question - I've skimmed through the git README, the abstract and all the pictures in the academic paper that it references.I have no idea what this thing does. Can someone explain in simple terms what it does?


But systems like those I list at the top of this post make it more accessible. Rather than complex APIs and semantics, developers can use SQL. DBSP could unlock more IVM solutions, too. Getting this technology into everyone’s hands will be a very big deal.


A special thanks toFrank McSherry,Lalith Suresh, andGunnar Morlingfor feedback on early drafts.


---


#### Book


Support this newsletter by purchasingThe Missing README: A Guide for the New Software Engineerfor yourself or gifting it to someone.


![](https://substackcdn.com/image/fetch/$s_!CI0B!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fde442631-41a6-4119-a99a-62957cd53edb_870x978.png)


Buy Now


---


#### Disclaimer


I occasionally invest in infrastructure startups. Companies that I’ve invested in are marked with a ﹩ in this newsletter. See myLinkedIn profileandMaterialized View Capitalfor a complete list.

[1](https://materializedview.io/p/everything-to-know-incremental-view-maintenance#footnote-anchor-1-161506403)

Frank McSherry was quick to point out that out-of-band was borrowed fromOut-of-Order Processing: A New Architecture for HighPerformance Stream Systems.Tyler Akidauet al. also cite the OOP paper inMillWheel: Fault-Tolerant Stream Processing at Internet Scale, which influenced Google’s Dataflow and Beam products.
