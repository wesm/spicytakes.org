---
title: "The Xanadu Dream"
date: 2009-10-12
url: https://blog.codinghorror.com/the-xanadu-dream/
slug: the-xanadu-dream
word_count: 1045
---

Links are the [fundamental building blocks of the web](https://blog.codinghorror.com/dont-click-here-the-art-of-hyperlinking/). And every time I click on one, I can’t help recalling the odd visionary who came up with the original idea of clickable links in text, aka [hypertext](http://en.wikipedia.org/wiki/Hypertext), in 1963 – [Ted Nelson](http://en.wikipedia.org/wiki/Ted_Nelson).


Ted Nelson is, shall we say, a *character*. He has gone on record many times with the four maxims that guide his life. He isn’t shy about sharing them with anyone he meets:

- most people are fools
- most authority is malignant
- God does not exist
- everything is wrong


And that, in a nutshell, is pretty much everything you need to know about Ted Nelson. He is **the archetypal borderline autistic, non-conformist, free-thinking technologist**. Any resemblance between Ted and your average programmer is, I’m sure, completely coincidental. That’s why his story is so fascinating to me. It hits close to home.


Like most programmers, Ted’s reach often exceeded his grasp. Ted’s vision of hypertext was far more grandiose than the motley assortment of links that is today’s web. His vision was (and is) a bit of computer history lore that has become the stuff of legend: [Project Xanadu](http://en.wikipedia.org/wiki/Project_Xanadu).

kg-card-begin: html
kg-card-end: html

The above text is excerpted from the definitive 1995 [Wired article on Project Xanadu](https://www.wired.com/1995/06/xanadu/), which is still as electrifying to read today as it was then. The hubris and sheer scale of the Xanadu dream are at turns both inspiring and desperately, hopelessly out of touch.


Xanadu has 17 rules defining its behavior. As you’re reading through this list, ask yourself **how many of these rules are satisfied by the current world wide web**, even in part:

1. Every Xanadu server is uniquely and securely identified.
2. Every Xanadu server can be operated independently or in a network.
3. Every user is uniquely and securely identified.
4. Every user can search, retrieve, create and store documents.
5. Every document can consist of any number of parts each of which may be of any data type.
6. Every document can contain links of any type including virtual copies (“transclusions”) to any other document in the system accessible to its owner.
7. Links are visible and can be followed from all endpoints.
8. Permission to link to a document is explicitly granted by the act of publication.
9. Every document can contain a royalty mechanism at any desired degree of granularity to ensure payment on any portion accessed, including virtual copies (“transclusions”) of all or part of the document.
10. Every document is uniquely and securely identified.
11. Every document can have secure access controls.
12. Every document can be rapidly searched, stored and retrieved without user knowledge of where it is physically stored.
13. Every document is automatically moved to physical storage appropriate to its frequency of access from any given location.
14. Every document is automatically stored redundantly to maintain availability even in case of a disaster.
15. Every Xanadu service provider can charge their users at any rate they choose for the storage, retrieval and publishing of documents.
16. Every transaction is secure and auditable only by the parties to that transaction.
17. The Xanadu client-server communication protocol is an openly published standard. Third-party software development and integration is encouraged.


It is instructive, then, to consider the primary ways in which the modern web is functionally broken:

- **Link rot**. The odds of a hyperlink working are inversely proportional to the age of that hyperlink. Old links frequently break, because the server hosting the content disappears for any number of reasons over time. I’ve gotten to the point where I dread clicking on links from old web pages, because the per-click success rate is so abysmally low.
- **Every website has unique usernames and passwords**. There is almost no [reliable centralized form of identity](https://blog.codinghorror.com/openid-does-the-world-really-need-yet-another-username-and-password/) on the internet, and those few that do exist are often poisoned by explicit commercial affiliation, such as Facebook Connect and Microsoft Passport. This is why curated anonymous, lightweight participation dominates the net – best illustrated by Wikipedia.
- **No redundancy**. If content is driven offline by temporary high traffic levels or, worse, catastrophic data loss, there may not be any way to recover that content. I know that Digg has services which auto-mirror highly rated links because Digg traffic can be so toxic to the destination links. (Ironically, all duggmirror.com links redirect to amazon.com now, which illustrates how ephemeral all this stuff tends to be.) I suppose if you’re lucky the [wayback machine](http://www.archive.org/) will eventually pick up a historical copy of the content, or the [Google cache](http://www.googleguide.com/cached_pages.html) will hold a copy for some unknown amount of time while the site is offline. You’d probably have better odds praying for missing content to reappear.


Let’s put aside the more ambitious parts of Project Xanadu for the moment. **The current world wide web does basically *one* thing: simple, stupid, mindless hyperlinks**. But even that alone was enough to build a functional and useful internet for the world. And Google was able to build a [zillion dollar algorithm](https://blog.codinghorror.com/markov-and-you/) out of discovering the relationship between those dumb hyperlinks.


All that, when the most fundamental building block of the web, the hyperlink, *barely works at all*. Hyperlinks are fraught with peril and pitfalls even under the best of conditions. The current state of hyperlinking is almost literally the stupidest thing we could build that works. Frankly, the current system sucks beyond belief, as Ted himself notes:


> HTML is precisely what we were trying to *prevent* – ever-breaking links, links going outward only, quotes you can’t follow to their origins, no version management, no rights management.


The next time you’re about to embark on a grandiose, glorious software Xanadu Dream of your own, [take Dare’s advice](http://www.25hoursaday.com/weblog/2009/09/27/DuctTapeProgrammersAndTheCultureOfComplexityInSoftwareProjects.aspx).


> The bottom line is that a lot of the time it’s OK to create a solution that solves 80% of the problem. Always remember that shipping is a feature.


Consider the reality of what’s actually possible, what people can understand, and what us all too human programmers can practically implement. It might not be the Xanadu you dreamed of – heck, it might even *suck* – but it’ll at least have a fighting chance of **existing in reality rather than fantasy**.

[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[technology trends](https://blog.codinghorror.com/tag/technology-trends/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[user experience](https://blog.codinghorror.com/tag/user-experience/)
