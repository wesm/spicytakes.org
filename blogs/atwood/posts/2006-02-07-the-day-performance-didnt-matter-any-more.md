---
title: "The Day Performance Didn’t Matter Any More"
date: 2006-02-07
url: https://blog.codinghorror.com/the-day-performance-didnt-matter-any-more/
slug: the-day-performance-didnt-matter-any-more
word_count: 788
---

OSNews published a [nine-language performance roundup](http://osnews.com/story.php?news_id=5602&page=3) in early 2004. The results are summarized here:

kg-card-begin: html


|  | **int** | **long** | **double** | **trig** | **I/O** |  |
| Visual C++ | 9.6 | 18.8 | 6.4 | 3.5 | 10.5 | 48.8 |
| Visual C# | 9.7 | 23.9 | 17.7 | 4.1 | 9.9 | 65.3 |
| gcc C | 9.8 | 28.8 | 9.5 | 14.9 | 10.0 | 73.0 |
| Visual Basic | 9.8 | 23.7 | 17.7 | 4.1 | 30.7 | 85.9 |
| Visual J# | 9.6 | 23.9 | 17.5 | 4.2 | 35.1 | 90.4 |
| Java 1.3.1 | 14.5 | 29.6 | 19.0 | 22.1 | 12.3 | 97.6 |
| Java 1.4.2 | 9.3 | 20.2 | 6.5 | 57.1 | 10.1 | 103.1 |
| Python/Psyco | 29.7 | 615.4 | 100.4 | 13.1 | 10.5 | 769.1 |
| Python | 322.4 | 891.9 | 405.7 | 47.1 | 11.9 | 1679.0 |


kg-card-end: html

It’s not a very practical benchmark, but it does tell us a few things. It’s no surprise that C++ is at the head of the pack. But the others aren’t terribly far behind. What I find really interesting, though, is how **most of the languages clump together in the middle**. There’s no significant performance difference between Java and .NET if you throw out the weirdly anomalous trig results.


However, there is one language definitely bringing up the rear – [Python](http://en.wikipedia.org/wiki/Python_programming_language). That’s because it’s an [interpreted language](http://en.wikipedia.org/wiki/Interpreted_language). This is explained in [Code Complete](http://www.amazon.com/exec/obidos/ASIN/0735619670):

kg-card-begin: html

> Interpreted languages tend to exact significant performance penalties because they must process each programming-language instruction before creating and executing machine code. In the performance benchmarking I performed for this chapter and chapter 26, I observed these approximate relationships in performance among different languages:
> **Language**
> **Type of Language**
> **Execution Time Relative to C++**
> C++
> Compiled
> 1:1
> Visual Basic
> Compiled
> 1:1
> C#
> Compiled
> 1:1
> Java
> Byte code
> 1.5:1
> PHP
> Interpreted
> > 100:1
> Python
> Interpreted
> > 100:1

kg-card-end: html

Clearly, the performance penalty for interpreted languages is extreme. How extreme? If you have to ask, *you probably can’t afford it.*


One of the biggest stigmas for early Visual Basic developers was that our code wasn’t compiled. It was interpreted. Interpreted executables were yet another reason so-called “professional” developers didn’t take VB seriously. It was too slow. This finally changed when we got compiled executables in 1997 with VB 5.


The most commonly used interpreted language today, however, is JavaScript. And JavaScript is the very backbone of [Web 2.0](http://www.paulgraham.com/web20.html). How is this feasible if JavaScript is a hundred times slower than Java? Consider this [ancient 1996 JavaScript benchmark page](http://web.archive.org/web/20060630033935/http://www.geocities.com/SiliconValley/7116/jv_bench.html):

kg-card-begin: html


|  | **1996** | **2006** |  |
| primes | 0.15 | 0.02 | 8x |
| pgap | 3.13 | 0.06 | 52x |
| sieve | 5.05 | 0.02 | 252x |
| fib(20) | 2.15 | 0.03 | 72x |
| tak | 10.44 | 0.08 | 131x |
| mb100 | 8.4 | 0.2 | 42x |


kg-card-end: html

In ten years, **JavaScript performance has improved a hundredfold**. But so what, right? Computers get faster every year. Well, our computers are now so fast that – with very few exceptions – *we don’t care how much interpreted code costs any more.*


What many pundits don’t realize is that **the viability of interpreted JavaScript for mainstream applications is a relatively recent development**. Consider [this JavaScript benchmark](http://web.archive.org/web/20060223030711/http://kazdan.com/current/technology/javabenchmark.html) of “ridiculously long algorithms and looping statements.” The top three results are all of 2003 vintage:

kg-card-begin: html


| AMD 1900+ | 1.6 GHz | 12.25 sec |
| P4 Mobile | 2.2 GHz | 15.48 sec |
| P4 Celeron | 1.4 GHz | 17.43 sec |


kg-card-end: html

The slowest computer I own, a 1.2 GHz Pentium M laptop purchased in 2003, completes this test in 13.64 seconds. The one I’m currently typing on completes it in around 7 seconds. So even in the *last three years*, we’ve almost doubled the speed of JavaScript.


I don’t expect this trend of doubling performance to continue. **I think JavaScript is about as fast as it can get now without some kind of really advanced dynamic compilation scheme**. If you [browse the results of BenchJS](https://web.archive.org/web/20060214035707/http://www.24fun.com/downloadcenter/benchjs/benchjs.html), a more recent JavaScript test suite, I think you’ll agree that they’ve plateaued. We might reduce that from 6 seconds to 4 seconds over the next two years, but that’s minor compared to the 100x speedup we’ve already had.

[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[performance benchmarks](https://blog.codinghorror.com/tag/performance-benchmarks/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[interpreted languages](https://blog.codinghorror.com/tag/interpreted-languages/)
[python](https://blog.codinghorror.com/tag/python/)
