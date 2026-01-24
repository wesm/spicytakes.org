---
title: "Don’t Go Dark"
date: 2008-06-14
url: https://blog.codinghorror.com/dont-go-dark/
slug: dont-go-dark
word_count: 859
---

Ben Collins-Sussman on [programmer insecurity](http://blog.red-bean.com/sussman/?p=96):

kg-card-begin: html

> What do you do when somebody shows up to an open source project with a gigantic new feature that took months to write? Who has the time to review thousands of lines of code? What if there was a bad design decision made early in the process – does it even make sense to point it out? Dropping code-bombs on communities is rarely good for the project: the team is either forced to reject it outright, or accept it and deal with a giant opaque blob that is hard to understand, change, or maintain. It moves the project decidedly in one direction without much discussion or consensus.
> And yet over and over, I’m gathering stories that point to the fact that programmers *do not want to write code out in the open*. Programmers don’t want their peers to see mistakes or failures. They want to work privately, in a cave, then spring “perfect” code on their community, as if no mistakes had ever been made.
>     I don’t think it’s hubris so much as fear of embarrassment. Rather than think of programming as an inherently social activity, most coders seem to treat it as an arena for personal heroics, and will do anything to protect that myth. They’re fine with sharing code, as long as they present themselves as infallible, it seems. Maybe it’s just human nature.

kg-card-end: html

Ben’s talking about open source development, but this anti-pattern exists in commercial software development, too. The very same phenomenon is documented in Jim McCarthy’s 1995 book [Dynamics of Software Development](http://www.amazon.com/dp/1556158238). It’s presented as Rule #30: **Don’t go dark**.


> You have to manage the granularity of development tasks in such a way that you emerge with visible deliverables over short intervals. In our group, we argue back and forth over how big the intervals should be: five days, ten days, three weeks? **In our world, three weeks is going dark.**
> I don’t know what’s appropriate for your world, but we want team members to have contracts with the other parts of the team so that they surface pretty often with visible components. When somebody surfaces and the deliverable isn’t done, we know right away. We know that this week we slipped one day. That’s worth knowing, much better than getting to the end of the project and observing, “Oh, we slipped six months!” At that point it’s too late to even bother counting up how much you’ve slipped.


Rule #30 is directly followed by a related rule, Rule #31: **Beware of a guy in a room.**


> Specialist developers who lock themselves away in a room, who go dark for long stretches, are anathema to shipping great software on time. No matter how brilliant a developer might be, don’t give the developer a significant assignment unless he or she understands and buys into the type of development program you intend to run. The brilliant developer must be capable of performing on a team, making his work visible in modest increments and subjecting it to scrutiny as it matures. Some people find this intolerable, and although there is a role for people of this disposition in the software world, it is not as a part of a team devoted to shipping great software on time.


This is easier to deal with in the workplace, because you typically have some kind of (theoretically) rational project management in place, and everyone works under the same umbrella. **It’s effectively impossible to go dark if you’re practicing any form of agile software development.** For example, Ron Jeffries borrowed this concept from Jim McCarthy’s book and codified it into [extreme programming lore](https://web.archive.org/web/20071117060759/http://www.xprogramming.com/Practices/PracDark.html). Tasks are always sliced up so they fit into a single iteration, and you never let them spill over into multiple iterations. You’ll always have *something* to show at the end of each iteration. You can’t go dark without quitting the project or, perhaps, your job.


An open source project is a very different animal. It’s a motley collection of widely distributed, loosely coupled volunteers. There’s no project manager breathing down your neck, urging you to break your work into short, shareable increments. **The risk of going dark is severe.** The burden of proof falls on the individual developers, not only to make their work on the project visible in modest increments, but also to get over their code insecurity and share their in-progress code with other people working on the project. How do you expect your fellow coders to take you seriously if you aren’t regularly showing them code? It’s the only form of currency that matters on an open source project.


**Don’t go dark. Don’t be that guy in the room.** Hiding your code until it’s “done” may feel safer, but it isn’t. Sharing your ongoing code with your coworkers is scary, much less the world – but it also results in feedback and communication that will improve your code and draw you closer to the project you’re working on. And isn’t that why we all write code in the first place?

[code review](https://blog.codinghorror.com/tag/code-review/)
[open source](https://blog.codinghorror.com/tag/open-source/)
[programming collaboration](https://blog.codinghorror.com/tag/programming-collaboration/)
[software development practices](https://blog.codinghorror.com/tag/software-development-practices/)
[transparency](https://blog.codinghorror.com/tag/transparency/)
