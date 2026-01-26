---
title: "Integration Database"
description: "In many organizations, it's expected that any persistent data   will be stored in relational databases that are managed by a central   database management group. There are various reasons for such   c"
date: 2013-02-25T00:00:00
tags: ["application integration", "database"]
url: https://martinfowler.com/bliki/IntegrationDatabase.html
slug: IntegrationDatabase
word_count: 223
---


An integration database is a database which acts as the
  data store for multiple applications, and thus integrates data across
  these applications (in contrast to an [ApplicationDatabase](https://martinfowler.com/bliki/ApplicationDatabase.html)).


An integration database needs a schema that takes all its client
  applications into account. The resulting schema is either more
  general, more complex or both - because it has to unify what should
  be separate [BoundedContexts](https://martinfowler.com/bliki/BoundedContext.html). The database usually is controlled by
  a separate organization to those that develop applications and database changes are more
  complex because they have to be negotiated between the database
  group and the various applications.


The benefit of this is that sharing data between applications
  does not require an extra layer of integration services on the
  applications. Any changes to data made in a single application are
  made available to all applications at the time of database commit -
  thus keeping the applications' data use better synchronized.


On the whole integration databases lead to serious problems
  becaue the database becomes a point of coupling between the
  applications that access it. This is usually a deep coupling that
  significantly increases the risk involved in changing those
  applications and making it harder to evolve them. As a result most software
  architects that I respect take the view that **integration
  databases should be avoided**.


Updated 2015-07-01: added link to Bounded Context and final paragraph
