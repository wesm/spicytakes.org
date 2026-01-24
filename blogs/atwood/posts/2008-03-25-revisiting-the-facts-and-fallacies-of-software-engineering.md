---
title: "Revisiting The Facts and Fallacies of Software Engineering"
date: 2008-03-25
url: https://blog.codinghorror.com/revisiting-the-facts-and-fallacies-of-software-engineering/
slug: revisiting-the-facts-and-fallacies-of-software-engineering
word_count: 1198
---

I like to re-read my favorite books every few years, so I brought Robert Glass’ seminal [Facts and Fallacies of Software Engineering](http://www.amazon.com/exec/obidos/ASIN/0321117425) with me on my most recent trip. I thought it was a decent, but imperfect read when I originally bought it in 2004. As I scanned through the introduction and table of contents, I realized that **I’ve written about almost everything in this book by now**.


![](https://blog.codinghorror.com/content/images/2025/04/image-35.png)


I’m not sure I gave Facts and Fallacies its due [on my first read](https://blog.codinghorror.com/the-delusion-of-reuse/).


Simply reciting the various facts and fallacies feels like a zen koan to software engineering. Even without any of the background discussion and explanation in the book, it’s therapeutic to ponder the brief one sentence summaries presented in the table of contents. As you read these, what comes to mind, based on your experience?


**People**

1. The most important factor in software work is the quality of the programmers.
2. The best programmers are up to 28 times better than the worst programmers.
3. Adding people to a late project makes it later.
4. The working environment has a profound impact on productivity and quality.


**Tools and Techniques**

1. Hype (about tools and technology) is a plague on the house of software.
2. New tools and techniques cause an initial *loss* of productivity / quality.
3. Software developers talk a lot about tools, but seldom use them.


**Estimation**

1. One of the two most common causes of runaway projects is poor estimation.
2. Software estimation usually occurs at the wrong time.
3. Software estimation is usually done by the wrong people.
4. Software estimates are rarely corrected as the project proceeds.
5. It is not surprising that software estimates are bad. But we live and die by them anyway!
6. There is a disconnect between software management and their programmers.
7. The answer to a feasibility study is almost always “yes.”


**Reuse**

1. Reuse-in-the-small is a solved problem.
2. Reuse-in-the-large remains a mostly unsolved problem.
3. Reuse-in-the-large works best in families of related systems.
4. Reusable components are three times as hard to build and should be tried out in three different settings.
5. Modification of reused code is particularly error-prone.
6. Design pattern reuse is one solution to the problems of code reuse.


**Requirements**

1. One of the two most common causes of runaway projects is unstable requirements.
2. Requirements errors are the most expensive to fix during production.
3. Missing requirements are the hardest requirements errors to correct.


**Design**

1. Explicit requirements ‘explode’ as implicit requirements for a solution evolve.
2. There is seldom one best design solution to a software problem.
3. Design is a complex, iterative process. Initial design solutions are usually wrong and certainly not optimal.


**Coding**

1. Designer ‘primitives’ rarely match programmer ‘primitives.’
2. COBOL is a very bad language, but all the others are so much worse.


**Error removal**

1. Error removal is the most time-consuming phase of the lifecycle.


**Testing**

1. Software is usually tested at best to the 55 to 60 percent coverage level.
2. 100 percent test coverage is still far from enough.
3. Test tools are essential, but rarely used.
4. Test automation rarely is. Most testing activities cannot be automated.
5. Programmer-created, built-in debug code is an important supplement to testing tools.


**Reviews and Inspections**

1. Rigorous inspections can remove up to 90 percent of errors before the first test case is run.
2. Rigorous inspections should not replace testing.
3. Post-delivery reviews, postmortems, and retrospectives are important and seldom performed.
4. Reviews are both technical and sociological, and both factors must be accommodated.


**Maintenance**

1. Maintenance typically consumes 40 to 80 percent of software costs. It is probably the most important software lifecycle phase.
2. Enhancements represent roughly 60 percent of maintenance costs.
3. Maintenance is a solution – not a problem.
4. Understanding the existing product is the most difficult maintenance task.
5. Better methods lead to *more* maintenance, not less.


**Quality**

1. Quality is a collection of attributes.
2. Quality is *not* user satisfaction, meeting requirements, achieving cost and schedule, or reliability.


**Reliability**

1. There are errors that most programmers tend to make.
2. Errors tend to cluster.
3. There is no single best approach to software error removal.
4. Residual errors will always persist. The goal should be to minimize or eliminate *severe* errors.


**Efficiency**

1. Efficiency stems more from good design than good coding.
2. High-order language code can be about 90 percent as efficient as comparable assembler code.
3. There are tradeoffs between optimizing for time and optimizing for space.


**Research**

1. Many researchers advocate rather than investigate.


I had forgotten how much ground the book covers; it’s a perfect springboard to all the essential topics in software engineering.


I’ve posted on almost every one of these facts in the intervening four years since I originally read them. As I delved into the table of contents presented above, I could barely contain myself. I remembered and mentally checked each post off the list as I went: check, check, check. I’ve been accused of gratuitous self-linking in the past, so I won’t clutter up the rules with dozens of links to my old posts on these topics. If you’re interested, you can find it. That’s sort of the point.


If those are the fifty-five facts, then these are the **ten fallacies** presented at the end. Fallacies have the *ring* of truth, but upon closer inspection, turn out to be problematic when applied to a real live software project.

1. You can’t manage what you can’t measure.
2. You can manage quality into a software product.
3. Programming can and should be egoless.
4. Tools and techniques: one size fits all.
5. Software needs more methodologies.
6. To estimate cost and schedule, first estimate lines of code.
7. Random test input is a good way to optimize testing.
8. “Given enough eyeballs, all bugs are shallow.”
9. The way to predict future maintenance costs and to make product replacement decisions is to look at past cost data.
10. You teach people how to program by showing them how to *write* programs.


If you’re curious about the rationale behind these facts and fallacies, that’s entirely the reason the book exists: to remind us to question what we’re doing. **We should be thinking about our craft every day, in some small way, on our own software projects.** That’s how we collectively advance software engineering – by building our shared memory and history in the field. As Mr. Glass states in the introduction:


> In presenting these facts, I am also identifying problems in the field. It is not my intention to present solutions to these problems. This is a what-is book, [not a how-to book](https://blog.codinghorror.com/ideas-are-more-important-than-code/). That’s important to me. I want to bring these facts into the open, where they can be freely discussed, and we can act on them to make progress.


I encourage you to pick up a copy of the full book for a deeper exploration. I do believe there’s a rich learning experience – or a rich remembering experience – here for those of you who choose to read on.

[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[software engineering](https://blog.codinghorror.com/tag/software-engineering/)
[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
