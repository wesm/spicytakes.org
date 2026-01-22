---
title: "Should lawmakers use algorithms?"
date: 2013-08-05
url: https://mathbabe.org/2013/08/05/should-lawmakers-use-algorithms/
word_count: 1013
---


Here is an idea I’ve been hearing floating around the big data/ tech community: the idea of having algorithms embedded into law.


The argument for is pretty convincing on its face: Google has gotten its algorithms to work better and better over time by optimizing correctly and using tons of data. To some extent we can think of their business strategies and rules as a kind of “internal regulation”. So why don’t we take a page out of that book and improve our laws and specifically our regulations with constant feedback loops and big data?


**No algos in law**


There are some concerns I have right off the bat about this concept, putting aside the hugely self-serving dimension of it.


First of all, we would be adding opacity – of the mathematical modeling kind – to an already opaque system of law. It’s hard enough to read the legalese in a credit card contract without there also being a black box algorithm to make it impossible.


Second of all, whereas the incentives in Google are often aligned with the algorithm “working better”, whatever that means in any given case, the incentives of the people who write laws often aren’t.


So, for example, [financial regulation is largely written by lobbyists](http://news.firedoglake.com/2013/05/27/wall-street-lobbyists-literally-writing-bills-in-congress/). If you gave them a new tool, that of adding black box algorithms, then you could be sure they would use it to further obfuscate what is already a hopelessly complicated set of rules, and on top of it they’d be sure to measure the wrong thing and optimize to something random that would not interfere with their main goal of making big bets.


Right now lobbyists are used so heavily in part because they understand the complexity of their industries more than the lawmakers themselves. In other words, they actually add value in a certain way (besides in the monetary way). Adding black boxes would emphasize this asymmetric information problem, which is a terrible idea.


Third, I’m worried about the “black box” part of algorithms. There’s a strange assumption among modelers that you have to make algorithms secret or else people will game them. But [as I’ve said before](https://mathbabe.org/2012/02/03/let-them-game-the-model/), if people can game your model, that just means your model sucks, and specifically that your proxies are not truly behavior-based.


So if it pertains to a law against shoplifting, say, you can’t have an embedded model which uses the proxy of “looking furtive and having bulges in your clothes.” You actually need to have proof that someone stole something.


If you think about that example for a moment, it’s absolutely not appropriate to use poor proxies in law, nor is it appropriate to have black boxes at all – we should all know what our laws are. This is true for regulation as well, since it’s after all still law which affects how people are expected to behave.


And by the way, what counts as a black box is to some extent in the eye of the beholder. It wouldn’t be enough to have the source code available, since that’s only accessible to a very small subset of the population.


Instead, anyone who is under the expectation of following a law should also be able to read and understand the law. That’s why the CFPB is trying to make credit card contracts be written in Plain English. Similarly, regulation law should be written in a way so that the employees of the regulator in question can understand it, and that means you shouldn’t have to have a Ph.D. in a quantitative field and know python.


**Algos as tools**


Here’s where algorithms may help, although it is still tricky: not in the law itself but in the implementation of the law. So it makes sense that the SEC has algorithms trying to catch insider trading – in fact it’s probably the *only* way for them to attempt to catch the bad guys. For that matter they should have many more algorithms to catch other kinds of bad guys, for example to catch people with suspicious accounting or consistently optimistic ratings.


In this case proxies are reasonable, but on the other hand it doesn’t translate into law but rather into a ranking of workflow for the people at the regulatory agency. In other words the SEC should use algorithms to decide which cases to pursue and on what timeframe.


Even so, there are plenty of reasons to worry. One could view the “Stop & Frisk” strategy in New York as following an algorithm as well, namely to stop young men in high-crime areas that have “furtive motions”. This algorithm happens to single out many innocent black and latino men.


Similarly, some of the highly touted New York City open data projects amount to figuring out that if you focus on looking for building code violations in high-crime areas, [then you get a better hit rate](http://www.slate.com/articles/technology/future_tense/2013/03/big_data_excerpt_how_mike_flowers_revolutionized_new_york_s_building_inspections.single.html). Again, the consequence of using the algorithm is that poor people are targeted at a higher rate for all sorts of crimes (key quote from the article: “causation is for other people”).


Think about this asymptotically: if you live in a nice neighborhood, the limited police force and inspection agencies never check you out since their algorithms have decided the probability of bad stuff happening is too low to bother. If, on the other hand, you are poor and live in a high-crime area, you get checked out daily by various inspectors, who bust you for whatever.


Said this way, it kind of makes sense that white kids smoke pot at the same rate as black kids but are [almost never busted for it](http://www.huffingtonpost.com/2013/06/03/racial-disparity-in-marijuana-arrests_n_3381725.html).


There are ways to partly combat this problem, [as I’ve described before](https://mathbabe.org/2011/12/27/is-stop-question-and-frisk-racist/), by using randomization.


**Conclusion**


It seems to me that we can’t have algorithms directly embedded in laws, because of the highly opaque nature of them together with commonly misaligned incentives. They might be useful as tools for regulators, but the regulators who choose to use internal algorithms need to carefully check that their algorithms don’t have unreasonable and biased consequences, which is really hard.
