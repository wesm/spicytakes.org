---
title: "How Long Would It Take if Everything Went Wrong?"
date: 2006-06-14
url: https://blog.codinghorror.com/how-long-would-it-take-if-everything-went-wrong/
slug: how-long-would-it-take-if-everything-went-wrong
word_count: 428
---

I’m currently reading Steve McConnell’s new book, [Software Estimation](http://www.amazon.com/exec/obidos/ASIN/0735605351): Demystifying the Black Art. The section on individual expert judgment provided one simple reason why my estimates are often so horribly wrong:

kg-card-begin: html

> If you ask a developer to estimate a set of features, the developer will often come back with an estimate that looks like this:
> FeatureEstimated Days
> Alpha1.5
> Bravo1.5
> Charlie2.0
> Delta0.5
> Echo0.5
> Foxtrot0.25
> Golf2.0
> Hotel1.0
> India0.75
> Juliet1.25
> **Total****11.25**
> If you then ask the same developer to reestimate each feature’s best case and worst case, the developer will often return with estimates similar to these:
> FeatureBest Case (days)Worst Case (days)
> Alpha1.252.0
> Bravo1.52.5
> Charlie2.03.0
> Delta0.752.0
> Echo0.51.25
> Foxtrot0.250.5
> Golf1.52.5
> Hotel1.01.5
> India0.51.0
> Juliet1.252.0
> **Total****10.5****18.25**
> When you compare the original single-point estimates to the Best Case and Worst Case estimates, you see that the 11.25 total of the single-point estimates is much closer to the Best Case estimate of 10.5 days than to the Worst Case total of 18.25 days.
> You’ll also notice that both the Best Case and Worst Case estimates are higher than the original single-point estimate. Thinking through the worst case result can sometimes expose additional work that must be done even in the best case, which can raise the nominal estimate. **In thinking through the worst case, I like to ask developers how long the task would take if *everything* went wrong. People’s worst case estimates are often optimistic worst cases rather than *true* worst cases.**

kg-card-end: html

It’s an eye-opening exercise. And I’m ashamed to report that I’ve always used single-point estimates when estimating my work. This is the starting point for many project scheduling disasters, something McConnell refers to as a **Collusion of Optimists**:


> *Considering that optimism is a near-universal fact of human nature, software estimates are often undermined by what I think of as a Collusion of Optimists. Developers present estimates that are optimistic. Executives like the optimistic estimates because they imply that desirable business targets are achievable. Managers like the estimates because they imply that they can support upper management’s objectives. And so the software project is off and running with no one ever taking a critical look at whether the estimates were well founded in the first place*


While it’s impossible to give a perfect estimate, it’s a good idea to start with the worst case scenario and extrapolate backwards to the best case.

[software development](https://blog.codinghorror.com/tag/software-development/)
[estimation](https://blog.codinghorror.com/tag/estimation/)
[project management](https://blog.codinghorror.com/tag/project-management/)
[software engineering](https://blog.codinghorror.com/tag/software-engineering/)
[software estimation](https://blog.codinghorror.com/tag/software-estimation/)
