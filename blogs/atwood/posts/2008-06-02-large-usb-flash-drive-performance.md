---
title: "Large USB Flash Drive Performance"
date: 2008-06-02
url: https://blog.codinghorror.com/large-usb-flash-drive-performance/
slug: large-usb-flash-drive-performance
word_count: 998
---

In the last three years, I’ve gone from [carrying](https://blog.codinghorror.com/whats-on-your-keychain/) a **512 MB** USB memory stick to a **16 GB** USB memory stick. That’s pretty amazing.


According to the [storagereview.com archives](https://web.archive.org/web/20080610204647/http://www.storagereview.com/legacy.sr), hard drives with 16 GB of storage were introduced sometime around the beginning of 1999. Barely 10 years later, we carry around that much on our *keychains*. Heck, [my laptop](https://blog.codinghorror.com/dell-xps-m1330-review/) only has a 32 GB solid state drive, and I manage to scrape by with that. These things are essentially miniature hard drives. I’m starting to wonder why we don’t just take our entire computing environment, operating system and all, along with us and boot it up on whatever computer we happen to encounter in the wild.


There is one big problem with this approach, however. **USB flash drive performance, even for the best models, is a small fraction of typical hard drive performance.**


Modern 2.5" hard drive performance looks [something like this](https://web.archive.org/web/20080620074335/http://www.xbitlabs.com/articles/storage/display/25inch-hdd-250gb_3.html#sect2):

kg-card-begin: html


| HDD Sequential Read | 55 MB/sec |
| HDD Sequential Write | 55 MB/sec |


kg-card-end: html

Mind you, those aren’t particularly fantastic numbers, just typical ones. You can get *significantly* faster hard drives, such as the Western Digital Velociraptor I just bought. Storage Review [described the Velociraptor](https://web.archive.org/web/20080605234639/http://www.storagereview.com/WD3000BLFS.sr) thusly:


> *single-user scores... blow away those of every other [hard drive]*


I was immediately sold once I read that. It’s not cheap, but you get what you pay for, and I’m firmly in the “hard drive performance matters” camp. To quote [Ferris Bueller](http://www.imdb.com/title/tt0091042/quotes), it is so choice. If you have the means, I highly recommend picking one up.


But what about large USB flash drives? How do they compare to typical hard drive speeds, much less the awe-inspiring Velociraptor? X-Bit Labs recently reviewed three [32 GB USB flash drives](https://web.archive.org/web/20080916184000/http://www.xbitlabs.com/articles/memory/display/32gb-usb-flash_3.html#sect2):

kg-card-begin: html


|  | Sequential Read | Seqential Write |
| [32 GB Corsair Flash Voyager](http://www.amazon.com/dp/B000XUMR6C) | 22 MB/sec | 10 MB/sec |
| [32 GB OCZ Rally 2](http://www.amazon.com/dp/B0013RKFB8) | 30 MB/sec | 22 MB/sec |
| [32 GB Patriot Xporter XT](http://www.amazon.com/dp/B0011EA4V4) | 31 MB/sec | 17 MB/sec |


kg-card-end: html

Not bad by any means, but *punishing* next to typical hard drive throughput. If you really were booting and running your operating system entirely from a USB flash drive, you’d feel like you had stepped back in time five full years.


Even if you’re only planning to use your USB flash drive for the mundane task of storing files, **you should care deeply about read and write speeds**. Throughput wasn’t much of an issue when USB drives were “only” a gigabyte or two. But when we’re talking about 8 GB, 16 GB or 32 GB of data, being limited to 10 MB/sec write speeds means 13, 26, and 52 minutes respectively to fill that flash drive up with data. Do you have that kind of time?


The OCZ Rally 2 flash drive appears to be the winner in the Xbit labs roundup, but does the 32 GB size really offer the best bang for your buck? I did a quick spot check of OCZ Rally 2 flash drive prices on Amazon:

kg-card-begin: html


| 2 GB | $17 | $8.50/GB |
| 4 GB | $26 | $6.50/GB |
| 8 GB | $37 | $4.62/GB |
| 16 GB | $78 | $4.88/GB |
| 32 GB | $136 | $4.25/GB |


kg-card-end: html

Surprisingly, yes. The 32 GB OCZ Rally2 flash drive offers the best price per gigabyte of storage. I actually didn’t do the math before I purchased, thinking that the 16 GB one would be a better deal. Now I wish I had! I just noticed there’s a $20 rebate on the 32 GB model, too, which makes it an even more outstanding deal.


I wasn’t sure which 16 GB flash drive would be faster – the Corsair Flash Voyager, or the OCZ Rally 2. So I ended up purchasing both.


![](https://blog.codinghorror.com/content/images/2025/04/image-135.png)


![](https://blog.codinghorror.com/content/images/2025/04/image-134.png)


I formatted both of the drives with the default NTFS filesystem and did a bit of ad-hoc testing in Vista. You can find the [raw ReadyBoost benchmark results](https://web.archive.org/web/20080605173903/http://www.techcrater.com/2007/04/06/how-to-find-readyboost-speed-rating/) if you know where to look in the event viewer.

kg-card-begin: html


|  | [16 GB Corsair
Flash Voyager](http://www.amazon.com/dp/B000LXTUT8) | [16 GB OCZ
Rally 2](http://www.amazon.com/dp/B000ZGX3P8) |
| 3GB ISO Copy, Read | 26 MB/sec | 26 MB/sec |
| 3GB ISO Copy, Write | 9 MB/sec | 10 MB/sec |
| Readyboost Random Read | 6,426 KB/sec | 6,434 KB/sec |
| Readyboost Random Write | 3,292 KB/sec | 4,695 KB/sec |


kg-card-end: html

In practice, the Rally is noticeably faster at writing, and a smidge faster at reading (not exposed here, but the chddspeed results confirm this). Not the results I expected based on reading the Xbit Labs review, but apparently there’s quite a bit of variance for USB flash drives depending on the vagaries of manufacturing and what particular flash memory chips the manufacturer happened to be using that month.


The results are close enough that you may want to pick on ergonomics rather than performance. The Corsair drive has a chunky rubberized coating, which works well on a keychain (less jangly, more durable) but becomes annoying in a pocket or next to a narrow USB slot. I think I prefer the Rally’s narrower metallic casing. Since it is a slightly better performer overall, the OCZ Rally 2 series gets my recommendation, if you’re in the market.


One caution: if you *do* plan to use your USB flash drive to run applications or even operating systems, **pay close attention to the random read and write speeds**. Sequential throughput is a good overall baseline, but it’s not the entire performance story. While typical portable storage usage does correlate well with sequential throughput, applications running on a USB flash drive are largely bounded by random access throughput.


You can never have enough storage on your keychain. Now if I can just figure out what else to put on mine...

[storage](https://blog.codinghorror.com/tag/storage/)
[usb flash drive](https://blog.codinghorror.com/tag/usb-flash-drive/)
[performance](https://blog.codinghorror.com/tag/performance/)
[hard drives](https://blog.codinghorror.com/tag/hard-drives/)
[technology trends](https://blog.codinghorror.com/tag/technology-trends/)
