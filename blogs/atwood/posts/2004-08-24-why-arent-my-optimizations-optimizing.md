---
title: "Why aren’t my optimizations optimizing?"
date: 2004-08-24
url: https://blog.codinghorror.com/why-arent-my-optimizations-optimizing/
slug: why-arent-my-optimizations-optimizing
word_count: 517
---

> *We should forget about small efficiencies, say about 97% of the time: premature optimization is the root of all evil. –* [Donald Knuth](https://en.wikipedia.org/wiki/Donald_Knuth)


Michael Teper’s blog has a great post about a bread and butter [optimization scenario involving string replacement](http://michaelteper.com/archive/2004/06/14/173.aspx). After implementing three logical alternatives, Mike looks at the benchmark runs and asks:


> *Why aren’t my optimizations optimizing?*


Optimizing code is a tricky business. I would have tried the exact same things – probably in the same order. Many times approaches I just assume will be “faster” turn out not to be. That’s why I tell developers, **always measure performance**. Never assume anything will be faster or slower until you’ve actually measured it to be so – you’ll be surprised how often your assumptions are wrong. Unfortunately, **sometimes the way you measure performance can even be flawed. **That’s what revealed [Mike’s third optimization](http://michaelteper.com/archive/2004/06/14/174.aspx), was, in fact, an optimization:


> *it turns out that Replace is only fast when the input string does not contain the string (or character) that is intended for replacement. When the string does contain it, the performance of CleanString class drops, and, as expected, the character array exhibits better perf.*


If you must optimize, make sure you’re benchmarking valid test cases, with a reasonable set of test data, to ensure that you actually have an improvement. And before “improving” anything, take the [optimization rules of M.A. Jackson](https://web.archive.org/web/20040827040509/http://cisx2.uma.maine.edu/NickTemp/JSP&JSDLec/jsd.html) to heart:


> Rules of Optimization:
> Rule 1: Don’t do it.
> Rule 2 (for experts only): Don’t do it yet.


And I would add a third: don’t optimize work that doesn’t have to be done. Don’t get me wrong, [performance is incredibly important](http://www.useit.com/papers/responsetime.html?ref=blog.codinghorror.com)...

kg-card-begin: html

> *
>   The basic advice regarding response times has been about the same for almost thirty years [Miller 1968; Card et al. 1991]: *
> **0.1 second** is about the limit for having the user feel that the system is reacting instantaneously, meaning that no special feedback is necessary except to display the result.
> **1 second** is about the limit for the user’s flow of thought to stay uninterrupted, even though the user will notice the delay. Normally, no special feedback is necessary during delays of more than 0.1 but less than 1.0 second, but the user does lose the feeling of operating directly on the data.
> **10 seconds** is about the limit for keeping the user’s attention focused on the dialogue. For longer delays, users will want to perform other tasks while waiting for the computer to finish, so they should be given feedback indicating when the computer expects to be done. Feedback during the delay is especially important if the response time is likely to be highly variable, since users will then not know what to expect.

kg-card-end: html

...but so is having a functioning, stable system. It’s up to you to decide how to balance that. For more, there’s an excellent treatment of this topic in chapter 9 of [Programming Pearls](http://www.amazon.com/exec/obidos/ASIN/0201657880/), and [Microsoft Performance Blogger, Rico](http://blogs.msdn.com/ricom/) is a fun (and .NET specific) read as well.

[optimization](https://blog.codinghorror.com/tag/optimization/)
[software development](https://blog.codinghorror.com/tag/software-development/)
[performance](https://blog.codinghorror.com/tag/performance/)
[benchmarking](https://blog.codinghorror.com/tag/benchmarking/)
[efficiency](https://blog.codinghorror.com/tag/efficiency/)
