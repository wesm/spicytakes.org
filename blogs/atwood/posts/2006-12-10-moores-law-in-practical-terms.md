---
title: "Moore’s Law in Practical Terms"
date: 2006-12-10
url: https://blog.codinghorror.com/moores-law-in-practical-terms/
slug: moores-law-in-practical-terms
word_count: 414
---

There are two popular [formulations of Moore’s Law](http://en.wikipedia.org/wiki/Moore's_law#Formulations_of_Moore.27s_Law):


> The most popular formulation [of Moore’s Law] is **the doubling of the number of transistors on integrated circuits every 18 months**. At the end of the 1970s, Moore’s Law became known as the limit for the number of transistors on the most complex chips. However, it is also common to cite Moore’s Law to refer to the rapidly continuing advance in computing power per unit cost, because transistor count is also a rough measure of computer processing power.


The number of transistors on a CPU hasn’t actually been doubling every 18 months; it’s been doubling every 24 months. Here’s a graph of [the transistor count](http://en.wikipedia.org/wiki/Transistor_count) of each major Intel x86 chip family release f from 1971 to 2006:


![](https://blog.codinghorror.com/content/images/2025/05/image-437.png)


The dotted line is the predicted transistor count if you doubled the 2,300 transistors from the Intel 4004 chip every two years since 1971.


That’s why I prefer the second, looser definition of Moore’s law: dramatic increases in computing power per unit cost. If you’re a stickler for detail, there’s an extensive investigation of [Moore’s law at Ars Technica](http://arstechnica.com/articles/paedia/cpu/moore.ars) you can refer to.


But how do we correlate Moore’s Law – the inexorable upward spiral of raw transistor counts – with performance in practical terms? Personally, I like to look at benchmarks that use “typical” PC applications, such as SysMark 2004. According to page 14 of [this PDF](https://web.archive.org/web/20070123222855/http://www.bapco.com/techdocs/SYSmark2004WhitePaper.pdf), SysMark 2004 scores are calibrated to a reference system: a Pentium 4 2.0 GHz. The reference system scores 100. **Thus, a system which scores 200 in SysMark 2004 will be twice as fast as the reference system.**


So, what was the first new CPU to *double* the performance of the SysMark 2004 reference system with a perfect 200? The Pentium 4 “Extreme Edition” 3.2 GHz scores 197 on the SysMark 2004 office benchmark in this [set of Tom’s Hardware benchmarks](https://web.archive.org/web/20081003033317/http://www.tomshardware.com/reviews/spring-speed-leap,774-25.html). Let’s compare the release dates of these two CPUs:

kg-card-begin: html


| Pentium 4 2.0 GHz | August 27th, 2001 |
| Pentium 4EE 3.2 GHz | November 3rd, 2003 |


kg-card-end: html

It took **26 months to double real world performance in SysMark 2004**. That tracks almost exactly with the doubling of transistor counts every 24 months.


This isn’t a perfect comparison, since other parts of the PC get faster at different rates. But it’s certainly a good indication that **CPU transistor count is fairly reliable indicator of overall performance.**

[hardware](https://blog.codinghorror.com/tag/hardware/)
[moore's law](https://blog.codinghorror.com/tag/moores-law/)
[transistors](https://blog.codinghorror.com/tag/transistors/)
[cpu](https://blog.codinghorror.com/tag/cpu/)
[integrated circuits](https://blog.codinghorror.com/tag/integrated-circuits/)
