---
title: "Building a Quiet PC"
date: 2006-08-22
url: https://blog.codinghorror.com/building-a-quiet-pc/
slug: building-a-quiet-pc
word_count: 1410
---

When the first version of Windows Media Center was released in summer 2003, I decided it was time to build my first home theater PC. After I placed it in the living room, I realized I had made a terrible mistake: I had to turn the volume up to 11 just to drown out the noise of the HTPC! I couldn’t believe how loud it was! For the next few months, I immersed myself in the world of [silent PC enthusiasts](http://www.silentpcreview.com/). I must have reconfigured that system a dozen times to reduce the noise.


Now every PC I build is optimized for performance *and* low noise from the very beginning.


Anyone can build a high-powered rig that sounds like a jet taking off. Building a high-powered rig that’s so quiet your wife can’t tell when it’s turned on or off – now *that’s* an accomplishment! It’s a bona-fide engineering challenge.


In the process, I’ve learned quite a few things about building quiet PCs. I’d like to share them with you, so you can avoid making the mistakes I did.


The easiest way to build a quiet PC is to start with components that run cool.


### 1. The easiest way to build a quiet PC is to start with components that run cool.


It’s as fundamental as the first law of thermodynamics: heat has to be exhausted from the system; more heat equals more noise. If you truly want a quiet system, start with cool running components. The three components that generate the most heat in your system are...

1. CPU
2. video card
3. power supply


... in that order. Select these items very carefully, because they will account for 90 percent of the heat and noise generated inside your computer. Research how many watts of power each will draw when idle; when normally loaded; and when fully loaded. And don’t underestimate the [importance of the power supply](http://www.silentpcreview.com/article28-page6.html); it’s the heart of your system, and it can be the source of serious stability, noise, and heat woes if you pick a clunker. The very *best* power supplies are only about 85% efficient, which means they’re still dumping 15% of the total power draw back into your case as waste heat.


### 2. Minimize the number of fans in your system.


Every fan is a source of noise. Remove fans unless they’re absolutely necessary. If a fan is necessary, use the largest possible model. All other things being equal, large fans are quieter than small fans. That’s why 120mm fans are now commonplace in PC cases.


One of the most useful noise diagnostics is to stop every fan in the system, one by one, using your Mark I finger. Repeat this a few times, listening closely to hear the difference with each fan stopped. Then try to eliminate or slow down the noisiest fan. Don’t forget to test your video cards and motherboard fans while you’re at it; these tend to be particularly noisy due to their small size. And remember, kids, always stop fans by touching them in the center, not in those whirling blades!


### 3. Control the speed of your fans.


Fans running at full speed are almost never quiet. Some modern motherboards allow you to control the speed of the fans connected via the 3-pin motherboard headers, either in the BIOS or in software. Set an absolute speed, or even better, use dynamic fan speeds based on a temperature sensor; spin faster when it gets hot, and slow down when things cool off. There are also devices like the Zalman Fanmate that allow you to retrofit a fan speed control on any 3-pin fan.


![](https://blog.codinghorror.com/content/images/2025/04/image-704.png)


The Zalman 56 Ohm resistor is a less expensive option if you don’t need precise speed control.


### 4. Consider aftermarket cooling solutions.


Aftermarket coolers for CPUs and video cards are typically *far* more efficient than the stock models manufacturers include. You might be able to get away with inefficient stock coolers for basic systems, but if you want high-end performance, a super-efficient cooler can literally be the difference between a quiet system and a loud system.

- The current top dogs for CPU cooling efficiency are tall heatpipe stack designs such as the [Thermalright Ultra-120](http://www.silentpcreview.com/article646-page1.html) and the [Scythe Ninja](http://www.silentpcreview.com/article251-page1.html).
- The current top dogs for VGA cooling efficiency are copper heatpipe designs, such as the Arctic Cooling [Accelero X1](http://www.techgage.com/article/arctic_cooling_accelero_x1) and the Zalman [VF900-CU](http://www.silentpcreview.com/article612-page5.html).
- Consider replacing any small fan and heatsink combinations – such as the [ones commonly found on motherboards](https://web.archive.org/web/20060906000702/http://forums.tweakguides.com/showthread.php?t=1408&page=2) – with larger, passive coolers. Two great options are the Zalman NB47J and the newer, flower style Zalman NBF47.


![](https://blog.codinghorror.com/content/images/2025/04/image-705.png)


![](https://blog.codinghorror.com/content/images/2025/04/image-706.png)


![](https://blog.codinghorror.com/content/images/2025/04/image-707.png)


Note that aftermarket coolers tend to be quite a bit larger than stock coolers; measure to make sure they’ll fit in your system before buying.


### 5. Dampen your hard drive.


Hard drive manufacturers have made huge strides in noise reduction in the last few years. You still need to be a bit careful in selecting a drive, but most new hard drives are relatively quiet. That’s the good news. The bad news is that hard drives are still giant hunks of metal spinning at 7,200 or 10,000 RPM.


As such, the first order of business here is to dampen the drives – make absolutely sure there is a soft material of some kind between the hard drive and your PC’s case. Some people improvise bungee suspension slings, some people use foam or sorbothane, some people [put them in dampening enclosures](http://www.silentpcreview.com/article245-page1.html). Whatever you do, always avoid metal-to-metal contact between a hard drive and the case.


![](https://blog.codinghorror.com/content/images/2025/04/image-708.png)


The truly hardcore use 2.5" laptop hard drives, which are even quieter, but they also have significant performance and price penalties over standard 3.5" desktop drives.


### 6. Use noise-reduction materials.


If you’ve ever worked in a recording studio where the walls are covered with noise-reduction materials, you’ve probably heard first-hand how effective they can be. However, noise reduction materials are *strictly* a second line of defense. They treat the symptom and not the source; ideally you want to quiet the thing that is making noise – not hide it behind a layer of dampening material.


That said, noise reduction materials can help take the edge off the last remaining bit of noise in a system. For PC builds, I like pax.mate and generic eggcrate foam. You can see pictures of both materials in action in this SilentPCReview thread [documenting a LAN party system](http://www.silentpcreview.com/forums/viewtopic.php?p=123107) I built in summer 2004. But they should always be a final, finishing step.


![](https://blog.codinghorror.com/content/images/2025/04/image-709.png)


I’m ashamed to admit that I have something of an eggcrate foam fetish. In addition to wedging it inside my systems wherever it’ll fit, I regularly put cardboard-mounted panels of the eggcrate foam behind my PCs to reduce the reflected noise from the rear exhaust fans. If your PC is under a desk, fitting eggcrate foam along the undersides of the desk can be surprisingly effective, too.


### 7. Passive cooling isn’t worth it.


If you really get bitten by the silence bug, you’ll invariably be drawn to that holy grail of silent computing: completely passive cooling. Passive cooling is totally silent by definition, but also it’s the equivalent of scaling the Himalayas – not something you undertake lightly and certainly not without a few years of experience under your belt.


Although there are exotic pre-built passive solutions like Zalman’s [TNN-500A](http://www.silentpcreview.com/article161-page1.html) and [TNN-300](http://www.silentpcreview.com/article302-page1.html) cases, they’re solidly in the “if you have to ask how much it costs, [you can’t afford it](https://web.archive.org/web/20071021034340/http://www.svc.com/zm-ttn500a.html)” category.


![](https://blog.codinghorror.com/content/images/2025/04/image-710.png)


Passive cooling setups are an order of magnitude more difficult to cool: they require a tricky balance of careful construction, natural convective airflow, and setup tweaking. You can achieve 90 percent of the results you’d get with completely passive cooling using a few nearly-silent, slow-moving fans – at a fraction of the effort and risk!


I can’t emphasize enough that **the best way to quiet your PC is to begin with the right parts.** If you’re really serious about silence, ensure that you have...

- CPUs and video cards that run cool
- a quiet, efficient power supply
- hard drives that run relatively quiet as shipped


Always try to deal with the *source* of the noise first. Beyond that, following the few tips I outlined above will eventually get you to near-complete silence – or at least to below-ambient noise level, which is pretty much the same thing.

[hardware](https://blog.codinghorror.com/tag/hardware/)
[pc building](https://blog.codinghorror.com/tag/pc-building/)
[noise reduction](https://blog.codinghorror.com/tag/noise-reduction/)
[home theater pc](https://blog.codinghorror.com/tag/home-theater-pc/)
[silent pc](https://blog.codinghorror.com/tag/silent-pc/)
