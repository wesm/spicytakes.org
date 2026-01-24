---
title: "Running XP with the pagefile disabled"
date: 2005-10-19
url: https://blog.codinghorror.com/running-xp-with-the-pagefile-disabled/
slug: running-xp-with-the-pagefile-disabled
word_count: 597
---

If you have 2 gigabytes (or more) of memory in your PC, **have you considered turning off your pagefile?** Here’s how to do it:

1. Control Panel, System
2. Advanced tab
3. Performance group, Settings button
4. Advanced tab
5. Virtual Memory group, Change button
6. Select “No paging file” and click Set, then OK.


![](https://blog.codinghorror.com/content/images/2025/03/image-332.png)


I’ve heard people talk about this before, but I had always disregarded it as crazy talk. The pagefile is a critical [part of the operating system](https://web.archive.org/web/20051112143633/http://www.windowsdevcenter.com/pub/a/windows/2004/04/27/pagefile.html):


> *The paging file (pagefile.sys) is a hidden system file that forms a key component of the Virtual Memory Manager (VMM) on Windows platforms. The origin of this file dates back to early 1990s when Windows ran on PC hardware that had limited physical memory due to the high cost of RAM and the limitations of motherboard design. (The concept of virtual memory itself, of course, is *[*much older*](https://web.archive.org/web/20051201152344/http://cne.gmu.edu/itcore/virtualmemory/vmhistory.html)*.) The purpose of the pagefile was to allow memory-hungry applications to circumvent insufficient RAM by allowing seldom-used pages of RAM to be swapped to disk until needed (hence the term swapfile used on earlier Windows platforms). For example, if a Windows 3.1 machine had 8MB of RAM and a 12MB permanent swap file (386spart.par) on its C: drive, then the effective memory that applications could use was 8 + 12 = 20MB.*


This idea was indeed crazy in a world where 256mb, 512mb and 1gb of memory were the norm. **Now that 2 gb of memory is relatively common, disabling the pagefile isn’t such a crazy idea any more.**


A number of developers are already running their systems with the pagefile disabled, as [this post](https://web.archive.org/web/20051218205345/http://agileprogrammer.com/geeknoise/archive/2005/10/16/8673.aspx) by Peter Provost illustrates. Clearly it works. I’ve been running this way for a few days, and I haven’t encountered any issues yet.


However, I’m not so sure there’s any practical performance increase from disabling your pagefile. **If our systems were never running out of physical memory with 2gb, then theoretically the pagefile never gets used anyway.** And disabling the pagefile also introduces a new risk: if an app requests more memory than is physically available, it will receive a stern “out of memory” error instead of the slow disk-based virtual memory the OS would normally provide. [This Q&A outlines the risks](https://web.archive.org/web/20051212123318/http://emea.windowsitpro.com/Article/ArticleID/42080/42080.html?Ad=1):


> ***So, if you have a lot of RAM, you don’t need a pagefile, right?** Not necessarily. When certain applications start, they allocate a huge amount of memory (hundreds of megabytes typically set aside in virtual memory) even though they might not use it. If no pagefile (i.e., virtual memory) is present, a memory-hogging application can quickly use a large chunk of RAM. Even worse, just a few such programs can bring a machine loaded with memory to a halt. Some applications (e.g., Adobe Photoshop) will display warnings on startup if no pagefile is present.
> My advice, therefore, is not to disable the pagefile, because Windows will move pages from RAM to the pagefile only when necessary. Furthermore, you gain no performance improvement by turning off the pagefile. To save disk space, you can set a small initial pagefile size (as little as 100MB) and set a high maximum size (e.g., 1GB) so that Windows can increase the size if needed. With 1GB of RAM under normal application loads, the pagefile would probably never need to grow.*


This is one case where the 32-bit process [memory limit of 4 gigabytes](https://web.archive.org/web/20051125084849/http://www.brianmadden.com/content/content.asp?ID=69) – which is really 2 gigabytes once you factor in the Windows kernel memory split – works in our favor.

[virtual memory](https://blog.codinghorror.com/tag/virtual-memory/)
[pagefile](https://blog.codinghorror.com/tag/pagefile/)
[windows operating system](https://blog.codinghorror.com/tag/windows-operating-system/)
[system performance](https://blog.codinghorror.com/tag/system-performance/)
