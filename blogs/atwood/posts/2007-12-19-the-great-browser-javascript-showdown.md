---
title: "The Great Browser JavaScript Showdown"
date: 2007-12-19
url: https://blog.codinghorror.com/the-great-browser-javascript-showdown/
slug: the-great-browser-javascript-showdown
word_count: 766
---

In [The Day Performance Didn’t Matter Any More](https://blog.codinghorror.com/the-day-performance-didnt-matter-any-more/), I found that **the performance of JavaScript improved a hundredfold between 1996 and 2006**. If Web 2.0 is built on a backbone of JavaScript, it’s largely possible only because of those crucial [Moore’s Law performance improvements](https://blog.codinghorror.com/moores-law-in-practical-terms/).


But have we hit a performance wall? **Is it possible for browsers to run JavaScript significantly faster than they do today?** I’ve always thought that just-in-time optimizing (or even compiling) JavaScript was an unexplored frontier in browser technology. And now the landscape has shifted:

1. Apple’s WebKit team [just announced](http://webkit.org/blog/152/announcing-sunspider-09/) a great new JavaScript benchmark, SunSpider.
2. The browser market is [more competitive](https://blog.codinghorror.com/what-if-they-gave-a-browser-war-and-microsoft-never-came/) than it has been in years, with Opera 9.5, Firefox 3, Safari 3, and IE 8 all vying for the coveted default browser position.


Perhaps browser teams will begin to consider JavaScript performance a competitive advantage. The last time I looked for common JavaScript benchmarks, I came away deeply disappointed. That’s why I’m particularly excited by [the SunSpider benchmark](https://web.archive.org/web/20071226160034/http://webkit.org/perf/sunspider-0.9/sunspider.html): it’s remarkably well thought out, easy to run, and comprehensive.


> It’s **based on real code that does interesting things**; both things that the web apps of today are doing, and more advanced code of the sorts we can expect as web apps become more advanced. Very few of the tests could be classed as microbenchmarks.
> It’s **balanced between different aspects of the JavaScript language** – not dominated by just a small handful of different things. In fact, we collected test cases from all over the web, including from other benchmarks. But at the same time, we avoided DOM tests and stuck to the core JavaScript language itself.
> It’s super **easy to run in the browser** or from the command line, so you can test both pure engine performance, and the results you actually get in the browser.
> We included **statistical analysis** so you can see how stable the results you’re getting really are.


Maciej Stachowiak, a member of Apple’s WebKit team, graciously explained what each subsection of the benchmarks do in the comments:

kg-card-begin: html


| 3d | Pure JavaScript computations of the kind you might use to do 3d rendering, but without the rendering. This ends up mostly hitting floating point math and array access. |
| access | Array, object property and variable access. |
| bitops | Bitwise operations, these can be useful for various things including games, mathematical computations, and various kinds of encoding/decoding. It's also the only kind of math in JavaScript that is done as integer, not floating point. |
| controlflow | Control flow constructs (looping, recursion, conditionals). Right now it mostly covers recursion, as the others are pretty well covered by other tests. |
| crypto | Real cryptography code, mostly covers bitwise operations and string operations. |
| date | Performance of JavaScript's "date" objects. |
| math | Various mathematical type computations. |
| regexp | Regular expressions. Pretty self-explanatory. |
| string | String processing, including code to generate a giant "tagcloud", extracting compressed JS code, etc. |


kg-card-end: html

SunSpider is the best JavaScript benchmark I’ve seen, something we desperately need in an era where [JavaScript is the Lingua Franca of the web](https://blog.codinghorror.com/javascript-the-lingua-franca-of-the-web/). I was so excited, in fact, that I ran some quick benchmarks to compare the four major players in the browser market:

- Windows Vista 32-bit
- 4 GB RAM
- dual-core 3.0 GHz Core 2 Duo CPU
- all browser extensions disabled (clean install)


![](https://blog.codinghorror.com/content/images/2025/03/image-183.png)


What surprised me here is that Firefox is substantially slower than IE, once you factor out that wildly anomalous string result. I had to use a beta version of Opera to get something other than invalid (NaN) results for this benchmark, which coincidentally summarizes my opinion of Opera. Great when it works! I expected Opera to do well; it was handily winning JavaScript benchmarks [way back in 2005](https://blog.codinghorror.com/a-need-for-speed-and-silence/). The new kid on the block, Safari, shows extremely well particularly considering that it is running outside its native OS X environment. Kudos to Apple. Well, except for [that whole font thing](https://blog.codinghorror.com/whats-wrong-with-apples-font-rendering/).


If you’re curious how each browser stacked up in each benchmark area, I broke that down, too:


![](https://blog.codinghorror.com/content/images/2025/03/image-182.png)


If you need greater detail – including variances – you can [download my complete set of SunSpider 0.9 results as a text file](https://web.archive.org/web/20071223143000/http://www.codinghorror.com/blog/files/sunspider-09-benchmark-results.txt).


If I’ve learned anything from the computer industry, it’s that competition benefits everyone. Here’s hoping that **a great JavaScript browser performance showdown** spurs the browser teams on to better performance in this increasingly crucial area.

[javascript](https://blog.codinghorror.com/tag/javascript/)
[web development](https://blog.codinghorror.com/tag/web-development/)
[browser technology](https://blog.codinghorror.com/tag/browser-technology/)
[performance optimization](https://blog.codinghorror.com/tag/performance-optimization/)
[javascript benchmarks](https://blog.codinghorror.com/tag/javascript-benchmarks/)
