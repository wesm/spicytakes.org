---
title: "The Noble Art of Maintenance Programming"
date: 2006-06-12
url: https://blog.codinghorror.com/the-noble-art-of-maintenance-programming/
slug: the-noble-art-of-maintenance-programming
word_count: 875
---

Mention the words “maintenance programming” to a group of developers and they’ll, to a man (or woman), recoil in horror. **Maintenance programming is widely viewed as janitorial work**.


![](https://blog.codinghorror.com/content/images/2025/05/image-316.png)


But maybe that’s an unfair characterization.


In [Software Conflict 2.0](http://www.amazon.com/exec/obidos/ASIN/0977213307): The Art and Science of Software Engineering, Robert L. Glass extols the virtues of software maintenance:

kg-card-begin: html

> Software maintenance is...
> **Intellectually complex** – it requires innovation while placing severe constraints on the innovator
> **Technically difficult** – the maintainer must be able to work with a concept and a design and its code all at the same time
> **Unfair** – the maintainer never gets all the things the maintainer needs, such as documentation
> **No-win** – the maintainer only sees people who have problems
> **Dirty work** – the maintainer must work at the grubby level of detailed coding
> **Living in the past** – the code was probably written by someone else before they got good at it
> **Conservative** – the going motto for maintenance is “if it ain’t broke, don’t fix it”
> Software maintenance is pretty complex, challenging stuff.
> In most computing installations, the people who do maintenance tend to be those who are new on the job or not very good at development. There’s a reason for that. Most people would rather do original development; maintenance is too constraining to the creative juices for most people to enjoy doing it. And so by default, the least capable and the least in demand are the ones who most often do the maintenance.
> The status quo is all wrong. Maintenance is a significant intellectual challenge as well as a solution and not a problem. If we want to maximize our effectiveness at doing it, we need to significantly change the way in which we assign people to it.

kg-card-end: html

Perhaps it depends on how you look at your code. According to Andy and Dave, [all programming is maintenance programming](http://www.artima.com/intv/dry.html):


> Dave Thomas: **All programming is maintenance programming, because you are rarely writing original code**. If you look at the actual time you spend programming, you write a bit here and then you go back and make a change. Or you go back and fix a bug. Or you rip it out altogether and replace it with something else. But you are very quickly maintaining code even if it’s a brand new project with a fresh source file. You spend most of your time in maintenance mode. So you may as well just bite the bullet and say, “I'm maintaining from day one.” The disciplines that apply to maintenance should apply globally.
> Andy Hunt: It’s only the first 10 minutes that the code’s original, when you type it in the first time. That’s it.


According to Joel Spolsky, developers are too [lazy to do software maintenance](http://www.joelonsoftware.com/articles/fog0000000069.html):


> We’re programmers. Programmers are, in their hearts, architects, and the first thing they want to do when they get to a site is to bulldoze the place flat and build something grand. We’re not excited by incremental renovation: tinkering, improving, planting flower beds.
> There’s a subtle reason that programmers always want to throw away the code and start over. The reason is that they think the old code is a mess. And here is the interesting observation: they are probably wrong. The reason that they think the old code is a mess is because of a cardinal, fundamental law of programming:
> **It’s harder to read code than to write it.**
> This is why code reuse is so hard. This is why everybody on your team has a different function they like to use for splitting strings into arrays of strings. They write their own function because it’s easier and more fun than figuring out how the old function works.
> As a corollary of this axiom, you can ask almost any programmer today about the code they are working on. “It’s a big hairy mess,” they will tell you. “I’d like nothing better than to throw it out and start over.”


I agree that most developers have an unnatural knee-jerk tendency to rewrite for the sake of rewriting. But other than resisting this urge, I can’t agree with Joel.


It’s a balancing act.

1. **We should probably have our best developers doing software maintenance**, not whoever draws the shortest straw. I’ve seen too many systems devolve into a patchwork of duct tape, spit, and a prayer. Probably because the least experienced and least talented developers are the only ones left to do any maintenance.
2. **At some point, you have to bite the bullet and reset the foundation so you have a stable platform to build on.** If a house’s foundation is unsound, no amount of routine maintenance is going to fix it. Total rewrites like Mozilla and Windows NT may have taken years to get traction, but imagine where open-source browsers – and Microsoft – would be if they hadn’t ever started.


Software maintenance, like Rodney Dangerfield, gets no respect. It’s time we changed that perception. But don’t use maintenance as a crutch for deeper problems, either; renovate fearlessly when the situation calls for it.

[software maintenance](https://blog.codinghorror.com/tag/software-maintenance/)
[software development](https://blog.codinghorror.com/tag/software-development/)
[programming concepts](https://blog.codinghorror.com/tag/programming-concepts/)
[technical practices](https://blog.codinghorror.com/tag/technical-practices/)
[software engineering](https://blog.codinghorror.com/tag/software-engineering/)
