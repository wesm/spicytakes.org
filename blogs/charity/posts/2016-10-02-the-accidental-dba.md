---
title: "The Accidental DBA"
date: 2016-10-02
url: https://charity.wtf/2016/10/02/the-accidental-dba/
word_count: 1260
---


This morning there was yet another [comment thread on hacker news](https://news.ycombinator.com/item?id=12617853#12620353) about Yet Another outage involving MongoDB and data loss, this time by some company called “CleverTap”.


### Recap


To summarize: the CleverTap engineering team noticed that the WiredTiger storage engine was faster than MMAPv1 for MongoDB.  They decided to … “upgrade the following weekend” (that sentence alone made my eyes bulge).


[According to the blog post](https://blog.clevertap.com/sleepless-nights-with-mongodb-wiredtiger-and-our-return-to-mmapv1/), they upgraded from 2.6 to 3.0, while simultaneously changing storage engines from MMAPv1 to WiredTiger, while leaving zero secondaries snapshot nodes with data on MMAPv1.  All over the course of 3 days.


(They are also running sharded mongo, with a mere 300 ops/sec on each primary, which **RAISES A LOT OF QUESTIONS** but I already feel like I’m beating up on these kids so I won’t pursue that.)


### Questions …


(But seriously what the *hell* can you be doing to have such a low request rate, that you

need to shard at an infinitesimal volume?  Why did you specify it in req/min instead of req/sec?  What is the breakdown of reads/writes?  What is the lock percentage?  What is the avg object size??  Are these like multi-MB documents????  Why did you *pause all incoming traffic* and process it after the upgrade?  If the primary can’t take the extra load, why not rs.syncFrom() a secondary?   If that doesn’t work, don’t you have other, bigger problems??)


Most bafflingly of all: why wait only a** few minutes** after electing a new WiredTiger primary for the **first time ever**, and then immediately **DELETE your only known-good copies of the data on MMAPv1** and re-sync over them with WiredTiger?


### Accidental DBAs


Okay.  So here’s the thing: you are clearly a team of accidental DBAs.  You are operations and software engineers who have found yourselves in charge of the data.


It’s cool.  I am too!  It’s a really neat and fun place to be in.  DBAs and network admins are kind of the last remaining priesthoods in our industry.


There’s a lot of powerful and fun stuff to be done for generalists who pick up specialty knowledge in one of those areas, or specialists (like my neteng friend [Leslie](http://twitter.com/lesliegeek)) who start bringing their skills back to the generalist side and merging the two.


### (Oh Right, We Wrote A Book About This!!!)


My friend [Laine](http://twitter.com/lainevcampbell) and I are writing a book for people on the data side, called “[Database Reliability Engineering](http://shop.oreilly.com/product/0636920039761.do)“, which is aimed at generalist engineers who want to learn how to deal with data responsibly and effectively.


(Actually that’s a good point, I am supposed to be pitching this book! — which is really mostly Laine with a smidgen of me but it’s going to be super awesome.  Consider this your sales pitch.)


So first, as an accidental DBA, you should obviously buy this book  :).  Second: **stateful services require a different mindset[*].  **It’s cool that you are running your own databases!  But reading post mortems like this where the conclusion is “MongoDB sucks” makes me fucking grind my teeth.


### Stop treating your databases like stateless services.


There are lots of ways that MongoDB (and every other database on the planet) really sucks.  Mongo set themselves up for special rage by overpromising too much early on, and seeming tone deaf to criticism from real database engineers.


But *I* can criticize Mongo all day long.  You children on hacker news who have never run it don’t get to. 😛  If you don’t know what the fuck you’re talking about, if you’re cargo culting other people’s years-old complaints, just shut up already.


Managing stateful services like databases means that **you need to be more paranoid** than you did with stateless services.  With stateless services the best practices are to to roll early, roll fast, roll often, roll back.  When you’re dealing with state, you need to be *careful*.


With stateful services you can’t play it fast and loose like that.  You’re going to have data loss, corruption, unpredictable results, catastrophic failures that you can’t simply roll back from.  Data loss can be ruinous to your company.  (This can also be true for stateless services that sit close to your data and mutate it a lot.)


But that’s what makes it fun.  🙂


### Be paranoid.


When we were moving from MMAPv1 to RocksDB at Parse, we ran hybrid replica sets for 6-9 months.  We were paranoid.  It was justified!  We spent half a year capturing production workloads and replaying them, electing Rocks primaries and rolling back, and even then keeping snapshots and secondaries of both storage engines for *months*.


This isn’t because MongoDB sucks.  It’s the nature of the game, it’s the difference between stateful and stateless services.


Do you know that there was a total query engine rewrite in 2.6?  We spent months flushing out tons of crazy bugs.  Do you know about the index intersection changes?  We helped chase down bugs in those too.  (You’re welcome.)


You can’t just go “dudes it’s faster” and jump off a cliff.  This shit is basic.  [Test real production workloads](https://github.com/ParsePlatform/flashback). Have a rollback plan.  (Not for *10 days* … try a month or two.)


### Lessons


If CleverTap had run their plan past anyone experienced with data, they would have called out all of those *completely predictable* failures, and advised them to change it:

1. Make one change at a time.  Do a major version upgrade *separately* from the storage engine upgrade.
2. Delay between each change.  Two weeks is absolutely minimal, any thing less is careless.  Let them bake.
3. Storage engine changes are scary.  It takes years to gain confidence in a new way of laying bits down on disk.  (Whenever people bitch and moan about mongo, I remind them that I’ve still lost WAY more data to MyISAM, InnoDB, and MySQL overall than Mongo.
4. You can run lots and lots of replicas (up to 7 votes per replica set, even more nodes) per each replica set in Mongo.  This is a killer feature.  Why didn’t you use it?
5. Keep backups around for months in the new storage engine *and* the old storage engine, just in case.  Have two hidden snapshot nodes.  The only cost is in dollars, which is fucking cheap compared to data or engineering time.


If you are a new accidental DBA, you have to make a point of learning things.  Go to conferences.  Read books.  Buy bottles of whiskey for your data friends and pick their brains.  Remember that they know things you do not.  Don’t blame the vendors when you fucked up.


Network engineering is the same way, but mistakes tend to be a lot less … permanent.  You drop some packets..  like grains of sand. ^_^


Remember that you’re in charge of keeping people’s data safe and secure.  You have much to learn.  Learn it.


### And get off my fucking lawn.  <3


Some slides from a couple of relevant talks I’ve given on the subject:

- [Maslow’s Hierarchy of Needs for Databases](https://speakerdeck.com/charity/maslows-hierarchy-of-database-needs): how to database as a startup
- [Upgrading Databases](https://speakerdeck.com/charity/upgrading-databases-without-losing-your-data-your-perf-or-your-mind): without losing your data, your perf or your mind


***[*] P.S.:**  “**Stop treating your stateful services like stateless services**” … this is a fact, but it’s not the aspiration.  DB folks should all be leaning in to the model of learning to **treat our stateful services like stateless services**, with the same casual disregard for individual nodes.  This is hard, and it’s going to take some time, but it’s clearly where the world is heading and it’s definitely a good thing.  🙂  The learning goes both ways!*
