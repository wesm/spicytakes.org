---
title: "Multiple Core CPU Futures"
date: 2005-05-08
url: https://blog.codinghorror.com/multiple-core-cpu-futures/
slug: multiple-core-cpu-futures
word_count: 595
---

Both AMD and Intel now have dual core CPUs on the market, in the form of the [Athlon 64 X2](https://web.archive.org/web/20050509142431/http://techreport.com/reviews/2005q2/athlon64-x2/index.x?pg=1) and the [Pentium 4 D](https://web.archive.org/web/20050923174834/http://www20.tomshardware.com/cpu/20050405/index.html) series. They may be expensive now, but I fully expect dual core architectures to trickle down to the rest of the lineup within the next two years.


I’ve mentioned before that I’m a big fan [of the Athlon 64 series](https://blog.codinghorror.com/athlon-64-developers-choice/) because it compiles code so much faster* than the equivalent Pentium 4. This advantage naturally extends to the dual core Athlon 64 X2 as you can see in these [multitasking compilation benchmarks](http://www.anandtech.com/cpuchipsets/showdoc.aspx?i=2397&p=25):


![](https://blog.codinghorror.com/content/images/2025/05/image-86.png)


**The Athlon 64 benefits more than the Pentium 4 from the dual core design** because it has a superior architecture – specifically, an on-die memory controller – and because it had no special threading support prior to the dual core update. Intel primed the market for better [threading support with Hyperthreading](https://web.archive.org/web/20060208090018/http://blogs.msdn.com/oldnewthing/archive/2004/09/13/228780.aspx), and we’re now poised to reap the benefits with the true dual core designs.


Dual core designs are fantastic from a technology standpoint, but as a software developer, it’s a scary trend. If the only way we can increase speed is through extra parallelism (aka threading), our coding and debugging burden just went through the roof. See “[Threading, Concurrency](https://blog.codinghorror.com/threading-concurrency-and-the-most-powerful-psychokinetic-explosive-in-the-univ/) and The Most Powerful Psychokinetic Explosive in The Universe” for my take on that. The challenge of increasing speed starts to shift from the [hardware to the software](https://web.archive.org/web/20061216160909/http://blogs.msdn.com/volkerw/archive/2005/05/02/413985.aspx):


> *But how will users benefit from multiple cores? Will the apps run faster just because there a now 2 processors on a single chip? I guess not really. There are benefits for the OS that may relate to improved performance. But the app itself? Well, you can run multiple instances easier and better for one. But what about a single app? **A single threaded (client) app that has been designed with a single processor and a single thread of execution in mind, will not benefit and therefore users will not benefit from multiple processors or multiple cores.***


And it gets worse. Check out this [interview with Hector Ruiz](https://web.archive.org/web/20060905071955/http://www.infoworld.com/article/05/05/02/18NNruiz_1.html), the CEO of AMD:


> *IW: What lies beyond dual-core for AMD?
> HR: **It’s hard to tell right now beyond four cores. The probability of having a four-core product is very high.** There’s a lot of work going on with our engineering teams and with our customers to figure out where we go beyond that. There are two or three options that look pretty attractive. We’ll be narrowing down our choices.
> IW: It is interesting that you did not say that four-core is a certainty. Are you looking at different ways of improving performance other than doubling the number of cores?
> HR: At the end of the day, for us, it’s going to be what our customers want. **Making transistors is pretty trivial. We can make hundreds of millions of transistors. Figuring out what the hell to do with those transistors is the challenge.** One could choose, for example, to have heterogeneous cores. You could have two cores that are different instead of the same. That opens up a completely different array of possibilities.*


Once two cores become standard, you can expect four cores to follow in short order. One day, **you won’t be able to throw money at your hardware to make your app run faster**. You’ll have no choice but to pour that money into parallelizing the algorithms inside your app, which is a far more difficult proposition.


*It’s also significantly faster in games, not that I play those.

[cpu](https://blog.codinghorror.com/tag/cpu/)
[dual core](https://blog.codinghorror.com/tag/dual-core-2/)
[architecture](https://blog.codinghorror.com/tag/architecture/)
[benchmark](https://blog.codinghorror.com/tag/benchmark/)
[multitasking](https://blog.codinghorror.com/tag/multitasking/)
