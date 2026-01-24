---
title: "Multiple Video Cards"
date: 2011-10-17
url: https://blog.codinghorror.com/multiple-video-cards/
slug: multiple-video-cards
word_count: 1305
---

Almost nobody should do what I am about to describe – that is, install and use more than one video card. Nobody really *needs* that much graphics performance. It’s also technically complex and a little expensive. But sometimes you gotta say **to hell with rationality and embrace the overkill**.


Why? [Battlefield 3](http://www.amazon.com/gp/search?ie=UTF8&keywords=battlefield%203), *that’s* why.


![](https://blog.codinghorror.com/content/images/2025/04/image-559.png)


I’ve been a fan of the series from the earliest days of Battlefield 1942, and I lost hundreds of hours to Battlefield 2 and Battlefield: Bad Company 2. I even wrote about the original Battlefield 2 demo on this very blog six years ago. So, yeah, I’m a superfan from way back. As much as I was anticipating Battlefield 3, I have to say the open beta convinced me it is everything I always wanted, and more. Glorious sandbox warfare on an enormous, next-generation *destructible* battlefield is a beautiful thing.


Since PC was the lead platform for Battlefield 3, it is the rare current game that isn’t dumbed down to PS3 and Xbox 360 console levels; it is a truly next-generation engine designed to scale over the next few years of PC performance.


![](https://blog.codinghorror.com/content/images/2025/04/image-558.png)


This also means **it’s going to be rough on current PCs**; at a minimum, you’ll need a fast dual core CPU, and a modern video card with 512mb or more video memory. It only goes up from there. Way up. Like most games, Battlefield 3 is far more limited by video card performance than CPU performance. This is normally the place where I’d trot out my standard advice urging you to buy one of the new hotness video cards released this holiday season. But unfortunately due to difficulties with the 40nm to 28nm process transition for ATI and NVIDIA, there *aren’t* any new hotness video cards this year.


So what’s a poor performance addicted Battlefield superfan to do? **Double down and add another video card for more performance, that’s what.** Both ATI and NVIDIA have offered mature multi-GPU support for a few years now, and they’ve mostly settled on a simple Alternate Frame Rendering (AFR) strategy where each video card alternates between frames to share the graphics rendering work.


![](https://blog.codinghorror.com/content/images/2025/04/image-557.png)


The little arrow there is a bridge attachment that you place on both cards so they can synchronize their work. Yes, there is a bit of overhead, but it scales surprisingly well, producing not *quite* double the performance but often in the area of 1.8x or so. Certainly enough to make it worth your while. You can technically add up to four video cards in this manner, but as with multiple CPUs your best bang for the buck is adding that second one; the third, fourth, and beyond provide increasingly diminished returns.


The good news is that the market crash in BitCoin GPU mining (if you don’t know what this is, don’t ask… please) means there is a glut of recent video cards up for sale on eBay right now. I have the same AMD Radeon HD 5870 that [I’ve had since early 2010](https://blog.codinghorror.com/three-monitors-for-every-user/). **I picked up another 5870 on eBay for a mere $170.** This is a great video card, well ahead of its time when it was originally released, and even now only 10% slower than the fastest video card AMD makes. I simply dropped the second card in my system and installed the bridge connector.


![](https://blog.codinghorror.com/content/images/2025/04/image-556.png)


You may recognize this computer as a further tweaked [version of my last build](https://blog.codinghorror.com/building-a-pc-part-vii-rebooting/) (which is still awesome, by the way, and highly recommended). Anyway, for this to work, you’ll need to establish a few things about your computer before rushing out and buying that second video card.

1. A motherboard that has two video card capable PCI Express slots. Most aftermarket and enthusiast motherboards have this, but if you bought a system from say, Dell, it’s less clear.
2. A power supply with enough headroom to drive two video cards. Warning: modern gaming video cards are major power hogs – they *easily* pull 100 to 200 watts under load. *Each.* Sometimes more than that! Be absolutely sure you have a quality power supply rated for a minimum of 600 watts. Each video card will have two power connectors, either 6 or 8 pin. Check that your power supply offers enough connectors, or that you have converters on hand.
3. A case with sufficient airflow to dissipate the 400 to 800 watts of CPU and GPU heat that you’ll be generating. Understand that this is *serious* amounts of heat while gaming, way more than even the highest of high end PCs would normally produce. Yes, it is possible to do this quietly (at least in the typical idle case), but it will take some engineering work.


Beyond *that*, I found there are some additional peculiarities of multi-GPU systems that you need to be aware of.

- Make sure that the two cards you use are not only of the exact same family (minor vendor differences are OK) but also **have *identical* clock and memory speeds**. It’s not supposed to matter, but I found that it did and I had to flash one of my cards to set it to default speeds to match the other card.
- Do not attempt to overclock your system while getting the multiple GPUs up and running. In particular, be *extremely* careful not to mess with the bus speed as timings are critical when dealing with two GPUs on the PCI Express bus synchronizing their work. [Trust me on this one](http://superuser.com/questions/343115/ati-crossfire-instability-and-horizontal-bands).
- Do a clean video driver remove and install the very very latest video drivers after putting the second card in. I recommend [Driver Sweeper](http://phyxion.net/item/driver-sweeper.html) to remove any traces of your old drivers before rebooting.


Don’t say I didn’t warn you about this stuff, because I said it would be technically complex in the first paragraph. **But after a (lot) of teething pains, I’m happy to report that multiple GPUs really does work as advertised.** I can crank up games to the absolute maximum settings on my 27" monitor and get nearly constant 60 frames per second. As you can see in the below example, we go from 44 fps to 77 fps in [Battlefield: Bad Company 2.](http://www.anandtech.com/show/4061/amds-radeon-hd-6970-radeon-hd-6950/18)


![](https://blog.codinghorror.com/content/images/2025/04/image-555.png)


Now, Battlefield 3 (beta) is [so very bleeding edge](https://web.archive.org/web/20111214033717/http://www.pcgameshardware.com/aid,847209/Battlefield-3-Beta-18-Radeon-and-Geforce-cards-SLI-und-Crossfire-benchmarked/Practice/) that I can’t quite get it to max settings *even with two GPUs in play*. But I can now run very high settings, much higher than I could with a single GPU.


To be honest, it’s unlikely I will continue with multiple GPUs through 2012 when the next-generation video cards are released. **With every new video card introduction, you’re *supposed* to get about the same performance in the new card as you did with two previous generation video cards working together.** So at best this is a sort of sneak preview, cheating time by pretending we have a next-generation video card today. There are obvious efficiencies involved in performing that parallelization on a single GPU die rather than through two distinct video cards sitting on the PCI bus.


There’s also the issue of [micro-stuttering](https://web.archive.org/web/20111023051252/http://techreport.com/articles.x/21516). I personally haven’t found that to be a big problem unless you’re pushing the graphics settings beyond what even two cards can reliably deliver. But if the frame rate dips low enough, the overhead of synchronization between the cards can interfere with overall frame rate in a perceptible way.


**A single fast video card is *always* going to be the simpler, easier, and cheaper route.** But multiple video cards sure is nifty tech in its own right, and it wasn’t too expensive to get started with at $170. In the meantime, I’m having a ball playing with it, and I am dying to test my configuration with the final release of Battlefield 3 on October 25th. Join me if you like!

[graphics cards](https://blog.codinghorror.com/tag/graphics-cards/)
[gaming](https://blog.codinghorror.com/tag/gaming/)
[video performance](https://blog.codinghorror.com/tag/video-performance/)
[hardware](https://blog.codinghorror.com/tag/hardware/)
[pc gaming](https://blog.codinghorror.com/tag/pc-gaming/)
