---
title: "Managed Code Analysis Tools"
date: 2005-09-06
url: https://blog.codinghorror.com/managed-code-analysis-tools/
slug: managed-code-analysis-tools
word_count: 438
---

Navigating a new codebase can feel like like landing on an alien planet. That’s where [static code analysis](http://en.wikipedia.org/wiki/Static_code_analysis) tools come in handy; they’re akin to [software tricorders](http://en.wikipedia.org/wiki/Tricorder). They provide a general snapshot of unfamiliar code: Is it normal? Is it unusual? Is it dangerous?*


![](https://blog.codinghorror.com/content/images/2025/05/image-134.png)


There’s an element of “correctness” associated with static code analysis, but I think this should be de-emphasized. **The last thing developers want is a Code Nazi peering over their shoulder.** I prefer to think of these tools as software tricorders, collecting a bunch of recommendations and metrics about our code. What we choose to do with that data is up to us.


The most famous static code analysis tool for .NET is, of course, [Microsoft’s FxCop](https://web.archive.org/web/20050923112406/http://www.gotdotnet.com/team/fxcop/). If you haven’t tried FxCop in a while, I recommend running the latest version across one of your compiled assemblies. You’d be surprised how helpful it is, particularly for identifying unused variables and functions. You may also be surprised how annoying some of the rules are; that’s why the entire list of rules can be selectively enabled or disabled and saved as profiles. You can even write your own custom FxCop rules – how about [a custom rule](https://web.archive.org/web/20060101064559/http://msdn.microsoft.com/msdnmag/issues/04/06/Bugslayer/default.aspx) that requires XML documentation for each assembly, as illustrated in this June 2004 MSDN article?


FxCop is currently a standalone .exe in an informal GotDotNet workspace, but in Visual Studio 2005, it’s an integrated part of the build process. You can enable output from the console version of FxCop by ticking the checkbox on the Code Analysis tab of the project properties. Any FxCop warnings or errors then show up as you would expect in the standard Task List tab.**


There’s at least one commercial tool that also does .NET static code analysis, namely [FMS Total .NET Analyzer](http://www.fmsinc.com/dotnet/analyzer/index.asp). I tried the evaluation version which is limited to identifying only one issue for each category. It’s nice enough, but it also seems to overlap quite a bit with FxCop. And it’s pricey.


In addition to those well-known tools, Raymond Lewallen and Robin Curry found some additional lesser known managed code analysis tools:

- [Reflector.CodeMetrics](https://web.archive.org/web/20070423080624/http://www.testingreflections.com/node/view/1158) (an add-in for the essential [Reflector](http://www.aisto.com/roeder/dotnet/))
- [DevMetrics](https://web.archive.org/web/20051121212805/http://www.anticipatingminds.com/Content/products/devMetrics/devMetrics.aspx) ($)
- [NDepend](https://web.archive.org/web/20050924034735/http://smacchia.chez.tiscali.fr/NDepend.html)
- [Complexity Analyzer](https://web.archive.org/web/20060328224027/http://www.knowdotnet.com/articles/complexityanalyzer.html) ($)
- [CCMetrics](https://web.archive.org/web/20051228135855/http://www.serviceframework.com/jwss/utility,ccmetrics,utility.aspx)
- [CRPlugin](https://sourceforge.net/projects/crplugin/) (plugin for [DxCore](http://www.devexpress.com/Downloads/NET/DXCore/))
- [Source Monitor](https://web.archive.org/web/20051026023636/http://www.campwoodsw.com/sm20.html)
- [vil](https://web.archive.org/web/20050924015732/http://www.1bot.com/)


I’ve heard good things about NDepends in particular, but I haven’t had a chance to check it out yet.


*Don’t bother if you’re wearing a red shirt. In classic Trek fashion, you may not be around long enough to care.
**At least in VS.NET 2005 beta 2, you can.

[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[static code analysis](https://blog.codinghorror.com/tag/static-code-analysis/)
[.net](https://blog.codinghorror.com/tag/net/)
[fxcop](https://blog.codinghorror.com/tag/fxcop/)
