---
title: "Fifty Years of Software Development"
date: 2006-09-20
url: https://blog.codinghorror.com/fifty-years-of-software-development/
slug: fifty-years-of-software-development
word_count: 1026
---

O’Reilly’s [History of Programming Languages poster](https://web.archive.org/web/20061022152741/http://www.oreilly.com/pub/a/oreilly/news/languageposter_0504.html) is fascinating reading.


![](https://blog.codinghorror.com/content/images/2025/05/image-367.png)


If you trace programming languages back to their origins, you’ll find that **we’ve been at this programming stuff a long, long time.**

- [Fortran](http://en.wikipedia.org/wiki/Fortran) (1954)
- [Cobol](http://en.wikipedia.org/wiki/COBOL) (1959)
- [Lisp](http://en.wikipedia.org/wiki/Lisp_programming_language) (1958)
- [Basic](http://en.wikipedia.org/wiki/BASIC_programming_language) (1964)
- [Forth](http://en.wikipedia.org/wiki/Forth_programming_language) (1970)
- [Pascal](http://en.wikipedia.org/wiki/Pascal_programming_language) (1970)
- [SmallTalk](http://en.wikipedia.org/wiki/Smalltalk) (1971)
- [C](http://en.wikipedia.org/wiki/C_programming_language) (1971)


C is roughly as old as I am; FORTRAN is as old as my parents. But what about the new kids on the block? the TIOBE software [TCPI metrics](https://web.archive.org/web/20061007115635/http://www.tiobe.com/tpci.htm) page provides some data on language popularity going back to the year 2001. Consider the tender age of many of the newest, hippest programming languages:

- [Perl](http://en.wikipedia.org/wiki/Perl) (1987)
- [Python](http://en.wikipedia.org/wiki/Python_programming_language) (1991)
- [Erlang](http://en.wikipedia.org/wiki/Erlang_programming_language) (1991)
- [Ruby](http://en.wikipedia.org/wiki/Ruby_programming_language) (1993)
- [Java](http://en.wikipedia.org/wiki/Java_programming_language) (1995)
- [JavaScript](http://en.wikipedia.org/wiki/JavaScript) (1995)
- [PHP](http://en.wikipedia.org/wiki/PHP) (1995)


Ruby is barely a teenager. JavaScript hasn’t even hit its teens yet.


Now correlate the ages of those modern languages with the publication dates of a few books that represent current thinking in [modern software development](https://blog.codinghorror.com/what-is-modern-software-development/):

kg-card-begin: html


| 1994 | [Object-Oriented Design](http://www.amazon.com/exec/obidos/ASIN/0805353402/) (Booch) |
| 1995 | [Design Patterns](http://www.amazon.com/exec/obidos/ASIN/0201633612/) (GoF) |
| 1997 | [UML Distilled](http://www.amazon.com/exec/obidos/ASIN/0321193687/) (Fowler) |
| 1999 | [Extreme Programming Explained](http://www.amazon.com/exec/obidos/ASIN/0321278658/) (Beck) |
| 1999 | [Refactoring](http://www.amazon.com/exec/obidos/ASIN/0201485672/) (Fowler) |
| 2001 | [Agile Alliance](http://www.agilealliance.org/) is formed |


kg-card-end: html

Modern software development is a recent development. Even though we collectively have over fifty years of experience under our belt, **the profession of software development is still very much in its infancy.**


Consider source control as an example. Source control is the absolute bedrock of software engineering. **I believe that source control was not widely prevalent until 1999**. Here’s why:

1. Although [CVS](http://en.wikipedia.org/wiki/Concurrent_Versions_System) has been around since the late eighties, it was widely popularized through [SourceForge](http://www.sourceforge.net), which didn’t exist until the year 2000.
2. Microsoft’s SourceSafe was available starting in the mid-90s but didn’t hit mainstream acceptance until it was bundled as a part of Visual Studio 6.0 Enterprise in 1998.


Clearly, source control existed before the year 1999. Why did it take so long for this essential tool of software engineering to filter down to the mainstream? The answer lies in the [Redwine-Riddle maturation model](http://www.cs.cmu.edu/~Compose/ftp/shaw-fin-etaps.pdf) (pdf):

kg-card-begin: html

> Redwine and Riddle reviewed a number of software technologies to see how they develop and propagate. **They found that it typically takes 15-20 years for a technology to evolve from concept formulation to the point where it’s ready for popularization.**
> They identify six typical phases:
> Basic research. Investigate basic ideas and concepts, put initial structure on the problem, frame critical research questions.
> Concept formulation. Circulate ideas informally, develop a research community, converge on a compatible set of ideas, publish solutions to specific subproblems.
> Development and extension. Make preliminary use of the technology, clarify
> underlying ideas, generalize the approach.
> Internal enhancement and exploration. Extend approach to another domain,
> use technology for real problems, stabilize technology, develop training materials, show value in results.
> External enhancement and exploration. Similar to internal, but involving a
> broader community of people who weren’t developers, show substantial evidence of value and applicability.
> Popularization. Develop production-quality, supported versions of the technology, commercialize and market technology, expand user community.
> Redwine and Riddle presented timelines for several software technologies as they progressed through these phases up until the mid-1980s. I presented a similar analysis for the maturation of software architecture in the 1990s.

kg-card-end: html

CVS was [released in 1986](http://groups.google.com/groups?:mod.sources.*&ie=UTF-8&c2coff=1&safe=off&selm=122%40mirror.UUCP&rnum=2). It took another fifteen years for CVS usage to become mainstream, *exactly as predicted by Redwine-Riddle*.


The model Redwine-Riddle proposed in 1980 is very much alive today. Mark Dominus, in [Design Patterns of 1972](https://web.archive.org/web/20061017101840/http://newbabe.pobox.com/~mjd/blog/prog/design-patterns.html), reaches back nearly thirty-five years to illustrate **how we’re still struggling to evolve our programming languages today**:


> Had the “Design Patterns” movement been popular in 1960, its goal would have been to train programmers to recognize situations in which the “subroutine” pattern was applicable, and to implement it habitually when necessary. While this would have been a great improvement over not using subroutines at all, it would have been vastly inferior to what really happened, which was that the “subroutine” pattern was codified and embedded into subsequent languages. Identification of patterns is an important driver of progress in programming languages. As in all programming, the idea is to notice when the same solution is appearing repeatedly in different contexts and to understand the commonalities. This is admirable and valuable. The problem with the “Design Patterns” movement is the use to which the patterns are put afterward: programmers are trained to identify and apply the patterns when possible. Instead, the patterns should be used as signposts to the failures of the programming language. As in all programming, the identification of commonalities should be followed by an abstraction step in which the common parts are merged into a single solution.
> Multiple implementations of the same idea are almost always a mistake in programming. The correct place to implement a common solution to a recurring design problem is in the programming language, if that is possible.
> The stance of the “Design Patterns” movement seems to be that it is somehow inevitable that programmers will need to implement Visitors, Abstract Factories, Decorators, and Faades. But these are no more inevitable than the need to implement Subroutine Calls or Object-Oriented Classes in the source language. These patterns should be seen as defects or missing features in Java and C++. **The best response to identification of these patterns is to ask what defects in those languages cause the patterns to be necessary, and how the languages might provide better support for solving these kinds of problems.**


I do think the pace of change in software development is quickening, thanks to exponential increases in communication over the last fifty years – television, satellites, cellular phones, and of course the internet. As software developers, we’ve grown accustomed to computer hardware doubling in speed every 18 months. What we haven’t been able to cope with so well is **how long it takes for the human beings to catch up with the hardware**.

[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[technology trends](https://blog.codinghorror.com/tag/technology-trends/)
[history of programming languages](https://blog.codinghorror.com/tag/history-of-programming-languages/)
