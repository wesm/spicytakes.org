---
title: "Check In Early, Check In Often"
date: 2008-08-20
url: https://blog.codinghorror.com/check-in-early-check-in-often/
slug: check-in-early-check-in-often
word_count: 511
---

I consider this the golden rule of source control:


**Check in early, check in often**.


Developers who work for long periods – and by *long* I mean more than a day – without checking anything into source control are setting themselves up for some serious integration headaches down the line. Damon Poole [concurs](http://damonpoole.blogspot.com/2005/07/check-in-early-and-check-in-often.html):


> Developers often put off checking in. They put it off because they don’t want to affect other people too early and they don’t want to get blamed for breaking the build. But this leads to other problems such as losing work or not being able to go back to previous versions.
> My rule of thumb is “check-in early and often,” but with the caveat that you have access to private versioning. If a check-in is immediately visible to other users, then you run the risk of introducing immature changes and/or breaking the build.


I’d much rather have small fragments checked in periodically than to go long periods with no idea whatsoever what my coworkers are writing. As far as I’m concerned, **if the code isn’t checked into source control, it doesn’t exist**. I suppose this is yet another form of [Don’t Go Dark](https://blog.codinghorror.com/dont-go-dark/); the code is invisible until it exists in the repository in some form.


I’m not proposing developers check in broken code – but I also argue that there’s a big difference between *broken* code and *incomplete* code. Isn’t it possible, perhaps even desirable, to write your code and structure your source control tree in such a way that you can **check your code in periodically as you’re building it?** I’d much rather have empty stubs and basic API skeletons in place than nothing at all. I can integrate my code against stubs. I can do code review on stubs. I can even help you build out the stubs!


But when there’s nothing in source control for days or weeks, and then a giant dollop of code is suddenly dropped on the team’s doorstep – none of that is possible.


Developers that wouldn’t even consider adopting the old-school [waterfall method](http://en.wikipedia.org/wiki/Waterfall_model) of software development somehow have no problem adopting essentially the very same model when it comes to their source control habits.


Perhaps what we need is a model of **software accretion**. Start with a tiny fragment of code that does almost nothing. Look on the bright side – code that does nothing can’t have many bugs! Test it, and check it in. Add one more small feature. Test that feature, and check it in. Add another small feature. Test *that*, and check it in. Daily. Hourly, even. You always have functional software. It may not do much, but it runs. And with every check in it becomes infinitesimally *more *functional.


![](https://blog.codinghorror.com/content/images/2025/04/image-196.png)


If you learn to check in early and check in often, you’ll have ample time for feedback, integration, and review along the way. And who knows – you might even manage to accrete that pearl of final code that you were looking for, too.

[version control](https://blog.codinghorror.com/tag/version-control/)
[source control](https://blog.codinghorror.com/tag/source-control/)
[software development](https://blog.codinghorror.com/tag/software-development/)
[best practices](https://blog.codinghorror.com/tag/best-practices/)
[collaboration](https://blog.codinghorror.com/tag/collaboration/)
