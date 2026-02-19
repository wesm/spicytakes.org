---
title: "JackAssassin"
date: 2003-05-18
url: https://daringfireball.net/2003/05/jackassassin
slug: jackassassin
word_count: 390
---


As I type these words, I’ve received exactly 450 spams in the last 7 days. [SpamAssassin](http://spamassassin.org/) has flagged all but 45 of them, for a batting average of .900.


My own filters (implemented in Mailsmith) flagged 32 of the spams missed by SpamAssassin, leaving only 13 spams that ended up in my inbox, for a combined batting average of .971. Not bad.


I had long been skeptical of SpamAssassin. But when [my web hosting company](http://www.pair.com/) added support for it a few weeks ago, I figured I’d give it a shot. It works by applying a long list of built-in rules against each message; for each rule that matches a message, points are added or subtracted. The higher the total score, the more likely the message is spam. Legitimate email often ends up with a negative score. You set a cut-off value; SpamAssassin flags messages with a score higher than the cut-off by adding custom headers. (This is an over-simplification of how SpamAssassin works, but it’s close enough.)


The problem I anticipated with SpamAssassin wasn’t false positives, but rather too many false negatives (missed spams). SpamAssassin is open source and written in Perl — it thus runs just about anywhere. A smart spammer, quite obviously, would do well to test their messages by sending them through SpamAssassin, then tweaking their content until they slip through undetected.


“Smart spammers”, apparently, are a very rare breed. My SpamAssassin cut-off value is 3.5; 8 of my 13 unfiltered spams from this past week had a value between 3.0 and 3.5. It helps that SpamAssassin is frequently updated; its ruleset is in constant flux, in a never-ending battle to remain one step ahead of any countermeasures enacted by savvy spammers.


I do get a few false positives, but they’re almost always borderline spam anyway — marketing messages from online retailers, or five-times forwarded “jokes” from distant relatives who use AOL. A whitelist allows you to make exceptions for serial offenders.


So it ends up SpamAssassin works very well. My concern, however, is that “very good” is not good enough. 97 percent is a fine detection rate when you receive 500 spams a week. It’s not so good if you receive 5,000 spams a week — and that’s where it seems we’re heading.



| **Previous:** | [Zeldman Reloaded](https://daringfireball.net/2003/05/zeldman_reloaded) |
| **Next:** | [Steaming Pile](https://daringfireball.net/2003/05/steaming_pile) |


PreviousNext