---
title: "Building a Computer the Google Way"
date: 2007-03-12
url: https://blog.codinghorror.com/building-a-computer-the-google-way/
slug: building-a-computer-the-google-way
word_count: 1230
---

If you’re ever in Silicon Valley, I highly recommend checking out the [Computer History Museum](http://www.computerhistory.org/). Where else can you see a live demonstration of the only known [working PDP-1](http://www.computerhistory.org/pdp-1/) in existence, and actually get to *play the original *[*Spacewar*](http://en.wikipedia.org/wiki/Spacewar!)* on it?* I did. It was incredible. I got chills. And my wife was bored beyond belief, but I love her all the more for soldiering through.


Beyond the special exhibits, the Visible Storage area is where the real action is at in the museum. It takes up the majority of the floor space, and it contains every computer I’ve ever heard of. Among the artifacts in visible storage is one of **Google’s original servers from 1999**:


![Google Server at the Computer History Museum, rack from afar](https://blog.codinghorror.com/content/images/uploads/2007/03/6a0120a85dcdae970b0128777004a4970c-pi.jpg)


![Google Server at the Computer History Museum, closeup of rack](https://blog.codinghorror.com/content/images/uploads/2007/03/6a0120a85dcdae970b0128777004bd970c-pi.jpg)


![Google Server at the Computer History Museum, placard: With limited funds, Google founders Larry Page and Sergey Brin initially deployed this system of inexpensive, interconnected PCs to process many thousands of search requests per second from Google users. This hardware system reflected the Google search algorithm itself, which is based on tolerating multiple computer failures and optimizing around them. This production server was one of about thirty such racks in the first Google data center. Even though many of the installed PCs never worked and were difficult to repair, these racks provided Google with its first large-scale computing system and allowed the company to grow quickly and at minimal cost.](https://blog.codinghorror.com/content/images/uploads/2007/03/6a0120a85dcdae970b0128777004d0970c-pi.jpg)


If Google’s first production server resembles a hastily cobbled together amalgam of off-the-shelf computer parts circa 1999, well, that’s because *it is*. Just like [Google’s original servers at Stanford](https://blog.codinghorror.com/google-hardware-circa-1999/). If you think this rack is scary, you should see what it *replaced*.


Instead of buying whatever pre-built rack-mount servers Dell, Compaq, and IBM were selling at the time, **Google opted to hand-build their server infrastructure themselves**. The sagging motherboards and hard drives are literally propped in place on handmade plywood platforms. The power switches are crudely mounted in front, the network cables draped along each side. The poorly routed power connectors snake their way back to generic PC power supplies in the rear.


Some people might look at these early Google servers and see an amateurish fire hazard. Not me. I see a prescient understanding of how inexpensive commodity hardware would [shape today’s internet](https://blog.codinghorror.com/web-2-0-and-the-whatever-box-server/). I felt right at home when I saw this server; it’s *exactly* what I would have done in the same circumstances. This rack is a perfect example of the commodity x86 market D.I.Y. ethic at work: if you want it done right, and done inexpensively, you build it yourself.


Even today, Google is serious about exerting total control over the servers in their now-massive server farms. They build their own [high-efficiency power supplies](http://www.nytimes.com/2006/09/26/technology/26google.html?ex=1173931200&en=372d524a3de3d515&ei=5070), and conduct fascinating, [public research on disk failure](https://web.archive.org/web/20080910032948/http://labs.google.com/papers/disk_failures.pdf) (pdf). Current estimates put [Google’s server farm](http://en.wikipedia.org/wiki/Google_platform) at around 450,000 machines – and they’re still custom built, commodity-class x86 PCs, just like they were in 1999.


**Like Google, I demand total control over every part of my PC.** I’ve always built my own. Building your own PC isn’t for everyone, but if you’re willing to add a little elbow grease, the D.I.Y. approach can result in a higher quality, better performing PC – often at a substantial cost savings.


Here’s a chart I put together based on my research for the Scott Hanselman [Ultimate Developer Rig Throwdown](http://www.hanselman.com/blog/TheCodingHorrorUltimateDeveloperRigThrowdownPart1.aspx):

kg-card-begin: html

**
D.I.Y.

“Big Bang” **

**
D.I.Y.

“Little Bang”**

**[
Mac  Pro](http://store.apple.com/AppleStore/WebObjects/BizCustom?qprm=78313&family=MacPro)**

**[
Dell XPS 710](http://www.dell.com/content/products/features.aspx/cto_xpsdt_410?c=us&cs=19&l=en&s=dhs)**

**[
Dell Dimension 410](http://www.dell.com/content/products/features.aspx/cto_xpsdt_410?c=us&cs=19&l=en&s=dhs)**



CPU

Intel Core 2 Quad

2.4 GHz 

Intel Core 2 Duo

2.4 GHz

2 x Intel Core 2 Duo

2.66 GHz

Intel Core 2 Duo

2.4 GHz

Intel Core 2 Duo

2.4 GHz



Memory

4 GB, DDR 800

2 GB, DDR 800

1 GB, DDR ECC 667

2 GB, DDR 667

2 GB, DDR 667



Mobo

P965 premium

P965 budget

Intel 5000x

unknown

unknown



Drives

2 x 150 GB 10k RPM (RAID 0)

2 x 750 GB (RAID 1)

500 GB

250 GB

500 GB

500 GB



Video

2 x 512 MB X1950 Pro

256 MB X1950 Pro

256 MB 7300 GT

256 MB 7900 GS

256 MB 7900 GS



Case

[Antec P180](http://www.antec.com/us/productDetails.php?ProdID=81800)




[Antec P180](http://www.antec.com/us/productDetails.php?ProdID=81800)

Apple




XPS




Dimension






Other

Premium PSU

Premium heatsink

Premium PSU

Premium heatsink

OS X

Bundled software

Windows Vista

Windows Vista



Price

$3,500

$1,400

$2,499

$2,039

$1,400



kg-card-end: html
If you’re willing to factor out the cost of the operating system, the D.I.Y. “Little Bang” system offers more bang for the buck than any of its peers. And the “Big Bang” is off the charts, if you have the budget.The lower-end Dell system looks quite similar, but closer inspection reveals otherwise:Dell’s use of non-standard case connectors and power supply connectors prevents future upgrades using standard commodity parts.The OEM parts used in Dell machines are generally of inferior quality to their retail equivalents. OEM parts are impressive on the surface, but cut corners to lower costs. For example, the use of slower DDR 667 memory; cut-down, featureless OEM motherboards; video cards with lower clocks and slower memory.Absolutely no overclocking potential.Limited internal case expansion for additional hard drives and video cards.The Mac Pro is a beautifully designed machine, but it has some quirks, too:Quad-core in a single socket, ala the “Big Bang” system, makes more sense than this Dual-Dual arrangement. Obviously Apple will produce a Dual-Quad for a total of 8 CPUs any day now. But there is a serious point of [diminishing returns with additional CPUs](https://blog.codinghorror.com/quad-core-desktops-and-diminishing-returns/) unless you’re doing something highly specific and highly parallelizable like raytracing or rendering.Requires expensive DDR2 buffered ECC RAM, because it’s a server motherboard.Zero overclocking options.667 MHz memory? Not that it matters very much to bottom-line performance, but support for different FSB speeds would be nice.The default video card and hard drive are totally pedestrian, and will limit overall performance unless replaced.If you don’t have the time or inclination to build your own desktop PC, the Dells and the Mac Pro are perfectly valid choices. The prices are reasonable; the configurations flexible. There’s absolutely nothing wrong with buying pre-built, as long as you spec carefully. But by the time I’m done setting up my D.I.Y. “Little Bang” system, it’ll be faster, quieter, and more power efficient than any of the pre-built systems – for the same money, or less. This is possible because the D.I.Y. system is uniquely mine; I choose exactly what goes in it, and exactly how it’s configured.Pre-built might work for typical users. But pre-built didn’t work for Google. And pre-built doesn’t work for me.We aren’t typical users. We’re programmers. **The x86 commodity PC is the essential, ultimate tool of our craft.** It’s the end product of 30 years of computer evolution. And it’s still evolving today, with profound impact on the way we code. If you treat your PC like an appliance you plug into a wall, you’ve robbed yourself of a crucial lesson on the symbiotic relationship between software and hardware. The best way to truly *understand* the commodity PC is to gleefully dig in and **build one yourself**. Get your hands dirty and experience the economics of computer hardware first hand – the same economics that have shaped the software industry since the very first line of code was stored in memory.Who knows, you might even enjoy it.

[hardware](https://blog.codinghorror.com/tag/hardware/)
[technology trends](https://blog.codinghorror.com/tag/technology-trends/)
[computer history](https://blog.codinghorror.com/tag/computer-history/)
[server infrastructure](https://blog.codinghorror.com/tag/server-infrastructure/)
[google](https://blog.codinghorror.com/tag/google/)
