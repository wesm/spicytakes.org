---
title: "Blacklists Don’t Work"
date: 2007-12-11
url: https://blog.codinghorror.com/blacklists-dont-work/
slug: blacklists-dont-work
word_count: 1717
---

[Jon Galloway](http://weblogs.asp.net/jgalloway/) and I got into a heated debate a few weeks ago about the efficacy of anti-virus software. My position is that [anti-virus software sucks](https://blog.codinghorror.com/trojans-rootkits-and-the-culture-of-fear/), and worst of all, it doesn’t work anyway. That’s what I’ve been saying all along, and it’s exactly what I told Jon, too:


> The [performance cost of virus scanning](https://blog.codinghorror.com/choosing-anti-anti-virus-software/) (lose 50% of disk performance, plus some percent of CPU speed) does not justify the benefit of a 33% detection rate and marginal protection. I would argue the *illusion* of protection is very, very dangerous as well.
> Ask yourself this: why don’t Mac users run anti-virus software? Why don’t UNIX users run anti-virus software? Because they don’t *need* to. They don’t run as administrators. Sadly, the cost of [running as non-admin is severe](https://blog.codinghorror.com/the-windows-security-epidemic-dont-run-as-an-administrator/) on Windows, because MS made some early, boneheaded architectural decisions and perpetuated them over a decade. But the benefit is substantial. There’s almost nothing a virus, malware, or trojan can do to a user who isn’t running as an administrator.
> I believe we should invest our money, time, and effort in things that make sense, things that work. Things like running as a non-administrator. And we should stop wasting our time on voodoo, which is what anti-virus software ultimately is.


To be fair, anti-virus software is more effective than I realized. In the August 2007 Anti-Virus Comparatives, the lowest detection rate was 90%, and the highest was 99.6%.


But I have a problem with the test methodology that produced these results. If we build a library of tests using all the viruses and malware in all of recorded history, we’ll get an absurdly high detection rate. But who really cares if Kapersky can detect a year old virus, much less a three or four year old one? What matters most, I think, is **detection rate for new threats**. That’s what’s *really* dangerous, not some ancient strain of a long-forgotten DOS virus. I’m sure anti-virus vendors love comparatives like this. It makes for great ad copy: we can detect 99.7% of threats! The bad news, which is hidden by a footnote marker and placed in 4-point text at the bottom of the page, is that 99.3% of them are so old as to be utterly irrelevant and meaningless. (Update: in a comment, Anders pointed out that a [November 27th “proactive/retrospective” test](https://web.archive.org/web/20100703110824/http://www.av-comparatives.org/seiten/ergebnisse/report16.pdf) (pdf) from the same site, using threats only a month old, showed far lower detection rates: between 80% and 33%.)


We could appeal to the data. Of the top 5 threats on [the virus radar](https://web.archive.org/web/20071229111332/http://www.virus-radar.com/index_c31d_enu.html), only one is younger than six months. However, the youngest dates from December 4th, a mere eight days ago. And it only takes one. If *anything* gets through your anti-virus software, you’re just as compromised as you would be if you were running no anti-virus software at all.


But for now, let’s assume these comparative statistics are correct. The heroic anti-virus teams can detect 99.7% of all the evil code in the world, and protect you from them, in the name of truth, justice, and the American Way. But it’s far from automatic. It only works if you stick to the plan. You know, *the plan*:

1. Purchase the best, most effective third party anti-virus software available. On a subscription plan. And install it.
2. Suck up the massive real-time virus check performance penalty.
3. Keep your anti-virus religiously up to date at all times. (Hourly? Daily? Weekly?)
4. Pray your anti-virus vendor can deliver signature updates faster than all the combined virus, trojan, and malware writers on the internet can create and deliver their payloads.


Wow, not much can go wrong there. And then you only have a 0.33% chance (or a 20% chance, depending which set of data you believe) of getting in very big trouble. Problem solved!


Or you could just, y’know, **not run as an administrator**, and then you’d *never* have any chance of getting in trouble. Ever. Well, at least not from trojans, malware, or viruses. But evidently a few children’s programs fail to run as non-administrator, and programming as a non-administrator is difficult, so that’s a deal-breaker for Jon.


After a lot (really, *a lot*) of back and forth with Jon on this topic, I realized that my position boiled down to one core belief:


**Blacklists don’t work.**


At its heart, anti-virus software is little more than a glorified blacklist. It maintains an internal list of evil applications and their unique byte signatures, and if it sees one on your system, kills it for you. Sure, anti-virus vendors will dazzle you with their ad copy, their *heuristic* this and *statistical* that; they’ll tell you (with a straight face, even) that their software is far more than a simple blacklist. It’s a blacklist with *lipstick*. It’s the prettiest, shiniest, most kissable blacklist you’ve ever seen!


I could waste your time by writing a long diatribe here about how blacklisting is a deeply flawed approach to security. But I don’t have to. We can turn to our old friend Mark Pilgrim for the [most radical deconstruction of blacklisting](https://web.archive.org/web/20060327074758/http://diveintomark.org/archives/2003/11/15/more-spam) you’ll probably ever read.


> I see from Jay’s Comment Spam Clearinghouse that **the latest and greatest tool available to us is a master [black]list of domain names and a few regular expressions.** No offense to Jay or all the people who have contributed to the list so far, but how quaint! I mean really. Savor this moment, folks. You can tell your children stories of how, back in the early days of weblogging, you could print out the entire spam blacklist on a single sheet of paper. Maybe with two or three columns and a smallish font, but still. Boy, those were the days.
> And they won’t last. They absolutely won’t last. They won’t last a month. The domain list will grow so unwieldy so quickly, you won’t know what hit you. It’ll get so big that it will take real bandwidth just to host it. Keeping it a free download will make you go broke. Code is free, but bandwidth never will be. Do you have a business plan? You’ll need one within 6 months.
> And then people will start complaining because a regex matches their site. Or spammers will set up fake identities to report real sites and try to poison the list. Are you manually screening new contributions? That won’t scale. Are you not manually screening new contributions? That won’t work either. Weighing contributions with a distributed Whuffie system? Yeah, that’s possible, but it’s a tricky balance, and still open to manipulation.
> It’s all been done. It’s all been done before, and it was completely all-consuming, and it still didn’t work. Spammers register dozens of new domains each day; you can’t possibly keep up with them. They’re bigger and smarter and faster than you. It’s an arms race, and you’ll lose, and along the way there will be casualties, massive casualties as innocent bystanders start getting blacklisted. (You do have a process for people to object to their inclusion, right? Yeah, except the spammers will abuse that too.)


Oh, and it goes on. That’s a mere slice. Read the rest. Like Mark, **blacklists make me angry**. Angry because I have to waste my time manually entering values in a stupid blacklist. Angry because the resulting list really doesn’t work worth a damn, and I’ll have to do the same exact thing again tomorrow, like clockwork. And most of all, angry because they’re a dark mirror into the absolute worst parts of human nature.


I’ve had plenty of experience with blacklists. A miniscule percentage of spammers have the resources to [bypass my naïve CAPTCHA](https://blog.codinghorror.com/captcha-effectiveness/). They hire human workers to enter spam comments. That’s why I enter URLs into a blacklist every week on this very site. It’s an ugly, thankless little thing, but it’s necessary. I scrutinize every comment, and I remove a tiny percentage of them: they might be outright spam, patently off-topic, or just plain mean. I like to refer to this as weeding my web garden. It’s a productivity tax you pay if you want to grow a bumper crop of comments, which, [despite what Joel says](http://www.joelonsoftware.com/items/2007/07/20.html), often [bear such wonderful fruit](https://blog.codinghorror.com/a-blog-without-comments-is-not-a-blog/). The labor can be minimized with improved equipment, but it’s always there in some form. And I’m OK with that. The myriad benefits of a robust comment ecosystem outweighs the minor maintenance effort.


I’ve also had some experience with the fancy, [distributed crowdsourcing style of blacklist](https://blog.codinghorror.com/whitelist-blacklist-greylist/). It’s a sort of consensual illusion; many hands may make light work, but they won’t miraculously fix the fundamentally broken security model of a blacklist. You’ll have the same core problems I have with the unpleasant little blacklist I maintain, writ much larger. The world’s largest decentralized blacklist is still, well, a blacklist.


So, in the end, perhaps I should apologize to Jon. I suppose anti-virus software *does* work, in a fashion... at a steep mental and physical cost. Like any blacklist, the effort necessary to maintain an anti-virus blacklist will slowly expand to occupy all available space and time. In philosophical terms, keeping an exhaustive and authoritative list of all the evil that men can do is an infinitely large task. At best, you can only hope to be ahead at any particular moment, *if* you’re giving 110%, and *if* you’re doing everything exactly the right way. Every single day. And sleep lightly, because tomorrow you’ll wake up to face a piping hot batch of fresh *new* evil.


If a blacklist is your only option, then by all means, use it.


With comments, I’m stuck. There’s no real alternative to the blacklist approach as a backup for my CAPTCHA. Furthermore, the ultimate value of a comment is subjective, so some manual weeding is desirable anyway. But **when it comes to anti-virus we *do* have another option**. A much better option. We can [run as non-administrators](https://blog.codinghorror.com/the-windows-security-epidemic-dont-run-as-an-administrator/). Running as a non-administrator has historically proven to be completely effective on OS X and UNIX, where the notion of anti-virus software barely exists.


Isn’t that the way it *should* be? **Relying on a blacklist model for security is tantamount to admitting failure before you’ve even started.** Why perpetuate the broken anti-virus blacklist model when we don’t have to?

[security](https://blog.codinghorror.com/tag/security/)
[antivirus](https://blog.codinghorror.com/tag/antivirus/)
[malware](https://blog.codinghorror.com/tag/malware/)
[virus scanning](https://blog.codinghorror.com/tag/virus-scanning/)
[software protection](https://blog.codinghorror.com/tag/software-protection/)
