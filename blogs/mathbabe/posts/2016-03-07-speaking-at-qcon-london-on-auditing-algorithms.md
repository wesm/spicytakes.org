---
title: "Speaking at QCon London on auditing algorithms"
date: 2016-03-07
url: https://mathbabe.org/2016/03/07/speaking-at-qcon-london-on-auditing-algorithms/
word_count: 338
---


Today I’m flying to London to join a [the QCon conference](https://qconlondon.com/), which is for professional software folks. I’m speaking on Wednesday afternoon in the Data Science vertical, and the title for my talk is, “[How Do We Audit Algorithms?](https://qconlondon.com/presentation/how-do-we-audit-algorithms)“. They also [interviewed me for the conference](https://qconlondon.com/presentation/how-do-we-audit-algorithms).


The speaker before me is discussing the nitty gritty of [recidivism modeling](https://qconlondon.com/presentation/applied-supervised-learning-predicting-recidivism), otherwise known as algorithms that help judges and parole boards decide what to do with prisoners depending on their “risk of returning to the justice system”. Given how deeply racist and anti-poor our justice system is, it’s a big question whether or how data-driven studies or algorithms can improve it.


In other words, the need for auditing algorithms could not be more front and center given the talk before mine. So I’m going to use it as a use case.


As for how we actually do audits, I’m cobbling together stuff that is known, current research, and a long list of to-dos. A very recent paper that I’ll talk about is entitled, [Discovering Unwarranted Associations in Data-Driven Applications with the FairTest Testing Toolkit](http://arxiv.org/pdf/1510.02377v1.pdf), and it seems to contain a pretty good set of tools – written in python, no less – that can help a curious person audit a data-driven system. However, it seems to lack real tools in the case where the “protected user attributes,” are not supplied.


So, if you have a dataset showing the history of a bunch of prisoners, their recidivism scores, and their subsequent sentencing lengths, you’d like to know whether the algorithms was biased against blacks or against poor people. But if you don’t have the column “race” or “income,” it’s a lot harder to do that analysis.


Best thing you can do, besides trying to collect such data in the future, might be [something along these lines](http://files.consumerfinance.gov/f/201409_cfpb_report_proxy-methodology.pdf), where you do your best to infer race from zip codes and last names. But not all modelers even have that, so it gets tricky pretty fast.


As usual all thoughts and references are deeply appreciated.
