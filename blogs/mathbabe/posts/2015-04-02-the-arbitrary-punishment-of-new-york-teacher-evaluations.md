---
title: "The arbitrary punishment of New York teacher evaluations"
date: 2015-04-02
url: https://mathbabe.org/2015/04/02/the-arbitrary-punishment-of-new-york-teacher-evaluations/
word_count: 670
---


The Value-Added Model for teachers (VAM), currently in use all over the country, is a terrible scoring system, [as I’ve described before](https://mathbabe.org/2012/03/06/the-value-added-teacher-model-sucks/). It is approximately a random number generator.


Even so, it’s still in use, mostly because it wields power over the teacher unions. Let me explain why I say this.


Cuomo’s new budget negotiations with the teacher’s union came up with the following rules around teacher tenure, [as I understand them](http://www.capitalnewyork.com/article/albany/2015/03/8565264/outline-education-reform-proposals-budget) (readers, correct me if I’m wrong):

1. It will take at least 4 years to get tenure,
2. A teacher must get at least 3 “effective” or “highly effective” ratings in those three years,
3. A teacher’s yearly rating depends directly on their VAM score: they are not allowed to get an “effective” or “highly effective” rating if their VAM score comes out as “ineffective.”


Now, I’m ignoring everything else about the system, because I want to distill the effect of VAM.


Let’s think through the math of how likely it is that you’d be denied tenure based only on this random number generator. We will assume only that you otherwise get good ratings from your principal and outside observations. Indeed, Cuomo’s big complaint is that 98% of teachers get good ratings, so this is a safe assumption.


My analysis depends on what qualifies as an “ineffective” VAM score, i.e. what the cutoff is. For now, let’s assume that 30% of teachers receive “ineffective” in a given year, because it has to be some number. Later on we’ll see how things change if that assumption is changed.


That means that 30% of the time, a teacher will not be able to receive an “effective” score, no matter how else they behave, and no matter what their principals or outside observations report for a given year.


Think of it as a biased coin flip, and 30% of the time – for any teacher and for any year – it lands on “ineffective”, and 70% of the time it lands on “effective.” We will ignore the other categories because they don’t matter.


How about if you look over a four year period? To avoid getting any “ineffective” coin flips, you’d need to get “effective” every year, which would happen 0.70^4 = 24% of the time. In other words, 76% of the time, you’d get at least one “ineffective” rating* just by chance. *


But remember, you don’t need to get an “effective” rating for all four years, you are allowed one “ineffective rating.” [The chances of exactly one “ineffective” coin flip and three “effective” flips is](http://en.wikipedia.org/wiki/Binomial_distribution#Probability_mass_function) 4 (1-0.70) 0.70^3 =  41%.


Adding those two scenarios together, it means that 65% of the time, over a four year period, you’d get sufficient VAM scores to receive tenure. But it also means that 35% of the time you wouldn’t, through no fault of your own.


This is the political power of a terrible scoring system. More than a third of teachers are being arbitrarily chosen to be punished by this opaque and unaccountable test.


Let’s go back to my assumption, that 30% of teachers are deemed “ineffective.” Maybe I got this wrong. It directly impacts my numbers above. If the overall probability of being deemed “effective” is p, then the overall chance of getting sufficient VAM scores will be


So if I got it totally wrong, and 98% of teachers are described as effective by the VAM model, this would mean almost all teachers get sufficient VAM scores.


On the other hand, remember that the reason VAM is being pushed so hard by people is that they don’t like it when evaluations systems think too many people are effective. In fact, they’d rather see arbitrary and random evaluation than see most people get through unscathed.


In other words, it is definitely more than 2% of teachers that are called “ineffective,” but I don’t know the true cutoff.


If anyone knows the true cutoff, please tell me so I can compute anew the percentage of teachers that are arbitrarily being kept from tenure.
