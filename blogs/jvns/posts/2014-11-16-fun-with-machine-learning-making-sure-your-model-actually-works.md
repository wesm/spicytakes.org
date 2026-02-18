---
title: "Fun with machine learning: does your model actually work?"
date: 2014-11-16
url: https://jvns.ca/blog/2014/11/16/fun-with-machine-learning-making-sure-your-model-actually-works/
slug: fun-with-machine-learning-making-sure-your-model-actually-works
word_count: 709
---


I’m writing a talk for [PyData NYC](http://pydata.org/nyc2014/schedule/)
right now, and it’s the first talk I’ve ever written about what I do at
work.


I’ve seen a lot of “training a model with scikit-learn for beginners”
talks. They are not the talk I’m going to give. If you’ve never done any
machine learning it’s fun to realize that there are tools that you can
use to start training models really easily. I made a [tiny example of
generating some fake data and training a simple
model](http://nbviewer.ipython.org/gist/jvns/891d4b80b77fef55782a) that
you can look at.


But honestly how to use scikit-learn is not something I struggle with,
and I wanted to talk about something harder.


I want to talk about what happens after you train a model.


# How well does it work?


If you’re building a model to predict something, the first question
anyone’s going to ask you is:


**“So, how well does it work?”**


I often feel like the only thing I’ve ever learned about machine
learning is how important it is to be able to answer this question, and
how hard it is. If
you read Cathy O’Neil’s blog posts about [why models to measure teachers’ teaching are flawed](http://mathbabe.org/2014/06/16/why-chettys-value-added-model-studies-leave-me-unconvinced/),
you see this everywhere:


> we should never trust a so-called “objective mathematical model” when
> we can’t even decide on a definition of success


> If it were a good model, we’d presumably be seeing a comparison of
> current VAM scores and current other measures of teacher success and
> how they agree. But we aren’t seeing anything like that.


If your model is actually doing something important (deciding whether
teachers should lose their jobs, or how risky a stock portfolio is, or
what the weather will be tomorrow), you *have to measure if it’s
working*.


There’s no fixed answer to how to do this – if it were easy,
statisticians wouldn’t have jobs. If you looked at the notebook I linked
to, we looked at the confusion matrix for our classifier:


```
[[8953 3508]
 [3500 9039]]

```


We could have instead calculated a score (0.2, 0.8, …) for each data
point and looked at something called the ROC curve (one day maybe I will
explain how [Steven Noble](https://twitter.com/snoble) told me how to
read one of these even though I thought I understood them already)


Here’s the ROC curve for the model we just built. It’s much prettier
than a real-life ROC curve will normally be, with no jagged edges.


![](https://jvns.ca/images/roc-curve.png)


This graph shows you the tradeoffs you’re making between catching the
stuff you want (true positive rate) and dealing with the stuff you don’t
want (false positive rate). It’s a Very Useful Graph.


You might have a notion of how much money this model would save you, and
want to graph that. Or maybe you care that some data is classified
correctly more than other data, and you need to express that in some
way. Or you’re predicting the weather for sailors and you need to make
sure that really extreme weather is handled well so that nobody dies.


This also isn’t quite what I want to talk about, though! It’s more than
I feel that I can really do justice to, and I’m still learning how to
think about it slowly. Here’s what I actually want to talk about:


# How well did it work in April?


Right now it’s November. I’m working on a project that I started in
October or so. I have some metrics we’ve decided on to measure whether
the project is going well, and I want to know that it’s making progress,
and that the models we’re building now are better than they were a month
ago.


These are some questions I want to discuss in my talk:

- How do you design a system where you can look up your model’s performance from 6 months ago?
- What if you change your mind after the fact about what metrics you wish you’d measured?
- What if you use a lot of different tools to train models? (R! Python! Scala!)
- How can you make it easy to use so that people, you know, actually use it?
- And not spend a lot of time on building it.


More on this later, maybe.
