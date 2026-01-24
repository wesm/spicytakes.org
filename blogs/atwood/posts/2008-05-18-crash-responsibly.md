---
title: "Crash Responsibly"
date: 2008-05-18
url: https://blog.codinghorror.com/crash-responsibly/
slug: crash-responsibly
word_count: 782
---

As programmers, it is our responsibility to **ensure that when something goes horribly wrong with our software, the user has a reasonable escape plan**. It’s an issue of fundamental safety in software error handling that I liken to those ubiquitous airline safety cards.


![](https://blog.codinghorror.com/content/images/2025/04/image-119.png)


![](https://blog.codinghorror.com/content/images/2025/04/image-118.png)


Which one accurately depicts the way *your* software treats the user in the event of an emergency?


If I’ve learned anything in the last thirty years, it’s that [I write shitty software – with bugs](https://blog.codinghorror.com/we-make-shitty-software-with-bugs/). I not only need to protect my users from my errors, I need to protect *myself* from my errors, too. That’s why **the first thing I do on any new project is set up an error handling framework**. Errors are inevitable, but ignorance shouldn’t be. If you know about the problems, you can fix them and respond to them.


Note that when I say “errors,” I don’t mean mundane, workaday problems like empty form values, no results, or file not found. Those kinds of errors are covered quite well in 37 Signals’ [Defensive Design for the Web:](http://www.amazon.com/exec/obidos/ASIN/073571410X) How to Improve Error Messages, Help, Forms, and Other Crisis Points.


![](https://blog.codinghorror.com/content/images/2025/04/image-117.png)


It’s a great book; a quick read with lots of visual do’s and don’ts side by side. Despite the giant exclamation point icon on the cover, however, it’s mostly about fundamental web usability, not error handling per se.


I’m talking about **catastrophic errors – real disasters**. Cases where a previously unknown bug in your code causes the application to crash and burn in spectacular fashion. It happens in all applications, whether they’re websites or traditional executables.


![](https://blog.codinghorror.com/content/images/2025/04/image-116.png)


![](https://blog.codinghorror.com/content/images/2025/04/image-115.png)


The situation is pretty dire at this point, but some disaster recovery is possible, if you plan ahead.

kg-card-begin: html

**It is not the user’s job to tell you about errors in your software!**

If users have to tell you when your app crashes, and why, you have *utterly failed your users*. I cannot emphasize this enough.

It’s bad enough that the user has to use our crashy software; are we really going to add insult to injury by pressing them into service as QA staff, too? If you’re relying on users to tell you about problems with your software, you’ll only see a tiny fraction of the overall errors. Most users won’t bother telling you about problems. They’ll just quietly stop using your application.

Whatever error handling solution you choose, it should automatically log everything necessary to troubleshoot the crash – and ideally send a complete set of diagnostic information back to your server. This is fundamental. If you don’t have something like this in place yet, do so immediately.

**Don’t expose users to the default [screen of death](http://en.wikipedia.org/wiki/Screens_of_death).**

It’s true that we can’t do much to recover from these kinds of crashes, but relying on the underlying operating system or webserver to deliver the generic bad news to the user is rude and thoughtless. Override the default crash screen and provide something customized, something relevant to *your* application and *your* users. Here are a few ideas:

Let users know that it’s our fault, not theirs.
Inform the user that the error was logged and dispatched.
If possible, suggest some workarounds and troubleshooting options.
Perhaps even provide direct contact information if they're really stuck and desperately need to get something done.


**Have a detailed public record of your application’s errors.**

In my experience, nothing motivates a team better than a detailed public record of all crashes. There should of course be a searchable, sortable database of errors somewhere, but active notifications are also a good idea. Crashes are *incredibly* annoying to your users. It’s only fair that the team behind the software share a little of that pain for each crash. You could broadcast an error email, text message, or instant message to everyone on the team. Or maybe have every crash automatically open a bug ticket in your bug tracking software. Tired of dealing with all those error emails and/or bug tickets? Fix the software so you don’t have to!

**Leverage the 80/20 rule.**

Once you have a comprehensive record of every crash, you can sort that data by frequency and spend your coding effort resolving the most common problems. Microsoft, based on data from their Windows Error Reporting Service, found that fixing 20 percent of the top reported bugs solved 80 percent of customer issues, and fixing 1 percent of the top reported bugs solved 50 percent of customer issues. That’s huge! Let the [Pareto principle](http://en.wikipedia.org/wiki/Pareto_principle) work for you, not against you.


kg-card-end: html
As software professionals, we should protect our users – and ourselves – from our mistakes. **Crash responsibly!**

[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[error handling](https://blog.codinghorror.com/tag/error-handling/)
[software safety](https://blog.codinghorror.com/tag/software-safety/)
[software bugs](https://blog.codinghorror.com/tag/software-bugs/)
[software frameworks](https://blog.codinghorror.com/tag/software-frameworks/)
