---
title: "Upgrading to a High Efficiency Power Supply"
date: 2007-05-24
url: https://blog.codinghorror.com/upgrading-to-a-high-efficiency-power-supply/
slug: upgrading-to-a-high-efficiency-power-supply
word_count: 911
---

In [When Hardware is Free, Power is Expensive](https://blog.codinghorror.com/when-hardware-is-free-power-is-expensive/), I referenced a [Google whitepaper](http://static.googleusercontent.com/media/services.google.com/en//blog_resources/PSU_white_paper.pdf) (pdf) that explained why typical PC power supplies are not particularly efficient:


> **Most likely, the computer you’re using wastes 30-40% of the electrical power it consumes because it is using an inefficient power supply. **It’s difficult to believe that something as basic as a power supply could be responsible for that amount of waste, but it’s true. The problem with power supplies is that they generate heat, which saps away energy meant to power the computer. That happens when the power supply converts AC current into the DC current needed by computers


Google’s solution for their datacenter computers is a radical makeover – switching wholesale to single-voltage 12 volt power supplies.


> The net result of [the switch to a single-voltage 12v power supply] is a dramatic improvement in efficiency (including the power supply and the regulators) to about 85%, at virtually no cost. In other words, **you won’t have to pay more for a higher-efficiency PC, because the power supply is actually getting simpler, not more complicated**. By spending another $20 or so extra, it is possible to use higher-quality components and achieve efficiencies well over 90%.
> You won’t be able to buy such computers for a while, and Google isn’t planning on selling you any. But we’re working with industry partners such as Intel to make this technology an open standard that everyone can use, and that all vendors hopefully will adopt. It’s the right solution technically, and the right thing to do for the environment.


Who knows when these hypothetical single-voltage systems will arrive on the market in the form of desktop PCs and laptops we can actually buy. In the meantime, **it is possible to upgrade your computer with a high efficiency multiple-voltage power supply**. Unfortunately, existing high efficiency power supplies aren’t available “at virtually no cost”; they tend to be quite a bit more expensive than their less efficient cousins. I just upgraded my home PC to a high efficiency power supply:

- Core 2 Duo 3.2 GHz CPU (overclocked, overvolted)
- Radeon X1900 XTX primary video card
- Radeon X1550 secondary video card
- Western Digital Raptor 150 GB primary hard drive
- Seagate 750 GB secondary hard drive
- Creative X-Fi sound card


Note that this is a fairly power hungry system by current desktop standards. The [gaming-class video card](https://blog.codinghorror.com/video-card-power-consumption/) and overclocked/overvolted CPU are the primary culprits. I used my trusty kill-a-watt to [measure the power usage](https://blog.codinghorror.com/why-estimate-when-you-can-measure/) before and after the power supply upgrade. The power supply was the *only* component that changed.

kg-card-begin: html


|  | Typical PSU | Efficient PSU |  |  |
| Off | 5 w | 5 w |  |  |
| Boot (peak) | 237 w | 215 w | -22 w | 9.3% |
| Desktop | 205 w | 185 w | -20 w | 9.8% |
| 1 × [Prime95](http://www.mersenne.org/freesoft.htm) | 236 w | 217 w | -19 w | 8.1% |
| 2 × Prime95 | 257 w | 237 w | -20 w | 7.8% |
| [DiRT demo](http://www.gamershell.com/download_19282.shtml) peak | 270 w | 247 w | -23 w | 8.5% |


kg-card-end: html

**Most typical desktop PC power supplies are only 60 to 75 percent efficient; high efficiency models offer 80+ percent, all the way up to 85 percent depending on the load**. And that’s exactly what we’re seeing in these results. With the new high-efficiency power supply installed, I gained about 10 percent efficiency at each load level. To get an idea of where this system stands in terms of overall power usage, you can compare with a few different systems shown on page 4 of the Silent PC [Review Power Supply Fundamentals](https://web.archive.org/web/20070611163300/http://www.silentpcreview.com/article28-page4.html).


I was surprised to find that **my PC uses 5 watts of power *even when it’s powered off***. This is what’s known as “standby” electricity loss, and at least [one study](http://www.berkeley.edu/news/media/releases/2001/02/09_energ.html) showed it accounts for 6 to 16 percent of all energy use in homes, and [another](https://web.archive.org/web/20070806101503/http://china.lbl.gov/publications/china_standby_sino1102.pdf) (pdf) estimates that standby power use is now responsible for 1% of total carbon emissions on earth. The only way to reduce your computer’s power use to zero watts is to unplug it from the wall, or flip the power switch on the back of the power supply.


If you’re interested in upgrading to a high-efficiency power supply, look for models tagged with [the 80 PLUS designation](http://www.80plus.org/), which are guaranteed 80% efficient at 20%, 50% and 100% of their rated load. Many vendors cut corners by stating their power supplies offer “up to” 80 percent efficiency, but what they don’t tell you is that you’ll only reach that level of efficiency under extreme power loads that are unrealistic for most desktops. Seasonic is a popular choice, as they have aggressively enforced the 80 PLUS certification on almost their entire product line. But fair warning: you will pay a premium.


You can use the handy calculator provided by the 80 PLUS website to determine how much money you could potentially save on your power bill by switching to a more efficient power supply. It’s usually not much, unless you happen to run a server farm. But every little bit helps, and until Google and Intel offer up their single-voltage 12 volt system designs – which supposedly offer greater than 90 percent efficiency – it’s the best we can do.

[hardware](https://blog.codinghorror.com/tag/hardware/)
[power supply](https://blog.codinghorror.com/tag/power-supply/)
[efficiency](https://blog.codinghorror.com/tag/efficiency/)
[energy efficiency](https://blog.codinghorror.com/tag/energy-efficiency/)
[technology trends](https://blog.codinghorror.com/tag/technology-trends/)
