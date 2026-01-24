---
title: "Unwanted Modeling Language"
date: 2005-05-01
url: https://blog.codinghorror.com/unwanted-modeling-language/
slug: unwanted-modeling-language
word_count: 496
---

If you develop software long enough, you’ll eventually run into Universal Modeling Language. This happened to me last year when we started working with our offshore vendor. UML is a diagramming standard that allows you to model software in a universal way. This could be theoretically be helpful if you were working with a bunch of developers in Bangalore, India. However, it doesn’t take long to conclude that **UML has some serious problems**, even for simple development scenarios. The biggest problem is noted in the [UML Wikipedia entry](http://en.wikipedia.org/wiki/Uml):


> *Although UML is a widely recognized and used standard, it has always been criticized for having **imprecise semantics, which causes its interpretation to be subjective**.*


The last time I checked, programming was about the least subjective human activity on earth. So there’s a huge disconnect. You can’t even get vendors to agree what UML is, as [Martin Fowler points out](http://www.martinfowler.com/bliki/UnwantedModelingLanguage.html):

- Is it a [sketch](http://www.martinfowler.com/bliki/UmlAsSketch.html)?
- Is it a [blueprint](http://www.martinfowler.com/bliki/UmlAsBlueprint.html)?
- Is it a [programming language](http://www.martinfowler.com/bliki/UmlAsProgrammingLanguage.html)?


Fowler appears to be positioning UML as a sort of common whiteboard notation for sketching out preliminary designs prior to coding. Given the tremendous amount of interpretation necessary to decode these diagrams, I tend to agree. Unfortunately, that distinction is lost on a lot of vendors and executives who see it as some kind of perfect, [universal documentation standard](https://web.archive.org/web/20060314231415/http://www.acmqueue.com/modules.php?name=Content&pa=showpage&pid=130&page=8). But it [fails so miserably](http://c2.com/cgi/wiki?UmlControversies=) at this:

1. UML isn’t bidirectional. If the UML changes, the code doesn’t magically write itself. And if the code changes, the UML documents don’t magically update themselves either. So you end up violating the [Don’t Repeat Yourself](http://www.artima.com/intv/dry.html) rule.
2. UML can’t capture many of the high-level details necessary to build software. For example, there’s no way to represent Properties, or Static members. You end up looking at the code anyway because the UML is so imprecise – even at the highest architectural level.
3. UML offers no significant advantage over other forms of documentation. In fact, UML diagrams are typically *worse* than other documentation. I find it much easier to read a typical all-text requirements document than a mish-mash of lines, arrows, and primitive looking stick figures.


I liked the [Pragmatic Programmer](http://www.amazon.com/exec/obidos/ASIN/020161622X/) take on UML:


![](https://blog.codinghorror.com/content/images/2025/05/image-82.png)


> *Workflow can be captured with UML activity diagrams, and conceptual-level class diagrams can sometimes be useful for modeling the business at hand. But true use cases are textual descriptions, with a hierarchy and cross-links. Use cases can contain hyperlinks to other use cases, and they can be nested within each other.
> It seems incredible to us that anyone would seriously consider documenting information this dense using only simplistic stick people such as Figure 7.3. **Don’t be a slave to any notation; use whatever method best communicates the requirements with your audience.***


Microsoft’s “whitehorse” diagramming tools in Visual Studio 2005 – which you can see visually depicted in the [new ClassDesigner WebLog](https://web.archive.org/web/20051125182139/http://blogs.msdn.com/classdesigner/default.aspx) – clearly arrived at the same conclusion.

[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[uml](https://blog.codinghorror.com/tag/uml/)
[modeling languages](https://blog.codinghorror.com/tag/modeling-languages/)
[martin fowler](https://blog.codinghorror.com/tag/martin-fowler/)
