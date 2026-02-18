---
title: "Machine learning isn't Kaggle competitions"
date: 2014-06-19
url: https://jvns.ca/blog/2014/06/19/machine-learning-isnt-kaggle-competitions/
slug: machine-learning-isnt-kaggle-competitions
word_count: 1036
---


I write about strace and kernel programming on this blog, but at work
I actually mostly work on machine learning, and it’s about time I
started writing about it! Disclaimer: I work on a data analysis /
engineering team at a tech company, so that’s where I’m coming from.


When I started trying to get better at machine learning, I went to
[Kaggle](http://www.kaggle.com/) (a site where you compete to solve
machine learning problems) and tried out one of the classification
problems. I used an
out-of-the-box algorithm, messed around a bit, and definitely did not
make the leaderboard. I felt sad and demoralized – what if I
was really bad at this and never got to do math at work?! I still
don’t think I could win a Kaggle competition. But I have a job where I do
(among other things) machine learning! What gives?


To back up from Kaggle for a second, let’s imagine that you have an
awesome startup idea. You’re going to predict flight arrival times for
people! There are a ton of decisions you’ll need to make before you even
start thinking about support vector machines:


### Understand the business problem


If you want to predict flight arrival times, what are you really
trying to do? Some possible options:

- Help the airline understand which flights are likely to be delayed, so
they can fix it.
- Help people buy flights that are less likely to be delayed.
- Warn people if their flight tomorrow is going to be delayed


I’ve spent time on projects where I didn’t understand at all how the
model was going to fit into business plans. If this is you, it *doesn’t
matter* how good your model is. At all.


Understanding the business problem will also help you decide:

- How accurate does my model really need to be? What kind of false
positive rate is acceptable?
- What data can I use? If you’re predicting flight days tomorrow, you
can look at weather data, but if someone is buying a flight a month
from now then you’ll have no clue.


### Choose a metric to optimize


Let’s take our flight delays example. We first have to decide whether to
do classification (“will this flight be delayed for at least an hour”)
or regression (“how long will this flight be delayed for?”). Let’s say
we pick regression.


People often optimize the sum of squares because it has nice statistical
properties. But mispredicting a flight arrival time by 10 hours and by
20 hours are pretty much equally bad. Is the sum of squares really
appropriate here?


### Decide what data to use


Let’s say I already have the airline, the flight number, departure
airport, plane model, and the departure and arrival times.


Should I try to buy more specific information about the different plane
models (age, what parts are in them..)? Really accurate weather data?
The amount of information available to you isn’t fixed! You can get
more!


### Clean up your data


Once you have data, your data will be a mess. In this flight search
example, there will likely be

- airports that are inconsistently named
- missing delay information all over the place
- weird date formats
- trouble reconciling weather data and airport location


Cleaning up data to the point where you can work with it is a
huge amount of work. If you’re trying to reconcile a lot of sources of
data that you don’t control like in this flight search example, it can
take 80% of your time.


### Build a model!


This is the fun Kaggle part. Training! Cross-validation! Yay!


Now that we’ve built what we think is a great model, we actually have to
use it:


### Put your model into production


Netflix didn’t actually implement the model that
won the Netflix competition because
[it was too complicated](http://www.forbes.com/sites/ryanholiday/2012/04/16/what-the-failed-1m-netflix-prize-tells-us-about-business-advice/).


If you trained your model in Python, can you run it in production in
Python? How fast does it need to be able to return results? Are you
running a model that bids on advertising spots / does high frequency
trading?


If we’re predicting flight delays, it’s probably okay for our model to
run somewhat slowly.


Another surprisingly difficult thing is gathering the data to evaluate
your model – getting historical weather data is one thing, but getting
that same data in real time to predict flight delays *right now* is
totally different.


### Measure your model’s performance


Now that we’re running the model on live data, how do I measure its
real-life performance? Where do I log the scores it’s producing? If
there’s a huge change in the inputs my model is getting after 6 months,
how will I find out?


### Kaggle solves all of this for you.


With Kaggle, almost all of these problems are already solved for you:
you don’t need to worry about the engineering aspects of running a
model on live data, the underlying business problem, choosing a metric,
or collecting and cleaning up data.


You won’t go through all these steps just once – maybe you’ll build a
model and it won’t perform well so you’ll try to add some additional
features and see if you can build a better model. Or maybe how useful
the model is to your business depends on how good the results are.


Doing Kaggle problems is fun! It means you can focus on machine
learning algorithm nerdery and get better at that. But it’s pretty far
removed from my job, where I work on a
[team (hiring!)](https://stripe.com/jobs#data_engineer) that thinks
about all of these problems. Right now I’m looking at measuring
models’ performance once they’re in production, for instance!


So if you look at Kaggle leaderboards and think that you’re bad at
machine learning because you’re not doing well, don’t. It’s a fun but
artificial problem that doesn’t reflect real machine learning work.


(to be clear: I don’t think that Kaggle misrepresents itself, or does
a bad job – it specializes in a particular thing and that’s fine. But
when I was starting out, I thought that machine learning work would be
like Kaggle competitions, and it’s not.)


(thanks to the fantastic [Alyssa Frazee](http://alyssafrazee.com/) for
helping with drafts of this!)
