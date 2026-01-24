---
title: "Defending Perpetual Intermediacy"
date: 2004-10-05
url: https://blog.codinghorror.com/defending-perpetual-intermediacy/
slug: defending-perpetual-intermediacy
word_count: 987
---

How many things would you classify yourself as “expert” at? I drive to and from work every day, but I hardly consider myself an expert driver. I brush my teeth at least twice every day, and I’m no expert on oral care; just ask my dentist. I use Visual SourceSafe all the time, but I rarely use the more esoteric branching, pinning, and rollback features. I have to look through the help files when I do those things. I am a **perpetual intermediate** at a vast array of tasks, and expert at only a very, very tiny number of tasks.


In, [The Inmates are Running the Asylum](http://www.amazon.com/exec/obidos/ASIN/0672316498), Alan Cooper makes a similar case for users as perpetual intermediates:


> *The experience of people using interactive systems – as in most things – tends to follow the classic bell curve of statistical distribution. For any silicon-based product, if we graph the number of users against their particular skill level, there will be a few beginners on the left side, a few experts on the right, and a preponderance of intermediate users in the center.
> But statistics don’t tell the whole story. This is a snapshot frozen in time, and while most people – the intermediates – tend to stay in that category for a long time, the people on the extreme ends of the curve – the beginners and experts – are always changing. The difficulty of maintaining a high level of expertise means that experts come and go rapidly. Beginners, on the left side of the curve, change even more rapidly.
> Although everybody spends some minimum time as a beginner, nobody remains in that state for long. That’s because nobody likes to be a beginner, and it is never a goal. People don’t like to be incompetent, and beginners – by definition – are incompetent. Conversely, learning and improving is natural, rewarding, and lots of fun, so beginners become intermediates very quickly. For example, it’s fun to learn tennis, but those first few hours or days, when you can’t return shots and are hitting balls over the fence are frustrating. After you have learned basic racket control, and aren’t spending all of your time chasing lost balls, you really move forward. That state of beginnerhood is plainly not fun to be in, and everybody quickly passes through it to some semblance of intermediate adequacy. If, after a few days, you still find yourself whacking balls around the tennis court at random, you will abandon tennis and take up fly-fishing or stamp collecting.
> The occupants of the beginner end of the curve will either migrate into the center bulge of intermediates, or they will drop off of the graph altogether and find some activity in which they can migrate into intermediacy. However, the population of the graph’s center is very stable. **When people achieve an adequate level of experience and ability, they generally stay there forever.** Particularly with high cognitive friction products, users take no joy in learning about them. So they learn just the minimum and then stop. Only *[*Homo Logicus*](https://blog.codinghorror.com/the-rise-and-fall-of-homo-logicus/)* finds learning about complex systems to be fun.*


Cooper goes on to decry the way software development is traditionally driven by opposite ends of the spectrum – developers as advocates for expert users, and marketing as advocates for beginners (which is typically their audience). Who speaks for the intermediate users?


I’ll take this a bit further: **I think intermediate users are the only users that matter.** The huge body of intermediate users is so dominant that you can and should ignore both beginner and expert users. Developing software to accommodate the small beginner and expert groups consumes too much time and ultimately makes your application worse at the expense of your core user base – the intermediates. Beginners should either become intermediates or, in a manner of speaking, die trying. As for software targeting expert users *exclusively* (aka, developers), that’s a tiny niche deserving of an entirely different design approach.


In my opinion, one of the most powerful tools we have for targeting intermediate users is the Inductive User Interface. IUI, as a concept, is actually quite simple: take the best design elements of the web...

- Back button
- Single-click hyperlink navigation
- Activity-centric “everything on one page” model


and combine those with the best design elements of traditional GUIs...

- Rich interface
- High performance
- Leverages client resources (disk, memory, visuals)


The first major application to utilize IUI was Microsoft Money 2000. My wife uses Money, and I distinctly remember installing Money 2000, and being absolutely blown away by how effective the UI was:


> *The IUI model was developed during the creation of Microsoft Money 2000, an application for managing personal finances. Money 2000 is the product’s eighth major release. Money 2000 is a large Microsoft Windows program with well over one million lines of code. **Money 2000 is a Web-style application. It is not a Web site, but shares many attributes with Web sites.** Its user interface consists of full-screen pages shown in a shared frame, with tools for moving back and forward through a navigational stack. On this foundation, Money 2000 adds a set of new user interface conventions that create a more structured user experience.*


The Inductive User Interface design is nothing more than good programming in practice: **never write what you can steal**. And stealing the wildly successful web UI metaphors is such an utter no-brainer. The only question I have is why it’s taking so long.


We have bits and pieces of IUI in Windows XP (try Control Panel, User Accounts), and there’s a lot of evidence that Microsoft plans to utilize IUI much [more heavily in Longhorn](https://web.archive.org/web/20041010084845/http://msdn.microsoft.com/Longhorn/understanding/ux/default.aspx?pull=%2Flibrary%2Fen-us%2Fdnaero%2Fhtml%2Fusercontrol.asp). But we don’t have to wait for Longhorn; as responsible .NET developers, we should be building IUI interfaces today – as in this [MSDN Windows Forms sample](https://web.archive.org/web/20041010085521/http://msdn.microsoft.com/vcsharp/using/columns/wonders/default.aspx?pull=%2Flibrary%2Fen-us%2Fdnforms%2Fhtml%2Fwinforms07202004.asp).

[software development](https://blog.codinghorror.com/tag/software-development/)
[user experience](https://blog.codinghorror.com/tag/user-experience/)
[perpetual intermediacy](https://blog.codinghorror.com/tag/perpetual-intermediacy/)
[expert](https://blog.codinghorror.com/tag/expert/)
[technical practices](https://blog.codinghorror.com/tag/technical-practices/)
