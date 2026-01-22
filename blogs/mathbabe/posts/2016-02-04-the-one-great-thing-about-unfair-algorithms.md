---
title: "The one great thing about unfair algorithms"
date: 2016-02-04
url: https://mathbabe.org/2016/02/04/the-one-great-thing-about-unfair-algorithms/
word_count: 492
---


People who make their living writing and deploying algorithms like to boast that they are fair and objective simply because they are algorithmic and mathematical. That’s bullshit, of course.


For example, there’s [this recent Washington Post story](https://www.washingtonpost.com/news/arts-and-entertainment/wp/2016/02/02/scientists-have-discovered-the-source-of-your-resting-bitch-face/?tid=pm_lifestyle_pop_b) about an algorithm trained to detect “resting bitch face,” or RBF, which contains the following line (hat tip Simon Rose):


> FaceReader, being a piece of software and therefore immune to gender bias, proved to be the great equalizer: It detected RBF in male and female faces in equal measure. Which means that the idea of RBF as a predominantly female phenomenon has little to do with facial physiology and more to do with social norms.


While I agree that social norms have created the questions RBF phenomenon, no algorithm is going to prove that without further inquiry. For that matter, I don’t even understand how the algorithm can claim to understand neutrality of faces at all; what is their ground truth if some people look non-neutral when they are, by definition, neutral? The answer entirely depends on how the modeler creates the model, and those choices could easily contain gender bias.


So, algorithms are not by their nature fair. But sometimes their specific brand of unfairness might still be an improvement, because it’s at least measurable. Let me explain.


Take, for example, [this recent Bloomberg piece](http://www.bloomberg.com/news/articles/2016-02-03/why-hundreds-of-nearly-identical-bankruptcy-claims-yielded-vastly-different-results-in-the-aftermath-of-the-housing-bubble) on the wildly random nature of bankruptcy courts (hat tip Tom Adams). The story centers on Heritage, a Texas LLC, which bought up defaulted mortgages and sued 210 homeowners in court, winning about half. Basically that was their business plan, a bet that they’d be able to get lucky with some judges and the litigation courts because they knew how to work the system, even though in at least one case it was decided they didn’t even have standing. Here’s the breakdown:


Now imagine that this entire process was embedded in an algorithm. I’m not saying it would be automatically fair, but it would be much more *auditable* than what we currently have. It would be a black box that we could play with. We could push through a case and see what happens, and if we did that we might create a system that made more sense, or at least became more consistent. If we found that one case didn’t have standing, we might be able to dismiss all similar cases.


I’m not claiming we want everything to become an algorithm; we already have algorithmized too many things too quickly, and it’s brought us into a world where [“big data blacklisting”](http://www.floridalawreview.com/2016/margaret-hu-big-data-blacklisting/) is a thing (one big reason: the current generation of algorithms often work for people in power).


Algorithms represent decision processes that are vulnerable to inspection more than most human-led processes are. And although we are not taking advantage of this yet, we could and should do so soon. We need to start auditing our algorithms, at least the ones that are widespread and high impact.
