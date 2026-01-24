---
title: "Building a PC, Part V: Upgrading"
date: 2008-04-17
url: https://blog.codinghorror.com/building-a-pc-part-v-upgrading/
slug: building-a-pc-part-v-upgrading
word_count: 1138
---

Last summer I posted a four part series on building your own PC:

- [Building a PC, Part I: Minimal boot](https://blog.codinghorror.com/building-a-pc-part-i/)
- [Building a PC, Part II: Burn in](https://blog.codinghorror.com/building-a-pc-part-ii/)
- [Building a PC, Part III: Overclocking](https://blog.codinghorror.com/building-a-pc-part-iii-overclocking/)
- [Building a PC, Part IV: Now It’s Your Turn](https://blog.codinghorror.com/building-a-pc-part-iv-now-its-your-turn/)


My personal system is basically identical to that build, though it predates it by [about six months](https://blog.codinghorror.com/my-giant-heatsink-fetish/). The only significant difference is the substitution of the Core 2 Duo E6600 CPU.

kg-card-begin: html

In my opinion, quad-core CPUs are still a [waste of electricity](https://blog.codinghorror.com/choosing-dual-or-quad-core/) unless you’re putting them in a server. Four cores on the desktop is great for bragging rights and mathematical superiority (yep, 4 > 2), but those four cores provide almost [no benchmarkable improvement](https://blog.codinghorror.com/quad-core-desktops-and-diminishing-returns/) in the type of applications most people use. Including software development tools. (Update: This paragraph was more controversial than intended. See [Should All Developers Have Manycore CPUs?](https://blog.codinghorror.com/should-all-developers-have-manycore-cpus/) for a clarification.)

kg-card-end: html

![](https://blog.codinghorror.com/content/images/2025/06/image-75.png)


My original advice stands: for the vast majority of users, the fastest possible dual-core CPU remains the best choice. I overclocked my E6600 CPU **from 2.4 Ghz to 3.2 Ghz**, instantly increasing the value of the processor by about 800 bucks.


Beyond overclocking, **the economy of building your own PC also lies in upgrading it in pieces and parts to keep it up to date**. Once you’ve taught yourself to build a PC, swapping parts out is easy. That’s an option you almost never have on laptops, and rarely on commercial desktops.


It’s been almost a year and a half since I made any significant change to my PC build. That’s an eternity in computer dog years. I was developing a serious itch to upgrade something – *anything* – on my PC. I did a bit of research, and I was surprised to find that the P965 chipset on my Asus P5B Deluxe motherboard supports the latest and greatest Intel CPUs. This is a pleasant surprise indeed; Intel and AMD change the pinouts and sockets of their CPUs quite regularly. A simple CPU upgrade, more often than not, forces a complete motherboard and memory upgrade. But not in this case!


So here’s what I did:

1. flash the BIOS* on my motherboard to the latest version, which supports the newest CPUs
2. remove the old and busted CPU (Core 2 Duo E6600, 2.4 GHz, 4 MB L2)
3. drop in the new hotness CPU (Core 2 Duo E8500, 3.16 GHz, 6 MB L2)
4. [Manually adjust](https://blog.codinghorror.com/building-and-overclocking-a-core-2-duo-system/) FSB speed, memory voltage and CPU voltage


This chip is an *outstanding* overclocker. It’s almost a no-brainer. The tubes are full of documented cases of this chip reaching 4.5 GHz and sometimes higher. I was fairly content with **my effortless 4 GHz overclock**:


![](https://blog.codinghorror.com/content/images/2025/04/image-74.png)


If you’re wondering why [CPU-Z](http://www.cpuid.com/cpuz.php) says this is a 2520 MHz CPU instead of the 4000 MHz you’d expect, that’s because the CPU is idle. All modern CPUs [clock down at idle](http://en.wikipedia.org/wiki/SpeedStep) to reduce power draw. If you run something CPU intensive, you’ll see the CPU speed dynamically change in CPU-Z, as illustrated by this animated GIF:


![CPU-Z SpeedStep animation](https://blog.codinghorror.com/content/images/uploads/2008/04/6a0120a85dcdae970b0120a86ddc03970b-pi.gif)


This power savings is achieved by dropping the CPU multiplier from its default of 9.5 down to 6.0. If we do a little math, it’s easy to infer the relationship between FSB (front side bus), CPU multiplier, and actual CPU speed:

kg-card-begin: html


| 315 MHz | 6.0x | 1890 MHz |
| 333 MHz | 9.5x | 3163 MHz |
| 420 MHz | 6.0x | 2520 MHz |
| 420 MHz | 9.5x | 3990 MHz |


kg-card-end: html

Overclocking the CPU is simple if you can stumble your way through a few basic BIOS screens. The default voltage on this E8500 is 1.128 volts. By juicing the CPU voltage up to 1.36 volts, and setting the front side bus (FSB) to 420 MHz, we can hit the magical 4 GHz number. All we need to do is a little unit testing burn-in torture testing, and we can confirm that it’s stable.


But you might wonder – does this overclocking stuff really justify the hassle? Is **going from 3.0 GHz to 4.0 GHz really *worth* it in terms of actual performance and not just bragging rights?**


I’m glad you asked!


I clocked my E8500 to 3.0 GHz / 315 FSB and 4.0 GHz / 420 FSB and ran a few quick [SunSpider JavaScript benchmarks](https://web.archive.org/web/20080419013331/http://webkit.org/perf/sunspider-0.9/sunspider.html). You may remember this great little benchmark from [The Great Browser JavaScript Showdown](https://blog.codinghorror.com/the-great-browser-javascript-showdown/). Here’s what I found:


![](https://blog.codinghorror.com/content/images/2025/04/image-73.png)


And the overall benchmark result in table form:

kg-card-begin: html


|  | 3 GHz | 4 GHz |  |
| Internet Explorer 7 SP1 | 15,824 ms | 12,748 ms | 19% faster |
| Firefox 3.0 Beta 5 | 3,018 ms | 2,450 ms | 19% faster |


kg-card-end: html

That’s **a consistent 19% performance improvement in an interpreted browser language for a 33% increase in raw CPU clock speed**. Not too shabby. It’s actually more than I expected. The real speed difference between an E6600 and E8500 would be (slightly) greater than the pure clock speed indicates, due to the architectural improvements and larger L2 cache in the E8500. There also might be other languages and apps that scale more linearly with that 33% CPU clock speed increase.


**Compare the result of going from 3 GHz to 4 GHz with adding another two cores**, which would produce exactly *zero* improvement in your JavaScript benchmarks. Most apps are barely multithreaded, much less capable of taking advantage of all four cores. Having four CPU cores won’t help you much when they’re all poking along at a leisurely 2 GHz.


So if you followed our original PC build plan, or if you’re planning to build your own PC – **don’t forget to factor upgrading into your system’s lifespan! **These builds are eminently upgradeable. Sometimes you’ll get lucky and have *knockout* upgrade options like the E8500: a 4 GHz (almost) guaranteed drop-in CPU replacement for under 300 bucks.


*I am simplifying a little because I don’t want to scare anyone. In the interests of full disclosure, here’s the story. The ASUS Windows x64 BIOS flash program crashed while updating the motherboard BIOS. I can’t quite describe the chill that went down my spine as I watched this happen. Any failure during a BIOS flash is irrevocable and permanent, the very definition of “bricking.” To be fair, this is literally the first time I’ve ever bricked *anything* in at least 10 years of regular yearly BIOS flashing. I had to buy another motherboard and initiate a RMA on my original, newly BIOS-free motherboard. Let this be a lesson to you, kids: don’t trust Windows software developers! Always update the BIOS from a boot CD or from within the BIOS itself using a USB key!

[hardware](https://blog.codinghorror.com/tag/hardware/)
[personal computer](https://blog.codinghorror.com/tag/personal-computer/)
[cpu](https://blog.codinghorror.com/tag/cpu/)
[overclocking](https://blog.codinghorror.com/tag/overclocking/)
[software development](https://blog.codinghorror.com/tag/software-development/)
