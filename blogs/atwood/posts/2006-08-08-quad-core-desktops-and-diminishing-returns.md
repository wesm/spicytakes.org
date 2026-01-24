---
title: "Quad Core Desktops and Diminishing Returns"
date: 2006-08-08
url: https://blog.codinghorror.com/quad-core-desktops-and-diminishing-returns/
slug: quad-core-desktops-and-diminishing-returns
word_count: 593
---

Dual core CPUs were [a desktop novelty](https://blog.codinghorror.com/multiple-core-cpu-futures/) in the first half of 2005. Now, with the introduction of the [Mac Pro](http://www.apple.com/macpro/) (see one [unboxed](https://web.archive.org/web/20061113152052/http://www.powermax.com/articles_reviews/article.php?id=33)), **dual core is officially pass**. Quad core – at least in the form of two dual-core CPUs – is where it’s at for desktop systems.


![](https://blog.codinghorror.com/content/images/2025/04/image-745.png)


And sometime early next year, the first true quad core CPUs will hit the market.


I think there are clear multitasking benefits in a dual-core configuration for typical computer users. All you need to do is run two applications at once, and who doesn’t do that these days?


However, **the benefits from moving to quad-core and beyond are less clear**. Effectively utilizing 4 or 8 CPU cores requires extremely aggressive multithreading support within applications. How aggressive? *Rewrite your entire application in a new language* aggressive. That’s a [much more difficult problem](https://blog.codinghorror.com/threading-concurrency-and-the-most-powerful-psychokinetic-explosive-in-the-univ/). It’s also not a common optimization, except within very specific application niches.


Dual CPU desktop systems weren’t twice as fast as single CPU desktop systems. But they were a substantial, worthwhile speed bump. **With quad CPU systems, we’ve hit the point of diminishing returns.**


Current benchmark data definitely bears this out. I distilled results from these [GamePC](https://web.archive.org/web/20070322090627/http://www.gamepc.com/labs/view_content.asp?id=opteron275&page=8&cookie%5Ftest=1&MSCSProfile=95385A1F52DEA1A229D5B37542054464EA4136EE5EB6A0A9B1096EE2CAE6C0A80619D814A9DB015E9ECEB9DDD91AF8926177A08A4E127E5F8C9E29D20EEA23136E86B91742F91952E41286768D63FA1F3012CAF5535BF21C43D8642B782EB2470393136E8D0330E02CECFAB44A5BBADD62E7F140E532410CDC8AD48B32697B780C33C1299FBE18EE) and [TechReport](https://web.archive.org/web/20061127131556/http://techreport.com/reviews/2005q2/opteron-x75/index.x?pg=6) reviews of the Opteron 275 (dual core 2.2 GHz), which also included the Opteron 247 (single core 2.2 GHz). **It’s an apples-to-apples comparison between Dual and Quad configurations of an Athlon 64 running at the same speed – 2.2 GHz.**

kg-card-begin: html


|  | **Dual CPU** | **Quad CPU** |  |
| 3D Studio Max 7.0 Radiosity Render | 239 | 144 | 1.7 x |
| POV-Ray chess2.pov | 144 | 87 | 1.6 x |
| Cinebench 2003 Rendering | 571 | 1021 | 1.8 x |
| Alias Maya 6.0 Zoo Render | 49 | 43 | 1.1 x |
| Photoshop CS Filter Benchmark | 146 | 131 | 1.1 x |
| Flash MX 2004 MPEG import | 37 | 35 | 1.1 x |
| Windows Media Encoder 9.0 MPEG to WMV | 125 | 119 | 1.1 x |
| Xmpeg/DivX encoding | 71 | 75 | 1.1 x |
| LAME 3.97 WAV to MP3 | 69 | 67 | none |
| Apache 2.0 10k user stress test | 1397 | 1478 | 1.1 x |
| Apache 2.0 50k user stress test | 1346 | 1875 | 1.4 x |
| Sysmark 2004 | 226 | 242 | 1.1 x |
| Half-Life 2: Airboat chase | 95 | 96 | none |
| Doom 3: Site 3 timedemo | 164 | 166 | none |
| 3DMark05 | 5244 | 5244 | none |


kg-card-end: html

I eliminated most of the synthetic benchmarks; I tried to focus on real desktop applications that people actually use. The [Sysmark 2004](https://web.archive.org/web/20061211012148/http://www.bapco.com/products/sysmark2004/) results are particularly telling.


However, the results I did find are so poor that **I wonder if any quad CPU system is good for much more than bragging rights**. Of the desktop apps, only three truly benefit from a quad CPU configuration: 3D Studio Max, POV-Ray, and Cinebench 2003. Notice a pattern? Rendering and encoding tend to parallelize well.


Unless you’re often running a specific application that is optimized for multithreading, there’s no compelling reason to run out and buy a quad-CPU desktop system today. And I don’t see that advice changing over the next few years. At least, not until the state of software development changes quite radically to embrace multithreading across the board.

[multicore processors](https://blog.codinghorror.com/tag/multicore-processors/)
[desktop systems](https://blog.codinghorror.com/tag/desktop-systems/)
[cpu cores](https://blog.codinghorror.com/tag/cpu-cores/)
[multithreading](https://blog.codinghorror.com/tag/multithreading/)
[software optimization](https://blog.codinghorror.com/tag/software-optimization/)
