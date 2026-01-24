---
title: "Stuck in a VB.NET Ghetto"
date: 2004-10-13
url: https://blog.codinghorror.com/stuck-in-a-vbnet-ghetto/
slug: stuck-in-a-vbnet-ghetto
word_count: 1210
---

At a recent [trinug](https://www.meetup.com/TRINUG/) user group meeting, [Richard Hale Shaw](https://web.archive.org/web/20050404011258/http://www.richardhaleshawgroup.com/RHSgroup/DesktopDefault.aspx) was going off on a tirade about how Visual Basic 6 was “the ultimate anti-pattern.” I don’t disagree. VB6 had some serious issues, many of which .NET resolves. Then he put a question to the audience: “What specific things about VB6 make it an anti-pattern?” I raised my hand and lazily pitched him a big fat underhand softball: **Option Explicit**. To which RHS responded, “what does that do? I’m not very familiar with VB6.”


You have to respect a man who isn’t about to let mere ignorance keep him from having an opinion.


The following reply to a [Paul Vick blog entry](https://web.archive.org/web/20051016192342/http://www.panopticoncentral.net/archive/2004/05/28/1085.aspx), unlike Mr. Shaw, **exemplifies the best qualities of criticism: it’s based on actual experience.** Familiarity, as they say, breeds contempt:

kg-card-begin: html

> *
>   Anyone have some actual results of making this choice? Like from a BIG project? Has anyone chosen C# and regretted it? Please don’t respond with “well my toy 2000 line app works just great in VB.NET or C#.” I’m looking for someone that can say “we chose C# and it has been a problem for X reason.” *
>  We chose VB.NET a year ago and we regret it. We have 25 very bright developers and a substantial ecommerce web site with plenty of traffic. One year ago we kicked off our port to .NET and we chose VB6 because our existing code base was VB6 and ASP. A few of us here had significant C# expertise from previous jobs and warned the bosses that the “advantages” of VB.NET were a mirage and that there were some clear disadvantages. They actually thought the “automatic conversion” tools were going to buy us some time. The pointy-haired contingent won out and not a day goes by that we don’t curse them for forcing VB.NET on us. 
>  As others have said, you take a big hit moving to .NET at all. The tiny additional hit of moving talented VB6 developers to C# is more than offset (IMHO) by the increased developer productivity achieved over the medium to long term in C#. (If your team is not very talented – or not talented in that way – YMMV.) 
>  Why do I think I am more productive in C# than in VB.NET? Here are a few reasons: 
> VB.NET has abysmal static code analysis: functions that don’t return values, uninitialized variables, unused variable declarations, etc... This is what a compiler is *for*. I wish VB.NET had an “Option ReallyStrict On” so it would check things as thoroughly as the C# compiler does. You can spend hours trying to track down which uninitialized variable or non-returning pathway in a function is the source of a bug, when the compiler could just tell you.
> VB.NET has more aggressive background compilation that you can’t turn off or control in any way and which is buggy! We have solutions for our web site with 30 projects and some projects with hundreds of files. You can’t add a method to a class without taking a coffee break while intellisense chews up a CPU. We’re reduced to having to buy double cpu machines for developers so that they can just type at full speed. And even then all that CPU is wasted because the background compilation just can’t keep up. I wish there were an option for intellisense so that you could *tell* VB.NET when to recompile and when to just chill out because I’m typing a raft of code.
> VB.NET (still) has lurking intellisense bugs whether you use project dependencies or file dependencies. Whichever you choose, you’re stuck with a different set of problems (“can’t copy dll X [v1.1.3000.1] over dll X [v1.1.3000.2]”or “dll A requires a reference to dll B” or “can’t copy dll Y to c:foobary.dll because it is locked”)
> VB.NET has no “using” directive. I know it’s just syntactic sugar... but I want more sugar. The truth is that interacting with non-managed resources (ie. the OS or the database) in .NET sucks even in C#. But having to write “Dim x ... Try ... Finally ... x.dispose EndTry” all the time is just pouring salt in the wound.
> VB.NET has no multiline comment syntax
> VB.NET has no within-the-line comment syntax
> VB.NET has no multiline string syntax
> VB.NET has a limit on line continuations (what is it, like 10 lines)?
> VB.NET projects cannot have pre-build or post-build steps (large, real-world projects inevitably need them)
> VB.NET has no built-in comment->documentation generatorAnd in case anyone is still reading... it’s hard to think of any advantage we’ve seen in using VB.NET. Maybe one: it made some COM coding easier because we could use late binding. I’d say if you are doing lots of COM interop especially if you need late binding, VB.NET is necessary. But I don’t recommend doing any more COM interop than you absolutely have to and late binding is worse than evil.
>  I think that pointy-haired types think that VB.NET will make it “faster.” That the learning curve will be less steep or that fewer changes will need to be made to the code. It just doesn’t work that way. Your project will take 2 or 3 times as long as you anticipated, even if you pick VB.NET. And when you choose VB.NET you may get started faster but you’ll be paying a tax forever, because the tools just aren’t as good as the C# ones. 
>  I’m crossing my fingers for VB improvements in 2005, but I’m not holding my breath. Doubtless something else will be “missed” (like multi-language projects were this time) and we’ll still be stuck in a VB.NET ghetto.

kg-card-end: html

I agree with a few of these criticisms; **you definitely get the sense that VB.NET is a ghetto language at Microsoft**. How hard could it be to support XML comment docs in VB.NET (#10)? And why doesn’t the compiler tell me when I forget to return a value from a function, or that I have an unused variable declaration (#1)? That’s just plain sloppy, especially considering MS has already gone one entire release (2003) without resolving these kinds of obvious things.


On the other hand, **I vehemently disagree that background compilation is a bad thing**. While it shouldn’t be so poorly designed that you can out-type it – perhaps having 30 projects in a solution file is part of the problem – what else are we going to use that 99.9% of idle time on a 3ghz CPU for, anyway (#2, #3)? One of the main reasons I don’t enjoy using C# is precisely *because* it lacks background compilation.* Computers get faster every day. My brain doesn’t. Our IDEs should be doing more for us in the background, not less.


The other bit of good news is that according to Paul, all of the listed issues are resolved in VS.NET 2005. Well, except for the multiline comment requests. And we can get XML comments today using an add-in in VS.NET 2003.


*The other reason is because case sensitivity is wrong in every imaginable way. And possibly in a few additional ways I haven’t yet imagined.

[vb.net](https://blog.codinghorror.com/tag/vb-net/)
[visual basic](https://blog.codinghorror.com/tag/visual-basic/)
[.net framework](https://blog.codinghorror.com/tag/net-framework/)
[software development](https://blog.codinghorror.com/tag/software-development/)
[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
