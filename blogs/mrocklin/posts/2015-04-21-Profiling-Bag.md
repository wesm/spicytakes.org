---
title: "Profiling Data Throughput"
date: 2015-04-21
url: https://mrocklin.github.io/blog/work/2015/04/21/Profiling-Bag
slug: Profiling-Bag
word_count: 1621
---

*This work is supported by [Continuum Analytics](http://continuum.io)
and the [XDATA Program](http://www.darpa.mil/program/XDATA)
as part of the [Blaze Project](http://blaze.pydata.org)*

*Disclaimer: This post is on experimental/buggy code.*

**tl;dr**  We measure the costs of processing semi-structured data like JSON
blobs.

## Semi-structured Data

Semi-structured data is ubiquitous and computationally painful.  Consider
the following JSON blobs:

```
{'name': 'Alice',   'payments': [1, 2, 3]}
{'name': 'Bob',     'payments': [4, 5]}
{'name': 'Charlie', 'payments': None}
```

This data doesn’t fit nicely into NumPy or Pandas and so we fall back to
dynamic pure-Python data structures like dicts and lists.  Python’s core data
structures are surprisingly good, about as good as compiled languages like
Java, but dynamic data structures present some challenges for efficient
parallel computation.

## Volume

Semi-structured data is often at the beginning of our data pipeline and so
often has the greatest size.  We may start with 100GB of raw data, reduce to
10GB to load into a database, and finally aggregate down to 1GB for analysis,
machine learning, etc., 1kB of which becomes a plot or table.

Common solutions for large semi-structured data include Python iterators,
multiprocessing, Hadoop, and Spark as well as proper databases like MongoDB and
ElasticSearch.   [Two months
ago](http://matthewrocklin.com/blog/work/2015/02/17/Towards-OOC-Bag/)  we built
 `dask.bag` , a toy dask experiment for semi-structured data.  Today we’ll
strengthen the  `dask.bag`  project and look more deeply at performance in this
space.

We measure performance with data bandwidth, usually in megabytes per
second (MB/s).  We’ll build intuition for why dealing with this data is costly.

## Dataset

As a test dataset we play with a dump of GitHub data from
 [https://www.githubarchive.org/](https://www.githubarchive.org/) .  This data
records every public github event (commit, comment, pull request, etc.) in the
form of a JSON blob.  This data is representative fairly representative of a
broader class of problems.  Often people want to do fairly simple analytics,
like find the top ten committers to a particular repository, or clean the
data before they load it into a database.

We’ll play around with this data using  `dask.bag` .  This is both to get a feel
for what is expensive and to provide a cohesive set of examples.  In truth we
won’t do any real analytics on the github dataset, we’ll find that the
expensive parts come well before analytic computation.

Items in our data look like this:

## Disk I/O and Decompression – 100-500 MB/s

A modern laptop hard drive can theoretically read data from disk to memory at
800 MB/s.  So we could burn through a 10GB dataset in fifteen seconds on our
laptop.  Workstations with RAID arrays can do a couple GB/s.  In practice I
get around 500 MB/s on my personal laptop.

To reduce storage and transfer costs we often compress data.  This requires CPU
effort whenever we want to operate on the stored values.  This can limit
data bandwidth.

So we lose some data bandwidth through compression.  Where we could previously
process 500 MB/s we’re now down to only 100 MB/s.  If we count bytes in terms
of the amount stored on disk then we’re only hitting 18 MB/s.  We’ll get around
this with multiprocessing.

## Decompression and Parallel processing – 500 MB/s

Fortunately we often have more cores than we know what to do with.
Parallelizing reads can hide much of the decompression cost.

Dask.bag infers that we need to use gzip from the filename.  Dask.bag currently
uses  `multiprocessing`  to distribute work, allowing us to reclaim our 500 MB/s
throughput on compressed data.  We also could have done this with
multiprocessing, straight Python, and a little elbow-grease.

## Deserialization – 30 MB/s

Once we decompress our data we still need to turn bytes into meaningful data
structures (dicts, lists, etc..)  Our GitHub data comes to us as JSON.  This
JSON contains various encodings and bad characters so, just for today, we’re
going to punt on bad lines.  Converting JSON text to Python objects
explodes out in memory a bit, so we’ll consider a smaller subset for this part,
a single day.

So in terms of actual bytes of JSON we can only convert about 30MB per second.
If we count in terms of the compressed data we store on disk then this looks
more bleak at only 6 MB/s.

### This can be improved by using faster libraries – 50 MB/s

The  [ultrajson](https://github.com/esnme/ultrajson)  library,  `ujson` , is pretty
slick and can improve our performance a bit.  This is what Pandas uses under
the hood.

### Or through Parallelism  – 150 MB/s

This can also be accelerated through parallelism, just like decompression.
It’s a bit cumbersome to show parallel deserializaiton in isolation.
Instead we’ll show all of them together.  This will under-estimate
performance but is much easier to code up.

## Mapping and Grouping - 2000 MB/s

Once we have data in memory, Pure Python is relatively fast.  Cytoolz moreso.

So slicing and logic are essentially free.  The cost of compression and
deserialization dominates actual computation time.  Don’t bother optimizing
fast per-record code, especially if CyToolz has already done so for you.  Of
course, you might be doing something expensive per record.  If so then most of
this post isn’t relevant for you.

## Shuffling - 5-50 MB/s

For complex logic, like full groupbys and joins, we need to communicate large
amounts of data between workers.  This communication forces us to go through
another full serialization/write/deserialization/read cycle.  This hurts.  And
so, the single most important message from this post:

**Avoid communication-heavy operations on semi-structured data.  Structure your
data and load into a database instead.**

That being said, people will inevitably ignore this advice so we need to have a
not-terrible fallback.

This groupby operation goes through the following steps:

1. Read from disk
2. Decompress GZip
3. Deserialize with  `ujson`
4. Do in-memory groupbys on chunks of the data
5. Reserialize with  `msgpack`  (a bit faster)
6. Append group parts to disk
7. Read in new full groups from disk
8. Deserialize  `msgpack`  back to Python objects
9. Apply length function per group

Some of these steps have great data bandwidths, some less-so.
When we compound many steps together our bandwidth suffers.
We get about 25 MB/s total.  This is about what pyspark gets (although today
 `pyspark`  can parallelize across multiple machines while  `dask.bag`  can not.)

Disclaimer, the numbers above are for  `dask.bag`  and could very easily be
due to implementation flaws, rather than due to inherent challenges.

I would be interested in hearing from people who use full groupby on BigData.
I’m quite curious to hear how this is used in practice and how it performs.

## Creative Groupbys - 250 MB/s

Don’t use groupby.  You can often work around it with cleverness.  Our example
above can be handled with streaming grouping reductions (see  [toolz
docs.](http://toolz.readthedocs.org/en/latest/streaming-analytics.html#split-apply-combine-with-groupby-and-reduceby) )
This requires more thinking from the programmer but avoids the costly shuffle
process.

We can also spell this with PySpark which performs about the same.

## Use a Database

By the time you’re grouping or joining datasets you probably have structured
data that could fit into a dataframe or database.  You should transition from
dynamic data structures (dicts/lists) to dataframes or databases as early as
possible.  DataFrames and databases compactly represent data in formats that
don’t require serialization; this improves performance.  Databases are also
very clever about reducing communication.

Tools like  `pyspark` ,  `toolz` , and  `dask.bag`  are great for initial cleanings
of semi-structured data into a structured format but they’re relatively
inefficient at complex analytics.  For inconveniently large data you should
consider a database as soon as possible.  That could be some big-data-solution
or often just Postgres.

## Better data structures for semi-structured data?

Dynamic data structures (dicts, lists) are overkill for semi-structured data.
We don’t need or use their full power but we inherit all of their limitations
(e.g.  serialization costs.)  Could we build something NumPy/Pandas-like that
could handle the blob-of-JSON use-case?  Probably.

DyND is one such project.  DyND is a C++ project with Python bindings written
by Mark Wiebe and Irwin Zaid and historically funded largely by Continuum and
XData under the same banner as Blaze/Dask.  It could probably handle the
semi-structured data problem case if given a bit of love.  It handles variable
length arrays, text data, and missing values all with numpy-like semantics:

Sadly DyND has functionality gaps which limit usability.

I would like to see DyND mature to the point where it could robustly handle
semi-structured data.  I think that this would be a big win for productivity
that would make projects like  `dask.bag`  and  `pyspark`  obsolete for a large
class of use-cases.  If you know Python, C++, and would like to help DyND grow
I’m sure that Mark and Irwin would love the help

* [DyND Mailing list](https://groups.google.com/forum/#!forum/libdynd-dev)
* [DyND GitHub repository](https://github.com/libdynd/dynd-python)

## Comparison with PySpark

Dask.bag pros:

1. Doesn’t engage the JVM, no heap errors or fiddly flags to set
2. Conda/pip installable.  You could have it in less than twenty seconds from now.
3. Slightly faster in-memory implementations thanks to  `cytoolz` ; this isn’t
important though
4. Good handling of lazy results per-partition
5. Faster / lighter weight start-up times
6. (Subjective) I find the API marginally cleaner

PySpark pros:

1. Supports distributed computation (this is obviously huge)
2. More mature, more filled out API
3. HDFS integration

Dask.bag reinvents a wheel; why bother?

1. Given the machinery inherited from  `dask.array`  and  `toolz` ,  `dask.bag`  is
very cheap to build and maintain.  It’s around 500 significant lines of code.
2. PySpark throws Python processes inside a JVM ecosystem which can cause some
confusion among users and a performance hit.  A task scheduling
system in the native code ecosystem would be valuable.
3. Comparison and competition is healthy
4. I’ve been asked to make a distributed array.  I suspect that distributed
bag is a good first step.
