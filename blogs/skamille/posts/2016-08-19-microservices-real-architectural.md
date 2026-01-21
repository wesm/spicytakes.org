---
title: "Microservices: Real Architectural Patterns"
date: 2016-08-19
url: https://www.elidedbranches.com/2016/08/microservices-real-architectural.html
word_count: 3105
---


### A dissection of our favorite folk architecture


### Introduction

I’m fascinated by the lore and mystery behind
*microservices.*
As a concept, microservices feels like one of the most interesting folk architectures of the modern era. It’s useful enough to be applied widely across different usage patterns and also vague enough to mean many different things.
I’ve been struggling for a while with understanding what people really mean when they discuss “microservices.” Despite deploying what I would consider to be a version of that pattern in my last gig, it’s quite clear to me that the architecture we used is not the same as the pattern that all other companies use. Recently I finally interrogated someone who has deployed the pattern in a very different way than I have, and so I decided it would be illustrative to compare and contrast the circumstances of our architectures for those in the larger technical audience.
This article is going to have two examples. The first is the rough way “microservices” was deployed in my last gig, and why I made the decisions I made in the architecture. The second is an example of an architecture that is much closer to the “beautiful dream” microservices as I have heard it preached, for architectures that are stream-focused.

#### Microservices Basics

I think that microservices as an architecture evolved due to a few factors.
1. A bunch of startups in the late 2000s started on monoliths like rails, scaled their business and team quickly, and hit the wall on what could reasonably be done in that monolith
2. The cloud made it significantly easier to get access to a new server instance to run software
3. We all got much more comfortable with the idea that we were dealing with distributed systems and in particular got comfortable making network calls as part of our systems

This combination of factors — scaling woes, easy access to new hardware, distributed systems and network access — played a huge part in what I might call “microservices for CRUD.” If you have managed to scale a company to a certain level of success on a monolith but you are having trouble scaling the technology and/or the engineering team, breaking the monolith into a services-style architecture makes sense. This is a situation I encountered first-hand.
The arguments for microservices here look something like:
1. Services allow for independent axes of scaling. If you have a part of the system with higher load or capacity requirements than other parts, you can scale to meet its needs. This is certainly doable in a monolith, but somewhat more complicated to reason about.
2. Services allow for independent failure domains, to a more limited extent. Insofar as parts of your system are independently operable, you may want to allow for partial availability by splitting them out into services. For example, in a commerce app, if you can serve the checkout flow even when the product search flow is down, that might be considered a good thing. This is much more complicated in practice than it is in theory, and people make many silly claims about microservices that imply that any overlap in services means that they are not valuable. Independent failure domains are sometimes more of a “nice to have” than a necessity, and making the architecture truly account for this is not easy.
3. Services allow for teams to work independently on parts of the system. Again, you can do this in a monolith. I have done this in a monolith. But the challenge with monolith (and a related challenge with services in a monorepo (single source repository)) is that humans struggle to tangibly understand domains that are theoretically separate when they are presented as colocated by the source code. If I can see all of the code and it all compiles together and feels like a single thing, my tendency is to want to use it as a single thing. Grab code from here to use there, grab data from there to use here, etc.

A few more notes. “Monolith” and “monorepo” often get tangled up when talking about this world. A monolithic application is one where you have a set of code that compiles into a single main server artifact (possibly with some additional client artifacts produced). You can use configuration to make monoliths do almost anything you can imagine, including all of the services-type things above, but the image produced tends to include most if not all of the code in the repository. This does get fuzzy because sometimes teams evolve their monoliths to compile to a couple of specialized server artifacts via a combination of build tooling and configuration. I would generally still call this a monolithic architecture.
Monorepo, or monolith repository, is the model where you have a single repository that holds all of the code for any system you are actively changing (so, possibly excluding the source code for your OSS/external dependencies). The repository itself contains source code that accounts for multiple artifacts that are run as separate applications, and which can be compiled/packaged and tested separately without using the entire repository. Often this is used to enable certain shared libraries to change across all of the services that use those libraries, so that developers who support shared libraries can more easily evolve them instead of having to wait for each dependent team to adopt the newest version. The biggest downside of the monorepo model is that there’s not much OSS tooling that supports this, because most OSS is not built this way, so large investments in tooling are usually needed to make this work.

#### Microservices for CRUD-based Applications

Before I get to how to evolve a CRUD monolith to microservices, let me further articulate the architecture needed to build your traditional mid-sized CRUD platform. This type of platform covers a use case that is pretty well-trod, that of “transactions” and “metadata.”

> Transactions: User does an action that you want to persist, consistency of data is very valuable. The “Create, Update, Delete” of CRUD. Much less frequent than the “Read” actions of CRUD.


> Metadata: Information that describes things to the users, but is usually only modified by internal content creators, or rarely by external users (reviews, for example). Changes less frequently, often highly cacheable. Even more, can often tolerate a degree of temporary inconsistency (showing stale data).

Are there more things that CRUD-heavy companies want to do, especially in the analytical space here? Sure. You may want to adjust results frequently based on user behavior as the user is browsing the site, and other personalization actions. However, that is a hard thing to do real-time and you don’t always have the volume of data you need from the user to actually do that well, so it isn’t generally the first-order concern of the system.
The process for moving off of a monolith in this type of architecture is relatively straightforward:
1. Identify independent entities. This paper by Pat Helland, [“Life Beyond Txns”](http://adrianmarriott.net/logosroot/papers/LifeBeyondTxns.pdf), has some useful and interesting definitions there. It’s better to go a little bit too big early than to go too small and end up having to implement significant distributed transactions. You probably want data-owning services for the major business objects(products, users, etc), and then sets of integration services that implement aggregations and logic over those objects.
2. Pull out the logic into services entity by entity. Try not to change the data model as much as possible in this process. Redirect the monolith to call APIs in the new services as functionality is moved.

That’s basically it. You pull pieces out until you have enough to cover a particular set of user functionality in data and integration terms, then you can start to evolve that part of the user functionality to do new things in the services.
These services are not classic SOA, but nor are they teeny-tiny microservices. The services that own the data may be fairly sophisticated. You may not want to have too many services because you want to be able to satisfy requests from the user without having to make a ton of network hops, and ideally, without needing to do distributed transactions.
You are probably not making new services every day, and especially if you have a sub-50-person engineering team and a long product roadmap, you may not want to invest extensive engineering time into complex orchestration and tooling that enables people to dynamically add new services at the click of a button
*(nb: the products to support this are getting better all the time, and so at some point this will be worth doing even for that smaller team. It is unclear to me whether that time is now or not.)*
.
The equation to apply for determining how much to invest in tooling is pretty straightforward: how much time does it cost devs to have a less automated process for adding a new service, vs how long does it take to implement and maintain the automation for doing it easily, and how many new services do you expect to want to deploy over time? You’re making a guess. Obviously, if you think there is value to enabling people to spin up tiny services fast and frequently, it is better to invest time and tooling into this. As with all engineering process optimization decisions, it’s not a matter of getting it perfectly right, but rather, of deciding for the foreseeable future and periodically re-evaluating.
There are many microservices “must-haves” in this instance that I have found to be anything but. I mentioned extensive orchestration above. Dynamic service discovery is also not needed if you are not automatically spinning up services or moving services around frequently (load balancers are pretty nice for doing this at a basic level).
Allowing teams to choose their ideal language, framework, and data store per service is also certainly not a must-have and in fact it’s likely to be far more of a headache than a boon to your team.
Having independent data stores for the services is also not a must-have, although it does mean that you will have a high-risk SPOF on the shared database. As I was writing this piece I discovered a section of
[some writing on microservices from 2015:](https://dzone.com/articles/adopting-microservices-netflix)

> Create a Separate Data Store for Each Microservice


> Do not use the the same back-end data store across microservices. … Moreover, with a single data store it’s too easy for microservices written by different teams to share database structures, perhaps in the name of reducing duplication of work. You end up with the situation where if one team updates a database structure, other services that also use that structure have to be changed too.

This is true, but for smaller teams you can prevent sharing of database structures by convention (process and code review, and automated testing and checking for such access if it is a huge worry). When you carefully define the data-owner services, it’s less likely this will happen. And the alternative is the next paragraph:

> Breaking apart the data can make data management more complicated, because the separate storage systems can more easily get out sync or become inconsistent, and foreign keys can change unexpectedly. You need to add a tool that performs [master data management](http://en.wikipedia.org/wiki/Master_data_management) (MDM) by operating in the background to find and fix inconsistencies. For example, it might examine every database that stores subscriber IDs, to verify that the same IDs exist in all of them (there aren’t missing or extra IDs in any one database). You can write your own tool or buy one. Many commercial relational database management systems (RDBMSs) do these kinds of checks, but they usually impose too many requirements for coupling, and so don’t scale.([original](https://dzone.com/articles/adopting-microservices-netflix))

This paragraph probably leads to sighs of exhaustion from anyone with experience doing data reconciliation. It’s due to this overhead that I encourage those of you in smaller organizations to at least evaluate a convention-based approach before deciding to use entirely independent and individual data stores. This is a decision you can delay as needed.
T
his version of the microservices architecture is very compelling for the scaled CRUD world because it lets you do a rewrite piece by piece. You can do the whole system, or you can simply take out pieces that are most sensitive to scaling. You proactively engage with many of the bits of distributed systems complexity by thinking carefully about the data and where transactions on that data will be needed. You probably don’t need a ton of fancy data pipelines floating around. You know where the data will be modified.
Do you
*have*
to go to microservices to scale this? Probably not, but that doesn’t mean using microservices to scale such systems is a bad idea. However, going extreme with the microservices model
*may*
be a bad idea, because you really don’t want to slice your data up in a way that ends up in distributed transaction land.

#### Microservices For Data Stream Processing

Now, let’s talk about a very different use case. This use case is not your classic CRUD application, thick with business rules around transactionally-updated objects. Instead, this use case has a large pipeline of data. It has small bits of data flowing into it from many different sources, a very large volume of many bits of data. This large volume of input data sources also has many different services that will consume it, modify it, and pass it along for further processing.
The major concern of this application is ingesting large quantities of ever-changing data, processing it in various ways, and showing a view of it to customers. CRUD concerns are secondary to the larger concerns of keeping up with the data stream and recalculating information based on what is happening on that stream.
Let’s take a metrics-aggregating SaaS application, for example. This application has customers all over the world with various applications, services, and machines that are reporting out metrics to the aggregator. These customers only need to see their data, although the combined total of data for any one customer may be very large. Our aggregator needs to consume these metrics and send them off to the application that is going to show them to the customer. The customer-facing application may be operating on a combination of incoming metrics in real-time plus historical data that comes from cache or a backing storage system. A large part of the value of the data is in the moving-window of what is happening right now/recently.
This architecture from the start has considerations of volume that even our scaled CRUD world may not care about for a very, very long time. Additionally, the data itself is mostly a stream of updates over time. The notion of the “stateful” data that is transactionally updated is minimal, the most useful data is more like a timeseries or log of events. The transactional data, say, stored user views and user configuration, may be more like the “metadata” of our CRUD application in the first example, infrequently changed compared to the updates coming in from the stream. The majority of developer time is most likely spent not in dealing with these transactional changes but rather in managing the streams of inputs, providing new types of inputs, applying new calculations to the stream of inputs, and changing the calculations.
In this example, you can imagine a service that wants to run an experiment by doing a different calculation across a particular element on the stream. Instead of modifying the existing code, the experimental service listens to the data stream at the same point as the existing calculation, provides a new calculation value, and pushes that calculation value back into the data pipeline on a different channel. At some point an experiment service pulls this data out for the customers who are assigned to the experimental treatment and shows the results of that calculation instead of the standard calculation. In all of these places you need a record of what happened in order to do analysis of experiment success and debugging, but that record does not need to be strongly, transactionally related to the record of other events in the system at this time, even across related users.
In this example, it may very well be much more effective to spin up new services as needed, in order to run quick experiments, rather than changing existing services. Especially in cases where the service can do this without needing to worry about coordinating the data consumption or production with any existing service. This is the world of what I would like to call “stream-centric microservices.”
If there is enormous value to your business to manage real-time data streams, and you are going to have a lot of developers consuming those streams by creating new services to listen to them and produce results, then you absolutely must be willing to commit to the investment in tooling to make the process of creating services and putting them into production as easy as possible. You will probably use this for all of your services over time, once you have it, but realize that the clear value is that you have dynamic data that can be processed and manipulated and experimented on independently.

#### Cron Jobs as Microservices

I’d be remiss if I didn’t mention this pattern. When it becomes very easy to make anything a microservice, everything becomes a microservice, including things we would traditionally run as cron jobs.
But cron jobs are a nice concept, and not everything has to be a “service.” You can use CloudWatch Events from AWS for this purpose, or scheduled Lambda functions. Use Gearman, a queue and async job runner, to schedule cron jobs. Remember your cron jobs need to be idempotent (can be run twice on the same input without changing the outcome). If you have an easy way to spin up services and it’s easy to create tiny services that are basically cron jobs, no problem, but cron jobs in and of themselves are not a great reason to create a large, orchestrated services environment.

### Conclusion

I hope that this has been a useful breakout across a few axes of the wild world of microservices. Going through the thought experiment was very useful for me, personally. It helped me understand how what seems obvious to people at one extreme, say those who spend most of their time focused on stream processing, doesn’t make as much sense for people who are more focused on the world of CRUD application scaling.
(This was originally published on
[medium](https://medium.com/@skamille/microservices-real-architectural-patterns-68bd83bbb6cd#.dl7jrbr5k)
)