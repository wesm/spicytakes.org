---
title: "DMG Kernel Panic Security Issue"
date: 2006-11-21
url: https://daringfireball.net/2006/11/dmg_kernel_panic
slug: dmg_kernel_panic
word_count: 187
---


[The latest “Month of Kernel Bugs” issue](http://blog.washingtonpost.com/securityfix/2006/11/exploit_released_for_unpatched_2.html) is quite serious: a “.dmg” disk image file which, if you attempt to mount it, will cause a kernel panic on any up-to-date Mac running 10.4.8.


You should be safe, of course, because you read Daring Fireball, and so you know that you should [turn *off* Safari’s incredibly foolish “Open ‘safe’ files after downloading” preference](http://daringfireball.net/search?q=open+safe+files+after+downloading). But given that this preference, which in my opinion shouldn’t even exist, is *on* by default, most Mac users are vulnerable to attack via this exploit. If you have this preference turned off, you’ll still get a kernel panic if you manually attempt to mount the disk image, but if you have the preference turned on, you’ll get a kernel panic *just by downloading the file* — and any web site you visit can initiate a file download automatically.


Question for Apple: How many times must this Safari preference be exploited before you remove it from Safari, or at least turn it off by default?



| **Previous:** | [Pinprick](https://daringfireball.net/2006/11/pinprick) |
| **Next:** | [Palm CEO Ed Colligan’s Head Seems to be Stuck Somewhere](https://daringfireball.net/2006/11/colligan_head_stuck) |


PreviousNext