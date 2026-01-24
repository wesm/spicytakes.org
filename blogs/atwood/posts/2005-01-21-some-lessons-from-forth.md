---
title: "Some Lessons From Forth"
date: 2005-01-21
url: https://blog.codinghorror.com/some-lessons-from-forth/
slug: some-lessons-from-forth
word_count: 516
---

It’s easy to get caught up in the “newer is better” mindset of software development and forget that [ideas are more important than code](https://blog.codinghorror.com/ideas-are-more-important-than-code/). Not everything we do is obsolete in four years. The [Evolution of Forth](http://www.forth.com/resources/evolution/evolve_1_2.html#1.2), which outlines Charles Moore’s guiding principles in creating and implementing the [FORTH](http://en.wikipedia.org/wiki/Forth_programming_language) language, is an excellent illustration of the timelessness of ancient computer wisdom:

1. **Keep it simple**
As the number of capabilities you add to a program increases, the complexity of the program increases exponentially. The problem of maintaining compatibility among these capabilities, to say nothing of some sort of internal consistency in the program, can easily get out of hand. You can avoid this if you apply the Basic Principle. You may be acquainted with an operating system that ignored the Basic Principle. It is very hard to apply. All the pressures, internal and external, conspire to add features to your program. After all, it only takes a half-dozen instructions, so why not? The only opposing pressure is the Basic Principle, and if you ignore it, there is no opposing pressure.
2. **Do not speculate**
Do not put code in your program that might be used. Do not leave hooks on which you can hang extensions. The things you might want to do are infinite; that means that each has 0 probability of realization. If you need an extension later, you can code it later – and probably do a better job than if you did it now. And if someone else adds the extension, will he notice the hooks you left? Will you document this aspect of your program?
3. **Do it yourself**
The conventional approach, enforced to a greater or lesser extent, is that you shall use a standard subroutine. I say that you should write your own subroutines. Before you can write your own subroutines, you have to know how. This means, to be practical, that you have written it before; which makes it difficult to get started. But give it a try. After writing the same subroutine a dozen times on as many computers and languages, you’ll be pretty good at it.


I covered the first two points before in [KISS and YAGNI](https://blog.codinghorror.com/kiss-and-yagni/). Point 3 is more subtle. It seems to fly in the face of [don’t repeat yourself](http://www.artima.com/intv/dry.html), but what he’s really saying – and I agree – is that **you have to make your own mistakes to truly learn**. There’s a world of difference between someone explaining “you should always index your tables because it’s a best practice,” and having your app get progressively slower as records are added to the table.* You learn “why” a lot faster when you’re actually experiencing it instead of passively reading about it.


Moore characterizes **simplicity as a force that must be applied** instead of a passive goal. And he’s right – all too often, I see developers failing to make the hard choices necessary to keep their applications simple. It’s easier to [just say yes](https://blog.codinghorror.com/just-say-no/) to everything.


*You laugh, but I’ve worked with developers who did this.

[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[technical practices](https://blog.codinghorror.com/tag/technical-practices/)
