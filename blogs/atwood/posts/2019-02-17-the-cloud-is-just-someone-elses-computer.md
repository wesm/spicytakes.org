---
title: "The Cloud Is Just Someone Else’s Computer"
date: 2019-02-17
url: https://blog.codinghorror.com/the-cloud-is-just-someone-elses-computer/
slug: the-cloud-is-just-someone-elses-computer
word_count: 1316
---

When we started [Discourse](https://discourse.org/) in 2013, our server requirements were high:

- 1GB RAM
- modern, fast dual core CPU
- speedy solid state drive with 20+ GB


I’m not talking about a cheapo shared cpanel server, either, I mean a *dedicated* virtual private server with those specifications.


We were OK with that, because we were [building in Ruby](https://blog.codinghorror.com/why-ruby/) for the next decade of the Internet. I predicted early on that the cost of renting a suitable VPS would drop to $5 per month, and courtesy of Digital Ocean that indeed happened in January 2018.


[The cloud got cheaper](https://meta.discourse.org/t/new-digital-ocean-pricing-spoiler-5-for-a-1gb-droplet/78230), and faster. Not really a surprise, since the [price of hardware trends to zero](https://blog.codinghorror.com/when-hardware-is-free-power-is-expensive/) over time. But it’s still the cloud, and that means it isn’t exactly *cheap*. It is, after all, someone else’s computer that you pay for the privilege of renting.


![there-is-no-cloud](https://blog.codinghorror.com/content/images/2019/02/there-is-no-cloud.png)


But wait… **what if you could put your *own* computer “in the cloud”?**


Wouldn’t that be the best of both worlds? Reliable connectivity, plus a nice low monthly price for extremely fast hardware? If this sounds crazy, it shouldn’t – Mac users have been [doing this for years](https://www.macstadium.com/pricing/colo) now.


![mac-colocation-2019-1](https://blog.codinghorror.com/content/images/2019/02/mac-colocation-2019-1.png)


I suppose it’s understandable that Mac users would be on the cutting edge here since [Apple barely makes server hardware](https://en.wikipedia.org/wiki/Xserve#Intel_Xserve), whereas the PC world has always been the literal de-facto [standard for server hardware](https://blog.codinghorror.com/building-a-computer-the-google-way/).


![mac-stadium-colocation](https://blog.codinghorror.com/content/images/2019/02/mac-stadium-colocation.jpg)


Given the prevalence and maturity of cloud providers, it’s even a *little* controversial these days to [colocate actual servers](https://blog.codinghorror.com/building-servers-for-fun-and-prof-ok-maybe-just-for-fun/). We’ve also experimented with colocating mini-pcs in various hosting roles. I’m still curious why there isn’t more of a cottage industry for colocating mini PCs. Because… *I think there should be*.


I originally wrote about [the scooter computers](https://blog.codinghorror.com/the-scooter-computer/) we added to our Discourse infrastructure in 2016, plus my own colocation experiment that ran concurrently. **Over the last three years of both experiments, I’ve concluded that these little boxes are plenty reliable**, with one role specific caveat that I’ll explain in the comments. I remain an unabashed fan of mini-PC colocation. I like it so much I put together a new 2019 iteration:

kg-card-begin: html


| **2017 — $670** | **2019 — $820** |
| [i7-7500u](https://ark.intel.com/products/95451/Intel-Core-i7-7500U-Processor-4M-Cache-up-to-3_50-GHz-)
2.7-3.5 Ghz, 2c / 4t | [i7-8750h](https://ark.intel.com/products/134906/Intel-Core-i7-8750H-Processor-9M-Cache-up-to-4-10-GHz-)
2.2-4.1 Ghz, 6c / 12t |
| 16GB DDR3 RAM | 32GB DDR4 RAM |
| 500GB SATA SSD | 500GB NVMe SSD |


kg-card-end: html

This year’s scooter computer offers **3× the cores, 2× the memory, and 3× faster drive**. It is, as the kids say… an *absolute unit*. 😱


![2019-scooter-computer-top-interior-1](https://blog.codinghorror.com/content/images/2019/02/2019-scooter-computer-top-interior-1.jpeg)


![2019-scooter-computer-bottom-interior](https://blog.codinghorror.com/content/images/2019/02/2019-scooter-computer-bottom-interior.jpeg)


![2019-scooter-computer-front-and-back](https://blog.codinghorror.com/content/images/2019/02/2019-scooter-computer-front-and-back.jpg)


It also has a rather elegant dual-sided internal layout. There is a slot for an old-school 2.5″ drive, plus built in wi-fi, but you won’t see it in my pictures because I physically removed both.


I vetted each box via my recommended [burn in and stability testing](https://blog.codinghorror.com/is-your-computer-stable/) and they all passed with flying colors, though I did have to RMA one set of dodgy RAM sticks in the process. The benchmarks tell the story, as compared to the average Digital Ocean droplet:


**Per-core performance**
`sysbench cpu --cpu-max-prime=20000 run`

kg-card-begin: html


| DO Droplet | 2,988 |
| 2017 Mini-PC | 4,800 |
| 2019 Mini-PC | 5,671 |


kg-card-end: html

**Multi-core performance**
`sysbench cpu --cpu-max-prime=40000 --num-threads=8 run`

kg-card-begin: html


| DO Droplet | 2,200 |
| 2017 Mini-PC | 5,588 |
| 2019 Mini-PC | 14,604 |


kg-card-end: html

**Disk performance**
`dd bs=1M count=512 if=/dev/zero of=test conv=fdatasynchdparm -Tt /dev/sda`

kg-card-begin: html


| DO Droplet | 701 / 8818 / 471 MB/sec |
| 2017 Mini-PC | 444 / 12564 / 505 MB/sec |
| 2019 Mini-PC | 1200 / 17919 / 3115 MB/sec |


kg-card-end: html

**Discourse rebuild**
`time ./launcher rebuild app`

kg-card-begin: html


| DO Droplet | 6:59 |
| 2017 Mini-PC | 3:41 |
| 2019 Mini-PC | 3:24 |


kg-card-end: html

Power consumption could be a concern, as the 2017 version had a much lower 15 watt TDP, compared to the 45 watts of this version. That 3× increase in core count ain’t free! So I tested that, too, with a combination of `i7z`, `stress`, and my handy dandy [watt meter](https://blog.codinghorror.com/why-estimate-when-you-can-measure/).


![2019-mini-pc-i7z-testing](https://blog.codinghorror.com/content/images/2019/02/2019-mini-pc-i7z-testing.png)

kg-card-begin: html


| (idle login) | 800 Mhz | 10w |
| `stress --cpu 1` | 4.1 GHz | 30w |
| `stress --cpu 2` | 4.1 GHz | 42w |
| `stress --cpu 3` | 4.0 GHz | 53w |
| `stress --cpu 4` | 3.9 GHz | 65w |
| `stress --cpu 5` | 3.7 GHz | 65w |
| `stress --cpu 6` | 3.5 GHz | 65w |
| `stress --cpu 12` | 3.3 Ghz | 65w |


kg-card-end: html

I’d expect around 10 - 20 watts doing typical low-load stuff that isn’t super CPU intensive. Note that running current-ish versions of `mprime` jacks power consumption up to 75w 🔥 and the overall clock scales down to 3.1 Ghz… let me tell you, I’ve learned to be very, *very* [afraid of AVX2 extensions](https://blog.cloudflare.com/on-the-dangers-of-intels-frequency-scaling/).


(If you’re worried about noise, don’t be. This active cooling solution is clearly overkill for a 65w load, because it barely spun up at all even under full core load. It was *extremely* quiet.)


So we’re happy that this machine is a slammin’ deal for $820, it’s super fast, and plenty reliable. But how about colocation costs? My colocation provider is EndOffice out of Boston, and they offer very competitive rates to colocate a Mini-PC: $29/month.


I personally colocate three Mini-PCs for redundancy and just-in-case; there are discounts for colocating more than one. Here they are racked up and in action. Of course I labelled the front and rear before shipping because that’s how I roll.


![endoffice-colocated-2019-mini-pcs](https://blog.codinghorror.com/content/images/2019/02/endoffice-colocated-2019-mini-pcs.jpg)


Let’s break this down and see what the actual costs of colocating a Mini-PC are versus the cloud. Given the plateauing of CPU speeds, I think five years of useful life for these boxes is realistic, but let’s assume a conservative three year lifespan to be safe.

- $880 mini-pc 32GB RAM, 6 CPUs, 500GB SSD
- $120 taxes / shipping / misc
- $29 × 12 × 3 = $1,044


That’s **$2,044 for three years of hosting**. How can we do on Digital Ocean? Per [their current pricing page](https://www.digitalocean.com/pricing/):

- 32GB RAM, 8 vCPUs, 640GB SSD
- $160/month
- $160 × 12 × 3 = **$5,760**


This isn’t *quite* apples to apples, as we are getting an extra 140GB of disk and 2 bonus CPUs, but those CPUs are both slower and partially consumed by multi-tenancy compared to our brand new dedicated, isolated CPUs. (I was curious about this, so I just spun up a new $160/month DO instance for a quick test. The `sysbench` results are 4086 and 11760 respectively, considerably below the 2019 Mini-PC results, above.) As you can see, **you pay almost three times as much for a cloud server.** 🤑


I’m not saying this is for everyone. If you just need to spin up a quick server or two for testing and experimentation, there’s absolutely no way you need to go to the trouble and up-front cost of building and then racking colocated mini-pcs. There’s no denying that spinning servers up in the cloud offers unparalleled flexibility and redundancy. But if you do have need for **dedicated computing resources over a period of years**, then building your own small personal cloud, with machines *you actually own*, is not only one third the cost but also… kinda cool?


![your-own-personal-cloud](https://blog.codinghorror.com/content/images/2019/02/your-own-personal-cloud.jpg)


If you’d also like to embark upon this project, you can get the same Partaker B18 box I did for [$490 from Amazon](https://www.amazon.com/Partaker-Coffee-Graphics-Barebone-System/dp/B07L4KJXWL), or $460 direct from China via AliExpress. Add memory and drive to taste, build it up, then check out [endoffice.com](https://endoffice.com/) who I can enthusiastically recommend for colocation, or the colocation provider of your choice.


Get something cool hosted out there; let’s do our part to keep the internet [fun and weird](https://jarredsumner.com/codeblog/)!

[cloud computing](https://blog.codinghorror.com/tag/cloud-computing/)
[virtual private server](https://blog.codinghorror.com/tag/virtual-private-server/)
[server specifications](https://blog.codinghorror.com/tag/server-specifications/)
[discourse](https://blog.codinghorror.com/tag/discourse/)
