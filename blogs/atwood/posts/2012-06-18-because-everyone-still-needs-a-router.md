---
title: "Because Everyone (Still) Needs a Router"
date: 2012-06-18
url: https://blog.codinghorror.com/because-everyone-still-needs-a-router/
slug: because-everyone-still-needs-a-router
word_count: 967
---

About a year and a half ago, I [researched the state of routers](https://blog.codinghorror.com/because-everyone-needs-a-router/): about as unsexy as it gets but essential to the stability, reliability, and security of your Internet connection. My conclusion?


> This is boring old plain vanilla commodity router hardware, but when combined with an open source firmware, it is a massive improvement over my three year old, proprietary high(ish) end router. The magic router formula these days is **a combination of commodity hardware and open-source firmware**. I’m so enamored of this one-two punch combo, in fact, I might even say it represents the future. Not just of the everyday workhorse routers we all need to access the Internet – but the future of *all* commodity hardware.


I felt a little bad about that post, because I quickly migrated from the [DD-WRT](http://en.wikipedia.org/wiki/DD-WRT) open source firmware to [OpenWRT](http://en.wikipedia.org/wiki/OpenWrt) and then finally settled on [Tomato](http://en.wikipedia.org/wiki/Tomato_(firmware)). I guess that’s open source, too many choices with nobody to really tell you what’s going to work reliably on your particular hardware. But the good news is that **I’ve been running Tomato quite happily with total stability for about a year now** – primarily because it is [gloriously simple](http://team-noehring.de/extern/wrt54gl/tomato125/tomato125.htm), but also because it has the most functional quality of service (QoS) implementation.


![](https://blog.codinghorror.com/content/images/2025/04/image-646.png)


Why does functional Quality of Service matter so very much in a router? Unless you have an Internet connection that’s only used by your grandmother to visit her church’s website on Sundays, **QoS is the difference between a responsive Internet and one that’s brutally dog slow**.


> Ever sat in an internet shop, a hotel room or lobby, a local hotspot, and wondered why you can’t access your email? Unknown to you, the guy in the next room or at the next table is hogging the internet bandwidth to download the Lord Of The Rings Special Extended Edition in 1080p HDTV format. You’re screwed - because the hotspot router does not have an effective QoS system. In fact, I haven’t come across a shop or an apartment block locally that has any QoS system in use at all. Most residents are not particularly happy with the service they [usually] pay for.


When I switched from DD-WRT and OpenWRT to Tomato, I had to buy a different router, because Tomato only supports certain router hardware, primarily Broadcom. The almost universal recommendation was the [Asus RT-N16](http://www.amazon.com/dp/B00387G6R8), so that’s what I went with.


![](https://blog.codinghorror.com/content/images/2025/04/image-645.png)


And it is still an *excellent* choice. If you just want a **modern, workhorse single band wireless N router** that won’t break the bank, but has plenty of power and memory to run Tomato, definitely try the Asus RT-N16. It’s currently available for under $80 (after $10 rebate). Once you get Tomato on there, you’ve got a fine combination of hardware and software. Take it from [this SmallNetBuilder user review](http://www.smallnetbuilder.com/wireless/wireless-reviews/31058-asus-rt-n16-gigabit-n-router-reviewed?showall=&start=4):


> I’m a semigeek. Some of the stuff on this site confuses me. But I figured out enough to get this router and install Tomato USB. Great combination. Have not had any problems with the router. Love all the features that Tomato gives me. Like blocking my son’s iPod after 7 PM. Blocking certain websites. Yeah, I know you can do that with other routers but Tomato made it easy. Also love the QoS features. Netflix devices get highest bandwidth while my wife’s bittorrent gets low.
> Review was too heavily slanted against the Asus software, which I agree is crap. I bought the router for its hardware specs. Large memory. Fast processor. Gigabyte lan. 2 USB ports.


What’s not to love? Well, the dual band thing, mainly. If you want **a truly top of the line router with incredible range**, and simultaneous dual band 2.4 GHz and 5 GHz performance bragging rights, fortunately there’s the [Asus RT-N66U](http://www.amazon.com/dp/B006QB1RPY).


![](https://blog.codinghorror.com/content/images/2025/04/image-644.png)


This is, currently at least, the state of the art in routers. It has a faster CPU and twice the memory (256 MB) of the RT-N16. But at $190 it is also over twice the price. Judge for yourself in [the SmallNetBuilder review](http://www.smallnetbuilder.com/wireless/wireless-reviews/31687-asus-rt-n66u-dark-knight-dual-band-wireless-n900-gigabit-router-reviewed):


> As good as the RT-66U is, our wireless performance results once again show that no router is good in every mode that we test. But that said, the Dark Knight clearly outperformed both the NETGEAR WNDR4500 and Cisco Linksys E4200V2 in most of our two and three-stream tests. And it’s the only router in recent memory able to reach to our worst-case/lowest-signal test location on the 5 GHz band, albeit with barely-usable throughput. Still, this is an accomplishment in itself.
> If you’re going to spend close to $200 for a wireless router, you should get a lot for your money. The Dark Knight seems to deliver wireless performance to justify its high price and has routing speed fast enough to handle any service a consumer is likely to have, even our friends in Europe and Asia.


Its only weakness? Take a guess. Oh wait, no need to guess, it’s the same “weakness” the RT-N16 shared, the sketchy Asus firmware it ships with out of the box. **That’s why we get our Tomato on, people!** There is complete and mature support for the RT-N66U in Tomato; for a walkthrough on how to get it installed (don’t be shy, it’s not hard) Check out Shadow Andy’s [TomatoUSB firmware flashing guide](http://www.shadowandy.net/2012/03/asus-rt-n66u-tomatousb-firmware-flashing-guide.htm).


Does having nice router hardware with a current open source firmware matter? Well, if your livelihood depends on the Internet like mine does, then I certainly think so.


![](https://blog.codinghorror.com/content/images/2025/04/image-643.png)


At the very least, if you or someone you love is also an Internet fan and **hasn’t given any particular thought to what router they use**, maybe it’s time to start checking into that. Now if you’ll excuse me, I’m going to go [donate to the Tomato project](https://blog.codinghorror.com/today-is-support-your-favorite-small-software-vendor-day/).

[routers](https://blog.codinghorror.com/tag/routers/)
[firmware](https://blog.codinghorror.com/tag/firmware/)
[open source](https://blog.codinghorror.com/tag/open-source/)
[hardware](https://blog.codinghorror.com/tag/hardware/)
[technology trends](https://blog.codinghorror.com/tag/technology-trends/)
