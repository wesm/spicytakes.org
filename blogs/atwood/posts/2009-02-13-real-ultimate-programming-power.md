---
title: "Real Ultimate Programming Power"
date: 2009-02-13
url: https://blog.codinghorror.com/real-ultimate-programming-power/
slug: real-ultimate-programming-power
word_count: 955
---

A common response to [The Ferengi Programmer](https://blog.codinghorror.com/the-ferengi-programmer/):


> From what I can see, the problem of “overly-rule-bound developers” is nowhere near the magnitude of the problem of “developers who don’t really have a clue.”
> The majority of developers do not suffer from too much design patterns, or too much SOLID, or agile, or waterfall for that matter. They suffer from whipping out cowboy code in a pure chaos environment, using simplistic drag & drop, data driven, vb-like techniques.


Absolutely.


But here’s the paradox: the types of programmers who would most benefit from these guidelines, rules, principles, and checklists are the least likely to read and follow them. **Throwing a book of rules at a terrible programmer just creates a terrible programmer with a bruise on their head where the book bounced off.** This is something I discussed previously in [Mort, Elvis, Einstein, and You](https://blog.codinghorror.com/mort-elvis-einstein-and-you/):


> Thus, if you read the article, you are most assuredly in the twenty percent category. The other eighty percent are not actively thinking about the craft of software development. They would never find that piece, much less *read* it. They simply don’t read programming blogs – other than as the result of web searches to find quick-fix answers to a specific problem they’re having. Nor have they read any of the books in my [recommended reading list](https://blog.codinghorror.com/recommended-reading-for-developers/). The defining characteristic of the vast majority of these so-called “vocational” programmers is that *they are unreachable*. It doesn’t matter what you, I or anyone else writes here – they’ll never see it.


In the absence of mentoring and [apprenticeship](https://blog.codinghorror.com/software-apprenticeship/), the dissemination of better programming practices is often conveniently packaged into [processes and methodologies](http://en.wikipedia.org/wiki/Software_engineering_methodology#Specific_software_development_methodologies). How many of these do you know? How many have you practiced?

kg-card-begin: html


| 1969 | [Structured programming](http://en.wikipedia.org/wiki/Structured_programming) |
| 1975 | [Jackson Structured Programming](http://en.wikipedia.org/wiki/Jackson_Structured_Programming) |
| 1980 | [Structured Systems Analysis and Design Methodology](http://en.wikipedia.org/wiki/Structured_Systems_Analysis_and_Design_Methodology) |
| 1980 | [Structured Analysis and Design Technique](http://en.wikipedia.org/wiki/Structured_Analysis_and_Design_Technique) |
| 1981 | [Information Engineering](http://en.wikipedia.org/wiki/Information_Engineering) |
| 1990 | [Object-oriented programming](http://en.wikipedia.org/wiki/Object-oriented_programming) |
| 1991 | [Rapid Application Development](http://en.wikipedia.org/wiki/Rapid_application_development) |
| 1990 | [Virtual finite state machine](http://en.wikipedia.org/wiki/Virtual_finite_state_machine) |
| 1995 | [Dynamic Systems Development Method](http://en.wikipedia.org/wiki/Dynamic_Systems_Development_Method) |
| 1998 | [Scrum](http://en.wikipedia.org/wiki/Scrum_(development)) |
| 1999 | [Extreme Programming](http://en.wikipedia.org/wiki/Extreme_Programming) |
| 2002 | [Enterprise Unified Process](http://en.wikipedia.org/wiki/Enterprise_Unified_Process) |
| 2003 | [Rational Unified Process](http://en.wikipedia.org/wiki/Rational_Unified_Process) |
| 2004 | [Constructionist Design Methodology](http://en.wikipedia.org/wiki/Constructionist_design_methodology) |
| 2005 | [Agile Unified Process](http://en.wikipedia.org/wiki/Agile_Unified_Process) |


kg-card-end: html

And how do we expect the average developer to find out about these? In a word, **marketing**. (I could have [substituted religion](https://blog.codinghorror.com/software-development-its-a-religion/) here without much change in meaning.) It’s no coincidence that a lot of the proponents of these methodologies make their living consulting and teaching about them. And they have their work cut out for them, too, because [most programmers are unreachable](http://www.ericsink.com/entries/Note_to_self.html):


> I was sitting in my office chatting with my coworker Jeremy Sheeley. Jeremy leads the dev team for Vault and Fortress. In the course of our discussion, I suddenly realized that none of our marketing efforts would reach Jeremy. He doesn’t go to trade shows or conferences. He doesn’t read magazines. He doesn’t read blogs. He doesn’t go to user group meetings.
> Jeremy is a decision-maker for the version control tool used by his team, and nothing we are doing would make him aware of our product. How many more Jeremys are out there?


Millions! As Seth Godin notes, the [unreachable are now truly unreachable](http://sethgodin.typepad.com/seths_blog/2007/05/reaching_the_un.html) – at least not through marketing.


So, if we know the programmers who would benefit most from these rules and principles and guidelines are:

- highly unlikely to ever read them of their own volition
- almost impossible to reach through traditional religion marketing


Remind me again – **who, exactly, are we writing these principles, rules, guidelines, and methodologies for?** If we’re only reaching the programmers who are thoughtful enough to care about their work in the first place, what have we truly accomplished? I agree with Jeff R., who left this comment:


> There’s nothing wrong with the [SOLID principles](http://butunclebob.com/ArticleS.UncleBob.PrinciplesOfOod); they make sense to me. But I’ve been programming since the days of card readers and teletypes. They *won’t* make sense to those with little experience. They don’t know when or how to apply them appropriately. They get bogged down in the attempt.
> So trying to follow them changes the focus from result to process. And that’s deadly.
> It’s the job of the lead programmer or manager to see that good principles are followed, perhaps by guiding others invisibly, without explicitly mandating or even mentioning those principles.


In my effort to [suck less every year](https://blog.codinghorror.com/sucking-less-every-year/), I’ve read hundreds of programming books. I’ve researched every modern programming methodology. I’m even a Certified Scrum Mastertm . All of it, to me, seems like endlessly restated versions of four core fundamentals. But “four core fundamentals?” that’s awful marketing. Nobody will listen in rapt, adoring attention to me as I pontificate, nor will they pay the exorbitant consulting fees I demand to support the lifestyle I have become accustomed to. It simply won’t do. Not at all. So, I dub this:


### The Atwood System of Real Ultimate Programming Power

- [DRY](https://blog.codinghorror.com/curlys-law-do-one-thing/)
- [KISS](https://blog.codinghorror.com/kiss-and-yagni/)
- [YAGNI](https://blog.codinghorror.com/were-building-the-space-shuttle/)
- [NAMBLA](http://www.youtube.com/watch?v=nMupwUD8vzk)


All those incredibly detailed rules, guidelines, methodologies, and principles? YAGNI. If it can’t be explained on a single double-spaced sheet of paper, it’s a waste of your time. Go read and write some code! And if you can’t grok these fundamentals in the [first three or four years](https://blog.codinghorror.com/how-to-become-a-better-programmer-by-not-programming/) of your programming career, well – this slightly [modified R. Lee Ermey quote](http://discourse.codinghorror.com/t/mastering-guids-with-occams-razor/1004/2) comes to mind.


*My name is Jeff, and I can’t stop thinking about programming.* And [neither should you](https://blog.codinghorror.com/programming-love-it-or-leave-it/).

[design patterns](https://blog.codinghorror.com/tag/design-patterns/)
[software development](https://blog.codinghorror.com/tag/software-development/)
[programming principles](https://blog.codinghorror.com/tag/programming-principles/)
[coding standards](https://blog.codinghorror.com/tag/coding-standards/)
[developer productivity](https://blog.codinghorror.com/tag/developer-productivity/)
