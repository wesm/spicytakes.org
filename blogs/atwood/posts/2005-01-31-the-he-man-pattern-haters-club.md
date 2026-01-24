---
title: "The He-Man Pattern Haters Club"
date: 2005-01-31
url: https://blog.codinghorror.com/the-he-man-pattern-haters-club/
slug: the-he-man-pattern-haters-club
word_count: 552
---

Richard Mansfield has a bone to pick [with object oriented programming](https://web.archive.org/web/20050227051032/http://www.devx.com/opinion/Article/26776/0/page/1):


> *Certainly for the great majority of programmers – amateurs working alone to create programs such as a quick sales tax utility for a small business or a geography quiz for Junior – the machinery of OOP is almost always far more trouble than it’s worth. **OOP introduces an unnecessary layer of complexity to procedure-oriented design**. That’s why very few programming books I’ve read use OOP techniques in their code examples. The examples are written as functions, not as methods within objects. Programming books are trying to teach programming – not the primarily clerical and taxonomic essence of OOP. Those few books that do superimpose the OOP mechanisms on their code are, not surprisingly, teaching about the mysteries of OOP itself.*


I am skeptical of [dogmatic adherence to OOP](https://blog.codinghorror.com/why-your-code-sucks-and-mine-doesnt/) myself, but even I did a double-take while reading this article. Is it a parody? I don’t think so, considering he cites an entire website devoted to this subject.* But before (or at least until) you write Mr. Mansfield off as a kook, consider his background:


> *Richard Mansfield has written 32 computer books since 1982, including bestsellers ‘Machine Language for Beginners’ (COMPUTE! Books) and ‘The Second Book of Machine Language’ (COMPUTE! Books). From 1981 through 1987, he was editor of COMPUTE! Magazine and from 1987 to 1991 he was editorial director and partner at Signal Research.*


This is a guy who has written a lot of code. While his opinion veers awfully close to religion, I wouldn’t disregard it altogether. Too many people accept patterns as gospel, so I think a little counter-programming is healthy.


On the other hand, if you think the [Gang of Four](http://c2.com/cgi/wiki?GangOfFour=) is as cool as, well, the [Gang of Four](https://web.archive.org/web/20050207145027/http://www.gillmusic.com/go4_history.html), then you may be interested in this [retrospective on Design Patterns](https://web.archive.org/web/20050301084049/http://www.devx.com/DevX/Article/26782), with comments from a variety of developers.


> *Ten years have passed since Erich Gamma, Richard Helm, Ralph Johnson, and John Vlissides (aka the Gang of Four or GoF) wrote and published *[*Design Patterns*](http://www.amazon.com/exec/obidos/ASIN/0201633612)*: Elements of Reusable Object-Oriented Software. And while most programming books that old are as pass as the technologies they covered or required second and third editions along the way, the GoF’s seminal work still flies off bookshelves, despite being the same text that debuted in the fall of 1994 – an eon ago in Internet time.*


One interesting fact: the most commonly cited patterns were [Singleton](http://c2.com/cgi/wiki?SingletonPattern), [Factory](http://c2.com/cgi/wiki?AbstractFactoryPattern), [Observer](http://c2.com/cgi/wiki?ObserverPattern), and [Command](http://c2.com/cgi/wiki?CommandPattern).


I’m currently reading [Head First Design Patterns](http://www.amazon.com/exec/obidos/ASIN/0596007124), which is basically Design Patterns for Dummies. It’s a good read. But I still feel patterns are more useful as a common design vocabulary than as actual implementation models. It’s kind of damning that **even the radically simplified pattern examples in the book are far more complicated than they need to be**. Would I really design a point of sale system that used the Decorator pattern to represent coffee pricing? I think I’d use a simple relational database table and some procedural code. If I needed to add a topping, I’d simply add a record to the table – no complex objects or inheritance models required.


*As [Damien Katz](https://web.archive.org/web/20050201122623/http://damienkatz.net/) points out, this is the website of a “a megalomaniac nut named Bryce Jacobs,” not the article’s author.

[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[object-oriented programming](https://blog.codinghorror.com/tag/object-oriented-programming/)
