---
title: "Dependency Avoidance"
date: 2006-01-24
url: https://blog.codinghorror.com/dependency-avoidance/
slug: dependency-avoidance
word_count: 938
---

Have you ever worked with developers that were **charter members of the third-party-control-of-the-month club**? You know the kind – they never met a third party control they didn’t like. They spend all day trolling downloads and experimenting with every tool listed on [The Daily Grind](https://web.archive.org/web/20060126235120/http://www.larkware.com/). Which means deploying your solution is now a tricky balancing act of obtaining and installing the proper license files from a half-dozen different control vendors. Who all do things slightly differently. Oh, and don’t forget to make sure the versions of all your controls are all up to date with the latest bugfixes, too.


These are also the kind of developers who are prone to adopt giant [complex frameworks](https://web.archive.org/web/20060126205511/http://msdn.microsoft.com/practices/) just to get tiny additional bits of functionality. If you’re not careful, your entire project is liable to come down with a severe case of [frameworkitis](https://web.archive.org/web/20060206150506/http://blogs.sun.com/roller/page/swinger?anchor=frameworkitis_and_reuse).


I, on the other hand, think **anything outside the base framework is guilty until proven innocent**. I’ll adopt third-party code, but as little as I can get away with, and *only* if it offers significant, proven benefit to the problem I’m working on. I’ve been burned too many times. My code may suck, but it’s a constant level of sucking that I can plan around.


That’s why I was heartened to read Joel’s account of how the Excel team [aggressively avoids dependencies](http://www.joelonsoftware.com/articles/fog0000000007.html):


> When I was the program manager in charge of the first implementation of Visual Basic for Applications, I put together a careful coalition of four, count them, four different teams at Microsoft to get custom dialog boxes in Excel VBA. The idea was complicated and fraught with interdependencies. There was a team called AFX that was working on some kind of dialog editor. Then we would use this brand new code from the OLE group which let you embed one app inside another. And the Visual Basic team would provide the programming language behind it. After a week of negotiation I got the AFX, OLE, and VB teams to agree to this in principle.
> I stopped by Andrew Kwatinetz’s office. He was my manager at the time and taught me everything I know. “The Excel development team will never accept it,” he said. “**You know their motto? ’Find the dependencies – and eliminate them.’ They'll never go for something with so many dependencies.”**
> In-ter-est-ing. I hadn’t known that. I guess that explained why Excel had its own C compiler.
> By now I’m sure many of my readers are rolling on the floor laughing. “Isn’t Microsoft stupid,” you’re thinking, “they refused to use other people’s code and they even had their own compiler just for one product.”
> Not so fast, big boy! The Excel team’s ruggedly independent mentality also meant that they always shipped on time, their code was of uniformly high quality, and they had a compiler which, back in the 1980s, generated pcode and could therefore run unmodified on Macintosh’s 68000 chip as well as Intel PCs. The pcode also made the executable file about half the size that Intel binaries would have been, which loaded faster from floppy disks and required less RAM.
> “Find the dependencies – and eliminate them.” When you’re working on a really, really good team with great programmers, everybody else’s code, frankly, is bug-infested garbage, and nobody else knows how to ship on time. When you’re a cordon bleu chef and you need fresh lavender, you grow it yourself instead of buying it in the farmers’ market, because sometimes they don’t have fresh lavender or they have old lavender which they pass off as fresh.


The .NET Framework was intended to be **the dependency to end all dependencies**. It’s huge. It’s also comprehensive and generally well-written. Any time you’re reaching outside the framework for a giant swath of functionality, pause first and think about what you’re trying to accomplish. Before you start [stacking dependencies](https://blog.codinghorror.com/respecting-abstraction/) on top of [the mother of all dependencies](http://msdn.microsoft.com/netframework/) itself, make sure what you’re getting justifies that risk.


Is it possible to take dependency avoidance too far? Of course. The flip side of reducing dependencies too aggressively is the [Lava Flow anti-pattern](http://www.antipatterns.com/lavaflow.htm):


> As we delved into it, we interviewed many of the developers concerning certain components of the massive pages of code printed out for us. Over and over again we got the same answer, “I don’t know what that class is for, it was written before I got here.” We gradually realized that between 30 and 50% of the actual code comprising this complex system was not understood or documented by any one currently working on it. Furthermore, as we analyzed it, we learned that the questionable code really served no purpose in the current system, rather it was mostly there from previous attempts or approached by long-gone developers. The current staff, while very bright, was loath to modify or delete code that they didn’t write or didn’t know what it did for fear of breaking something and not knowing why or how to fix it.


I’ve never had a problem with lava flow because I am pathologically addicted to [deleting code](https://blog.codinghorror.com/the-joy-of-deletion/). I’m not afraid to get all [Strunk and White](http://polaris.gseis.ucla.edu/pagre/272/needless.html) on that codebase. I don't care if it woulda, coulda, shoulda been used – *is it being used right now? *No? Then it’s gone. Period. If you need it back, well, that’s why God invented source control systems.


I’m not against dependencies. Everything software developers do is one giant string of dependencies. I’m a pragmatist. **Strive to make your dependency stack as small as you possibly can.**

[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[third-party dependencies](https://blog.codinghorror.com/tag/third-party-dependencies/)
[software architecture](https://blog.codinghorror.com/tag/software-architecture/)
[technical practices](https://blog.codinghorror.com/tag/technical-practices/)
