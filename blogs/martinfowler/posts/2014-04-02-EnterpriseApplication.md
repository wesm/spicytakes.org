---
title: "Enterprise Application"
description: "MostEnterpriseApplicationsstore persistent data with a   database. This database supports operational updates of the   application's state, and also various reports used for decision   support and ana"
date: 2014-04-02T00:00:00
tags: ["application integration", "application architecture"]
url: https://martinfowler.com/bliki/EnterpriseApplication.html
slug: EnterpriseApplication
word_count: 931
---


In the early part of this century, I worked on my book [Patterns
  of Enterprise Application Architecture](https://martinfowler.com/books/eaa.html). One of the problems I
  had when writing the book was how to title it, or rather what to
  call the kinds of software systems that I was writing about. I've
  always been conscious that my experience of software development has
  always been focused on one particular form of software - things like
  health care records, foreign exchange trading, payroll, and lease
  accounting. These are very different to embedded software inside
  printers, games, flight control software, or telephone switches. I
  needed a name to describe these kinds of systems and settled on the
  term âenterprise applicationâ.


![](images/enterpriseApplication/sketch.png)


As I so often have to say, there is no formal definition for this
  term. However there are some characteristics that enterprise
  applications have in common.


Enterprise applications usually have **a lot of persistent data**,
  usually managed by some kind of database management system. Usually
  this database is relational, but increasingly we're seeing NoSQL
  alternatives. This data will usually be longer lasting and more
  valuable than the applications that process it.


This **data is accessed and manipulated concurrently**. The
  numbers vary a lot, in-house applications may have a few tens of
  users, but customer-facing web applications can easily have tens of
  thousands. Despite high levels of concurrency, many enterprise
  application developers don't think much about critical regions, race
  conditions and other elements of classic concurrent programming.
  Instead they build their thinking on top of transactions managed by
  databases or specialized transaction management tools.


With so much data, enterprise applications have **a lot of user
  interface screens** to handle it. Usually the same data is
  manipulated in different ways in different contexts. Users vary from
  regular to occasional users, so the interfaces need to match
  different levels of familiarity. There is also a significant amount
  of offline (batch) processing that is easily forgotten.


Even if you are building a brand new enterprise application, you
  don't do so in isolation. Instead you'll need to **integrate with
  other enterprise applications**. These systems are built by a wide
  range of teams, some from vendors who sell to many customers, others
  built internally just for your organization. These applications will have been written over many
  decades in a host of different technologies, some of which you'll
  have to ask your mother about. There are many
  integration mechanisms to deal with - file exchange, shared
  databases, messaging middleware. Every so often there will be an
  attempt to rationalize all this communication technology, but they
  never entirely succeed leaving behind more complexity in
  their wake.


Even when different applications access the same data there is
  considerable **conceptual dissonance** between them, a customer may mean
  something quite different to the sales organization than it does to
  technical support. The same sounding entity has different fields in
  different contexts, or worse have fields with the same name yet
  different meanings.


And then there's so-called âbusiness logicâ. When you are writing
  an operating system you strive to keep the whole thing logical and
  stive to discover and implement simplifications to keep the software
  straightforward and reliable. But business rules are given to you as
  they stand, and if you want to change them you need sixty-seven meetings and three
  vice-presidents retiring. They are usually a haphazard array of strange
  conditions that interact in surprising ways. Their insanity derives
  from a good reason, each one is a case where salesman could close a
  particular deal by offerring some special one-off condition. Do this
  a thousand times and you have the **complex business âillogicâ** that lies
  in the heart of many enterprise applications.


Enterprise applications can be large or small. Often discussion
  focuses on large, complex applications, but there is also a
  challenge for smaller applications that need to be built quickly.
  Big systems make a lot of noise when they go wrong, yet the
  cumulative effect of small systems can have a surprising effect on
  an enterprises's health.


Coming up with names for things is always tricky. You need to use
  a minimum number of words, and want them to trigger the right
  connotations in the readers' minds, so that you don't have to
  constantly remind them what the definition means. On the whole I've
  been reasonably happy with my choice, but since I finished the book
  the word enterprise has taken on connotations which don't quite fit
  my usage.


One problem that's emerged since the book is that âenterpriseâ
  now usually means a large, well-established company. People think of
  G.E. or Siemens rather than Facebook, Etsy, or a company of a
  hundred people producing custom T-shirts. But according to my
  definition above, even small start-ups rely on software that I would
  call an enterprise application. So even though the Ruby on Rails
  community has ended up using enterprise as an insult, I would call
  Ruby on Rails a framework for building enterprise applications and
  [BaseCamp](https://basecamp.com) a classic example of
  an enterprise application. (Just don't tell DHH I said so or he'll
  turn me into a hood ornament.)


These connotations around âenterpriseâ have made me muse about
  whether we need a different term. When I was writing P of EAA my
  working title was âInformation Systems Architectureâ, but we felt
  that âinformation systemsâ had its own undesirable connotations of
  elder technologies. I guess I could go really retro and use âdata
  processingâ, but on the whole âenterprise applicationâ still seems a
  better term than anything else I could come up with.


This post is adapted from the definition of Enterprise
    Application in the introduction of [P of EAA.](https://martinfowler.com/books/eaa.html)
