---
title: "UI Follies, Volume I"
date: 2004-10-30
url: https://blog.codinghorror.com/ui-follies-volume-i/
slug: ui-follies-volume-i
word_count: 180
---

Occasionally I run into UI elements so boneheaded, I have to wonder [what the programmers were thinking](https://blog.codinghorror.com/the-rise-and-fall-of-homo-logicus/).


It’s a standard convention for installers to show (estimate, really) how long the install will take. That way users have some idea how long they’ll be waiting, and whether they can safely go do something else while the install proceeds. This installer bravely bucks that trend, choosing to show elapsed time:


![](https://blog.codinghorror.com/content/images/2025/06/image-6.png)


Not only elapsed time, but **elapsed time down to the tenth of a second**. Way to take a useful installer convention, reverse it, and utterly ruin it. Bravo!


I’ve talked before about how windows apps can benefit from adopting web conventions. Well, the converse is not true: **web apps should not pretend to be windows apps**; they should follow standard web conventions. Well, this MySQL error page avoids those standards, choosing instead to build its own [FUI](https://web.archive.org/web/20050325061359/http://md.hudora.de/blog/guids/45/32/57200212091157323745.html):


![](https://blog.codinghorror.com/content/images/2025/06/image-8.png)


On top of that, it’s [a poor error message](https://blog.codinghorror.com/whats-worse-than-a-bad-error-message/). I doubt “threads” or “OS-dependent bugs” mean anything to most users browsing xbitlabs articles.

[ui design](https://blog.codinghorror.com/tag/ui-design/)
[user experience](https://blog.codinghorror.com/tag/user-experience/)
[software development](https://blog.codinghorror.com/tag/software-development/)
[error handling](https://blog.codinghorror.com/tag/error-handling/)
[web conventions](https://blog.codinghorror.com/tag/web-conventions/)
