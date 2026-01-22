---
title: "How do you quantify morality?"
date: 2016-12-20
url: https://mathbabe.org/2016/12/20/how-do-you-quantify-morality/
word_count: 473
---


Lately I’ve been thinking about technical approaches to measuring, monitoring, and addressing discrimination in algorithms.


To do this, I consider the different stakeholders and the relative harm they will suffer depending on mistakes made by the algorithm. It turns out that’s a really robust approach, and one that’s basically unavoidable. Here are three examples to explain what I mean.

1. [AURA is an algorithm](http://www.scpr.org/news/2015/01/13/49191/can-an-algorithm-predict-child-abuse-la-county-chi/) that is being implemented in Los Angeles with the goal of finding child abuse victims. Here the stakeholders are the children and the parents, and the relative harm we need to quantify is the possibility of taking a child away from parents who would not have abused that kid (bad) versus not removing a child from a family that does abuse them (also bad). I claim that, unless we decide on the relative size of those two harms – so, if you assign “unit harm” to the first, then you have to decide what the second harm counts as – and then optimize to it using that ratio in the penalty function, then you cannot really claim you’ve created a moral algorithm. Or, to be more precise, you cannot say you’ve implemented an algorithm in line with a moral decision. Note, for example, that arguments [like this](https://www.datainnovation.org/2016/02/why-are-child-welfare-advocates-sabotaging-data-driven-efforts-to-protect-children/) are making the assumption that the ratio is either 0 or infinity, i.e. that one harm matters but the other does not.
2. COMPAS is a well-known algorithm that measures recidivism risk, i.e. the risk that a given person will end up back in prison within two years of leaving it. Here the stakeholders are the police and civil rights groups, and the harms we need to measure against each other are the possibility of a criminal going free and committing another crime versus a person being jailed in spite of the fact that they would not have gone on to commit another crime. ProPublica has been going head to head with COMPAS’s maker, Northpointe, but unfortunately, the relative weight of these two harms is being sidestepped both by [one side](https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing) and [the other](https://www.propublica.org/article/technical-response-to-northpointe).
3. Michigan recently acknowledged its [automated unemployment insurance fraud detection system, called Midas, was going nuts](https://www.theguardian.com/us-news/2016/dec/18/michigan-unemployment-agency-fraud-accusations), accusing upwards of 20,000 innocent people of fraud while filling its coffers with (mostly unwarranted) fines, which it’s now using to balance the state budget. In other words, the program deeply undercounted the harm of charging an innocent person with fraud while it was likely overly concerned with missing out on a fraud fine payment that it deserved. Also it was probably just a bad program.


If we want to build ethical algorithms, we will need to weight harms against each other and quantify their relative weights. That’s a moral decision, and it’s hard to agree on. Only after we have that difficult conversation can we optimize our algorithms to those choices.
