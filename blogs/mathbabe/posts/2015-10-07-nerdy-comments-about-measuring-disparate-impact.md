---
title: "Nerdy comments about measuring disparate impact"
date: 2015-10-07
url: https://mathbabe.org/2015/10/07/nerdy-comments-about-measuring-disparate-impact/
word_count: 750
---


For the past few days I’ve been contemplating how the Consumer Financial Protection Bureau (CFPB), or anyone for that matter, might attempt to measure disparate impact. This is timely because the CFPB is trying to nail auto dealers for racist practices, and an important part of those cases is measuring who should receive restitution and how much.


[As I wrote last week](https://mathbabe.org/2015/10/02/the-tricky-thing-about-disparate-impact/), the CFPB has been under fire recently for using an imperfect methodology to guess at a consumer’s race with proxy information such as zip code and surname. [Here’s their white paper](http://files.consumerfinance.gov/f/201409_cfpb_report_proxy-methodology.pdf) on it. I believe the argument between the CFPB and the bankers they’re charging with disparate impact hinges on the probability threshold they use: too high, and you get a lot of false negatives (skipping payments to minority borrowers), too low and a lot of false positives (offering money to white borrowers).


Actually, though, the issue of who is what race is only one source of uncertainty among many. Said another way, even if we had a requirement that the borrowers specify their race on their loan application forms, like they do for mortgages because of a history of redlining (so why don’t we do it for other loans too?), we’d still have plenty of other questions to deal with statistically.


Here’s a short list of those concerns, again assuming we already know the minority status of borrowers:

1. First, it has to be said that it’s difficult if not impossible to prove an individual case of racism. A given loan application might have terms that are specific to that borrower and their situation. So it is by nature a statistical thing – what terms and interest rates do the pool of minority applicants get on their loans compared to a similar pool of white applicants?
2. Now assume the care dealerships have two locations. The different locations could have different processes. Maybe one of them, location A is fairer than the other, location B. But if the statistics are pooled, the overall disparate impact will be estimated as smaller than it should be for location B but bigger for location A.
3. Of course, it could also be that different car dealers in the same location treat their customers differently, so the same thing could be happening in one location.
4. Also, over time you could see different treatment of customers. Maybe some terrible dude retires. So there’s a temporal issue to consider as well.
5. The problem is, if you try to “account” for all these things, at least in the obvious way where you cut down your data, you end up looking at a restricted location, for a restricted time window, maybe for a single car dealer, and your data becomes too thin and your error bars become too large.
6. The good thing about pooling is that you have more data and thus smaller error bars; it’s easier to make the case that disparate impact has taken place beyond a reasonable statistical doubt.
7. Then again, the way you end up doing it exactly will obviously depend on choices you make – you might end up deciding that you really need to account for location, and it gives you enough data to have reasonably small error bars, but another person making the same model decides to account for time instead. Both might be reasonable choices.
8. And so we come to the current biggest problem the CFPB is having, namely gaming between models. Because there are various models that could be used, such as I’ve described, there’s always one model that ends up costing the bank the least. They will always argue for that one, and claim the CFPB is using the wrong model with “overestimates” the disparate impact.
9. They even have an expert consultant who works both for the CFPB and the banks and helps them game the models in this way.


For this reason, I’d suggest we have some standards for measuring disparate impact, so that the “gaming between models” comes to an end. Sure, the model you end up choosing won’t be perfect, and it might be itself gameable, but I’m guessing the extent of gaming will be smaller overall. And, going back to the model which guesses at someone’s minority status, I think the CFPB needs to come up with a standard threshold for that, and for the same reason: not because it’s perfect, but because it will prevent banks from complaining that other banks get treated better.
