---
title: "Gold Plating"
date: 2004-12-07
url: https://blog.codinghorror.com/gold-plating/
slug: gold-plating
word_count: 532
---

One of McConnell’s [36 classic development project mistakes](https://blog.codinghorror.com/escaping-from-gilligans-island/) is gold-plating. It’s also repeated in the list, so I guess the risk of falling into this particular trap is twice as high:


> *#28: **Requirements gold-plating**. Some projects have more requirements than they need right from the beginning. Performance is stated as a requirement more often than it needs to be, and that can unnecessarily lengthen a software schedule. Users tend to be less interested in complex features than marketing and development are, and complex features add disproportionately to a development schedule.
> #30: **Developer gold-plating**. Developers are fascinated by new technology and are sometimes anxious to try out new features of their language or environment or to create their own implementation of a slick feature they saw in another product – whether or not it’s required in their product. The effort required to design, implement, test, document, and support features that are not required lengthens the schedule.*


As defined by McConnell, gold-plating means adding unnecessary, frivolous features or requirements. This is covered in the book, [Rapid Development](http://www.amazon.com/exec/obidos/ASIN/1556159005/). Gold-plating is a great metaphor for adding artificial value, like cheaply manufactured jewelry.


However, when it comes to [writing code](http://c2.com/cgi/wiki?GoldPlating=), I’m not sure that gold-plating deserves the “classic mistake” moniker. In the purest sense, all refactoring is gold-plating. That is, it consumes extra project time and results in no material benefit for the users. But without periodic and aggressive refactoring, we can’t produce sane, maintainable code. **Where does the refactoring stop, and the gold-plating begin?** Maybe I’m biased, but I can’t recall the last time I’ve excessively gold-plated software by making it simpler and easier to support.


**I also have a hard time criticizing the few developers who care enough to gold-plate their code in the first place**. As alluded to in Dan Appleman's post – by way of Joel Spolsky – [most developers don’t even try](http://www.danappleman.com/index.php?p=31):


> *On one end you have the individual who solves problems. When they have a task or goal, and run into obstacles, they will solve them, overcome them, bypass them, work around, above or right through them, even if it means redefining the problem to do something just as good or better than the original task or goal. These people would, I think, be Joel’s “rosh gadol.”
> On the other end of the spectrum, you have the person who stops at the first excuse. In other words, as soon as the individual as a justifiable reason to stop looking for a solution, they are finished. While this can be intentional (Joel’s example of a “work to rule” situation applies), it is more often just part of their nature. These would be the “rosh katan.”
> There are, sad to day, a lot more of the latter than the former.*


While there is certainly plenty of over-engineered, over-abstracted, gold-plated software out there, it’s far more common to have... pure lead. If you have a developer who is going the extra mile and gold-plating stuff, count yourself lucky. With a bit of direction and focus you could have a developer producing real gold eventually. And that is rare indeed.

[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[project management](https://blog.codinghorror.com/tag/project-management/)
[requirements management](https://blog.codinghorror.com/tag/requirements-management/)
[gold-plating](https://blog.codinghorror.com/tag/gold-plating/)
[software scheduling](https://blog.codinghorror.com/tag/software-scheduling/)
