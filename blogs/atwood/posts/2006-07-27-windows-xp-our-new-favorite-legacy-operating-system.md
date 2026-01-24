---
title: "Windows XP, Our New Favorite Legacy Operating System"
date: 2006-07-27
url: https://blog.codinghorror.com/windows-xp-our-new-favorite-legacy-operating-system/
slug: windows-xp-our-new-favorite-legacy-operating-system
word_count: 735
---

John Gruber gloats that Windows XP does not fare well in a [comparison against OS X](http://daringfireball.net/2006/04/windows_the_new_classic):

kg-card-begin: html

> But everything about Boot Camp is calibrated to position Windows-on-Mac as the next Classic-style ghetto  –  a compatibility layer that you might need but that you wish you didn’t.
> Even the Boot Camp logo:
> reinforces this. It’s a bastardized variant of Microsoft’s Windows logo, sans color, and with the whitespace between the four panels forming a hidden “X,” la [the hidden arrow](https://web.archive.org/web/20060813191318/http://www.thesneeze.com/mt-archives/000273.php) in the FedEx logo.
> [Microsoft is] stuck with the fact that in a fair shoot-out, Mac OS X is better. It looks better, it’s better designed, it’s more exciting, more intriguing, more satisfying. Cf. This [joke from an anonymous poster](http://minimsft.blogspot.com/2006/03/vista-2007-fire-leadership-now.html#c114302448628930798) in the comments at Mini-Microsoft’s weblog:
>  What’s the difference between OS X and Vista?
> Microsoft employees are excited about OS X…

kg-card-end: html

What’s conspicuously missing from this comparison is any mention of the fact that Windows XP was originally released in *October 2001*.


In the intervening five years, Apple’s OS X has seen [five major releases](http://en.wikipedia.org/wiki/Mac_OS_X#Timeline_of_Apple_Macintosh_operating_systems). If you squint your eyes, tilt your head, and look at it from a distance, perhaps you could consider [Service Pack 2](https://web.archive.org/web/20060811233949/http://www.microsoft.com/windowsxp/sp2/default.mspx) a point release. But any way you slice it, **Windows XP is going on five years old now**. That’s ancient. It’s also the longest time Microsoft has ever gone between [major releases of Windows](http://en.wikipedia.org/wiki/History_of_Microsoft_Windows#Timeline).


Consider the minimum system requirements for Windows XP:

- 233 MHz processor
- 64 MB of RAM (128 MB recommended)
- Super VGA (800 x 600) display
- CD-ROM or DVD drive
- Keyboard and mouse


The cost of a license to Windows XP is – quite literally – more expensive than purchasing a PC that meets these minimum specs today.


What Gruber doesn’t realize is that relegating Windows XP to “Classic” status isn’t an insult. It’s simply acknowledging what every Windows user already knows: **Windows XP is a legacy operating system.**


![](https://blog.codinghorror.com/content/images/2025/05/image-468.png)


And there’s no shame in it.


Look at the age of UNIX, which OS X is based on. In the same way that OS X is a modern remodeling of its BSD and Mach kernel origins, Windows Vista will be a much-needed modern renovation of the XP core.


But in the meantime, as the guys at Engadget [recently said](http://www.engadget.com/2006/07/28/microsoft-exec-avoids-confirming-vista-release/):


> At this point we don’t really know what to expect anymore, and since **our current XP-powered setup already does everything we need it to**, we’re getting pretty close to not caring if Vista is ever released at all.


I’m perfectly content to use Windows XP “classic,” as long as Windows Vista is on the horizon for 2007.


And there are other benefits to Windows XP’s advanced age, too.


Since XP’s minimum system requirements are absurdly low by today’s standards, you’ll have no problem running Windows XP – even *multiple instances* of Windows XP – in a virtual machine on a modern development PC. My optimized, fully-patched Windows XP SP2 [Virtual Machine image](https://blog.codinghorror.com/creating-smaller-virtual-machines/) is down to **587 megabytes**. That’s a mere 139 megabytes as a self-extracting RAR file.


Most apps run fine in Windows XP with 128 megabytes or 160 megabytes of memory. For example, here’s a screenshot of IE 7, Beta 3. It’s running in an optimized Windows XP virtual machine with **only 128 megabytes of memory:**


![](https://blog.codinghorror.com/content/images/2025/05/image-469.png)


That’s with four tabs open to ESPN, eBay, Yahoo news, and MSN. Even with all that going on, I have more than 20 megabytes of free memory. And my commit charge total is well under the physical memory total. There’s still room for more stuff!


Clearly, **if all you need to do is test IE7 beta 3 in a virtual machine, a humble developer machine with 512 megs of memory will work fine.*** Of course, you still need to be careful if you don’t have a gigabyte or more of system memory. There are [more detailed guidelines](https://web.archive.org/web/20070205133201/http://blogs.msdn.com/virtual_pc_guy/archive/2005/09/22/473045.aspx) at the Virtual PC guy blog.


Here’s the complete Task Manager process list for this VM, if you’re curious.


![](https://blog.codinghorror.com/content/images/2025/05/image-470.png)


I see a few services that could be disabled to free up even more memory.


*However, if you’re working at a job where developers are expected to work on machines with less than 1 gigabyte of memory, it’s definitely time to start looking for a new job.

[operating systems](https://blog.codinghorror.com/tag/operating-systems/)
[windows xp](https://blog.codinghorror.com/tag/windows-xp/)
[mac os x](https://blog.codinghorror.com/tag/mac-os-x/)
[software compatibility](https://blog.codinghorror.com/tag/software-compatibility/)
[os comparison](https://blog.codinghorror.com/tag/os-comparison/)
