---
title: "Key Points from NoSQL Distilled"
description: "When we designed the book,NoSQL Distilled, we concluded    most chapters with some summary key points to act as a refresher    for people re-reading the book. We've included these on the website    as"
date: 2012-09-12T00:00:00
url: https://martinfowler.com/articles/nosqlKeyPoints.html
slug: nosqlKeyPoints
word_count: 1188
---


# Key Points from NoSQL Distilled


In our book NoSQL Distilled we summarize many chapters with a handful of key points. As a quick reference, weâve included the key points here.


Expand All | Collapse All


Pramod Sadalage & Martin Fowler: 12 Sep 2012


Ch. 1


## Why NoSQL?

- Relational databases have been a successful technology for
    twenty years, providing persistence, concurrency control, and an
    integration mechanism.
- Application developers have been frustrated with the impedance
    mismatch between the relational model and the in-memory data structures.
- There is a movement away from using databases as integration
    points towards encapsulating databases within applications and
    integrating through services.
- The vital factor for a change in data storage was the need to
    support large volumes of data by running on clusters. Relational
    databases are not designed to run efficiently on clusters.
- NoSQL is an accidental neologism. There is no prescriptive
    definition—all you can make is an observation of common characteristics.
- The common characteristics of NoSQL databases are
- The most important result of the rise of NoSQL is Polyglot Persistence.


Ch. 2


## Aggregate Data Models

- An aggregate is a collection of data that we interact with as
    a unit. Aggregates form the boundaries for ACID operations with
    the database.
- Key-value, document, and column-family databases can all be
    seen as forms of aggregate-oriented database.
- Aggregates make it easier for the database to manage data
    storage over clusters.
- Aggregate-oriented databases work best when most data
    interaction is done with the same aggregate; aggregate-ignorant
    databases are better when interactions use data organized in many
    different formations.


Ch. 3


## More Details on Data Models

- Aggregate-oriented databases make inter-aggregate
    relationships more difficult to handle than intra-aggregate relationships.
- Graph databases organize data into node and edge graphs; they
    work best for data that has complex relationship structures.
- Schemaless databases allow you to freely add fields to
    records, but there is usually an implicit schema expected by users
    of the data.
- Aggregate-oriented databases often compute materialized views
    to provide data organized differently from their primary
    aggregates. This is often done with map-reduce computations.


Ch. 4


## Distribution Models

- There are two styles of distributing data:



A system may use either or both techniques.
- Replication comes in two forms:

Leader-follower replication reduces the chance of update conflicts but peer-to-peer replication avoids loading all writes onto a single point of failure.


Ch. 5


## Consistency

- Write-write conflicts occur when two clients try to write the same data at the same time. Read-write conflicts occur when one client reads inconsistent data in the middle of another client's write.
- Pessimistic approaches lock data records to prevent conflicts. Optimistic approaches detect conflicts and fix them.
- Distributed systems see read-write conflicts due to some nodes having received updates while other nodes have not. Eventual consistency means that at some point the system will become consistent once all the writes have propagated to all the nodes.
- Clients usually want read-your-writes consistency, which means
    a client can write and then immediately read the new value. This can
    be difficult if the read and the write happen on different nodes.
- To get good consistency, you need to involve many nodes in data operations, but this increases latency. So you often have to trade off consistency versus latency.
- The CAP theorem states that if you get a network partition, you have to trade off availability of data versus consistency.
- Durability can also be traded off against latency, particularly if you want to survive failures with replicated data.
- You do not need to contact all replicants to preserve strong
    consistency with replication; you just need a large enough
    quorum.


Ch. 6


## Version Stamps

- Version stamps help you detect concurrency conflicts. When
    you read data, then update it, you can check the version stamp to ensure
    nobody updated the data between your read and write.
- Version stamps can be implemented using counters, GUIDs,
    content hashes, timestamps, or a combination of these.
- With distributed systems, a vector of version stamps allows you
    to detect when different nodes have conflicting updates.


Ch. 7


## Map-Reduce

- Map-reduce is a pattern to allow computations to be parallelized over a cluster.
- The map task reads data from an aggregate and boils it down to
    relevant key-value pairs. Maps only read a single record at a time
    and can thus be parallelized and run on the node that stores the
    record.
- Reduce tasks take many values for a single key output from map tasks and summarize them into a single output. Each reducer operates on the result of a single key, so it can be parallelized by key.
- Reducers that have the same form for input and output can be combined into pipelines. This improves parallelism and reduces the amount of data to be transferred.
- Map-reduce operations can be composed into pipelines where the output of one reduce is the input to another operation's map.
- If the result of a map-reduce computation is widely used, it can be stored as a materialized view.
- Materialized views can be updated through incremental map-reduce operations that only compute changes to the view instead of recomputing everything from scratch.


Ch. 12


## Schema Migrations

- Databases with strong schemas, such as relational databases,
    can be migrated by saving each schema change, plus its data
    migration, in a version-controlled sequence.
- Schemaless databases still need careful migration due to the implicit schema in any code that accesses the data.
- Schemaless databases can use the same migration techniques as databases with strong schemas.
- Schemaless databases can also read data in a way that's tolerant to changes in the data's implicit schema and use incremental migration to update data.


Ch. 13


## Polyglot Persistence

- Polyglot persistence is about using different data storage technologies to handle varying data storage needs.
- Polyglot persistence can apply across an enterprise or within a single application.
- Encapsulating data access into services reduces the impact of data storage choices on other parts of a system.
- Adding more data storage technologies increases complexity in
    programming and operations, so the advantages of a good data
    storage fit need to be weighed against this complexity.


Ch. 14


## Beyond NoSQL

- NoSQL is just one set of data storage technologies. As they increase comfort with polyglot persistence, we should consider other data storage technologies whether or not they bear the NoSQL label.


Ch. 15


## Choosing Your Database

- The two main reasons to use NoSQL technology are:
- It's essential to test your expectations about programmer productivity and/or performance before committing to using a NoSQL technology.
- Service encapsulation  supports changing data storage technologies as needs and technology evolve. Separating parts of applications into services also allows you to introduce NoSQL into an existing application.
- Most applications, particularly nonstrategic ones, should stick with relational technology—at least until the NoSQL ecosystem becomes more mature.


There are no key points for Chapters 8-11 since these are examples of database use
