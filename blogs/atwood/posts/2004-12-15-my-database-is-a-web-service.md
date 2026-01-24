---
title: "My Database is a Web Service"
date: 2004-12-15
url: https://blog.codinghorror.com/my-database-is-a-web-service/
slug: my-database-is-a-web-service
word_count: 1283
---

In [The Fallacy of the Data Layer](https://web.archive.org/web/20050113212359/http://www.theserverside.net/articles/showarticle.tss?id=FallacyDataLayer), Rocky Lhotka makes a case for something I’ve come to believe as absolute truth:


> *It is commonly held as a truth that applications have a UI layer, a business layer and a data layer. In most of my presentations and writing I use a four layer model: UI, business, data access and data storage. In this case the “data storage” layer is really the same as the traditional data layer in a 3-layer model.
> But I want to challenge this idea of a data layer. Over the past few months, in discussing service-orientation (SOA) as well as distributed object-oriented architecture, I have become increasingly convinced that the idea of a data tier, data layer or data storage layer is fundamentally flawed.
> Note that in this article I use the word “layer” to describe logical separation between concepts regardless of physical configuration, while “tier” means a physical separation. That said, the reality is that a typical data layer really is also a data tier, because most data layers exist in the form of SQL Server, Oracle or some other server-based database engine.
> Service-orientated design leads us to the idea that any software component used by more than one other software component (used by more than one “client”) should be a service. A service is a powerful unit of reuse, providing a contractual interface by which clients can interact with the service.
> More importantly, a service defines a trust boundary. This means that a service protects itself against invalid usage by clients. This is one of the defining elements of service-orientation and is a key benefit. The benefit is that a service can safely service many disparate clients because it trusts none of them. The service ensures that all clients get the same behaviors, and that any data sent to the service by any client is checked for validity based on the rules of the service.
> **My contention is that the traditional “data layer” is the ideal candidate to be a service.***


In other words, your data layer should be a web service.* Based on the applications I’ve worked on, I agree completely. I touched on this briefly in my [Who needs Stored Procs, Anyway?](https://blog.codinghorror.com/who-needs-stored-procedures-anyways/) entry – what I was really trying to say is that stored procedures are a terribly inadequate place to build a data API. Web Services, on the other hand, are ideal for building APIs:

- **A web service is the only level of abstraction that really buys you anything.** It’s as close to the holy grail as I’ve ever been: complete platform and technology independence. You really could have Macintosh or Dos clients using your API. Behind the scenes, you could decide to replace database technologies entirely (or move to the all stored procs approach), or migrate to an entirely different operating system. What other API interface offers anything even remotely close to this?
- **HTTP and SOAP are the cockroaches of platform technology.** They’ll probably outlive us both. If you’re bothering to create a formal API, why not create one using a technology that has a chance of surviving more than five years? Yes, COM+, I’m looking at you.
- **A web service forces you to keep your API methods simple and abstract.** A good API is difficult to get right, and easy to overcomplicate. A web service interface minimizes this risk. KISS!
- **A web service API can be developed and debugged independently of the UI and other layers.** Other API technologies (stored procedures, binary DLLs, remoting, etc.) make it a lot easier for undesired, accidental coupling to creep in, along with inappropriate opportunities to “optimize” for your particular implementation. They can also trap you in that interface: good luck passing objects to stored procedures, or getting remoting to work once you install .NET 2.0 on the server.
- **Database performance is almost always the bottleneck anyway**. Adding a web service to the mix doesn’t cost you anything. An additional 20ms of latency is just going to be lost in the noise of the 200ms it takes the database to process your query. Behind the façade of a web service, the optimization choices are almost infinite, so this choice will likely make you more performant, not less!


I’ve already been burned by this on one large application I worked on. Over my protests, we implemented a binary .NET remoting protocol – instead of a web service – for communication between the smart client and the server. All this in the name of performance. The remoting works fine, but the fallout from this decision was painful:

- It’s a giant pain to get developers set up on this project due to all the crazy server API dependencies they need on their machines. Less developers working on the project equals less getting done; it ends up being a barrier.
- Our API is far more complicated than it needs to be, and heavily tied to the client application. There’s less visibility into the nooks and crannies of a remotable DLL than there is to a simple web page with a list of methods. On a recent code review, I found *three* methods that all did the same thing. All of them had completely different names, of course.
- It’s difficult enough with our own developers; selling this API to other internal groups is an uphill battle. Just getting to “hello world” is far too much effort. I wish I could email them a link to a basic method to inspire confidence.
- We ended up writing a minimal web service to mediate some of the difficulty. Now we’ve committed the ultimate sin: we’re [repeating ourselves](http://www.artima.com/intv/dry.html). Why not have a single well designed API rather than one crazy hard-to-deploy one, and one that’s little more than a toy?
- Due to the inadequacy of remoting as a proper API abstraction layer, we ended up with a mish-mash of stored procedures, triggers, client-side rule enforcement, and raw SQL. And it will be incredibly painful to change any of it. Just writing about it is causing my arm to twitch uncontrollably.


With the inclusion of .NET runtime code support in upcoming versions of SQL Server, and even Oracle, you may be tempted to move more of your API into the database. But [don’t fall into that trap](https://web.archive.org/web/20060207115805/http://blogs.msdn.com/draper/archive/2004/07/13/182691.aspx), either:

kg-card-begin: html

> *
> How does the presence of managed code execution in the database improve matters?  Frankly, I don’t see it helping much at all unless you’re doing some of the things I mention above as a possible reason to consider porting from T-SQL.  On the other side of the fence, tossing your entire business logic layer into the database makes many of the positive improvements you could make to scalability all the more challenging:*
> You’re going to the DB box more often
> You’re chewing up more threads for greater periods of time.
> You’re running more code that’ll consume more resources.  Just think about all the temporary objects and associated GC pressure that box is going to have to endure.
> You’ve got additional locking scenarios to worry about.  A deadlock on a single app server is real trouble while in a distributed environment you’re just taking one of N boxes down with the deadlock.

kg-card-end: html

Give yourself options by choosing the right architecture early on. For most common business apps, **I feel very strongly that a web service data API *is* the right architecture.** And I have the scars to prove it.


*Yes, yes, SOA [doesn’t technically mean web service](https://web.archive.org/web/20051124094429/http://weblogs.asp.net/mnolton/archive/2004/12/15/313909.aspx). But in practical terms, it does.

[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[architecture](https://blog.codinghorror.com/tag/architecture/)
[service-orientation](https://blog.codinghorror.com/tag/service-orientation/)
[data storage](https://blog.codinghorror.com/tag/data-storage/)
[data access](https://blog.codinghorror.com/tag/data-access/)
