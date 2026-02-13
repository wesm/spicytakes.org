---
title: "How Trello is different"
date: 2012-01-06
url: https://www.joelonsoftware.com/2012/01/06/how-trello-is-different/
word_count: 1744
---


Just a few months ago, we launched [Trello](http://trello.com/), a super simple, web-based team coordination system. The feedback has been overwhelmingly positive and adoption has been very strong, even in its early, 1.0 state.


Trello is new kind of development project for Fog Creek. It’s 100% hosted; there will never be an “installed software” version of Trello. That allowed us to modernize many aspects of our development process; I am happy to announce that there is *absolutely no Visual Basic code involved in any part of Trello*. What’s next, flying cars?


The biggest difference you’ll notice (compared to our [previous](http://www.fogcreek.com/FogBugz/) [products](http://www.fogcreek.com/kiln/) pitched solely at software developers) is that *Trello is a totally horizontal product.*** **


Horizontal means that it can be used by people from all walks of life. Word processors and web browsers are horizontal. The software your dentist uses to torture you with drills is vertical.


Vertical software is much easier to pull off and make money with, and it’s a good choice for your first startup. Here are two key reasons:

- It’s easier to find customers. If you make dentist software, you know which conventions to go to and which magazines to advertise in. All you have to do is find dentists.
- The margins are better. Your users are professionals at work and it makes sense for them to give you money if you can solve their problems.


Making a major horizontal product that’s useful in any walk of life is almost impossible to pull off. You can’t charge very much, because you’re competing with other horizontal products that can amortize their development costs across a huge number of users. It’s high risk, high reward: not suitable for a young bootstrapped startup, but not a bad idea for a second or third product from a mature and stable company like Fog Creek.


Forgive me if I now divert into telling you a quick story about my time spent on the Microsoft Excel team way back in 1991. (Yes, I know you were not born yet, but I assure you that computers had been invented. Just hop up here on my knee and shut up.)


Everybody thought of Excel as a financial modeling application. It was used for creating calculation models with formulas and stuff. You would put in your assumptions and then calculate things like “if interest rates go up by 0.00001% next year, what percentage of Las Vegas homeowners will plunge into bankruptcy?” For example.


Round about 1993 a couple of us went on customer visits to see how people were using Excel.


We found a fellow whose entire job consisted of maintaining the “number of injuries this week” spreadsheet for a large, highly-regulated utility.


Once a week, he opened an Excel spreadsheet which listed ten facilities, containing the name of the facilities and the number 0, which indicated that were 0 injuries that week. (They never had injuries).


He typed the current date in the top of the spreadsheet, printed a copy, put it in a three-ring binder, and that was pretty much his whole, entire job. It was kind of sad. He took two lunch breaks a day. I would too, if that was my whole job.


Over the next two weeks we visited dozens of Excel customers, and did not see anyone using Excel to actually perform what you would call “calculations.” Almost all of them were using Excel because it was a convenient way to create a table.


(Irrelevant sidenote: the few customers we could find who were doing calculations were banks, devising explosive devices called “derivatives.” They used Excel to maximize the bankers’ bonuses on nine out of ten years, and to cause western civilization to nearly collapse every tenth year. Something about [black swans](http://www.amazon.com/gp/product/1400063515/ref=as_li_ss_tl?ie=UTF8&tag=joelonsoftware&linkCode=as2&camp=1789&creative=390957&creativeASIN=1400063515). Probably just a floating point rounding error.)


What was I talking about? Oh yeah… most people just used Excel to make lists. Suddenly we understood why Lotus Improv, which was this fancy futuristic spreadsheet that was going to make Excel obsolete, had failed completely: because it was great at calculations, but terrible at creating tables, and everyone was using Excel for tables, not calculations.


Bing! A light went off in my head.


The great horizontal killer applications are actually just fancy data structures.


Spreadsheets are not just tools for doing “what-if” analysis. They provide a specific data structure: a table. Most Excel users never enter a formula. They use Excel when they need a table. The gridlines are the most important feature of Excel, not recalc.


Word processors are not just tools for writing books, reports, and letters. They provide a specific data structure: lines of text which automatically wrap and split into pages.


PowerPoint is not just a tool for making boring meetings. It provides a specific data structure: an array of full-screen images.


Some people saw Trello and said, “oh, it’s Kanban boards. For developing software the agile way.” Yeah, it’s that, but it’s also for planning a wedding, for making a list of potential vacation spots to share with your family, for keeping track of applicants to open job positions, and for a billion other things. In fact Trello is for anything where you want to maintain a *list of lists *with a group of people.


There are millions of things that need that kind of data structure, and there hasn’t been a great “list-of-list” app before Trello. (There have been outliners, but outlines are, IMHO, one of the great dead ends in UI design: so appealing to programmers, yet so useless to civilians).


Once you get into Trello, you’ll use it for everything. I use about thirty Trello boards regularly, and I use them with everyone in my life, from the APs (Aged Parents), with whom I plan vacations, with every team at work, and just about every project I’m involved in.


So, ok, that was the first big difference with Trello: horizonal, not vertical. But there are a bunch of other differences:


**It’s delivered continuously.** Rather than having major and minor releases, we pretty much just continuously push out new features from development to customers. A feature that you built and tested, but didn’t deliver yet because you’re waiting for the next major release, becomes *inventory*. Inventory is dead weight: money you spent that’s just wasting away without earning you anything. Sure, 100 years ago, we had these things called “CD-ROMs” and we shipped software that way, so there was an economic reason to bunch up features before we inflict ‘em on the world. But there’s no reason to work that way any more. You already knew that, of course. I’m just saying—I stopped using Visual Basic about five minutes ago. Brave New World.


**It’s not exhaustively tested before being released.** We thought we could get away with this because Trello is free, so customers are more forgiving. But to tell the truth, the real reason we get away with it is because bugs are fixed in a matter of hours, not months, so the net number of “bugs experienced by the public” is low.


**We work in public.** The rule on the Trello team is “default public.” We have a [public Trello board](https://trello.com/board/trello-development/4d5ea62fd76aa1136000000c) that shows everything that we’re working on and where it’s up to. We use this to let customers vote and comment on their favorite features. By the way, while Trello was under development, it was secret. We had a lot of beta testers who gave us customer feedback so that the development team could use [lean startup](http://www.amazon.com/gp/product/0307887898/ref=as_li_ss_tl?ie=UTF8&tag=joelonsoftware&linkCode=as2&camp=1789&creative=390957&creativeASIN=0307887898) principles, but the nine months we spent building version 1.0 in secret gave us a significant lead in a competitive marketplace. But now that we’re shipping, there’s no reason not to talk about our plans.


**This is a “Get Big Fast” product, not a “Ben and Jerry’s”  product.** See [Strategy Letter I](https://www.joelonsoftware.com/articles/fog0000000056.html). The business goal for Trello is to ultimately get to 100 million users. That means that our highest priority is removing any obstacles to adoption. *Anything *that people might use as a reason not to use Trello has to be found and eliminated. For example:


**Trello is free. **The friction caused by charging for a product is the biggest impediment to massive growth. In the long run, we think it’s much easier to figure out how to extract a small amount of money out of a large number of users than to extract a large amount of money out of a small number of users. Once you have 100 million users, it’s easy to figure out which of those users are getting the most value out of the product you built. The ones who are getting the most value will be happy to pay you. The others don’t cost much to support.


**The API and plug-in architectures are the highest priority. **Another way of putting that is:  never build anything in-house if you can expose a basic API and get those high-value users (the ones who are getting the most value out of the platform) to build it for you. On the Trello team, any feature that *can *be provided by a plug-in *must* be provided by a plug-in.


(The [API](http://trello.com/api) is currently in very rudimentary form. You can already use it to do very interesting things. It is under rapid development.)


**We use cutting edge technology. **Often, this means we get cut fingers. Our developers bleed all over MongoDB, WebSockets, CoffeeScript and Node. But at least they’re having fun. And in today’s tight job market, great programmers have a lot of sway on what they’re going to be working on. If you can give them an exciting product that will touch millions of people, and let them dig deep into TCP-IP internals while they try to figure out why simple things aren’t working, they’ll have fun and they’ll love their jobs. Besides, we’re creating a product that we’ll be working on for the next ten years. Technology that’s merely “state of the art” today is going to be old and creaky in five years. We tried to go a little bit beyond “state of the art.” It’s a calculated risk.


None of this is very radical. TL;DR: Fog Creek Software develops an internet product using techniques that every Y-combinator startup has been using since spez was [sleeping with his laptop](http://www.mentalfloss.com/blogs/archives/14093) so he could reboot Reddit when Lisp crashed in the middle of the night. If you haven’t tried Trello yet, try it, then [tell me on twitter](https://twitter.com/#!/spolsky) if it worked.
