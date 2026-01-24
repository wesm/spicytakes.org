---
title: "Head First Design Patterns"
date: 2005-09-05
url: https://blog.codinghorror.com/head-first-design-patterns/
slug: head-first-design-patterns
word_count: 542
---

I’m beginning to wonder if the book [Head First Design Patterns](http://www.amazon.com/exec/obidos/ASIN/0596007124) would be better titled **Ass Backwards Design Patterns**. Here are some quotes from pages 594 and 595 of this 629 page book:


> First of all, when you design, solve things in the simplest way possible. [Your goal should be simplicity](https://blog.codinghorror.com/kiss-and-yagni/), not “how can I apply a pattern to this problem.” Don’t feel like you aren’t a sophisticated developer if you don’t use a pattern to solve a problem. Other developers will appreciate and admire the simplicity of your design. That said, sometimes the best way to keep your design simple and flexible is to use a pattern.
> No one ever talks about when to remove a pattern. You’d think it was blasphemy! Nah, we’re all adults here, we can take it. So when do you remove a pattern? When your system has become complex and the flexibility you planned for isn’t needed. In other words, when a simpler solution without the pattern would be better.
> Design patterns are powerful, and it’s easy to see all kinds of ways they can be used in your current designs. Developers naturally [love to create beautiful architectures](https://blog.codinghorror.com/were-building-the-space-shuttle/) that are ready to take on change from all directions.
> Resist the temptation. If you have a practical need to support change in a design today, go ahead and employ a pattern to handle that change. However, if the reason is only hypothetical, don’t add the pattern. It’s only going to add complexity to your system, and you might never need it.


Filling 593 pages with rah-rah pattern talk, and then tacking this critical guidance on at the end of the book is downright irresponsible. **This advice should be in 72 point blinking Comic Sans on the very first page.**


Beginning developers never met a pattern or an object they didn’t like. Encouraging them to experiment with patterns is like throwing gasoline on a fire. And yet that’s exactly what this book does. Page 597 outlines how therapeutic it is for beginners to abuse patterns:


> The beginner uses patterns everywhere. This is good. The beginner gets lots of experience with and practice using patterns. The beginner also thinks, “The more patterns I use, the better the design.” The beginner will learn that this is not so, that all designs should be as simple as possible. Complexity and patterns should only be used where they are needed for practical extensibility.


Do you really want a junior developer using patterns everywhere? It’s about as safe as encouraging them to “experiment” with a gas-powered chainsaw. The best way to learn to write simple code is to *write simple code!* **Patterns, like all forms of complexity, should be avoided until they are absolutely necessary. **That’s the first thing beginners need to learn. Not the last thing.


The book isn’t the only thing that’s backwards: did you know the Head First girl pictured on the front of the book [leads a shocking double life?](http://fishbowl.pastiche.org/2005/08/12/the_head_first_girls_double_life) That’s right, student by day, [stripper by night](http://www.imdb.com/title/tt0086896/). Ok, maybe not...


![](https://blog.codinghorror.com/content/images/2025/03/image-273.png)


![](https://blog.codinghorror.com/content/images/2025/03/image-272.png)


... but shocking nonetheless. Perhaps they’re referring to the [code smell](http://en.wikipedia.org/wiki/Code_smell) of overcomplicated “explosion at the pattern factory” code this book encourages?

[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[design patterns](https://blog.codinghorror.com/tag/design-patterns/)
[simplicity](https://blog.codinghorror.com/tag/simplicity/)
[flexibility](https://blog.codinghorror.com/tag/flexibility/)
[software design](https://blog.codinghorror.com/tag/software-design/)
