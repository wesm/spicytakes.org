---
title: "Folding: The Death of the General Purpose CPU"
date: 2007-03-23
url: https://blog.codinghorror.com/folding-the-death-of-the-general-purpose-cpu/
slug: folding-the-death-of-the-general-purpose-cpu
word_count: 599
---

A few recent articles have highlighted the disproportionate contribution PlayStation 3 consoles are making to the Folding@Home effort. The [OS statistics page for Folding@Home](https://web.archive.org/web/20080907202608/http://fah-web.stanford.edu/cgi-bin/main.py?qtype=osstats) tells the tale:

kg-card-begin: html


|  | [TFLOPS](http://en.wikipedia.org/wiki/FLOPS) | Active CPUs | Total CPUs |
| Windows | 152 | 160,173 | 1,626,609 |
| Mac/PPC | 7 | 8,776 | 95,435 |
| Mac/Intel | 9 | 2,864 | 7,400 |
| Linux | 43 | 25,239 | 216,067 |
| GPU | 43 | 733 | 2,228 |
| PS3 | 659 | 26,911 | 29,843 |


kg-card-end: html

There are a couple caveats to bear in mind when reading this chart:

1. The measurement of [FLOPS](http://en.wikipedia.org/wiki/FLOPS) isn’t an exact science. It would be more accurate to compare actual work units returned, but I don’t see any way to do that from the folding statistics page.
2. Current PC and Mac / PPC contributors span the entire gamut of CPUs released in the last seven years.
3. Folding does cost money, in the form of electricity. Superior clients offer efficiency: bang per watt. You could make a compelling argument that certain clients with low efficiency aren’t worth the cost of the electricity they’re using. For reference, a [PS3](https://web.archive.org/web/20070329120011/http://www.hardcoreware.net/reviews/review-356-2.htm) and a gaming-class PC both use about 200 watts of power under load.


The PlayStation 3 is indeed dominating the charts; as of this writing, the PS3 is responsible for a whopping 72 percent of the computing power in the entire Folding@Home project.

kg-card-begin: html

UPDATE: as of 3/26/2007, the F@H network has arbitrarily halved the TFLOPS score for the PS3.

kg-card-end: html

![](https://blog.codinghorror.com/content/images/2025/05/image-483.png)


**It’s only a matter of time – a few weeks at most – before the PS3 constitutes more than 95 percent of the computing power in the entire Folding@Home network.** This doesn’t surprise me in the least. The PlayStation 3 can harness the considerable power of its [specialized Cell CPU](http://en.wikipedia.org/wiki/Cell_microprocessor) to crunch work units far more efficiently than any general purpose CPU ever could.


If you look closely at the chart, you’ll see even more powerful evidence of the dominance of specialized processors.


![](https://blog.codinghorror.com/content/images/2025/05/image-484.png)


GPU clients run on modern, high-end video cards. The [GPU on these video cards](https://blog.codinghorror.com/cpu-vs-gpu/) is even more specialized than the Cell processor in the PS3.


The GPU client is limited to the current high-end ATI X1800 and X1900 video cards at the moment, which are already a generation behind NVIDIA’s newest 8800 series. Even so, **the GPU clients are almost 2.5 times faster than the PS3**. Of course, this performance differential is more than balanced by the fact that PS3 is an easily obtainable (albeit somewhat expensive) consumer item; it’s trivially easy to add one to the Folding@Home network, whereas the Folding@Home GPU client is quite immature, and few users have the necessary high-end ATI video cards to use it.


But the *real* lesson of this chart lies in the OS X / Intel data point. Intel-based Macs are, by definition, based on only the newest Intel processors – Core Duo or better. Even so, it’s an utter blowout:

kg-card-begin: html


| Intel Core Duo | 1x |
| PS3 | 7.8x faster |
| GPU | 18.6x faster |


kg-card-end: html

With these kinds of performance ratios – and I expect the performance gap to *widen* every year – **there’s almost no point in adding general purpose CPUs to the folding network any more.** It’s a waste of time, effort, and electricity.


For folding and other distributed computing efforts, it’s **the death of the general purpose CPU as we know it**.

[cuda](https://blog.codinghorror.com/tag/cuda/)
[cpu](https://blog.codinghorror.com/tag/cpu/)
[folding@home](https://blog.codinghorror.com/tag/folding-home/)
[tflops](https://blog.codinghorror.com/tag/tflops/)
[efficiency](https://blog.codinghorror.com/tag/efficiency/)
