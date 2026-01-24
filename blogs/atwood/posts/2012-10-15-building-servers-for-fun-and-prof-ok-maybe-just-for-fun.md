---
title: "Building Servers for Fun and Prof... OK, Maybe Just for Fun"
date: 2012-10-15
url: https://blog.codinghorror.com/building-servers-for-fun-and-prof-ok-maybe-just-for-fun/
slug: building-servers-for-fun-and-prof-ok-maybe-just-for-fun
word_count: 1314
---

In 1998 I briefly worked for FiringSquad, a gaming website founded by Doom and Quake champion Thresh aka [Dennis Fong](http://en.wikipedia.org/wiki/Dennis_Fong) and his brother Lyle. I can trace my long-standing interest in chairs and keyboards to some of the early, groundbreaking articles they wrote. Dennis and Lyle were great guys to work with, and we’d occasionally chat on the phone about geeky hardware hotrodding stuff, like the one time they got so embroiled in PC build one-upmanship that they were actually building rack-mount PCs… *for their home*.


So I suppose it is inevitable that I’d eventually get around to writing an article about **building rack-mount PCs**. But *not* the kind that go in your home. No, that’d be as nuts as the now-discontinued [Windows Home Server](http://en.wikipedia.org/wiki/Windows_Home_Server) product.


![](https://blog.codinghorror.com/content/images/2025/04/image-680.png)


Servers belong in their native habitat, the datacenter. Which can be [kind of amazing places](http://scobleizer.com/2011/04/16/photo-tour-of-facebooks-new-datacenter/) in their own right.


![](https://blog.codinghorror.com/content/images/2025/04/image-679.png)


The above photo is from Facebook’s [Open Compute Project](http://opencompute.org/), which is about building extremely energy efficient datacenters. And that starts with minimalistic, [no-frills 1U server designs](https://web.archive.org/web/20121025162621/http://www.datacenterknowledge.com/closer-look-open-compute-server-designs/), where 1U is the smallest amount of space divisible in a server rack.


I doubt many companies are big enough to even consider building their own datacenter, but if Facebook is building their own custom servers out of commodity x86 parts, couldn’t we do it too? In a world of inexpensive, rentable virtual machines, like [Amazon EC2](http://aws.amazon.com/ec2/), [Google Compute Engine](https://cloud.google.com/products/compute-engine), and [Azure Cloud](http://www.windowsazure.com/en-us/), **does it really make sense to build your own server and colocate it in a datacenter?**


It’s kind of tough to tell exactly how much an Amazon EC2 instance will cost you since it varies a lot by usage. But if I use the Amazon Web Services [simple monthly calculator](http://calculator.s3.amazonaws.com/calc5.html) and select the Web Application “common customer sample,” that provides a figure of**$1,414 per month, or $17k/year**. If you want to run a typical web app on EC2, that’s what you should expect to pay. So let’s use that as a baseline.


The [instance types](http://aws.amazon.com/ec2/instance-types/) included in the Web Application customer sample are 2 4 small (for the front end), and 12 large (for the database). Here are the current specs on the large instance:

- 7.5 GB memory
- 2 virtual cores with 2 EC2 Compute Units each
- 850 GB instance storage
- 64-bit platform
- I/O Performance: High


You might be wondering what the heck a [EC2 Compute Unit](http://aws.amazon.com/ec2/faqs/#What_is_an_EC2_Compute_Unit_and_why_did_you_introduce_it) is; it’s Amazon’s way of normalizing CPU performance. By their definition, what we get in the large instance is akin to an old [2008 era](http://en.wikipedia.org/wiki/Xeon#Overview) dual core 2.4 GHz Xeon CPU. Yes, you can pay more and get faster instances, but switching instances from the small to the high-CPU and from the large to the high-MEM more than doubles the bill to **$3,302 per month or $40k/year**.


Assuming you subscribe to the theory of [scaling out versus scaling up](https://blog.codinghorror.com/scaling-up-vs-scaling-out-hidden-costs/), building a bunch of decent bang-for-the-buck commodity servers is what you’re supposed to be doing. I avoided directly building servers when we were scaling up Stack Overflow, electing to buy [pre-assembled hardware from Lenovo](http://blog.stackoverflow.com/2009/01/new-stack-overflow-server-glamour-shots/) instead. But this time, I decided the state of hardware has advanced sufficiently since 2009 that I’m comfortable cutting out the middleman in 2012 and **building the servers myself, from scratch**. That’s why I just built four servers exactly like this:

- Intel Xeon E3-1280 V2 Ivy Bridge 3.6 Ghz / 4.0 Ghz turbo quad-core ($640)
- SuperMicro [X9SCM-F-O](http://www.amazon.com/dp/B004WKRDA4) ($190)
- 32 GB DDR3-1600 ($292)
- SuperMicro SC111LT-330CB 1U rackmount chassis ($200)
- Two [Samsung 830](http://www.amazon.com/dp/B0077CR6B0) 512GB hard drives in a [RAID-1 mirror](https://blog.codinghorror.com/beyond-raid/) ($540 × 2)


(If you are using this as a shopping list, you will also need 4-pin power [extensions](http://www.newegg.com/Product/Product.aspx?Item=N82E16812200961) for the case, and the SuperMicro 1u [passive heatsink](http://www.newegg.com/Product/Product.aspx?Item=N82E16816101298). The killer feature of SuperMicro motherboards that makes them all server-y in the first place is the built in [hardware KVM-over-IP](http://www.servethehome.com/supermicro-ipmiview-review-remote-server-monitoring-management-ipmi-20-kvm-over-ip/). That’s right, unless the server is literally unplugged, you can remote in and install an operating system, tweak the BIOS, power it on and off, and so on. It works. I use it daily.)


![](https://blog.codinghorror.com/content/images/2025/04/image-678.png)


Based on the above specs, this server has comparable memory to the High-Memory Double Extra Large Instance, comparable CPU power to the High-CPU Extra Large Instance, and comparable disk performance to the High I/O Quadruple Extra Large Instance. This is a very, *very* high end server by EC2 standards. It would be prohibitively expensive to run this hardware in the Amazon cloud. But how much will it cost us to build? Just $2,452. Adding 10% for taxes, shipping, etc. let’s call it $2,750 per server. **One brand new top-of-the-line server costs about as much as two months of EC2 web application hosting.**


Of course, that figure doesn’t include the cost in time to build and rack the server, the [cost of colocating the server](https://web.archive.org/web/20120628130319/http://blog.pinboard.in/2012/06/going_colo/), and the ongoing cost of managing and maintaining the server. But I humbly submit that the one-time cost of paying for three of these servers, plus the cost of colocation, plus a bunch of extra money on top to cover provisioning and maintenance and support, will still be *significantly* less than $17,000 for a *single year* of EC2 web application hosting. Every year after the first year will be gravy, until the servers are obsolete – which even conservatively has to be at least three years. Perhaps most importantly, these servers will offer **vastly better performance** than you could get from EC2 to run your web application, at least not without paying astronomical amounts of money for the privilege.


![](https://blog.codinghorror.com/content/images/2025/04/image-677.png)


(If you are concerned about power consumption, don’t be. I just measured the power use of the server using my trusty [Kill-a-Watt device](https://blog.codinghorror.com/why-estimate-when-you-can-measure/): **31 watts** (0.28 amps) at idle, **87 watts** (0.75 amps) under never-gonna-happen artificial 100% CPU load. The three front fans in the SuperMicro case are plugged into the motherboard and only spin up at boot and under extreme load. It’s shockingly quiet in typical use for a 1U server.)


I realize that to some extent we’re comparing apples and oranges. Either you have a perverse desire to [mess around with hardware](https://web.archive.org/web/20121016115200/http://blog.pinboard.in/2012/05/a_cloud_of_my_own/), or you’re more than willing to pay exorbitant amounts of money to have someone else worry about all that stuff (and, to be fair, give you levels of flexibility, bandwidth, and availability that would be impossible to achieve even if you colocate servers at multiple facilities). $51,000 over three years is enough to pay for a *lot* of colocation and very high end hardware. But maybe the truly precious resource at your organization is people’s time, not money, and that $51k is barely a rounding error in your budget.


Anyway, I want to make it clear that **building and colocating your own servers isn’t (always) crazy, it isn’t scary, heck, it isn’t even particularly *hard***. In some situations it can make sense to build and rack your own servers, provided…

- you want absolute top of the line server performance without paying thousands of dollars per month for the privilege
- you are willing to invest the time in building, racking, and configuring your servers
- you have the capital to invest up front
- you desire total control over the hardware
- you aren’t worried about the flexibility of quickly provisioning new servers to handle unanticipated load
- you don’t need the redundancy, geographical backup, and flexibility that comes with cloud virtualization


Why do I choose to build and colocate servers? Primarily to achieve maximum performance. That’s the one thing you consistently just *do not get* from cloud hosting solutions unless you are willing to pay a massive premium, per month, forever: raw, unbridled performance. I’m happy to spend money on nice dedicated hardware because I know that [hardware is cheap, and programmers are expensive](https://blog.codinghorror.com/hardware-is-cheap-programmers-are-expensive/).


But to be totally honest with you, mostly I build servers because it’s fun.

[hardware](https://blog.codinghorror.com/tag/hardware/)
[servers](https://blog.codinghorror.com/tag/servers/)
[rack-mount pcs](https://blog.codinghorror.com/tag/rack-mount-pcs/)
[datacenter](https://blog.codinghorror.com/tag/datacenter/)
[open compute project](https://blog.codinghorror.com/tag/open-compute-project/)
