---
title: "Why do we use the Linux kernel's TCP stack?"
date: 2016-06-30
url: https://jvns.ca/blog/2016/06/30/why-do-we-use-the-linux-kernels-tcp-stack/
slug: why-do-we-use-the-linux-kernels-tcp-stack
word_count: 1323
---


I’m at PolyConf in Poland today, and I watched this super interesting talk by Leandro Pereira about [Lwan](https://lwan.ws/), an ~8000 line of code web server. He talked about a bunch of the optimizations they’d done (improve CPU cache performance! be really careful about locking!). You can read more about the performance on the website & the links there.


It’s a super cool project because it started out as a hobby project, and now he says it’s getting to a state where it kinda actually really works and people are using it for real things. This web server is extremely fast – it can do, in some benchmarks, 2 million requests per second.


Before I start talking about this – of course practically nobody needs to do 2 million requests per second. I sure don’t. But thinking about high performance computing is a really awesome way to understand the limits of computers better!


I tracked him down to ask him questions later, and he mentioned that most of the time is spent talking to the Linux kernel and copying things back and forth.


### writing your own tcp stack is way faster


Then he said something really surprising: that in the [Seastar](http://www.seastar-project.org/) HTTP framework, they **wrote their own TCP stack**, and it made everything several times times faster. What?!


So – this made me wonder. When we do high performance networking – why do we bother using the Linux kernel’s TCP stack at all, if it’s so expensive? Why not just do all the networking in userspace? I had no idea where to start with this question, so I [asked on Twitter](https://twitter.com/b0rk/status/748649763118133248). As often happens, you all came through with ONE BILLION INTERESTING LINKS AND ANSWERS.


### embedded devices


If you’re working on a very small computer without an operating system, you sometimes need to do networking anyway! In this case it seems pretty common to use a separate TCP stack. A ton of people mentioned that they either used [lwIP](http://savannah.nongnu.org/projects/lwip/) or wrote their own TCP stack to meet their own specific requirements.


I asked a few people whether anyone uses lwIP on a Real Server, but it seems like it’s optimized for small devices, and not for doing huge amounts of network traffic on big servers.


### high frequency trading


Who cares about doing a ton of very fast network requests? People who do high frequency trading! Luke Gorrie on Twitter (who works on the extremely cool [Snabb Switch](https://snabb.co/) open source Ethernet stack) said:


> Solarflare sell a userspace TCP stack to HFT market (OpenOnload) for use with
> their NICs. Code is GPL actually.


So, this makes a lot of sense. If you want to do super high performance networking, you can probably afford to buy special network cards and special software to make those network cards perform super well. Cool. But what if you want to do higher performance networking on commodity hardware, with any random network card? Is that a thing?


### what about Google?


Who else does a ton of networking? Google! Happily Google sometimes writes papers so we know a little bit about what they do there.


Tons of people told me about [Maglev](http://research.google.com/pubs/pub44824.html), which is Google’s load balancer, and they do all of their networking for that in userspace! I think they operate at a lower level than TCP so they don’t have a TCP stack, but it is an example of extremely fast networking without using the Linux kernel.


I haven’t read the Maglev paper yet but it seems like a good starting point.


There’s also [this blog post](https://cloudplatform.googleblog.com/2015/06/A-Look-Inside-Googles-Data-Center-Networks.html?m=1) and [paper](http://conferences.sigcomm.org/sigcomm/2015/pdf/papers/p183.pdf) about software-defined networking at Google. A useful keyword here seems to be “Jupiter” or “Jupiter fabrics” but I’m not sure what that is. [Here’s another article though](http://www.nextplatform.com/2015/06/19/inside-a-decade-of-google-homegrown-datacenter-networks/).


### is the real reason to write your own TCP stack for performance?


[@tgraf__](https://twitter.com/tgraf__) made a super interesting point – I thought the reason you would make your own TCP stack was to make it fast. But maybe not always!!


> Google can’t force Android vendors to rebase kernels but requires new TCP
> functionality such as TCP fast open.


The TCP standard is evolving, and if you have to always use your kernel’s TCP stack, that means you can NEVER EVOLVE.


### why is TCP in the kernel slow?


This [article from LWN](https://lwn.net/Articles/169961/) “Van Jacobsen’s network channels” says that dealing with TCP in kernel space means locks and contention. thanks for @tef_ebooks for linking this article and explaining it to me :)


> The key to better networking scalability, says Van, is to get rid of locking and shared data as much as possible, and to make sure that as much processing work as possible is done on the CPU where the application is running. It is, he says, simply the end-to-end principle in action yet again. This principle, which says that all of the intelligence in the network belongs at the ends of the connections, doesn’t stop at the kernel. It should continue, pushing as much work as possible out of the core kernel and toward the actual applications.


### how does Seastar work?


That fast networking framework Seastar from before is written using something from Intel called [DPDK](http://dpdk.org/). The deal with DPDK seems to be that it’s a network card driver and some libraries, but instead of it giving you packets through interrupts (asynchronously), instead it polls the network card and say “do you have a packet yet? now? now? now?”.


This makes sense to me because in general if you always have new events to process, then polling is faster (because you basically don’t have to wait). Here’s some documentation about the [poll mode driver](http://dpdk.org/doc/guides-16.04/prog_guide/poll_mode_drv.html) and an [example of a DPDK] application.


I think with DPDK you can write networking applications that work entirely in userspace with no system calls.  [Cory Benfield](https://twitter.com/Lukasaoz/status/748853883703820293) explained a bunch of these things to me.


### open source stuff right now: pretty specific


As far as I can tell, there aren’t any available general purpose open source userspace TCP/IP stacks available. There are a few specialized ones, but this does not seem to exist right now. But people seem to be interested in the topic!


### some more links


Here are some more links that do networking in userspace! This is mostly a link dump so that I can click on them later but maybe you will like them too.


[zmap](https://zmap.io/paper.pdf) is a TCP port scanner.


[masscan](https://github.com/robertdavidgraham/masscan) is another TCP port scanner. It says it can scan the entire internet in 5 minutes. What? Outlandish! I will need to read more about this!


[LKL](https://github.com/lkl/linux) is an attempt to make the Linux kernel networking code (as well as other Linux code) into a library (!!) so that we can use it in userspace. This sounds like a monumental effort and also extremely interesting. [@thehakime said about this](https://twitter.com/thehajime/status/748657015702986752):. [Here’s a talk about LKL.](http://www.slideshare.net/hajimetazaki/library-operating-system-for-linux-netdev01)


> there are so many uspace network stacks (mtcp, lwip, seastar, sandstrom) but all are so specialized. I think it can be generalized.


[libuinet](https://github.com/pkelsey/libuinet) is a library version of FreeBSD’s TCP stack. I guess there’s a theme here.


[mtcp](https://github.com/eunyoung14/mtcp) is a userspace TCP stack. I don’t know anything about it. There’s also [uip](https://github.com/adamdunkels/uip) and [lwIP](http://savannah.nongnu.org/projects/lwip/).


### phew.


Okay, that was a lot of new facts and ideas to come out of the comment “a lot of the overhead of a HTTP server is communicating with the kernel”.


I like how if you ask the right questions Twitter will just hurl super interesting information at you until you’re like OK OK OK MY BRAIN IS FULL. And then they keep telling you awesome stuff anyway :)


There seems to be a lot of work going on here! There are like 100 interesting rabbit holes which I have zero time to investigate right now! Awesome.


Update: Marek Majkowski at Cloudflare wrote a very interesting response to this post [Why we use the Linux kernel’s TCP stack](https://blog.cloudflare.com/why-we-use-the-linux-kernels-tcp-stack/) which is worth reading.
