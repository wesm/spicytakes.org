---
title: "NoSQL and the Enterprise Developer"
date: 2011-11-07
url: https://www.elidedbranches.com/2011/11/nosql-and-enterprise-developer.html
word_count: 787
---

One of the people I follow on twitter,
[@strlen](https://twitter.com/#!/strlen)
, posted a pretty good comment on
[Hacker News](http://news.ycombinator.com/item?id=3204735)
the other day. In it, he calls for NoSQL stores to become better than they currently are (a notion I doubt anyone would disagree with), and mentions some of the things he would like see evolving in the NoSQL landscape:

> * Support for new and interesting distribution models. Allowing users to choose between eventual consistency, quorum protocols, primary copy replication and even transactional replication.


> * Support for large, unstructured blob data[...]


> * Most NoSQL systems support transactions within the scope of a single value (or document) via the use of quorums, serializing through a single master, etc... However, it'd be nice if something like MegaStore's Entity Groups (or Tablet Groups in Microsoft Azure Cloud SQL server) were supported.


> * Secondary indices, whether internal or external (by shipping a changelog) to the system.


> * True multi-datacenter support (local quorums if desired, async replication to the remote site) including across unreliable, high latency WAN links (disclosure: Voldemort supports this -- [https://github.com/voldemort/voldemort/wiki/Multi-datacenter...](https://github.com/voldemort/voldemort/wiki/Multi-datacenter-results) )

These are all great points. In particular for the enterprise space (and especially the financial space), I think the first and last points are extremely interesting.
A major concern for the financials is business continuity. If a data center goes down, you had better be able to keep the critical parts of your business running. This has traditionally been done in a few different ways. One major way is through the use of
[SRDF disk](http://en.wikipedia.org/wiki/SRDF)
, a rather slow and expensive facility that will automatically mirror data from one disk to a backup disk in a different site. For it to be performant at all, the two sites are generally kept pretty close together, with a fat link connecting them. But the overhead of the synchronous write and the cost of the disk are still meaningful, and the ultimate reality of dealing with SRDF failover of a database or file system is that frequently system administrators and DBAs need to get involved and the failover time can be quite slow. It satisfies certain regulatory requirements, and it satisfies the basic needs of business continuity, but rarely in a clean and easy to use fashion.
Now, many NoSQL systems can do some level of data replication across data centers. I personally chose to use Cassandra for a project because of the fact that I could choose write-level coherence that would guarantee writes hitting a quorum of global servers, thus assuring no data loss even in the event of a single data center failure. And hand-in-hand with point number one, this configurable read/write coherence meant that I could have a system that would always be available for reads even if a region was network partitioned from the other global regions, and would always guarantee that a quorum of servers would see a write before committing thus guaranteeing no loss of data.
Here's a tricky point quorum-based system designers should know: Many enterprises don't have data centers set up to support quorum-based systems in a local region. Often you will see 2 data centers per global region, meaning that if you need to run a quorum-based system and withstand the loss of any one data center (a general requirement for high availability business continuity), you need to have data crossing the WAN at some point. To a distributed systems programmer, this is agony. If only I had 3 data centers available in-region the possibilities for quorum-based systems to keep my data safe while still having relatively fast writes becomes so much more! But don't count on that being available to your clients.
A few glimmers of hope are on the horizon. Companies are aware of the cloud, and some are investigating whether they can use external cloud providers to host some computing. If this becomes a possibility, a cloud datacenter could become the third center in a quorum-based system. Regulators are also taking a closer look at data center locality, and wondering if there isn't too much of a concentration risk with two data centers so close together within a geographic region. This may prompt build out of additional data centers farther away in the states, but with better network connections than a cross-Atlantic link.
NoSQL folks looking for the enterprise and financial services markets, take heed. There's desire out there for what you are selling, but if it isn't easy to meet business continuity and regulatory requirements, you will never gain more than a niche position at these firms.
There's one other todo in the NoSQL space around authentication, but I will take the advice of my post reviewers and save that for a later rant.