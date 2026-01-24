---
title: "Code Reviews: Just Do It"
date: 2006-01-21
url: https://blog.codinghorror.com/code-reviews-just-do-it/
slug: code-reviews-just-do-it
word_count: 571
---

In [Humanizing Peer Reviews](https://web.archive.org/web/20060315135514/http://www.processimpact.com/articles/humanizing_reviews.html), Karl Wiegers starts with a powerful pronouncement:


> Peer review – an activity in which people other than the author of a software deliverable examine it for defects and improvement opportunities – is one of the most powerful software quality tools available. Peer review methods include inspections, walkthroughs, peer desk checks, and other similar activities. After experiencing the benefits of peer reviews for nearly fifteen years, I would never work in a team that did not perform them.


After participating in code reviews for a while here at Vertigo, I believe that **peer code reviews are the single biggest thing you can do to improve your code.** If you’re not doing code reviews *right now* with another developer, you’re missing a lot of bugs in your code and cheating yourself out of some key professional development opportunities. As far as I’m concerned, my code isn’t done until I’ve gone over it with a fellow developer.


But don’t take my word for it. McConnell provides plenty of evidence for the efficacy of code reviews in [Code Complete](http://www.amazon.com/exec/obidos/ASIN/0735619670):

kg-card-begin: html

> … software testing alone has limited effectiveness – the average defect detection rate is only 25 percent for unit testing, 35 percent for function testing, and 45 percent for integration testing. In contrast, **the average effectiveness of design and code inspections are 55 and 60 percent**. Case studies of review results have been impressive:
> In a software-maintenance organization, 55 percent of one-line maintenance changes were in error before code reviews were introduced. After reviews were introduced, only 2 percent of the changes were in error. When all changes were considered, 95 percent were correct the first time after reviews were introduced. Before reviews were introduced, under 20 percent were correct the first time.
> In a group of 11 programs developed by the same group of people, the first 5 were developed without reviews. The remaining 6 were developed with reviews. After all the programs were released to production, the first 5 had an average of 4.5 errors per 100 lines of code. The 6 that had been inspected had an average of only 0.82 errors per 100. Reviews cut the errors by over 80 percent.
> The Aetna Insurance Company found 82 percent of the errors in a program by using inspections and was able to decrease its development resources by 20 percent.
> IBM’s 500,000 line Orbit project used 11 levels of inspections. It was delivered early and had only about 1 percent of the errors that would normally be expected.
> A study of an organization at AT&T with more than 200 people reported a 14 percent increase in productivity and a 90 percent decrease in defects after the organization introduced reviews.
> Jet Propulsion Laboratories estimates that it saves about $25,000 per inspection by finding and fixing defects at an early stage.

kg-card-end: html

The only hurdle to a code review is finding a developer you respect to do it, and making the time to perform the review. Once you get started, I think you’ll quickly find that every minute you spend in a code review is paid back tenfold.


If your organization is new to code reviews, I highly recommend Karl’s book, [Peer Reviews in Software](http://www.amazon.com/exec/obidos/ASIN/0201734850): A Practical Guide. The [sample chapters](https://web.archive.org/web/20060315135046/http://www.processimpact.com/reviews_book/reviews_book_toc.shtml) Karl provides on his website are a great primer, too.

[software development](https://blog.codinghorror.com/tag/software-development/)
[code reviews](https://blog.codinghorror.com/tag/code-reviews/)
[peer reviews](https://blog.codinghorror.com/tag/peer-reviews/)
[code quality](https://blog.codinghorror.com/tag/code-quality/)
[professional development](https://blog.codinghorror.com/tag/professional-development/)
