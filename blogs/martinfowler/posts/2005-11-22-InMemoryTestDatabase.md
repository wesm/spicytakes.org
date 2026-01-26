---
title: "In Memory Test Database"
description: "An in-memory database is a database that runs entirely in main memory, without touching a disk. Often they run as an embedded database: created when a process starts, running embedded within that proc"
date: 2005-11-22T00:00:00
tags: ["testing", "database"]
url: https://martinfowler.com/bliki/InMemoryTestDatabase.html
slug: InMemoryTestDatabase
word_count: 821
---


An in-memory database is a database that runs entirely in main
memory, without touching a disk. Often they run as an embedded
database: created when a process starts, running embedded within that
process, and is destroyed when the process finishes.


While most people think of databases as large disk-centered
	creatures, there's a small but busy world of in-memory databases out
	there. There are applications which need fast access to some sort of
	managed data which doesn't need to be persisted either because it
	doesn't change, or it can be reconstructed (imagine a routing table
	in a router, or an [EventPoster](https://martinfowler.com/bliki/EventPoster.html).)


Yet even developers of traditional database systems can find an
	in-memory database useful, particularly for testing. When
	you're developing an enterprise application, tests that hit the
	database can be a huge time drain when running your test suites. Switching
	to an in-memory database can have an order of magnitude effect which
	can dramatically reduce build times. Since most ThoughtWorkers get
	the shakes if they haven't had a green bar recently, this makes a
	big difference to us.


There are two routes people seem to take to a in-memory database
	for testing. The first one is to use a SQL in-memory database
	library. In Java-land the popular one seems to be
	[HSQLDB](http://hsqldb.org/). Elsewhere [SQLite](http://www.sqlite.org/) and [Firebird](http://firebird.sourceforge.net/) come up. The nice thing
	about these tools is that they allow you to use regular SQL to query
	them. One issue is that they may not support quite the same dialects
	or have all the features of the target database. You can do
	something similar by running a file-based database on a ram disk,
	which allows you to keep the test and production deployments closer
	to each other.


Another route is to abstract all the database access behind a
	[Repository](https://martinfowler.com/eaaCatalog/repository.html). Then you can swap out the database with regular
	in-memory data structures. Often just a bunch of hash-tables for the
	entry points to the object graph is enough. One of the strengths of
	the repository approach is that it gives you a consistent way to
	access (and stub out) non SQL data sources too. This
	means that your object-relational mapping system is also hidden
	inside the repository.


Indeed a few people actively dislike using SQL in-memory
databases under the belief that they encourage spreading either SQL or
object-relational mapper code around the domain model. Running SQL
in-memory may removes much of the pain of slow access but acts as a
deodorant to cover the smell of a missing repository.


Testing is the main driver thus far, but I think there's more to
	come from in-memory databases. Memory sizes are now enough that many
	application databases can be loaded into memory. If you use an approach that
	keeps an event log of all changes to your application state, you can
	treat the in-memory database as a cache of the result of applying
	the log, rebuilding it and snapshotting it as you need. Such styles
	can be very scalable and have high performance in cases where you
	have lots of readers and few writers. I've run into a few cases
	where people have used in-memory databases for very high performance
	applications. A difference here is that these experiences tend to be
	with niche commercial databases while for testing people seem to
	prefer open-source.


[Prevayler](http://www.prevayler.org) got a lot of
attention for taking this kind of approach. People I know who tried it
found it's tight coupling to the in-memory objects and lack of
migration tools caused serious problems. But I think the approach of
persistent change logs as systems of record is a fertile ground to
explore in the future.


## Follow Ups


I got some interesting mail after writing this page, so I thought
	I'd share some of the points.


One correspondent said he liked using in-memory databases for
	tasks that SQL does well but objects don't do as well. There are
	certainly cases where SQL can solve a problem rather more elegantly
	than objects or procedural code, although usually I find it's only a
	minority of developers who like thinking in SQL.


My colleague Steve Sparks told me about a recent project where for
testing they would pull data from the live database on the first call
then save that data in a file to initialize the in-memory repository
so that subsequent queries wouldn't hit the database. I first saw that
done in the C3 project, it kept it's data in a hash table keyed by the SQL query
string. If there was no value it went to DB2 and cached the
result.


Steven Graves pointed out that my original entry didn't really
		talk enough about the general uses of in-memory databases, as a
		result of which I did some rewriting and gave the item a re-titling.


(Thanks for Peter Becker, Zane Rockenbaugh, and Steve Sparks
		for their comments to me. I should also thank various unspecified
		ThoughtWorkers for helpful comments on our internal mailing list.
