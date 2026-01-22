---
title: "A simple mathematical model of congressional geriatric penis pumps"
date: 2014-04-22
url: https://mathbabe.org/2014/04/22/a-simple-mathematical-model-of-congressional-geriatric-penis-pumps/
word_count: 561
---


*This is a guest post written by Stephanie Yang and reposted from [her blog](http://whatdoesthequantsay.com/). Stephanie and I went to graduate school at Harvard together. She is now a quantitative analyst living in New York City, and will be joining the data science team at [Foursquare](www.foursquare.com) next month.*


Last week’s hysterical report by the Daily Show’s Samantha Bee on [federally funded penis pumps](http://thedailyshow.cc.com/videos/pvhtvo/federally-funded-penis-pumps) contained a quote which piqued our quantitative interest. Listen carefully at the 4:00 mark, when [Ilyse Hogue](http://www.thenation.com/authors/ilyse-hogue) proclaims authoritatively:


> *“Statistics show that probably some our members of congress have a vested interested in having penis pumps covered by Medicare!”*


Ilya’s wording is vague, and intentionally so. Statistically, a lot of things are “probably” true, and many details are contained in the word “probably”. In this post we present a simple statistical model to clarify what Ilya means.


First we state our assumptions. We assume that penis pumps are uniformly distributed among male Medicare recipients and that no man has received two pumps. These are relatively mild assumptions. We also assume that what Ilya refers to as “members of Congress [with] a vested interested in having penis pumps covered by Medicare,” specifically means male member of congress who received a penis pump covered by federal funds. Of course, one could argue that female members congress could also have a vested interested in penis pumps as well, but we ***do not want*** to go there.


Now the number crunching. According to the report, Medicare has spent a total of $172 million supplying penis pumps to recipients, at “360 bucks a pop.” This means a total of 478,000 penis pumps bought from 2006 to 2011.


[45% of the current 49,435,610 Medicare recipients are male](http://kff.org/medicare/state-indicator/medicare-beneficiaries-by-gender). In other words, Medicare bought one penis pump for every 46.5 eligible men. Inverting this, we can say that 2.15% of male Medicare recipients received a penis pump.


There are currently 128 members of congress (32 senators plus 96 representatives) who are males over the age of 65 and therefore Medicare-eligible. The probability that none of them received a federally funded penis pump is:


In other words, the chances of *at least one* member of congress having said penis pumps is 93.8%, which is just shy of the 95% confidence that most statisticians agree on as significant. In order to get to 95% confidence, we need a total of 138 male members of congress who are over the age of 65, and this has not happened yet as of 2014. Nevertheless, the estimate is close enough for us to agree with Ilya that there is *probably* someone member of congress who has one.


Is it possible that there two or more penis pump recipients in congress? We did notice that Ilya’s quote refers to plural members of congress. Under the assumptions laid out above, the probability of having *at least two* federally funded penis pumps in congress is:


Again, we would say this is *probably* true, though not nearly with the same amount of confidence as before. In order to reach 95% confidence that there are two or moreq congressional federally funded penis pump, we would need 200 or more Medicare-eligible males in congress, which is unlikely to happen anytime soon.


*Note: As a corollary to these calculations, I became the first developer in the history of mankind to type the following command: `git merge --squash penispump`.*
