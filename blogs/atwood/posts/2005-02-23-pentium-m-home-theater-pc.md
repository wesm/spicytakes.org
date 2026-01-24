---
title: "Pentium-M Home Theater PC"
date: 2005-02-23
url: https://blog.codinghorror.com/pentium-m-home-theater-pc/
slug: pentium-m-home-theater-pc
word_count: 613
---

I recently built a new, much lower wattage home theater PC using the Pentium-M processor. The P-M was, until very recently, a mobile-only part. And that’s why it’s ideal for HTPC duties – it offers very high levels of performance at an astonishingly modest power draw. For example, per these [system power consumption measurements](https://web.archive.org/web/20050227052512/http://techreport.com/reviews/2005q1/pentium4-600/index.x?pg=16) at Tech-Report:


Pentium 4 640 @3.2ghz
125w idle, **211w** load


Pentium-M @ 2.4ghz (overclocked)
92w idle, **107w** load


So the P-M system consumes 35% less power at idle and 97% less power at load – while offering comparable performance. The Pentium-M is much more efficient per clock, so it doesn’t *need* to run at exorbitant clock rates. There’s a direct correlation between power consumption and heat/noise. The cooler a system runs, the quieter it will be. And quiet is what you want for a HTPC.


In my bench testing of the Pentium-M 1.6ghz, **the large, fanless Alpha heatsink never exceeded 50c under Prime95 torture test load**, even when left running overnight. And that’s totally passive, with virtually zero directed airflow! Try that with a Pentium 4 and you’ll create your own personal [China Syndrome](http://www.imdb.com/title/tt0078966/). Because the P-M runs so cool, I was able to get away with using only two fans in the final system – the power supply fan, and a dramatically undervolted 60mm exhaust fan:


![](https://blog.codinghorror.com/content/images/2025/05/image-54.png)


See the three hard drives in there? Two are mounted under the DVD-R. Here’s a breakdown of all the parts.


**Core system**

- AOpen i855GMEm mobo
- 1.6ghz Pentium-M “Dothan” (2mb L2 cache)
- Alpha PAL8952 P4 heatsink
- Zalman northbridge cooler
- 512mb DDR


**Storage**

- Samsung Spinpoint 160gb (3)
- Generic 4x DVD-R


**Case**

- Logisys acrylic HTPC case
- Sparkle 180w MicroATX power supply


**Expansion cards**

- Radeon 9600 128mb AGP, passively cooled with Zalman ZM-17
- Generic PCI 802.11 b/g adapter
- Hauppauge PVR-350
- AOpen SPDIF bracket


The AOpen mobo offers voltage and bus speed controls; I undervolted the P-M from ~1.3v to ~1.1v, and overclocked it to 1.7ghz. This system, as measured by my [trusty Kill-a-Watt](https://web.archive.org/web/20050225094038/http://www.the-gadgeteer.com/killawatt-review.html), consumes 72w at windows desktop and 81w in [Prime95 torture test](http://www.mersenne.org/freesoft.htm). Now, that’s power draw from the wall; due to inefficiencies in all power supplies, some of that power is immediately lost as conversion heat inside the PSU. A typical power supply is about 70 percent efficient, so the actual power consumption inside the PC is closer to **50w idle / 57w load**. Pretty amazing for a fully loaded 1.7ghz PC that performs like a Pentium 4 2.6ghz.


When building a quiet PC, pay close attention to the hard drives and video card you use:

1. Modern video cards are the **second largest consumer of power** after the CPU; I recommend the Radeon 9600 which is an outstanding blend of respectable DX9 performance and ultra-low power consumption. They are trivial to cool passively. Can you get a faster card? Sure, at double or triple the power budget. Do be careful to avoid the hotter running 9600XT models; 9600Pros are fine but will require a passive heatsink retrofit.
2. **Hard drives are the second loudest item in your system after the fans**. Unfortunately, very few hard drive manufacturers make low noise a priority, although that is slowly changing. It helps to decouple your hard drives; they are spinning significant chunks of metal at 7,200rpm. I used [sorbothane](http://www.sorbothane.com/) in my case to soft mount the drives and damp vibration. That definitely helps, but it can’t silence a fundamentally noisy drive. **Buy a quiet hard drive or you’ll regret it**. I’ve had excellent results with the Samsung Spinpoints, which are a favorite of silent PC enthusiasts.

[processor](https://blog.codinghorror.com/tag/processor/)
[pentium-m](https://blog.codinghorror.com/tag/pentium-m/)
[htpc](https://blog.codinghorror.com/tag/htpc/)
[power efficiency](https://blog.codinghorror.com/tag/power-efficiency/)
[performance](https://blog.codinghorror.com/tag/performance/)
