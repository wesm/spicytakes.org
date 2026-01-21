---
title: "SymPy and Theano -- Matrix Expressions"
date: 2013-04-05
url: https://mrocklin.github.io/blog/work/2013/04/05/SymPy-Theano-part-3
slug: SymPy-Theano-part-3
word_count: 988
---

## Introduction

*This post uses some LaTeX.  You may want to read it on the [original site](http://matthewrocklin.com/blog/work/2013/04/05/SymPy-Theano-part-3/).*

This is the last of a three part series connecting SymPy and Theano to transform mathematical expressions into efficient numeric code (see  [part 1](http://matthewrocklin.com/blog/work/2013/03/19/SymPy-Theano-part-1/)  and  [part 2](http://matthewrocklin.com/blog/work/2013/03/28/SymPy-Theano-part-2/) ).  We have seen that it is simple and computationally profitable to combine the best parts of both projects.

In this post we’ll switch from computing scalar expressionss to computing matrix expressions.  We’ll define the Kalman filter in SymPy and send it to Theano for code generation.  We’ll then use SymPy to define a more performant blocked version of the same algorithm.

## Kalman Filter

The  [Kalman filter](http://en.wikipedia.org/wiki/Kalman_filter)  is an algorithm to compute the Bayesian update of a normal random variable given a linear observation with normal noise.  It is commonly used when an uncertain quantity is updated with the results of noisy observations.  For example it is used in weather forecasting after weather stations report in with new measurements, in aircraft/car control to automatically adjust for external conditions real-time, or even on your smartphone’s GPS navigation as you update your position based on fuzzy GPS signals.   It’s everywhere, it’s important, and it needs to be computed quickly and continuously.  It suits our needs today because it can be completely defined with a pair of matrix expressions.

\(\Sigma H^T \left(H \Sigma H^T + R\right)^{-1} \left(-data + H \mu\right) + \mu\)
\(- \Sigma H^T \left(H \Sigma H^T + R\right)^{-1} H \Sigma + \Sigma\)

## Theano Execution

The objects above are for symbolic mathematics, not for numeric computation.  If we want to compute this expression we pass our expressions to Theano.

Theano builds a Python function that calls down to a combination of low-level  `C`  code,  `scipy`  functions, and calls to the highly optimized  `DGEMM`  routine for matrix multiplication.  As input this function takes five numpy arrays corresponding to our five symbolic  `inputs`  and produces two numpy arrays corresponding to our two symbolic  `outputs` .   [Recent work](https://github.com/sympy/sympy/pull/1965)  allows  *any*  SymPy matrix expression to be translated to and run by Theano.

## Blocked Execution

These arrays are too large to fit comfortably in the fastest parts of the memory hierarchy.  As a result each sequential  `C` ,  `scipy` , or  `DGEMM`  call needs to move big chunks of memory around while it computes.  After one operation completes the next operation moves around the same memory while it performs its task.  This repeated memory shuffling hurts performance.

A common approach to reduce memory shuffling is to cut the computation into smaller blocks.  We then perform as many computations as possible on a single block before moving on.  This is a standard technique in matrix multiplication.

We are now able to focus on substantially smaller chunks of the array.  For example we can choose to keep  `A`  in local memory and perform all computations that involve  `A` .  We will still need to shuffle some memory around (this is inevitable) but by organizing with blocks we’re able to shuffle less.

This idea extends beyond matrix multiplication.  For example, SymPy knows how to block a matrix inverse

High performance dense linear algebra libraries hard-code all of these tricks into each individual routine.  The call to the general matrix multiply routine  `DGEMM`  performs blocked matrix multiply within the call.  The call to the general matrix solve routine  `DGESV`  can perform blocked matrix solve.  Unfortunately these routines are unable to coordinate blocked computation  *between*  calls.

Fortunately, SymPy and Theano can.

SymPy can define and reduce the blocked matrix expressions using relations like what are shown above.

Theano is then able to coordinate this computation and compile it to low-level code.  At this stage the expresssions/computations are fairly complex and difficult to present.  Here is an image of the computation (click for zoomable PDF) as a directed acyclic graph.

## Results

Lets time each function on the same inputs and see which is faster

That’s a 20% performance increase from just a few lines of high-level code.

Blocked matrix multiply and blocked solve routines have long been established as  *a good idea* .  High level mathematical and array programming libraries like SymPy and Theano allow us to extend this good idea to  *arbitrary*  array computations.

## Analysis

### Good Things

First, lets note that we’re not introducing a new library for dense linear algebra.  Instead we’re noting that pre-existing general purpose high-level tools can be composed to that effect.

Second, lets acknoledge that we could take this further.  For example Theano seemlessly handles GPU interactions.  We could take this same code to a GPU accelerated machine and it would just run faster without any action on our part.

### Bad Things

However, there are some drawbacks.

Frequent readers of my blog might recall a  [previous post about the Kalman filter](http://matthewrocklin.com/blog/work/2012/11/24/Kalman-Filter/) .  In it I showed how we could use SymPy’s inference engine to select appropriate BLAS/LAPACK calls.  For example we could infer that because $ H \Sigma H^T + R $ was symmetric positive definite we could use the substantially more efficient  `POSV`  routine for matrix solve rather than  `GESV`  ( `POSV`  uses the Cholesky algorithm for decomposition rather than straight LU).  Theano doesn’t support the specialized BLAS/LAPACK routines though, so we are unable to take advantage of this benefit.  The lower-level interface (Theano) is not sufficiently rich to use all information captured in the higher-level (SymPy) representation.

Also, I’ve noticed that the blocked version of this computation experiences some significant roundoff errors (on the order of  `1e-3` ).  I’m in the process of tracking this down.  The problem must occur somewhere in the following tool-chain

```
SymPy -> Blocking -> Theano -> SciPy -> C routines -> BLAS
```

Debugging in this context can be wonderful if all elements are well unit-tested.  If they’re not (they’re not) then tracking down errors like this requires an unfortunate breadth of expertise.

## References

Scripts

* [Kalman example](https://mrocklin.github.io/blog/scripts/kalman.py)
* [Block Matrix example](https://mrocklin.github.io/blog/scripts/blocks.py)
* [Block Kalman](https://mrocklin.github.io/blog/scripts/kalman_blocked.py)
