---
title: "Sentencing more biased by race than by class"
date: 2016-06-01
url: https://mathbabe.org/2016/06/01/sentencing-more-biased-by-race-than-by-class/
word_count: 360
---


Yesterday  I was super happy to be passed along [this amazing blogpost](https://lawyerist.com/110584/big-bias-big-data/) from lawyerist.com called *[Uncovering Big Bias with Big Data](https://lawyerist.com/110584/big-bias-big-data/) *and written by [David Colarusso](https://lawyerist.com/author/david-colarusso/), a lawyer who became a data scientist (hat tip Emery Snyder).


For the article, David mines a [recently opened criminal justice data set from Virginia](http://virginiacourtdata.org/), and asked the question, what affects the length of sentence more: income or race? His explanation of each step is readable by non-technical people, it’s a real treasure.


And, unsurprisingly to those of us who have thought about this, the answer he came up with is race, by a long margin, although he also found that class matters too.


In particular he fit his data with the outcome variable set to length of sentence in days – or rather, log(1 + that term), which he explains nicely – and he chose the attributes to be the gender of the defendant, a bunch of indicator variables to determine the race of the defendant (one for each race except white, which was the “default race,” which I thought was a nice touch), the income of the defendant, and finally the “seriousness of the charge,” a system which he built himself and explains. He gives a reasonable explanation of all of these choices except for the gender.


His conclusion:


> For a black man in Virginia to get the same treatment as his Caucasian peer, he must earn more than half a million dollars $90,000 a year.


This sentence follows directly from staring at this table for a couple of minutes, if you imagine two defendants with the same characteristics except one is white and the other is black:


It’s simplistic, and he could have made other choices, but it’s a convincing start. Don’t trust me though, take a look at [his blogpost](https://lawyerist.com/110584/big-bias-big-data/), and also [his github code](https://github.com/colarusso/measured_justice) which includes his iPython notebook.


I am so glad people are doing this. Compared to [shitty ways of using data](https://mathbabe.org/2016/05/25/3-terrible-big-data-ideas/), which end up doubling down on poor and black folks, this kind of analysis shines a light on how the system works against them, and gives me hope that one day we’ll fix it.
