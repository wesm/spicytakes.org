---
title: "Revisiting the Home Theater PC"
date: 2011-03-28
url: https://blog.codinghorror.com/revisiting-the-home-theater-pc/
slug: revisiting-the-home-theater-pc
word_count: 900
---

It’s been almost three years since I [built my home theater PC](https://blog.codinghorror.com/building-your-own-home-theater-pc/). I *adore* that little machine; it drives all of our family entertainment and serves as a general purpose home media server and streaming box. As I get older, I find that I’m no longer interested in having a home full of PCs whirring away. I only want *one* PC in my house on all the time, and I want it to be as efficient and versatile as possible.


My old low-power Athlon X2 based HTPC generally worked great, but still struggled with some occasional 1080p content. And when you have a toddler in the house, believe me, you *need* reliable 1080p playback. Only the finest in children’s entertainment for my [spawned process](https://blog.codinghorror.com/spawned-a-new-process/), I say!


When I recently had to transcode [Megamind](http://www.imdb.com/title/tt1001526/) down to 720p to get it to play back without stuttering or pausing at times… I knew my current HTPC’s days were numbered.


![](https://blog.codinghorror.com/content/images/2025/04/image-518.png)


(Megamind is *hilarious* and highly recommended, by the way; it’s far better than its Metacritic and Rotten Tomatoes percentages would seem to indicate.)


Now that Intel has finally released their Sandy Bridge CPUs – the first with integrated GPUs – I was eager to revisit and rebuild. The low power Core i3-2100T is the one I had my eye on, with **a miserly TDP of 35 watts**. Combine that with a decent [Mini-ITX](https://blog.codinghorror.com/the-impossibly-small-pc-nano-itx/) motherboard and a few other essential parts, and you’re good to go:

kg-card-begin: html


| CPU | Intel Core i3-2100T | $135 |
| Motherboard | ASRock H67M ITX | $100 |
| RAM | Corsair 4GB DDR3 | $45 |
| Case + PSU | Antec ISK 300-65 | $70 |
| HDD | 750GB 2.5" | $70 |


kg-card-end: html

Now, I am fudging a bit here. This is just the basic level of hardware to get a functional home theater PC. I didn’t actually buy a case, PSU, or even hard drive for that matter; I recycled many of my old existing parts, so my personal outlay was all of 300 bucks. I’m including the fuller part list as courtesy recommendations in case you’re starting from scratch. You also might want to add a Blu-Ray drive, and perhaps a Windows 7 Home Premium license ($99) for its excellent 10-foot [Windows Media Center](https://blog.codinghorror.com/windows-vista-media-center/) interface.


![](https://blog.codinghorror.com/content/images/2025/04/image-517.png)


The magical part here is the extreme level of hardware integration: the CPU has a GPU and memory controller on die, and the motherboard has optical digital out and HDMI out built in. It’s delightfully simple to build and downright *cheap*. Just assemble it, install your OS of choice (sorry, Apple fans), then plug it into your receiver and television and boot it up.


My results? I’ll just get right to the good part, but please bear in mind **each step is about twice as powerful** as the one before:

kg-card-begin: html


| [2005](https://blog.codinghorror.com/pentium-m-home-theater-pc/) | ~$1000 | 512 MB RAM, single core CPU | 80 watts idle |
| 2008 | ~$520 | 2 GB RAM, dual core CPU | 45 watts idle |
| **2011** | **~$420** | **4 GB RAM, dual core CPU + GPU** | **22 watts idle** |


kg-card-end: html

I know I get way too excited about this stuff, but… *holy crap, 22 tesla-lovin’ watts at idle!*


![](https://blog.codinghorror.com/content/images/2025/04/image-516-1.png)


The [kill-a-watt never lies](https://blog.codinghorror.com/revisiting-how-much-power-does-my-laptop-really-use/). To be fair, it’s more like 25 watts idle with [torrents in the background](https://blog.codinghorror.com/everybody-loves-bittorrent/). This little box is remarkably efficient; even when playing back a 1080p video it’s not unusual to see CPU usage well under 50%, which equates to around 30-35 watts in practice. Under full, artificial multithreaded Prime95 load, it tops out at an absolute peak of 55 watts.

kg-card-begin: html

(Update: I ended up replacing my old Seasonic ECO 300 SFX power supply with a [Pico PSU-90 plus 60 watt](http://www.amazon.com/exec/obidos/ASIN/B0035UETHW) adapter kit. That got the idle power down from 22 watts to **17 watts**, a solid savings of 22%. Recommended!)

kg-card-end: html

This is a killer setup, but don’t take my word for it. There is an [excruciatingly in-depth review](http://www.missingremote.com/review/intel-core-i3-2100t-and-bh67cf-mini-itx-motherboard) of essentially the same system at [Missing Remote](http://www.missingremote.com/), with a particular eye toward home theater duties. Spoiler: they loved the hell out of it too. And it compromises almost nothing in performance, with a Windows Experience score of 5.1 – that would be a solid 5.8 if you factored out desktop Aero performance.


![](https://blog.codinghorror.com/content/images/2025/04/image-515.png)


(Also, in case you’re wondering, I intentionally dropped the analog cable tuner. All modern cable is now digital, which means awkward DRM-ed up the wazoo CableCard systems. I’ve cancelled cable altogether; I’d rather take that $60+ per month and use it to support innovative companies who will deliver media through the internet, like Netflix, Hulu, etcetera. Or as I like to call it: *the future*, unless the media conglomerates with vaults full of cash manage to [subvert net neutrality](https://blog.codinghorror.com/the-importance-of-net-neutrality/).)


When all is said and done, I have a new always-on, does-anything home theater box that is **twice as fast as the one I built in 2008, while consuming less than half the power**.


I’ve been a computer nerd since age 8, and I just turned 40. I should be jaded by [computer hardware pornography](https://blog.codinghorror.com/computer-hardware-pornography/) by now, but I still find this progress *amazing*. At this rate, I can’t wait to find out what my 2014 home theater PC will look like.

[media server](https://blog.codinghorror.com/tag/media-server/)
[home theater](https://blog.codinghorror.com/tag/home-theater/)
[htpc](https://blog.codinghorror.com/tag/htpc/)
[streaming](https://blog.codinghorror.com/tag/streaming/)
[1080p playback](https://blog.codinghorror.com/tag/1080p-playback/)
