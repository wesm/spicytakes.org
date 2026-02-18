---
title: "Notes from my PyData Berlin keynote"
date: 2016-05-21
url: https://jvns.ca/blog/2016/05/21/a-few-notes-from-my-pydata-berlin-keynote/
slug: a-few-notes-from-my-pydata-berlin-keynote
word_count: 435
---


I did one of the keynotes at PyData Berlin yesterday, called “How to trick a neural network”. I spent the first while talking about tricking neural networks, and then we talked about how having black box models can be dangerous, and a few strategies for making black box models more interpretable. There’s a ton of interesting work there, and here are a few links:

- if you want to understand exactly how we tricked a neural network, [Breaking Linear Classifiers on ImageNet](http://karpathy.github.io/2015/03/30/breaking-convnets/) uses exactly the same technique, but on a simpler linear classifier instead of on a neural network. In general Andrej Karpathy’s blog is great.
- [the blog post I wrote about how to trick a neural network](http://codewords.recurse.com/issues/five/why-do-neural-networks-think-a-panda-is-a-vulture)
- [the original paper I read called “Explaining and Harnessing Adversarial Examples”](http://arxiv.org/abs/1412.6572). This paper is pretty short and I found it easy to read.


some fun art projects that generate images with neural networks:

- [deep dream](http://deepdreamgenerator.com/)
- [A Neural Algorithm of Artistic Style](http://arxiv.org/abs/1508.06576) and the corresponding website [deepart.io](https://deepart.io/). Someone told me that the “artistic style” paper is actually super readable and interesting!


In general, I became more convinced at this conference that sometimes people do really cool things (like training a machine learning model to play space invaders), and those things are actually possible to reproduce for yourself if you read the paper and invest a bunch of time! I think it can often take like 2 months to fully read and understand the paper and get it to work, but it’s not impossible, which is cool.


We talked about how machine learning sometimes doesn’t work or can have unintended effects. I mentioned

- [Carina Zona: Consequences of an insightful algorithm](http://www.slideshare.net/cczona/consequences-of-an-insightful-algorithm)
- this paper by Google on building reliable production machine learning systems is great [Machine Learning: the high interest credit card of technical debt](http://research.google.com/pubs/pub43146.html)


Here are a few methods to get more interpretability out of black box machine learning models:

- this paper called [A Model Explanation System](http://www.blackboxworkshop.org/pdf/Turner2015_MES.pdf) has some really good ideas and is very short. We’ve used some of these ideas at work and it’s been helpful so far.
- someone linked me to this other model explanation system called [LIME](http://homes.cs.washington.edu/~marcotcr/blog/lime/) which I haven’t looked at yet
- a [package for scikit-learn](https://github.com/tmadl/sklearn-expertsys) that produces more interpretable results (the “Bayesian rule list” classifier)


This problem of how to make a complicated machine learning model more interpretable definitely isn’t solved, and I’d love to have more conversations about it. If you have other useful links you think I should include, let me know!


thanks to Piotr Migdal & Thomas Friedel for sending me links!
