---
title: "How about an hourly build?"
date: 2004-10-08
url: https://blog.codinghorror.com/how-about-an-hourly-build/
slug: how-about-an-hourly-build
word_count: 865
---

The [benefits of a daily build](https://web.archive.org/web/20041012043856/http://www.stevemcconnell.com/bp04.htm) are well understood by now. McConnell even cites the book [Showstopper!](https://blog.codinghorror.com/showstopper/) as an extreme example circa 1993:


> *Who can benefit from this process? Some developers protest that it is impractical to build every day because their projects are too large. But what was perhaps the most complex software project in recent history used daily builds successfully. By the time it was released, Microsoft Windows NT 3.0 consisted of 5.6 million lines of code spread across 40,000 source files. A complete build took as many as 19 hours on several machines, but the NT development team still managed to build every day. Far from being a nuisance, the NT team attributed much of its success on that huge project to their daily builds. Those of us who work on projects of less staggering proportions will have a hard time explaining why we aren’t also reaping the benefits of this practice.*


I think the main argument against daily builds was, frankly, a technological one – it simply took too long. In this age of [blazingly fast 64-bit processors](https://blog.codinghorror.com/athlon-64-developers-choice/) – and even cool distributed build stuff like [IncrediBuild](http://www.xoreax.com/main.htm) – time should no longer be a factor.


Most of us will never work on a project as large as Windows NT, so our builds should be near-instantaneous. And we should do better than a daily build. **I believe, for all but the largest projects, you should be building multiple times per day.** This is also known as [continuous integration](http://www.extremeprogramming.org/rules/integrateoften.html):


> *Developers should be integrating and releasing code into the code repository every few hours, whenever possible. In any case never hold onto changes for more than a day. Continuous integration often avoids diverging or fragmented development efforts, where developers are not communicating with each other about what can be re-used, or what could be shared. Everyone needs to work with the latest version. Changes should not be made to obsolete code causing integration head aches.*


I’m at the point now that **I get aggravated when other developers leave files checked out overnight**. Perhaps it’s a question of programming style, but I believe your code should almost always be in a compileable state. It may not do much, but it should successfully compile. I strongly believe that an aggressive check-in policy leads to better code. So does [Martin Fowler](http://www.martinfowler.com/articles/continuousIntegration.html):


> *One of the hardest things to express about continuous integration is that makes a fundamental shift to the whole development pattern, one that isn’t easy to see if you’ve never worked in an environment that practices it. In fact most people do see this atmosphere if they are working solo - because then they only integrate with themself. For many people team development just comes with certain problems that are part of the territory. Continuous integration reduces these problems, in exchange for a certain amount of discipline.
> The fundamental benefit of continuous integration is that it removes sessions where people spend time hunting bugs where one person’s work has stepped on someone else’s work without either person realizing what happened. These bugs are hard to find because the problem isn’t in one person’s area, it is in the interaction between two pieces of work. This problem is exacerbated by time. Often integration bugs can be inserted weeks or months before they first manifest themselves. As a result they take a lot of finding.
> With continuous integration the vast majority of such bugs manifest themselves the same day they were introduced. Furthermore it’s immediately obvious where at least half of the interaction lies. This greatly reduces the scope of the search for the bug. And if you can’t find the bug, you can avoid putting the offending code into the product, so the worst that happens is that you don’t add the feature that also adds the bug. (Of course you may want the feature more than you hate the bug, but at least this way it’s an informed choice.)
> Now there’s no guarantee that you get all the integration bugs. The technique relies on testing, and as we all know testing does not prove the absence of errors. The key point is that continuous integration catches enough bugs to be worth the cost.
> The net result of all this is increased productivity by reducing the time spent chasing down integration bugs. While we don’t know of anyone who’s given this anything approaching a scientific study the anecdotal evidence is pretty strong. Continuous Integration can slash the amount of time spent in integration hell, in fact it can turn hell into a non-event.*


I’m not making any conscious effort to use so-called [Extreme Programming](http://www.extremeprogramming.org); my concern is a more practical one. I simply can’t think of any justifiable reason for a developer to hold on to code that long. If you’re writing code that is so broken you can’t check any of it in for more than a day – you might have some bad programming habits. I believe it’s far healthier to grow or accrete your software from a small, functional base and use aggressive daily check-ins to checkpoint those growth stages.

[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[continuous integration](https://blog.codinghorror.com/tag/continuous-integration/)
[technical practices](https://blog.codinghorror.com/tag/technical-practices/)
