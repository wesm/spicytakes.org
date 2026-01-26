---
title: "Nosql Definition"
description: "âCloudâ has become a very over-hyped term over the last few years.   One of the characteristics of over-hyped words is that they have   little or no definition to them (yesNosqlDefinitionI'm   loo"
date: 2013-07-11T00:00:00
tags: ["database", "nosql"]
url: https://martinfowler.com/bliki/NosqlDefinition.html
slug: NosqlDefinition
word_count: 610
---


As soon as we started work on [Nosql Distilled](https://martinfowler.com/books/nosql.html) we were
  faced with a tricky conundrum - what are we writing about? What
  exactly is a NoSQL database? There's no strong definition of the
  concept out there, no trademarks, no standard group, not even a manifesto.


The term originally surfaced at [an informal
  meetup](http://blog.oskarsson.nu/2009/06/nosql-debrief.html) on June 11 2009 in San Francisco organized by Johan
  Oskarsson. 1At the session there were presentations from Voldemort,
  Cassandra, Dynomite, HBase, Hypertable, CouchDB, and MongoDB.
  The term caught on rapidly and few people would argue that only the
  databases mentioned at that meeting should be called NoSQL.


1: 
       Although this is the origin of “NoSQL” as we use it now, it wasn’t the
       first time someone used the word “NoSQL”. The word was first used as the
       name of an [open-source
       relational database](http://www.strozzi.it/cgi-bin/CSA/tw7/I/en_US/NoSQL/Home%20Page) in the late 90's, a project led by Carlo Strozzi.
       The name didn't get much attention and, other than the terminological
       coincidence, hasn't any bearing on “NoSQL” in today's usage.


Indeed there's often a twist in the name itself: many advocates
  of NoSQL say that it does not mean a “no” to SQL, rather it means
  Not Only SQL. On this point I think it's useful to separate an
  individual database from the kind of ecosystem that NoSQL advocates
  see as the future. When we say “x is a NoSQL database” I think it's
  silly to interpret NoSQL as “Not Only” because that would render the
  term meaningless. (You could then reasonably argue that SQL Server
  (say) is a NoSQL database.) So I think it's best to say a “NoSQL
  database” is a “no-sql” database. You should separately interpret the
  NoSQL ecosystem as a “not only” - although I prefer the term
  [PolyglotPersistence](https://martinfowler.com/bliki/PolyglotPersistence.html) for this usage. 2


2: 
       If we take the “not-only” interpretation, then we should write
       “NOSQL” rather than “NoSQL”. I almost always see it written as “NoSQL”.


Even with this matter out of the way, it's still not easy to
  define a NoSQL database. Does any database that doesn't use SQL
  qualify? How about older database technologies such as [IMS](http://en.wikipedia.org/wiki/IBM_Information_Management_System)
  or [MUMPS](http://en.wikipedia.org/wiki/MUMPS)? How
  about a relational system that didn't have SQL (such as the early [Ingres](http://en.wikipedia.org/wiki/Ingres_(database)))?
  What happens if someone manages to bolt a SQL interface onto one of the
  original septet?


So for our book we took a view that NoSQL refers to a particular
  rush of recent databases. Some characteristics are common amongst
  these databases, but none are definitional.

- Not using the relational model (nor the SQL language)
- Open source
- Designed to run on large clusters
- Based on the needs of 21st century web properties
- No schema, allowing fields to be added to any record without controls


While I'm used to the blurry lines of definitions in the
   software industry, I confess my heart sinks at yet another one. But
   the important thing is that these databases provide a important
   addition to the way we'll be building application in next couple of
   decades. A lack of a clear definition will be no more than a gnat
   bite on their future successes.


## Notes


1: 
       Although this is the origin of “NoSQL” as we use it now, it wasn’t the
       first time someone used the word “NoSQL”. The word was first used as the
       name of an [open-source
       relational database](http://www.strozzi.it/cgi-bin/CSA/tw7/I/en_US/NoSQL/Home%20Page) in the late 90's, a project led by Carlo Strozzi.
       The name didn't get much attention and, other than the terminological
       coincidence, hasn't any bearing on “NoSQL” in today's usage.


2: 
       If we take the “not-only” interpretation, then we should write
       “NOSQL” rather than “NoSQL”. I almost always see it written as “NoSQL”.
