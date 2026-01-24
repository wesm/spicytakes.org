---
title: "Building a PC, Part VIII: Iterating"
date: 2015-09-17
url: https://blog.codinghorror.com/building-a-pc-part-viii-iterating/
slug: building-a-pc-part-viii-iterating
word_count: 747
---

The last time I seriously upgraded my PC was in 2011, because [the PC is over](https://blog.codinghorror.com/the-pc-is-over/). And in some ways, it truly is – they can slap a ton more CPU cores on a die, for sure, but the overall single core performance increase from a 2011 high end Intel CPU to today’s high end Intel CPU is… really quite modest, on the order of maybe 30% to 40%.


In that same timespan, mobile and tablet CPU performance has continued to just about double every year. Which means the forthcoming iPhone 6s will be [almost **10 times faster**](http://www.techtimes.com/articles/77083/20150818/alleged-iphone-6s-geekbench-3-results-show-2gb-ram-and-tri-core-1-5-ghz-cpu.htm) than the iPhone 4 was.


![](https://blog.codinghorror.com/content/images/2025/02/image-95.png)


Remember, that’s only single core CPU performance – I’m not even factoring in the move from single, to dual, to triple core as well as generally faster memory and storage. This stuff is old hat on desktop, where we’ve had mainstream dual cores for a decade now, but they are *huge* improvements for mobile.


When your mobile devices get 10 times faster in the span of four years, it’s hard to muster much enthusiasm for a modest 1.3 × or 1.4 × iterative improvement in your PC’s performance over the same time.


I’ve been slogging away at this for a while; my current PC build series spans 7 years:

- [Building a PC, Part VII: Rebooting](https://blog.codinghorror.com/building-a-pc-part-vii-rebooting/)
- [Building a PC, Part VI: Rebuilding](https://blog.codinghorror.com/building-a-pc-part-vi-rebuilding/)
- [Building a PC, Part V: Upgrading](https://blog.codinghorror.com/building-a-pc-part-v-upgrading/)
- [Building a PC, Part IV: Now It’s Your Turn](https://blog.codinghorror.com/building-a-pc-part-iv-now-its-your-turn/)
- [Building a PC, Part III: Overclocking](https://blog.codinghorror.com/building-a-pc-part-iii-overclocking/)
- [Building a PC, Part II: Burn in](https://blog.codinghorror.com/building-a-pc-part-ii/)
- [Building a PC, Part I: Minimal boot](https://blog.codinghorror.com/building-a-pc-part-i/)


The fun part of building a PC is that it’s relatively easy to swap out the guts when something compelling comes along. CPU performance improvements may be modest these days, but there are still bright spots where performance is increasing more dramatically. Mainly in graphics hardware and, in this case, **storage**.


The current latest-and-greatest Intel CPU is Skylake. Like Sandy Bridge in 2011, which brought us much faster 6 Gbps SSD-friendly drive connectors (although only two of them), the Skylake platform brings us another key storage improvement – the ability to connect hard drives directly to the PCI Express lanes. Which looks like this:


![](https://blog.codinghorror.com/content/images/2025/02/image-96.png)


…and performs like this:


![](https://blog.codinghorror.com/content/images/2025/02/image-97.png)


**Now *there’s* the 3× performance increase we’ve been itching for!** To be fair, a raw increase of 3× in drive performance doesn’t necessarily equate to a computer that boots in one third the time. But here’s why disk speed matters:


> If the CPU registers are how long it takes you to fetch data from your brain, then going to disk is the equivalent of [fetching data from Pluto](https://blog.codinghorror.com/the-infinite-space-between-words/).


What I’ve always loved about SSDs is that they attack the **PC’s worst-case performance scenario**, when information has to come off the slowest device inside your computer – the hard drive. SSDs massively reduced the variability of requests for data. Let’s compare L1 cache access time to minimum disk access time:


> Traditional hard drive
> 0.9 ns → 10 ms (variability of 11,111,111× )
> SSD
> 0.9 ns → 150 µs (variability of 166,667× )


SSDs provide a reduction in overall performance variability of 66×! And when comparing latency:


> [7200rpm HDD](https://web.archive.org/web/20151226192129/http://storagereview.com/toshiba_sata_hdd_enterprise_35_review_mg03acax00) – 1800ms
> [SATA SSD](http://storagereview.com/intel_ssd_dc_s3500_enterprise_review) – 4ms
> [PCIe SSD](http://storagereview.com/huawei_tecal_es3000_application_accelerator_review) – 0.34ms


Even going from a fast SATA SSD to a PCI Express SSD, you’re looking at a 10x reduction in drive latency.


Here’s what you need:

- [256GB Samsung 950 Pro NVMe M.2 drive](http://www.amazon.com/dp/B01639696U/?tag=codihorr-20) – $198
- [Asus Z170-A motherboard](http://www.amazon.com/dp/B012NH05UW/?tag=codihorr-20) – $165
- [Intel i5-i6600k Skylake CPU](http://www.amazon.com/dp/B012M8M7TY/?tag=codihorr-20) – $270
- [16GB DDR4 memory](http://www.amazon.com/dp/B00TPQPOIS/?tag=codihorr-20) – $134


These are the basics. It’s best to use the M.2 connection as a fast boot / system drive, so I scaled it back to the smaller 256 GB version. I also had a lot of trouble getting my hands on the faster i7-6700k CPU, which appears supply constrained and is currently overpriced as a result.


(Also, be careful, as some older M.2 drives can use the older **AHCI** connection type. Make sure yours is **NVMe**, as the [performance difference can be substantial](http://www.anandtech.com/show/7843/testing-sata-express-with-asus/4).)


Even though the days of doubling (or even 1.5×-ing) CPU performance are long gone for PCs, there are still some key iterative performance milestones to hit. Like [mainstream 4k displays](https://blog.codinghorror.com/our-brave-new-world-of-4k-displays/), I believe mainstream PCI express SSDs are another important step in the overall evolution of desktop computing. Or its corpse, anyway.

[hardware](https://blog.codinghorror.com/tag/hardware/)
[cpu performance](https://blog.codinghorror.com/tag/cpu-performance/)
[desktop](https://blog.codinghorror.com/tag/desktop/)
[mobile devices](https://blog.codinghorror.com/tag/mobile-devices/)
[technology trends](https://blog.codinghorror.com/tag/technology-trends/)
