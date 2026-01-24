---
title: "Alpha, Beta, and Sometimes Gamma"
date: 2008-07-30
url: https://blog.codinghorror.com/alpha-beta-and-sometimes-gamma/
slug: alpha-beta-and-sometimes-gamma
word_count: 680
---

As we begin the private beta for Stack Overflow later this week, I wondered: where do the software terms **alpha** and beta come from? And why don’t we ever use **gamma**?

kg-card-begin: html


|  |  |


kg-card-end: html

Alpha and Beta are the first two characters of the [Greek alphabet](http://en.wikipedia.org/wiki/Greek_alphabet). Presumably these characters were chosen because they refer to the first and second rounds of software testing, respectively.


But where did these terms originate? There’s an [uncited Wikipedia section](http://en.wikipedia.org/wiki/Software_release_life_cycle#Origin_of_.27alpha.27_and_.27beta.27) that claims the alpha and beta monikers came, as did so many other things, from **the golden days of IBM**:


> The term beta test comes from an [IBM hardware product test](http://en.wikipedia.org/wiki/IBM_Product_Test) convention, dating back to punched card tabulating and sorting machines. Hardware first went through an alpha test for preliminary functionality and small scale manufacturing feasibility. Then came a beta test, by people or groups other than the developers, to verify that the hardware correctly performed the functions it was supposed to, and that it could be manufactured at scales necessary for the market. And finally, a c test to verify final safety. With the advent of programmable computers and the first shareable software programs, IBM used the same terminology for testing software. As other companies began developing software for their own use, and for distribution to others, the terminology stuck – and is now part of our common vocabulary.


Based on the software release lifecycle page, and my personal experience, here’s how I’d characterize each phase of software development:

1. **Pre-Alpha**
The software is still under active development and not feature complete or ready for consumption by anyone other than software developers. There may be **milestones** during the pre-alpha which deliver specific sets of functionality, and **nightly builds** for other developers or users who are comfortable living on the absolute bleeding edge.
2. **Alpha**
The software is complete enough for *internal* testing. This is typically done by people other than the software engineers who wrote it, but still within the same organization or community that developed the software.
3. **Beta**
The software is complete enough for *external* testing – that is, by groups outside the organization or community that developed the software. Beta software is usually feature complete, but may have known limitations or bugs. Betas are either closed (private) and limited to a specific set of users, or they can be open to the general public.
4. **Release Candidate** (aka gamma or delta)
The software is almost ready for final release. No feature development or enhancement of the software is undertaken; tightly scoped bug fixes are the only code you’re allowed to write in this phase, and even then *only* for the most heinous and debilitating of bugs. One of the [most experienced](https://web.archive.org/web/20080809120243/http://weblogs.asp.net/swarren/) software developers I ever worked with characterized the release candidate development phase thusly: “does this bug kill small children?”
5. **Gold**
The software is finished – and by finished, we mean there are no show-stopping, little-children-killing bugs in it. *That we know of*. There are probably numerous lower-priority bugs [triaged into](https://blog.codinghorror.com/not-all-bugs-are-worth-fixing/) the next point release or service pack, as well.


These phases all sound perfectly familiar to me, although there are two clear trends:

- The definition of beta grows more all-encompassing and elastic every year.
- We are awfully eager to throw alpha quality code over the wall to external users and testers.


In the brave new world of web 2.0, **the alpha and beta designations don’t mean quite the same things they used to**. Perhaps the most troubling trend is the [perpetual beta](http://www.oreillynet.com/pub/a/oreilly/tim/news/2005/09/30/what-is-web-20.html?page=4). So many websites stay in perpetual beta, it’s almost become a running joke. Gmail, for example, [is *still* in beta](http://www.esquire.com/the-side/opinion/gmail-061307) after over four years!


Although I’ve seen plenty of release candidates in my day, I’ve rarely seen a “gamma“ or “delta.” Apparently Flickr used it for a while in their logo, after heroically soldiering on from beta:


![](https://blog.codinghorror.com/content/images/2025/04/image-186.png)


“loves you” is certainly more fun than “gold,” but I’m not sure it’s ever the same as *done*. Maybe that’s the way it should be.

[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[technology trends](https://blog.codinghorror.com/tag/technology-trends/)
[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
