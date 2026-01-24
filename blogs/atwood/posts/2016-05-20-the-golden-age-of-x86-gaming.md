---
title: "The Golden Age of x86 Gaming"
date: 2016-05-20
url: https://blog.codinghorror.com/the-golden-age-of-x86-gaming/
slug: the-golden-age-of-x86-gaming
word_count: 1770
---

I’ve been happy with [my 2016 HTPC](https://blog.codinghorror.com/the-2016-htpc-build/), but the situation has changed, largely because of something I mentioned in passing back in November:

kg-card-begin: html

> The Xbox One and PS4 are effectively plain old PCs, built on:
> Intel Atom class (aka slow) AMD 8-core x86 CPU
> 8 GB RAM
> AMD Radeon 77xx / 78xx GPUs
> cheap commodity 512GB or 1TB hard drives (not SSDs)
> The **golden age of x86** gaming is well upon us. That’s why the future of PC gaming is looking brighter every day. We can see it coming true in the solid GPU and idle power improvements in Skylake, riding the inevitable wave of x86 becoming the dominant kind of (non mobile, anyway) gaming for the foreseeable future.

kg-card-end: html

And then, the bombshell. It is all but announced that Sony will be [upgrading the PS4](http://arstechnica.com/gaming/2016/04/ps4k-neo-details-specs-revealed-rumours/) this year, no more than three years after it was first introduced… **just like you would upgrade a PC.**

kg-card-begin: html

> Sony may be tight-lipped for now, but it’s looking increasingly likely that the company will release an updated version of the PlayStation 4 later this year. So far, the rumored console has gone under the moniker PS4K or PS4.5, but a new report from gaming site GiantBomb suggests that the codename for the console is “NEO,” and it even provides hardware specs for the PlayStation 4’s improved CPU, GPU, and higher bandwidth memory.
> CPU: 1.6 → 2.1 Ghz CPU
> GPU: 18 CUs @ 800Mhz → 36 CUs @ 911Mhz
> RAM: 8GB DDR5 176 GB/s → 218 GB/s

kg-card-end: html

In PC enthusiast parlance, you might say Sony just slotted in a new video card, a faster CPU, and slightly higher speed RAM.


![](https://blog.codinghorror.com/content/images/2025/02/image-67.png)


This is old hat for PCs, but to release a new, faster model that is perfectly backwards compatible is almost unprecedented in the console world. I have to wonder if this is partially due to the [intense performance pressure of VR](https://blog.codinghorror.com/i-tried-vr-and-it-was-just-ok/), but whatever the reason, I applaud Sony for taking this step. It’s a giant leap towards consoles being more like PCs, and **another sign that the golden age of x86 is really and truly here.**


I hate to break this to PS4 enthusiasts, but as big of an upgrade as that is – and it really is – it’s still nowhere *near* enough power to drive modern games at 4k. Nvidia’s [latest and greatest 1080 GTX](http://arstechnica.com/gadgets/2016/05/nvidia-gtx-1080-review/) can only sometimes manage 30fps at 4k. The increase in required GPU power when going from 1080p to 4k is so vast that even the PC “cost is no object” folks who will happily pay $600 for a video card and $1000 for the rest of their box have some difficulty getting there today. Stuffing all that into a $299 box for the masses is going to take quite a few more years.


![](https://blog.codinghorror.com/content/images/2025/02/image-68.png)


Still, I like the idea of the PS4 Neo so much that I’m considering buying it myself. I strongly support this sea change in console upgradeability, even though I swore I’d stick with the Xbox One this generation. To be honest, my Xbox One has been a disappointment to me. I bought the “Elite” edition because it had a hybrid 1TB drive, and then added a 512GB USB 3.0 SSD to the thing and painstakingly moved all my games over to that, and it is *still* appallingly slow to boot, to log in, to page through the UI, to load games. It’s also noisy under load and sounds like a broken down air conditioner even when in low power, background mode. The Xbox One experience is way too often drudgery and random errors instead of the gaming fun it’s supposed to be. Although I do unabashedly love the new controller, I feel like the Xbox One is, overall, a worse gaming experience than the Xbox 360 was. And that’s sad.


Or maybe I’m just spoiled by PC performance, and the relatively crippled flavor of PC you get in these $399 console boxes. If all evidence points to the golden age of x86 being upon us, why not double down on x86 in the living room? Heck, while I’m at it… why not *triple down?*


![](https://blog.codinghorror.com/content/images/2025/02/image-69.png)


This, my friends, is what tripling down on x86 in the living room looks like.


It’s Intel’s latest [Skull Canyon NUC](http://www.amazon.com/dp/B01DJ9XS52/). What does that acronym stand for? Too embarrassing to explain. Let’s just pretend it means “tiny awesome x86 PC.” What’s significant about this box is it contains **the first on-die GPU Intel has ever shipped that can legitimately be considered console class**.


![](https://blog.codinghorror.com/content/images/2025/02/image-70.png)


It’s not cheap at $579, but this tiny box bristles with cutting edge x86 tech:

- Quad-core i7-6770HQ CPU (2.6 Ghz / 3.5 Ghz)
- Iris Pro Graphics 580 GPU with 128MB eDRAM
- Up to 32GB DDR4-2666 RAM
- Dual M.2 PCI x4 SSD slots
- 802.11ac WiFi / Bluetooth / Gigabit Ethernet
- Thunderbolt 3 / USB 3.1 gen 2 Type-C port
- Four USB 3.0 ports
- HDMI 2.0, mini-DP 1.2 video out
- SDXC (UHS-I) card reader
- Infrared sensor
- 3.5mm combo digital / optical out port
- 3.5mm headphone jack


All impressive, but the most remarkable items are the GPU and the Thunderbolt 3 port. Putting together a HTPC that can kick an Xbox One’s butt as a gaming box is now as simple as adding these three items together:

1. Intel NUC kit NUC6i7KYK – $579
2. [16GB DDR4-2400](http://www.amazon.com/dp/B014R8JWEA/) – $75
3. [Samsung 950 Pro NVMe M.2 (512GB)](http://www.amazon.com/dp/B01639694M/) – $317


Ok, fine, it’s a cool **$970** plus tax compared to $399 for one of those console x86 boxes. But did I mention it has *skulls* on it? *Skulls!*


The CPU and disk performance on offer here are hilariously far beyond what’s available on current consoles:

- Disk performance of the two internal PCIe 3.0 4x M.2 slots, assuming you choose a proper NVMe drive as you should, is measured in not megabytes per second but [*gigabytes* per second.](http://www.anandtech.com/show/10303/choosing-the-right-ssd-for-a-skylakeu-system/2) Meanwhile consoles lumber on with, at best, hybrid drives.
- The Jaguar class AMD x86 cores in the Xbox One and PS4 are about the same as the [AMD A4-5000 reviewed here](http://anandtech.com/show/7314/intel-baytrail-preview-intel-atom-z3770-tested/2); those benchmarks indicate a modern Core i7 will be about [four times faster](http://www.anandtech.com/show/7003/the-haswell-review-intel-core-i74770k-i54560k-tested/6).


But most importantly, its [GPU performance is on par](http://nucblog.net/2016/05/skull-canyon-nuc-review-conclusion/) with current consoles. NUC blog measured **41fps average** in Battlefield 4 at 1080p and medium settings. Digging through old benchmarks I find plenty of pages where a Radeon 78xx or 77xx series video card, the closest analog to what’s in the XBox One and PS4, achieves a [similar result in Battlefield 4](http://www.bit-tech.net/hardware/graphics/2013/11/27/battlefield-4-performance-analysis/3):


![](https://blog.codinghorror.com/content/images/2016/05/radeon-77xx-perf-bf4-1080p-medium.png)


I personally benchmarked GRID 2 at 720p (high detail) on all three of the last HTPC models I owned:

kg-card-begin: html


|  | Max | Min | Avg |
| i3-4130T, HD 4400 | 32 | 21 | 27 |
| i3-6100T, HD 530 | 50 | 32 | 39 |
| i7-6770HQ, Iris Pro 580 | 96 | 59 | 78 |


kg-card-end: html

When I up the resolution to 1080p, I get **59fps average**, 38 min, 71 max. Checking with [Notebookcheck’s exhaustive benchmark database](http://www.notebookcheck.net/Computer-Games-on-Laptop-Graphics-Cards.13849.0.html), that is closest to the AMD R7 250, a rebranded Radeon 7770.


What we have here is legitimately the first on-die GPU that can compete with a low-end discrete video card from AMD or Nvidia. Granted, an older one, one you could buy for about $80 today, but one that is certainly equivalent to what’s in the Xbox One and PS4 *right now*. This is a real first for Intel, and it probably won’t be the last time, considering that on-die GPU performance increases have massively outpaced CPU performance increases for the last 5 years.


As for power usage, I was pleasantly surprised to measure that this box idles at **15w** at the Windows Desktop doing nothing, and drops to **13w** when the display sleeps. Considering the best idle numbers I’ve measured are from the [Scooter Computer](https://blog.codinghorror.com/the-scooter-computer/) at 7w and my previous HTPC build at 10w, that’s not bad at all! Under full game load, it’s more like 70 to 80 watts, and in typical light use, 20 to 30 watts. It’s the idle number that matters the most, as that represents the typical state of the box. And compared to the [75 watts a console uses](http://www.extremetech.com/gaming/182829-new-report-slams-xbox-one-and-ps4-power-consumption-inefficiencies-still-abound) even when idling at the dashboard, it’s no contest.


Of course, 4k video playback is no problem, though 10-bit 4K video may be a stretch. If that’s not enough – if you dream bigger than medium detail 1080p gameplay – the presence of a Thunderbolt 3 port on this little box means you can, at considerable expense, use **any external GPU of your choice**.


![](https://blog.codinghorror.com/content/images/2016/05/razer-core-external-GPU.jpg)


That’s the Razer Core external graphics dock, and it’s $499 all by itself, but it opens up an entire world of upgrading your GPU to whatever the heck you want, as long as your x86 computer has a Thunderbolt 3 port. And it really works! In fact, here’s a video of it working live with this exact configuration:


Zero games are meaningfully CPU limited today; the disk and CPU performance of this Skull Canyon NUC is already so vastly far ahead of current x86 consoles, even the PS4 Neo that’s about to be introduced. So being able to replace the one piece that needs to be the most replaceable is huge. Down the road you can add the latest, greatest GPU model whenever you want, just by plugging it in!


The only downside of using such a small box as my HTPC is that my two 2.5″ 2TB media drives become external USB 3.0 enclosures, and I am limited by the 4 USB ports. So it’s a little… cable-y in there. But I’ve come to terms with that, and its tiny size is an acceptable tradeoff for all the cable and dongle overhead.


![](https://blog.codinghorror.com/content/images/2016/05/skull-canyon-with-razer-core-external.jpg)


I still remember how shocked I was when [Apple switched to x86](https://blog.codinghorror.com/x86-uber-alles/) back in 2005. I was also surprised to discover just how thoroughly both the PS4 and Xbox One embraced x86 in 2013. Add in the current furor over VR, plus the PS4 Neo opening new console upgrade paths, and the future of x86 as a gaming platform is rapidly approaching supernova.


If you want to experience what console gaming will be like in 10 years, invest in a Skull Canyon NUC and an external Thunderbolt 3 graphics dock today. **If we are in a golden age of x86 gaming, this configuration is its logical endpoint.**

[x86 gaming](https://blog.codinghorror.com/tag/x86-gaming/)
[pc gaming](https://blog.codinghorror.com/tag/pc-gaming/)
[gaming trends](https://blog.codinghorror.com/tag/gaming-trends/)
