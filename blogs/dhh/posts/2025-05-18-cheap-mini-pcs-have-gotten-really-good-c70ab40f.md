---
title: "Cheap mini PCs have gotten really good"
date: 2025-05-18
url: https://world.hey.com/dhh/cheap-mini-pcs-have-gotten-really-good-c70ab40f
slug: cheap-mini-pcs-have-gotten-really-good-c70ab40f
word_count: 929
---

For the past week, I've been working off the
[Minisforum UM870](https://www.minisforum.com/products/minisforum-um680-um760-um870-slim?variant=49516307939634)
. A tiny mini PC with an 8-core/16-thread AMD 8745H CPU, which retails for
[$343](https://www.amazon.com/MINISFORUM-Barebone-Computer-5-0GHz-Support/dp/B0DL5ZRQV3/)
(or
[€379](https://minisforumpc.eu/products/um680-760-870-slim-mini-pc?variant=51700059144558)
) as a bare-bone unit, and stays below $550, even after adding
[48GB of RAM](https://www.amazon.com/Crucial-5600MT-5200MT-4800MT-CT48G56C46S5/dp/B0C79LKJK4/)
and
[1TB of storage](https://www.amazon.com/WD_BLACK-SN850X-Internal-Gaming-Solid/dp/B0B7CKVCCV/)
. I'm shocked to report that I really don't need more than this!
I mean, I knew that Apple's Mac Mini, which is equally petite to the Minisforum, had plenty of power for macOS. But somehow I thought Apple had some special sauce that made this possible, and that PCs were forever condemned to be bigger, louder, and slower. How 2020 of me.
The UM870 is a little beast. It runs our full HEY test suite in just 2m28s. In comparison, it takes a 14-core M4 Pro 2m49s, and such
[an Apple costs $2,199](https://www.apple.com/shop/buy-mac/mac-mini/apple-m4-pro-chip-with-12-core-cpu-16-core-gpu-24gb-memory-512gb)
, once you've given it 48GB of RAM and 1TB of storage.
Now, that M4 Mac Mini can probably do things with, say, 8K video editing that the UM870 can't touch. But on the other hand, the UM870 can
[play the latest video games](https://www.youtube.com/watch?v=xKD2mU6shdo&t=269s)
. Everything from Fortnite to Cyberpunk 2077 to Forza Horizon. It won't trouble a modern, dedicated Nvidia card for max FPS, but it's perfectly playable at 1080p at medium settings in a ton of games.
In raw CPU power, the AMD 8745H will match a regular M4 in multi-core. They both clock in right around 13,000 points on Geekbench 6. Though the M4 is a fair bit quicker in single-core. The AMD is also far behind an M4 Pro in raw multi-core power (13K vs 22K), but at less than a quarter the cost, it's hard to complain.
But as with the example of video games, it's often deceiving just to compare the Geekbench numbers, because it all depends on what you're doing. If you're really into video games, it's no use to have extra grunt, if your favorite games won't run. The same is true if you're a developer working with Docker containers and a Linux toolchain. As quoted above, the UM870 handily defeats the M4 Pro in our all-cores-buzzing HEY test suite.
That's partly because we run databases and accessories, like MySQL, Redis, and ElasticSearch, in Docker containers. Even though we run the Ruby code natively on both platforms, the Docker dependencies put the Mac further behind than it otherwise would have been, because Linux runs Docker natively, and the Mac has to deal with the file-system tax and other drawbacks.
The irony is that it was partly Apple's volume with and investment in TSMC that got us these incredible AMD chips, as they're riding the same improvements in TSMC manufacturing prowess as Apple's M chips. The Zen 4 cores in the 8745H are all forged on the same 5nm process as the M2, so it's no surprise that the AMD cores are dead-on-the-money for Apple's in Geekbench single-core performance.
And Zen 4 is even the last generation! The insane new (and insanely named) AMD Ryzen AI Max 395+ chip that's used in the upcoming
[Framework Desktop](https://frame.work/desktop)
runs on Zen 5 cores. And with 16 of those, the 395+ is faster in Geekbench multi-core than an M4 Pro, and only ever so slightly behind the M4 Max. On my HEY test suite, it completes the run in an insane 1m21s — more than twice as fast as the 14-core M4 Pro!
But I digress. The 395+ chip isn't cheap, even if it's still a great deal. The Framework Desktop with 64GB/1TB, which is twice as fast as the M4 Pro with our HEY tests, is $1,744. That's still less than the $2,199 Mac Mini, which only has 48GB of RAM. But obviously way more than a $550 Minisforum! And while it's quite small, it's not tiny, like the UM870.
Regardless, this is what I love about technology. I love when our assumptions are tested: just how small and cheap can an awesome developer machine become? I love that open-source Linux is able to run laps around Apple in the workloads that many developers need (like working with Docker containers). I love that this tiny little silent $550 mini PC on my desk is capable of putting out computing power that only a decade ago would have been reserved to loud, honking metal in a data center.
Mini PCs have gotten really good.
[AMD is on a roll](https://world.hey.com/dhh/amd-in-everything-0ec0cc6e)
.
[Linux is a blast](https://world.hey.com/dhh/the-year-on-linux-7f30279e)
. These are my conclusions. Check out the
[Minisforum UM870](https://store.minisforum.com/products/minisforum-um760-slim?variant=46040999624949)
or the
[Beelink SER8](https://www.bee-link.com/products/beelink-ser8-8745hs)
. Anything with an AMD 7745H and up to an 8945HS should be a great deal. If you want to splurge (yet still get a bargain compared to the macs), you could have a look at the new HX370 in the
[Beelink SER9](https://www.bee-link.com/products/beelink-ser9-ai-9-hx-370)
or
[Minisforum X1](https://store.minisforum.com/products/minisforum-ai-x1?variant=46484114014453)
, but I'd save my money, buy a
[Lofree Flow84](https://www.lofree.co/products/lofree-flow-the-smoothest-mechanical-keyboard)
keyboard to go with the new mini rig, and put the rest of the money towards a
[KEF LSX II savings fund](https://world.hey.com/dhh/what-is-hifi-dddab2ae)
!
*Update: The MediaTek Wifi + Bluetooth card used in the UM870 isn't compatible with Ubuntu out of the box. I run everything hardwired for performance, so didn't notice during my testing, but a reader caught it, and I confirmed it. 

If you need wireless out-of-the-box on Ubuntu, I found that the card in the Beelink SER9 works great with both. If you already have a UM870 or still want one, and you need wireless, you could buy the AMD RZ616 Wi-Fi 6E card*
[from Framework](https://frame.work/products/amd-rz616-wi-fi-6e?v=FRANRFFX01)
*or*
[Amazon](https://www.amazon.com/OKN-AX210NGW-Bluetooth-Wireless-Ultra-Low/dp/B08MJLPZPL/)
*for around $20 — that works and slots right in.*
