---
title: "Desktop RAID: Oversold?"
date: 2005-07-07
url: https://blog.codinghorror.com/desktop-raid-oversold/
slug: desktop-raid-oversold
word_count: 696
---

I’ve seen a number of hardware-oriented developers talk about setting up striped RAID arrays on their personal desktops. It does seem like a reasonable idea, given the current strong trend towards “doubling up” on hardware to leverage performance benefits from parallelism in various forms – dual core CPUs, dual channel DDR, dual graphics cards in SLI, and dual hard drives in RAID 0.


However, except for dual channel memory, **none of these parallel hardware approaches are clear across-the-board performance wins**. They can be twice as fast *in very specific circumstances*, but as a general rule they’re just somewhat faster, and not without adding significant costs and even risks of their own.


[RAID 0 (aka striping)](https://web.archive.org/web/20050721031808/http://www.pcguide.com/ref/hdd/perf/raid/levels/singleLevel0-c.html) on the desktop, is especially dubious in my opinion. Just because current motherboard chipsets now make it easy and (relatively) inexpensive to do this doesn’t mean that you should:

1. **RAID 0 literally doubles your chance of drive failure**. All it takes is a single drive failure on either drive to render your striped array completely and utterly unrecoverable. A “normal” single drive failure is at least theoretically recoverable, albeit expensive. How expensive? If you have to ask, [you probably can’t afford it.](https://web.archive.org/web/20060621180047/http://forums.actionfront.com/showthread.php?t=59)
2. **Of all the hardware failures you can have, drive failure is by far the most traumatic.** Losing a CPU, video card, or even motherboard, means you just go out and buy another one. Losing a drive means you’ve probably lost your critical data, unless you have a good backup regimen in place. And 99% of us don’t. Kudos to the 1% of you reading this who do.
3. **The performance benefits of RAID 0 aren’t that compelling** for typical desktop usage scenarios.


So why would you go to the trouble of building a RAID 0 array if it’s more expensive, more complex, prone to failure, and not all that much faster? Short answer: you probably shouldn’t, **unless you know you have a specific scenario that justifies this setup.** There are a number of articles on the web that debunk the myth that RAID 0 is a universal performance improvement for a typical desktop PC:

- [Western Digital’s Raptors in RAID-0: Are two drives better than one?](http://www.anandtech.com/storage/showdoc.aspx?i=2101&p=11)
- Chipset Serial ATA and RAID performance comparison
- [TCQ, RAID, SCSI, and SATA](https://web.archive.org/web/20050730021827/http://www.storagereview.com/articles/200406/20040625TCQ_6.html)


All these articles are variations on the same theme; the AnandTech article summarizes nicely:


> If you haven’t gotten the hint by now, we’ll spell it out for you: there is no place and no need for a RAID-0 array on a desktop computer. The real world performance increases are negligible at best and the reduction in reliability, thanks to a halving of the mean time between failure, makes RAID-0 far from worth it on the desktop.
> There are some exceptions, especially if you are running a particular application that itself benefits considerably from a striped array, and obviously, our comments do not apply to server-class IO of any sort. But for the vast majority of desktop users and gamers alike, save your money and stay away from RAID-0.


The original hard drive benchmark review website, storagereview.com, offers this guidance:


> The enthusiasm of the power user community combined with the marketing apparatus of firms catering to such crowds has led to an extraordinarily erroneous belief that striping data across two or more drives yields significant performance benefits for the majority of non-server uses. This could not be farther from the truth! Non-server use, even in heavy multitasking situations, generates lower-depth, highly-localized access patterns where read-ahead and write-back strategies dominate. Theory has told those willing to listen that striping does not yield significant performance benefits. Some time ago, a controlled, empirical test backed what theory suggested. Doubts still lingered- irrationally, many believed that results would somehow be different if the array was based off of an SATA or SCSI interface. As shown above, the results are the same. Save your time, money and data- leave RAID for the servers!


If you have your heart set on RAID 0, go for it. It won’t *hurt* performance. But be sure you’re making [an informed decision](https://web.archive.org/web/20060308074131/http://www.devhardware.com/c/a/Storage-Devices/RAID-Not-Such-a-Clever-Idea-for-Your-Home-PC/). There’s a lot to be said for simplicity.

[hardware](https://blog.codinghorror.com/tag/hardware/)
[raid](https://blog.codinghorror.com/tag/raid/)
[desktop](https://blog.codinghorror.com/tag/desktop/)
[performance](https://blog.codinghorror.com/tag/performance/)
[risks](https://blog.codinghorror.com/tag/risks/)
