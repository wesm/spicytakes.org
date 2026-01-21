---
title: "Maximum a Posteriori Estimation"
date: 2013-02-25
url: https://mrocklin.github.io/blog/work/2013/02/25/MaximumAposteriori
slug: MaximumAposteriori
word_count: 478
---

*Disclaimer:  I know relatively little about this application.  Corrections welcome.*

In this post we see how SymPy can simplify common numeric calculations, particularly in Bayesian inference problems.

Imagine you are a scientist studying some  [counting process](http://en.wikipedia.org/wiki/Poisson_process)  (like radioactive decay or the number of page requests on a web server).  You describe this process with a  [Poisson random variable](http://en.wikipedia.org/wiki/Poisson_distribution)  and try to learn the rate parameter of this distribution by observing some random samples.

If you have no preconceptions about the rate then this problem is easy.  You just divide total counts by total time and you’re done.

A more complex problem arises when external theory provides prior information
about your rate parameter (for example physics might impose rules on the rate
of radioactive decay).  Lets model this problem in SymPy.  For the sake of
concreteness lets arbitrarily assume that $\lambda$, the rate parameter, follows a Beta distribution with parameters  `a`  and  `b` .

In the lab we observe many samples $x_i$ taken from  `count` .  From these we wish to find the most likely value of  `rate` .  The probability of any single value of  `rate`  given our data can be rewritten with Bayes’ rule.

In this case the distributions are given by

To find the maximizer of $p(\lambda \vert x_i)$ we set the derivative equal to zero.  We simplify the computation by taking the  `log` .  Because  `log`  is monotonic this does not change the solution.

We can accomplish this in SymPy with the following code

## Discussion

SymPy reduces this Bayesian inference problem to finding roots of the above equation.  I suspect that many prevalent numeric problems could be similarly accelerated through a symbolic preprocessing step.

Looking at the equation above it’s clear that this problem can be simplified further.  However I like the existing solution because it does not depend on the user possessing any mathematical expertise beyond the ability to describe their mathematical model (the derivatives, log, etc… are generally applicable to this problem).  In what other automated ways can SymPy further process computations like this?  What are other ways that aren’t in SymPy but could be developed in the future?

I suspect that the problem given here is analytically solvable.  To the extent possible SymPy should try to solve these problems.  However for the vast number of problems without analytic solutions I suspect there is still a great deal we can do, either by reducing the problem as above or through the mathematically informed selection of numeric algorithms.

Various root finding algorithms are appropriate in different cases.  Wikipedia suggests  [Householder’s Method](http://en.wikipedia.org/wiki/Householder%27s_method) , a generalization on Newton’s method for scalar systems with known derivatives.  Perhaps in cases where SymPy is unable to solve the problem analytically it could select the correct numeric algorithm.  Is this a reasonable use case for SymPy?

## References

* [Maximum A Posteriori Estimation](http://en.wikipedia.org/wiki/Maximum_a_posteriori_estimation)
* [Poisson process](http://en.wikipedia.org/wiki/Poisson_process)
* [Householder’s Method](http://en.wikipedia.org/wiki/Householder%27s_method)
