---
title: "Looking inside machine learning black boxes"
date: 2016-04-10
url: https://jvns.ca/blog/2016/04/10/why-i-dont-like-black-boxes/
slug: why-i-dont-like-black-boxes
word_count: 1745
---


I do machine learning at work. For a long time (the whole time I’ve had this job, 2 years), I’ve struggled with a bunch of questions about complicated machine learning models. Are black box models good? Should we be using them? What are the consequences? What can I do about it?


I’ve learned a few things now thanks to my coworkers who are amazing, which I’m going to try to write down here.


First, what do I mean when I say “black box model”?


The main two kinds of models I use at work are logistic regression (which I’ve written about [previously](https://jvns.ca/blog/2014/11/17/fun-with-machine-learning-logistic-regression/)) and random forests.


### simple models & complicated models


Logistic regression models have a fancy name, but they’re really **simple**. Let’s say you’re trying to model whether or not a flight will be late, and you have two inputs: number of passengers and hour of day.


Your model is then going to use `coefficient1 * # passengers + coefficient2 * hour_of_day`, and then apply the logistic function. There are just 2 coefficients! It’s so simple.


I worked for a long time with this kind of model and it was amazing in a lot of ways. You can pretty easily read off how important each input is (it got a coefficient of 0.000001? guess it wasn’t important!!). If you have a small number of inputs, like 20, then your model is 20 numbers which you can look at by hand. Easy to debug!


I’m not going to explain in depth what a random forest is here (it’s basically a collection of decision trees which you let vote on your outcome), but they’re more **complicated**. It’s not unusual for me to work with models that are tens of megabytes. You can’t read off the numbers there by hand! In fact, people often refer to a large multi-megabyte model as a “black box”, basically to say that it works well but you have no idea what it’s doing.


The same thing can happen with logistic regressions – some people use logistic regressions with millions of inputs, and then it becomes very difficult to understand what they’re doing.


Not understanding what my models are doing made me very uncomfortable.


People told me a lot “well, you have a tradeoff between interpretability and how well the model performs!”. But I didn’t feel satisfied with that. I wanted interpretability *and* a model that performs well.


### why it feels scary to have a black box


So, I had these large random forest models, and I didn’t understand what they were doing. I want to explain a few super-concrete reasons why this was bad.

- people would come to me and say “why did the model make this choice?”. Sometimes I’d be able to tell them exactly (“it picked up this super obvious signal!”), but often I would say “we don’t know exactly, it’s complicated, you know, machine learning”. They said “okay”, but I didn’t feel good about that answer.
- It was super hard to do quality assurance on the models. If you have a model making important decisions, and you don’t clearly understand what it’s doing, how do you know it’s not going to blow up in your face tomorrow? We did lots of validation in advance of putting a model into production, but what happens if the input data distribution changes? Will it blow up? Will it be fine? In general our validation held up pretty well.
- when you train a model and it doesn’t perform well, how do you know how to fix it? Is it missing features? Did you use the wrong hyperparameters? You have to sort of magically intuit why it’s not performing well. Magical intuition is Very Hard.


### looking inside a random forest (it’s easy, and it helps)


So we’ve established that I felt bad about not understanding random forest models. What do you do about it?


This is probably obvious to many people who know about random forests, but – random forests are actually a REALLY SIMPLE THING. They’re large, but they’re conceptually very simple and the algorithms you use to train them are not actually that complicated.


Let’s talk about what a random forest does. Say I have the following information about a flight:

- # passengers: 20
- time of day: 3:49pm
- % late flights in departing airport: 5%
- % late flights to arriving airport: 10%
- departing airport: Chicago


Suppose I have 10 trees in my random forest. They might classify my flight as follows. If the decision tree goes through 2 decisions: time of day > 2pm and passengers # 40, I’ll represent that as `# time of day > 2pm AND passengers < 40`.


```
         condition                              |    probability of lateness
Tree 1 | time of day > 2pm AND passengers < 40  |    10%
Tree 2 | % late flights dep airport < 70%       |    30%
Tree 3 | departing airport = chicago            |    15%
Tree 4 | passengers < 30                        |    2%
... and so on

```


I haven’t tried very hard to be realistic here – it’s likely that you’ll see conditions (or “predicates”) that are quite complicated like `passengers < 30 AND time of day < 5:20pm AND departing airport != LAX AND [ten more things]`


But what the random forest chose to assign a given probability of lateness to my flight is actually totally explainable by

- 10 conditions (one for each tree, like `time of day > 2pm AND passengers < 40`)
- and 10 probabilities (what the tree associated to that condition)


I knew this for a long time, but I honestly didn’t think it would be useful. Then one week, over a couple of days, my awesome product manager [Isaac](https://twitter.com/isaach) implemented (in javascript!!) a tool to explain to you why a random forest model made a given choice.


It was AMAZING. Right away I started putting into it choices I hadn’t understood, and I could often tell “oh, that’s why it did that! That makes sense!” or “hmm, I think its training data might have been a little off, that doesn’t seem right”. For example! Suppose it said


```
condition                                |    probability of lateness
  passengers < 30 AND time of day > 7am  |    98%

```


I… really don’t believe that flights with less than 30 passengers have a probability of lateness of 98%. `time of day > 7am` is like all flights! That’s not right at all! There must have been something wrong with the training data!


Or I might have seen this:


```
condition                                |    probability of lateness
 departing airport IN ('ORD', 'YUL', 'SFO',
                       'LHR', 'LGA')     |    10%

```


Now, maybe `ORD` (chicago) famously is extremely bad at getting flights out on time. It’s okay if one of my trees groups Chicago flights from flights with other airports, but if it’s consistently doing it? Not good! That will mean that it’ll overestimate the probability of a late flight coming out of Montreal (and underestimate it for Chicago). This is an easy thing to end up doing in scikit-learn, because even if you encode your airports as numbers (YUL=1, ORD=2, LHR=3, LGA=4, SFO=5), it’ll make its splits like `airport < 6`. You need to use a thing called “one-hot encoding” to avoid this.


So it turns out that if you just do the simplest possible thing (get the random forest to report exactly why it made the choice that it did), it’s actually surprisingly helpful in helping debug! My coworkers also report that it’s useful in helping them build their models, even if it only tells you about one instance at a time.


And it’s something that you can basically build from scratch in a few days! You can see a kind of messy example of how to print out what a scikit-learn random forest is doing in [this IPython notebook](https://github.com/jvns/forestspy/blob/afea31e545d8a8818ef502f68a5fe8bc48c1c43c/inspecting%20random%20forest%20models.ipynb).


### using machine learning as way to guide experts


I talked to someone at a conference a while ago who worked on automated trading systems, and we were talking about how machine learning approaches can be really scary because you fundamentally don’t know whether the ML is doing a thing because it’s smart and correct and better than you, or because there’s a bug in the data.


He said that they don’t use machine learning in their production systems (they don’t trust it). But they DO use machine learning! Their approach was to

- have experts hand-build a model
- have the machine learning team train a model, and show it to the experts
- the expert says “oh, yes, I see the model is doing something smart there! I will build that in to my hand-built system”


I don’t know if the this is the best thing to do, but I thought it was very interesting.


### how do you debug your machine learning models?


I was really inspired after I did this exploration of [looking inside what a neural network is doing](https://codewords.recurse.com/issues/five/why-do-neural-networks-think-a-panda-is-a-vulture) – it seems like you can get at least a little bit of interpretability out of almost any model!


There are more posts about this on the internet! Airbnb has one called [Unboxing the random forest classifier](http://nerds.airbnb.com/unboxing-the-random-forest-classifier/), Sift Science has [Large Scale Decision Forests: Lessons Learned](http://blog.siftscience.com/blog/2015/large-scale-decision-forests-lessons-learned), and this short paper called [A Model Explanation System](http://www.blackboxworkshop.org/pdf/Turner2015_MES.pdf) discusses a general system for explaining black box models (I’m actually, unusually, *very* excited about that paper)


The more I learn about machine learning, the more I think that debugging tools & a clear understanding of how the algorithms you’re using work are totally essential for making your models better (actually, I don’t understand how they *wouldn’t* be – how can you make your models better if you have no idea what they’re doing? it makes no sense to me.) I imagine the people who build amazing neural nets and things like AlphaGo have an extremely strong understanding of the foundations of how neural networks work, and some sense for how the algorithms are translating the data into choices.


As far as I can tell, scikit-learn ships with very few model debugging tools. For an example of what I mean by model debugging tools, check out [this toy notebook](https://github.com/jvns/forestspy/blob/afea31e545d8a8818ef502f68a5fe8bc48c1c43c/inspecting%20random%20forest%20models.ipynb) where I train an overfit model, investigate a specific instance of something it predicted poorly, and find out why.


I’d love to hear about what work you’re doing in explaining / debugging / untangling complex machine learning models, and especially if you’ve written anything about it.
