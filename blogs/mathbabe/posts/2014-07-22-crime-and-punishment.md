---
title: "Crime and punishment"
date: 2014-07-22
url: https://mathbabe.org/2014/07/22/crime-and-punishment/
word_count: 858
---


When I was prepping for my [Slate Money podcast](http://www.slate.com/articles/podcasts/slate_money.html) last week I read [this column by Matt Levine at Bloomberg](http://www.bloombergview.com/articles/2014-07-14/citigroup-mortgage-trader-sent-a-7-billion-e-mail) on the Citigroup settlement. In it he raises the important question of how the fine amount of $7 billion was determined. Here’s the key part:


> Citi’s and the Justice Department’s approaches both leave something to be desired. Citi’s approach seems to be premised on the idea that the misconduct was *securitizing mortgages**:* The more mortgages you did, the more you gotta pay, regardless of how they performed. The DOJ’s approach, on the other hand, seems to be premised on the idea that the misconduct was *sending bad e-mails about mortgages: *The more “culpable” you look, the more it should cost you, regardless of how much damage you did.
> I [would have thought](http://www.bloombergview.com/articles/2013-11-19/jpmorgan-s-mortgage-confessions-don-t-include-o-j-simpson) that the misconduct was *knowingly securitizing bad mortgages*, and that the penalties ought to scale with the aggregate badness of Citi’s mortgages. So, for instance, you’d want to measure how often Citi’s mortgages didn’t match up to its stated quality-control standards, and then compare the actual financial performance of the loans that didn’t meet the standards to the performance of the loans that did. Then you could say, well, if Citi had lived up to its promises, investors would have lost $X billion less than they actually did. And then you could fine Citi that amount, or some percentage of that amount. And you could do a similar exercise for the other big banks — JPMorgan, say, which already settled, or Bank of America, which is negotiating its settlement — and get comparable amounts that appropriately balance market share (how many bad mortgages did you sell?) and culpability (how bad were they?).


I think he nailed something here, which has eluded me in the past, namely the concept of what comprises evidence of wrongdoing and how that translates into punishment. It’s similar to what I talked about in [this recent post](https://mathbabe.org/2014/07/07/what-constitutes-evidence/), where I questioned what it means to provide evidence of something, especially when the data you are looking for to gather evidence has been deliberately suppressed by either the people committing wrongdoing or by other people who are somehow gaining from that wrongdoing but are not directly involved.


Basically the way I see Levine’s argument is that the Department of Justice used a *lawyerly definition* of evidence of wrongdoing – namely, through the existence of emails saying things like “it’s time to pray.” After determining that they were in fact culpable, they basically did some straight-up negotiation to determine the fee. That negotiation was either purely political or was based on information that has been suppressed, because as far as anyone knows the number was kind of arbitrary.


Levine was suggesting a more *quantitative definition* for evidence of wrongdoing, which involves estimating both “how much you know” and “how much damage you actually did” to determine the damage, and then some fixed transformation of that damage becomes the final fee. I will ignore Citi’s lawyers’ approach since their definition was entirely self-serving.


Here’s the thing, there are problems with both approaches. For example, with the lawyerly approach, you are basically just sending the message that* you should never ever write some things on email*, and most or at least many people know that by now. In other words, you are training people to game the system, and if they game it well enough, they won’t get in trouble. Of course, given that this was yet another fine and nobody went to jail, you could make the argument – and I did on the podcast – that nobody got in trouble anyway.


The problem with the quantitative approach, is that first of all you still need to estimate “how much you knew” which again often goes back to emails, although in this case could be estimated by how often the stated standards were breached, and second of all, when taken as a model, can be embedded into the overall trading model of securities.


In other words, if I’m a quant at a nasty place that wants to trade in toxic securities, and I know that there’s a chance I’d be caught but I know the formula for how much I’d have to pay if I got caught, then I could include this cost, in addition to an estimate of the likelihood for getting caught, in an optimization engine to determine exactly how many toxic securities I should sell.


To avoid this scenario, it makes sense to have an element of randomness in the punishments for getting caught. Every now and then the punishment should be much larger than the quantitative model might suggest, so that there is less of a chance that people can incorporate the whole shebang into their optimization procedure. So maybe what I’m saying is that arriving at a random number, like the DOJ did, is probably better even though it is less satisfying.


Another possibility to actually deter crimes would be to arbitrarily increasing the likelihood of catching people up to no good, but that has been bounded from above by the way the SEC and the DOJ actually work.
