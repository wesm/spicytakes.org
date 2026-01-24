---
title: "Mort, Elvis, Einstein, and You"
date: 2007-11-29
url: https://blog.codinghorror.com/mort-elvis-einstein-and-you/
slug: mort-elvis-einstein-and-you
word_count: 1662
---

Earlier this week I wrote about [The Two Types of Programmers](https://blog.codinghorror.com/the-two-types-of-programmers/). Based on the huge number of comments, it seemed to strike a nerve. Or two. This surprised me, because it was never meant to be the inflammatory, provocative diatribe that many people interpreted it as. It got so out of hand that Ben Collins-Sussman, the original author of the post I quoted, was driven to post [a follow up](http://blog.red-bean.com/sussman/?p=82) clarifying his original post.


Many of the commenters were offended that I somehow lumped them into a vast unwashed eighty-percent sea of vocational programmers. Here’s what’s particularly ironic: **the very act of commenting on an article about software development automatically means you’re *not* a vocational eighty-percenter**. Trust me. I absolutely was not calling any of my [readers inadequate](http://secretgeek.net/inadequate.asp). I don’t say that because I’m a world class suckup; my blog isn’t some kind of special case or even particularly good. I say it because if you’re reading *any* programming blog whatsoever, you’re demonstrated a willingness to improve your skills and learn more about your chosen profession.


Thus, if you read the article, you are most assuredly in the twenty percent category. **The other eighty percent are not actively thinking about the craft of software development.** They would never find that piece, much less *read* it. They simply don’t read programming blogs – other than as the result of web searches to find quick-fix answers to a specific problem they’re having. Nor have they read any of the books in my [recommended reading list](https://blog.codinghorror.com/recommended-reading-for-developers/). The defining characteristic of the vast majority of these so-called “vocational” programmers is that *they are unreachable*. It doesn’t matter what you, I or anyone else writes here – they’ll never see it.


The problem isn’t the other 80%. The problem is that *we’re* stuck inside our own insular little 20% world, and *we* forget that there’s a very large group of programmers we have almost no influence over. Very little we do will make any difference outside our relatively small group. The problem, as I obviously failed to make clear in the post, is figuring out **how to reach the unreachable**. That’s how you make lasting and permanent changes in the craft of software development. Not by catering to the elite – these people take care of themselves – but by reaching out to the majority of everyday programmers.


That was my point. I’m sorry I did such a bad job of communicating it. But on the plus side, at least it got people thinking and talking about the issue.


Some people objected to the very idea of categorizing programmers into groups of any kind. But there’s a rich history of doing exactly that, with interesting and sometimes unintended consequences. In early 2004, Nikhil Kothari [wrote about three personas](https://web.archive.org/web/20080218051638/http://www.nikhilk.net/Personas.aspx) Microsoft came up with while working on Visual Studio 2005.

kg-card-begin: html

> We have three primary personas across the developer division: Mort, Elvis and Einstein.
>   **Mort**, the opportunistic developer, likes to create quick-working solutions for immediate problems. He focuses on productivity and learns as needed.
> **Elvis**, the pragmatic programmer, likes to create long-lasting solutions addressing the problem domain, and learning while working on the solution.
> **Einstein**, the paranoid programmer, likes to create the most efficient solution to a given problem, and typically learn in advance before working on the solution.
> These personas helped guide the design of features during the Visual Studio 2005 product cycle.
> The description above is only a rough summarization of several characteristics collected and documented by our usability folks. During the meeting, a program manager on our team applied these personas in the context of server controls rather well:
> **Mort** would be a developer most comfortable and satisfied if the control could be used as-is and it just worked.
> **Elvis** would like to be able to customize the control to get the desired behavior through properties and code, or be willing to wire up multiple controls together.
> **Einstein** would love to be able to deeply understand the control implementation, and want to be able to extend it to give it different behavior, or go so far as to re-implement it.

kg-card-end: html

I can’t quite date exactly when these personas came to exist at Microsoft. Wesner Moise has an even [earlier reference to these personas](https://web.archive.org/web/20071207175435/http://wesnerm.blogs.com/net_undocumented/2003/09/who_are_you_mor.html), wherein he amusingly refers to himself as “used to be an Einstein.” Wes, old buddy, I’m afraid you’re the archetypal Einstein, no matter how much you might think otherwise.


These personas have been controversial for *years*; they’ve sparked a [lot](http://www.hanselman.com/blog/BeyondElvisEinsteinAndMortNewProgrammingStereotypesForWeb20.aspx) of intense discussion. Evidently there’s a fine line between [“persona” and “stereotype](https://web.archive.org/web/20071215043140/http://codebetter.com/blogs/scott.bellware/archive/2006/04/25/143303.aspx)”:


> The Microsoft developer personas that include Mort, Elvis, and Einstein are ultimately an ethically bankrupt mechanism to pigeonhole software developers into the kind of overly simplified categories that a typical marketing staffer is comfortable with. While intended to help this particular parasitic segment of the corporate world to behaviorally model the psychological predispositions of software developers at their work in an unrealistically simple way, it has instead turned into a system of limitations that developers have begun to impose upon themselves to the detriment of the advancement of software development practice and industry. It appears to be a bid by developers to rid themselves of the capacity for rational thought in favor of tribal identification with corporate brands and software rock stars.


Personas, in and of themselves, are not a bad thing. I’ve written before about [the importance of API usability](https://blog.codinghorror.com/developers-are-users-too/), and personas let you get a leg up on usability by considering the different audiences that will be using your code.


But I can empathize. **As a long time Visual Basic and VB.NET developer by trade, I truly resented being lumped in with Mort**. I’m not just some clock-punching code monkey – I actually *care* about the craft of software development. So what if I happen to write code in a language that doesn’t brutalize me with [case sensitivity](https://blog.codinghorror.com/the-case-for-case-insensitivity/) and curly-bracket megalomania? My language choice is ultimately no more meaningful than [the choice](https://blog.codinghorror.com/choosing-between-net-pepsi-and-net-coke/) between caffeinated cola beverages, so it’s an illusory difference at that.


Paul Vick works on the VB language team at Microsoft and he [echoes some of my concerns](https://web.archive.org/web/20071217155012/http://www.panopticoncentral.net/archive/2006/04/26/11851.aspx):


> The fundamental error I think most people make with the personas is that they see them as mutually exclusive rather than points along the experience spectrum. When I’m working on the VB compiler, I’m definitely an Einstein, thinking at a very high level. When I’m working on stuff like the VBParser sample, I’m generally an Elvis, thinking at a somewhat lower level. And when I’m writing batch scripts or ad-hoc data analysis tools, I’m definitely a Mort, hacking around to figure out what I’m trying to do.
> **The point really is that most people are usually Mort, Elvis and Einstein all at the same time, depending on what they’re doing.** And by building tools that target one or the other, we’re artificially segregating people’s work into buckets that don’t really map onto their daily lives. (I would also argue that the past several releases of Visual Studio has emphasized some personas over others.) Finding a way to better serve people as they move through the flow of the day-to-day work is something that is need of some serious attention.


Mort, like the twenty percent analogy Ben originally came up with, is more than a persona or a stereotype. It’s [a call to action](https://web.archive.org/web/20120421233245/http://haacked.com/archive/2005/08/03/DoesMortKnowWeAreTalkingSmackAboutHimBehindHisBack.aspx).


> **I think the solution is to quit pandering to Mort with our condescending paternalistic attitude, and instead demand better from Mort.** If the capabilities of the average developer truly is as bleak as many make it out to be, we shouldn’t just accept it, but work to raise the quality of the average developer. “Average developer” should describe an acceptable level of competence.
> We have to realize that Mort is responsible for a lot of important systems. Systems that affect the general population. When I hear of recent cases of identity thefts at Choicepoint, especially those caused by lax security such as using default passwords for the database, I think of Mort. When I read that $250 million worth of taxpayer money has gone into an overhaul of the FBI Case File system, and the system has to be scrapped, I think of Mort.
> Given this much responsibility, we should expect more from Mort. So Mort, I hate to say this, but software development is not like working the register at McDonalds where putting in your 9 to 5 is enough. I am all for work-life balance, but you have to understand that software development is an incredibly challenging field, requiring intense concentration and strong mental faculty. It’s time for you to attend a conference or two to improve your skills. It’s time for you to subscribe to a few blogs and read a few more books. But read deeper books than How to program the VCR in 21 days. For example, read a book on Design Patterns or Refactoring. Mort, I am afraid it’s time for you to quit coasting. It’s time for you to step it up a notch.


I firmly believe it is our job to **leave the craft of software development better than we found it**. If you’re anything like me, you wrote horrible code when you started out as a fledgling programmer, too. But through concerted effort and practice, I was determined to [suck less every year](https://blog.codinghorror.com/sucking-less-every-year/). I’ll admit this is sort of painful, because us programmers aren’t exactly known for [our people skills](https://blog.codinghorror.com/in-programming-one-is-the-loneliest-number/). But we owe it to our craft – and to ourselves – to reach out and help our fellow programmers, at least in some small way.


Being a professional programmer is more than just writing great code. Being a professional programmer means helping *other* programmers become professionals, too. We’re all in this thing together. Not everyone can be reached. But some can.

[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[technical practices](https://blog.codinghorror.com/tag/technical-practices/)
