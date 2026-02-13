---
title: "Solid State Disks"
date: 2009-03-27
url: https://www.joelonsoftware.com/2009/03/27/solid-state-disks/
word_count: 638
---


One of the FogBugz developers complained that compiling was pretty slow (about 30 seconds), which was leading to a lot of [sword fights in the hallway](http://xkcd.com/303/). He asked if it would be OK if someone spent a few weeks looking for ways to parallelize and speed it up, since we all have multiple CPU cores and plenty of memory.


Intel Corp.I thought it might be a good idea to just try throwing money at the problem first, before we spent a lot of (expensive and scarce) developer time. And I had just read a [glowing review](http://www.anandtech.com/printarticle.aspx?i=3531) by Anand Lal Shimpi of the [Intel X25-M SSD](http://www.intel.com/design/flash/nand/mainstream/index.htm), so I thought I’d experiment with replacing some of the hard drives around here with solid state, flash hard drives to see if that helped.


The first experiment was trying to rejuvenate an 18 month old IBM Thinkpad X61s notebook, which I originally got for the FogBugz World Tour. I got the new, 160GB Intel X25-M drives, which are about $760 on NewEgg.com.


The trick in replacing your main, boot hard drive is making an exact copy of the partitions, [MBR](http://en.wikipedia.org/wiki/Master_boot_record), and data, from the old drive to the new one. There are several apps that can do this. There’s an open source app called [Clonezilla](http://clonezilla.org/), which, I have to say, is only free if your time is worthless. Two of the popular commercial applications I tried are [Symantec Norton Ghost 14](http://www.symantec.com/norton/ghost) and [Acronis Migrate Easy 7.0](http://www.acronis.com/homecomputing/products/migrateeasy/).


With the Thinkpad, neither Ghost nor Acronis worked right. I think there’s something unusual about the MBR on ThinkPads. The bottom line was that every time I attempted to clone the drive, I got an unbootable drive. I wasted about a day and a half trying lots of different things. I even tried booting with a Ubuntu Live CD and copying all the files (this doesn’t work right, and leaves Windows apparently working, but actually broken in many tiny ways).


Eventually I gave up and just reinstalled everything from scratch. Not fun, but now I have a fresh new machine with a bigger, faster solid state drive.


ThermaltakeOne tool which was really helpful: the [Thermaltake BlacX Docking Station](http://www.thermaltakeusa.com/Product.aspx?C=1346&ID=1642). It’s a toaster for raw SATA hard drives, either 2.5” or 3.5”. You drop any hard drive in the top and plug the USB 2.0 plug into your computer and, poof, the hard drive is connected. $37 at NewEgg.


I did a little bit of benchmarking… don’t take these numbers too seriously since I didn’t run many tests and it’s hard to get everything right. Boot time dropped from 2:11 to 0:34. That’s from a cold boot to launching Firefox and navigating to google.com. Launching 6 major applications went from about 20 seconds to about 10 seconds. In general, the fact that app launching is so much faster makes a *huge* difference and it was totally worth it. This little laptop is now the fastest computer I’ve ever used.


For my next experiment, I upgraded the main desktop, a Dell Optiplex 745. This time Acronis Migrate Easy worked perfectly the first time. Literally all I had to do was clone the drive, turn off the computer, and replace the old drive with the new one, and I was done. Plink!


Suddenly everything was faster. Booting, launching apps… even Outlook is ready to use in about 1 second. This was a really great upgrade.


But… compile time. Hmm. That wasn’t much better. I got it down from 30 seconds to … 30 seconds.


Our compiler is single threaded, and, I guess, a lot more CPU-bound than IO bound. Oh well. We’ll still probably upgrade all the developer’s desktops with SSD drives, because making everything *else *snappy will make their lives better, but we may still be forced to spend some time making the compiler do its work in parallel.
