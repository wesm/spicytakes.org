---
title: "How to fix recidivism risk models"
date: 2017-01-05
url: https://mathbabe.org/2017/01/05/how-to-fix-recidivism-risk-models/
word_count: 496
---


Yesterday [I wrote a post about the unsurprising discriminatory nature of recidivism models](https://mathbabe.org/2017/01/04/recidivism-risk-algorithms-are-inherently-discriminatory/). Today I want to add to that post with an important goal in mind: we should fix recidivism models, not trash them altogether.


The truth is, the [current justice system is fundamentally unfair](http://www.crf-usa.org/brown-v-board-50th-anniversary/the-color-of-justice.html), so throwing out algorithms because they are also unfair is not a solution. Instead, let’s improve the algorithms and then [see if judges are using them at all](https://points.datasociety.net/models-in-practice-19e68b18c340#.uo31qc8bz).


The great news is that [the paper I mentioned yesterday](http://download.springer.com/static/pdf/530/art%253A10.1007%252Fs10115-011-0463-8.pdf?originUrl=http%3A%2F%2Flink.springer.com%2Farticle%2F10.1007%2Fs10115-011-0463-8&token2=exp=1483465340~acl=%2Fstatic%2Fpdf%2F530%2Fart%25253A10.1007%25252Fs10115-011-0463-8.pdf%3ForiginUrl%3Dhttp%253A%252F%252Flink.springer.com%252Farticle%252F10.1007%252Fs10115-011-0463-8*~hmac=40acd34bc79dfb336102e58b347e57df9eefe91b8e986969f4ad8871be454258) has three methods to do just that, and in fact there are [plenty of papers](http://www.fatml.org/resources) that address this question with various approaches that get increasingly encouraging results. Here are brief descriptions of the three approaches from the paper:

1. **Massaging the training data.** In this approach the training data is adjusted so that it has less bias. In particular, the choice of classification is switched for some people in the preferred population from + to -, i.e. from the good outcome to the bad outcome, and there are similar switches for some people in the discriminated population from – to +. The paper explains how to choose these switches carefully (in the presence of continuous scorings with thresholds).
2. **Reweighing the training data.** The idea here is that with certain kinds of models, you can give weights to training data, and with a carefully chosen weighting system you can adjust for bias.
3. **Sampling the training data. **This is similar to reweighing, where the weights will be nonnegative integer values.


In all of these examples, the training data is “preprocessed” so that you can train a model on “unbiased” data, and importantly, at the time of usage, you will not need to know the status of the individual you’re scoring. This is, I understand, a legally a critical assumption, since there are anti-discrimination laws which forbid you to “consider” the race of someone when deciding whether to hire them or so on.


In other words, we’re constrained by anti-discrimination law to not use all the information that might help us avoid discrimination. This constraint, generally speaking, prevents us from doing as good a job as possible.


Remarks:

1. We might not think that we need to “remove all the discrimination.” Maybe we stratify the data by violent crime convictions first, and then within each resulting bin we work to remove discrimination.
2. We might also use the racial and class discrepancies in recidivism risk rates as an opportunity to experiment with interventions that might lower those discrepancies. In other words, why are there discrepancies, and what can we do to diminish them?
3. In other words, I do not claim that this is a trivial process. It will in fact require lots of conversations about the nature of justice and the goals of sentencing. Those are conversations we should have.
4. Moreover, there’s the question of [balancing the conflicting goals of various stakeholders](https://mathbabe.org/2016/12/20/how-do-you-quantify-morality/) which makes this an even more complicated ethical question.
