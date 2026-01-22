---
title: "ProPublica report: recidivism risk models are racist"
date: 2016-05-24
url: https://mathbabe.org/2016/05/24/propublica-report-recidivism-risk-models-are-racist/
word_count: 713
---


Yesterday an exciting ProPublica article entitled *[Machine Bias](https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing)* came out. Written by Julia Angwin, [author of Dragnet Nation](https://mathbabe.org/2014/03/14/julia-angwins-dragnet-nation/), and Jeff Larson, [data journalist extraordinaire](https://mathbabe.org/2014/08/22/jeff-larson-kills-it-at-the-lede-program/), the piece explains in human terms what it looks like when algorithms are biased.


Specifically, they looked into a class of models I featured in my upcoming book, Weapons of Math Destruction, called “recidivism risk” scoring models. These models score defendants and give those scores to judges to help them decide how long to sentence them to prison, for example. Higher scores of recidivism are supposed to correlate to a higher likelihood of returning to prison, and people who have been assigned high scores also tend to get sentenced to longer prison terms.


**What They Found**


Angwin and Larson studied the recidivism risk model called COMPAS. Starting with COMPAS scores for 10,000 criminal defendants in Broward County, Florida, they looked at the  difference between who was predicted to get rearrested by COMPAS versus who actually did. This was a direct test of the accuracy of the risk model. The highlights of their results:

- Black defendants were often predicted to be at a higher risk of recidivism than they actually were. Our analysis found that black defendants who did not recidivate over a two-year period were nearly twice as likely to be misclassified as higher risk compared to their white counterparts (45 percent vs. 23 percent).
- White defendants were often predicted to be less risky than they were. Our analysis found that white defendants who re-offended within the next two years were mistakenly labeled low risk almost twice as often as black re-offenders (48 percent vs. 28 percent).
- The analysis also showed that even when controlling for prior crimes, future recidivism, age, and gender, black defendants were 45 percent more likely to be assigned higher risk scores than white defendants.
- Black defendants were also twice as likely as white defendants to be misclassified as being a higher risk of violent recidivism. And white violent recidivists were 63 percent more likely to have been misclassified as a low risk of violent recidivism, compared with black violent recidivists.
- The violent recidivism analysis also showed that even when controlling for prior crimes, future recidivism, age, and gender, black defendants were 77 percent more likely to be assigned higher risk scores than white defendants.


Here’s one of their charts (lower scores mean low-risk):


**How They Found It**


ProPublica is awesome and has the highest standards in data journalism. Which is to say, they [published their methodology](https://www.propublica.org/article/how-we-analyzed-the-compas-recidivism-algorithm), including a description of the (paltry) history of other studies that looked into racial differences for recidivism risk scoring methods. They even have [the data and the ipython notebook they used for their analysis on github](https://github.com/propublica/compas-analysis).


They made heavy use of the open records law in Florida to do their research, including the original scores, the subsequent arrest records, and the classification of each person’s race. That data allowed them to build their analysis. They tracked both “recidivism” and “violent recidivism” and tracked both the original scores and the error rates. [Take a look.](https://www.propublica.org/article/how-we-analyzed-the-compas-recidivism-algorithm)


**How Important Is This?**


This is a triumph for the community of people (like me!) who have been worrying about exactly this kind of thing but who haven’t had hard proof until now. In my book I made multiple arguments for why we should expect this exact result for recidivism risk models, but I didn’t have a report to point to. So, in that sense, it’s extremely useful.


More broadly, it sets the standard for how to do this analysis. The transparency involved is hugely important, because nobody will be able to say they don’t know how these statistics were computed. They are basic questions by which every recidivism risk model should be measured.


**What’s Next?**


Until now, recidivism risk models have been deployed naively, in judicial systems all across the country, and judges in those systems have been presented with such scores as if they are inherently “fair.”


But now, people deploying these models – and by people I mostly mean Department of Corrections decision-makers – will have pressure to make sure the models are audited for racism before using them. And they can do this kind of analysis in-house with much less work. I hope they do.
