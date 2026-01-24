---
title: "The Ferengi Programmer"
date: 2009-02-11
url: https://blog.codinghorror.com/the-ferengi-programmer/
slug: the-ferengi-programmer
word_count: 978
---

There was a little [brouhaha](https://web.archive.org/web/20090211185550/http://blog.objectmentor.com/articles/2009/01/31/quality-doesnt-matter-that-much-jeff-and-joel) recently about [some comments Joel Spolsky made](http://www.joelonsoftware.com/items/2009/01/31.html) on our podcast:


> Last week I was listening to a [podcast on Hanselminutes](http://www.hanselminutes.com/default.aspx?showID=163), with Robert Martin talking about the [SOLID principles](http://butunclebob.com/ArticleS.UncleBob.PrinciplesOfOod). (That’s a real easy-to-Google term!) It’s object-oriented design, and they’re calling it agile design, which it really, really isn’t. It’s principles for how to design your classes, and how they should work. And, when I was listening to them, they all sounded to me like extremely bureaucratic programming that came from the mind of somebody that has not written a lot of code, frankly.


There’s nothing really objectionable about Bob’s object-oriented design principles, on the face of it. (Note that all links in the below table are PDFs, so click accordingly.)

kg-card-begin: html


| [The Single Responsibility Principle](https://web.archive.org/web/20090306160217/http://www.objectmentor.com/resources/articles/srp.pdf) | A class should have one, and only one, reason to change. |
| [The Open Closed Principle](https://web.archive.org/web/20090306160314/http://www.objectmentor.com/resources/articles/ocp.pdf) | You should be able to extend a class's behavior, without modifying it. |
| [The Liskov Substitution Principle](https://web.archive.org/web/20090306160238/http://www.objectmentor.com/resources/articles/lsp.pdf) | Derived classes must be substitutable for their base classes. |
| [The Dependency Inversion Principle](https://web.archive.org/web/20090306160139/http://www.objectmentor.com/resources/articles/dip.pdf) | Depend on abstractions, not on concretions. |
| [The Interface Segregation Principle](https://web.archive.org/web/20090306160252/http://www.objectmentor.com/resources/articles/isp.pdf) | Make fine grained interfaces that are client specific. |
| [The Release Reuse Equivalency Principle](https://web.archive.org/web/20090306160157/http://www.objectmentor.com/resources/articles/granularity.pdf) | The granule of reuse is the granule of release. |
| [The Common Closure Principle](https://web.archive.org/web/20090306160157/http://www.objectmentor.com/resources/articles/granularity.pdf) | Classes that change together are packaged together. |
| [The Common Reuse Principle](https://web.archive.org/web/20090306160157/http://www.objectmentor.com/resources/articles/granularity.pdf) | Classes that are used together are packaged together. |
| [The Acyclic Dependencies Principle](https://web.archive.org/web/20090306160157/http://www.objectmentor.com/resources/articles/granularity.pdf) | The dependency graph of packages must have no cycles. |
| [The Stable Dependencies Principle](https://web.archive.org/web/20090306160327/http://www.objectmentor.com/resources/articles/stability.pdf) | Depend in the direction of stability. |
| [The Stable Abstractions Principle](https://web.archive.org/web/20090306160327/http://www.objectmentor.com/resources/articles/stability.pdf) | Abstractness increases with stability. |


kg-card-end: html

While I do believe every software development team should endeavor to follow the [instructions on the paint can](https://blog.codinghorror.com/are-you-following-the-instructions-on-the-paint-can/), there’s a limit to what you can fit on a paint can. It’s the most basic, most critical information you need to proceed and not make a giant mess of the process. As brief as the instructions on a paint can are, they do represent the upper limit of what most people will realistically read, comprehend, and derive immediate benefit from.


**Expanding from a few guidelines on a paint can into a detailed painting manual is far riskier.** The bigger and more grandiose the set of rules you come up with, the more severe the danger. A few broad guidelines on a paint can begets thirty rules for painting, which begets a hundred detailed principles of painting...


Pretty soon you’ll find yourself believing that every possible situation in software development can be prescribed, *if only you could come up with a sufficiently detailed set of rules!* And, of course, a critical mass of programmers patient enough to read Volumes I - XV of said rules. You’ll also want to set up a few message boards for these programmers to argue endlessly amongst themselves about the meaning and interpretation of the rules.


This strikes me as **a bit like Ferengi programming**.


![](https://blog.codinghorror.com/content/images/2025/04/image-301.png)


The [Ferengi](http://en.wikipedia.org/wiki/Ferengi) are a part of the Star Trek universe, primarily in [Deep Space Nine](http://en.wikipedia.org/wiki/Star_Trek:_Deep_Space_Nine). They’re a race of ultra-capitalists whose every business transaction is governed by [the 285 Rules of Acquisition](http://memory-alpha.org/en/wiki/Rules_of_Acquisition). There’s a rule for every possible business situation – and, inevitably, an interpretation of those rules that gives the Ferengi license to cheat, steal, and bend the truth to suit their needs.


At what point do you stop having a set of basic, reasonable programming guidelines – and start being **a Ferengi programmer, an imperfect manifestation of the ruleset?**


Like James Bach, I’ve found less and [less use for rules](https://web.archive.org/web/20091016082901/http://www.satisfice.com/blog/archives/174) in my career. Not because I’m a self-made genius who [plays by my own rules](https://blog.codinghorror.com/paul-grahams-participatory-narcissism/), mind you, but because I value the skills, experience, and judgment of my team far more than any static set of rules.


> When Ron says there is an [“absolute minimum of practice”](https://web.archive.org/web/20091006061258/http://xprogramming.com/blog/2009/01/30/context-my-foot/) that must be in for an agile project to succeed, I want to reply that I believe there is an absolute minimum of practice needed to have a competent opinion about things that are needed – and that in his post he does not achieve that minimum. I think part of that minimum is to understand what words like “practice” and “agile” and “success” can mean (recognizing they are malleable ideas). Part of it is to recognize that people can and have behaved in agile ways without any concept of agile or ability to explain what they do.
> My style of development and testing is highly agile. I am agile in that I am prepared to question and rethink anything. I change and develop my methods. I may learn from packaged ideas like Extreme Programming, but I never *follow* them. *Following is for novices who are under active supervision*. Instead, I craft methods on a project by project basis, and I encourage other people to do that, as well. **I take responsibility for my choices. That's engineering for adults like us.**


Guidelines, particularly in the absence of experts and mentors, [are useful](https://blog.codinghorror.com/following-instructions-for-dummies/). But there’s also a very real danger of **hewing too slavishly to rulesets**. Programmers are already quite systematic by disposition, so the idea that you can come up with a detailed enough set of rules, and sub-rules, and sub-sub-rules, that you can literally *program yourself* for success with a “system” of sufficient sophistication – this, unfortunately, comes naturally to most software developers. If you’re not careful, you might even slip and [fall into a Methodology](https://blog.codinghorror.com/level-5-means-never-having-to-say-youre-sorry/). Then you’re in *real* trouble.


**Don’t become a Ferengi Programmer.** Rules, guidelines, and principles are gems of distilled experience that should be studied and respected. But they’re never a substitute for thinking critically about your work.

[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[object-oriented design](https://blog.codinghorror.com/tag/object-oriented-design/)
[solid principles](https://blog.codinghorror.com/tag/solid-principles/)
