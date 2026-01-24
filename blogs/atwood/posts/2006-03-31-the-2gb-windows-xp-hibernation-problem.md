---
title: "The 2GB Windows XP Hibernation Problem"
date: 2006-03-31
url: https://blog.codinghorror.com/the-2gb-windows-xp-hibernation-problem/
slug: the-2gb-windows-xp-hibernation-problem
word_count: 346
---

If you...

- use Windows XP SP2 of any flavor
- have 1+ gigabytes or more of system memory
- use hibernate functionality


... you may have experienced this error at some point when attempting to hibernate:


![](https://blog.codinghorror.com/content/images/2025/05/image-247.png)


I know I have. It drives me nuts, because my system fails to hibernate after I’ve already initiated the hibernation process and walked away from it. This is on my desktop.* You can imagine how catastrophic this could be on a laptop; you’d be putting a laptop in your bag that was still fully on!


To avoid the error, install [this Microsoft hotfix](https://web.archive.org/web/20060409220409/http://www.u-g-h.com/InsufficientSystemResourcesExistToCompleteTheAPISOLIVED.aspx), which is graciously hosted by Owen Cutajar. It’s from Microsoft KB909095, which also explains the problem in a bit more detail:


> *To prepare the computer to hibernate, the Windows kernel power manager requires a block of contiguous memory. The size of this contiguous memory is proportional to the number of physical memory regions that the computer is using. A computer that uses lots of RAM is likely to use more physical memory regions when the computer prepares to hibernate. Therefore, a larger amount of contiguous memory is required to prepare the computer to hibernate.
> Additionally, the number of physical memory regions varies according to the programs, services, and device drivers that the computer uses. Therefore, the hibernate feature occasionally fails.
> When the Windows kernel power manager detects that the hibernate feature has failed, the hibernate feature remains disabled until you restart the computer.*


I originally researched this back in December, but the problem wasn’t happening with enough frequency to make me call Microsoft support and dig up a hotfix. Now it is. And people have mirrored the patch so we don’t have to go through **the busywork exercise of calling Microsoft support to obtain a necessary hotfix.** What a ridiculous policy.


*I would use sleep, but the motherboard I use isn’t smart enough to restore the correct overclocked CPU speed. I get bumped down to stock CPU speeds every time I resume from a sleep state.

[windows xp](https://blog.codinghorror.com/tag/windows-xp/)
[hibernation](https://blog.codinghorror.com/tag/hibernation/)
[hotfix](https://blog.codinghorror.com/tag/hotfix/)
[system memory](https://blog.codinghorror.com/tag/system-memory/)
