---
title: "Auditing Algorithms"
date: 2016-07-22
url: https://mathbabe.org/2016/07/22/auditing-algorithms/
word_count: 366
---


Big news!


I’ve started a company called [ORCAA](https://oneilrisk.com/), which stands for O’Neil Risk Consulting and Algorithmic Auditing and is pronounced “orcaaaaaa”. ORCAA will audit algorithms and conduct risk assessments for algorithms, first as a consulting entity and eventually, if all goes well, as a more formal auditing firm, with open methodologies and toolkits.


So far all I’ve got is a [webpage](http://oneilrisk.com) and a legal filing (as an [S-Corp](https://en.wikipedia.org/wiki/S_corporation)), but no clients.


No worries! I’m busy learning everything I can about the field, small though it is. Today, for example, my friend [Suresh Naidu](http://tuvalu.santafe.edu/~snaidu/) suggested I read [this fascinating study](http://siteresources.worldbank.org/INTPAH/Resources/Publications/459843-1195594469249/HealthEquityCh12.pdf), referred to by those in the know as “Oaxaca’s decomposition,” which separates differences of health outcomes for two groups – referred to as “the poor” and the “nonpoor” in the paper – into two parts: first, the effect of “worse attributes” for the poor, and second, the effect of “worse coefficients.” There’s also a worked-out example of children’s health in Viet Nam which is interesting.


The specific formulas they use depends crucially on the fact that the underlying model is a linear regression, but the idea doesn’t: in practice, we care about both issues. For example, with credit scores, it’s obvious we’d care about the coefficients – the coefficients are the ingredients in the recipe that takes the input and gives the output, so if they fundamentally discriminate against blacks, for example, that would be bad (but it has to be carefully defined!). At the same time, though, we also care about which inputs we choose in the first place, which is why there are laws about not being able to use race or gender in credit scoring.


And, importantly, this analysis won’t necessarily tell us what to do about the differences we pick up. Indeed many of the tests I’ve been learning about and studying have that same limitation: we can detect problems but we don’t learn how to address them.


If you have any suggestions for me on methods for either auditing algorithms or for how to modify problematic algorithms, I’d be very grateful if you’d share them with me.


Also, if there are any artists out there, I’m on the market for a logo.
