---
title: "Threading, Concurrency, and the Most Powerful Psychokinetic Explosive in the Universe"
date: 2004-12-29
url: https://blog.codinghorror.com/threading-concurrency-and-the-most-powerful-psychokinetic-explosive-in-the-univ/
slug: threading-concurrency-and-the-most-powerful-psychokinetic-explosive-in-the-univ
word_count: 987
---

Back when I was [writing for Tech Report](https://web.archive.org/web/20041204094628/http://www.tech-report.com/reviews/2001q2/tnl/index.x?pg=1), I had an epiphany: **the future of CPU development had to be multiple cores on the same die**. Even in 2001, a simple extrapolation of transistor counts versus time bore this out: what the heck are they going to do with those millions of transistors they can add to chips every year? Increase level two cache to twenty megabytes? Add to that the well known heat and scaling problems of Intel’s “more Ghz, less work per Mhz” Pentium 4 architecture and you’ve got a recipe for both lower clocks and lots of transistors. When you can’t go forward, go sideways: more CPUs on the same die.


Unfortunately, as [Chris Sells](http://www.sellsbrothers.com/) points out, our current languages are extremely poorly suited for the kind of development necessary in a world where CPUs don’t get faster:


> *Because CPU speeds have topped off recently even though I/O speeds continue to increase, Herb Sutter posits that the Moore’s Law *[*free performance lunch is over*](http://www.gotw.ca/publications/concurrency-ddj.htm)*, i.e. no more getting faster software by waiting for the next gen of faster hardware. Instead, we’ll have to write our apps to be a lot more concurrent to take advantage of hyper-threading, multi-core CPUs and multi-CPU machines if we want our apps to continue to run faster.
> What this means to me is that **we’ll have to have much better language-level support for concurrent programming. What we have now sucks. Rocks. Hard.***


Does it suck rocks? Hard? Rick Brewster recently wrote this about the [threading code in Paint.NET](http://blogs.msdn.com/rickbrew/):


> *[Algorithms for splitting rendering work between processors], as well as the thread synchronization that goes with the progressive effect rendering, is **easily the most complex code in Paint.NET.** It’s worth it though because this gives us a huge performance boost when rendering effects.*


You can make a very strong case that, as developers, **we’re pretty screwed if the only way to get more performance out of our apps is to make them heavily multithreaded.** Writing software is hard enough as-is without adding a pinch of “the most complex code in our app” throughout... your app. The best treatment of the perils of threading I’ve found is in Dan Appleman’s book, [Moving to VB.NET](http://www.desaware.com/products/books/net/movingtovbnet/index.aspx): Strategies, Concepts, and Code:


> *In his classic science fiction novel, *[*The Stars My Destination*](http://www.amazon.com/exec/obidos/tg/detail/-/0679767800/qid=1104391826/)*, Alfred Bester describes a psychokinetic explosive called PyrE – so powerful that a single grain of it can blow up a house. And all that is needed for it to blow up is for anyone to just think at it and want it to explode. The hero of the story has to decide whether to keep it locked up and secret or to spread it around the planet leaving the fate of the world in the hands and thoughts of every single person on earth.
> Which brings us to multithreading.
> It’s a useful technology – one that has the potential to improve your application’s real (or perceived) performance. **But it is the software equivalent of a nuclear device because if it is used incorrectly, it can blow up in your face. No – worse than that – used incorrectly, it can destroy your reputation and your business because it has nearly infinite potential to increase your testing and debugging costs.**
> Multithreading in VB.NET scares me more than any other new feature. And as is the case with a number of new .NET technologies, the reason for this has to do with human factors as much as with technology.
> Several months before the .NET PDC preview, I was doing a session with Bill Storage at a VBits conference. I asked the audience, which consisted of fairly experienced Visual Basic programmers, whether they wanted free threading in the next version of Visual Basic. Almost without exception, their hands quickly went up. I then asked how many of them actually understood what they were asking for. Only a few hands were raised and there were knowing smiles on the faces of those individuals.
> I’m afraid of multithreading in VB.NET because Visual Basic programmers have little in their experience to prepare them for designing and debugging free-threaded applications VB6 provides enormous protection (along with severe limits) in its implementation of multithreading. The only way to use free threading safely is to understand it and to design your applications correctly.
> Again, I stress, design your applications correctly. If your design is incorrect, it will be virtually impossible to patch up the problems later. And again, the potential cost to fix threading problems has no upper limit.
> I’ve always felt that it’s my responsibility as an author to not only teach technology but to put it into context and help readers choose the right technology to solve their problems. Because multithreading is such a serious issue, I’ve decided to take a somewhat unusual approach in teaching it. **Instead of focusing on the benefits of multithreading and why you would want to use it, I’m going to start by doing my best to help you gain a healthy respect for the technology and the kinds of problems you will run into.** Only towards the end of this chapter, once you understand how to use multithreading, will I discuss scenarios where it is advisable to use it.*


This book is written for VB developers, however, I believe Dan’s cautionary tale applies to virtually all developers currently working in Windows. Programming with threads is hard because:

- our current programming models don’t deal with concurrency well
- most of the programming we do is linear in nature
- programmers have a hard time thinking in terms of events than can interrupt each other at any time


While threading can – and should – be made easier in .NET 2.0, I seriously doubt programmers can adapt to a concurrent world without deeper, more radical changes.

[multithreading](https://blog.codinghorror.com/tag/multithreading/)
[concurrency](https://blog.codinghorror.com/tag/concurrency/)
[cpu development](https://blog.codinghorror.com/tag/cpu-development/)
[transistor technology](https://blog.codinghorror.com/tag/transistor-technology/)
[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
