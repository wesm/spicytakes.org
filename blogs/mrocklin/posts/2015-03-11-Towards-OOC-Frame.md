---
title: "Towards Out-of-core DataFrames"
date: 2015-03-11
url: https://mrocklin.github.io/blog/work/2015/03/11/Towards-OOC-Frame
slug: Towards-OOC-Frame
word_count: 1275
---

*This work is supported by [Continuum Analytics](http://continuum.io)
and the [XDATA Program](http://www.darpa.mil/program/XDATA)
as part of the [Blaze Project](http://blaze.pydata.org)*

*This post primarily targets developers.  It is on experimental code that is
not ready for users.*

**tl;dr**  Can we build  `dask.frame` ?  One approach involves indexes and a lot
of shuffling.

## Dask arrays work

Over the last two months we’ve watched the creation of
 [`dask`](http://dask.pydata.org) , a task scheduling specification, and
 [`dask.array`](http://dask.pydata.org/en/latest/array.html)  a project to
implement the out-of-core nd-arrays using blocked algorithms.
(blogposts:
 [1](http://matthewrocklin.com/blog/work/2014/12/27/Towards-OOC/) ,
 [2](http://matthewrocklin.com/blog/work/2014/12/30/Towards-OOC-Frontend/) ,
 [3](http://matthewrocklin.com/blog/work/2015/01/06/Towards-OOC-Scheduling/) ,
 [4](http://matthewrocklin.com/blog/work/2015/01/14/Towards-OOC-MatMul/) ,
 [5](http://matthewrocklin.com/blog/work/2015/01/16/Towards-OOC-SpillToDisk/) ,
 [6](http://matthewrocklin.com/blog/work/2015/02/13/Towards-OOC-Slicing-and-Stacking/) ).
This worked pretty well.  Dask.array is available on the main conda channel and on PyPI
and, for the most part, is a pleasant drop-in replacement for a subset of NumPy
operations.  I’m really happy with it.

```
conda install dask
or
pip install dask
```

There is still work to do, in particular I’d like to interact with people who
have real-world problems, but for the most part  `dask.array`  feels ready.

## On to dask frames

Can we do for Pandas what we’ve just done for NumPy?

Question:  *Can we represent a large DataFrame as a sequence of in-memory DataFrames and
perform most Pandas operations using task scheduling?*

Answer:  *I don’t know.  Lets try.*

## Naive Approach

If represent a dask.array as an N-d grid of NumPy ndarrays, then maybe we should
represent a dask.frame as a 1-d grid of Pandas DataFrames; they’re kind of like arrays.

This approach supports the following operations:

* Elementwise operations    `df.a + df.b`
* Row-wise filtering    `df[df.a > 0]`
* Reductions  `df.a.mean()`
* Some split-apply-combine operations that combine with a standard reduction
like  `df.groupby('a').b.mean()` .  Essentially anything you can do with
 `df.groupby(...).agg(...)`

The reductions and split-apply-combine operations require some cleverness.
This is how Blaze works now and how it does the does out-of-core operations in
these notebooks:
 [Blaze and CSVs](http://nbviewer.ipython.org/github/ContinuumIO/blaze/blob/gh-pages/notebooks/timings-csv.ipynb) ,
 [Blaze and Binary Storage](http://nbviewer.ipython.org/github/ContinuumIO/blaze/blob/gh-pages/notebooks/timings-bcolz.ipynb) .

However this approach does not support the following operations:

* Joins
* Split-apply-combine with more complex  `transform`  or  `apply`  combine steps
* Sliding window or resampling operations
* Anything involving multiple datasets

## Partition on the Index values

Instead of partitioning based on the size of blocks we instead partition on
value ranges of the index.

This opens up a few more operations

* Joins are possible when both tables share the same index.  Because we have
information about index values we we know which blocks from one side need to
communicate to which blocks from the other.
* Split-apply-combine with transform/apply steps are possible when the grouper
is the index.  In this case we’re guaranteed that each group is in the same
block.  This opens up general  `df.gropuby(...).apply(...)`
* Rolling or resampling operations are easy on the index if we share a small
amount of information between blocks as we do in  `dask.array`  for  [ghosting
operations](http://dask.pydata.org/en/latest/ghost.html) .

We note the following theme:

*Complex operations are easy if the logic aligns with the index*

And so a recipe for many complex operations becomes:

1. Re-index your data along the proper column
2. Perform easy computation

## Re-indexing out-of-core data

To be explicit imagine we have a large time-series of transactions indexed by
time and partitioned by day.  The data for every day is in a separate DataFrame.

```
Block 1
-------
                     credit    name
time
2014-01-01 00:00:00     100     Bob
2014-01-01 01:00:00     200   Edith
2014-01-01 02:00:00    -300   Alice
2014-01-01 03:00:00     400     Bob
2014-01-01 04:00:00    -500  Dennis
...

Block 2
-------
                     credit    name
time
2014-01-02 00:00:00     300    Andy
2014-01-02 01:00:00     200   Edith
...
```

We want to reindex this data and shuffle all of the entries so that now we
partiion on the name of the person.  Perhaps all of the A’s are in one block
while all of the B’s are in another.

```
Block 1
-------
                       time  credit
name
Alice   2014-04-30 00:00:00     400
Alice   2014-01-01 00:00:00     100
Andy    2014-11-12 00:00:00    -200
Andy    2014-01-18 00:00:00     400
Andy    2014-02-01 00:00:00    -800
...

Block 2
-------
                       time  credit
name
Bob     2014-02-11 00:00:00     300
Bob     2014-01-05 00:00:00     100
...
```

Re-indexing and shuffling large data is difficult and expensive.  We need to
find good values on which to partition our data so that we get regularly sized
blocks that fit nicely into memory.  We also need to shuffle entries from all
of the original blocks to all of the new ones.  In principle every old block
has something to contribute to every new one.

We can’t just call  `DataFrame.sort`  because the entire data might not fit in
memory and most of our sorting algorithms assume random access.

We do this in two steps

1. Find good division values to partition our data.  These should partition
the data into blocks of roughly equal size.
2. Shuffle our old blocks into new blocks along the new partitions found in
step one.

## Find divisions by external sorting

One approach to find new partition values is to pull out the new index
from each block, perform an out-of-core sort, and then take regularly spaced
values from that array.

1. Pull out new index column from each block 
 `indexes = [block['new-column-index'] for block in blocks]
`
2. Perform [out-of-core sort](en.wikipedia.org/wiki/External_sorting) on that
column 
 `sorted_index = fancy_out_of_core_sort(indexes)
`
3. Take values at regularly spaced intervals, e.g. 
 `partition_values = sorted_index[::1000000]
`

We implement this using parallel in-block sorts, followed by a streaming merge
process using the  `heapq`  module.  It works but is slow.

### Possible Improvements

This could be accelerated through one of the following options:

1. A streaming numeric solution that works directly on iterators of NumPy
arrays ( `numtoolz`  anyone?)
2. Not sorting at all.  We only actually need approximate regularly spaced
quantiles.  A brief literature search hints that there might be some good
solutions.

## Shuffle

Now that we know the values on which we want to partition we ask each block to
shard itself into appropriate pieces and shove all of those pieces into a
spill-to-disk dictionary.  Another process then picks up these pieces and calls
 `pd.concat`  to merge them in to the new blocks.

For the out-of-core dict we’re currently using
 [Chest](https://github.com/ContinuumIO/chest) .  Turns out that serializing
DataFrames and writing them to disk can be tricky.  There are several good
methods with about an order of magnitude performance difference between them.

## This works but my implementation is slow

Here is an example with snippet of the NYCTaxi data (this is small)

## Some Problems

* First, we have to evaluate the dask as we go.  Every `set_index` operation (and
hence many groupbys and joins) forces an evaluation.  We can no longer, as in
the dask.array case, endlessly compound high-level operations to form more and
more complex graphs and then only evaluate at the end.  We need to evaluate as
we go.
* Sorting/shuffling is slow.  This is for a few reasons including the
serialization of DataFrames and sorting being hard.
* How feasible is it to frequently re-index a large amount of data?  When do we
reach the stage of “just use a database”?
* Pandas doesn’t yet release the GIL, so this is all single-core.  See post on
[PyData and the GIL](https://mrocklin.github.io/blog/work/2015/03/10/PyData-GIL/).
* My current solution lacks basic functionality.  I’ve skipped
the easy things to first ensure sure that the hard stuff is doable.

## Help!

I know less about tables than about arrays.  I’m ignorant of the literature and
common solutions in this field.  If anything here looks suspicious then  *please
speak up* .  I could really use your help.

Additionally the Pandas API is much more complex than NumPy’s.  If any
experienced devs out there feel like jumping in and implementing fairly
straightforward Pandas features in a blocked way I’d be obliged.
