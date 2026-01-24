---
title: "Development is Inherently Wicked"
date: 2004-09-02
url: https://blog.codinghorror.com/development-is-inherently-wicked/
slug: development-is-inherently-wicked
word_count: 560
---

> *Horst Rittel and Melvin Webber defined a “wicked” problem as one that could be clearly defined only by solving it, or by solving part of it*. This paradox implies, essentially, that you have to *“*solve*”* the problem once in order to clearly define it and then solve it again to create a solution that works. This process has been motherhood and apple pie in software development for decades.**** ([Steve McConnell](https://web.archive.org/web/20041221140135/http://www.cc2e.com/docs/Chapter5-Design.pdf))


> *A computer industry adage is that Microsoft does not make a successful product until version 3. Its Windows operating system was not a big success until the third version was introduced in 1990 and, similarly, its Internet Explorer browsing software was lackluster until the third version. *([Seattle Post-Intelligencer](https://web.archive.org/web/20041029113521/http://seattlepi.nwsource.com/business/palm18.shtml))


As far as I’m concerned, all software development can be classified as a [Wicked Problem](https://web.archive.org/web/20041009185103/http://www.poppendieck.com/wicked.htm). It’s far too complex and far too annoyingly micro-complicated to allow for a whole lot of rational planning. I know from personal experience that **I can never get very far without writing code to better understand the problem I am trying to solve.**


I’m not proposing that we all revert to a “code like hell” methodology. But I think it’s incredibly foolish to believe any team of developers, however talented, can plan out an entire project from start to end, foreseeing all the contingencies, emergent problems, and weird-ass edge conditions they’re bound to run into. It’s thinking like this that leads to classic waterfall project catastrophes. Too much up-front planning is counterproductive and potentially disastrous.


Instead, I believe you have to **continuously code throughout the lifecycle of a project** and constantly integrate that development feedback into your planning. The sooner you’ve attempted to solve the problem, the sooner you will have a handle on the problem. I’d even go this far: if you’re not writing code for more than two days at a time, you are putting your project at risk. But you have to write *the right kind of code at the right time*:

- In the beginning: you should be researching, prototyping, evaluating risky and unfamiliar areas. What alternative approaches can be used? What architectures make sense? What third party tools will work? If there are any software packages that perform a similar task, how do they approach this problem?
- In the middle: you will figure out things that obsolete code you’ve already written. Don’t be afraid of this – embrace it. Break stuff. Rebuild it. Refactor it. This is your most productive development phase, as long as you don’t fall into the trap of treating existing code as sacrosanct. You should be first in line to obsolete your own code.
- At the end: have the courage to start saying “no”. Even to yourself, which takes discipline. You have to finish, because you’re never *really* finished – each version is a stepping stone for the next version. Ship something and let users beat on it for a while. The quicker you get a release out, the quicker you can get that critical user feedback to fold into the next version.


There are a lot of different methodologies that cover the same ground. Some people call this [Agile Development](http://www.agilealliance.org/home), [XP](http://www.extremeprogramming.org/), or [SCRUM](http://www.controlchaos.com/). All of these fancy buzzwords have a common ancestor: the classic book [Wicked Problems, Righteous Solutions: A Catalog of Modern Engineering Paradigms](http://www.amazon.com/exec/obidos/ASIN/013590126X/).

[software development](https://blog.codinghorror.com/tag/software-development/)
[programming concepts](https://blog.codinghorror.com/tag/programming-concepts/)
[technical practices](https://blog.codinghorror.com/tag/technical-practices/)
[technology trends](https://blog.codinghorror.com/tag/technology-trends/)
