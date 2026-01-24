---
title: "About... The About Box"
date: 2004-02-17
url: https://blog.codinghorror.com/about-the-about-box/
slug: about-the-about-box
word_count: 320
---

You’d think someone would have written a decent, generic .NET About Box by now. Well, if it’s out there, I couldn’t find it! The About Box isn’t an essential part of any application, but my research (and practical experience) indicates it has two key uses:

- For **users**: so they can identify the application, who made it, and what version they’re dealing with. Real basic stuff. Dogtags for your application, if you will.
- For **developers**: to provide detailed build, version, and file information. Typically used when troubleshooting problems with compiled, deployed code. Medic!


It’s convenient to have an About Box– but to continue with the dogtag analaogy, if you’re whipping out dogtags on a regular basis, that’s symptomatic of a deeper problem. The About Box is not meant to be used every day, but when you need it, it can be a lifesaver. It’s OK to be used infrequently, but it also needs to provide decent diagnostic info. Decorative About Boxes are not helpful.

In order to meet both user and developer needs, I put together a tiered dialog, with simple mode, for users:


![](https://blog.codinghorror.com/content/images/2025/06/image-60.png)


and complex mode, for developers:


![](https://blog.codinghorror.com/content/images/2025/06/image-61.png)


Most of the identity of your application can be derived from those tricky little AssemblyInfo files:


> <Assembly: AssemblyTitle(“About Box Demo”)>
> <Assembly: AssemblyDescription(“Demonstration of AboutBox.vb code”)>
> <Assembly: AssemblyCompany(“Atwood Heavy Industries”)>
> <Assembly: AssemblyProduct(“Demo code”)>
> <Assembly: AssemblyCopyright(“2004, Atwood Heavy Industries”)>
> <Assembly: AssemblyTrademark(“All Rights Reserved”)>


That’s the same information you’d expect to see when right clicking your .EXE file, then selecting properties. And it is!


![](https://blog.codinghorror.com/content/images/2025/06/image-62.png)


I tried to include all the Application and Assembly level diagnostic info that I’ve found useful. I’m sure I left something out, but I’m pretty sure I covered all the standard stuff, too. Try it out and let me know what you think.

[Download the Visual Studio .NET 2003 project](https://www.codeproject.com/Articles/7390/About-The-About-Box) from CodeProject.

[.net](https://blog.codinghorror.com/tag/net/)
[about box](https://blog.codinghorror.com/tag/about-box/)
[software development](https://blog.codinghorror.com/tag/software-development/)
[user experience](https://blog.codinghorror.com/tag/user-experience/)
[debugging.](https://blog.codinghorror.com/tag/debugging-2/)
