---
title: "What’s In a Version Number, Anyway?"
date: 2007-02-15
url: https://blog.codinghorror.com/whats-in-a-version-number-anyway/
slug: whats-in-a-version-number-anyway
word_count: 846
---

I remember when Microsoft announced that Windows 4.0 would be known as [Windows 95](http://en.wikipedia.org/wiki/Windows_95). At the time, it seemed like a radical, unnecessary change – naming software with *years* instead of *version numbers*? Inconceivable! How will users of Windows 3.1 possibly know what software version they should upgrade to?


In retrospect, switching away from software version numbers to years seems like one of the wisest decisions Microsoft ever made.

- **Users don’t care about version numbers.** Major, minor, alpha, beta, build number... what does it all mean? What users *might* care about is knowing whether or not the software they’re running is current. A simple date is the most direct way to communicate this to the user.
- **A model year is easy to understand.** Why should it take two arbitrary numbers and a decimal point to identify what software you’re using? We identify tons of consumer products using a simple model year designator. Software should be no different.
- **Version numbers don’t scale.** Once you get beyond ten versions, what’s the point of meticulously counting every new release? Better to stamp it with a date and move on.


Microsoft Office 2003 is a far more meaningful name than Microsoft Office 11. And Firefox 2007 would be a much better name than Firefox 2.0 for all the same reasons.


But version numbers live on, at least for programmers. Here’s a quick survey of version numbers for the software running on my machine at the moment:

kg-card-begin: html

7.0.6000.16386
8.1.0178.00
11.11
2.7.0.0
2.5.10 / build 6903
2.0 build 0930
0122.1848.2579.33475
2.0.50727.312
2.0.0.1
1.8.20061.20418


kg-card-end: html
As you can see, there’s not even a commonly accepted pattern for version numbers. In .NET, the [version number convention](http://msdn2.microsoft.com/en-us/library/system.version.aspx) is:`(Major version).(Minor version).(Revision number).(Build number)`But it’s hardly universal. And even if it was, what does all this meticulously numbered version data get us? What does it mean? Why have version numbers at all? It’s partly because version number is an expected software convention. And partly because programmers never met a piece of arbitrarily detailed metadata they didn’t love. Personally, **I like to think of version numbers as dog tags for your software**. Like dog tags, they’re primarily designed for use *in the event of an emergency*.In the event of a software problem – if, on the battlefield, you hear someone screaming “medic!” – it is useful to consult the dog tags so you know exactly what version of the software you’re dealing with.But software version numbers, even arbitrarily detailed programmer version numbers, can’t seem to avoid dates, either. Jensen Harris explains the [Microsoft Office version numbering scheme](https://web.archive.org/web/20070223113854/http://blogs.msdn.com/jensenh/archive/2005/11/11/491779.aspx):
kg-card-begin: html

The most interesting thing to watch for is the first 4-digit number you encounter.  In the examples above, 5608 and 3417.  These are what we refer to as the “build number.”  Every few days during the development cycle, we compile all of the code in Office and turn it into a “build”: essentially an installable version of all the work everyone’s done up until that point.  Eventually, a build becomes “final” and that is the one that ends up on CDs and in the store.

The 4-digit build number is actually an encoded date which allows you tell when a build was born.  The algorithm works like this:


Take the year in which a project started.  For Office “12”, that was 2003.
Call January of that year “Month 1.”
The first two digits of the build number are the number of months since “Month 1.”
The last two digits are the day of that month.


So, if you have build 3417, you would do the following math: “Month 1” was January 2003.  “Month 13” was January 2004.  “Month 25” was January 2005.  Therefore, “Month 34” would be October 2005. 3417 = October 17, 2005, which was the date on which Office 12 build 3417 started. For Office 2003 and XP both, “Month 1” was January 2000.  So, the final build of Office 2003, 5608, was made on August 8, 2003.


kg-card-end: html
So Microsoft Office version numbers end up containing three relevant bits of data:the software generation (Office 97, Office XP, Office 2003, Office 2007), which is patently obvious to anyone using the software – and can be directly inferred from the build date anyway.the date of the build.the number of builds done after “code freeze.”Of those three, how many are actually useful to users? How many are useful to developers?On the whole, I encourage software developers to **avoid confounding users with version numbers**. That’s what leads to crappy ideas like SID 6.7 and even crappier movies like [Virtuosity](http://en.wikipedia.org/wiki/Virtuosity). We brought it on ourselves by letting our geeky, meaningless little construct of major and minor version numbers spill over into pop culture. It’s not worth it. Let’s reel it back in.Whenever possible, **use simple dates instead of version numbers**, particularly in the public names of products. And if you absolutely, positively must use version numbers internally, make them dates anyway: be sure to encode the date of the build somewhere in your version number.

[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[version control](https://blog.codinghorror.com/tag/version-control/)
[software versioning](https://blog.codinghorror.com/tag/software-versioning/)
[user experience](https://blog.codinghorror.com/tag/user-experience/)
