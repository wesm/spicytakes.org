---
title: "The Problem With Code Folding"
date: 2008-07-06
url: https://blog.codinghorror.com/the-problem-with-code-folding/
slug: the-problem-with-code-folding
word_count: 913
---

When you join a team, it’s important to **bend your preferences a little to accommodate the generally accepted coding practices of that team.** Not everyone has to agree on every miniscule detail of the code, of course, but it’s a good idea to discuss it with your team and decide on overall approaches and philosophy beforehand. It promotes team harmony, and more than that, it’s just common courtesy. As they say, [*when in Rome*](http://en.wikipedia.org/wiki/When_in_Rome)*, do as the Romans do.*


I’ve always been wary of cowboy coders who rolled into an ongoing project on fresh horses and immediately started dictating terms. It’s a very short trip indeed from there to [Who Wrote This Crap](https://blog.codinghorror.com/who-wrote-this-crap/), and the predictable, inevitable finger-pointing at the foolhardy programmers who came before you begins. Don’t be that guy or gal. [Work with your team](https://web.archive.org/web/20080919141649/http://www.yafla.com/dennisforbes/Effectively-Integrating-Into-Software-Development-Teams/Effectively-Integrating-Into-Software-Development-Teams.html), not against it.


Still, there are some coding preferences people may feel... *strongly.*.. about. If that’s the case, try to clear the air and address those strong preferences up front, as early as possible. Don’t let them simmer. For me, the use of [#region](http://www.google.com/search?q=c%23+region) is one of those things. I tried to make myself clear in this twitter message:


![No, I will not use #regions. And no, I DO NOT NEGOTIATE WITH TERRORISTS. Shut up.](https://blog.codinghorror.com/content/images/2025/07/image-5.png)


So what is `#region`? It’s a named hint you place in C# or VB.NET code to set a **code folding point**. Any code placed inside that region is, by default, collapsed when you re-open it in the editor. Here’s a random example from the [Log4Net project](https://web.archive.org/web/20080913104052/http://logging.apache.org/log4net/download.html):


![](https://blog.codinghorror.com/content/images/2025/04/image-172.png)


Immediately I have a problem: **I can’t see anything!** I have to manually expand those sections to browse any of the code in this class. It is possible to configure the Visual Studio IDE to not fold any of the regions when files are opened, but this is the out of box behavior, so that’s what most developers will see. And of course there are keyboard shortcuts to deal with the regions:

kg-card-begin: html


| Ctrl+M, Ctrl+M | Collapse or expand the block you’re currently in. |
| Ctrl+M, Ctrl+O | Collapse all blocks in the file |
| Ctrl+M, Ctrl+L | Expand all blocks in the file |
| Ctrl+M, Ctrl+P | Stop outlining mode. (Ctrl+M, Ctrl+O resumes) |


kg-card-end: html

Here’s the really sick part: once you expand the above log4net code there’s **literally three pages worth of code there!** After you strip out all the massive XMLDoc comments and the dozen or so #region directives, you *could* have had all the code at your fingertips with a minor flick of the mouse wheel, in a simple scrollable layout.


I daresay being able to *see the damn code* is more important than having it meticulously segmented into six pointless little named buckets, but apparently a lot of programmers can’t get enough of stuffing their code into pointless little named buckets. It’s as if they’ve forgotten what the scroll bar – and [incremental search](https://blog.codinghorror.com/search-if-it-isnt-incremental-its-excremental/) – is for.


The `#region` directive drives me bonkers. It’s not evil, per se, but I feel it is criminally overused in practice and heavily prone to abuse. I strongly urge you to think about how you’re using code folding, because as I see it, there are a lot of downsides:

1. **Folding directives are glorified comments**. `#region` has zero meaning to the compiler; it’s a hint to the editor to allow code folding. It doesn’t do any namespacing or scoping. Why, exactly, are we writing code to accommodate the editor? It boggles my mind that we’d add significant lines of code to our project that do nothing but offer organizational hints to the editor. Even traditional comments are a better value for your keystroke, because they can be more expressive. And folding is certainly no substitute at all for bona-fide refactoring.
2. **Folding is used to sweep code under the rug**. Got a bunch of boring boilerplate code that makes your eyes water? A slew of ugly, gnarly code that nobody in their right mind wants to look at? Hide it in a region and fold that sucker into oblivion! Problem solved, right? Hardly. Your project is now full of crappy code that *you can’t see*. That’s worse. Much worse! Code that hides from you is code that will rot in the most putrescent and painful way possible. Your code should be front and center at all times – exposed to as many programmers’ eyes, and as much healing light, as possible.
3. **Folding is used to mask excessive length.** The presence of folded code can lull developers into a false sense of what clean code looks like. Under the cover of folding, you can end up writing long, horrible spaghetti code blocks. If the code needs the crutch of folding to *look* organized, it’s bad code.
4. **Folding can hide deficiencies in your editor.** The presence of so-called “standard” boilerplate regions like “Public Constructors” and “Public Properties” and “Events” is not a feature. It’s a bug. The editor should *automatically* offer to fold up these common structural blocks for you! I’m continually amazed that programmers spend time doing this scutwork when they could be writing useful code. Or at least demanding a smarter code editor.


I urge developers to **write code that doesn’t *need* folding to be readable, clear, and concise**. I’m sure there are sane uses for code folding out there somewhere, but I rarely see them.

[programming practices](https://blog.codinghorror.com/tag/programming-practices/)
[teamwork](https://blog.codinghorror.com/tag/teamwork/)
[coding style](https://blog.codinghorror.com/tag/coding-style/)
[team collaboration](https://blog.codinghorror.com/tag/team-collaboration/)
[software development](https://blog.codinghorror.com/tag/software-development/)
