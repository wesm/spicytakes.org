---
title: "When Hardware is Free, Power is Expensive"
date: 2007-05-22
url: https://blog.codinghorror.com/when-hardware-is-free-power-is-expensive/
slug: when-hardware-is-free-power-is-expensive
word_count: 1626
---

Bill Gates has often said that **over time, the cost of computer hardware approaches zero**. Here’s [one such example](https://www.wired.com/2004/03/gates-hardware-will-be-free/):


> Ten years out, in terms of actual hardware costs you can almost think of hardware as being free.


History has proven him right. Computer hardware isn’t literally free, of course. But it’s *effectively* free relative to the level of computing power you’re getting for your dollar. **What does it mean when computer hardware is effectively free, and getting even more free every day?**


For one thing, computer software starts to look [incredibly expensive](https://blog.codinghorror.com/what-if-software-was-never-free/). But let’s put aside the ratio of software cost to hardware cost for now.


If you’re Google, or any other company building out massive datacenter farms, cheap hardware is a strategic advantage. It means you can build larger and larger datacenters for less money. Computers may be smaller and cheaper than ever, but they [still require electricity to operate.](https://www.cnet.com/news/power-could-cost-more-than-servers-google-warns/) You now have a new problem. The electrical power used to drive all that free hardware you’ve amassed becomes your greatest expense:


> Over the last three generations of Google’s computing infrastructure, performance has nearly doubled, Barroso said. But because performance per watt remained nearly unchanged, that means electricity consumption has also almost doubled.
> **If server power consumption grows 20 percent per year, the four-year cost of a server’s electricity bill will be larger than the $3,000 initial price of a typical low-end server with x86 processors.** Google’s data center is populated chiefly with such machines. But if power consumption grows at 50 percent per year, “power costs by the end of the decade would dwarf server prices,” even without power increasing beyond its current 9 cents per kilowatt-hour cost, Barroso said.


Computer hardware costs may be approaching zero, but power costs are fixed – or rising. The thirst for power in the face of increasingly large datacenters has driven Google to build datacenters in out-of-the-way places [where power costs are low](http://www.infoworld.com/article/2662029/operating-systems/it-confronts-the-datacenter-power-crisis.html):


> Google, for example, has watched its energy consumption almost double during the past three generations of upgrades to its sprawling computing infrastructure. **It recently unveiled a major new datacenter site in a remote part of Oregon, where power costs are a fraction of those at Google’s home base in Silicon Valley.** But cheap power may not be enough. Last year, Google engineer Luiz Andr Barroso predicted that energy costs would dwarf equipment costs – “possibly by a large margin” – if power-hungry datacenters didn’t mend their ways. Barroso went on to warn that datacenters’ growing appetite for power “could have serious consequences for the overall affordability of computing, not to mention the overall health of the planet.”


Google doesn’t just [build their own servers](https://blog.codinghorror.com/building-a-computer-the-google-way/). They [build their own power supplies](http://www.networkworld.com/article/2304459/data-center/google-builds-own-servers-for-efficiency.html), too:


> The power supply to servers is one place that energy is unnecessarily lost. One-third of the electricity running through a typical power supply leaks out as heat, [Urs Hlzle] said. That’s a waste of energy and also creates additional costs in the cooling necessary because of the heat added to a building.
> **Rather than waste the electricity and incur the additional costs for cooling, Google has power supplies specially made that are 90% efficient.** “It’s not hard to do. That’s why to me it’s personally offensive” that standard power supplies aren’t as efficient, he said.
> While he admits that ordering specially made power supplies is more expensive than buying standard products, Google still saves money ultimately by conserving energy and cooling, he said.


Google wants to extend that same efficiency outside their datacenter to your home PC. The three page Google whitepaper [High-efficiency power supplies for home computers and servers](http://static.googleusercontent.com/media/services.google.com/en//blog_resources/PSU_white_paper.pdf) (pdf) outlines how and why:


> At Google, we run many computers in our data centers to serve your queries, so energy conservation and efficiency are important to us. For several years we’ve been developing more efficient power supplies to eliminate waste from power supplies. Instead of the typical efficiencies of 60-70%, our servers’ power supplies now run at 90% efficiency or better, cutting down the energy losses by a factor of four.
> We believe this energy-saving power supply technology can be applied to home computers, too. So we’ve been working with Intel and other partners to propose a new power supply standard. The opportunity for savings is immense – we estimate that if deployed in 100 million PCs running for an average of eight hours per day, this new standard would save 40 billion kilowatt-hours over three years, or more than $5 billion at California’s energy rates.


I can vouch for this: power is *incredibly* expensive in California, to the point that running even a single PC 24/7 can have a noticeable [impact on your power bill](https://blog.codinghorror.com/the-cost-of-leaving-your-pc-on/).


Google’s proposal to increase the efficiency of PC power supplies mirrors a push for efficiency that’s been going on for a while in the PC enthusiast space. It’s partly a reflection of [the quiet PC movement](https://blog.codinghorror.com/building-a-quiet-pc/): less heat always equal less noise. But it can also have a bottom-line impact on how much you pay the power company each month.


I’m not aware of any standard PC power supplies that reach the lofty 90% efficiency goal Google claims. What Google’s proposing is a deeper, more fundamental change to the way the PC power supply is built – simplifying from multiple voltages (+12v, -12v, 5v, and 3.3v) to a single voltage (12v). But **a standard PC power supply of sufficient quality *can* reach up to 85% efficiency**. Consider the following graph comparing the efficiency of two PC power supplies:


![Computer power supply efficiency comparison graph](https://blog.codinghorror.com/content/images/uploads/2007/05/6a0120a85dcdae970b01287770154f970c-pi.png)


The graph shows **the difference between a typical PC power supply and one of the most energy efficient power supplies currently on the market**. The data table tells the story in raw watts:

kg-card-begin: html


| **[NeoPower 480 Power Supply](http://www.silentpcreview.com/article177-page4.html)** |
| AC Input | 110 | 142 | 220 | 276 | 336 | 390 | 515 | 596 |
| DC Output | 65 | 90 | 150 | 200 | 250 | 300 | 400 | 460 |
| Efficiency | 59% | 63% | 68% | 72% | 74% | 77% | 78% | 77% |
| Waste | 45 | 52 | 70 | 76 | 86 | 90 | 115 | 136 |


kg-card-end: html
kg-card-begin: html


| **[Corsair HX520W Power Supply](http://www.silentpcreview.com/article692-page4.html)** |
| AC Input | 64 | 88 | 115 | 183 | 236 | 295 | 350 | 486 | 638 |
| DC Output | 43 | 63 | 89 | 148 | 199 | 251 | 298 | 407 | 519 |
| Efficiency | 68% | 72% | 77% | 81% | 84% | 85% | 85% | 84% | 81% |
| Waste | 21 | 24 | 26 | 35 | 37 | 44 | 52 | 79 | 119 |


kg-card-end: html

It’s a decent result; efficiency increases by more than 10 percent across the board. But there’s a catch: **the power supply efficiency curve peaks at around 250 watts**.


Most desktop PCs barely [use 200 watts of power](https://blog.codinghorror.com/why-estimate-when-you-can-measure/). It’s extremely difficult to build a desktop computer that uses 250 watts of power without adding a high-powered [$300+ gaming class video card](https://blog.codinghorror.com/video-card-power-consumption/) to the mix – or even two of them in SLI mode. Furthermore, you’ll only reach that level of power usage under extreme load – with the video card and CPU both operating at near 100% usage. In other words, *only when you’re playing a video game*. The difference between idle and gaming load power usage can be more than 100w.


Unless you’re a gamer, you won’t even come *close* to 200 watts of power usage, even under full load. And how often is your PC operating at full load? If you’re like most users, almost never. Your PC is statistically idle 99% of the time it is turned on. Idle power consumption for a typical desktop PC ranges between 120 and 150 watts. Thus, **the real challenge is to deliver 90%+ efficiency at typical idle power consumption levels – 120-150 watts.**


The savings from upgrading to an efficient power supply on a single PC are rarely worth it. I’ll demonstrate using my old server as an example. It draws 160 watts of power at idle, and is turned on 24/7, 365 days a year. If I was to hypothetically install a power supply in this server that was 15 percent more efficient – a *best-case* scenario – how much power would I save per year?

kg-card-begin: html

```

160 watts * (8,760 hours per year) / 1000 = 1401.6 kilowatt-hours
136 watts * (8,760 hours per year) / 1000 = 1191.4 kilowatt-hours

```

kg-card-end: html

At the insanely expensive California power rates in my area, that equates to the following dollar amount per year:

kg-card-begin: html

```

1401.6 kilowatt-hours * 14.28 cents / 100 = $200.15
1191.4 kilowatt-hours * 14.28 cents / 100 = $170.13

```

kg-card-end: html

I’d save a whopping *thirty bucks per year*. That’s not even enough to cover the cost of the energy-efficient power supply! I’d have to amortize the cost of the power supply over three years to justify the expense.


All this tells us is that Google’s problems aren’t necessarily our personal problems. Not exactly news. But if you multiply that result by the tens of thousands of servers in [Google’s server farm](https://en.wikipedia.org/wiki/Google_Data_Centers), all operating at near 100% load, it’s a whole different ballgame. Efficiency is a strategic business decision for Google. Considering the millions upon millions of computers in the world, **more efficient PC power supplies are also part of the greater public good**. Do no evil, indeed.

[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[technology trends](https://blog.codinghorror.com/tag/technology-trends/)
[hardware](https://blog.codinghorror.com/tag/hardware/)
[computing power](https://blog.codinghorror.com/tag/computing-power/)
[data centers](https://blog.codinghorror.com/tag/data-centers/)
