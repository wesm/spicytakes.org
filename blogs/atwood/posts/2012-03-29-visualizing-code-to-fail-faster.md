---
title: "Visualizing Code to Fail Faster"
date: 2012-03-29
url: https://blog.codinghorror.com/visualizing-code-to-fail-faster/
slug: visualizing-code-to-fail-faster
word_count: 643
---

In [What You Can’t See You Can’t Get](https://blog.codinghorror.com/what-you-cant-see-you-cant-get/) I mentioned in passing how frustrated I was that the state of the art in code editors and IDE has advanced so little since 2003. A number of commenters pointed out the amazing [Bret Victor](http://worrydream.com/) talk Inventing on Principle. I hadn’t seen this, but thanks for mentioning it, because I definitely should have. Maybe you haven’t seen it either?


[Bret Victor - Inventing on Principle](https://vimeo.com/906418692) from CUSEC on [Vimeo](https://vimeo.com/).


It’s a bit long at 54 minutes, but worth viewing in its entirety. What Bret shows here is indeed exactly the sort of thing we should be doing, but aren’t.


In some ways we’ve actually regressed from my ancient Visual Basic 6.0 days, when you’d get dynamically notified about errors *as you typed*, not just [when you compiled](https://blog.codinghorror.com/c-and-the-compilation-tax/) or [ran unit tests](https://blog.codinghorror.com/i-pity-the-fool-who-doesnt-write-unit-tests/). The idea that **you should be able to type (or gesture, or speak) and *immediately* see the result of that change** is simple, but extremely powerful. It’s [speed of iteration](https://blog.codinghorror.com/boyds-law-of-iteration/) in the small. That’s essentially the basis for my argument that showing markup and rendered output side-by-side, and dynamically updating them as you type, is vastly superior for learning and experimentation compared to any attempt at WYSIWYG.


But Bret goes further than that – **why not show the effects of predicted changes, and change over time?** Time is the missing element in a static display of code and rendered output; how do we show that?


![](https://blog.codinghorror.com/content/images/2025/04/image-597.png)


Again, watch the video because it’s easier to see in action than it is to explain. But maybe you’d like to play with it yourself? That’s sort of the *point*, isn’t it? As I [wrote in 2007](https://blog.codinghorror.com/dynamic-lightweight-visualization/):


> I yearn for the day when web pages are regularly illustrated with the kind of beautiful, dynamic visualizations that Ben Fry creates.


That day, I’m happy to report, seems to have arrived. Bret’s article, [Up and Down the Ladder of Abstraction](http://worrydream.com/LadderOfAbstraction/) is *extremely* interactive in plain old boring HTML 5.


![](https://blog.codinghorror.com/content/images/2025/04/image-596.png)


Yes, it’s artsy, yes these are mostly toy projects, but this isn’t entirely abstract art house visualization nonsense. Designing tools that let you make rapid changes, and see the *effects* of those changes as soon as possible [can be transformative](http://uxmag.com/articles/you-are-solving-the-wrong-problem).


> Paul realized that what we needed to be solved was not, in fact, human powered flight. That was a red-herring. The problem was the process itself, and along with it the blind pursuit of a goal without a deeper understanding how to tackle deeply difficult challenges. He came up with a new problem that he set out to solve: **how can you build a plane that could be rebuilt in hours not months**. And he did. He built a plane with Mylar, aluminum tubing, and wire.
> The first airplane didn’t work. It was too flimsy. But, because the problem he set out to solve was creating a plane he could fix in hours, he was able to quickly iterate. Sometimes he would fly three or four different planes in a single day. The rebuild, retest, relearn cycle went from months and years to hours and days.
> Eighteen years had passed since Henry Kremer opened his wallet for his vision. Nobody could turn that vision into an airplane. Paul MacCready got involved and changed the understanding of the problem to be solved. Half a year later later, MacCready’s [Gossamer Condor](http://en.wikipedia.org/wiki/Gossamer_Condor) flew 2,172 meters to win the prize. A bit over a year after that, the [Gossamer Albatross](http://en.wikipedia.org/wiki/Gossamer_Albatross) flew across the channel.


Don’t get me wrong, [we’re failing plenty fast](https://blog.codinghorror.com/the-only-truly-failed-project/) with our existing tools. But I can’t shake the feeling that we could we fail even faster if we optimized our IDEs and code editors to better visualize the effects of our changes in real time as we make them.

[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[ide](https://blog.codinghorror.com/tag/ide/)
[user experience](https://blog.codinghorror.com/tag/user-experience/)
