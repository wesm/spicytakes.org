---
title: "Understanding The Hardware"
date: 2008-07-26
url: https://blog.codinghorror.com/understanding-the-hardware/
slug: understanding-the-hardware
word_count: 1914
---

I got a call from [Rob Conery](https://web.archive.org/web/20080907085300/http://blog.wekeroad.com/) today asking for advice on building his own computer. Rob works for Microsoft, but lives in Hawaii. I’m not sure how he managed that, but being so far from the mothership apparently means he has the flexibility to spec his own PC. Being stuck in Hawaii is, I’m sure, [a total bummer, dude](http://flickr.com/search/?q=hawaii).


Rob and I may disagree on [pretty much everything](https://web.archive.org/web/20080908080443/http://blog.wekeroad.com/2007/10/30/in-which-we-discuss-proprietary-object-noise/) from a coding perspective, but we can agree on one thing: [we love computers](https://blog.codinghorror.com/if-loving-computers-is-wrong-i-dont-want-to-be-right/). And what better way to celebrate that love by building your own? It’s not hard. This industry was [built on](https://blog.codinghorror.com/web-2-0-and-the-whatever-box-server/) the [commodification of hardware](https://blog.codinghorror.com/building-a-computer-the-google-way/). If you can snap together a Lego kit, [you can build a computer](https://blog.codinghorror.com/building-a-pc-part-i/).


Maybe this is a minority opinion, but I find understanding the hardware to be instructive for programmers. Peter Norvig – now director of research at Google – [appears to concur](http://www.norvig.com/21-days.html).


> **Understand how the hardware affects what you do.** Know how long it takes your computer to execute an instruction, fetch a word from memory (with and without a cache miss), transfer data over ethernet (or the internet), read consecutive words from disk, and seek to a new location on disk.


In my book, one of the best ways to understand the hardware is to get your hands dirty and put one together, including installing the OS, yourself. It’s a shame Apple programmers can’t do this, as their hardware has to be blessed by [the Cupertino DRM gods](https://blog.codinghorror.com/why-doesnt-anyone-give-a-crap-about-freedom-zero/). Or, you could [build a frankenmac](http://www.macworld.com/article/133028/2008/04/building_mac_clone.html), though you’ll run the risk of running a “patched” OS X indefinitely.


As Rob and I were talking about the philosophy of building your own development PC – something I also [discussed on a Hanselminutes podcast](http://www.hanselman.com/blog/HanselminutesPodcast69BuildingADeveloperPC.aspx) – he said *you know, you should blog this*. But Rob – I already have, many times over! Let’s walk down the core list of components I recommended for Rob, and I’ll explain my choices with links to the relevant blog posts I’ve made on that particular topic.


**ASUS P5E Intel X38 motherboard** ($225)


I’m a [big triple monitor guy](https://blog.codinghorror.com/joining-the-prestigious-three-monitor-club/), so I insist on motherboards that are **capable of accepting two video cards** – in other words, they have two x8 or x16 PCI Express card slots suitable for video cards. I also [demand quiet from my PC](https://blog.codinghorror.com/building-a-quiet-pc/), which means a motherboard with all passive cooling. Beyond that, I don’t like to pay a lot for a fancy motherboard. After spending the last five years with motherboards packing scads of features I *never* end up using (two ethernet ports, anyone?), I’ve realized there are better ways to invest your money. People tend to respect ASUS as one of the largest and most established Taiwanese OEMs, so it’s usually a safe choice. I’d go as far down on price on the motherboard as you can without losing whatever essential features you truly need. Save that money for the other parts.


**Intel Core 2 Duo E8500 3.16 GHz CPU** ($190)
**Intel Core 2 Quad Q9300 2.5 GHz CPU** ($270)


Ah, the eternal debate: [dual versus quad](https://blog.codinghorror.com/choosing-dual-or-quad-core/). Despite what Intel’s marketing weasels might want you to believe, **clock speed still matters very much**. Here’s an example: SQL Server 2005 queries on my local box, a 3.5 GHz dual core, execute **more than twice as fast** as on our server, a 1.8 GHz eight core machine. Sadly, very few development environments parallelize well, with the [notable exception of C++ compilers](https://blog.codinghorror.com/should-all-developers-have-manycore-cpus/). Outside of a few niche activities, such as video encoding and professional 3D rendering, most computing tasks don’t scale worth a damn beyond two cores. Yes, it’s exciting to see those four graphs in Task Manager (and even I get a little giddy when [I see sixty-four of ’em](https://web.archive.org/web/20080727061102/http://blogs.technet.com/markrussinovich/archive/2008/07/21/3092070.aspx)), but take a look at the [cold, hard benchmark data](https://blog.codinghorror.com/quad-core-desktops-and-diminishing-returns/) and the contents of your wallet *before* letting that seductive 4 > 2 math hijack the rational parts of your brain.


It’s also smart to **buy a little below the maximum**, with the ultimate goal of upgrading to a whizzy-bang 4 GHz quad core CPU sometime in the future. One of the hidden value propositions in building your own PC is the ability to easily [upgrade it later](https://blog.codinghorror.com/building-a-pc-part-v-upgrading/). CPU is one of the most obvious upgrade points where you want to intentionally underbuy a little. Give yourself some room for future upgrades. Until a quad costs the same as a dual at the same clock speed, my vote still goes to the fastest dual core you can afford.


**Kingston 4GB (2 x 2GB) DDR2 800 x 2** ($156)


Memory is awesomely cheap. When it comes to memory, I like to buy a few notches above the cheapest stuff, and Kingston has been a consistently reliable brand for me at that pricing level. There’s no reason to bother with anything under 8 GB these days. **Don’t get hung up on memory speed**, though. Quantity is more important than a few extra ticks of speed. But don’t take my word for it. As an experiment, Digit-Life cut the [speed of memory in half](https://web.archive.org/web/20080729170203/http://www.digit-life.com/articles3/cpu/amd-phenom-x4-9850-ddr2-533-p2.html), with a resulting **overall average performance loss of merely *three percent***. By the time your system has to reach outside of the L1, L2, and possibly even L3 cache – it’s already so slow from the system’s perspective as to be academic. Memory that is a few extra nanoseconds faster isn’t going to make any difference. This is also why I specified the latest and greatest Intel CPUs with larger 6 MB L2 caches. Remember, kids, Caching Is Fundamental!


**Western Digital VelociRaptor 300 GB 10,000 RPM Hard Drive** ($290)


This is arguably the only indulgence on the list. The Velociraptor is an incredibly expensive drive, but it’s also **a rocket of a hard drive**. I’m a big believer in the importance of disk speed to overall system performance, *particularly* for software developers. At least [Scott Guthrie backs me up](http://weblogs.asp.net/scottgu/archive/2007/11/01/tip-trick-hard-drive-speed-and-visual-studio-performance.aspx) on this one. Trust me, [you want a 10,000 RPM boot drive](https://blog.codinghorror.com/you-want-a-10000-rpm-boot-drive/). Buy a slower large drive for your archiving needs. You want two drives, anyway; having two spindles will give you a lot of flexibility and also [help your virtual machine performance](https://blog.codinghorror.com/the-single-most-important-virtual-machine-performance-tip/) immensely.


This new raptor model is the best of the series. It’s much quieter, uses less power, generates less heat, and is by far the fastest – *embarrassingly* fast. It’s expensive, yes. I won’t hold it against you if you decide to disregard this advice and go with a respectably fast, less expensive hard drive. But to me, it’s all about putting the money where the most significant bottlenecks are, and considered in that light –man, this thing is *so* worth it. As [Storage Review said](https://web.archive.org/web/20080728132458/http://www.storagereview.com/WD3000BLFS.sr?page=0%2C7), “[its] single-user scores... blow away those of every other [hdd].”


**Radeon HD 4850 512MB video card** ($155 after rebate)


Even if you’re not a gamer, it’s hard to ignore the charms of this amazing [powerhouse of a video card](https://web.archive.org/web/20081010180834/http://techreport.com/articles.x/14967). The brand new ATI 4850 delivers performance on par with the very fastest $500+ video card you can buy for **a measly hundred and fifty bucks!** Modern operating systems require video grunt, either for windowing effects or high-definition video playback. Beyond that, it’s looking more and more like some highly parallizable tasks may move to the GPU. Have you ever [read stuff](http://www.tomshardware.com/reviews/nvidia-cuda-gpu,1954-12.html) like “*even the slowest GPU implementation was nearly 6 times faster than the best-performing CPU version”*? Get used to reading statements like that; I expect you’ll be reading a lot more of them in the future as general purpose APIs for GPU programmability become mainstream. That’s another reason, as a programmer and not necessarily a gamer, you still want a modern video card. For all this talk of coming 8 and 16 core CPUs, eventually the GPU could be [the death of the general purpose CPU](https://blog.codinghorror.com/folding-the-death-of-the-general-purpose-cpu/).


We also want our video card to be efficient. Many don’t realize this, but your video card can consume as much power [as your CPU](https://blog.codinghorror.com/video-card-power-consumption/). Sometimes even more! The 4850, for all its muscle, is remarkably efficient as well. According to [a recent AnandTech roundup](http://www.anandtech.com/video/showdoc.aspx?i=3340&p=2), it’s on par with the most efficient cards of this generation. Pay attention to [your idle power consumption](https://blog.codinghorror.com/why-estimate-when-you-can-measure/), because power consumed means heat produced, which in turn means additional noise and possible instability.


**Corsair 520HX 520W Power Supply** ($100 after rebate)


The power supply is probably one of the most underrated and misunderstood components of a modern PC. First, because people tend to focus on the “watts” number when the really [important number is actually *efficiency*](https://blog.codinghorror.com/upgrading-to-a-high-efficiency-power-supply/) – a certain percentage of energy that goes into every power supply is turned into waste heat. **An efficient power supply will run cooler and more reliably because it uses higher quality parts.** People think you need [1.21 Jigawatts](http://www.imdb.com/title/tt0088763/quotes) to run a powerful desktop system, but that’s [just not true](https://blog.codinghorror.com/why-estimate-when-you-can-measure/). Unless you have a bleeding-edge CPU paired with *two* high-end top of the line gaming class video cards, trust me – even 500 watts is overkill.


The Corsair model I recommend gets [stellar reviews](https://web.archive.org/web/20080908080403/http://www.silentpcreview.com/article692-page1.html). It has modular cables and the 80 plus designation, so it’s 80% efficient at all input voltages. Note that a quality power supply is not a substitute for a [quality UPS or surge protector](https://blog.codinghorror.com/power-surge-protection-pcs-and-you/), but it helps.


**Scythe “Ninja” SCNJ-2000 cooler** ($50)
**Scythe “Ninja Mini” SCMNJ-1000 cooler** ($35)


I’ll be honest with you. I have a [giant heatsink fetish](https://blog.codinghorror.com/my-giant-heatsink-fetish/). These giant hunks of aluminum and copper, and the liquid-filled heatpipes that drive them, fascinate me. But there’s a more practical reason, as well: if you want a quiet computer, you don’t even bother with the stock coolers that are bundled with the CPU. Over the last few years, I keep coming back to Scythe’s classic “Ninja” tower cooler, which is available in tall and short varieties. They’re so **astoundingly efficient** that, with adequate case ventilation, they can be run fanless. I even (barely) managed to squeeze the Ninja Mini into [my home theater PC build](https://blog.codinghorror.com/building-your-own-home-theater-pc/), and it’s now mercifully fanless as well. There are plenty of other great tower/heatpipe coolers on the market, but the Ninja is still one of the best, a testament to its pioneering design. The CPU is (usually) the biggest consumer of power in your PC, so it’s sensible to invest in a highly efficient aftermarket cooler to keep noise and heat at bay under load.


There you have it. More than you ever possibly wanted to know about how an obsessive geek builds a PC – painstakingly analyzing every single part that goes into it. Now, like Rob, you’re probably sorry you asked; **who needs all the philosophical digressions, just give us the damn parts list!** OK, here it is:

- ASUS P5E Intel X38 motherboard ($225)
- Intel Core 2 Duo E8500 3.16 GHz CPU ($190) or Intel Core 2 Quad Q9300 2.5 GHz CPU ($270)
- Kingston 4GB (2 x 2GB) DDR2 800 x 2 ($156)
- Western Digital VelociRaptor 300 GB 10,000 RPM Hard Drive ($290)
- Radeon HD 4850 512MB video card ($155 after rebate)
- Corsair 520HX 520W Power Supply ($100 after rebate)
- Scythe “Ninja” SCNJ-2000 cooler ($50) or Scythe “Ninja Mini” SCMNJ-1000 cooler ($35)


The **best bang for the buck developer x86 box I can come up with**, all for around $1100.


I try to avoid posting about hardware *too* much, but sometimes I can’t help myself. I blame Rob. Enjoy your new system, Mr. Conery.

[hardware](https://blog.codinghorror.com/tag/hardware/)
[computer hardware](https://blog.codinghorror.com/tag/computer-hardware/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[computer building](https://blog.codinghorror.com/tag/computer-building/)
[hardware understanding](https://blog.codinghorror.com/tag/hardware-understanding/)
