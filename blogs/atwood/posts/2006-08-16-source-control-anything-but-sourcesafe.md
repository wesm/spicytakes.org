---
title: "Source Control: Anything But SourceSafe"
date: 2006-08-16
url: https://blog.codinghorror.com/source-control-anything-but-sourcesafe/
slug: source-control-anything-but-sourcesafe
word_count: 547
---

Everyone agrees that [source control is fundamental](https://blog.codinghorror.com/what-is-modern-software-development/) to the practice of modern software development. However, there are dozens of source control options to choose from. VSoft, the makers of [FinalBuilder](http://www.vsoft-tech.com.au/finalbuilder.aspx), just published the results of their annual customer survey. One of the questions it asked was which version control systems do you currently use, or plan to use, [in the next 12 months?](http://www.vsoft-tech.com.au/Default.aspx?tabid=77&EntryID=190)


![Source control adoption graph, May 2005 to August 2006](https://blog.codinghorror.com/content/images/uploads/2006/08/6a0120a85dcdae970b0128776fde59970c-pi.png)


The top 9 responses are reprinted here. I’m disheartened to see that [Visual SourceSafe](http://msdn.microsoft.com/vstudio/products/vssafe/default.aspx) is still at the top of the list. **If you are serious about the practice of software development, you should not be using SourceSafe.** This isn’t a new idea; plenty of other developers have been warning us away from SourceSafe for years:

- [Visual SourceSafe: Microsoft’s Source Destruction System](http://www.highprogrammer.com/alan/windev/sourcesafe.html)
- [Visual SourceSafe Version Control: Unsafe at any Speed?](https://web.archive.org/web/20070207023001/http://www.developsense.com/testing/VSSDefects.html)


There’s simply no reason to use SourceSafe when there are so many inexpensive (and even free) alternatives that are vastly superior. The more customers I visit, and the more developers I talk to, the more I believe that **SourceSafe poisons the minds of software developers.** Note that I include our own shop, Vertigo Software, in this list.

- SourceSafe gives you the *illusion* of safety and control, while exposing your project to risk.
- SourceSafe teaches developers bad habits: avoid branching, exclusive locks, easy permanent deletions.


SourceSafe was a perfectly adequate source control system in the late 90s. Unfortunately, SourceSafe was never updated architecturally to reflect modern source control practices. Even the latest version, SourceSafe 2005, absolutely *reeks* of 1999. And, to be fair, **some of the same criticisms apply to CVS**. CVS is no longer a modern source control system, either; it doesn’t even support the concept of atomic check ins.


**One of my biggest hurdles has been unlearning all the bad things SourceSafe taught me about source control.** Source control is the absolute bedrock of software engineering. It’s as fundamental as it gets. If my knowledge in this area isn’t deep, wide, and fundamentally sound, can I really call myself a software engineer?


So, how do we learn modern source control?

1. Start with [Eric Sink’s Source Control HOWTO](http://www.ericsink.com/scm/source_control.html). Eric is self-admittedly biased because his company created [SourceGear Vault](http://www.sourcegear.com/vault/), but he’s up front about this. He has truly lived and breathed the topic of source control, and it shines through in his excellent writing.
2. The online Subversion manual is well worth your time. The first few introductory chapters, starting with [Chapter 2: Basic Concepts](http://svnbook.red-bean.com/nightly/en/svn.basic.html), are wonderful primers.
3. Chris Birmele’s [paper on Branching and Merging](https://web.archive.org/web/20070317213445/http://blogs.msdn.com/chrisbirmele/archive/2006/05/31/611179.aspx) is the best introduction I’ve found to this essential source control task. There are dozens of ways to branch, and no one correct way to do it. Get familiar with your options so you know what the tradeoffs are with each one.


Visual SourceSafe was most Microsoft developers’ first introduction to any kind of source control at all. That’s great. But holding on to SourceSafe’s archaic source control conventions is doing more damage than good these days. Make the switch to Team System, Subversion, or any other modern source control system of your choice.


But whatever you do, **please don’t use Visual SourceSafe.** Think of the children.

[source control](https://blog.codinghorror.com/tag/source-control/)
[version control systems](https://blog.codinghorror.com/tag/version-control-systems/)
[software development practices](https://blog.codinghorror.com/tag/software-development-practices/)
