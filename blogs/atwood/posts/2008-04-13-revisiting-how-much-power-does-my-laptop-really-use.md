---
title: "Revisiting “How Much Power Does My Laptop Really Use?”"
date: 2008-04-13
url: https://blog.codinghorror.com/revisiting-how-much-power-does-my-laptop-really-use/
slug: revisiting-how-much-power-does-my-laptop-really-use
word_count: 1009
---

Back in 2006, I [examined the power usage](https://blog.codinghorror.com/how-much-power-does-my-laptop-really-use/) of my Dell Inspiron 300M laptop. It was the first ultraportable I ever owned, and I fell in love with it. I stuck it out as long as possible on that wonderful little laptop until the true heir to the ultraportable throne was unveiled: the [Dell XPS M1330](https://blog.codinghorror.com/dell-xps-m1330-review/). The specs are much better, as you’d expect after almost five years. But what about power consumption? How much has that changed? Let’s find out.


One of the key weapons in my geek arsenal is the [Kill-a-Watt electricity usage monitor](http://www.amazon.com/exec/obidos/ASIN/B00009MDBU). Here’s an action shot of me using it while [building a PC](https://blog.codinghorror.com/building-a-pc-part-ii/):


![](https://blog.codinghorror.com/content/images/2025/04/image-71.png)


I see that there’s a newer, more advanced [Kill-a-Watt model P4600](http://www.amazon.com/exec/obidos/ASIN/B000RGF29Q) on the market now, but the modest [P4400](http://www.amazon.com/exec/obidos/ASIN/B00009MDBU/codihorr-20) I own is only 24 bucks and works plenty well enough for me. I know, I know, I’m always encouraging you to buy more crap. But this is something I really do *use* quite regularly. Here, I’ll prove it:

- [Why Estimate When You Can Measure?](https://blog.codinghorror.com/why-estimate-when-you-can-measure/)
- [The Cost of Leaving Your PC On](https://blog.codinghorror.com/the-cost-of-leaving-your-pc-on/)
- [When Hardware is Free, Power is Expensive](https://blog.codinghorror.com/when-hardware-is-free-power-is-expensive/)
- [Upgrading to a High Efficiency Power Supply](https://blog.codinghorror.com/upgrading-to-a-high-efficiency-power-supply/)


And here I am today using it again. It’s awfully handy to know how much power the stuff around your house is using. So let’s get down to brass tacks on this laptop. Here are the specifications of my Dell XPS M1330:

- Intel Core 2 Duo 2.0 GHz processor
- 2 GB RAM
- 32 GB solid state hard drive
- 13.3" 1280x800 LED backlit display
- NVIDIA GeForce Go 8400M GS video
- Windows Vista Ultimate


It’s not the world’s fastest laptop, to be sure, but totally respectable for an under 4 pound ultraportable. Here are some baseline power usage measurements:


I should point out that I’m using a very clean install of Vista, with most of the [unnecessary background stuff](https://blog.codinghorror.com/choosing-anti-anti-virus-software/) disabled. I left the laptop in a typical real world configuration; screen brightness is at maximum, WiFi is enabled and connected to an access point, power management is set to the default of “Balanced.” I let the machine quiesce for an hour at the desktop so all those background processes Vista loves to run were idle.


All the below tests were run with the laptop connected to AC power and the battery physically removed from the machine.


**How much power does the LCD display use?**

kg-card-begin: html


| LCD brightness 7 (max) | 20w |
| LCD brightness 6 | 19w |
| LCD brightness 5 | 18w |
| LCD brightness 0-4 | 17w |


kg-card-end: html

**How much power does the hard drive use?**

kg-card-begin: html


| HDD idle | 20w |
| HDD defragmenting | 23w |


kg-card-end: html

**How much power does the onboard WiFi use?**

kg-card-begin: html


| WiFi disabled | 17.5w |
| WiFi enabled | 20w |
| WiFi [bandwidth test](https://blog.codinghorror.com/gigabit-ethernet-and-back-of-the-envelope-calculations/) | 24w |


kg-card-end: html

**How much power does the CPU use?**

kg-card-begin: html


| CPU idle | 20w |
| CPU running one [prime95](http://www.mersenne.org/) torture test | 50w |
| CPU running two prime95 torture tests | 63w |


kg-card-end: html

**How much power does the video card (GPU) use?**

kg-card-begin: html


| GPU idle | 20w |
| GPU running [rthdribl](https://web.archive.org/web/20080416233029/http://www.daionet.gr.jp/~masa/rthdribl/) | 55w |
| GPU running [ATITool](http://www.softpedia.com/get/Tweak/Video-Tweak/ATITool.shtml) 3D warmup | 40w |


kg-card-end: html

(The ATITool number is the more accurate one, as this particular 3D warmup “fuzzy cube” test exercises the GPU while only loading the CPU to about 14%, whereas the rthdribl test loads the CPU to around 50%.)


**How much power does the integrated DVD drive use?**

kg-card-begin: html


| DVD idle | 20w |
| DVD spinning with disc inserted | 25w |
| DVD copying | 33w |


kg-card-end: html

**How much power does the integrated CPU fan use?**

kg-card-begin: html


| CPU fan off | 20w |
| CPU fan low | 21w |
| CPU fan med/high | 22w |


kg-card-end: html

Realize that the Kill-o-watt is a fine instrument, but it’s not scientifically precise. It’s the overall percentages and patterns we’re interested in more than the absolute numbers. The results are different than last time, yet **the rules of laptop power consumption haven’t fundamentally changed**. Here’s the data in chart form, with minimum and maximum power draw I measured for each component. The number in red is the difference between the two.


![](https://blog.codinghorror.com/content/images/2025/04/image-70.png)


The top consumers of your laptop’s power are the CPU, the GPU, the DVD, and WiFi – in that order. So, armed with this data, **how do we maximize our laptop battery life?**


Some of this is fairly obvious. When you’re on battery:

1. Don’t do anything with 3D graphics (gaming, etc.)
2. Avoid using DVDs
3. Turn down the screen brightness 1 or 2 notches
4. Avoid CPU intensive web pages or programs


That will get you most of the way there. It’s tough to reduce your use of wireless on a laptop without sacrificing the essential laptop quality of portability. Beyond that, **keep a serious eye on your CPU usage**; you *desperately *want to avoid CPU intensive programs and websites while on battery. They’ll kill your battery life far faster than anything else you can do with your laptop.


You could run Task Manager all the time, which shows a tiny graph of your CPU usage in real time. But do you really want to think about this? I recommend clicking on the little battery icon in the taskbar and explicitly enabling Vista’s “Power saver” mode whenever you’re on battery. This **automatically enforces a CPU usage throttle of 50 percent**. On a dual-core CPU, giving up one core is usually no big deal for most tasks.


![](https://blog.codinghorror.com/content/images/2025/04/image-69.png)


For even more battery life protection, you can edit the Power Saver plan configuration to set “minimum processor state” to something lower than 50%. Even 25% would be more than enough power for most things I do on this laptop.

[laptop](https://blog.codinghorror.com/tag/laptop/)
[power consumption](https://blog.codinghorror.com/tag/power-consumption/)
[ultraportable](https://blog.codinghorror.com/tag/ultraportable/)
[electricity monitor](https://blog.codinghorror.com/tag/electricity-monitor/)
[hardware](https://blog.codinghorror.com/tag/hardware/)
