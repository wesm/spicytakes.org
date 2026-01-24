---
title: "Web 2.0 and The “Whatever Box” Server"
date: 2006-04-24
url: https://blog.codinghorror.com/web-2-0-and-the-whatever-box-server/
slug: web-2-0-and-the-whatever-box-server
word_count: 493
---

One of the key differences between the original dot-com bubble and the Web 2.0 bubble we’re entering now is that our servers are a lot cheaper and a lot more powerful. [Moore’s Law](http://en.wikipedia.org/wiki/Moore's_law) in action isn’t exactly news, but the new web is definitely [powered by cheap "whatever boxes"](http://bnoopy.typepad.com/bnoopy/2005/06/its_a_great_tim.html):


> In the 10 years between Excite and JotSpot, hardware has literally become 100X cheaper. It’s two factors – Moore’s law and the rise of Linux as an operating system designed to run on generic hardware. Back in the Excite days, we had to buy proprietary Sun hardware and Sun hard drive arrays. Believe me, none of it was cheap. Today, we buy generic Intel boxes provided by one of a million different suppliers.


We recently specced out a new server at work and I was curious about this: **exactly how much more powerful did servers get in the last six years?**


The parts list for our homebrew server is saved in a Newegg wish list. I set out to find a year 2000 equivalent by looking up a typical Dell server on the mid-2000 internet archive of Dell’s website. According to that page, an entry-level [PowerEdge 4400](https://web.archive.org/web/20060427172357/http://support.dell.com/support/edocs/systems/pe4400/en/index.htm) server started at **$4,814**. I can’t get to the detailed spec pages, so I’m estimating the entry-level specs based on the many PowerEdge 4400 machines for sale on eBay.

kg-card-begin: html


| **Typical 2006 server** | **Typical 2000 server** |
| Dual Core 64-bit CPU, 2.0 Ghz | Two 32-bit CPUs, 733 Mhz |
| 4 GB DDR400 memory | 512mb PC133 ECC memory |
| 150 GB 10,000 RPM SATA-II mirrored | 9 GB 10,000 RPM UltraSCSI mirrored |
| 1000baseT network | 100baseT network |
| $1,743 | $4,814 |


kg-card-end: html

Now, this comparison isn’t entirely fair. The PowerEdge 4400 supports real hot-swappable power supplies and hardware RAID-ed hard drives; our homebrew rig has to be powered down to switch out a failed hard drive or (single) power supply.


But the general thrust of the comparison is still valid. In a nutshell, we get...

- 10x the network bandwidth
- 8x the memory
- 4x the memory bandwidth
- 16x the disk space
- 10x the CPU power


... all for about one-third the price. And we have the luxury of running a commonly available 64-bit operating system in [native 64-bit mode](https://blog.codinghorror.com/64-bit-desktop-vs-64-bit-server/), too.


I would still argue that the the relative costs of software and hardware – relative to the cost of human labor, I mean – haven’t changed that much in the last six years. But you can plainly see where **this extravagant excess of server power makes it possible to use labor-saving software that wasn’t viable in the year 2000**. You can build your site on extremely high-level software, such as [interpreted languages](https://blog.codinghorror.com/the-day-performance-didnt-matter-any-more/) like Ruby and Python, and still scale across thousands of simultaneous user requests... even on a single “whatever box” server.

[server](https://blog.codinghorror.com/tag/server/)
[technology trends](https://blog.codinghorror.com/tag/technology-trends/)
[hardware](https://blog.codinghorror.com/tag/hardware/)
[web 2.0](https://blog.codinghorror.com/tag/web-2-0/)
[moore's law](https://blog.codinghorror.com/tag/moores-law/)
