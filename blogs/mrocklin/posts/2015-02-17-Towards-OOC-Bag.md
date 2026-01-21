---
title: "Towards Out-of-core ND-Arrays -- Dask + Toolz = Bag"
date: 2015-02-17
url: https://mrocklin.github.io/blog/work/2015/02/17/Towards-OOC-Bag
slug: Towards-OOC-Bag
word_count: 1117
---

*This work is supported by [Continuum Analytics](http://continuum.io)
and the [XDATA Program](http://www.darpa.mil/program/XDATA)
as part of the [Blaze Project](http://blaze.pydata.org)*

**tl;dr**  We use dask to build a parallel Python list.

## Introduction

This is the seventh in a sequence of posts constructing an out-of-core nd-array
using NumPy, and dask.  You can view these posts here:

1. [Simple task scheduling](http://matthewrocklin.com/blog/work/2014/12/27/Towards-OOC/) ,
2. [Frontend usability](http://matthewrocklin.com/blog/work/2014/12/30/Towards-OOC-Frontend/)
3. [A multi-threaded scheduler](http://matthewrocklin.com/blog/work/2015/01/06/Towards-OOC-Scheduling/)
4. [Matrix Multiply Benchmark](http://matthewrocklin.com/blog/work/2015/01/14/Towards-OOC-MatMul/)
5. [Spilling to disk](http://matthewrocklin.com/blog/work/2015/01/16/Towards-OOC-SpillToDisk/)
6. [Slicing and Stacking](http://matthewrocklin.com/blog/work/2015/02/13/Towards-OOC-Slicing-and-Stacking/)

Today we take a break from ND-Arrays and show how task scheduling can attack
other collections like the simple  `list`  of Python objects.

## Unstructured Data

Often before we have an  `ndarray`  or a  `table/DataFrame`  we have unstructured
data like log files.  In this case tuned subsets of the language (e.g.
 `numpy` / `pandas` ) aren’t sufficient, we need the full Python language.

My usual approach to the inconveniently large dump of log files is to use
Python  [streaming
iterators](http://toolz.readthedocs.org/en/latest/streaming-analytics.html) 
along with  [multiprocessing or IPython
Parallel](http://toolz.readthedocs.org/en/latest/parallelism.html)  on a single
large machine.  I often write/speak about this workflow when discussing
 [`toolz`](http://toolz.readthedocs.org/) .

This workflow grows complex for most users when you introduce many processes.
To resolve this we build our normal tricks into a new  `dask.Bag`  collection.

## Bag

In the same way that  `dask.array`  mimics NumPy operations (e.g. matrix
multiply, slicing),  `dask.bag`  mimics functional operations like  `map` ,
 `filter` ,  `reduce`  found in the standard library as well as many of the
streaming functions found in  `toolz` .

* Dask array = NumPy + threads
* Dask bag = Python/Toolz + processes

## Example

Here’s the obligatory wordcount example

We use all of our cores and stream through memory on each core.  We use
 `multiprocessing`  but could get fancier with some work.

## Related Work

There are a lot of much larger much more powerful systems that have a similar
API, notably  [Spark](http://spark.apache.org/)  and
 [DPark](https://github.com/douban/dpark) .  If you have  *Big Data*  and need to
use very many machines then you should stop reading this and go install them.

I mostly made dask.bag because

1. It was very easy given the work already done on dask.array
2. I often only need multiprocessing + a heavy machine
3. I wanted something trivially pip installable that didn’t use the JVM

But again, if you have  *Big Data* , then this isn’t for you.

## Design

As before, a  `Bag`  is just a dict holding tasks, along with a little meta data.

In this way we break up one collection

```
[0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4]
```

into three independent pieces

```
[0, 1, 2, 3, 4]
[0, 1, 2, 3, 4]
[0, 1, 2, 3, 4]
```

When we abstractly operate on the large collection…

… we generate new tasks to operate on each of the components.

And when we ask for concrete results (the call to  `list` ) we spin up a
scheduler to execute the resulting dependency graph of tasks.

More complex operations yield more complex dasks.  Beware, dask code is pretty
Lispy.  Fortunately these dasks are internal; users don’t interact with them.

The current interface for  `Bag`  has the following operations:

```
all             frequencies         min
any             join                product
count           map                 std
filter          map_partitions      sum
fold            max                 topk
foldby          mean                var
```

Manipulations of bags create task dependency graphs.  We eventually execute
these graphs in parallel.

## Execution

We repurpose the threaded scheduler we used for arrays to support
 `multiprocessing`  to provide parallelism even on pure Python code.  We’re
careful to avoid unnecessary data transfer.  None of the operations listed above
requires significant communication.  Notably we don’t have any concept of
 *shuffling*  or scatter/gather.

We  [use dill](http://trac.mystic.cacr.caltech.edu/project/pathos/wiki/dill)  to
take care to serialize functions properly and collect/report errors, two issues
that  [plague naive use of
`multiprocessing`](http://matthewrocklin.com/blog/work/2013/12/05/Parallelism-and-Serialization/)  in Python.

These tricks remove need for user expertise.

## Productive Sweet Spot

I think that there is a productive sweet spot in the following configuration

1. Pure Python functions
2. Streaming/lazy data
3. Multiprocessing
4. A single large machine or a few machines in an informal cluster

This setup is common and it’s capable of handling terabyte scale workflows.
In my brief experience people rarely take this route.  They use single-threaded
in-memory Python until it breaks, and then seek out  *Big Data Infrastructure* 
like Hadoop/Spark at relatively high productivity overhead.

*Your workstation can scale bigger than you think.*

## Example

Here is about a gigabyte of
 [network flow data](http://ita.ee.lbl.gov/html/contrib/UCB.home-IP-HTTP.html) ,
recording which computers made connections to which other computers on the
UC-Berkeley campus in 1996.

```
846890339:661920 846890339:755475 846890340:197141 168.237.7.10:1163 83.153.38.208:80 2 8 4294967295 4294967295 846615753 176 2462 39 GET 21068906053917068819..html HTTP/1.0

846890340:989181 846890341:2147 846890341:2268 13.35.251.117:1269 207.83.232.163:80 10 0 842099997 4294967295 4294967295 64 1 38 GET 20271810743860818265..gif HTTP/1.0

846890341:80714 846890341:90331 846890341:90451 13.35.251.117:1270 207.83.232.163:80 10 0 842099995 4294967295 4294967295 64 1 38 GET 38127854093537985420..gif HTTP/1.0
```

This is actually relatively clean.  Many of the fields are space delimited (not
all) and I’ve already compiled and run the decade old C-code needed to
decompress it from its original format.

Lets use Bag and regular expressions to parse this.

This returns instantly.  We only compute results when necessary.  We trigger
computation by calling  `list` .

Because bag operates lazily this small result also returns immediately.

To demonstrate depth we find the ten client/server pairs with the most
connections.

## Comparison with Spark

First, it is silly and unfair to compare with PySpark running locally.  PySpark
offers much more in a distributed context.

So, given a compute-bound mostly embarrassingly parallel task (regexes are
comparatively expensive) on a single machine they are comparable.

Reasons you would want to use Spark

* You want to use many machines and interact with HDFS
* Shuffling operations

Reasons you would want to use dask.bag

* Trivial installation
* No mucking about with JVM heap sizes or config files
* Nice error reporting.  Spark error reporting includes the typical giant
Java Stack trace that comes with any JVM solution.
* Easier/simpler for Python programmers to hack on.
The implementation is 350 lines including comments.

Again, this is really just a toy experiment to show that the dask model isn’t
just about arrays.  I absolutely do not want to throw Dask in the ring with
Spark.

## Conclusion

However I do want to stress the importance of single-machine parallelism.
Dask.bag targets this application well and leverages common hardware in a
simple way that is both natural and accessible to most Python programmers.

A skilled developer could extend this to work in a distributed memory context.
The logic to create the task dependency graphs is separate from the scheduler.

Special thanks to  [Erik Welch](http://github.com/eriknw)  for finely crafting
the dask optimization passes that keep the data flowly smoothly.
