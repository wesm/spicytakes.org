---
title: "Virtual PC 2004 tips"
date: 2005-02-08
url: https://blog.codinghorror.com/virtual-pc-2004-tips/
slug: virtual-pc-2004-tips
word_count: 450
---

I’m working with Microsoft’s [Virtual PC 2004](https://blog.codinghorror.com/virtual-pc-2004/) again. Since the last time I discussed VPC, Microsoft released the essential Virtual PC 2004 Service Pack 1, which addresses a lot of outstanding issues, particularly compatibility with SP2 and newer AMD/Intel processors.


If you start delving into VPC, I highly recommend reading through the excellent [Virtual PC FAQ](https://web.archive.org/web/20050213101431/http://www.robertmoir.co.uk/win/VirtualPC2004FAQ.html). The biggest bugaboo is, of course, performance. This is the price we pay for the flexibility of virtualized hardware. Although performance is decent once you get the OS up and running, the OS installs themselves can be downright brutal. Plan for at least two hours for any OS install, and possibly many more.


Even if you have fire-breathing PC hardware – and [any self-respecting developer should](https://blog.codinghorror.com/athlon-64-developers-choice/), because time is money, and PCs are cheap these days – you’ll be disappointed with Virtual PC performance. It’s adequate, nothing more. Scott Hanselman has some great [Virtual PC performance tips](http://www.hanselman.com/blog/PermaLink,guid,097ce75a-838a-4511-a858-d6de8e8e78a9.aspx) direct from Microsoft. Some interesting comments on performance targets:

kg-card-begin: html

> *
> Ideally Virtual PC performance is at:
> CPU: 96-97% of host
> Network: 70-90% of host
> Disk: 40-70% of host
> *

kg-card-end: html

Evidently, **emulated disk performance is terrible**. I use dynamically expanding disk images for flexibility, but it might be worth experimenting with fixed-size disk images, dedicating a separate drive to VPC, or even the oddball physical drive mapping mode (see the Virtual PC FAQ) to get around that bottleneck. This also means you never, ever want to starve your VMs for memory. If these guys start paging to disk, you’ll be in a world of hurt. Oddly, video performance is not mentioned there. The emulated video hardware is also substantially slower than a native device, but is typically less of a bottleneck in real world usage (well, until Longhorn, but let’s not go there right now). These percentages jibe with the [Virtual PC benchmarks](http://www.osnews.com/story.php?news_id=1054) I found. The CPU, memory, and network performance is respectable – **the biggest performance problems in Virtual PC are caused by the slow emulated disk and video subsystems.**


When installing operating systems, it’s important to know exactly which devices Virtual PC emulates:

- S3 Trio Video Card
- Intel / DEC 21140 Network Card
- Soundblaster 16 ISA PnP Sound Card
- Intel 440BX Motherboard Chipset


Host CPU is equal to your physical CPU, obviously. This isn’t that kind of emulation. Why did they choose to emulate these particular devices? [Compatibility](https://web.archive.org/web/20051204042429/http://blogs.msdn.com/virtual_pc_guy/archive/2005/01/26/361361.aspx).


Also, VirtualPC is slow enough as-is without torturing yourself with physical floppies or CDs. **Always use disk image files!** You’ll want WinImage for making floppy images, and something like [LC ISO Creator](https://web.archive.org/web/20050215202329/http://www.lucersoft.com/freeware.php) for creating CD/DVD ISO images.

[microsoft](https://blog.codinghorror.com/tag/microsoft/)
[virtual pc 2004](https://blog.codinghorror.com/tag/virtual-pc-2004/)
[virtualization](https://blog.codinghorror.com/tag/virtualization/)
[performance](https://blog.codinghorror.com/tag/performance/)
[tips](https://blog.codinghorror.com/tag/tips/)
