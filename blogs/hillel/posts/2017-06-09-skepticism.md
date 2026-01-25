---
title: "List of Articles about Programming Skepticism"
date: 2017-06-09
url: https://www.hillelwayne.com/post/skepticism/
slug: skepticism
word_count: 1272
---

There are a lot of curated lists out there about good programming resources. One thing they all have in common is that they’re focused on relatively mainstream ideas: good languages, good techniques, etc. I want to try something a little different and focus on the articles that are skeptical about what everybody believes in programming. To keep them “curated”, I tried to make sure that the articles were well-referenced or original research. An article skeptical about standard practice is much more interesting coming from a veteran than an outsider.


Here ares some of the ones I like. Note that I don’t necessarily *agree* with any given article. I just think they’re worth reading.

- [Verification Techniques](http://www.cypherpunks.to/~peter/04_verif_techniques.pdf): I love formal methods. I’ve written a lot about how they are powerful and applicable to everybody, not just high assurance software. Gutmann’s essay on its limitations is like a bucket of ice water: a reminder that we went through the hype before and that there are serious limitations of formal methods that we need to acknowledge if we want to use them well.
- [Static vs Dynamic Typing: a literature review](https://danluu.com/empirical-pl/): Luu consistently writes solid, comprehensive articles that break down common assumptions about programming. This article is one of his best: an extensive analysis of static vs dynaming typing research, which shows there’s no clear evidence one way or another. Note this was written before gradual typing (mypy and typescript) became popular, so it’d be interesting to study those in particular.
- [Scalability! but at what COST?](http://www.frankmcsherry.org/graph/scalability/cost/2015/01/15/COST.html): There’s a difference between performance and scalability, and highly-scalable algorithms are often less performant than smart optimization even for 10+gb datasets.
- [Web Framework Benchmarks](https://www.techempower.com/benchmarks/): A lot of arguments about server performance either come from logical arguments or limited benchmarks. This instead tries to be as comprehensive as possible, running multiple benchmarks across every possible combination of framework, database, platform, etc. Lots of interesting results here: for example, despite the common believe that node is good for high I/O tasks, it’s consistently outperformed by Java and C++.
- [Taking PHP Seriously](https://slack.engineering/taking-php-seriously-cf7a60065329): Slack’s argument about why PHP is, despite all of its misfeatures, a solid language for webdev. It got a lot of traction recently, with a lot of people saying they should be using PHP7 instead. I haven’t been able to find any similar defenses of PHP7, though.
- [In defense of Whiteboarding](https://www.linkedin.com/pulse/20140721195105-42102166-in-defense-of-whiteboard-coding): Whiteboard interview questions are an interesting case: A few years ago, everybody thought they were a great idea, while nowadays everybody thinks they’re terrible. This is the strongest pro-whiteboarding article I could find. It argues that whiteboard questions give useful signals about *creative* thinking, but we never set it up that way.
- [Books Programmers Don’t Really Read](https://web.archive.org/web/20140326194159/http://www.billthelizard.com/2008/12/books-programmers-dont-really-read.html): Fascinating from a cultural perspective: a lot of the books that we consider important are also the books that we don’t read. I’m reminded of some discussions about programming patterns: apparently the book advocates something very different, and much more nuanced, than how we think of patterns today.
- [Disadvantages of purely functional programming](http://flyingfrogblog.blogspot.be/2016/05/disadvantages-of-purely-functional.html): I’m torn on this article, because the tone is pretty hostile (see the ‘smug weenies’ point), but the content is well-grounded. Harrop points at specific data structures that are hard to write in a purely functional language, and lists resources addressing specific claims made that he attempts to debunk.
- [Why should I use a pointer rather than the object itself?](https://stackoverflow.com/questions/22146094/why-should-i-use-a-pointer-rather-than-the-object-itself): Fascinating specifically because it talks about how best practices change over time and have to be reevaluated. In this case, using pointers in early C++ vs C++11.
- [A Practical Comparison of Alloy vs Spin](http://www.pamelazave.com/compare.html): Definitely more niche than the others, but very comprehensive in that niche. Zave compares two specification tools and shows how their claimed benefits are often very different from their actual benefits. Probably only interesting if you’re into lightweight formal methods.


---


So what makes a good skeptical article? Here’s my first pass at defining that, along with “antiexamples” of specific articles which fail to meet the criteria.


#### Controversial


The article should specifically be taking a stance that runs counter to “mainstream views”, either attacking something everybody believes or defending something everybody mocks. Note the article can still be a solid, insightful article without this. It’s just not a solid, insightful *skeptical* article.


*Antiexample*: [PHP: a fractal of bad design](https://eev.ee/blog/2012/04/09/php-a-fractal-of-bad-design/). Even at the time this was written, most people believed that PHP was a badly designed language, so this wasn’t particularly skeptical.


#### Understanding


The article should show a clear understanding (if not respect) of whatever it’s attacking and the arguments against whatever it’s defending. Without this, it’s impossible to write a watertight argument, because you have no idea what you’re arguing against. You’re also much more likely to leave critical holes in your argument.


A rough rule of thumb I have is that if you can’t teach something you other people, you don’t know it well enough to rant about it.


*Antiexample*: [The Dark Path](http://blog.cleancoder.com/uncle-bob/2017/01/11/TheDarkPath.html). Uncle Bob is well-respected for a lot of solid reasons. But his article about type systems shows some basic misunderstandings: for example, that language-level safety features don’t affect the bug-rate, and that tests completely obviate the need for other safety features.1


#### Rigorous


Hard data, if available, should be included and discussed. Hard data showing the *opposite* of what you want should also be included and discussed. If hard data isn’t available but could be generated (for example, benchmarks), it should be generated as objectively as possible. The arguments itself should be rock-solid and not have any implicit assumptions or leaps in logic. All objections should be preemptively discussed in the article.


Of course this is important for any good essay, but it’s especially so for skeptical ones. By definition you’re writing something that a lot of people disagree with, so people are going to write responses. Don’t give them any openings.


*Antiexample*: [Test your private methods](https://medium.com/@hwayne/test-your-private-methods-d697b02706b6). I’m pretty embarassed about having written that article. No concrete examples, poor arguments, and confuses architecture, performance, and testing.


#### Respectful


Unfortunately this is more a nice-to-have than an essential property, which says more about the state of programming culture than how to write a good argument. The article should treat the other side as reasonable, thoughtful people that just happen to be wrong. While you may be attacking their positions, the ultimate goal is to convince and inform people, not antagonize them.


*Antiexample*: [The Case Against Python 3](https://learnpythonthehardway.org/book/nopython3.html). This also lacks comprehension or rigour2, but it’s an extreme example of being obnoxious. Shaw claims that there’s a cabal of Pythonistas brainwashing people, beginners aren’t smart enough to understand him, and that anybody who calls him out is an idiot.


---


It’s really hard to find good skeptical articles. It requires a deep knowledge of both why people believe something and why it breaks down. Plus it’s hard enough to find well-written, well-researched articles in general, even about things that excite people. Research is hard, writing is hard, and rhetoric is hard. Not that I do any better; there’s plenty of programming essays out there I’m embarassed to have written.


I’m always looking for good skeptical articles, so if you have one you like, please send it [my way](https://www.hillelwayne.com/about). I’m particularly interested in articles you *disagree with*, but still think are good.


---

1. Oddly enough, a lot of people have the opposite problem: they argue if you have a strong type system, you don’t need tests.
 [return]
2. In an earlier draft Shaw claimed that Python 3 wasn’t Turing complete. After being [roundly mocked](https://www.reddit.com/r/Python/comments/5efe3t/the_case_against_python_3/dac1i3m/) he backpedaled and said that was a troll.
 [return]
