---
title: "The Prototype Pitfall"
date: 2005-04-05
url: https://blog.codinghorror.com/the-prototype-pitfall/
slug: the-prototype-pitfall
word_count: 609
---

Tim Weaver, channeling [Robert Glass](http://www.amazon.com/exec/obidos/ASIN/0321117425/), on [the five laws of prototypes](https://web.archive.org/web/20060219193500/http://dotnetjunkies.com/WebLog/tim.weaver/archive/2004/09/01/23928.aspx):

1. The answer to any prototype / feasibility question is always yes
2. Whatever poor coding practices you use to build your prototype will be replicated in the final production version
3. No matter how poor the performance of the prototype the production version will be much worse
4. Once in production a prototype will never die
5. Any controls used to build the prototype will be used in the production version even if they aren’t appropriate


How do we avoid these prototype pitfalls? According to [The Pragmatic Programmer](http://www.amazon.com/exec/obidos/ASIN/020161622X/), it takes discipline. **Prototypes are designed to be thrown away**. If you can’t bring yourself to throw the prototype away, then stop prototyping and start writing **tracer code**:


> *You might think that this tracer code concept is nothing more than prototyping under an aggressive name. There is a difference. With a prototype, you’re aiming to explore specific aspects of the final system. With a true prototype, you will throw away whatever you lashed together when trying out the concept, and recode it properly using the lessons you’ve learned.
> For example, say you’re producing an application that helps shippers determine how to pack odd-sized boxes into containers. Among other problems, the user interface needs to be intuitive and the algorithms you use to determine optimal packing are very complex.
> You could prototype a user interface for your end users in a GUI tool. You code only enough to make the interface responsive to user actions. Once they’ve agreed to the layout, you might throw it away and recode it, this time with the business logic behind it, using the target language. Similarly, you might want to prototype a number of algorithms that perform the actual packing. You might code functional tests in a high-level, forgiving language such as Perl, and code low-level performance tests in something closer to the machine. In any case, once you’d made your decision, you’d start again and code the algorithms in their final environment, interfacing to the real world. This is prototyping, and it is very useful.
> The tracer code approach addresses a different problem. You need to know how the application as a whole hangs together. You want to show your users how the interactions will work in practice, and you want to give your developers an architectural skeleton on which to hang code. In this case, you might construct a tracer consisting of a trivial implementation of the container packing algorithm (maybe something like first-come, first-served) and a simple but working user interface. Once you have all the components in the application plumbed together, you have a framework to show your users and your developers. Over time, you add to this framework with new functionality, completing stubbed routines. But the framework stays intact, and you know the system will continue to behave the way it did when your first tracer code was completed.
> The distinction is important enough to warrant repeating. Prototyping generates disposable code. Tracer code is lean but complete, and forms part of the skeleton of the final system. Think of prototyping as the reconnaissance and intelligence gathering that takes place before a single tracer bullet is fired.*


Dave and Andy elaborate more on the distinction [between prototypes and tracer code](http://www.artima.com/intv/tracerP.html) in an Artima interview.


I think it might help to develop prototypes in a totally different language or environment. That’d reduce the temptation to code around the prototype. If you don’t have the discipline to **throw away the prototype**, you’re defeating the very purpose of prototyping.

[prototyping](https://blog.codinghorror.com/tag/prototyping/)
[software development](https://blog.codinghorror.com/tag/software-development/)
[coding practices](https://blog.codinghorror.com/tag/coding-practices/)
[performance optimization](https://blog.codinghorror.com/tag/performance-optimization/)
[technical practices](https://blog.codinghorror.com/tag/technical-practices/)
