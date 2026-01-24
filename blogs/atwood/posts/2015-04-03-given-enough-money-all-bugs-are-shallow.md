---
title: "Given Enough Money, All Bugs Are Shallow"
date: 2015-04-03
url: https://blog.codinghorror.com/given-enough-money-all-bugs-are-shallow/
slug: given-enough-money-all-bugs-are-shallow
word_count: 1934
---

Eric Raymond, in [The Cathedral and the Bazaar](http://en.wikipedia.org/wiki/The_Cathedral_and_the_Bazaar), famously wrote:


> Given enough eyeballs, all bugs are shallow.


The idea is that open source software, by virtue of allowing anyone and everyone to view the source code, is inherently less buggy than closed source software. He dubbed this “Linus’s Law.”


![](https://blog.codinghorror.com/content/images/2015/04/eyeballs.jpg)


Insofar as it goes, I believe this is true. When only the 10 programmers who happen to work at your company today can look at your codebase, it’s unlikely to be as well reviewed as a codebase that’s public to the world’s scrutiny on GitHub.


However, the [Heartbleed SSL vulnerability](http://en.wikipedia.org/wiki/Heartbleed) was a turning point for Linus’s Law, a catastrophic exploit based on a [severe bug in open source](http://www.theregister.co.uk/2014/04/09/heartbleed_explained/) software. How catastrophic? It affected about 18% of all the HTTPS websites in the world, and allowed attackers to view all traffic to these websites, unencrypted... *for two years*.


All those websites you thought were secure? Nope. This bug went unnoticed for two full years.


*Two years!*


OpenSSL, the library with this bug, is **one of the most critical bits of Internet infrastructure the world has** – relied on by major companies to encrypt the private information of their customers as it travels across the Internet. OpenSSL was used on millions of servers and devices to protect the kind of important stuff you want encrypted, and hidden away from prying eyes, like passwords, bank accounts, and credit card information.


This should be some of the most well-reviewed code in the world. What happened to our eyeballs, man?


> In reality, it’s generally very, very difficult to fix real bugs in anything but the most trivial Open Source software. I know that I have rarely done it, and I am an experienced developer. Most of the time, what really happens is that you tell the actual programmer about the problem and wait and see if he/she fixes it. – [Neil Gunton](https://www.neilgunton.com/doc/?o=Sh&doc_id=8585)
> Even if a brave hacker communities to read the code, they’re not terribly likely to spot one of the hard-to-spot problems. Why? Few open source hackers are security experts. – [Jeremy Zawodny](http://jeremy.zawodny.com/blog/archives/000028.html)
> The fact that many eyeballs are looking at a piece of software is not likely to make it more secure. It is likely, however, to make people believe that it is secure. The result is an open source community that is probably far too trusting when it comes to security. – [John Viega](https://web.archive.org/web/20150311194140/http://www.developer.com/tech/article.php/626641/The-Myth-of-Open-Source-Security.htm)


I think there are a couple problems with Linus’s Law:

1. There’s a big difference between *usage* eyeballs and *development* eyeballs. Just because you pull down some binaries in a RPM, or compile something in Linux, or even report bugs back to the developers via their bug tracker, doesn’t mean you’re doing anything at all to contribute to the review of the underlying code. Most eyeballs are looking at the outside of the code, not the inside. And while you can discover bugs, even important security bugs, through usage, the hairiest security bugs require inside knowledge of how the code works.
2. The act of *writing* (or cut-and-pasting) your own code is easier than understanding and *peer reviewing* someone else’s code. There is a fundamental, unavoidable asymmetry of work here. The amount of code being churned out today – even if you assume only a small fraction of it is “important” enough to require serious review – far outstrips the number of eyeballs available to look at the code. (Yes, this is another argument in favor of [writing less code](https://blog.codinghorror.com/the-best-code-is-no-code-at-all/).)
3. There are not enough *qualified* eyeballs to look at the code. Sure, the overall number of programmers is slowly growing, but what percent of those programmers are skilled enough, and have the right security background, to be able to audit someone else’s code effectively? A tiny fraction.


Even if the code is 100% open source, utterly mission critical, and used by major companies in virtually every public facing webserver for customer security purposes, we end up with critical bugs that compromise everyone. For *two years!*


That’s the lesson. If we **can’t naturally get enough eyeballs on OpenSSL**, how does any other code stand a chance? What do we do? How do we get more eyeballs?


The short term answer was:

- Create more [alternatives to OpenSSL](http://www.libressl.org/) for ecosystem diversity.
- Improve [support and funding for OpenSSL](http://arstechnica.com/information-technology/2014/04/tech-giants-chastened-by-heartbleed-finally-agree-to-fund-openssl/).


These are both very good things and necessary outcomes. We should be doing this for all the critical parts of the open source ecosystem people rely on.


But what’s the long term answer to the general problem of not enough eyeballs on open source code? It’s something that will sound very familar to you, though I suspect Eric Raymond won’t be too happy about it.


![](https://blog.codinghorror.com/content/images/2015/04/pile-of-money-1.jpg)


*Money.* Lots and lots of money.


Increasingly, companies are turning to **commercial bug bounty programs**. Either ones they create themselves, or run through third party services like [Bugcrowd](https://bugcrowd.com/), [Synack](https://www.synack.com/), [HackerOne](https://hackerone.com/), and Crowdcurity. This means you pay per bug, with a larger payout the bigger and badder the bug is.


Or you can attend a yearly event like [Pwn2Own](http://en.wikipedia.org/wiki/Pwn2Own), where there’s a contest and massive prizes, as large as hundreds of thousands of dollars, for exploiting common software. Staging a big annual event means a lot of publicity and interest, attracting the biggest guns.


That’s the message. If you want to find bugs in your code, in your website, in your app, you do it the old fashioned way: by paying for them. You buy the eyeballs.


While I applaud any effort to make things more secure, and I completely agree that security is a battle we should be fighting on multiple fronts, both commercial and non-commercial, **I am uneasy about some aspects of paying for bugs becoming the new normal.** What are we incentivizing, exactly?


### Money makes security bugs go underground


There’s now a price associated with exploits, and the deeper the exploit and the lesser known it is, the more incentive there is to not tell anyone about it until you can collect a major payout. So you might wait up to a year to report anything, and meanwhile this security bug is out there in the wild – who knows who else might have discovered it by then?


If your focus is the payout, who is paying more? The good guys, or the bad guys? Should you hold out longer for a bigger payday, or build the exploit up into something even larger? I hope for our sake the good guys have the deeper pockets, otherwise we are all screwed.


I like that Google [addressed a few of these concerns](http://blog.chromium.org/2015/02/pwnium-v-never-ending-pwnium.html) by making Pwnium, their Chrome specific variant of Pwn2Own, a) no longer a yearly event but all day, every day and b) increasing the prize money to “infinite.” I don’t know if that’s enough, but it’s certainly going in the right direction.


### Money turns security into a “me” goal instead of an “us” goal


I first noticed this trend when one or two people reported minor security bugs in Discourse, and then seemed to hold out their hand, expectantly. (At least, as much as you can do something like that in email.) It felt really odd, and it made me uncomfortable.


Am I now obligated, on top of providing a completely free open source project to the world, to pay people for contributing information about security bugs that make this open source project better? Believe me, I was very appreciative of the security bug reporting, and I sent them whatever I could, stickers, t-shirts, effusive thank you emails, callouts in the code and checkins. But open source isn’t supposed to be about the money… is it?


Perhaps the landscape is different for closed-source, commercial products, where there’s no expectation of quid pro quo, and everybody already pays for the service directly or indirectly anyway.


### No Money? No Security.


If all the best security researchers are working on ever larger bug bounties, and every major company adopts these sorts of bug bounty programs, what does that do to the software industry?


It implies that unless you have a big budget, you can’t expect to have great security, because nobody will want to report security bugs to you. Why would they? They won’t get a payday. They’ll be looking elsewhere.


A ransomware culture of “pay me or I won’t tell you about your terrible security bug” does not feel very far off, either. We’ve had mails like that already.


### Easy money attracts all skill levels


One unfortunate side effect of this bug bounty trend is that it attracts not just bona fide programmers interested in security, but anyone interested in *easy money*.


We’ve gotten too many “serious” security bug reports that were extremely low value. And we have to follow up on these, because they are “serious,” right? Unfortunately, many of them are a waste of time, because…

- The submitter is more interested in scaring you about the massive, critical security implications of this bug than actually providing a decent explanation of the bug, so you’ll end up doing all the work.
- The submitter doesn’t understand what is and isn’t an exploit, but knows there is value in anything *resembling* an exploit, so submits everything they can find.
- The submitter can’t share notes with other security researchers to verify that the bug is indeed an exploit, because they might “steal” their exploit and get paid for it before they do.
- The submitter needs to convince you that this is an exploit in order to get paid, so they will argue with you about this. At length.


The incentives feel really wrong to me. As much as I know security is incredibly important, I view these interactions with an increasing sense of dread because they generate work for me and the returns are low.


### What can we do?


Fortunately, we all have the same goal: **make software more secure**.


So we should view bug bounty programs as an additional angle of attack, another aspect of “defense in depth,” perhaps optimized a bit more for commercial projects where there is ample money. And that’s OK.


But I have some advice for bug bounty programs, too:

- You should have someone vetting these bug reports, and making sure they are credible, have clear reproduction steps, and are repeatable, before we ever see them.
- You should build additional incentives in your community for some kind of collaborative work towards bigger, better exploits. These researchers need to be working together in public, not in secret against each other.
- You should have a reputation system that builds up so that only the better, proven contributors are making it through and submitting reports.
- Encourage larger orgs to fund bug bounties for common open source projects, not just their own closed source apps and websites. At Stack Exchange, we donated to open source projects we used every year. Donating a bug bounty could be a big bump in eyeballs on that code.


I am concerned that we may be slowly moving toward a world where **given enough money, all bugs are shallow**. Money does introduce some perverse incentives for software security, and those incentives should be watched closely.


But I still believe that the people who will freely report security bugs in open source software because:

- It is the right thing to do™


and

- They want to contribute back to open source projects that have helped them, and the world


…will hopefully not be going away any time soon.

[open source](https://blog.codinghorror.com/tag/open-source/)
[software development](https://blog.codinghorror.com/tag/software-development/)
[security](https://blog.codinghorror.com/tag/security/)
[linus's law](https://blog.codinghorror.com/tag/linuss-law/)
[heartbleed](https://blog.codinghorror.com/tag/heartbleed/)
[technical practices](https://blog.codinghorror.com/tag/technical-practices/)
