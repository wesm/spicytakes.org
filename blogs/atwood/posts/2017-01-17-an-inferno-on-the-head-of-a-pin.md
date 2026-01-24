---
title: "An Inferno on the Head of a Pin"
date: 2017-01-17
url: https://blog.codinghorror.com/an-inferno-on-the-head-of-a-pin/
slug: an-inferno-on-the-head-of-a-pin
word_count: 1771
---

Today’s processors contain [billions of heat-generating transistors](https://blog.codinghorror.com/moores-law-in-practical-terms/) in an ever shrinking space. The power budget might go from:

- 1000 watts on a specialized server
- 100 watts on desktops
- 30 watts on laptops
- 5 watts on tablets
- 1 or 2 watts on a phone
- 100 milliwatts on an [embedded system](http://www.anandtech.com/show/8702/ingenic-launches-newton2-mips-based-iot-and-wearables-solution)


That’s three four orders of magnitude. Modern CPU design is **the delicate art of placing an inferno on the head of a pin.**


Look at the original 1993 Pentium compared to the 20th anniversary Pentium:

kg-card-begin: html


|  | 1993
Pentium
66 Mhz
16kb L1
**3.2 million** transistors |
|  | 2014
Pentium G3258
3.2 Ghz × 2 cores
128kb L1, 512kb L2, 3MB L3
**1.4 billion** transistors |


kg-card-end: html

I remember cooling the early CPUs with simple heatsinks; no fan. Those days are long gone.


A roomy desktop computer affords cooling opportunities (and thus a watt budget) that a laptop or tablet could only dream of. How often will you be at peak load? For most computers, the answer is “rarely.” The smaller the space, the higher the required performance, the more… challenging your situation gets.


![](https://blog.codinghorror.com/content/images/2017/01/challenge-accepted-barney.gif)


Sometimes, [I build servers](https://blog.codinghorror.com/to-ecc-or-not-to-ecc/).


> Inspired by Google and their use of cheap, commodity x86 hardware to scale on top of the open source Linux OS, I also [built our own servers](https://blog.codinghorror.com/building-servers-for-fun-and-prof-ok-maybe-just-for-fun/). When I get stressed out, when I feel the world weighing heavy on my shoulders and I don’t know where to turn… *I build servers*. It’s therapeutic.


Servers are one of those situations where you *may* be at full CPU load more often than not. I prefer to build [1U servers](http://www.computerhope.com/jargon/num/1u.htm) which is the smallest rack mountable unit, at 1.75″ total height.


![](https://blog.codinghorror.com/content/images/2017/01/1u-servers.jpg)


You get plenty of cores on a die these days, so I build single CPU servers. One reason is price; the other reason is that clock speed declines proportionally to the number of cores on a die (this is for the Broadwell Xeon V4 series):

kg-card-begin: html


|  | cores | GHz |  |
| E5-1630 | 4 | 3.7 | $406 |
| E5-1650 | 6 | 3.6 | $617 |
| E5-1680 | 8 | 3.4 | $1723 |
| E5-2680 | 12 | 2.4 | $1745 |
| E5-2690 | 14 | 2.6 | $2090 |
| E5-2697 | 18 | 2.3 | $2702 |


kg-card-end: html

Yes, there are server CPUs with even more cores, but if you have to ask how much they cost, you *definitely* can’t afford them… and they’re clocked even slower. What we do at [Discourse](https://discourse.org/) is serviced better by a smaller number of super fast cores than a larger number of slow cores, anyway.


With that in mind, consider these two Intel Xeon server CPUs:

- E5-1630 V3 (4 core, 3.7 - 3.8 Ghz)
- E5-1650 V3 (6 core, 3.5 - 3.8 Ghz)


As you can see from the official Intel product pages for each processor, they both have a TDP heat budget of **140 watts**. I’m scanning the specs, thinking maybe this is an OK tradeoff.


![](https://blog.codinghorror.com/content/images/2017/01/thought-bubble-more-cores.png)


Unfortunately, here’s what I actually measured with [my trusty Kill-a-Watt](https://blog.codinghorror.com/why-estimate-when-you-can-measure/) for each server build as I performed [my standard stability testing](https://blog.codinghorror.com/is-your-computer-stable/), with completely identical parts except for the CPU:

- E5-1630: 40w idle, 170w mprime
- E5-1650: 55w idle, **250w** mprime


I am here to tell you that Intel’s TDP figure of 140 watts for the 6 core version of this CPU is a *terrible, scurrilous lie!*


This caused a bit of a problem for me as our standard 1U server build now **overheats, alarms, and throttles with the 6 core CPU** – whereas the 4 core CPU was just fine. Hey Intel! From my home in California, [I stab at thee!](https://www.penny-arcade.com/comic/2002/07/22)


But, you know...


![](https://blog.codinghorror.com/content/images/2017/01/challenge-accepted.gif)


#### Better Heatsink


The 1.75″ maximum height of the 1U server form factor doesn’t leave a lot of room for creative cooling of a CPU. But you *can* switch from an Aluminum cooler to a Copper one.


![](https://blog.codinghorror.com/content/images/2017/01/1u-heatsink-copper-vs-alu.jpg)


Copper is significantly more expensive, plus heavier and harder to work with, so it’s generally easier to throw an ever-larger mass of aluminum at the cooling problem when you can. But when space is a constraint, as it is with a 1U server, copper dissipates more heat [in the same form factor](https://web.archive.org/web/20170725020853/https://www.ecnmag.com/article/2010/04/comparing-impact-different-heat-sink-materials-cooling-performance).


The famous “Ninja” CPU cooler came in identical [copper and aluminum versions](http://www.silentpcreview.com/article805-page2.html) so we can compare apples to apples:

- Aluminum Ninja – 24C rise over ambient
- Copper Ninja – 17C rise over ambient


You can scale the load and the resulting watts of heat by spinning up MPrime threads for the exact number of cores you want to “activate,” so that’s how I tested:

- Aluminum heatsink – stable at 170w (mprime threads=4), but heat warnings with 190w (mprime threads=5)
- Copper heatsink – stable at 190w (mprime threads=5) but heat warnings with 230w (mprime threads=6)


Each run has to be overnight to be considered successful. This helped, noticeably. But we need more.


#### Better Thermal Interface


When it comes to server builds, I stick with the pre-applied grey thermal interface pad that comes on the heatsinks. But out of boredom and a desire to experiment, I…

- Removed the copper heatsink.
- Used isopropyl alcohol to clean both CPU and heatsink.
- Applied fancy “Ceramique” thermal compound I have on hand, [using an X shape pattern](https://www.pugetsystems.com/labs/articles/Thermal-Paste-Application-Techniques-170/).


![](https://blog.codinghorror.com/content/images/2017/01/applying-thermal-paste.jpg)


I wasn’t expecting any change at all, but to my surprise with the new TIM applied **it took 5x longer to reach throttle temps** with mprime threads=6. Before, it would thermally throttle within a minute of launching the test, and after it took ~10 minutes to reach that same throttle temp. The difference was noticeable.


That’s a surprisingly good outcome, and it tells us the default grey goop that comes pre-installed on heatsinks is... not great. Per [this 2011 test](https://web.archive.org/web/20160918160737/http://skinneelabs.com/2011-thermal-paste-review-comparison/3/), the difference between worst and best thermal compounds is 4.3°C.


But as Dan once bravely noted while testing [Vegemite as a thermal interface material](http://www.dansdata.com/goop.htm):


> If your PC’s so marginal that a CPU running three or four degrees Celsius warmer will crash it [or, for modern CPUs, cause the processor to auto-throttle itself and substantially reduce system performance], the solution is not to try to edge away from the precipice with better thermal compound. It’s to make a big change to the cooling system, or just lower the darn clock speed.


An improved thermal interface just gets you there *faster* (or slower); it doesn’t address the underlying problem. So we’re not done here.


#### Ducted Airflow


Most, but not all, of the SuperMicro cases I’ve used have included a basic fan duct / shroud that lays across the central fans and the system. Given that the case fans are pretty much directly in front of the CPU anyway, I’ve included the shroud in the builds out of a sense of completeness more than any conviction that it was doing anything for the cooling performance.


This particular server case, though, did *not* include a fan duct. I didn’t think much about it at the time, but considering the heat stress this 6-core CPU and its 250 watt heat generation was putting on our 1U build, I decided I should build a quick duct out of card stock and test it out.


![](https://blog.codinghorror.com/content/images/2017/01/server-duct-testing.jpg)


(I know, I know, it’s a super janky duct! But I was prototyping!)


Sure enough, this duct, combined with the previous heatsink and TIM changes, enabled the server to **remain stable overnight with a full MPrime run of 12 threads.**


![](https://blog.codinghorror.com/content/images/2017/01/chuck_norris_approves.gif)


I think we’ve certainly demonstrated the surprising (to me, at least) value of fan shrouds. But before we get too excited, let’s consider one last thing.


#### Define “CPU Load”


Sometimes you get so involved with solving the problem at hand that you forget to consider whether you are, in fact, solving the *right* problem.


In these tests, we defined 100% CPU load using MPrime. Some people claim MPrime is more of a [power virus](https://en.wikipedia.org/wiki/Power_virus) than a real load test, because it exerts so much heat pressure on the CPUs. I initially dismissed these claims since I’ve used MPrime (and its Windows cousin, Prime95) for almost 20 years to test CPU stability, and it’s never let me down.


But I [did more research](https://web.archive.org/web/20170602092805/http://www.overclock.net/t/1510388/haswell-e-overclock-leaderboard-owners-club/2390#post_22900116) and I found that MPrime, since 2011, uses **AVX2 **instructions extensively on newer Intel CPUs:


> The newer versions of Prime load in a way that they are only safe to run at near stock settings. The server processors actually downclock when AVX2 is detected to retain their TDP rating. On the desktop we’re free to play and the thing most people don’t know is how much current these routines can generate. It can be lethal for a CPU to see that level of current for prolonged periods.
> …
> That’s why most stress test programs alternate between different data pattern types. Depending on how effective the rotation is, and how well that pattern causes issues for the system timing margin, it will, or will not, catch potential for instability. So it’s wise not to hang one’s hat on a single test type.


This explains why I saw such a large discrepancy between other CPU load programs like BurnP6 and MPrime.


MPrime does an amazing job of generating the type of CPU load that causes maximum heat pressure. But unless your servers regularly chew through zillions of especially [power-hungry AVX2 instructions](http://superuser.com/questions/981466/in-prime95-why-do-small-ffts-generate-the-most-heat-despite-cpu-at-100-for-al/981477#981477) this may be completely unrepresentative of any real world load your server would *actually see*.


#### Your Own Personal Inferno


Was this overkill? Probably. Even with the aluminum heatsink, no change to thermal interface material, and zero ducting, we’d probably see no throttling under normal use in our server rack. But I wanted to be *sure*. Completely sure.


Is this extreme? Putting 140 TDP of CPU heat in a 1U server? Not really. Nick at Stack Overflow told me they just put two 22 core, 145W TDP Xeon 2699v4 CPUs *and* four 300W TDP GPUs in a single Dell C4130 1U server. I’d sure hate to be in the room when those fans spin up. I’m also a little afraid to find out what happens if you run MPrime plus full GPU load on that box.


Servers are an admittedly rare example of big CPU performance heat and size tradeoffs, one of the few left. It is fun to play at the extremes, but the SoC inside your phone makes the same tradeoffs on a smaller scale. **Tiny infernos in our pockets**, each and every one.

[processor](https://blog.codinghorror.com/tag/processor/)
[cpu design](https://blog.codinghorror.com/tag/cpu-design/)
[power consumption](https://blog.codinghorror.com/tag/power-consumption/)
[servers](https://blog.codinghorror.com/tag/servers/)
