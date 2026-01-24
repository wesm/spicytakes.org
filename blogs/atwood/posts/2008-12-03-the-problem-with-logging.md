---
title: "The Problem With Logging"
date: 2008-12-03
url: https://blog.codinghorror.com/the-problem-with-logging/
slug: the-problem-with-logging
word_count: 1058
---

A recent Stack Overflow post described [one programmer’s logging style](http://stackoverflow.com/questions/153524/code-to-logging-ratio#153547). Here’s what he logs:

kg-card-begin: html

> **INFO Level**
> The start and end of the method
> The start and end of any major loops
> The start of any major case/switch statements
> **DEBUG Level**
> Any parameters passed into the
> method
> Any row counts from result sets I retrieve
> Any datarows that may contain suspicious data when being passed down to the method 
> Any “generated” file paths, connection strings, or other values that could get mungled up when being “pieced together” by the environment.
> **ERROR Level**
> Handled exceptions
> Invalid login attempts (if security is an issue)
> Bad data that I have intercepted forreporting
> **FATAL Level**
> Unhandled exceptions.

kg-card-end: html

I don’t mean to single out [the author](https://web.archive.org/web/20081216171626/http://www.dillieodigital.net/) here, but this strikes me as a bit... excessive.


Although I’ve never been a particularly big logger, myself, one of my teammates on Stack Overflow is. So when building Stack Overflow, we included [log4net](http://logging.apache.org/log4net/index.html), and logged a bunch of information at the various levels. I wasn’t necessarily a big fan of the approach, but I figured what’s the harm.


Logging does have a certain seductive charm. **Why not log as much as you can whenever you can?** Even if you’re not planning to use it today, who knows, it might be useful for troubleshooting tomorrow. Heck, just log everything! What could it possibly hurt?


Oh, sure, logging seems harmless enough, but let me tell you, it can deal some *serious* hurt. We ran into a particularly nasty recursive logging bug:

- On thread #1, our code was doing Log (lock) / DB stuff (lock)
- On thread #2, our code was doing DB stuff (lock) / log stuff (lock)


If these things happened close together enough under heavy load, this resulted in – you guessed it – a classic out-of-order deadlock scenario. I’m not sure you’d ever see it on a lightly loaded app, but on our website it happened about once a day on average.


I don’t blame log4net for this, I blame our crappy code. We spent days troubleshooting these deadlocks by... wait for it... **adding more logging!** Which naturally made the problem worse and even harder to figure out. We eventually were forced to [take memory dumps](https://web.archive.org/web/20081223213032/http://blogs.msdn.com/tess/archive/2008/05/21/debugdiag-1-1-or-windbg-which-one-should-i-use-and-how-do-i-gather-memory-dumps.aspx) and use dump analysis tools. With the generous assistance of [Greg Varveris](http://samuraiprogrammer.com/community/Default.aspx), we were finally able to identify the culprit: our logging strategy. How ironic. And I mean *real* irony, not the [fake Alanis Morrissette kind](http://www.youtube.com/watch?v=nT1TVSTkAXg).


Although I am a strong believer in logging exceptions, I’ve never been a particularly big fan of logging in the general “let’s log everything we possibly can” sense:

1. **Logging means more code**. If you’re using a traditional logging framework like log4net, every logged event is at least one additional line of code. The more you log, the larger your code grows. This is a serious problem, because [code is the enemy](https://blog.codinghorror.com/the-best-code-is-no-code-at-all/). Visible logging code is clutter – [like excessive comments](https://blog.codinghorror.com/coding-without-comments/), it actively obscures the code that’s doing the real work in the application.
2. **Logging isn’t free.** Most logging frameworks are fairly efficient, but they aren’t infinitely fast. Every log row you write to disk has an overall performance cost on your application. This can also be tricky if you’re dissecting complex objects to place them in the log; that takes additional time.
3. **If it’s worth saving to a logfile, it’s worth showing in the user interface**. This is the paradox: if the information you’re logging is at all valuable, it deserves to be surfaced in the application itself, not buried in an anonymous logfile somewhere. Even if it’s just for administrators. Logfiles are all too often where useful data goes to die, alone, unloved and ignored.
4. **The more you log, the less you can find.** Log enough things and eventually your logs are so noisy nobody can find anything. It’s all too easy to bury yourself in an avalanche of log data. Heck, that’s the default: any given computer is perfectly capable of generating more log data than any of us could possibly deal with in our lifetime. The hidden expense here isn’t the logging, it’s the brainpower needed to make sense of these giant logs. I don’t care how awesome your log parsing tools are, nobody looks forward to mining a gigabyte of log files for useful diagnostic information.
5. **The logfile that cried Wolf.** Good luck getting everyone on your team to agree on the exact definitions of FATAL, ERROR, DEBUG, INFO, and whatever other logging levels you have defined. If you decide to log only the most heinous serial-killer mass-murderer type problems, evil has a lot less room to lurk in your logfiles – and it’ll be a heck of a lot less boring when you *do* look.


So **is logging a giant waste of time?** I’m sure some people will read about this far and draw that conclusion, no matter what else I write. I am not anti-logging. I am anti-*abusive*-logging. Like any other tool in your toolkit, when used properly and appropriately, it can help you create better programs. The problem with logging isn’t the logging, per se – it’s the seductive OCD “just one more bit of data in the log” trap that programmers fall into when *implementing* logging. Logging gets a bad name because it’s so often abused. It’s a shame to end up with all this extra code generating volumes and volumes of logs that aren’t helping anyone.


We’ve since removed all logging from Stack Overflow, relying exclusively on exception logging. Honestly, I don’t miss it at all. I can’t even think of a *single* time since then that I’d wished I’d had a giant verbose logfile to help me diagnose a problem.


When it comes to logging, the right answer is not “yes, always, and as much as possible.” **Resist the tendency to log everything.** Start small and simple, logging only the most obvious and critical of errors. Add (or ideally, inject) more logging only as demonstrated by specific, verifiable needs.


If you aren’t careful, those individual log entries, as wafer thin as they might be, have a disturbing tendency to make your logs end up like [the unfortunate Mr. Creosote](http://www.youtube.com/results?search_query=mr+creosote).

[logging](https://blog.codinghorror.com/tag/logging/)
[programming practices](https://blog.codinghorror.com/tag/programming-practices/)
[debugging](https://blog.codinghorror.com/tag/debugging/)
[software development](https://blog.codinghorror.com/tag/software-development/)
[log management](https://blog.codinghorror.com/tag/log-management/)
