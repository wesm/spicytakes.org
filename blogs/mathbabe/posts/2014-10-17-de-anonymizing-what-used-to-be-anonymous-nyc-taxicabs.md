---
title: "De-anonymizing what used to be anonymous: NYC taxicabs"
date: 2014-10-17
url: https://mathbabe.org/2014/10/17/de-anonymizing-what-used-to-be-anonymous-nyc-taxicabs/
word_count: 442
---


Thanks to [Artem Kaznatcheev](https://egtheory.wordpress.com/author/kaznatcheev/), I learned yesterday about [the recent work](http://research.neustar.biz/2014/09/15/riding-with-the-stars-passenger-privacy-in-the-nyc-taxicab-dataset/) of [Anthony Tockar](http://www.analytics.northwestern.edu/current-students/2014-profiles/tockar-anthony.html) in exploring the field of [anonymization](http://en.wikipedia.org/wiki/Data_anonymization) and [deanonymization](http://en.wikipedia.org/wiki/De-anonymization) of datasets.


Specifically, he [looked at the 2013 cab rides in New York City](http://research.neustar.biz/2014/09/15/riding-with-the-stars-passenger-privacy-in-the-nyc-taxicab-dataset/), which was provided under a FOIL request, and he stalked celebrities Bradley Cooper and Jessica Alba (and discovered that neither of them tipped the cabby). He also stalked a man who went to a slew of NYC titty bars: found out where the guy lived and even got a picture of him.


Previously, [some other civic hackers had identified the cabbies themselves](https://medium.com/@vijayp/of-taxis-and-rainbows-f6bc289679a1), because the original dataset had scrambled the medallions, but not very well.


The point he was trying to make was that we should not assume that “anonymized” datasets actually protect privacy. Instead we should learn how to use more thoughtful approaches to anonymizing stuff, and he proposes a method called “differential privacy,” which he explains [here](http://research.neustar.biz/2014/09/08/differential-privacy-the-basics/). It involves adding noise to the data, in a certain way, so that at the end any given person doesn’t risk too much of their own privacy by being included in the dataset versus being not included in the dataset.


Bottomline, it’s actually pretty involved mathematically, and although I’m a nerd and it doesn’t intimidate me, it does give me pause. Here are a few concerns:

1. It means that most people, for example the person in charge of fulfilling FOIL requests, will not actually understand the algorithm.
2. That means that, if there’s a requirement that such a procedure is used, that person will have to use and trust a third party to implement it. This leads to all sorts of problems in itself.
3. Just to name one, depending on what kind of data it is, you have to implement differential privacy differently. There’s no doubt that a complicated mapping of datatype to methodology will be screwed up when the person doing it doesn’t understand the nuances.
4. Here’s another: the third party may not be trustworthy and may have created a backdoor.
5. Or they just might get it wrong, or do something lazy that doesn’t actually work, and they can get away with it because, again, the user is not an expert and cannot accurately evaluate their work.


Altogether I’m imagining that this is at best an expensive solution for very important datasets, and won’t be used for your everyday FOIL requests like taxicab rides unless the culture around privacy changes dramatically.


Even so, super interesting and important work by Anthony Tockar. Also, if you think that’s cool, take a look at my friend [Luis Daniel](http://luisdaniel.com/)‘s work on [de-anonymizing the Stop & Frisk data](http://blog.luisdaniel.com/de-anonymizing-stop-and-frisk-data/).
