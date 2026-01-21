---
title: "Infrastructure Vendors Are in a Tough Spot"
subtitle: "Cloud native, AI-enabled, post-ZIRP companies are the new apex predator."
date: 2025-01-13T18:43:12+00:00
url: https://materializedview.io/p/infrastructure-vendors-are-in-a-tough
slug: infrastructure-vendors-are-in-a-tough
word_count: 1321
---


Andy Pavloposted hisyearly database retrospectiveto kick off the new year. Andy covers license changes, the catalog wars, DuckDB, funding, and more. A brief comment in the acquisition section got me thinking:


> Warpstream → ConfluentRewriting Kafka in golang but then making it spill to S3. I'm happy for the Warpstream team, but Confluent could have done this themselves.


As Andy says, WarpStream﹩ is a Kafka re-implementation that uses S3 rather than local disks (aZero Disk Architecture). The tradeoff with this design is that writes take a little bit longer to be durably sent—usually 100ms-500ms. It turns out, a little bit of extra latency is tolerable for many use cases, especially when you factor in cost savings, operational simplicity, and the ease of BYOC support.


Andy’s comment begs the question, if Confluent could build WarpStream, why didn’t they? One could offer many theories: it was cheaper to buy than to build, to eliminate competition, to capitalize on WarpStream’s branding, to acquire talent, or something else.


I believe Confluent didn’t build WarpStream because it wasn’t set up, as an organization, to build such a product. To understand why, let’s first consider what WarpStream did: they built a Kafka-compatible BYOC solution with a handful of engineers in less than 18 months. They were also in the process of rolling outWarpStream SaaSand adding transaction support when they were acquired.


Next, let’s consider what percentage of total Kafka usage in the world would have been satisfied with a 100ms-500ms SaaS or BYOC Kafka offering. My guess is a significant portion; well over 50% of all usage.


This is just my guess, but it sounds right based on my experience. All of our Kafka usage at WePay would have been completely fine with a 250ms-500ms P99 latency. All of our data integration, our ETL, our service-to-service queuing would have worked just fine. And we would have loved to be able to run Kafka as a stateless service in our own cloud onGoogle Cloud Storage.


Another thing to consider is revenue: WarpStream can be run very cheaply. This let WarpStream undercut Confluent on cost. They went hard on this messaging, talking about how S3 allowed them to bypass Amazon Web Service’s (AWS)inter-availability zone costs.


WarpStream was also moving into the platform layer. They launchedOrbitto compete withConfluent Replicator,Managed Data Pipelinesto compete withKafka Connect, and aBYOC schema registryto compete withConfluent Schema Registry.


Let’s pause to let this sink in. WarpStream was in the process of building a cheaper (and arguably better) version of Confluent’s platform with a handful of engineers that could service the majority of Confluent customers’ use cases. That’s a pretty staggering statement.


To compete, Confluent would have to build WarpStream. Indeed, they tried to do this with Confluent Freight. Shortly before the WarpStream acquisition, Confluent announcedConfluent Freightas Kafka re-implementation that writes to S3, ABS, or GCS. It’s nearly identical to WarpStream, but there’sone key difference:


> Freight clusters utilize the latest innovations in Confluent Cloud’s cloud-native engine,Kora, to deliver low cost networking by trading off ultra low latency performance.


Freight is built on top of ConfluentKora. The very first paragraph of Kora’s announcement post says:


> Kora isn’t something you can download, or even something you could run outside our control plane and the rest of our cloud


And there-in lies a very significant difference. Freight can’t be run outside of Confluent’s cloud. WarpStream can. Why would Confluent build Freight without BYOC support? I think the answer is that it was too encumbered by its legacy tech stack, its customers (the innovator’s dilemma), and its organization (Conway’s law).


Apache Kafka was built before cloud native architectures existed. It had to solve its own replication, handle its own leadership election, and manage its own storage. As with all legacy systems, this means it carries baggage with it. Many design decisions would have been made differently if it started from scratch. This is why Confluent has forked Kafka and why WarpStream wrote their implementation from scratch.


Kafka’s original design did, however, come with some flexibility that newer cloud-native designs didn’t have. Namely, it could handle low-latency use cases that systems like WarpStream couldn’t. I’m not making the claim that it’s impossible to build a low-latency cloud-native Kafka (Confluent has done so with Kora). But I’m saying that, even if you did that, it would look different from Kafka.


Regardless, Confluent picked up some large, high-margin customers that depend on some of Kafka’s more exotic features, including its low latency support.


> [The Innovator’s Dilemma] describes how large incumbent companies lose market share by listening to their customers and providing what appears to be the highest-value products, but new companies that serve low-value customers with poorly developed technology can improve that technology incrementally until it is good enough to quickly take market share from established business.


Confluent can’t easily abandon these customers and their use cases. Such customers tend to be big name companies with large contracts (and presumably, higher margins). Confluent needs this revenue; they now have over 3,300 employees on six continents (according toleadIQ). Some of Confluent’s size could be attributed to its maturing duringzero interest rate policy(ZIRP) when money was cheap. Some could also be attributed to its obligation to support such use cases with more complex systems. Regardless, WarpStream was unencumbered by both.


Finally, even if Confluent decided that building Freight with BYOC support was the right thing to do, they still had to deal with entrenched teams in their organization whose raison d'être was in direct conflict with a BYOC Freight solution. If Confluent could service the majority of their users with a product that looked like WarpStream, what happens to the Kora team, the legacy Kafka teams, the entire sales motion, the marketing, and so on? Such a pivot would be seismic. Many teams would need to be eliminated or reorganized.


You need not look far to see what such a change would look like.Elon Musk’s shake up atTwitteris a reflection of very similar headwinds.


![](https://substackcdn.com/image/fetch/$s_!oPpt!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe4e818c4-ae6c-48f2-891c-d8d8cd0e2d5b_1160x376.png)

*View Post*


It’s simply much easier to build very lean, very efficient companies now. When you compound cloud native efficiencies with AI-enabled developers, things get even more pronounced. New companies are adding engineers at a rate that accounts for the AI multiplier that these engineers come with.ChatGPT,Claude,Windsurf,Cursor, and many other AI tools have improved engineering productivity.


Legacy companies built their teams before the AI shift happened. It’s harder and more painful to turn the ship. Salesforce recently announcedit won’t hire engineers in 2025. Meta is looking forward toreplacing mid-level engineers with AI.LinkedIn had layoffs, and is running very lean (from what I hear). New competitors don’t have to deal with the damage that these changes cause. This has left legacy companies in a tight spot.


![](https://substackcdn.com/image/fetch/$s_!7_CN!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6770b645-ef6d-4a97-b215-fd7de1ca2247_1156x594.png)

*View Post*


Given all this, it’s no surprise that Confluent decided to build Freight on top of Kora. WarpStream fits nicely in the product offering as its BYOC option. But as I say in my post above, I worry this strategy is delaying the inevitable.


Kafka, itself, is commoditized.Bufstream,AutoMQ, WarpStream,Redpanda, andS2show this. When these companies move up the platform stack, as WarpStream was doing, as Bufstream is doing with its schema registry, Confluent will be competing with much more efficient organizations.


Much of this post has been about Confluent and WarpStream, but that’s simply the angle I’ve taken. I don’t mean to pick on them. It’s easy to see this pattern across the industry. Many new startups are going after Elastic, for example.Datadog’sQuickwitacquisitionis a strong signal there. Legacy infrastructure companies are going to have a tough time competing with these new cloud native, AI-enabled, post-ZIRP companies.


---


#### Book


Support this newsletter by purchasingThe Missing README: A Guide for the New Software Engineerfor yourself or gifting it to someone.


![](https://substackcdn.com/image/fetch/$s_!CI0B!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fde442631-41a6-4119-a99a-62957cd53edb_870x978.png)


Buy Now


---


#### Disclaimer


I occasionally invest in infrastructure startups. Companies that I’ve invested in are marked with a ﹩ in this newsletter. See myLinkedIn profileandMaterialized View Capitalfor a complete list.
