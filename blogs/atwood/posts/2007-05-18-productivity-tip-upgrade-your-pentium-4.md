---
title: "Productivity Tip: Upgrade Your Pentium 4"
date: 2007-05-18
url: https://blog.codinghorror.com/productivity-tip-upgrade-your-pentium-4/
slug: productivity-tip-upgrade-your-pentium-4
word_count: 432
---

In [C# and the Compilation Tax](https://blog.codinghorror.com/c-and-the-compilation-tax/), several commenters noted that they have “fast dual-core computers,” and yet background compilation performance was unsatisfactory for them on large projects. It’s entirely possible that this is Visual Studio’s fault. However, I’d like to point out that **not all dual core computers are created equal**. Not by a long shot.


Take a look at this [Visual C++ compilation benchmark](https://web.archive.org/web/20070630142828/http://www.digit-life.com/articles2/cpu/intel-core2-duo-e6600.html). Details of the benchmark methodology are available on [this page](https://web.archive.org/web/20070623100651/http://www.digit-life.com/articles2/cpu/method-2006-2-0-rc.html), but for now let’s assume this is typical compilation performance in a typical IDE. **The baseline score of 100 represents a 2.6 GHz Pentium D 805 CPU**.


![Visual C++ Compilation time CPU benchmark results](https://blog.codinghorror.com/content/images/uploads/2007/05/6a0120a85dcdae970b0120a86d9c00970b-pi.png)


Clearly the [multiple core future](https://blog.codinghorror.com/multiple-core-cpu-futures/) has already arrived – every CPU you see here is a dual-core model. Many Pentium 4 models come in dual-core flavor.


The CPU at the bottom of the benchmark results isn’t just any garden variety Pentium 4, though. It’s the [Pentium 965 “Extreme Edition,”](https://web.archive.org/web/20071014115855/http://techreport.com/articles.x/9627/1) the absolute pinnacle of the Pentium 4 CPU family. It’s a 3.73 GHz dual-core, dual-hyperthreaded CPU that originally retailed for almost a thousand dollars. **The *fastest possible* Pentium 4 is nearly 50 percent slower at compilation than a midrange Athlon 64 or Core 2 Duo CPU**. But wait! It gets worse!


Consider [WorldBench - Mozilla 1.4 results](https://web.archive.org/web/20071014115900/http://techreport.com/articles.x/10351/11). The times shown are in seconds; lower scores are better.


![WorldBench - Mozilla 1.4 benchmark CPU results](https://blog.codinghorror.com/content/images/uploads/2007/05/6a0120a85dcdae970b0120a86d9c07970b-pi.png)


Bringing up the rear, by a large margin, are two members of the Pentium 4 CPU family. The 3.6 GHz Pentium D 960 is **almost twice as slow** as the 2.6 GHz Core 2 Duo E6700 in Mozilla.


Perhaps this is why Tech Report called the Pentium 4 “[a] CPU based on a lame-duck microarchitecture.”


If you’re running a Pentium 4 CPU – even a “fast” 3.4 GHz+ dual-core model– you could **more than double your performance** by upgrading to a middle-of-the-road Core 2 Duo CPU. And I’m not talking about meaningless synthetic performance benchmark numbers; I’m talking about performance in real world apps that software developers use every day, meat and potatoes stuff like web browsers and compilers.


If you’re using a Pentium 4 CPU of any kind, consider upgrading at the earliest possible opportunity. Given how much software developers are paid, it makes no economic sense to hobble them with old, slow PCs based on the underperforming Pentium 4 CPU. [Demand your rights](https://blog.codinghorror.com/the-programmers-bill-of-rights/). You can pick up a midrange Core 2 Duo system, sans monitor, for under a thousand dollars. Isn’t the value of your time worth at least that?

[c#](https://blog.codinghorror.com/tag/c-2/)
[visual studio](https://blog.codinghorror.com/tag/visual-studio/)
[pentium 4](https://blog.codinghorror.com/tag/pentium-4/)
[dual-core](https://blog.codinghorror.com/tag/dual-core/)
[cpu benchmark](https://blog.codinghorror.com/tag/cpu-benchmark/)
