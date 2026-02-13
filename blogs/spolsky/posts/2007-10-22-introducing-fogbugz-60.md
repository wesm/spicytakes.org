---
title: "Introducing FogBugz 6.0"
date: 2007-10-22
url: https://www.joelonsoftware.com/2007/10/22/introducing-fogbugz-60/
word_count: 277
---


At some point, while I was running around the country giving demos of [FogBugz 6.0](http://www.fogbugz.com/), the development team officially got it out the door, and I don’t think I ever officially announced, “FogBugz 6.0 is now shipping,” so, here it is:


FogBugz 6.0 is now shipping!


It has a [ton](http://www.fogcreek.com/FogBugz/docs/60/topics/basics/Whatsnewinversion6.0.html) of major new features: an integrated Wiki, an API, a completely overhauled search engine, and lots of Ajax to make things really snappy.


Probably the most interesting part of 6.0 is [Evidence-Based Scheduling](http://www.fogcreek.com/FogBugz/learnmore.html?section=PredictShipDates), which uses a statistical technique called bootstrapping (a variation on Monte Carlo) to determine the probability that you’ll ship on any given date. EBS is interesting enough that I’ll devote a whole article to explaining it as soon as I get a minute of free time. Briefly, with EBS, you estimate features as usual. But then, instead of adding up everyone’s estimates—instead of taking them on faith—FogBugz does a Monte Carlo simulation looking at what speeds developers worked at in the past, vis-à-vis their estimates. You use that same distribution of probabilities that you had in the past and run a simulation of 60 futures each of which will occur with equal probability. What you get, instead of a date, is a probability distribution curve that shows the probability that the product will ship on such-and-such a date:


The introductory price is a terrific deal, and it’s only good until November 1st. For example, a ten-pack is only $999 instead of $1899. If you sign up for the [On Demand](http://www.fogcreek.com/FogBugz/IntrotoOnDemand.html) version, you can lock in a rate of $21/user/month instead of $25. Go make yourself a free [online trial](http://try.fogbugz.com/), what are you waiting for?
