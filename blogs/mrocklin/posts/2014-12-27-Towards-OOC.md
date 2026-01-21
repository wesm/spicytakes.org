---
title: "Towards Out-of-core ND-Arrays"
date: 2014-12-27
url: https://mrocklin.github.io/blog/work/2014/12/27/Towards-OOC
slug: Towards-OOC
word_count: 1526
---

*This work is supported by [Continuum Analytics](http://continuum.io)
and the [XDATA Program](http://www.darpa.mil/program/XDATA)
as part of the [Blaze Project](http://blaze.pydata.org)*

**tl;dr**  We propose a system for task-centered computation, show an example
with out-of-core nd-arrays, and ask for comments.

*Note: This post is not user-focused.  It is intended for library writers.*

## Motivation

Recent notebooks (links
 [1](http://nbviewer.ipython.org/url/blaze.pydata.org/en/latest/_static/notebooks/timings-csv.ipynb) ,
 [2](http://nbviewer.ipython.org/url/blaze.pydata.org/en/latest/_static/notebooks/timings-bcolz.ipynb) )
describe how Blaze handles out-of-core single-dataset tabular computations in
the following stages.

1. Partition the dataset into chunks
2. Apply some computation on each chunk
3. Concatenate the results (hopefully smaller)
4. Apply another computation into the concatenated result

Steps 2 and 4 require symbolic analysis of  *what*  work should be done; Blaze
does this well.  Steps 1 and 3 are more about coordinating  *where*  data goes
and  *when*  computation executes.

This setup is effective for a broad class of single-dataset tabular
computations.  It fails for more complex cases.  Blaze doesn’t currently have a
good target for describing complex inter-block data dependencies.  The model
for breaking apart data and arranging computations (1 and 3) is too simple.

A good example of a complex case is an nd-array matrix-matrix multiply / dot
product / tensor contraction.  In this case a blocked approach has a more
complex communication pattern.  This post is about finding a simple framework
that allows us to express these patterns.  It’s about finding a replacement for
steps 1 and 3 above.

## Task Scheduling

The common solution to this problem is to describe the computation as a
bipartite directed acyclic graph where nodes are computations and data and
edges indicate which pieces of data a computation takes as input and delivers
as output.

Many solutions to this problem exist, both theoretical algorithms and
implemented software.  Forgive me for describing yet-another system.

## `dask`

We use a low-tech representation of a task dependency graph.
We use a dictionary of key-value pairs where keys are any hashable identifier
and values are one of the following:

1. A value, like  `1`
2. A tuple containing a function and arguments, like  `(inc, 1)` .  This is like
an s-expression and should be interpreted as an unevaluated  `inc(1)`
3. A tuple containing a function and arguments. Arguments may include other
keys,  `(inc, 'my_key')`

This is more clear with an example.  We show this example on the right.

The  [`dask` library](http://github.com/mrocklin/dask)  contains a small
reference implementation to get values associated to keys in this task graph.

In principle this could be executed by a variety of different implementations
each with different solutions for distributed computing, caching, etc..

Dask also includes convenience functions to help build this graph.

Although this is mainly to help those who feel uncomfortable putting the
parenthesis on the left side of a function call to avoid immediate execution

## Why low tech?

These “graphs” are just dictionaries of tuples.  Notably, we imported  `dask` 
 *after*  we built our graph.  The framework investment is very light.

* **Q** : Why don’t we build  `Task`  and  `Data`  classes and construct a Python
framework to represent these things formally?
* **A** : Because people have to learn and buy in to that framework and that’s
hard to sell.  Dictionaries are easier to sell.  They’re also easy to translate
into other systems.   Additionally, I was able to write a reference
implementation in  [a couple dozen lines](https://github.com/mrocklin/dask/blob/master/dask/core.py#L36-L68) .

It’s easy to build functions that create  `dict` s like this for various
applications.  There is a decent chance that, if you’ve made it this far in
this blogpost, you already understand the spec.

## ND-Arrays

I want to encode out-of-core ND-Array algorithms as data.
I’ve written a few functions that create dask-style dictionaries to help me
describe a decent class of blocked nd-array computations.

The following section is a specific example applying these ideas to the domain
of array computing.  This is just one application and not core to the idea
of task scheduling.  The core ideas to task scheduling and the dask
implementation have already been covered above.

### Getting blocks from an array

First, we break apart a large possibly out-of-core array into blocks.
For convenience in these examples we work in in-memory numpy arrays rather than
on-disk arrays.   Jump to the end if you’d like to see a real OOC dot product
on on-disk data.

We make a function  `ndget`  to pull out a single block

We now make a function  `getem`  that makes a  `dict`  that uses this  `ndget` 
function to pull out all of the blocks.  This creates more  `keys`  in our
dictionary, one for each block.  We name each key by the key of the array
followed by a block-index.

* `getem` : Given a large possibly out-of-core array and a blocksize, pull
 apart that array into many small blocks

So we have a single original array,  `x`  and using  `getem`  we describe how to
get many blocks out of  `x`  using the function  `ndget`  for on each block.

* `ndget`  actually does work on data
* `getem`  creates dask dict that describes on what ndget should operate

We haven’t done work yet.  We only do work when we finally call  `dask.get`  on
the appropriate key for one of the blocks.

We use  `numpy.ndarrays`  for convenience.  This would have worked with anything
that supports numpy-style indexing, including out-of-core structures like
 `h5py.Dataset` ,  `tables.Array` , or  `bcolz.carray` .

### Example: Embarrassingly Parallel Computation

If we have a simple function

That we want to apply to all blocks of the dataset we could, in principle,
add the following to our dictionary.

Our use of keys like  `('name', i, j)`  to refer to the  `i,jth`  block of an array is
an incidental convention and not intrinsic to  `dask`  itself.  This use of
tuples as keys should not be confused with the use of tuples in values to
encode unevaluated functions.

### Index expressions

A broad class of array computations can be written with index expressions

\(Z_{ij} = X_{ji} \;\;\)  – Matrix transpose

\(Z_{ik} = \sum_j X_{ij} Y_{jk} \;\;\)  – Matrix-matrix multiply

Fortunately, the blocked versions of these algorithms look pretty much the
same.  To leverage this structure we made the function  `top`  for  `t` ensor
 `op` erations (ideas for a better name welcome).  This writes index operations
like the following for blocked transpose:

The first argument  `np.transpose`  is the function to apply to each block.
The second and third arguments are the name and index pattern of the output.
The succeeding arguments are the key and index pattern of the inputs.  In this
case the index pattern is the reverse.  We map the  `ij` th block to the  `ji` th
block of the output after we call the function  `np.transpose` .
Finally we have the numblocks keyword arguments that give the block structure
of the inputs.  Index structure can be any iterable.

### Matrix Multiply

We represent tensor contractions like matrix-matrix multiply with indices that
are repeated in the inputs and missing in the output like the following.  In
the following example the index  `'j'`  is a contracted dummy index.

In this case the function receives an iterator of blocks of data that iterate
over the dummy index,  `j` .  We make such a function to take iterators of square
array blocks, dot product the pairs, and then sum the results.  This is the
inner-most loop of a conventional blocked-matrix-matrix multiply algorithm.

By combining this per-block function with  `top`  we get an out-of-core dot
product.

The  `top`  function inspects the index structure of the inputs and outputs and
constructs dictionaries that reflect this structure, matching indices between
keys and creating lists of keys over dummy indices like  `j` .

And that was it, we have an out-of-core dot product.  Calling dask.get on these
keys results in out-of-core execution.

## Full example

Here is a tiny proof of concept for an out-of-core dot product.  I wouldn’t
expect users to write this.  I would expect libraries like Blaze to write this.

### Create random array on disk

### Define computation  `A.T * A`

### Do work

Three minutes for a 7GB dot product.  This runs at about half the FLOPS of a
normal in-memory matmul.  I’m not sure yet why the discrepancy.  Also, this
isn’t using an optimized BLAS; we have yet to leverage multiple cores.

This isn’t trivial to write, but it’s not bad either.

## Complexity and Usability

This system is not appropriate for users; it’s unPythonic, low-level, and
LISP-y.  However I believe that something like this would be an appropriate
standard for infrastructural libraries.  It’s a simple and easy standard for
code to target.

Using projects like  `into`  and  `blaze`  we can build a usable high-level
front-end onto  `dask`  for the subproblems of arrays and tables. Blaze could
generate these dictionaries and then hand them off to other systems to execute.

## Execution

Using the reference implementation, multithreading, HDF5/BColz, and out-of-core
caching systems like  `chest`  I think that we can build a decent out-of-core
 `ndarray`  solution that fully leverages a large workstation.

Ideally other people come along and build better execution engines / task
schedulers.  This might be an appropriate application for IPython parallel.

## Help

This could use design and technical feedback.
What would encourage community buy-in to a system like this?
