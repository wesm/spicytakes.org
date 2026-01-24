---
title: "Is Eeyore Designing Your Software?"
date: 2008-03-24
url: https://blog.codinghorror.com/is-eeyore-designing-your-software/
slug: is-eeyore-designing-your-software
word_count: 727
---

This [classic Eric Lippert post](https://web.archive.org/web/20080404005623/http://blogs.msdn.com/ericlippert/archive/2003/10/28/53298.aspx) describes, in excruciating, painful detail, exactly how much work it takes to add a single *ChangeLightBulbWindowHandleEx* function to a codebase at Microsoft:

kg-card-begin: html

> One dev to spend five minutes implementing ChangeLightBulbWindowHandleEx.
> One program manager to write the specification.
> One localization expert to review the specification for localizability issues.
> One usability expert to review the specification for accessibility and usability issues.
> At least one dev, tester and PM to brainstorm security vulnerabilities.
> One PM to add the security model to the specification.
> One tester to write the test plan.
> One test lead to update the test schedule.
> One tester to write the test cases and add them to the nightly automation.
> Three or four testers to participate in an ad hoc bug bash.
> One technical writer to write the documentation.
> One technical reviewer to proofread the documentation.
> One copy editor to proofread the documentation.
> One documentation manager to integrate the new documentation into the existing body of text, update tables of contents, indexes, etc.
> Twenty-five translators to translate the documentation and error messages into all the languages supported by Windows.The managers for the translators live in Ireland (European languages) and Japan (Asian languages), which are both severely time-shifted from Redmond, so dealing with them can be a fairly complex logistical problem.
> A team of senior managers to coordinate all these people, write the cheques, and justify the costs to their Vice President.

kg-card-end: html

I think sometimes programmers forget how much work it is to create software at large companies. What may seem like a no-brainer five line code change to us on the outside is perhaps five man-weeks of work once you factor in all the required process overhead. We’re picking on Microsoft here, but this is by no means limited to Microsoft; it’s a simple function of scale and audience for all commercial software.


So then, the obvious question: **who does all those things for non-commercial, open source software?** The answer, per a Raymond Chen comment on the same post, is “nobody”:


> Who develops the test plans for open source software? Who updates the screenshots in the user’s guide and online help? And who translates the documentation into Polish and Turkish? Who verifies that the feature doesn’t violate the Americans with Disabilities Act or German privacy laws? Back when I worked on Linux, the answer was “Nobody. There is no test plan, there is no printed user’s guide, what little documentation there is exists only in English, and nobody cares about complying with the ADA or German privacy laws.” Maybe things have changed since then.


Here’s my honest question: does open source software *need* all that process to be successful? **Isn’t the radical lack of process baggage in open source software development not a weakness, but in fact an evolutionary advantage?** What open source software lacks in formal process it makes up ten times over in ubiquity and community. In other words, if the Elbonians feel so strongly about localization, they can take that effort on themselves. Meanwhile, the developers have more time to implement features that delight the largest base of customers, instead of plowing through mountains of process for every miniscule five line code change.


Are large commercial software companies [crippled by their own process](http://minimsft.blogspot.com/2005/06/recent-random-bits.html)?


> If you openly reward and promote people for killing work by bemoaning the risk and the testing cost and localization impact of each feature and interrogating a design change request as if it were Dan Brown shackled in-front of a wild-eyed, hot-poker wielding Pope, well, everyone is going to grab pitchforks and jump on that “No can do! No can ship!” bandwagon.
> It makes me think of how many feature meetings I’ve had and what a small percent of those features have actually ever shipped. Not that every feature is a good idea, but it’s damn near wake-worthy sometimes for a feature to actually get out into shipping bits. Que [Eeyore](http://en.wikipedia.org/wiki/Eeyore): “Oh no. Now we have to support it. I suppose a hotfix request will come in any moment now...”


All too often, **it really does feel like Microsoft’s software was designed by Eeyore**.


![](https://blog.codinghorror.com/content/images/2025/04/image-34.png)


In this case, the bird represents features that delight customers.

[software development](https://blog.codinghorror.com/tag/software-development/)
[programming concepts](https://blog.codinghorror.com/tag/programming-concepts/)
[software design](https://blog.codinghorror.com/tag/software-design/)
[software testing](https://blog.codinghorror.com/tag/software-testing/)
[documentation](https://blog.codinghorror.com/tag/documentation/)
