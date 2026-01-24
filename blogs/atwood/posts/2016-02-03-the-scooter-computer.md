---
title: "The Scooter Computer"
date: 2016-02-03
url: https://blog.codinghorror.com/the-scooter-computer/
slug: the-scooter-computer
word_count: 1895
---

When we initially deployed our [handbuilt colocated servers](https://blog.codinghorror.com/building-servers-for-fun-and-prof-ok-maybe-just-for-fun/) for Discourse in 2013, I needed a way to provide an isolated VPN channel in for secure remote access and troubleshooting. Rather than dedicate a whole server to [this task](https://blog.codinghorror.com/because-everyone-still-needs-a-router/), I purchased the inexpensive, open source firmware friendly Asus RT-N16 router, flashed it with the popular TomatoUSB open source firmware, removed the antennas, turned off the WiFi and dropped it off in our colocated rack to let it act as a dedicated VPN access point.


![](https://blog.codinghorror.com/content/images/2025/02/image-84.png)


And that box – which was $100 then and around $70 now – worked well enough until now. Although the version of OpenSSL in the 2012 era Tomato firmware we used is not vulnerable to Heartbleed, it’s still getting out of date in terms of the encryption it supports and allows. And Tomato itself is updated sporadically, chaotically at best.


Let’s face it: **this is just a little box that runs a chopped up version of Linux**, with a bit of specialized wireless hardware and multiple antennas tacked on… that we’re not even using. So when it came time to upgrade, we wondered:


> Why not just go with a small box that can run a real, full Linux distro? Wouldn’t that be simpler and easier to keep up to date?


After doing some research and asking on Twitter, I discovered there are a ton of amazing little Broadwell “mini-PC” boxes [available on AliExpress](http://www.aliexpress.com/category/70803003/mini-pcs.html).


![](https://blog.codinghorror.com/content/images/2016/02/IMG_2485.JPG)


![](https://blog.codinghorror.com/content/images/2016/02/IMG_2486.JPG)


The specs are kind of amazing for the price. I paid **~$350** each for the ones I selected:

- [i5-5200](https://web.archive.org/web/20160421010137/http://ark.intel.com/products/85212/Intel-Core-i5-5200U-Processor-3M-Cache-up-to-2_70-GHz) Broadwell 2 core / 4 thread CPU at 2.2 Ghz - 2.7 Ghz
- 16GB DDR3 RAM
- 128GB M.2 SSD
- Dual gigabit Realtek 8168 ethernet
- front 4 USB 3.0 ports / rear 4 USB 2.0 ports
- Dual HDMI out


(There’s also optical and analog audio connectors on the front, as well as a SD card reader, which I covered with a sticker since we had no need for audio. I also stripped the WiFi out since we didn’t need it, but it was included for the price, too.)


Selecting the [i5-4258u](https://web.archive.org/web/20160809023843/http://ark.intel.com/products/75990/Intel-Core-i5-4258U-Processor-3M-Cache-up-to-2_90-GHz), 4GB RAM, and 64GB SSD pushes the price down to **$270**. That’s still a solid CPU, only a single generation behind Intel’s latest and greatest Skylake, and carrying the midrange i5 moniker; it’s no pushover. There are also many, many variants of this box from other AliExpress sellers that have slightly older, cheaper CPUs that are still plenty powerful. You can easily spec a box similar to this one for $200.


That’s not a whole lot more than the $200 you’d pay for a high end router these days, and as Ars Technica notes, the average [x86 box is radically faster](http://arstechnica.com/gadgets/2016/01/numbers-dont-lie-its-time-to-build-your-own-router/).


![](https://blog.codinghorror.com/content/images/2025/02/image-85.png)


Note that the above graphs, “homebrew” means an old, 1.8 Ghz Ivy Bridge dual core chip, 3 generations behind current CPUs, that doesn’t even merit the i3 or i5 designation, and has no hyperthreading. Do bear that in mind as you keep reading.


**Meet The Scooter Computer**


This box may be small, and only 15 watt TDP, but it is mighty. I spun up a new Digital Ocean droplet and ran a quick benchmark:


```
sudo apt-get install sysbench
sysbench --test=cpu --cpu-max-prime=20000 run

```

kg-card-begin: html


| Tie Shuttle 6
total time:           28.0707s
total num events:     10000
total time take:      28.0629
per-request stats:
     min:             2.77ms
     avg:             2.81ms
     max:             3.99ms
     ~95 percentile:  3.00ms | Digital Ocean Droplet
total time:          35.9541s
total num events:    10000
total time taken:    35.9492
per-request stats:
     min:             3.50ms
     avg:             3.59ms
     max:             13.31ms
     ~95 percentile:  3.79ms |


kg-card-end: html

Results will of course vary by cloud provider, but rest assured this box is just as fast as and possibly even faster than the average cloud box you could spin up right now. Of course it is “only” 2 cores / 4 threads, but the more cores you need, the slower they tend to go because of the overall TDP limits of the core package.


One thing that’s not immediately obvious in photos is that this thing is indeed small but *hefty*, like holding a solid chunk of aluminum in your hand. That’s because the box is passively cooled – the whole case is the heatsink, as the CPU on the bottom of the motherboard mates with the finned top of the case.


![](https://blog.codinghorror.com/content/images/2016/02/tie-shuttle-top-case.jpg)


![](https://blog.codinghorror.com/content/images/2016/02/scooter-computer-internals.jpg)


Opening this box you realize just how simple things are inside it; it’s barely more than a highly integrated motherboard strapped to an aluminum block. This isn’t a Steve Jobs truck, a Mac Mini car, or even a motorcycle. **This is **[**a scooter**](https://blog.codinghorror.com/geek-transportation-systems/)**.**


> Scooters are very primitive machines; it is both their greatest strength and their greatest weakness. It’s arguably the simplest personal wheeled vehicle there is. In these short distance scenarios, scooters tend to win over, say, bicycles because there’s less setup and teardown necessary – you don’t have to lock up a scooter, nor do you have to wear a helmet. Just hop on and go! You get almost all the benefits of gravity and wheeled efficiency with a minimum of fuss and maintenance. And yes, it’s fun, too!


Passively cooled computers are paragons of simplicity and reliable consumer electronics, but passively cooling a “real” x86 PC is the holy grail. To get serious performance you usually need to feed the CPU at least 10 to 20 watts – and dissipating that kind of energy with zero fans and ambient airflow alone is not trivial. Let’s see how our scooter does overnight running [Mersenne Primes](http://www.mersenne.org/download/), which is the heaviest CPU load possible.


![](https://blog.codinghorror.com/content/images/2016/02/CZ30-0eWYAAZniT.jpg)


You can place your hand on the top of the box during this, but it’s uncomfortable. And the whole box radiates heat, not just the top. Overall it was completely stable for me during overnight mprime torture testing with the 15w TDP CPU I chose, and I am comfortable with these boxes sitting in our rack in the datacenter, even under extended full load. However, I would be *very* careful putting a 28w TDP CPU in this box unless you are absolutely sure it won’t be at full load very often. Passive cooling is hard.


Power consumption, as measured by my Kill-a-Watt, ranged from **7 watts** at the Ubuntu Server 14.04 text login screen, to 8-10 watts at an idle Ubuntu 15.10 GUI login screen (the default OS it arrived with), to 14-18 watts in memory testing, to **26 watts in mprime**.


I should also mention that even under extreme mprime load, both CPUs stayed at 2.5 Ghz indefinitely, which is unusual in my experience. To achieve 2.7 Ghz you need a single threaded load. Considering the base clock of the i5-5200u is 2.2 Ghz, that’s quite good! Many 4-6-8 core CPUs drop all the way down to their base clock pretty fast once they have significant load, which makes the “turbo” moniker a bit of a lie.


(By the way, don’t bother using burnP6, it generates way too little heat compared to mprime, which is an absolute *monster*. If your CPU can survive an overnight run of mprime, I can assure you it’s ready for just about anything the real world can throw at it, ever.)


**Disk**


The machine has M.2 slots for two drives, as well as a SATA port and power cable (not pictured, but was included in the box) if you want to mate a 2.5″ drive with the drive mounting holes on the bottom of the case. So if you prefer a mirrored two drive RAID array here for reliability, or a giant honking 2TB 2.5″ HDD slapped in there for media storage, all of that is possible!


Be careful, as the internal M.2 slots are **2242**, [meaning 42mm length](https://web.archive.org/web/20160327153212/http://rog.asus.com/313352014/labels/guides/buying-an-m-2-ssd-how-to-tell-which-is-which/). There seem to be mostly (only?) lower cost SSD drives available in this size for whatever reason.


![](https://blog.codinghorror.com/content/images/2016/02/m-2-length.jpg)


Don’t worry, though, the bundled 128GB [Phison S9](http://mydigitalssd.com/msata-ssd.php) M.2 SSD has [decent performance](http://www.servethehome.com/mydigitalssd-bp4-128gb-msata-benchmarks-review/), roughly equal to a good SSD from a few years ago:


```
dd bs=1M count=512 if=/dev/zero of=test conv=fdatasync
hdparm -Tt /dev/sda

536870912 bytes (537 MB) copied, 1.52775 s, 351 MB/s
Timing cached reads:   11434 MB in  2.00 seconds = 5720.61 MB/sec
Timing buffered disk reads:  760 MB in  3.00 seconds = 253.09 MB/sec

```


That’s respectable SSD performance and won’t hold you back in most use cases, but it’s not a barn-burning disk subsystem, either. If you want to upgrade, I recommend the [Samsung 850 EVO](http://www.amazon.com/dp/B00TGIVVKU/) which comes in the required form factor.


Of course the Samsung 850 Pro would fit fine as a traditional 2.5″ SATA drive mounted to the case cover, and would perform like this:


```
536870912 bytes (537 MB) copied, 1.20895 s, 444 MB/s
Timing cached reads:   38608 MB in  2.00 seconds = 19330.61 MB/sec
Timing buffered disk reads: 1584 MB in  3.00 seconds = 527.92 MB/sec

```


**RAM**


Intel limits these Broadwell U class CPUs to 16GB RAM total, so maxing the box out is only going to set you back around $70. Still, that’s a significant percentage of the ~$350 total cost, and you may not need that much RAM for what you have in mind.


However, do be careful that you get dual-channel RAM for lower RAM configurations; you don’t want a single 4GB DIMM, you want two 2GB DIMMs. They ship from the vendor with a single DIMM, so beware. It may not matter [depending on the task](http://www.anandtech.com/show/8672/lenovo-thinkstation-p300-workstation-review-haswell-plus-quadro/6), as noted by AnandTech, but our boxes will be used for OpenSSL, and memory is cheap, so why not?


**The Versatile Scooter**


When I began looking at this, I was shocked to discover just how low-end the x86 CPUs are in a lot of “dedicated” devices, such as the official [pfSense hardware](https://www.pfsense.org/products/):


![](https://blog.codinghorror.com/content/images/2016/02/pfsense-hardware-lineup.png)


Sure, 2.4 Ghz and 8 cores on that C2758 sounds reasonable – until you realize those are old Intel Bay Trail Atom cores. Even the *current* Cherry Trail Atom cores aren’t so hot. Furthermore, those are probably the maximum “turbo” frequencies being quoted, which are unlikely to be sustained under any kind of real multi-core load. Also, did I mention this is being sold as a $1,400 device? Except for the lack of more than 2 dedicated gigabit ethernet ports, I’d put our scooter computer up against that C2758 any day of the week. And you know what? It’d win.


I think this logic applies to a lot of dedicated hardware these days – routers, switches, firewalls, and so on. **You’re often better off building up a modern high power, low TDP x86 box and slapping a regular Linux distro on there.**


You can even kinda-sorta fit six of them in a 1U rack space.


![](https://blog.codinghorror.com/content/images/2016/02/shuttles-vs-1u.jpg)


(Well, except for the power bricks and cables. Vertical mounting on a 1U shelf works out a bit better, and each conveniently came with a stand for vertical operation.)


Now that I’ve worked with these boxes, I’ve become rather enamored of the Scooter Computer concept. Wherever we were thinking that we had to run either:

- A virtual machine on big iron for some small but important utility function in our rack.
- Dedicated, purpose built hardware for networking, firewall, or switching with a custom OS.


…we can now take advantage of cheap, reliable, flexible, totally solid state commodity x86 hardware that’s spread across many machines and running standard Linux distributions, like all the rest of our 1U servers.

[router](https://blog.codinghorror.com/tag/router/)
[vpn](https://blog.codinghorror.com/tag/vpn/)
[firmware](https://blog.codinghorror.com/tag/firmware/)
[security](https://blog.codinghorror.com/tag/security/)
[open source](https://blog.codinghorror.com/tag/open-source/)
