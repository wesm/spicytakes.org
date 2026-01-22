---
title: "Two clarifications"
date: 2017-01-11
url: https://mathbabe.org/2017/01/11/two-clarifications/
word_count: 453
---


First, I think [I over-reacted to automated pricing](https://mathbabe.org/2017/01/09/algorithmic-collusion-and-price-fixing/) models (thanks to my buddy Ernie Davis who made me think harder about this). I don’t think immediate reaction to price changes is necessarily odious. I do think it changes the dynamics of price optimization in weird ways, but upon reflection I don’t see how they’d necessarily be bad for the general consumer besides the fact that Amazon will sometimes have weird disruptions much like the flash crashes we’ve gotten used to on Wall Street.


Also, in terms of the question of “accuracy versus discrimination,” I’ve now read [the research paper](https://arxiv.org/pdf/1609.05807v2.pdf) that I believe is under consideration, and it’s more nuanced than [my recent ](https://mathbabe.org/2017/01/04/recidivism-risk-algorithms-are-inherently-discriminatory/)[blog posts](https://mathbabe.org/2017/01/05/how-to-fix-recidivism-risk-models/) would suggest (thanks to Solon Barocas for help on this one).


In particular, the [2011 paper I referred defines discrimination](http://link.springer.com/article/10.1007/s10115-011-0463-8) crudely, whereas this new article allows for different “base rates” of recidivism. To see the different, consider a model that assigns a high risk score 70% of the time to blacks and 50% to whites. Assume that, as a group, blacks recidivate at a 70% rate and whites at a 50% rate. The article I referred to would define this as discriminatory, but the newer paper refers to this as “well calibrated.”


Then the question the article tackles is, can you simultaneously ask for a model to be well-calibrated, to have equal false positive rates for blacks and whites, and to have equal false negative rates? The answer is no, at least not unless you are in the presence of equal “base rates” or a perfect predictor.


Some comments:

1. This is still unsurprising. The three above conditions are mathematical constraints, and there’s no reason to expect that you can simultaneously require a bunch of really different constraints. The authors do the math and show that intuition is correct.
2. Many of my comments still hold. The most important one is the question of why the base rates for blacks and whites are so different. If it’s because of police practice, at least in part, or overall increased surveillance of black communities, then I’d argue “well-calibrated” is insufficient.
3. We need to be putting the science into data science and examining questions like this. In other words, we cannot assume the data is somehow fixed in stone. All of this is a social construct.


This question has real urgency, by the way. [New York Governor Cuomo announced yesterday the introduction of recidivism risk scoring systems to modernize bail hearings](https://www.governor.ny.gov/news/governor-cuomo-presents-12th-proposal-2017-state-state-agenda-launching-new-york-promise-agenda). This could be great if fewer people waste time in jail pending their hearings or trials, but if the people chosen to stay in prison are chosen on the basis that they’re poor or minority or both, that’s a problem.
