---
title: "The Good, the Bad, and the Avie"
date: 2003-07-14
url: https://daringfireball.net/2003/07/the_good_the_bad_and_the_avie
slug: the_good_the_bad_and_the_avie
word_count: 1356
---


Last Tuesday, Apple announced that [Avie Tevanian was taking on the new title](http://www.apple.com/pr/library/2003/jul/08avie.html) of “chief software technology officer”, and that taking his place as senior vice president of software engineering would be Bertrand Serlet. The announcement also indicates that the change was more than titular, and that Serlet would be taking over responsibility for day-to-day management of the company’s copious software projects. The announcement might seem like a bit of a shake-up, but I don’t think it is.


Serlet joined NeXT in 1989, and has been working under Tevanian (and Jobs) ever since. So it’s not like he came out of the blue, or that his promotion would in any way indicate a change in direction or priorities for Apple’s software.


But one can hope.


Tevanian’s stewardship over Apple’s software has been a decidedly mixed bag. Overall, he’s done a tremendous job. But where he’s gone wrong, he’s gone terribly wrong, flashing a spiteful streak that has been largely detrimental to Mac OS X’s overall usability.


## The Good


Tevanian’s greatest and most profound success has been project management. Since taking responsibility for Apple’s software in 1997, large projects have shipped on schedule, or very close to it.


Admittedly, the debut of Mac OS X took several years longer than originally stated, and much of that delay can be attributable to design choices mandated by Tevanian. (More on this in the next section.) But it did eventually ship, which in and of itself was a notable accomplishment. Apple had launched numerous previous attempts at creating a viable successor to the original Mac OS, and Mac OS X is the only one that ever shipped.


But an essential aspect to Mac OS X’s success is that it didn’t merely ship, it shipped with discernable momentum. It has gotten better — both in terms of performance and usability — steadily and on a regular schedule. First the public beta, then each released version from 10.0 through 10.2 (and soon, 10.3).


This one-major-update-per-year schedule is an essential aspect of Mac OS X’s success. The general perception is that Mac OS X isn’t just good, but that it’s good and getting better. That perception seems to be held not just by the Mac community, but by the computer industry in general.


And for all of Tevanian’s widely-noted antipathy towards the traditional Mac OS (once again, see below), it was under his management, post NeXT-merger, that Mac OS 8 through 9.2 shipped, restoring momentum to a platform that had stagnated for years. From 1998 through 2001, the classic Mac OS was on the same one-major-update-per-year schedule that Mac OS X is adhering to, quite a welcome contrast from the early-to-mid-1990s era of System 7.


So in fact, from 1998 through 2001, Apple had two major operating systems under active development, both of them successful. That’s a major accomplishment. And while Tevanian and his fellow expatriates from NeXT surely spent the majority of their own time and effort working on Mac OS X, Tevanian was still ultimately responsible for shipping Mac OS 8-9, and deserves acclaim for the success. Even if his direct role amounted to little more than putting the ball in the court of brilliant long-time Mac engineers like [Keith Stattenfield](http://stattenfield.org/keith/index.shtml) (leader of the Mac OS 9 project), the fact remains that the state of the traditional Mac OS improved dramatically after Tevanian became v.p. of software engineering.


Mac OS X’s current schedule is in direct contrast to every other desktop operating system in the industry. Microsoft’s Windows, most notably, is on a much longer, more monolithic update schedule. XP, its last major update, shipped in late 2001, and the next update, Longhorn, isn’t coming until at least 2005 or 2006. Many people have compared the features of Apple’s Panther (10.3) to Microsoft’s Longhorn, but why? Even if Longhorn does ship in 2005, Apple will likely have shipped two major updates *after* Panther in that same time.


Longhorn will surely be much more improved over XP than any single point-upgrade of Mac OS X is over the previous release, but over the course of the same four- or five-year period, which system will have improved more?


Mac OS X’s successful incremental update schedule is a testimony both to Apple’s software engineering management, and to the modular architecture of Mac OS X. Tevanian certainly deserves at least some of the credit for both. The end result is a win for everyone — users get improved software quicker, and Apple gets something new to sell and to promote annually.


## The Bad


Tevanian’s legacy is marred, however, by Mac OS X’s usability flaws, most of which are attributable to Tevanian’s nearly unyielding obsession with promoting old NeXT technology over old Apple technology. His technical acumen may be undisputed, but neither is his tin ear for usability.


Epitomizing this flaw was the infamous Technical Note #2034, entitled “Mac OS X Programming Guidelines”, which as reported by [MDJ](http://www.macjournals.com/) was written by Tevanian personally. Technote #2034 was so inflammatory, and in places so *ludicrous*, that Apple withdrew it afters howls of derision from professional Mac developers.


It’s still down, thus the lack of a link to it. Technotes #2033 and #2035 (“How to use the ATSUI APIs to get glyph outlines” and “ColorSync on Mac OS X”, respectively) are available at the following URLs:


```

http://developer.apple.com/technotes/tn/tn2033.html

```


```

http://developer.apple.com/technotes/tn/tn2035.html

```


[**Update:**I’ve posted a [PDF archive of Technote #2034](https://daringfireball.net/misc/2003/07/tn2034.pdf).]


But #2034 is nowhere to be seen on apple.com. And for good reason. Technote #2034, ostensibly a series of guidelines on how to write better Mac OS X software, in fact amounted to little more than dogma against Mac technologies. E.g.: Mandating filename extensions in lieu of genuine type and creator metadata for “compatibility”; recommending against using HFS metadata at all, because doing so causes performance issues for UFS disks (no matter that UFS is a vastly inferior disk format); promoting Objective-C as a more portable cross-platform language than C++; and, most laughably, recommending the use of hard-coded pathname APIs for accessing files, rather than more flexible, friendly, and traditional Mac APIs which access files by file ID.


Mac developers tend to be independent thinkers, and flatly rejected the precepts of Tevanian’s “Guidelines”.


All too often, Tevanian’s decisions and edicts have been dogmatic rather than pragmatic. For example, the decision to build Mac OS X around the Mach kernel rather than Apple’s own NuKernel. The problem, such that it was a “problem”, is that NuKernel was developed at Apple before the NeXT merger; whereas [Tevanian himself co-created Mach](http://www-2.cs.cmu.edu/afs/cs/project/mach/public/www/people-former.html) while he was a grad student at Carnegie Mellon in the mid-1980s.


I’m not claiming that NuKernel was perfect, or superior to Mach in every way. I’m not in any position to make such judgments. But by all accounts, the idea of using NuKernel rather than Mach was never even considered by Tevanian, no matter what advantages it might have held. (For one, superior power management, a continuing weak spot in Mac OS X.) NuKernel, remember, was designed from the outset as a kernel to power future PowerPC-based Mac operating systems; Mach wasn’t. It’s certainly conceivable that Mac OS X might have shipped significantly sooner had Apple used NuKernel.


Such kernel gossip, however, is speculation. In other areas, Tevanian’s decisions have had a demonstrably detrimental effect on Mac OS X usability. The aforementioned filename extension shenanigans. Or the aforementioned admonition to use path-based APIs to access files, which advice directly led to Apple installers which failed to work if you moved or renamed any of your applications, and even worse, the [infamous iTunes 2.0 installer debacle](http://www.apple.com/itunes/alert/), which led to entire volumes being deleted — perhaps the worst bug in Apple’s history, and which could have been avoided simply by using traditional Mac OS file access APIs.


In short, many of Tevanian’s design decisions have not been made with the best interests of Mac users in mind. Here’s to hoping that Serlet either has a better sense of usability than Tevanian, or that if not, that he’s humble enough to delegate such decisions to those who do.



| **Previous:** | [Independent Days](https://daringfireball.net/2003/07/independent_days) |
| **Next:** | [Finding Avie](https://daringfireball.net/2003/07/finding_avie) |


PreviousNext