---
title: "Log-structured storage"
date: 2017-06-11
url: https://jvns.ca/blog/2017/06/11/log-structured-storage/
slug: log-structured-storage
word_count: 1023
---


This morning I’m reading [Designing data-intensive applications](http://dataintensive.net/) by Martin Kleppmann.


I’m only a couple chapters in, but it’s already definitely the best
thing about databases I’ve ever read. It’s doing an amazing job of

- introducing totally new-to-me concepts (like “log-structured storage”)
- explaining what terms like “ACID” mean in a rigorous and clear way
(turns out that the “C” in ACID stands for “consistency”, but has
nothing to do with either linearizability or “eventual consistency”,
it’s actually about maintaining application-level invariants.
It’s really helpful to know that there are actually 5 completely
unrelated uses of the word “consistency” when talking about
databases). He’s also very up front about “this word is used
very inconsistently in practice, be careful!”
- explaining how the concepts in the book relate to real-world databases
like PostgreSQL, MySQL, Redis, Cassandra, and many many more
- giving references (just the first chapter on storage engines has 65
amazing-looking references), if you want to learn more and go deeper


I often find blog posts/papers on databases difficult because there’s so
much terminology+concepts, and this book introduces concepts in a way that I can
relate back to my actual experiences with using databases in practice.
Now I feel more like I can use this to read database documentation and
understand what’s going on!


For example here’s a comic summary of the explanation of ACID he gives
(which I loved, I seriously thought atomicity in databases was the same
idea as atomicity in concurrent programs like an “atomic instruction”
and it’s a TOTALLY DIFFERENT THING).


But! Raving about this book aside (for now), let’s talk about a new idea
I learned this morning from it, log-structured storage!


### log-structured storage: the simplest database


This chapter starts by describing the “world’s simplest database”: these
2 bash functions (save it to a file `db.sh` and run `source db.sh` to
install it!)


```
#!/bin/bash

db_set() {
    echo "$1,$2" >> database
}

db_get() {
    grep "^$1," database | sed -e "s/^$1,//" | tail -n 1
}

```


Basically this appends to a text file (called `database`) every time you
write, and greps that text file for the latest update every time you
read. I tried it! This is a totally functional database :)


### 2 kinds of database storage


There are a lot of ways to segment databases – “SQL vs not-SQL”,
“replicated vs not replicated”, and, er, a lot more. This storage
chapter started by saying that there are 2 basic ways to do database
storage (which I hadn’t heard before!)

- log-structured storage engines (like “log-structured merge trees”)
- page-oriented storage engines (like b-trees)


A log-structured storage engine is a little like our Bash script – you write new
stuff to the end of the log, and then query for the latest update to
read. The idea here is that this way you don’t need to make random disk
writes – you can just write to the end, and so writes can be a lot
faster. Unlike our bash script, you don’t just grep to query (that would
be way too slow!!). One thing you can do (a “SSTable”) is write the new
data to a red-black tree in memory, and then periodically (every few megabytes,
maybe?) write the tree to disk.


When you want to write a page-oriented database, you need to search for
the right page (4k of data or so) that contains your data and update it. I wrote a blog post about [sqlite and  btrees](https://jvns.ca/blog/2014/10/02/how-does-sqlite-work-part-2-btrees/) a while back.


PostgreSQL, MySQL, etcd, and sqlite all use page-oriented storage engines.


I was googling for what MongoDB uses, and it turns out that MongoDB’s
new WiredTiger storage engine actually supports both a log-structured
backend and a btree backend! There’s a [Btree vs LSM](https://github.com/wiredtiger/wiredtiger/wiki/Btree-vs-LSM)
benchmark in the MongoDB wiki, and it shows that in that benchmark, the
BTree table has higher read throughput and lower write throughout, and
the LSM table has higher write throughput and lower read throughput.


Leveldb, Rocksdb, and Cassandra all use log-structured storage.


### the write-ahead log


This chapter also helped me understand what’s going on with write-ahead
logs better! Write-ahead logs are different from log-structured storage,
both kinds of storage engines can use write-ahead logs.


Recently at work the team that maintains Splunk wrote a post called
“Splunk is not a write-ahead log”. I thought this was interesting
because I had never heard the term “write-ahead log” before!


Here’s what I think the deal is now.


Writing to disk is expensive. Because of that, databases will often just
do writes to memory, and then save their state to disk later. This is
smart and efficient!


But if you crash, then you can lose data. Losing data is bad. To avoid
losing data, you can just log all your writes to disk by appending to a
file (just like our “simplest database ever”). Most of the time you
don’t use this log at all (you don’t use it to query!). But if you crash
or something goes wrong, you can go back and use the log to recover. You
can see that [Postgres does this in its doc](https://www.postgresql.org/docs/9.1/static/wal-intro.html).


From the Postgres docs:


> If we follow this procedure, we do not need to flush data pages to
> disk on every transaction commit, because we know that in the event of
> a crash we will be able to recover the database using the log: any
> changes that have not been applied to the data pages can be redone
> from the log records. (This is roll-forward recovery, also known as
> REDO.)


There’s a nice post about how [SQLite uses a WAL](https://sqlite.org/wal.html) on its site.
I think in practice a WAL can actually mean a few different things –
for example SQLite is an embedded database and I think its WAL implementation
doesn’t involve holding data in memory at all, it has different goals.


### more things I’m excited to understand from this book

- raft & consensus algorithms (I’m using etcd now and I don’t really
understand what’s going on with Raft yet)
- how different database systems handle replications
- and partitioning!
- and more
