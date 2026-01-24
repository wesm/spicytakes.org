---
title: "Are your exceptions silent?"
date: 2004-10-10
url: https://blog.codinghorror.com/are-your-exceptions-silent/
slug: are-your-exceptions-silent
word_count: 699
---

This [Slate article](https://web.archive.org/web/20041010041003/http://slate.msn.com/id/2107471/) highlights an interesting statistic:


> *A few years ago, Microsoft set up the Windows Error Reporting Service to help find out where crashes come from. After a Windows application – or your whole PC – shuts down, a box pops up asking you to send a confidential error report. Using pattern-matching software to sift through the data from millions of these reports, Microsoft discovered a surprising statistic. **Seventy percent of Windows crashes involve one particular kind of software: device drivers.** (I couldn’t get stats for the Mac, but, at least anecdotally, device drivers are a major cause of drop-dead crashes.)*


Device driver code is privileged and talks directly to the kernel of the OS. Isolating it, as you would with a standard user-mode executable, cripples hardware performance to an absurd degree: imagine hard drive access times an order of magnitude slower than they are now. Historically, more and more functions are moving into the NT kernel. For a recent example, one of the big performance wins in IIS6 (over IIS5) is that the [HTTP stack does business mostly in the kernel](http://certcities.com/editorial/columns/story.asp?EditorialsID=163) and avoids a lot of expensive ring transitions. This was driven by a similar change in Linux/Apache about a year earlier, which cost Microsoft a bunch of benchmark performance wins and probably forced their hand.


Although the performance gain can be substantial, the potential costs are high: kernel mode crashes are irrecoverable. That means an exception crashes the entire OS, not just the single application that cause the problem. Hello BSOD. Anyway, just because I trust Microsoft to write stable kernel-mode code, that doesn’t mean I trust J. Random Taiwanese Device Driver Coder – or myself – to. That’s why Microsoft has their fancy hardware certifications and WHQL assurance labs.


Anyway, the important thing here is not the device drivers, but the way Microsoft is getting automatic feedback when users encounter an error. This weakness is nothing new; it has existed in every Microsoft OS since Windows 95. The only difference is that there is now irrefutable data guiding Microsoft to the source of the problem, and thus the solution. So here’s my question to you: **do your applications tell you when users encounter an error?** Witness this compelling statistical data gathered from Microsoft’s [Windows Error Reporting](https://web.archive.org/web/20041014120100/http://www.microsoft.com/whdc/maintain/WERHelp.mspx):

kg-card-begin: html

> *
> Broad-based trend analysis of error reporting data shows that across all the issues that exist on the affected Windows platforms and the number of incidents received:
> **Fixing 20 percent of the top-reported bugs can solve 80 percent of customer issues.**
> Addressing 1 percent of the bugs would address 50 percent of the customer issues.
> The same analysis results are generally true on a company-by-company basis. The data that WER provides can show you the product problems that are causing your customers the most serious problems.
> *

kg-card-end: html

Remember: these aren’t hardware device drivers they are talking about. These are garden variety software applications.


![](https://blog.codinghorror.com/content/images/2025/06/image-22.png)


Microsoft is in a unique position to gather global statistics on this, and they are compelling – **if your exceptions are “silent,” you are willfully throwing away data that could improve your application for everyday users by eighty percent.** Eighty percent! That’s just an incredible number. And bear in mind, these are real problems encountered in the wild by actual users, arguably the most important kinds of fixes.


Of course, you don’t have to use WER. The framework has robust global exception handling baked in. Coming from a VB6, this was one of my most anticipated features, and it’s something I’ve since worked with extensively:

- [User-Friendly .NET Exception Handling](https://web.archive.org/web/20041012214701/http://www.codeproject.com/dotnet/ExceptionHandling.asp)
- [User-Friendly ASP.NET Exception Handling](http://www.codeproject.com/aspnet/ASPNETExceptionHandling.asp)


There’s also Microsoft’s Exception Management Application Block for .NET, although it’s little more than a plugin framework. The more recent Using HTTP Modules and Handlers to Create Pluggable ASP.NET Components is more practical, though ASP-specific. This is such a good idea that I think I will build a HttpModule version of my ASP.NET handler, too. The main advantage is being able to plug error handling into an app without needing to touch the global.asx file – and thus recompiling.

[security](https://blog.codinghorror.com/tag/security/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[technology trends](https://blog.codinghorror.com/tag/technology-trends/)
[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[user experience](https://blog.codinghorror.com/tag/user-experience/)
