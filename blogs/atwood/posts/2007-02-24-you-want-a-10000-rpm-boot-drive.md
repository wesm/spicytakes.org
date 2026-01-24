---
title: "You Want a 10,000 RPM Boot Drive"
date: 2007-02-24
url: https://blog.codinghorror.com/you-want-a-10000-rpm-boot-drive/
slug: you-want-a-10000-rpm-boot-drive
word_count: 890
---

I don’t go out of my way to recommend building your own computer. I do it, but I’m an OCD-addled, pain-loving masochist. You’re usually better off buying whatever cut-rate OEM box Dell is hawking at the moment, particularly now that Intel has finally abandoned the awful Pentium 4 CPU series and is back in the saddle with its excellent Core Duo processor. PC parts are so good these days it’s difficult to make a bad choice, no matter what you buy.


If you really *must* build your own computer, sites like Tech Report provide excellent advice in the form of [their system guides](https://web.archive.org/web/20070312004057/http://techreport.com:80/etc/2007q1/system-guide/index.x?pg=2). However, their guide sets the bar a little too low for my tastes. There are a few **baseline requirements for any new computer build** that aren’t negotiable for me:

- current dual core chip, such as the Core Duo 2 or Athlon 64 X2
- minimum of 2 GB of memory
- modern PCI express video card with 256mb or more of memory, such as the NVIDIA 7600GS, or the ATI Radeon X1650. Both of these cards can be found for about $100. Whatever you do, avoid on-board video, because it’s universally crappy. The rule of thumb I use is this: if you’re spending significantly less than $100 on your video card, you’re making a terrible mistake.


It’s not expensive. At today’s prices, you’re looking at around $800 for a new system based on these parts. Build that up and you’ve got a machine that can handle anything you throw at it, from cutting-edge games to full resolution high definition video playback. Oh yeah, and it compiles code pretty fast, too. If you’re an avid gamer you might possibly want to throw another $50 to $100 at the video card for higher resolutions, but that’s about it.


But one of the recommendations I make often gets some unexpected resistance. I believe every new PC build should have **two hard drives**:

1. small 10,000 RPM boot drive
2. large 7,200 RPM data/apps/games/media drive


I am a total convert to the [Western Digital Raptor series](http://www.wdc.com/en/products/Products.asp?DriveID=189) of 10,000 RPM SATA hard drives. Maybe you’re skeptical that a hard drive could make that much difference to a computer’s performance. Well, I started out as a skeptic, too. But once I sat down and actually *used* a computer with a 10,000 RPM drive, my opinion did a complete about-face. I was blown away by how responsive and snappy it felt compared to my machine with a 7,200 RPM hard drive. It’s a substantial difference that I continue to feel every day in typical use. **Don’t underestimate the impact of hard drive performance on your everyday use of the computer.**


![](https://blog.codinghorror.com/content/images/2025/05/image-482.png)


The difference in performance between a 7,200 RPM boot drive and a 10,000 RPM boot drive is not subtle in any way. But don’t take my word for it. Surf the benchmarks yourself:

- [StorageReview.com’s review of the 150GB WD Raptor](https://web.archive.org/web/20070301201357/http://www.storagereview.com/articles/200601/WD1500ADFD_4.html)
- [AnandTech’s review of the 150GB WD Raptor](http://www.anandtech.com/storage/showdoc.aspx?i=2760&p=7)
- [TechReport’s review of the 150GB WD Raptor](https://web.archive.org/web/20070316130736/http://techreport.com/reviews/2006q2/raptor-wd1500/index.x?pg=1)


Unfortunately, the Raptors aren’t large drives, and they’re expensive on a per-megabyte basis. Current pricing is about $140 for the 74 GB model, and $180 for the 150 GB model. But once you factor in the incredible performance, and the idea that your don’t need a lot of space on your primary drive because your secondary drive will be the large workhorse storage area, I think it’s a completely reasonable tradeoff.


A number of people have expressed concerns that a 10,000 RPM drive will be run hot and noisy. I am [a noise fanatic](https://blog.codinghorror.com/building-a-quiet-pc/), and I can assure you that this is not the case. According to the [StorageReview noise and heat analysis](https://web.archive.org/web/20071022033724/http://www.storagereview.com/), the Raptor is squarely in the ballpark with its 7,200 RPM peers. I mount all my drives with [sorbothane](http://www.sorbothane.com/), and I use eggcrate foam on nearby surfaces to further reduce any reflected noise. Once I do this, the Raptor is no noisier than any other 3.5" desktop hard drive I’ve used.


Setting aside the performance argument for a moment, using two hard drives also provides additional flexibility. Although [I cannot recommend RAID 0](https://blog.codinghorror.com/desktop-raid-oversold/) on the desktop, there are clear benefits to using two standalone hard drives. You can isolate your essential user data from the operating system by storing it on the larger, secondary drive. This gives you the freedom to blow away your primary OS drive with relative impunity. It’s also [optimal for virtual machine use](https://blog.codinghorror.com/the-single-most-important-virtual-machine-performance-tip/), as one drive can be dedicated to OS functions and the other can act exclusively as a virtual disk. There are plenty of usage scenarios where taking advantage of two hard drive spindles can provide a serious performance boost, such as extracting a large archive from one drive to another.


It’s gotten to the point now where **I won’t even consider building a machine *without* a Raptor as the boot drive**. Sure, your computer may have 2 or even 4 gigabytes of memory, but going to disk is inevitable. And every time you go to disk, you’ll become thoroughly spoiled by the speed of the Raptor.


You may not know it yet, but **you want a 10,000 RPM boot drive, too**. In the words of Scott Hanselman: [Go on. Treat yourself](http://www.hanselman.com/blog/ImTotallyVistaedNowUpgradingTheFamilyToVista.aspx). I guarantee you won’t be disappointed.

[hardware](https://blog.codinghorror.com/tag/hardware/)
[storage](https://blog.codinghorror.com/tag/storage/)
[solid state drive](https://blog.codinghorror.com/tag/solid-state-drive-2/)
[performance](https://blog.codinghorror.com/tag/performance/)
[computer build](https://blog.codinghorror.com/tag/computer-build/)
