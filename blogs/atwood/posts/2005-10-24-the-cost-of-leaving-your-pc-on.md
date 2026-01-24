---
title: "The Cost of Leaving Your PC On"
date: 2005-10-24
url: https://blog.codinghorror.com/the-cost-of-leaving-your-pc-on/
slug: the-cost-of-leaving-your-pc-on
word_count: 746
---

Between my server and my Windows Media Center home theater PC, I have at least two PCs on all the time at home. **Have you ever wondered how much it’s costing you to leave a computer on 24 hours a day, 7 days a week?**


The first thing you need to know is **how much power your computer draws**. The best way is to [measure the actual power consumption](https://blog.codinghorror.com/why-estimate-when-you-can-measure/). You’ll need a $30 device like the [Kill-a-Watt](http://www.amazon.com/exec/obidos/ASIN/B00009MDBU) to do this accurately. Once you get one, you’ll inevitably go through a phase where you run around your home, measuring the power draw of everything you can plug into a wall socket. For example, I learned this weekend that our 42" plasma television draws between 90 watts (totally black screen) and 270 watts (totally white screen). Based on a little ad-hoc channel surfing with an eye on the Kill-a-Watt’s LCD display, the average appears to be around 150 watts for a typical television show or movie.


But I digress. Once you’ve measured the power draw in watts (or [guesstimated the power draw](http://michaelbluejay.com/electricity/computers.html)), you’ll need to convert that to kilowatt-hours. Here’s the kilowatt-hour calculation for my server, which draws ~160 watts:

kg-card-begin: html

```

160 watts * (8,760 hours per year) / 1000 = 1401.6 kilowatt-hours

```

kg-card-end: html

The other thing you’ll need to know is how much you’re paying for power in your area. Power here in California is rather expensive and calculated using a byzantine rate structure. According to this [recent PG&E PDF](https://web.archive.org/web/20210318005152/https://www.pge.com/pge_global/common/pdfs/rate-plans/how-rates-work/Residential-Rates-Plan-Pricing.pdf), the household average for our area is between **28 and 44 cents per kilowatt-hour**. Let’s split the difference and call it 36 cents.

kg-card-begin: html

```

1401.6 kilowatt-hours * 36 cents / 100 = $504.58

```

kg-card-end: html

**So leaving my server on is costing me $500 / year, or $42 per month.** My home theater PC is a bit more frugal at 65 watts. Using the same formulas, that costs me $205 / year or $17 per month.


So, how can you reduce the power draw of the PCs you leave on 24/7?

- **Configure the hard drives to sleep on inactivity.** You can do this via Control Panel, Power, and it’s particularly helpful if you have multiple drives in a machine. My server has four hard drives, and they’re typically asleep at any given time. That saves a solid 4-5 watts per drive.
- **Upgrade to a more efficient power supply.** A certain percentage of the input power to your PC is lost as waste during the conversion from wall power to something the PC can use. At typical power loads (~90w), the average power supply efficiency is a disappointing 65%. But the good news is that there’s been a lot of recent vendor activity around [more efficient power supplies](https://web.archive.org/web/20061227012422/http://www.silentpcreview.com/article276-page1.html). The [Fortron Zen fanless power supply](https://web.archive.org/web/20061227012422/http://www.silentpcreview.com/article263-page1.html), for example, offers an astonishing 83% efficiency at 90w load! If you upgraded your power supply, you could theoretically drop from 122w @ 65% efficiency to 105w @ 83% efficiency. That’s only a savings of $20 per year in this 90w case, but the larger the power usage, the bigger the percentage savings.
- **Don’t use a high-end video card.** I’m not sure this is widely understood now, but after the CPU, the video card is *by far* the biggest power consumer in a typical PC. It’s not uncommon for the typical “mid-range” video card to suck down [20+ watts at idle](https://blog.codinghorror.com/video-card-power-consumption/) – and far more under actual use or gameplay! The worrying number, though, is the idle one. Pay close attention to the video card you use in an “always-on” machine.
- **Configure the monitor to sleep on inactivity.** This one’s kind of a no-brainer, but worth mentioning. A CRT eats about 80 watts, and a LCD of equivalent size less than half that.
- **Disconnect peripherals you don’t use.** Have a server with a CD-ROM you rarely use? Disconnect the power to it. A sound card you don’t use? Pull it out. Redundant fans? Disconnect them. That’s only a savings of a few watts, but it all adds up.


If you’re building a new PC, it’s also smart to avoid Intel’s Pentium 4 series, as they use substantially more power than [their AMD equivalents](https://web.archive.org/web/20070607193404/http://blogs.zdnet.com/BTL/?p=1670). Intel’s Pentium-M, on the other hand, delivers the best bang for the watt on the market. Although it was originally designed for laptops, it can be retrofitted into desktops.

[power consumption](https://blog.codinghorror.com/tag/power-consumption/)
[electricity cost](https://blog.codinghorror.com/tag/electricity-cost/)
[energy efficiency](https://blog.codinghorror.com/tag/energy-efficiency/)
[pc usage](https://blog.codinghorror.com/tag/pc-usage/)
[hardware monitoring](https://blog.codinghorror.com/tag/hardware-monitoring/)
