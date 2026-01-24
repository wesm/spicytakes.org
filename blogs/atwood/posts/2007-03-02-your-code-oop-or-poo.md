---
title: "Your Code: OOP or POO?"
date: 2007-03-02
url: https://blog.codinghorror.com/your-code-oop-or-poo/
slug: your-code-oop-or-poo
word_count: 852
---

I’m not a fan of object orientation for the sake of object orientation. Often the proper OO way of doing things ends up being [a productivity tax](https://blog.codinghorror.com/when-object-oriented-rendering-is-too-much-code/). Sure, objects are the backbone of any modern programming language, but sometimes I can’t help feeling that [slavish adherence to objects](https://blog.codinghorror.com/why-objects-suck/) is making my life a lot more difficult. I’ve always found [inheritance hierarchies](https://blog.codinghorror.com/inherits-nothing/) to be brittle and unstable, and then there’s the massive [object-relational divide](https://blog.codinghorror.com/object-relational-mapping-is-the-vietnam-of-computer-science/) to contend with. OO seems to bring at least as many problems to the table as it solves.


Perhaps Paul Graham [summarized it best](http://www.paulgraham.com/noop.html):


> Object-oriented programming generates a lot of what looks like work. Back in the days of fanfold, there was a type of programmer who would only put five or ten lines of code on a page, preceded by twenty lines of elaborately formatted comments. Object-oriented programming is like crack for these people: it lets you incorporate all this scaffolding right into your source code. Something that a Lisp hacker might handle by pushing a symbol onto a list becomes a whole file of classes and methods. So it is a good tool if you want to convince yourself, or someone else, that you are doing a lot of work.


Eric Lippert observed a similar occupational hazard among developers. It’s something he calls [object happiness](https://web.archive.org/web/20070316124537/http://blogs.msdn.com/ericlippert/archive/2004/03/18/92422.aspx).


> What I sometimes see when I interview people and review code is symptoms of a disease I call Object Happiness. Object Happy people feel the need to apply principles of OO design to small, trivial, throwaway projects. They invest lots of unnecessary time making pure virtual abstract base classes – writing programs where IFoos talk to IBars but there is only one implementation of each interface! I suspect that early exposure to OO design principles divorced from any practical context that motivates those principles leads to object happiness. People come away as OO True Believers rather than OO pragmatists.


I’ve seen so many problems caused by excessive, slavish adherence to OOP in production applications. Not that object oriented programming is inherently bad, mind you, but **a little OOP goes a very long way**. Adding objects to your code is like adding salt to a dish: use a little, and it’s a savory seasoning; add too much and it utterly ruins the meal. Sometimes it’s better to err on the side of simplicity, and I tend to favor the approach that results in *less* code, not *more*.


Given my ambivalence about all things OO, I was amused when [Jon Galloway](http://weblogs.asp.net/jgalloway/) forwarded me a link to [Patrick Smacchia’s web page](http://smacchia.chez-alice.fr/en/Articles.html). Patrick is a French software developer. Evidently the acronym for object oriented programming is spelled a little differently in French than it is in English: POO.


![S.S. Adams gag fake dog poo 'Doggonit'](https://blog.codinghorror.com/content/images/uploads/2007/03/6a0120a85dcdae970b012877700749970c-pi.png)


That’s exactly what I’ve imagined when I had to work on code that abused objects.


But POO code can have another, more constructive, meaning. This blog author argues that OOP pales in importance to POO. [Programming fOr Others](http://a-nickels-worth.blogspot.com/2006/08/eop.html), that is.


> The problem is that programmers are taught all about how to write OO code, and how doing so will improve the maintainability of their code. And by “taught,” I don’t just mean “taken a class or two.” I mean: have pounded into head in school, spend years as a professional being mentored by senior OO “architects” and only then finally kind of understand how to use properly, some of the time. Most engineers wouldn’t consider using a non-OO language, even if it had amazing features. The hype is that major.
> So what, then, about all that code programmers write before their 10 years OO apprenticeship is complete? Is it just doomed to suck? Of course not, as long as they apply other techniques than OO. These techniques are out there but aren’t as widely discussed.
> The improvement [I propose] has little to do with any specific programming technique. It’s more a matter of empathy; in this case, empathy for the programmer who might have to use your code. The author of this code actually thought through what kinds of mistakes another programmer might make, and strove to make the computer tell the programmer what they did wrong.
> In my experience the best code, like the best user interfaces, seems to magically anticipate what you want or need to do next. Yet it’s discussed infrequently relative to OO. Maybe what’s missing is a buzzword. So let’s make one up, Programming fOr Others, or POO for short.


The principles of object oriented programming are far more important than mindlessly, robotically instantiating objects everywhere:

- [Information hiding and encapsulation](http://stevemcconnell.com/ieeesoftware/bp02.htm)
- Simplicity
- Re-use
- Maintainability and empathy


Stop worrying so much about the objects. Concentrate on satisfying the *principles* of object orientation rather than object-izing everything. And most of all, **consider the poor sap who will have to read and support this code after you’re done with it**. That’s why POO trumps OOP: programming as if people mattered will always be a more effective strategy than satisfying the [architecture astronauts](https://blog.codinghorror.com/it-came-from-planet-architecture/).

[object-oriented programming](https://blog.codinghorror.com/tag/object-oriented-programming/)
[oop](https://blog.codinghorror.com/tag/oop/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
