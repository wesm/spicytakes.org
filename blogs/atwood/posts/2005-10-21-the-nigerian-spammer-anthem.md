---
title: "The Nigerian Spammer Anthem"
date: 2005-10-21
url: https://blog.codinghorror.com/the-nigerian-spammer-anthem/
slug: the-nigerian-spammer-anthem
word_count: 764
---

A [recent Los Angeles Times article](https://www.latimes.com/la-fg-scammers20oct20-story.html) reveals that the [419 scam spammers](http://www.snopes.com/crime/fraud/nigeria.asp) have their very own anthem: a song titled *I Go Chop Your Dollars* by Nigerian recording artist Osofia:


> “419 is just a game, you are the losers, we are the winners.
> White people are greedy, I can say they are greedy
> White men, I will eat your dollars, will take your money and disappear.
> 419 is just a game, we are the masters, you are the losers.”


We may [joke about the 419 scams](http://j-walk.com/other/conf/)... after all, who in their right mind actually falls for [this stuff](https://www.snopes.com/2004/10/07/son-of-spam/)? But like all spammers, **they do it because it works**:


> [Samuel] sent 500 e-mails a day and usually received about seven replies. Shepherd would then take over. “When you get a reply, it’s 70% sure that you’ll get the money,” Samuel said.


Spam only became a problem for me about a year and a half ago, but clearly it’s here to stay. I’ve [used POPFile](https://blog.codinghorror.com/some-plans-for-spam/) for about a year to cut down on my email spam.** Some people swear by **challenge-response human verification systems **such as SpamArrest, but as Scott Mitchell notes, [this system has some issues](https://web.archive.org/web/20051029212413/http://scottonwriting.net/sowblog/posts/647.aspx):

kg-card-begin: html

> While the challenge/response system was effective in reducing my spam intake from about 100 messages a day to around 1 or 2 messages a day, the approach, in my estimation, was not ideal. One big disadvantage was that fewer people took the time to respond to the challenge email than I had anticipated, for two reasons:
> Some people don’t want to take the time to follow instructions for a challenge email. Maybe their message wasn’t that important after all, maybe they’re busy, or maybe they just don’t like being told what to do. These people’s messages, I reckoned, weren’t that vital. If you can’t take two seconds to respond to the challenge, then just how important is that email you’re sending me?
> What worried me most, and led me to suspend my C/R anti-spam system, is that I noticed some people weren’t responding to the challenge email because they never received it! This unfortunate circumstance could happen if their own spam blocking solution halted my challenge email. A couple folks informed me that Outlook 2003 categorized my challenge emails as spam. Others using a similar challenge/response anti-spam system would never get my challenge as my challenge would generate a challenge on their side.

kg-card-end: html

The “I challenge your challenge!” scenario is particularly amusing. And on top of the two issues Scott highlights, there are other social problems with [challenge/response spam blocking](https://blog.codinghorror.com/popfile-vs-popfile/).


Although I’ve had great success with [POPFile](http://popfile.sourceforge.net/), which uses Bayesian filtering techniques, I had no idea that there’s an even better technique: Markovian filtering. That’s what [the CRM114 Discriminator](http://crm114.sourceforge.net/)* uses. There’s an [outstanding slide deck](https://web.archive.org/web/20090420024324/http://crm114.sourceforge.net/docs/Plateau99.pdf) (pdf) that explains how it all works. In a nutshell, **Markovian filtering weights phrases and words, whereas Bayesian filtering only looks at individual words**. How much better is it? I’ll let the CRM114 author, Bill Yerazunis, pitch it:


> For the month of April 2005, I received over 10,000 emails. About 60% were spam. I had ZERO classification errors. ZERO.
> As of Feb 1 through March 1, 2004, 8738 messages (4240 spam, 4498 non-spam), and my total error rate was ONE. That translates to better than 99.984% accuracy, which is over ten times more accurate than human accuracy
> I measured my own accuracy to be around 99.84%, by classifying the same set of about 3000 messages twice over a period of about a week, reading each message from the top until I feel “confident” of the message status, (one message per screen unless I want more than one screen to decide on a message.) and doing the classification in small batches with plenty of breaks and other office tasks to avoid fatigue. Then I diff()ed the two passes to generate a result. Assuming I never duplicate the same mistake, I, as an unassisted human, under nearly optimal conditions, am 99.84% accurate.


Most Bayesian techniques top out at around ~98% percent accuracy with a little training, but Markovian can achieve a rarified 99.5% accuracy. The most notable Windows port of CRM114 is SpamRIP.


*A reference to the movie [Dr. Strangelove](http://www.imdb.com/title/tt0057012/). In the movie, the “CRM114 Discriminator” is a fictional accessory for a radio receiver that’s “designed not to receive *at all,”* that is, unless the message is properly authenticated.


**I have since switched to [K9](http://www.keir.net/k9.html) because it’s simpler and faster – and does the same Bayesian filtering.

[scam](https://blog.codinghorror.com/tag/scam/)
[spamming](https://blog.codinghorror.com/tag/spamming/)
[email security](https://blog.codinghorror.com/tag/email-security/)
