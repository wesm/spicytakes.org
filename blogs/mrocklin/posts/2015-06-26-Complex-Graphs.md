---
title: "Write Complex Parallel Algorithms"
date: 2015-06-26
url: https://mrocklin.github.io/blog/work/2015/06/26/Complex-Graphs
slug: Complex-Graphs
word_count: 548
---

*This work is supported by [Continuum Analytics](http://continuum.io)
and the [XDATA Program](http://www.darpa.mil/program/XDATA)
as part of the [Blaze Project](http://blaze.pydata.org)*

**tl;dr: We discuss the use of complex dask graphs for non-trivial algorithms.
We show off an on-disk parallel SVD.**

## Most Parallel Computation is Simple

Most parallel workloads today are fairly trivial:

Graphs for these computations look like the following:

[
](https://mrocklin.github.io/blog/images/dask-bag-embarassing.png)

This is great; these are simple problems to solve efficiently in parallel.
Generally these simple computations occur at the  *beginning*  of our analyses.

## Sophisticated Algorithms can be Complex

Later in our analyses we want more complex algorithms for statistics
, machine learning, etc..  Often this stage fits
comfortably in memory, so we don’t worry about parallelism and can use
 `statsmodels`  or  `scikit-learn`  on the gigabyte result we’ve gleaned from
terabytes of data.

However, if our reduced result is still large then we need to think about
sophisticated parallel algorithms.  This is fresh space with lots of exciting
academic and software work.

## Example: Parallel, Stable, Out-of-Core SVD

I’d like to show off work by  [Mariano Tepper](http://www.marianotepper.com.ar/) ,
who is responsible for  `dask.array.linalg` .  In particular he has a couple of
wonderful algorithms for the
 [Singular Value Decomposition (SVD)](https://en.wikipedia.org/wiki/Singular_value_decomposition) 
(also strongly related to  [Principal Components Analysis (PCA)](https://en.wikipedia.org/wiki/Principal_component_analysis) .)
Really I just want to show off this pretty graph.

[
](https://mrocklin.github.io/blog/images/dask-svd.png)

This algorithm computes the exact SVD (up to numerical precision) of a large
tall-and-skinny matrix in parallel in many small chunks.  This allows it to
operate out-of-core (from disk) and use multiple cores in parallel.  At the
bottom we see the construction of our trivial array of ones, followed by many
calls to  `np.linalg.qr`  on each of the blocks.  Then there is a lot of
rearranging of various pieces as they are stacked, multiplied, and undergo more
rounds of  `np.linalg.qr`  and  `np.linalg.svd` .  The resulting arrays are
available in many chunks at the top and second-from-top rows.

The  [dask dict](http://dask.pydata.org/en/latest/spec.html)  for one of these
arrays,  `s` , looks like the following:

So to write complex parallel algorithms we write down dictionaries of tuples of
functions.

The dask schedulers take care of executing this graph in parallel using
multiple threads.  Here is a profile result of a larger computation on a
30000x1000 array:

## Low Barrier to Entry

Looking at this graph you may think “Wow, Mariano is awesome” and indeed he is.
However, he is more an expert at linear algebra than at Python programming.
Dask graphs (just dictionaries) are simple enough that a domain expert was able
to look at them say “Yeah, I can do that” and write down the very complex
algorithms associated to his domain, leaving the execution of those algorithms
up to the dask schedulers.

You can see the source code that generates the above graphs
 [on GitHub](https://github.com/ContinuumIO/dask/blob/master/dask/array/linalg.py) .

[
](https://mrocklin.github.io/blog/images/dask-svd-random.png)

## Randomized Parallel Out-of-Core SVD

A few weeks ago
 [a genomics researcher asked](https://github.com/ContinuumIO/dask/issues/265) 
for an approximate/randomized variant to SVD.
Mariano had  [a solution](https://github.com/ContinuumIO/dask/pull/280) 
up in a few days.

I’ll omit the full dict for obvious space reasons.

## Final Thoughts

Dask graphs let us express parallel algorithms with very little extra
complexity.  There are no special objects or frameworks to learn, just
 [dictionaries of tuples of functions](http://dask.pydata.org/en/latest/spec.html) .
This allows domain experts to write sophisticated algorithms without fancy code
getting in their way.
