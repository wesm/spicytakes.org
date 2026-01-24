---
title: "Rethinking Design Patterns"
date: 2007-07-02
url: https://blog.codinghorror.com/rethinking-design-patterns/
slug: rethinking-design-patterns
word_count: 664
---

Many developers consider the book [Design Patterns](http://www.amazon.com/exec/obidos/ASIN/0201633612) a classic.


![](https://blog.codinghorror.com/content/images/2025/05/image-501.png)


So what’s a design pattern?


> A design pattern systematically names, motivates, and explains **a general design that addresses a recurring design problem** in object-oriented systems. It describes the problem, the solution, when to apply the solution, and its consequences. It also gives implementation hints and examples. The solution is a **general arrangement of objects and classes** that solve the problem. The solution is customized and implemented to solve the problem in a particular context.


It’s certainly worthwhile for every programmer to read Design Patterns at least once, if only to learn the [shared vocabulary of common patterns](https://web.archive.org/web/20070805111717/http://www.developer.com/design/article.php/1502691). But I have two specific issues with the book:

1. Design patterns are a form of complexity. As with all complexity, I’d rather see developers focus on simpler solutions *before* going straight to a [complex recipe of design patterns](https://blog.codinghorror.com/head-first-design-patterns/).
2. If you find yourself frequently writing a bunch of boilerplate design pattern code to deal with a “recurring design problem,” that’s *not* good engineering – it’s a sign that [your language is fundamentally broken](https://blog.codinghorror.com/are-design-patterns-how-languages-evolve/).


In his presentation [“Design Patterns” Aren’t](http://perl.plover.com/yak/design/samples/slide001.html), Mark Dominus says **the “Design Patterns” solution is to turn the programmer into a fancy macro processor**. I don’t want to put words in Mark’s mouth, but I think he agrees with at least one of my criticisms.


But Dominus also digs deeper into the source material than most. He cites Christopher Alexander’s book [A Pattern Language](http://www.amazon.com/exec/obidos/ASIN/0195019199), which was the inspiration for Design Patterns.


![](https://blog.codinghorror.com/content/images/2025/05/image-502.png)


Dominus summarizes the book thusly:


> Suppose you want to design a college campus. You must delegate some of the design to the students and professors, otherwise the Physics building won’t work well for the physics people. No architect knows enough about about what physics people need to do it all themselves. But you can’t delegate the design of *every* room to its occupants, because then you’ll get a giant pile of rubble.
> How can you distribute responsibility for design through all levels of a large hierarchy, while still maintaining consistency and harmony of overall design? This is the architectural design problem Alexander is trying to solve, but it’s also a fundamental problem of computer systems development.


That’s the key insight that drives both books. Unfortunately, Dominus believes that the Gang-of-Four version [obstructs Alexander’s message](http://perl.plover.com/yak/design/samples/note.html), replacing actual thought and insight with a plodding, mindless, cut-and-paste code generation template mentality:


> The point of [the talk](http://perl.plover.com/yak/design/) is this: The “design patterns” you get from the Gang-of-Four book are not the same as the idea of “design patterns” that are put forward in Alexander’s books. People say they are, but they aren’t the same thing. Alexander’s idea is a really good one, one that programmers might find useful. But very few programmers are going to find out about it, because they think they already know what it is. But they actually know this other idea which happens to go by the same name.
> **So (once again) we need to take a fresh look at Christopher Alexander**. Forget what I said about the damn iterator pattern, already.


I know it’s not technically a software development book, but consider [this advice from Don Park](https://web.archive.org/web/20070709080417/http://www.docuverse.com/blog/donpark/2007/07/01/eclipse-as-a-city):


> If [Eclipse](http://www.eclipse.org/) is a boomtown which countless developers and companies continue to pour into, it now looks like LA, tiny downtown surrounded by endless expanse of suburban neighborhoods indistinguishable from each other other than by their names. Although one of the key pioneers behind Eclipse is Eric Gamma, one of the four authors of the infamous Design Patterns book, I feel that not enough attention is being paid to the original concepts that inspired the book, concepts captured in books by Christopher Alexander.


You could read Design Patterns like any number of other software developers before you. But I humbly suggest that you should go deeper and read A Pattern Language, too, because [ideas are more important than code](https://blog.codinghorror.com/ideas-are-more-important-than-code/).

[design patterns](https://blog.codinghorror.com/tag/design-patterns/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[object-oriented programming](https://blog.codinghorror.com/tag/object-oriented-programming/)
