---
title: "Who Wrote This Crap?"
date: 2007-11-06
url: https://blog.codinghorror.com/who-wrote-this-crap/
slug: who-wrote-this-crap
word_count: 336
---

Does this sound familiar?


> ***your program*** (n): a maze of non-sequiturs littered with clever-clever tricks and irrelevant comments. Compare *MY PROGRAM*.
> ***my program*** (n): a gem of algorithmic precision, offering the most sublime balance between compact, efficient coding on the one hand, and fully commented legibility for posterity on the other. Compare *YOUR PROGRAM*.


I first read this in the original 1993 edition of [Code Complete](http://www.amazon.com/exec/obidos/ASIN/0735619670). It’s quoted from a much earlier book, Stan Kelley-Bootle’s [The Devil’s Dp Dictionary](http://www.amazon.com/exec/obidos/ASIN/0070340226), which was published in 1981. It’s still true, more than 25 years later. There’s a knee-jerk predisposition to look at code you didn’t write, and for various reasons large and small, proclaim it *absolute crap*. But figuring out who’s actually *responsible* for that crappy code takes some detective work.


The upcoming Visual Studio 2008, or at least the [Team System](https://web.archive.org/web/20071215011909/http://msdn2.microsoft.com/en-us/teamsystem/default.aspx) flavor of it, finally delivers a feature I’ve wanted for years: **it can display the code side-by-side with the person who last changed that code.**


![Visual Studio IDE with source control annotations (blame)](https://blog.codinghorror.com/content/images/uploads/2007/11/6a0120a85dcdae970b0120a86da4df970b-pi.png)


The last person to change any particular line is identified right there, next to the lines they changed, along with the date and revision number. Hovering over the revision number reveals a tooltip containing any check in comments associated with that change. Clicking on the revision number brings up the full details dialog for that check in.


Although I have mixed feelings about source control integration with the IDE, I think this is a fairly compelling argument in favor of it. Sometimes you just want to know **who wrote this crap**, and having that information directly next to the code in your editor saves many tedious steps of manually tracking down the owner of those particular lines.


This feature is called “annotate” [in Team System](http://blogs.msdn.com/bharry/archive/2006/09/07/744993.aspx) source control, but it’s called “blame” [in Subversion](http://svnbook.red-bean.com/en/1.0/re02.html) and [in Vault](http://www.ericsink.com/scm/scm_history.html). So if you’re wondering who to blame, now you know. It’s all those *other* developers. Obviously.

[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[code quality](https://blog.codinghorror.com/tag/code-quality/)
[software engineering](https://blog.codinghorror.com/tag/software-engineering/)
[debugging](https://blog.codinghorror.com/tag/debugging/)
