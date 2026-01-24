---
title: "User-Friendly Exception Handling"
date: 2004-06-22
url: https://blog.codinghorror.com/user-friendly-exception-handling/
slug: user-friendly-exception-handling
word_count: 260
---

I just posted a new article on Code Project, [User Friendly Exception Handling](https://www.codeproject.com/KB/exception/ExceptionHandling.aspx). This is a set of classes that deal with unhandled and handled exceptions through a consistent UI, as presented in [Alan Cooper’s](https://web.archive.org/web/20040616203722/https://www.cooper.com/alan/father_of_vb.html) great book, [About Face: The Essentials of User Interface Design](http://www.amazon.com/exec/obidos/ASIN/0764526413/).


![](https://blog.codinghorror.com/content/images/2025/06/image-63.png)


Anyway, at the time of the unhandled exception, here’s what you get for free:

- Display an automatic, Cooper-Approved(tm) exception interface
- Capture a screenshot of the user’s desktop
- Build a string containing comprehensive diagnostic information
- Notify the developers via SMTP e-mail, and attach the screenshot
- Write an event to the event log
- Write a plain-text exception log in the application folder


I have used the hell out of this code and it works like gangbusters. There’s nothing like an extremely tight loop between developers and exceptions to facilitate quick, responsive fixes to broken code. And since we have it set up to email every team member for every Unhandled Exception – it’s a therapeutic form of punishment, too!


Also, if anyone is interested in those animated GIF screenshots – I had been looking for a simple tool to do this for literally *years – *it’s the archaic 1997 version of [GifgIfgiF](http://www.peda.com/ggg/). Extremely old-school, but it still works great and generates very tiny, ultra-compatible animated Gifs. Of course you’ll want to turn off all the crazy XP theming and revert to 256-color friendly Win2k style forms before you generate these kinds of Gif animations, too.


Download the [VS.NET 2003 solution](https://www.codeproject.com/Articles/7390/About-The-About-Box).

[user experience](https://blog.codinghorror.com/tag/user-experience/)
[exception handling](https://blog.codinghorror.com/tag/exception-handling/)
[software development practices](https://blog.codinghorror.com/tag/software-development-practices/)
[user interface design](https://blog.codinghorror.com/tag/user-interface-design/)
