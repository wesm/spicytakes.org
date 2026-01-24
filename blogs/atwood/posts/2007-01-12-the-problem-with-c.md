---
title: "The Problem With C++"
date: 2007-01-12
url: https://blog.codinghorror.com/the-problem-with-c/
slug: the-problem-with-c
word_count: 703
---

MIT’s Technology Review recently interviewed [Bjarne Stroustrup](http://en.wikipedia.org/wiki/Bjarne_Stroustrup) in a two-part article ([part one](https://web.archive.org/web/20070120151529/http://www.technologyreview.com/InfoTech/17831), [part two](https://web.archive.org/web/20070120231943/http://www.technologyreview.com/Infotech/17868/)). You may know Bjarne as the inventor of the [C++ programming language](http://en.wikipedia.org/wiki/C++). Indeed, he even maintains a [comprehensive C++ FAQ](https://web.archive.org/web/20070114025037/http://www.research.att.com/~bs/bs_faq.html) that answers every imaginable C++ question.


Here are a few select quotes from the interview that I found notable:


> C++ has indeed become too “expert friendly” at a time where the degree of effective formal education of the average software developer has declined. However, the solution is not to dumb down the programming languages but to use a variety of programming languages and educate more experts. There has to be languages for those experts to use – and C++ is one of those languages.
> What I did do was to design C++ as first of all a systems programming language: I wanted to be able to write device drivers, embedded systems, and other code that needed to use hardware directly. Next, I wanted C++ to be a good language for designing tools. That required flexibility and performance, but also the ability to express elegant interfaces. My view was that to do higher-level stuff, to build complete applications, you first needed to buy, build, or borrow libraries providing appropriate abstractions. Often, when people have trouble with C++, the real problem is that they don’t have appropriate libraries – or that they can’t find the libraries that are available.
> Other languages have tried to more directly support high-level applications. That works, but often that support comes at the cost of specialization. Personally, I wouldn’t design a tool that could do only what I wanted – I aim for generality.
> I think [making computer languages easier for average people] would be misguided. The idea of programming as a semiskilled task, practiced by people with a few months’ training, is dangerous. We wouldn’t tolerate plumbers or accountants that poorly educated. We don’t have as an aim that architecture (of buildings) and engineering (of bridges and trains) should become more accessible to people with progressively less training. Indeed, one serious problem is that currently, too *many* software developers are undereducated and undertrained.


In the FAQ and the interview, **Bjarne comes off as a little defensive about C++** and its role in [the history of computer languages](https://blog.codinghorror.com/fifty-years-of-software-development/). Maybe that’s because the importance of C++ has diminished over time, principally for two reasons:

1. **C++ is fast but unforgiving.** It was an appropriate solution for an era of limited computing resources. But we’ve long since left that behind; we live in an [era of abundance](http://longtail.typepad.com/the_long_tail/2005/03/the_tragically_.html). We have more computer power than we possibly know what to do with on the desktop. Even the naïve solutions for most computing problems are “fast enough” these days. Computers get faster every day, but programmers’ brains, sadly, do not. It’d be a waste not to trade some of that abundant raw power to make things easier on us. It’s time to evolve up [the one trillion dollar programming pyramid](https://blog.codinghorror.com/the-one-trillion-dollar-development-pyramid/).
2. **C++ is designed for any possible programming task, from the lowest level to the highest.** It makes sense to use C++ to write operating system kernels and device drivers. But when was the last time you used C++ to write a line of business app or website? C++ is perhaps the ultimate generalist language. Because it can do all these things, it’s complicated and [dangerous](http://en.wikipedia.org/wiki/Buffer_overflow). Other languages don’t try to span the entire range of low-level to high-level programming tasks; they simplify to attack a specific high-level problem domain.


C++ is a key historic milestone in the evolution of computer languages. There will always be a place in a programmer’s toolbox for C++, but I’d argue that it’s an increasingly a niche language for a very specific subset of programming tasks. The most important question to ask about any language these days isn’t how fast it is, or how general it is, but **how well does it protect you from yourself? **Stroustrup has a great [quote that says it all](https://web.archive.org/web/20070114025037/http://www.research.att.com/~bs/bs_faq.html#really-say-that):


> C makes it easy to shoot yourself in the foot; C++ makes it harder, but when you do it blows your whole leg off.

[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[c++](https://blog.codinghorror.com/tag/c/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[technical practices](https://blog.codinghorror.com/tag/technical-practices/)
[technology trends](https://blog.codinghorror.com/tag/technology-trends/)
