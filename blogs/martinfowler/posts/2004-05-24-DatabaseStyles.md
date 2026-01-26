---
title: "Database Styles"
description: "When I talk about databases and how they relate to applications, I've found it useful to distinguish between two styles of database:ApplicationDatabaseandIntegrationDatabase. The difference between th"
date: 2004-05-24T00:00:00
tags: ["application integration", "database"]
url: https://martinfowler.com/bliki/DatabaseStyles.html
slug: DatabaseStyles
word_count: 273
---


When I talk about databases and how they relate to applications,
I've found it useful to distinguish between two styles of database:
[ApplicationDatabase](https://martinfowler.com/bliki/ApplicationDatabase.html) and [IntegrationDatabase](https://martinfowler.com/bliki/IntegrationDatabase.html). The
difference between the two lies in whether the database is controlled
and encapsulated within a single [ApplicationBoundary](https://martinfowler.com/bliki/ApplicationBoundary.html).


I've found that in discussions about how databases are managed,
often people assume that one of styles is being used - if different
participants assume different styles then the discussion can quickly
get very confused as the two styles imply very different assumptions
about database management. Certainly in the database and data
management communities, people tend to assume that databases will be
[IntegrationDatabase](https://martinfowler.com/bliki/IntegrationDatabase.html)s. This has been the working assumption
of many years of the database community. Increasingly, however, this
assumption has been questioned. Integration databases end up with
interfaces that have a large surface area and limited abilities to
separate interface from implementation. The resulting links between
applications and databases end up being brittle and thus difficult to
change.


The recent rise of Service Oriented Architecture seems to mean
very different things to different people, but one plausible thread is
a rise of autonomous applications with their own [ApplicationDatabase](https://martinfowler.com/bliki/ApplicationDatabase.html)
that communicate through service interfaces - effectively replacing [shared

database](http://www.enterpriseintegrationpatterns.com/SharedDataBaseIntegration.html) integration with [rpc](http://www.enterpriseintegrationpatterns.com/EncapsulatedSynchronousIntegration.html)

or [messaging](http://www.enterpriseintegrationpatterns.com/Messaging.html)

based integration. I'm very sympathetic to this view, particularly
favoring integration through messaging - which is why I encouraged the
development of 
[EIP](https://martinfowler.com/books/eip.html). In this view of the world the integration database is
no longer the default assumption.


So my principal point is this: beware of the difference between
the two database styles and take it into account when you are
discussing issues of database management.
