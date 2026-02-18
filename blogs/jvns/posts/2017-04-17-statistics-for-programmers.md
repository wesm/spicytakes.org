---
title: "Some good 'Statistics for programmers' resources"
date: 2017-04-17
url: https://jvns.ca/blog/2017/04/17/statistics-for-programmers/
slug: statistics-for-programmers
word_count: 956
---


This post is basically a list of books & other resources that teach statistics
using programming. But first I wanted to say why I think that is important! You can skip further down if you’re already sold.


Statistics can sometimes seem boring and difficult to understand. When I
start reading statistics textbooks, I read about

- the normal distribution
- t-tests
- chi-squared tests
- the central limit theorem


I know what some of those things are (I have a math degree, after all, and so
I have some idea of what the central limit theorem says). But I often don’t
find them that *useful* for solving my day to day statistics problems.


Like, here are some questions I sometimes have about data

- I measured some performance numbers, made a change, and then measured
some new numbers. Did my change really make a difference? (“hypothesis testing”)
- I have a bunch of numbers and I want to know what the average is, and I want to know how seriously I should take that average (is it 6 +/- 1? or 6 +/= 0.01?) (“confidence intervals”)


One of the biggest problems with tests like the chi-squared test is that they
make a lot of *assumptions* about how your data was generated. Usually they
assume that your data is normally distributed. Not everything follows a normal
distribution!


So – can I figure out if my change really made my code faster or not
without having to make a bunch of assumptions?


It turns out the answer is “yes”, and that there’s a whole subfield of
statistics devoted making less assumptions (“nonparametric statistics”). And
even better – that subfield is actually *easier to use* than regular
statistics.


Some of the methods:

- bootstrapping (which lets you calculate a mean + error bars for that mean!)
- shuffling your data (which lets you tell if 2 groups of numbers “really” have a different mean or not)


These methods are often really computational – like
instead of using a bunch of formulas, you’ll write a program. And you’ll get
statistically valid answers back! I like this because even though I know a lot
of math, I often find programs more intuitive than formulas.


### why program instead of use formulas?


A lot of the formulas you can use to do statistics make a lot of assumptions,
and then you can quickly use a formula to calculate the statistical thing you
want (like a chi-square test or whatever). This was necessary when people had
really limited computational resources (like, they had a book with tables in
it and a pen and paper).


But today we have computers! So we can use really dramatically different
statistical methods than people used in the 19th century. And often you
can make less assumptions, which can be really good!


Anyway, I asked for recommendations for “nonparametric statistics for programmers” resources [on Twitter](https://twitter.com/b0rk/status/854019965816623104) and I got a lot of good recommendations back. Here they are. I haven’t


## some good “statistics for programmers” resources


### statistics without the agonizing pain


This is a [really nice 10 minute talk about how to do statistics using programming](https://www.youtube.com/watch?v=5Dnw46eC-0o). Here, I even embedded it!


### statistics for hackers, by jake vanderplas


This [talk from PyCon 2016](https://www.youtube.com/watch?v=Iq9DzN6mvYA) is exactly
the kind of intro to nonparametric methods I’m talking about!!  It has a slide deck which is
good to read by itself. It introduces shuffling & bootstrapping which I think
are two of the most important statistics methods to know.


### nonparametric stats with R


This is the best thing I found so far that actually explains these nonparametric methods in an introductory way with programming.


It’s is an online textbook that teaches basic nonparametric statistics with R. [An Introduction to Statistical and Data Sciences via R](https://ismayc.github.io/moderndiver-book/)


the two chapters i found most useful to look at were

- [hypothesis testing](https://ismayc.github.io/moderndiver-book/7-hypo.html)
- [how to calculate confidence intervals using bootstrapping](https://ismayc.github.io/moderndiver-book/8-ci.html) which is a great thing to be able to do.


### all of nonparametric statistics by Larry Wasserman


This is a [physical book from Springer](http://www.springer.com/us/book/9780387251455) and you can [get the PDF from his website](http://www.stat.cmu.edu/~larry/all-of-nonpar/contents.pdf). It’s a math book and not “teaching statistics with programming” but a a lot of people recommended it.


Now we’re going to veer away from nonparametric stats and into statistics books for programmers generally.


### Allen Downey’s work


Allen Downey wrote this great [textbook manifesto](http://greenteapress.com/wp/textbook-manifesto/) and his work looks really approachable. All of his books are available online for free which is a really lovely thing.


not so much nonparametric statistics but I hear really good things

- [Think Stats](http://greenteapress.com/thinkstats/)
- [Think Bayes](http://greenteapress.com/wp/think-bayes/)


Someone also mentioned


> Allen is a great teacher, so it’s worth watching (or, even better, attending) his tutorials as well as reading the books.


I remember watching a statistics talk Allen gave at PyCon a few years back and being really impressed.


### introduction to probability by Peter Norvig


[Here it is](http://nbviewer.jupyter.org/url/norvig.com/ipython/Probability.ipynb)!


### probabilistic programming & bayesian methods for hackers


[Probabilistic Programming & Bayesian Methods for Hackers](http://camdavidsonpilon.github.io/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers/) by Cam Davidson-Pilon is a cool introduction to bayesian methods with a lot of calculations.


### even more links

- a paper someone said was good (by Efron): [Bootstrap Methods: another look at the jackknife](http://www.stat.cmu.edu/~fienberg/Statistics36-756/Efron1979.pdf)
- this [book by 5 people named lock](http://www.lock5stat.com/)
- this [blog post has an overview of different nonparametric tests](http://miningthedetails.com/blog/r/non-parametric-tests/)
- this [podcast with Philip Guo and John DeNero where they talk about teaching stats to programmers](http://pgbovine.net/PG-Podcast-2-John-DeNero.htm)
- [nonparametric statistical methods](https://www.amazon.com/Nonparametric-Statistical-Methods-Myles-Hollander/dp/0470387378/ref=pd_sim_14_2?_encoding=UTF8&pd_rd_i=0470387378&pd_rd_r=S25ACHMQ2N1T8W9ZSPTD&pd_rd_w=gsGP9&pd_rd_wg=49Jkx&psc=1&refRID=S25ACHMQ2N1T8W9ZSPTD)
- [openintro](https://www.openintro.org/stat/textbook.php?stat_book=isrs) has free some statistics books


### tell me if you have more cool recommendations


If there is an amazing book that teaches statistics with programming that I left out I would like to know about it! I’m on twitter at @b0rk.
