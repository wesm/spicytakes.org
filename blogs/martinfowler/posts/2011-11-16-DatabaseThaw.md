---
title: "Database Thaw"
description: "In 2006, my colleague Neal Ford coined the termPolyglot   Programming, to express the idea that applications should be written   in a mix of languages to take advantage of the fact that different   la"
date: 2011-11-16T00:00:00
tags: ["database", "nosql"]
url: https://martinfowler.com/bliki/DatabaseThaw.html
slug: DatabaseThaw
word_count: 732
---


A few years ago I heard programming language people talk about
  the âNuclear Winterâ in languages caused by Java. The feeling was
  that everyone had so converged on Java's computational model (C# at
  that point seen as little more than a rip-off) that creativity in
  programming languages had disappeared. That feeling is now abating,
  but perhaps a more important thaw that might be beginning - the
  longer and deeper freeze in thinking about databases.


When I started in the software development profession, I worked
  with several people who had evangelized relational databases. I came
  across them in the object-oriented world. Many people at that time
  expected OO databases to be the next evolutionary step for
  databases. As we now know, that didn't happen. These days
  relational databases are so deeply embedded that most projects
  assume an RDBMS right out of the gate.


At [QCon](http://qconsf.com/sf2008/conference/) last
  week, there was a strong thread of talks that questioned this
  assumption. Certainly one that struck me was [Tim Bray's](http://www.tbray.org/ongoing/) keynote, which took a
  [journey](http://qconsf.com/sf2008/presentation/Application+Design+in+the+context+of+the+shifting+storage+spectrum) through several aspects of data management. In doing so he
  highlighted a number of interesting projects.

- [Drizzle](http://en.wikipedia.org/wiki/Drizzle_(database_server)) is a form of relational database, but one that eschews
    much of the machinery of modern relational products. I think
    of it as a RISC RDBMS - supporting only the bare bones of the
    relational feature set.
- [Couch DB](http://incubator.apache.org/couchdb/)
    is one of many forays into a distributed key-value pair
    model. Although a sharply simple data-model (nothing more than a
    hashmap really) this kind of approach has become quite popular in
    high-volume websites.
- [Gemstone](http://www.gemstone.com/products/smalltalk/) was one
    of the object database crowd, and I found the Gemstone-Smalltalk
    combination a very powerful development environment (superior to
    most of its successors). Gemstone is still around as a niche
    player, but may gain more traction through [Maglev](http://www.infoq.com/news/2008/05/MagLevAtRailsConf) - a project to
    bring its approach (essentially a fusion of database and virtual
    machine) to the Ruby world.


As well as this talk, there was a whole [track](http://qconsf.com/sf2008/tracks/show_track.jsp?trackOID=170) on alternative
   databases hosted by Kresten Krab Thorup. One of the additional
   tools mentioned there was [Neo4J](http://neo4j.org/) -
   a graph (network) database tool that earned some rare praise from
   Jim Webber.


The natural question to ask about these products is why they
   should prevail when the ODBMSs failed. What's changed in the
   environment that could thaw the relational grip? There are many
   hypotheses about why relational has been so dominant - my opinion
   is that their dominance is due less to their role in data
   management than their role in integration.


For many organizations today, the primary pattern for integration
   is [Shared Database Integration](http://www.eaipatterns.com/SharedDataBaseIntegration.html) - where multiple applications are
   integrated by all using a common database. When you have these
   [IntegrationDatabases](https://martinfowler.com/bliki/IntegrationDatabase.html), it's important that all these applications
   can easily get at this shared data - hence the all important role
   of SQL. The role of SQL as mostly-standard query language has been
   central to the dominance of relational databases.


The heating of the database space comes from the presence of
   alternatives to integration - in particular the rise of web
   services. Under various banners there's a growing movement for
   applications to talk to each other by passing text (mostly XML)
   documents over HTTP. The web, both in internet and intranet forms,
   has made this integration mode even more prevalent than SQL. This
   is a good thing, I've never liked the approach of multiple
   applications tightly coupled through a common database - you can't
   get bigger breach of encapsulation than that.


If you switch your integration protocol from SQL to HTTP, it now
   means you can change databases from being [IntegrationDatabases](https://martinfowler.com/bliki/IntegrationDatabase.html) to
   [ApplicationDatabases](https://martinfowler.com/bliki/ApplicationDatabase.html). This change is profound. In the first step it
   supports a much simpler approach to object-relational mapping -
   such as the approach taken by Ruby on Rails. But furthermore it
   breaks the vice-like grip of the relational data model. If you
   integrate through HTTP it no longer matters how an application
   stores its own data, which in turn means an application can choose
   a data model that makes sense for its own needs.


I don't think this means that relational databases will disappear
   - after all they are the right choice for many situations. But it
   does mean that now application developers should think about what
   the right option is for their needs. As non-relational projects
   grow in popularity and maturity, more and more will go for other
   options.
