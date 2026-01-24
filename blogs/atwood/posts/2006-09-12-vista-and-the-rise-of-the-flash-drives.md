---
title: "Vista and the Rise of the Flash Drives"
date: 2006-09-12
url: https://blog.codinghorror.com/vista-and-the-rise-of-the-flash-drives/
slug: vista-and-the-rise-of-the-flash-drives
word_count: 836
---

In my recent [Windows Vista performance investigation](https://blog.codinghorror.com/have-you-ever-been-windows-experienced/), I discovered the new [ReadyBoost](https://web.archive.org/web/20061205212558/http://www.microsoft.com/windowsvista/features/foreveryone/performance.mspx) feature. ReadyBoost allows you to **augment your PC’s performance using a USB flash memory drive.** It’s very easy to use; just plug in a USB flash drive that’s 256 megabytes or larger, then navigate to the ReadyBoost tab on the properties dialog for the drive:


![](https://blog.codinghorror.com/content/images/2025/05/image-355.png)


The drive has to meet certain minimum performance characteristics (defined in the [ReadyBoost FAQ](https://web.archive.org/web/20061107203342/http://blogs.msdn.com/tomarcher/archive/2006/06/02/615199.aspx)) to be usable for ReadyBoost. Vista performs a one-time performance benchmark on the drive after it’s inserted to determine if the drive is suitable.


But what is ReadyBoost actually *doing* to improve performance? It’s leveraging the **unique advantages of flash memory**...

1. decent read and write speeds
2. extremely fast random access times
3. very low power consumption


... by caching the system pagefile on that USB flash drive.* Subsequent accesses hit the cached, compressed pagefile on the flash drive and bypass the hard drive entirely.


If we’ve gone this far, you might wonder why we just don’t go all the way and use a [giant 32-gigabyte flash drive](https://web.archive.org/web/20061008100055/http://www.reghardware.co.uk/2006/03/21/samsung_unveils_ssd/) as our primary hard drive. I can think of three reasons why you wouldn’t want to do that:

1. Speed. Flash memory is fast, but it’s not nearly as fast a modern hard drive. And it’s not even remotely in the same league as system memory.
2. Cost. Although flash memory pricing has been in freefall for a while, it’s still rather expensive on a cost-per-megabyte basis. This will definitely change over time, however.
3. Durability. Flash memory literally wears out after a fixed number of writes, usually 100,000 or so. Hard drives last many orders of magnitude longer.


Also, the performance benefits of a solid state hard drive – even one based on ultra-fast battery-backed DDR memory – aren’t as amazing [as you might think](https://blog.codinghorror.com/what-if-it-was-infinitely-fast/).


That’s why the best solution might be a combination of traditional mechanical hard drives *and* flash memory – **so-called “hybrid” hard drives with embedded flash cache**. For example, the Seagate Momentus 5400 PSD includes 256 megabytes of flash RAM. This feature is called [ReadyDrive](https://web.archive.org/web/20070308004555/http://www.microsoft.com/whdc/system/sysperf/accelerator.mspx), and it’s even better than ReadyBoost. Unlike a USB flash drive, the flash RAM on a hard drive can be read *before the system is booted*, and thus can be used to speed up boot and resume times, too.


It’s looking more and more like flash memory is the future. But be careful, because **not all flash memory is created equal**. I researched USB flash drive performance recently and I found benchmark roundups at [hardware secret](https://web.archive.org/web/20070111085733/http://www.hardwaresecrets.com/article/321/4), [AnandTech](http://www.anandtech.com/memory/showdoc.aspx?i=2549&p=1), and [Ars Technica](http://arstechnica.com/reviews/hardware/flash2005.ars/1). In my research, I found that there are at least three distinct tiers of flash drive performance today: mediocre, good, and best. The price difference between the best performers and the worst performers isn’t much, so you might as well buy the fast ones. The flash drives that performed the best in the above three benchmarks were the **Kingston Data Traveller Elite** and the **Lexar JumpDrive Lightning**.


Cheap flash drives are cheap for a reason – they skimp on performance. Here’s performance comparison of three USB thumb drives I had on hand: a 1 gigabyte Iomega Micro Mini, a 1 gigabyte Kingston Data Traveler Elite, and a generic no-name 128 megabyte model I got at a trade show.


I ran [SiSoft Sandra’s](http://www.sisoftware.net/) flash memory test on these three drives. The results are summarized below. Note that the bars are stacked, so the total transfer rate is only as high as the largest sub-color in the bar.


![](https://blog.codinghorror.com/content/images/2025/05/image-356.png)


There’s a big disparity between read and write performance on flash drives. And small files are disproportionately painful to transfer through these devices. The cheaper the flash drive, the worse these characteristics will be. When you go for an inexpensive USB flash drive, that’s the tradeoff you’re making.


I also ran the [command line chddspeed utility](http://www.benchmarkhq.ru/english.html?/be_hdd.html) on these three drives. Here are the results for the random access read test.


![](https://blog.codinghorror.com/content/images/2025/05/image-357.png)


Flash memory is exceptionally strong at random access; my fast WD Raptor drive can’t touch these scores.


Here are the chddspeed results for sequential access.


![](https://blog.codinghorror.com/content/images/2025/05/image-358.png)


Up to 12 Mb/sec is nothing to sneeze at, but it’s nearly 6 times slower than the 68 Mb/sec the Raptor achieves. If you need fast sequential read (or write) speeds, you want a hard drive.


After all this analysis, it’s clear to me that traditional hard drives and flash memory are quite complimentary; they’re strong in different areas. But **flash drives are the future**. They will definitely replace hard drives in almost all low end and low power devices – and future high performance hard drives will need to have a substantial chunk of flash memory on board to stay competitive.


*Yes, it’s encrypted, and yes, it is optimized for the limited duty cycle of flash drives. It’s even compressed, so that 1 GB flash drive is effectively 2 GB of cache. This is all covered in the excellent ReadyBoost FAQ.

[flash memory](https://blog.codinghorror.com/tag/flash-memory/)
[performance optimization](https://blog.codinghorror.com/tag/performance-optimization/)
[usb drives](https://blog.codinghorror.com/tag/usb-drives/)
[windows vista](https://blog.codinghorror.com/tag/windows-vista/)
[readyboost](https://blog.codinghorror.com/tag/readyboost/)
