---
title: "On Managed Code Performance"
date: 2005-03-08
url: https://blog.codinghorror.com/on-managed-code-performance/
slug: on-managed-code-performance
word_count: 876
---

My personal turning point on the importance of managed code was in September 2001, when the [NIMDA worm](https://web.archive.org/web/20050408022420/http://news.com.com/2100-1001-273128.html?legacy=cnet) absolutely *crushed* our organization. It felt like a natural disaster without the “natural” part – the first notable port 80 IIS buffer overrun exploit. We got literally zero work done that day, and the next day wasn’t much better. After surveying the carnage first hand, I immediately saw the benefit of **languages where buffer overruns weren’t even possible**.


Managed code, of course, isn’t free. All that bit-twiddling was there for a reason – to squeeze every last iota of performance out of your 386 and 486. Trading some of that performance for security makes more sense in the era of 1ghz Pentium chips, of course – but how much performance are we really giving up? One of the more interesting examples of managed code performance is Vertigo Software’s port of [Quake II to .NET](https://web.archive.org/web/20050320093635/http://www.vertigosoftware.com/Quake2.htm):


> ***How is the performance of the managed version of Quake II?** Initially, the managed version was faster than the native version when the default processor optimization setting /G5 (Pentium) was used. Changing the optimization setting to /G7 (Pentium 4 and Above) created **a native version that runs around 15% faster then the managed version.** Note that assembly code was disabled for the native and managed versions, so both versions are slower than the original version of Quake 2.*


[David Notario](https://web.archive.org/web/20050306020922/http://www.xplsv.com/blogs/devdiary/), who works in Microsoft’s CLR JIT compiler group, with a little [demo scene coding](https://web.archive.org/web/20050305192127/http://www.xplsv.com/) on the side, posted this interesting message with more detail on the performance of Managed Quake II:

kg-card-begin: html

> *
> This version doesn’t use any 3D hardware acceleration at all, which is good. It’s interesting to see the performance of the .NET platform isolated from the performance of the graphics card. In apps/demos/games that use 3D acceleration, expect the difference between managed and unmanaged code to be even smaller, as the bottleneck of rendering is the 3D card, not the CPU.
> With this benchmark, you are measuring the quality of the codegen. The managed version is just a recompile of the unmanaged version with the /clr option (which targets IL instead of x86). It’s not taking into account GCs that happen in an app that does managed allocations, it’s a pure JIT benchmark. This also means that it doesn’t show some problems you may have doing realtime graphics with managed code if you’re not careful, such as dropping frames due to periodic GCs.
> On my P4, the managed Q2 timedemo runs at 63.2 fps, and the native Q2 timedemo runs at 72.8 fps, which means the managed code is performing at 85.6% the speed of native C++ code with VS.2003.
> The original Q2 [and Quake 1] had optimized x86 assembly rasterizers. These were one of the fastest of their time, and they used cunning tricks such as explicitly paralellizing x86 and x87 instructions to achieve maximum speed. For example, the division for perspective correction for the next 8 pixel span was performed in parallel with the actual rendering of the current 8 pixel span, so perspective correction was almost ‘free.’ The C rasterizers this version uses don’t have this property. To compare apples to apples, Vertigo Software compiled their native version with the C rasterizers – i.e., both versions are slower than the original Q2 demo shipped by [Id Software](https://www.idsoftware.com/en). Just for kicks, I compared the managed version with the original assembly optimized version. **The original version gave me 92.5 fps, which means our codegen is generating code with about 70% of the performance of the original hand optimized assembly.** I personally think this is great – especially considering that our codegen has quite a bit of room to improve.
> *

kg-card-end: html

I guess we’ll see how much codegen has improved in .NET 2.0 – from what I hear, performance improvements aren’t a big priority – but **I’ll gladly trade 15 percent of performance to live in a world where NIMDA can’t exist.** That’s a no-brainer.


In his woefully out-of-date blog, David mentions that one of his coding heroes is **Mike Abrash**. All this talk of Quake and performance reminded me of Mike, too. He worked at Microsoft on the graphics subsystem in NT 3.1, and wrote a number of very influential early assembly and graphics programming books. He also worked on the all-assembly graphics architecture of Quake 1, aka “[the last great software rasterizer](http://www.bluesnews.com/abrash/contents.shtml).”


Mike’s not only a true programming God, but an amazing, humble and approachable writer. I remember randomly browsing through his 1994 [Graphics Programming Black Book](http://www.amazon.com/exec/obidos/tg/detail/-/1576101746/qid=1110344883/sr=8-1/ref=sr_8_xs_ap_i1_xgl14/002-1437771-2723220?v=glance&s=books&n=507846) as a *beginning Visual Basic programmer* and being totally engrossed in it, even though it was technically far* above my level. He’s that great of a writer. For a taste, there’s a little snippet of a 2001 article he wrote for Gamasutra in [this archived news post.](http://www.xent.com/FoRK-archive/2001.01/0583.html) Or, you can relive my amazement as you browse through a complete online version of the [Graphics Programming Black Book](https://web.archive.org/web/20050329091504/http://www.byte.com/abrash/). The techniques may be obsolete, but the problem solving he describes so compellingly is truly timeless. Very, very highly recommended.


I wonder what Michael Abrash is up to these days.


*Really, really, REALLY far above my level.

[security](https://blog.codinghorror.com/tag/security/)
[managed code](https://blog.codinghorror.com/tag/managed-code/)
[performance](https://blog.codinghorror.com/tag/performance/)
[software development](https://blog.codinghorror.com/tag/software-development/)
[technology trends](https://blog.codinghorror.com/tag/technology-trends/)
