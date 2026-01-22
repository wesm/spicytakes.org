---
title: "The Models Were Telling Us Trump Could Win"
date: 2016-11-11
url: https://mathbabe.org/2016/11/11/the-models-were-telling-us-trump-could-win/
word_count: 778
---


*This is a post by Eugene Stern, originally posted on his blog [sensemadehere.wordpress.com](https://sensemadehere.wordpress.com/).*


Nate Silver got the election right.


Modeling this election was never about win probabilities (i.e., saying that Clinton is 98% likely to win, or 71% likely to win, or whatever). It was about finding a way to convey meaningful information about uncertainty and about what could happen. And, despite the not-so-great headline, [this article](http://fivethirtyeight.com/features/final-election-update-theres-a-wide-range-of-outcomes-and-most-of-them-come-up-clinton/) by Nate Silver does a pretty impressive job.


First, let’s have a look at what not to do. [This article](http://election.princeton.edu/2016/11/06/is-99-a-reasonable-probability/) by Sam Wang (Princeton Election Consortium) explains how you end up with a win probability of 98-99% for Clinton. First, he aggregates the state polls, and figures that if they’re right on average, then Clinton wins easily (with over 300 electoral votes I believe). Then he looks for a way to model the uncertainty. He asks, reasonably: what happens if the polls are all off by a given amount? And he answers the question, again reasonably: if Trump overperforms his polls by 2.6%, the election becomes a toss-up. If he overperforms by more, he’s likely to win.


But then you have to ask: how much *could* the polls be off by? And this is where Wang goes horribly wrong.


The uncertainty here is virtually impossible to model statistically. US presidential elections don’t happen that often, so there’s not much direct history, plus the challenges of polling are changing dramatically as fewer and fewer people are reachable via listed phone numbers. Wang does say that in the last three elections, the polls have been off by 1.3% (Bush 2004), 1.2% (Obama 2008), and 2.3% (Obama 2012). So polls being off by 2.6% doesn’t seem crazy at all.


For some inexplicable reason, however, Wang ignores what is right in front of his nose, picks a tiny standard error parameter out of the air, plugs it into his model, and basically says: well, the polls are very unlikely to be off by very much, so Clinton is 98-99% likely to win.


*Always be wary of models, especially models of human behavior, that give probabilities of 98-99%. Always ask yourself: am I anywhere near 98-99% sure that my model is complete and accurate? If not, STOP, cross out your probabilities because they are meaningless, and start again*.


How do you come up with a meaningful forecast, though? Once you accept that there’s genuine uncertainty in the most important parameter in your model, and that trying to assign a probability is likely to range from meaningless to flat-out wrong, how do you proceed?


Well, let’s look at what Silver does in [this article](http://fivethirtyeight.com/features/final-election-update-theres-a-wide-range-of-outcomes-and-most-of-them-come-up-clinton/). Instead of trying to estimate the volatility as Wang does (and as Silver also does on the front page of his web site, people just can’t help themselves), he gives a careful analysis of some possible *specific scenarios*. What are some good scenarios to pick? Well, maybe we should look at recent cases of when nationwide polls have been off. OK, can you think of any good examples? Hmm, I don’t know, maybe…


Aiiieeee!!!!


Look at the numbers in that Sun cover. Brexit (Leave) won by 4%, while the polls before the election were essentially [tied](https://elections.huffingtonpost.com/pollster/uk-european-union-referendum), with Remain perhaps enjoying a slight lead. That’s a polling error of at least 4%. And the US poll numbers are very clear: if Trump overperforms his polls by 4%, he wins easily.


In financial modeling, where you often don’t have enough relevant history to build a good probabilistic model, this technique — pick some scenarios that seem important, play them through your model, and look at the outcomes — is called *stress testing*. Silver’s article does a really, really good job of it. He doesn’t pretend to know what’s going to happen (we can’t all be [Michael Moore](http://michaelmoore.com/trumpwillwin/), you know), but he plays out the possibilities, makes the risks transparent, and puts you in a position to evaluate them. *That* is how you’re supposed to analyze situations with inherent uncertainty. And with the inherent uncertainty in our world increasing, to say the least, it’s a way of thinking that we all better start becoming really familiar with.


The models were plain as day. What the numbers were telling us was that if the polls were right, Clinton would win easily, but if they were underestimating Trump’s support by anywhere near a Brexit-like margin, Trump would win easily. Shouldn’t *that* have been the headline? Wouldn’t you have liked to have known that? Isn’t it way more informative than saying that Clinton is 98% or 71% likely to win based on some parameter someone plucked out of thin air?


We should have been going into this election terrified.
