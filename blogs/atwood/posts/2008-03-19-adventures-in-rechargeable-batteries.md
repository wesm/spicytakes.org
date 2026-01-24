---
title: "Adventures in Rechargeable Batteries"
date: 2008-03-19
url: https://blog.codinghorror.com/adventures-in-rechargeable-batteries/
slug: adventures-in-rechargeable-batteries
word_count: 1167
---

Every self-respecting geek loves gadgets. I’m no exception. And so many of my favorite gadgets have a voracious appetite for batteries. I don’t know why all the other battery types fell so far out of favor, but between AA and AAA, I could probably power 95% of my household gadget needs.


![](https://blog.codinghorror.com/content/images/2025/04/image-29.png)


I’ve been a rechargeable battery user for years. It seems the frugal thing to do in the long run, and it’s also healthier for the planet when we aren’t discarding mountains of single-use batteries into landfills. I remember switching over to the then-new NiMH battery type based on a late 90’s John Dvorak column touting their availability and power. Miraculously, that very article is still [available on the internet](https://web.archive.org/web/20080324031001/http://www.hayestech.com/nimh.htm):


> The calculation of cost for nickel hydride batteries in the table is for 100 recharges. Hawk says the industry knows that nickel hydride batteries can easily last through 500 recharges. I’ve seen data indicating that 1,000 charges are possible. This drops the cost per 10,000 pictures to 70 cents! I’m convinced that the industry doesn’t want people to know about these batteries. I seriously doubt you’ll be seeing them on a rack in the grocery store anytime soon. Do the math: It’s like buying 1,000 alkaline batteries for less than 10 bucks. Imagine what this does to the lucrative disposable-battery business.
> So now I wonder where the D, C, and AAA nickel hydride batteries are? Mostly in Japan. As far back as January 1996, Toshiba rolled out the first complete line of standard cells and other Japanese battery makers have followed. This event was essentially hushed up in the U.S. market. The big-name American battery companies have avoided this market-killing technology for obvious reasons.


I immediately rushed out bought a bunch of the batteries and the charger from the importer that Mr. Dvorak recommended. In fact I still have some of those original models. Let’s compare these ten year old 1998 NiMH batteries to their 2008 cousins:


![](https://blog.codinghorror.com/content/images/2025/04/image-28.png)


The picture can be a little hard to read, so I’ve reprinted the technical details from each AA battery below:

kg-card-begin: html


| 1998 | NiMH GP Rechargeable | 1.2v, 1300 mAh |
| 2008 | NiMH Energizer Rechargeable | 1.2v, 2500 mAh |


kg-card-end: html

Is it really true that **AA battery capacity has *almost doubled* in the last ten years?** That’s pretty amazing. But as I found out, it’s not the entire story.


For one thing, there’s the issue of **discharge rate**. It turns out that massive 2500mAh capacity of the Energizer rechargeable battery doesn’t mean much when the battery drains itself within a month. Take it from [Mr. Lee](https://web.archive.org/web/20080327225723/http://www.amazon.com/review/R2UW60Y48A0V70/ref=cm_cr_rdp_perm):


> All rechargeable battery manufacturers love to boast about their product’s current capacity (mAh). But there is a dirty little secret that they don’t want you to hear: self-discharge rate. Simply put: a fully charged NiCd of NiMH cell will gradually lose its stored energy over time. Technical papers I have researched typically put the self-discharge rate at 10-20% per month for NiCd cells, and 20-30% per month for NiMH cells. This kind of self-discharge rate is usually acceptable in applications such as digital cameras.
> I bought 8 of those Energizer 2500mAh rechargeable NiMH batteries over one year ago. At first, I was very happy about the large current capacity offered by those batteries. But within a few months, I started to notice that they die very quickly in my digital camera. In fact, a set of Sony 2000mAh NiMH batteries I bought one year earlier seems to last much longer when used in the same camera.


So putting a larger number on the box is ultimately a method of fooling consumers with marketing. Where have we seen that before? Oh right, *everywhere*. Caveat emptor. Mr. Lee recommends the following model batteries, which exhibit much saner self-discharge rates; I’ve since bought a few batches of both the Eneloop and the Hybrid cells:

- [Sanyo Eneloop NiMH AA](http://www.amazon.com/exec/obidos/ASIN/B004UG41W8)
- Rayovac Hybrid NiMH AA
- Duracell Pre-Charged NiMH AA


In general you want the “hybrid” or “pre-charged” varieties, and should ignore ridiculous claims about capacity.


The other pitfall of rechargeable batteries lies in the recharging process itself. Even if you buy the very best rechargeable batteries, **if you charge them improperly**, you’ll get [poor results](http://www.amazon.com/review/R1911A7DQEVRKF/ref=cm_cr_rdp_perm).


> Charging NiMH batteries is the result of a compromise. A low current is gentle on the battery and maximizes its lifespan, but a full charge takes hours. A high current will recharge the battery much faster, but put more strain on it, causing it to wear out prematurely. It also requires careful monitoring of the battery’s electrical characteristics to prevent damage.
> Most of the chargers on the market today use one or the other of these methods. The fast chargers, especially the cheap ones, excel at one thing: destroying perfectly good batteries, because they lack the monitoring circuitry to control the charge current and detect when the battery is full. The slow chargers are usually better, mainly because it’s harder to design a really bad slow charger. Unfortunately... they’re slow.


Most bundled battery chargers are junk. Given the inherent compromises of charging, you need something smart. That’s why I ended up tossing my generic “rapid” chargers in favor of the majestic, glorious, and surprisingly inexpensive La Crosse Technology [BC-900 AlphaPower battery charger](http://www.amazon.com/exec/obidos/ASIN/B004J6DLD4).


![](https://blog.codinghorror.com/content/images/2025/06/image-27.png)


Seriously, just look at this thing. It’s a geek’s dream. Each battery can be controlled individually, with its own real-time LCD readout, in four modes:

1. **Charge** at various rates, from 200/500/700/1000mA
2. **Discharge** at 1/2 the charging rate
3. **Test** to determine *true* battery capacity
4. **Refresh** to “revitalize” older batteries


You can also switch between four different readouts after the mode is engaged: time elapsed, voltage, mAh charge/discharge rate, and current mAh capacity. That **refresh** mode is incredibly slow – it’s basically discharging and recharging over and over – but it really works. It can take marginal batteries from the brink of death and give them new life.


But you don’t have to care about any of that; **if you just drop 4 AAs or AAA batteries in the device, it will charge them fine**. I spent several hours after I got it plugging various batteries in it, trying different modes, and watching it work. I’m not sure what the exact definition of geek is, but I think “enjoys recharging batteries” has to be very high on that list.


I can’t recommend the BC-900 highly enough. Did I mention it comes packaged with a starter set of 4 rechargeable AA and AAA batteries, D-cell adapter shells, and a nifty nylon carrying case, too? But don’t take my word for it. Read the Amazon reviews; they’re positively *glowing*.


The gadget world may run on AA and AAA cells, but armed with a basic knowledge of NiMH battery technology and a great recharger, you too can be more than prepared to meet that challenge.


Gentlemen, start your chargers.

[rechargeable batteries](https://blog.codinghorror.com/tag/rechargeable-batteries/)
[nimh](https://blog.codinghorror.com/tag/nimh/)
[gadgets](https://blog.codinghorror.com/tag/gadgets/)
[technology trends](https://blog.codinghorror.com/tag/technology-trends/)
[sustainability](https://blog.codinghorror.com/tag/sustainability/)
