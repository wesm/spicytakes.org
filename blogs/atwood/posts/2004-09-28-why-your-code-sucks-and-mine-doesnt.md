---
title: "Why Your Code Sucks... and Mine Doesn’t"
date: 2004-09-28
url: https://blog.codinghorror.com/why-your-code-sucks-and-mine-doesnt/
slug: why-your-code-sucks-and-mine-doesnt
word_count: 296
---

OK, the title is just, [Why Your Code Sucks](http://www.artima.com/weblogs/viewpost.jsp?thread=71730), but you know you were thinking it. The article may not be as grammatically (sp) correct as I would like, but it’s got some solid advice. My favorite is rejection of dogma:


> ***Your code sucks if it dogmatically conforms to a trendy framework at the cost of following good design and implementation practices.**
> For example, Bob Martin recently raised the issue of dogmatically using private fields and getters/setters for a simple data structure (e.g., a DTO). If a field is transparently readable and writable why not simply make the field public? In most languages you can do that. Granted, in some you can’t. For example, traditionally in Smalltalk all fields are private and all methods are public.
> In general it’s a good thing whenever you can throw out, or avoid writing, some code. Using a heavy framework generally requires that you must write a significant amount of code that has no business value. There are a variety of lightweight frameworks for Java that are a response to the heavyweight frameworks (e.g., EJB) that have become matters of dogma lately. O’Reilly has a new book out on this topic, coauthored by Bruce Tate.
> When making framework decisions, consider if a lighter framework will do the required job. Using something like Hibernate, Prevayler, Spring, PicoContainer, NakedObjects, etc. can be a real win in many situations. Never blindly adopt a heavy framework just because it’s the current bandwagon. Likewise, don’t blindly adopt a lightweight framework in defiance. Always give due consideration to your choices.*


Of course, the *real* problem with software development is the users. It’s unbelievable. They’ve caused problems with every program I’ve ever written.

[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[technical practices](https://blog.codinghorror.com/tag/technical-practices/)
[software design](https://blog.codinghorror.com/tag/software-design/)
[frameworks](https://blog.codinghorror.com/tag/frameworks/)
