---
title: "Hardware is fun again"
date: 2023-01-26
url: https://world.hey.com/dhh/hardware-is-fun-again-b819d0b4
slug: hardware-is-fun-again-b819d0b4
word_count: 505
---

I lost interest in computer hardware during the 2010s. It seemed years would pass with only meager, marginal improvements. Intel was stuck in a rut, so CPUs were barely improving. The only bright spot for me was Apple's progress with their A-series chips for phones. But that felt like a segregated reality from that of regular computers. Not any more!
Now computer hardware is happening again! Ever since Apple's M1 premiered, it seems the floodgates to interesting and large improvements have opened up. Not just in Apple land, but with AMD and Intel too. The generational jumps are happening more frequently, and the gains aren't measly any longer. The core count is shooting up, the individual cores are leaping 20-30% forward regularly. That kind of progress accumulates quickly.
While it's fun to geek out on the tech itself, I'm even more interested in what these new leaps enable. Like there was a time during the 2010s when we had to create specialized versions of Basecamp's web app for mobile, because phones were too slow to run JavaScript quickly. Now most iPhones are faster than most computers, and even chips for Android are catching up. So all that complexity of maintaining separate builds has long since washed away.
Something similar is happening now with SSD/NVMe storage. The generational jumps there have been even larger than in CPU land. We've rapidly gone from speeds around ~500MB/sec with Gen 2 drives to ~2.5GB/sec with Gen 3 to ~5GB/sec with Gen 4 and now Gen 5 is promising us a ridiculous ~13GB/sec shortly! That's the kind of order-of-magnitude leap forward that requires you to rethink your assumptions.
We're exploring moving both caching and job queuing at Basecamp to NVMe instead of RAM. The latency is now close enough that the advantages of abundant, fast NVMe storage wins. We just bought some 12TB NVMe Gen 4 cards for $2,390. 12TB! Using the new
[E1/E3 NVMe form factor](https://www.servethehome.com/e1-and-e3-edsff-to-take-over-from-m-2-and-2-5-in-ssds-kioxia/)
, we're now looking at the possibility of a petabyte's worth of NVMe storage in a single rack server for around $200K. That's bananas!
There's a whole generation of app developers who've only ever known the cloud, which separates them from appreciating the direct advances in hardware considerably. As more companies start
[redoing the math on cloud](https://dev.37signals.com/our-cloud-spend-in-2022/)
, and
[pulling their applications off the rental racket](https://world.hey.com/dhh/why-we-re-leaving-the-cloud-654b47e0)
, I think we'll see a resurgence of developers caring about the metal again.
As one example, I loved
[this back-of-the-envelope validation](https://thume.ca/2023/01/02/one-machine-twitter/)
of a thesis that Twitter could conceivably run a single server. You might not actually want to do that, but the math is fascinating. And I think it does posit the idea that eventually we'll easily be able to do just that. Run all our fancy services, with millions of users, on a single machine (or three, for redundancy).
Can't wait to get my hands on some AMD Zen4 machines with Gen 5 NVMe. A potential 384 vCPUs running off 13GB/sec storage in a single dual-CPU rack server. Sign me up for this near future!
