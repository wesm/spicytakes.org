---
title: "We Don’t Use Software That Costs Money Here"
date: 2008-04-09
url: https://blog.codinghorror.com/we-dont-use-software-that-costs-money-here/
slug: we-dont-use-software-that-costs-money-here
word_count: 1326
---

Whenever the regular expression topic comes up, I unashamedly recommend the best tool on the market for parsing and building regular expressions – [RegexBuddy](http://www.regexbuddy.com/cgi-bin/affref.pl?aff=jatwood). But there’s one tiny problem.


RegexBuddy costs money.


![](https://blog.codinghorror.com/content/images/2025/05/ms-excel-software-boxed-vintage.jpg)


I’ve always encountered vague resistance when recommending commercial tools that I considered best of breed. The source of that resistance was spelled out for me by Henrik Sarvell in this comment he left on [Rob Conery’s blog:](https://web.archive.org/web/20080704130239/http://blog.wekeroad.com/2007/10/30/in-which-we-discuss-proprietary-object-noise/)


> Yes, I also have to brush up on the regex from time to time. **We don’t use software that costs money here**, and last time I checked RegexBuddy wasn’t free.


People usually don’t state their preferences this boldly. I, for one, applaud the honesty.


I’ve [recommend Beyond Compare](https://blog.codinghorror.com/in-praise-of-beyond-compare/) before; it’s a fantastic file and directory comparison tool. It’s not expensive, but it’s not free, either. Which means many programmers I recommend it to will beg off and go install the free [WinMerge](http://winmerge.org/) comparison tool instead.


It’s tempting to ascribe this to the “cult of no-pay,” programmers and users who simply **won’t pay for software** no matter how good it is, or how inexpensive it may be. These people used to be called *pirates*. Now they’re *open source enthusiasts*.

kg-card-begin: html

(Update: This paragraph was intended to be tongue in cheek, but has been widely misinterpreted. Dan summarized my opinion in the comments: “in the past, if someone told you they used software and didn’t pay for it, the only plausible interpretation was that they were a pirate, because all good PC software cost money. Now there’s also **good software available for free**, so that assumption is no longer correct.”)

kg-card-end: html

But there’s something else going on here, too: **the free software alternatives keep getting better every year**. Consider how immature Linux development tools were in 2000 compared to what’s available today: [Eclipse](http://www.eclipse.org/), [Subversion](https://web.archive.org/web/20080312035657/http://subversion.tigris.org/),  [MySQL](http://www.mysql.com/), [Firefox](http://www.mozilla.com/en-US/). These tools either didn’t exist, or have come astounding distances in closing the gap between their commercial counterparts in eight years.


![](https://blog.codinghorror.com/content/images/2025/04/image-67.png)


PHP was dangerously close to a joke language in 2000, but you can barely go anywhere on the web today without running into something huge built on PHP. I could say the same thing about MySQL – a toy database in 2000, but a totally credible free alternative to Oracle and SQL Server today for most uses. **The competitive pressure of free products on commercial tools intensifies every year**. It’s relentless. And to be honest, I feel many of the commercial alternatives aren’t evolving fast enough to stay ahead of their free competition.


The onus is on the commercial tool vendors to prove that they provide enough value to warrant spending money. In the case of Beyond Compare, the vendor has taken so long to ship version 3.x of their software that some of the free comparison tools have matched and even exceeded its feature set in the meantime – as you can see in this amusingly titled [comparison of file comparison tools](http://en.wikipedia.org/wiki/Comparison_of_file_comparison_tools). Resting on their laurels is a luxury they no longer have.


It’s entirely possible for commercial development tools to survive alongside the strong, vibrant – and now firmly established – ecosystem of free tools. But it won’t be easy, as Steven Frank points out in [The First, The Free, and The Good](https://web.archive.org/web/20080414002515/http://stevenf.com:80/archive/the-first--the-free--and-the-good.php):


> A free program need not be glamorous or even completely bug-free. It can garner a respectable following simply by not costing anything.
> I’ve seen many times people struggle and struggle on with a clunky freeware app just because they’re not willing to pay $20 for a significantly better alternative. There’s nothing wrong with that particular brand of masochism. People prioritize differently, and money is more valuable than time to a whole lot of people. It’s Capitalism in action.
> The people who are most tenacious about exclusively using freeware whenever possible are usually incredulous that anyone would buy a commercial product when a free alternative is available. I’ve heard many times, “how can you guys make a living when *free* command line file transfer clients are *included* with the OS?”


Beyond Compare was the best compare tool by far in 2005 – an easy justification for spending thirty bucks on a compare tool. But no longer. They have to claw their way back to the top and become the best again in the face of endless free competition.


> If you’re neither first nor free, there is still a way to carve out a niche for yourself: **have a better application than everyone else**.
> Quality is the third leg of the axis. A free app may not be worth what you paid if it doesn’t work right, or works so clumsily that you have to re-read the help file every time you use it. The first app may be OK, but resting on its laurels of first-ness and not moving forward.


This phenomenon isn’t limited to development software, although I think it’s particularly vicious there due to the peculiarities of the audience: the type of people who would buy development tools are also exactly the same people who could potentially *build* them.


You may wonder how anything survives online in the face of free competition. Don MacAskill of [SmugMug](http://smugmug.com/) – a pay photo sharing website – [offers this advice](https://web.archive.org/web/20080414000613/http://www.npost.com/interview.jsp?intID=INT00183):


> It turns out that people are happy to pay [for web photo sharing], and have been happy to pay for the last four years. The reason is that our pay service eliminates a lot of the baggage and a lot of headaches that at least some percentage of the population doesn’t want. Quite of a few of the big brands have shut their free sites down. They shut them down without notice. It turns out that it’s sort of like a death spiral. When you offer accounts for free, some garbage comes in with the good stuff. People will upload porn or whatever. So you end up hiring people to work at your company to filter out the bad stuff. I know Photobucket and Webshots and some of the other guys have an entire room full of people who, all they do all day is watch the photos that are coming in and say yes or no, this photo is OK or not.
> But inevitably, some of the junk slips through, and then the people who are using your service who don’t have any junk see their photos side by side with the junk, and get up set and leave. Or even worse yet, some of your advertisers (because if you’re free you’re likely ad supported) see their ad right next to something disgusting or that damages their brand or something like that. So they bail. So eventually, your customers and your advertisers tend to run away screaming. Or you’re left with a demographic which isn’t a very important demographic for advertisers, or who wouldn’t be likely to upgrade. So it gets kind of nasty.


I knew Don from his days [in the gaming industry](http://don.smugmug.com/gallery/127686_dJQBJ#4611586) at Ritual Entertainment. I finally got to meet him at last year’s MIX conference, and I thoroughly enjoy reading his blog. It’s a case study in how you can beat ‘free’ by understanding the weaknesses of your free competition.


It won’t be easy for commercial software or subscription websites. If past history is any indication, **beating the free alternatives is going to get progressively more difficult every year**. Kevin Kelly offers eight generative qualities that are [better than free](http://www.kk.org/thetechnium/archives/2008/01/better_than_fre.php). I’m not sure it has to be that complicated. Free is indeed a competitive advantage. But free is also a weakness: it is cheap, mass-produced, and the same for everyone. Don and Steven make a compelling argument that some people are willing to pay for a premium experience.


So the salient question, then, is this: **do you understand what it takes to build the premium experience that trumps your free competition?** And can you *deliver* it?

[regular expressions](https://blog.codinghorror.com/tag/regular-expressions/)
[commercial tools](https://blog.codinghorror.com/tag/commercial-tools/)
[programming preferences](https://blog.codinghorror.com/tag/programming-preferences/)
[software cost](https://blog.codinghorror.com/tag/software-cost/)
