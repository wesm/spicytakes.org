---
title: "Distributed Prototype"
date: 2015-10-09
url: https://mrocklin.github.io/blog/work/2015/10/09/Distributed
slug: Distributed
word_count: 681
---

*This work is supported by [Continuum Analytics](http://continuum.io)
and the [XDATA Program](http://www.darpa.mil/program/XDATA)
as part of the [Blaze Project](http://blaze.pydata.org)*

**tl;dr: We demonstrate a prototype distributed computing library and discuss
data locality.**

## Distributed Computing

Here’s a new prototype library for distributed computing.
It could use some critical feedback.

* [distributed.readthedocs.org/en/latest/](http://distributed.readthedocs.org/en/latest/)
* [github.com/mrocklin/distributed/](http://github.com/mrocklin/distributed/)

This blogpost uses  `distributed`  on a toy example.  I won’t talk about the
design here, but the docs should be a quick and informative read.  I recommend
the  [quickstart](http://distributed.readthedocs.org/en/latest/quickstart.html) 
in particular.

We’re going to do a simple computation a few different ways on a cluster of
four nodes.  The computation will be

1. Make a 1000 random numpy arrays, each of size 1 000 000
2. Compute the sum of each array
3. Compute the total sum of the sums

We’ll do this directly with a distributed Pool and again with a dask graph.

## Start up a Cluster

I have a cluster of four  `m3.xlarge` s on EC2

```
$ ssh node1
$ dcenter

$ ssh node2
$ dworkder node1:8787

$ ssh node3
$ dworkder node1:8787

$ ssh node4
$ dworkder node1:8787
```

[Notes on how I set up my cluster.](https://gist.github.com/mrocklin/3c1e47f403490edb9473)

## Pool

On the client side we spin up a distributed  `Pool`  and point it to the center
node.

Then we create a bunch of random numpy arrays:

Our result is a list of proxy objects that point back to individual numpy arrays
on the worker computers.  We don’t move data until we need to.  (Though we
could call  `.get()`  on this to collect the numpy array from the worker.)

Further computations on this data happen on the cluster, on the worker nodes
that hold the data already.

This avoids costly data transfer times.  Data transfer will happen when
necessary though, as when we compute the final sum.  This forces communication
because all of the intermediate sums must move to one node for the final
addition.

## distributed.dask

Now we do the same computation all at once by manually constructing a dask
graph (beware, this can get gnarly, friendlier approaches exist below.)

Apparently not everyone finds dask dictionaries to be pleasant to write by
hand.  You could also use this with dask.imperative or dask.array.

### dask.imperative

### dask.array

The dask approach was smart enough to delete all of the intermediates that it
didn’t need.  It could have run intelligently on far more data than even our
cluster could hold.  With the pool we manage data ourselves manually.

## Mix and Match

We can also mix these abstractions and put the results from the pool into dask
graphs.

## Discussion

The  `Pool`  and  `get`  user interfaces are independent from each other but both
use the same underlying network and both build off of the same codebase.  With
 `distributed`  I wanted to build a system that would allow me to experiment
easily.  I’m mostly happy with the result so far.

One non-trivial theme here is data-locality.  We keep intermediate results on
the cluster and schedule jobs on computers that already have the relevant data
if possible.  The workers can communicate with each other if necessary so that
any worker can do any job, but we try to arrange jobs so that workers don’t
have to communicate if not necessary.

Another non-trivial aspect is that the high level  `dask.array`  example works
without any tweaking of dask.  Dask’s separation of schedulers from collections
means that existing dask.array code (or dask.dataframe, dask.bag,
dask.imperative code) gets to evolve as we experiment with new fancier
schedulers.

Finally, I hope that the cluster setup here feels pretty minimal.  You do need
some way to run a command on a bunch of machines but most people with clusters
have some mechanism to do that, even if its just ssh as I did above.  My hope
is that  `distributed`  lowers the bar for non-trivial cluster computing in
Python.

## Disclaimer

Everything here is  *very experimental* .  The library itself is broken
and unstable.  It was made in the last few weeks and hasn’t been used on
anything serious.  Please adjust expectations accordingly and
 [provide critical feedback.](https://github.com/mrocklin/distributed/pull/3)

* [Distributed Documentation](http://distributed.readthedocs.org/en/latest/)
