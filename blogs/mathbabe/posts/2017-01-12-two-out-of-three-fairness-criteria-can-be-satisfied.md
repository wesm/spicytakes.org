---
title: "Two out of three “fairness” criteria can be satisfied"
date: 2017-01-12
url: https://mathbabe.org/2017/01/12/two-out-of-three-fairness-criteria-can-be-satisfied/
word_count: 607
---


This is a continuation of a discussion I’ve been having with myself about the various definition of fairness in scoring systems. Yesterday I mentioned a recent paper entitled *[Inherent Trade-Offs in the Fair Determination of Risk Scores](https://arxiv.org/pdf/1609.05807v2.pdf) *that has a proof of the following statement:


> You cannot simultaneously ask for a model to be well-calibrated, to have equal false positive rates for blacks and whites, and to have equal false negative rates unless you are in the presence of equal “base rates” or a perfect predictor.


The good news is that you can ask for two out of three of these. Here’s a picture of a specific example of this, where I’ve simplified the situation so there are two groups of people being scores, B and W, and they each can be scored as either empty or full, and then the reality is that could either be empty or full. They have different “base rates,” which is to say that in reality, a different proportion of the B group is empty (70%) than the W group (50%). We insist, moreover, that the labeling scheme is “well-calibrated”, so the right proportion of them are labeled empty or full. I’ve drawn 10 “perfect representatives” from each group here:


In my picture, I’ve assumed there was some mislabeling – there’s a full in the empty bin and there are empties in the full bin. Because we are assuming the model is well-calibrated, every time we have one kind of mistake we have to make up for that mistake with exactly one of the other type. In the picture there’s exactly one of each mistake for both the W group and the B group, so that’s fine.


Quick calculation: in the picture above, the “false full rate”, which we can think of as the “false positive rate,” for B is 1/3 = 33% but the “false positive rate” for W is 1/5 = 20%, even though they each have only one mislabeled representative each.


Now it’s obvious that, theoretically, the scoring system could adjust the false positive rate for B to match that of W, which would mean having 3/5 of a representative be mislabeled. But again, that’d mean we would need only 3/5 of a representative be mislabeled in the empty bin as well.


That’s a false negative rate for B of 3/35 = 8.6% (note it used to be 1/7 = 14.3%). By contrast the false negative rate for A stays fixed at 1/5 = 20%.


If you think about it, what we’ve done is sacrificed some false negative rate balance for a perfect match on the false positive rate, while keeping the model well-calibrated.


Applying this to recidivism scores, we can ask for the high scores to reflect base rates for the populations, and we can ask for similar false positive rates for populations, but we cannot also ask for false negative rates to be equal. That might be better overall, though, because the harm that comes from unequal false positive rate – sending someone to jail for longer – is arguably more toxic than an unequal false negative rate, which means certain groups are let off the hook more often than the others.


By the way, I want to be clear that I don’t think recidivism risk algorithms should actually be the goal, summed up in [this conversation](https://mathbabe.org/2017/01/11/two-clarifications/#comment-93405) I had with Tom Slee. I’m not even sure why their use is constitutional, to tell the truth. But given that they are in use, I think it makes sense to try to make them as good as possible, and to investigate what “good” means in this context.
