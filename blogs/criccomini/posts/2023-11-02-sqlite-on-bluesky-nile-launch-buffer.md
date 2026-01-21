---
title: "SQLite on Bluesky, Litestream, Nile Launch, Buffer Pool Refresher, and more..."
subtitle: "Blue Sky's PDS is moving to SQLite, I rabbit hole on mmap and buffer pools, Nile is released, and I highlight Tigris."
date: 2023-11-02T10:00:20+00:00
url: https://materializedview.io/p/sqlite-on-bluesky-nile-launch-buffer
slug: sqlite-on-bluesky-nile-launch-buffer
word_count: 762
---


## SQLite for Bluesky’s PDS Server


Bryan Newboldpostedan interesting updateonBlue Sky’spersonal data server(PDS). A PDS is the thing that hosts your posts and some other stuff (more detailshere). They’re moving from a monolithic PostgreSQL instance to a distributed implementation.Jake Gold(also at Blue Sky) posted some more notes:


![](https://substackcdn.com/image/fetch/$s_!NJLb!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F273a092b-99eb-4c79-be26-1323985e3ee3_528x266.png)


See Jake’spostsfor the logic behind this change. SQLite is showing up more and more in distributed systems. I think this trend will continue. Blue Sky’s yet more evidence.


## Poking at Litestream


TheLitestreamcomment in Jake’s thread, above, caught my eye. I’m on the lookout for more examples of Litestream in the wild.Fly.iois clearly a big one.Ben Johnson, the Litestream author, works there. Their post,Introducing LiteFS, got me thinking.


> LiteFS works by interposing a very thin virtual filesystem between your app and your on-disk database file. It’s not a file system like ext4, but rather a pass-through. Think of it as a file system proxy. What that proxy does is track SQLite databases to spot transactions and then LiteFS copies out those transactions to be shipped to replicas.


I’m hearing more and more good stuff about Fly.io.


Ben Johnson’sWhy I Built Litestreamis also a great read. It made me nostalgic for the good ‘ole days. A quote I feel compelled to pull from the post:


> This works particularly well for SaaS applications where each customer is isolated from one another.


Timely considering Nile’s announcement.


## Nile Launch


Nile[$] launched a new serverless Postgres-compatible DB built for SaaS.


I’m really excited about this, andI’mnotalone. Most people who’ve worked on SaaS immediately get why this database is a big deal. As a concrete example, some of my friends are currently usingRails’s apartment libraryto bolt multi-tenancy on top of their SaaS application. With Nile, all of this moves to the database layer. Pretty slick.


I’ve knownSriram(Ram) andGwenfor a while. Sriram sat a few aisles over from me at LinkedIn when he startedAmbry(which really should get more attention). I first met Gwen when she was at Cloudera.


Sriram pitched Nile to me a few years ago over coffee. At the time,Chrix Finneand I were thinking about metered billing for SaaS payments. Ram had a very similar outlook on the space. Since then, they’ve iterated their way to a serverless SaaS database.


## Buffer Pool Refresher


Simon Eskildsen(ofNapkin MathandTurbopufferfame) shared a link to a really interesting paper and presentation on mmap in databases.


![](https://substackcdn.com/image/fetch/$s_!02Zt!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff4d64949-3bc5-4210-98e7-96ba0477f633_690x409.png)


Thepaper and videolist four problems:

- Transactional safety
- I/O stalls
- Error handling
- Performance issues


A comment on buffer pools in the video sent me down a rabbit hole. If you’re like me, and want to refresh yourmemoryon buffer pools (see what I did there?), starthereor this video:


I also foundMySQL’s InnoDB buffer pool algorithmpage, which describes an actual implementation. It uses LRU eviction, but inserts pages into the middle of the pool in a specific way.


## Project Highlight:Tigris


I’m talking withOvais Tariq(ofTigris) about serverless infrastructure in a few weeks. Ovais is the CEO ofTigris Data, which builds an open source serverless NoSQL DB.


Tigrisis based on Uber’sDocstore.1


> Docstore is a general-purpose multi-model database that provides a strict serializability consistency model on a partition level and can scale horizontally to serve high volume workloads. Features such as Transaction, Materialized View, Associations, and Change Data Capture combined with modeling flexibility and rich query support, significantly improve developer productivity, and reduce the time to market for new applications at Uber.


There’s a lot going on with Tigris, but some here are some highlights:

- Strict serializability
- Built onFoundation DB(I plan to do a paper highlight on Foundation soon.)
- Runs aforkedversion ofTypesensefor search.
- MongoDB-compatible protocol(and gRPC/HTTP)
- It’sopen source! (Apache 2)


Sadly, it seems Tigris is missing change data capture (CDC)—something Docstore had. I’d be happy to be corrected if I’m wrong on this.


## awesome-infra Repo


A friend asked me this week for a list of recent infrastructure projects I’m tracking. I decided to post the list to Twitter, too.


![](https://substackcdn.com/image/fetch/$s_!Z-ki!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa9a47c65-dff3-4046-92a5-7725fe4de80d_688x533.png)


The tweet was a hit so I createdawesome-infra. I’m going to track cool software infrastructure projects there. I could use your help curating the list and getting the categories right. You’re welcome to submit your own projects and startups as long as they satisfy theCONTRIBUTING.mdandPR template.


---


I occasionally invest in infrastructure startups. Companies that I’ve invested in are marked with a [$] in this newsletter. See myLinkedIn profilefor a complete list.

[1](https://materializedview.io/p/sqlite-on-bluesky-nile-launch-buffer#footnote-anchor-1-138463142)

If you really want to pull at this thread, the Docstore post links to previous posts on Uber’sSchemalessdatabase, which precedes Docstore. They also tried Cassandra.
