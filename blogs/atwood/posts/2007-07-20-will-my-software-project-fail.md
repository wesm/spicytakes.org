---
title: "Will My Software Project Fail?"
date: 2007-07-20
url: https://blog.codinghorror.com/will-my-software-project-fail/
slug: will-my-software-project-fail
word_count: 747
---

[Most software projects fail](https://blog.codinghorror.com/the-long-dismal-history-of-software-project-failure/). But that doesn’t mean yours has to. The first question you should ask is a deceptively simple one: **how big is it?** Steve McConnell explains in [Software Estimation](http://www.amazon.com/exec/obidos/ASIN/0735605351): Demystifying the Black Art:


> [For a software project], size is easily the most significant determinant of effort, cost, and schedule. The kind of software you’re developing comes in second, and personnel factors are a close third. The programming language and environment you use are not first-tier influences on project outcome, but they are a first-tier influence on the estimate.


All other things being equal, large projects tend to fail. That’s probably not news to anyone familiar with [Metcalfe’s Law](http://en.wikipedia.org/wiki/Metcalfe's_law) and [Diseconomies of Scale](https://blog.codinghorror.com/diseconomies-of-scale-and-lines-of-code/).


So if the three most important factors determining the outcome of a software project are...

1. Project size
2. Kind of software being developed
3. Personnel factors


... in that order, what else is left? If you can get those three factors under control – if you’re developing a small, simple CRUD database website with a dream team of tightly gelled superstar developers, are you done? Of course there’s never *any* guarantee of project success, but can you at least say you’ve performed adequate risk management?


I’m not so sure. According to Bill de hra, you also have to consider [the three pillars](https://web.archive.org/web/20071009014025/http://www.dehora.net/journal/2007/01/3_pillars.html):

kg-card-begin: html

> The conclusion I draw from this and my own experience having migrating my fair share of source trees is that **the version control system is a first order effect on software, along with two others – the build system and the bugtracker.**
> Those choices impact absolutely everything else. Things like IDEs, by comparison, don’t matter at all. Even choice of methodology might matter less. Although I’m betting there are plenty of software and management teams out there that see version control, build systems and bugtrackers as being incidental to the work, not mission critical tools.

kg-card-end: html

Bill’s analysis came as a pleasant surprise to me, because it’s exactly the same conclusion I reached while working with [Microsoft’s Team System](http://msdn.microsoft.com/teamsystem/). Once you get the three pillars in place...

1. Version control
2. Work item tracking
3. Build system


... it’s a major improvement in software engineering quality for any software development project. Of course, you don’t have to use Team System to get there, but a *huge* part of the value proposition for Team System is that it’s “software engineering in a box.” It provides tight integration between these three pre-installed pieces, with no complex configuration required.


However you get there, it’s just plain good software engineering to have these essentials – the three pillars – in place before proceeding too far on a software project.


So if we set up our dream team of tightly gelled superstar developers working on our small, simple CRUD database website with an outstanding best-of-breed integrated set of source control, work item tracking, and build tools – are we done? Have we mitigated all the major project risks and set ourselves up to effortlessly, weightlessly [fall into the pit of success](https://web.archive.org/web/20071013094747/http://blogs.msdn.com/brada/archive/2003/10/02/50420.aspx)?


Sadly, no.


Bill notes that choosing a framework [poorly suited to your problem](https://web.archive.org/web/20071008161816/http://www.dehora.net/journal/2007/07/earned_value.html) domain can have a crippling effect on your productivity, too.


> The relative verbosity of programming languages isn’t the interesting thing; nor is typing doctrine. What’s interesting is the culture of frameworks and what different communities deem valuable. My sense of it is that on Java, too many web frameworks – think JSF, or Struts 1.x – consider the Web something you work around using software patterns. The goal is get off the web, and back into middleware. Whereas a framework like Django or Rails is purpose-built for the Web; integrating with the internal enterprise is a non-goal.
> ETag support is just one example; there are so many things frameworks like Rails/Django do ranging from architectural patterns around state management, to URL design, to testing, to template dispatching, to result pagination, right down to table coloring that the cumulative effect on productivity is startling. **I suspect designing for the Web instead of around it is at least as important as language choice.**


So maybe the real lesson here is that software project success isn’t about doing any one particular thing right; it’s the much more daunting task of [not doing anything wrong](https://blog.codinghorror.com/escaping-from-gilligans-island/). It certainly gives you a new appreciation for those rare successful software projects that somehow managed to snatch victory from the jaws of defeat.

[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[project management](https://blog.codinghorror.com/tag/project-management/)
