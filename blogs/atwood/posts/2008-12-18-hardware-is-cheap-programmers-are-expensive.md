---
title: "Hardware is Cheap, Programmers are Expensive"
date: 2008-12-18
url: https://blog.codinghorror.com/hardware-is-cheap-programmers-are-expensive/
slug: hardware-is-cheap-programmers-are-expensive
word_count: 1061
---

Given the [rapid advance of Moore’s Law](https://blog.codinghorror.com/moores-law-in-practical-terms/), **when does it make sense to throw hardware at a programming problem?** As a general rule, I’d say almost *always*.


Consider the [average programmer salary](http://www.payscale.com/research/US/Job=Sr._Software_Engineer_%2F_Developer_%2F_Programmer/Salary) here in the US:


![](https://blog.codinghorror.com/content/images/2025/04/image-245.png)


You probably have several of these programmer guys or gals on staff. I can’t speak to how much your servers may cost, or how many of them you may need. Or, maybe you don’t need any – perhaps all your code executes on your users’ hardware, which is an entirely different scenario. Obviously, situations vary. But even the most rudimentary math will tell you that **it'd take a* massive *hardware outlay to equal the yearly costs of even a modest five person programming team.**


For example, I just bought two very [powerful servers for Stack Overflow](http://blog.stackoverflow.com/2008/12/server-hosting-rent-vs-buy/). Even after accounting for a third backup server and spare hard drives for the RAID arrays, my total outlay is around $5,000. These servers, compared to the ones we’re on now, offer:

- roughly 50% more CPU speed
- 2 to 6 times the memory capacity
- almost twice the disk space (and it’s a faster RAID 10 array)


Under this new hardware regime, we can expect average page response times to improve by about half. All that for *less than one month* of an average programmer’s salary.


I’d say that’s a great deal. A no-brainer, even.


Incidentally, this is also why failing to outfit your (relatively) highly paid programmers with decent equipment as per the [Programmer’s Bill of Rights](https://blog.codinghorror.com/the-programmers-bill-of-rights/) is such a colossal mistake. If a one-time investment of $4,000 on each programmer makes them merely 5% more productive, you’ll break even after the first year. Every year after that you’ve made a profit. Also, having programmers who believe that their employers actually *give a damn about them* is probably a good business strategy for companies that actually want to be around five or ten years from now.


Clearly, **hardware is cheap, and programmers are expensive**. Whenever you’re provided an opportunity to leverage that imbalance, it would be incredibly foolish not to.


Despite the enduring wonder of the yearly parade of newer, better hardware, we’d also do well to remember my all time favorite graph from [Programming Pearls](http://www.amazon.com/exec/obidos/ASIN/0201657880):


![](https://blog.codinghorror.com/content/images/2025/04/image-244.png)


[Everything is fast for small n](https://blog.codinghorror.com/everything-is-fast-for-small-n/). When n gets large, that’s when things start to go sideways. The above graph of an ancient [Trash-80](http://en.wikipedia.org/wiki/TRS-80) clobbering a semi-modern [DEC Alpha](http://en.wikipedia.org/wiki/DEC_Alpha) is a sobering reminder that **the fastest hardware in the world can’t save you from bad code**. More specifically, poorly chosen data structures or algorithms.


It won’t *hurt* to run badly written code on the fastest possible boxes you can throw at it, of course. But if you want tangible performance improvements, you’ll often have to buckle down and optimize the code, too. Patrick Smacchia’s [lessons learned from a real-world focus on performance](https://web.archive.org/web/20081204095704/http://codebetter.com/blogs/patricksmacchia/archive/2008/12/01/lessons-learned-from-a-real-world-focus-on-performance.aspx) is a great case study in optimization.


![](https://blog.codinghorror.com/content/images/2025/04/image-243.png)


Patrick was able to improve [nDepend](http://www.ndepend.com/) analysis performance fourfold, and cut memory consumption in half. As predicted, most of this improvement was algorithmic in nature, but at least half of the overall improvement came from a variety of different optimization techniques. Patrick likens this to his early days writing demo scene code on the Commodore Amiga:


> In the early 90s, I participated in the Amiga demo scene. It’s a great illustration of the idea that **there is always room for better performance**. Every demo ran on the same hardware. It was the perfect incentive for demo developers to produce more and more optimized code. For several years, every month some record was beaten: the number of 3D polygons, the number of sprites, or the number of dots displayed simultaneously at the rate of 50 frames per second. Over a period of a few years, the performance factor obtained was around 50x! Imagine what it means to perform a computation in one second that originally took an entire minute. This massive gain was the result of both better algorithms (with many pre-computations and delegations to sub-chips) and micro-optimizations at assembly language level (better use of the chip registers, better use of the set of instructions).


Patrick achieved outstanding results, but let’s be clear: **optimizing your code is hard**. And sometimes, dangerous. It is not something you undertake lightly, and you’d certainly want your most skilled programmers working on it. To put it in perspective, let’s dredge up a few classic quotes.


> *Rules of Optimization:
> Rule 1: Don’t do it.
> Rule 2 (for experts only): Don’t do it yet.*
> – [M.A. Jackson](http://en.wikipedia.org/wiki/Michael_A._Jackson)
> *More computing sins are committed in the name of efficiency (without necessarily achieving it) than for any other single reason - including blind stupidity.*
> – [W.A. Wulf](http://en.wikipedia.org/wiki/William_Wulf)


Programmers have a tendency to get lost in the details of **optimizing for the sake of optimization**, as I’ve noted before in [Why Aren’t My Optimizations Optimizing?](https://blog.codinghorror.com/why-arent-my-optimizations-optimizing/) and [Micro-Optimization and Meatballs](https://blog.codinghorror.com/micro-optimization-and-meatballs/). If you’re not extremely careful, you could end up spending a *lot* of very expensive development time with very little to show for it. Or, worse, you’ll find yourself facing a slew of new, even more subtle bugs in your codebase.


That’s why I recommend the following approach:

1. Throw cheap, faster hardware at the performance problem.
2. If the application now meets your performance goals, stop.
3. Benchmark your code to identify specifically where the performance problems are.
4. Analyze and optimize the areas that you identified in the previous step.
5. If the application now meets your performance goals, stop.
6. Go to step 1.


Always try to **spend your way out of a performance problem first** by throwing faster hardware at it. It’ll often be a quicker and cheaper way to resolve immediate performance issues than attempting to code your way out of it. Longer term, of course, you’ll do both. You’ll eventually be forced to revisit those deeper algorithmic concerns and design issues with your code that prevent the application from running faster. And the advantage of doing this on new hardware is that you’ll look like an even *bigger* hero when you deliver the double whammy of optimized code running on speedier hardware.


But until the day that Moore’s Law completely gives out on us, one thing’s for sure: **hardware is cheap – and programmers are expensive**.

[hardware](https://blog.codinghorror.com/tag/hardware/)
[programmers](https://blog.codinghorror.com/tag/programmers/)
[moore's law](https://blog.codinghorror.com/tag/moores-law/)
[programming problem](https://blog.codinghorror.com/tag/programming-problem/)
[servers](https://blog.codinghorror.com/tag/servers/)
[cpu speed](https://blog.codinghorror.com/tag/cpu-speed/)
[memory capacity](https://blog.codinghorror.com/tag/memory-capacity/)
