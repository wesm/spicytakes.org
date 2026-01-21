---
title: "Using SymPy within Theano"
date: 2013-08-14
url: https://mrocklin.github.io/blog/work/2013/08/14/SymPy-Theano-part-4
slug: SymPy-Theano-part-4
word_count: 662
---

Several months ago I published a sequence of blogposts about using SymPy and Theano together to generate efficient mathematical codes.  Main points from the posts were as follows

* [Code Generation](http://matthewrocklin.com/blog/work/2013/03/19/SymPy-Theano-part-1/) : We created a drop-in replacement for SymPy’s code generation with a thin layer to Theano.
* [Scalar Simplificaiton](http://matthewrocklin.com/blog/work/2013/03/28/SymPy-Theano-part-2/) :  We used SymPy’s simplification routines to accelerate programs prior to code printing in Theano
* [Matrix Expressions](http://matthewrocklin.com/blog/work/2013/04/05/SymPy-Theano-part-3/) :  We generate fast blocked numeric linear algebra programs from SymPy’s matrix expressions using Theano array operations.

A week ago  [someone popped up on the SymPy mailing list](https://groups.google.com/d/topic/sympy/VtaxCRNO4sE/discussion)  asking if a particular SymPy operation ( `sympy.Piecewise` ) could be supported in the SymPy-Theano translation.  Because Theano has a similar operation ( `theano.tensor.switch` ) it was simple to add this translation.  In general though this post raised some interesting questions:

* Is there a way to avoid constantly making new translations for operations that exist both in SymPy and in Theano?
* What do we do with SymPy’s more exotic operations for which no Theano analog exists?  E.g. how do we generate code for factorial or bessel functions?

In an attempt to resolve these issues we recently merged a general  `SymPyCCode`  operation into the  `Theano`  project.  It enables the expression of a Theano scalar operation through SymPy expressions using SymPy’s original code generation capability.  For example we can create a simple addition operation like so

Theano operators can be applied to Theano variables to make compound Theano expressions

Theano can then turn these expressions into functions

So we can describe scalar operations in SymPy and use them directly in Theano without having to translate anything.  Of course, the  `add`  operation is already native in Theano.  This is more useful for complex scalar expressions, particularly if Theano does not already have such an operation

## Under the Hood

Internally the  `SymPyCCode`  op calls SymPy’s C code printers to generate an implementation of the scalar operation.  For example the following SymPy code generates C code to compute the probability density function of a normal distribution.

Theano is then able to use this generated C code within its generated C program.  Theano still handles memory, common sub-expressions, arrays, etc. but is now able to leverage SymPy to generate low-level kernels for mathematical operations.

## But Don’t Use This

But you shouldn’t use this mechanism if you don’t have to.  Recall from the  [first post](http://matthewrocklin.com/blog/work/2013/03/19/SymPy-Theano-part-1/)  that SymPy can translate many standard operations to Theano directly, without having to wrap the SymPy expressions up in a black box Theano operation.  Native translation enables Theano to  use many additional optimizations like the use of the GPU, automatic differentiation, and common sub-expression elimination across many expressions.  This approach is mainly for cases where your complex scalar expressions don’t translate well to Theano.  In some cases the SymPyCCode op may also provide better performance (maybe SymPy’s generated C code is a bit tighter?)

## Future Work

We need to improve SymPy’s code printers.  While they support all the standard operators they neglect to cover the really interesting cases like bessel functions or factorial.  These are cases where the numerical analysis community can concisely describe the “right way” to compute many of these operations in isolation.   For example the factorial of  `n`  can be computed as  `gamma(n+1)` , a fact rarely known by mainstream programmers.

I’ve been thinking about the right way to do this generally.  Right now my thought is that we should create a new  `expand`  hint for computation.  If you have thoughts I’d love to hear about them; please speak up in the comments.

## Example

There are a number of ways to compute a SymPy expression numerically.  I’m going to explicily run throuh an example with a few of them below.  You should ignore this section if these are already familiar to you.

We create a function to evaluate a normal distribution probability density function for a particular mean and standard deviation across a range of values for  `x` .
