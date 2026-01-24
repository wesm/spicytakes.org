---
title: "Building Your Own Home Theater PC"
date: 2008-04-25
url: https://blog.codinghorror.com/building-your-own-home-theater-pc/
slug: building-your-own-home-theater-pc
word_count: 1367
---

I’ve kept a PC in my living room for the past three years as my [primary home theater interface](https://blog.codinghorror.com/windows-vista-media-center/), and I heartily recommend it. It’s shocking **how cheap and easy it is to build a home theater PC these days**.


I’ve been pondering an upgrade to my [creaky old home theater PC](https://blog.codinghorror.com/pentium-m-home-theater-pc/), and rave reviews of the new integrated AMD platform at [Tech Report](https://web.archive.org/web/20080513153734/http://techreport.com/articles.x/14261/1), [Silent PC Review](http://www.silentpcreview.com/article807-page1.html), and [Tom’s Hardware](http://www.tomshardware.com/reviews/amd-780g-chipset,1785.html) finally pushed me over the edge.

kg-card-begin: html


| CPU | AMD Athlon X2 4850e 2.5 GHz (45w) | $60 |
| Mobo | Gigabyte GA-MA78GPM-DS2H Micro ATX | $100 |
| RAM | Kingston 2GB DDR2 800 | $39 |
| PSU | Seasonic ECO 300W | $55 |
| DVD | Lite-On 20X DVDÃ‚Â±R SATA | $29 |


kg-card-end: html

I didn’t buy the PSU because I already have that particular model, but I bought everything else on this list for a grand total of **less than 250 bucks.** (You can save a bit on the power supply, but I don’t recommend it, particularly if you plan to leave your HTPC running 24/7. [Efficient power supplies](https://blog.codinghorror.com/upgrading-to-a-high-efficiency-power-supply/) not only save you money on electricity in the long run, but also tend to be of generally higher quality, and quieter to boot.)


The new [AMD 780G](http://www.amd.com/us-en/0,,3715_15532,00.html?redir=780g1) platform is striking in its simplicity. Just pop in the RAM and the low-power Athlon X2 CPU and you have an (almost) complete ultra low-power home theater PC. Just check out the awesome array of rear panel connections:


![](https://blog.codinghorror.com/content/images/2025/04/image-99.png)


We have the expected stuff (4x USB, gigabit ethernet), but the exciting part is **DVI, VGA, and HDMI video out!** Not to mention optical digital out for beautiful, pristine digital audio direct to your receiver. Those are the key connections for a home theater PC. We even have an eSATA port and firewire thrown in, which is always nice.


I simply dropped the new motherboard and DVD in my existing transparent acrylic Micro-ATX PC case, replacing the old stuff. (If you’re thinking of going this route, I can recommend the Antec Minuet Micro-ATX case for $100, which conveniently comes with an efficient power supply, too – but be aware of the half-height expansion slots.)


![](https://blog.codinghorror.com/content/images/2025/04/image-98.png)


I kept my existing hard drives (a small 2.5" boot drive for low noise / power consumption, and giant capacity 3.5" drives for long-term storage and recording), and my Hauppauge PVR-150 dual analog PCI tuner card, which I love to death.


For the longest time, *integrated* graphics was synonymous with *craptacular* graphics. That’s not the case for this new AMD 780g chipset. The integrated graphics are fully DirectX 10 compliant, comparable to the latest entry-level discrete video cards. Gaming isn’t our goal, though this would be perfectly adequate for many games. More importantly for a HTPC build, the integrated graphics support the full suite of H.264 and WMV video playback acceleration.


![](https://blog.codinghorror.com/content/images/2025/04/image-97.png)


I know a WEI graphics score of 3.5 doesn’t sound like much, but brother, let me tell you – this is light years ahead of anything else on the market at this power consumption point.


Update: I had a hardware failure of my own causing (don’t ask) and I needed to replace this motherboard. Fortunately, there is a new version of this motherboard with 128 MB of dedicated “sideport” DDR3 graphics memory on board. With the addition of dedicated video memory **the WEI graphics score went from 3.5 / 3.6 to 4.0 / 4.0!**


My old Pentium-M single core struggled to [play back 1080p videos](https://blog.codinghorror.com/high-definition-video-on-the-pc/). The Athlon X2 4050e CPU I chose is one of AMD’s [low power dual core models](http://www.tomshardware.com/reviews/amd-power-cpu,1925.html), far from top of the line. The testers at SilentPCReview found **any modern dual core chip **is more than enough for the most strenuous of video playback tasks:


> Gradually underclocking the CPU, we found that the Blu Ray disc began to stutter at about 1.1Ghz, while audio glitches were detected in the WVC1 clip at 1.4Ghz. 1.5Ghz was the lowest clock speed that would smoothly play back all our clips. This was a fantastic result as the lowest clocked X2 on the market is 2.0 Ghz.


AMD is a better choice for a home theater PC because their idle voltage and multiplier throttling – the marketing term is “Cool n’ Quiet” – is outstanding. (I’m also glad to have the opportunity to support AMD because I’m desperately afraid of a world where Intel is the only CPU vendor. And you should be too.) This variant of the Athlon 64 X2 chip is so new that [CPU-Z](http://www.cpuid.com/cpuz.php) doesn’t quite recognize it by name. But as you can see, at idle, it clocks down to a miserly 1 GHz and reduces its power consumption to barely over one volt.


![](https://blog.codinghorror.com/content/images/2025/04/image-96.png)


My old highly optimized HTPC build consumed just under 80 watts at idle, up from around 65 before I began upgrading it to make it more Vista friendly. Guess how much this new HTPC platform build, which is **more than twice as powerful**, consumes at idle? Let’s whip out our [handy dandy kill-a-watt](https://blog.codinghorror.com/revisiting-how-much-power-does-my-laptop-really-use/) and find out:


![](https://blog.codinghorror.com/content/images/2025/04/image-95.png)


FORTY. SIX. WATTS.


That is flippin’ *amazing*. We’re talking about a powerful modern PC here, with quite a bit of additional hardware you wouldn’t find in most PCs, including a dual TV tuner PCI card and three hard drives. Granted two of those drives are in sleep mode most of the time, but still. 46 watts – twice the power at almost half the energy consumption! Incredible! Silence and efficiency were nowhere *near* this easy three or four years ago.


Needless to say, I’m pretty excited about this particular $250 upgrade, and I can sell my old parts to underwrite it.


On the software front, as I mentioned at the top, I’ve been a fan of Windows Media Center [since the first version](https://blog.codinghorror.com/media-center-goes-retail/); it’s one of the best products to come out of Redmond in years, and the version of [Media Center bundled with Vista](https://blog.codinghorror.com/windows-vista-media-center/) (well, Ultimate and Home Premium, anyway) is the best yet. With a hardware setup this compelling, I’m sure you’ll have no problem at all mating it with your favorite HTPC software.


If you do end up running Windows and connecting your HTPC to a DVI or HDMI capable television, beware. Getting an exact, pixel-for-pixel connection between your HTPC and your TV isn’t easy. For example, I had trouble getting the ATI Catalyst graphics driver to accept **852x480, the standard resolution of our old plasma EDTV**. Sure 800x600 worked fine, but the aspect ratio was totally off. That’s where [PowerStrip](http://www.entechtaiwan.com/util/ps.shtm) comes in.


![](https://blog.codinghorror.com/content/images/2025/04/image-94.png)


PowerStrip will let you achieve that ideal pixel-for-pixel perfect connection between your graphics card and your television. I selected the built in EDTV preset as a custom resolution, and all was well. PowerStrip is *the* go-to utility for tweaking home theater display output.


**We use our home theater PC every day.** It’s silent, draws very little power, and it’s small enough to tuck away cleanly in our living room decor. It plays *anything* through a slick 10-foot UI, and offers unrestricted access to the web at any time. Putting a great one together today is almost ridiculously easy. If you haven’t considered building your own home theater PC – why not?

kg-card-begin: html

UPDATE: since people asked, here’s a complete from-scratch build list for a home theater PC.

kg-card-end: html
kg-card-begin: html


| CPU | AMD Athlon X2 4850e 2.5 GHz (45w) | $70 |
| Mobo | Gigabyte GA-MA78GPM-DS2H Micro ATX | $100 |
| RAM | Kingston 2GB DDR2 800 | $40 |
| DVD | Lite-On 20X DVDÃ‚Â±R SATA | $30 |
| Case/PSU | Antec Minuet w/80plus certified PSU | $100 |
| HDD | Western Digital quiet 500 GB | $90 |
| Tuner | Hauppauge low profile analog cable/TV | $76 |
| Remote | Standard Media Center IR | $17 |
|  |  | **$523** |


kg-card-end: html

If you plan to use Vista Media Center, add a Vista Home Premium SP1 license for $110. I also saw that Blu-Ray internal drives (read only) are down to $130 as of the time I’m writing this.

[home theater](https://blog.codinghorror.com/tag/home-theater/)
[pc building](https://blog.codinghorror.com/tag/pc-building/)
[amd platform](https://blog.codinghorror.com/tag/amd-platform/)
[hardware components](https://blog.codinghorror.com/tag/hardware-components/)
[htpc](https://blog.codinghorror.com/tag/htpc/)
