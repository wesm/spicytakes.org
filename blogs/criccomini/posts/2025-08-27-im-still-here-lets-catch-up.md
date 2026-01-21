---
title: "I'm Still Here! Let's Catch Up."
subtitle: "The latest on Designing Data-Intensive Applications, SlateDB, AI, Materialized View Capital, and forthcoming newsletter posts."
date: 2025-08-27T18:26:22+00:00
url: https://materializedview.io/p/im-still-here-lets-catch-up
slug: im-still-here-lets-catch-up
word_count: 596
---


My apologies for the lack of posts recently. I’ve been hard at work on a few things over the summer, which has left little time for this newsletter. I’m getting my bearings now. More posts are back on the docket. My first post—this one—will be a quick catch-up.


Martinand I have been working onDesigning Data-Intensive Applications’s batch and streaming chapters for its second edition. The batch chapter has been published to Safari Online as an early release; it required a full rewrite. The streaming chapter is still a work-in-progress.Kafka: The End of the Beginning, my previous post on this newsletter, reflected on how stagnant the streaming ecosystem has been over the past 10-15 years. The updates to the streaming chapter reflect this; they’ll be more minimal. I do plan to add a section onincremental view maintenance (IVM), which I’ll base off of my IVM newsletter post.

[Everything You Need to Know About Incremental View Maintenance](https://materializedview.io/p/everything-to-know-incremental-view-maintenance)
[Chris](https://substack.com/profile/69592459-chris)
·
April 18, 2025

Incremental view maintenance has been a hot topic lately. Materialize has been around for a while, but newcomers like PostgreSQL’s (semi-working) pg_ivm extension, Feldera, Epsio, Bytewax, and many others are starting to make noise. In the data warehousing space,

[Read full story](https://materializedview.io/p/everything-to-know-incremental-view-maintenance)

Meanwhile,SlateDBwork continues apace.Li Yazhouhasaddedserializable snapshot isolation (SSI)support. He’s in the process ofadding transactions. The RFC ishereif you’d like to learn more. We also have bothPythonandGobindings now. I have been focusing on refactoring and stability; I added a basicdeterministic simulation testerrecently.Sujeet Sawalaisworking on an RFCto persist compaction progress. We’re starting to see somereal adoption. More projects are launching in the near future, too.


The biggest news with SlateDB, though, isPierre Barre’sZeroFSproject. ZeroFS providesnetwork filesystem (NFS),network block device (NBD), andPlan 9 Filesystem Protocol (9P)implementations on top of SlateDB. The filesystem is alsoPOSIX compliant—no small feat. On the performance front, check out Pierre’sAWS EFS,AWS Mountpoint-S3,JuiceFS, andAzure Filesbenchmarks.


ZeroFS is a young project, but I’m very excited about it. SlateDB’sbranching and forkingfeatures mean ZeroFS will be able to provide zero-copy filesystem forking—an important feature for AI and many other use cases.


Speaking of AI, I’m still getting my bearings with it. I’ve been reluctant to post about the topic because I don’t feel I’m an expert in the subject. (Then again, it’s so new that very few are.) I use coding agents constantly, though. As a user, I’ve begun to form some opinions aroundmodel context protocol (MCP), agent adoption in the enterprise, and its impact on developer tooling and infrastructure. I plan to write more on AI in the near future.


I’ve continued to invest in startups throughout the summer.Materialized View Capitalis now 75% deployed and will be fully deployed ~18 months from its inception. One usually targets a 3 year deployment. An 18 month deployment for a smaller fund like MVC is not unheard of. I’m quite pleased with our portfolio, which includesBauplan,Dosu,Fiveonefour,Gauge,Loophole Labs,ParadeDB,Reboot,Signadot,Spiral,Tigris,Tensorlake, andmany more.


Starting a fund has been rewarding. I plan to take a few months off after the fund is deployed. I’d like to evaluate what’s next for my startup investing adventure.


And that pretty much sums it up! I’m sure I’ve missed a few things. Let me know if there’s something specific that’s worth noting. In the meantime, expect an interview next week withXorq’s﹩ CEO,Hussain Sultan.


---


#### Book


Support this newsletter by purchasingThe Missing README: A Guide for the New Software Engineerfor yourself or gifting it to someone.


![](https://substackcdn.com/image/fetch/$s_!CI0B!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fde442631-41a6-4119-a99a-62957cd53edb_870x978.png)


Buy Now


---


#### Disclaimer


I occasionally invest in infrastructure startups. Companies that I’ve invested in are marked with a ﹩ in this newsletter. See myLinkedIn profileandMaterialized View Capitalfor a complete list.
