---
title: "How Much Power Does My Laptop Really Use?"
date: 2006-04-09
url: https://blog.codinghorror.com/how-much-power-does-my-laptop-really-use/
slug: how-much-power-does-my-laptop-really-use
word_count: 452
---

I’ve determined power usage [on my desktop](https://blog.codinghorror.com/why-estimate-when-you-can-measure/) and [on my server](https://blog.codinghorror.com/the-cost-of-leaving-your-pc-on/), but I hadn’t gotten around to testing the power usage of my laptop. As battery life is always a concern with a laptop, I was particularly curious to see which parts of the laptop draw the most power. So I ran a few tests with my trusty kill-a-watt on my [Dell Inspiron 300m](https://web.archive.org/web/20060421122926/http://compreviews.about.com/cs/laptops/gr/aaprDellIns300m.htm). It’s an ultraportable 2 pound laptop of late 2003 vintage with the following specs:

- Intel Pentium M 1.2GHz low voltage processor
- 640 megabytes of RAM
- 60 gigabyte hard drive
- 12.1" 1024x768 LCD screen
- Windows XP Pro


Let’s start with some baselines:

kg-card-begin: html

> Laptop off, battery charging
> 63w
> Laptop off, battery disconnected
> 1w
> Laptop off, sleeping
> 1w
> Laptop on, idle at Windows desktop
> 15w

kg-card-end: html

All subsequent tests were run with the laptop connected to AC power and the battery physically removed from the machine.


**How much power does the LCD display use?**

kg-card-begin: html

> maximum screen brightness15w
> minimum screen brightness11w


kg-card-end: html
**How much power does the hard drive use?**
kg-card-begin: html

hard drive sleeping14w
hard drive idle15w
hard drive defragmenting18w


kg-card-end: html
**How much power does the onboard WiFi use?**
kg-card-begin: html


wifi disabled15w
wifi enabled16w
wifi [bandwidth test](https://blog.codinghorror.com/gigabit-ethernet-and-back-of-the-envelope-calculations/)19w


kg-card-end: html
**How much power does the CPU use?**
kg-card-begin: html


cpu idle15w
cpu running [prime95](http://www.mersenne.org/) torture test26w

kg-card-end: html
**How much power does the integrated video use?**Running 3dMark2001 produced a peak power usage of 29 watts. We can subtract the Prime95 number of 26 watts – which is entirely CPU-only – to estimate *about three watts* are used exclusively by the integrated Intel “extreme”* video hardware.Bear in mind the kill-a-watt is only accurate to plus or minus a watt. And these are all rough figures based on a sample size of one laptop. But I think the rules here can be generalized to most laptops.Here’s what I learned:**The CPU is, by far, the biggest consumer of power in a laptop**. No surprise there. If you want to drain your battery lickety-split, run a bunch of apps that peg your CPU at 100 percent.**Putting your hard drive to sleep isn’t worth it.** Ever. You save a whopping... single watt. Why bother?**For maximum battery life, dim your screen**. I was surprised that the screen alone accounted for 25% of the total power draw of my laptop at idle. You can moderate use of WiFi or your hard drive, but you can’t exactly moderate the use of your screen. Plan accordingly.Of course, your mileage may vary.*It’s extreme, all right. Extremely *crappy*.

[laptop](https://blog.codinghorror.com/tag/laptop/)
[power usage](https://blog.codinghorror.com/tag/power-usage/)
[hardware](https://blog.codinghorror.com/tag/hardware/)
[battery life](https://blog.codinghorror.com/tag/battery-life/)
[energy consumption](https://blog.codinghorror.com/tag/energy-consumption/)
[lcd display](https://blog.codinghorror.com/tag/lcd-display/)
[technology trends](https://blog.codinghorror.com/tag/technology-trends/)
