---
title: ".NET Compiler Performance"
date: 2004-02-17
url: https://blog.codinghorror.com/net-compiler-performance/
slug: net-compiler-performance
word_count: 262
---

After working with VB6 and “classic” ASP for so long, I got spoiled with effectively nonexistent compile times. Part of that, of course, is due to how old the environments are – or were. I remember using VB5 shortly after its release on Pentium 1 class hardware, and it wasn’t what I would call ‘fast’ either.


If you’re curious, as I was, about which of the current CPU generation is fastest at VS.NET compilation, check out [this page at Xbit Labs](https://web.archive.org/web/20040618184918/https://www.xbitlabs.com/articles/cpu/display/prescott-tests_13.html). Very interesting. It’s quite rare for a CPU roundup to perform any benchmarks related to development.


It’s technically a C++ eMule client compiled using the latest VS.NET – so probably not managed code, but I assume the results would be similar to a large, managed C# or VB.NET project.


![](https://blog.codinghorror.com/content/images/2025/06/image-59.png)


The Athlon 64 is absolutely mopping the floor with everything else. I think L2 cache is clearly a factor – look at the results of the P4 extreme edition with 2mb L2 cache – but the on-die memory controller must be what gives it the runaway victory. It certainly can’t be clock speed, since the Athlon 64 runs at ~ 2ghz.


The other interesting thing to consider, is that **the fastest CPU compiles debug releases almost twice as fast as the the “slowest” CPU**. And in this case “slowest” is a Pentium 4 3.0ghz, which isn’t exactly chopped liver... depending on how much you compile, and how much your time is worth, an Athlon 64 upgrade could pay for itself in no time. Something to consider.

[.net](https://blog.codinghorror.com/tag/net/)
[compiler](https://blog.codinghorror.com/tag/compiler/)
[performance](https://blog.codinghorror.com/tag/performance/)
[vs.net](https://blog.codinghorror.com/tag/vs-net/)
[compilation](https://blog.codinghorror.com/tag/compilation/)
