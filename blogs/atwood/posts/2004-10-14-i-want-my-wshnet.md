---
title: "I want my WSH.NET!"
date: 2004-10-14
url: https://blog.codinghorror.com/i-want-my-wshnet/
slug: i-want-my-wshnet
word_count: 352
---

Speaking of ghetto languages, when exactly is the Windows Script Host going to be updated with a modern language – like, say, .NET? **I want my WSH.NET!**


I still use WSH to write quick and dirty command line utilities that don’t justify a full blown .NET console executable. Like UNIX shell scripts, there’s a lot of power there for relatively little effort. And I don’t have to fire up the VS.NET 2003 IDE to do it, either. Unfortunately, VBScript – the shared script language of classic ASP and the Windows Scripting Host – is rapidly being left behind in an increasingly .NET-centric world. The worst thing is, it’s *just* similar enough to fool you into trying some VB.NET syntax, even though you know better.


It seems like a relatively simple exercise to build WSH.NET, and in fact, several third parties offer stopgaps that deliver script-alike execution of .NET code in plaintext files:

- [Alintex Script .NET](https://web.archive.org/web/20051104042052/http://www.alintex.com/products.aspx)
- [NScript @ Code Project](http://www.codeproject.com/dotnet/nscript.asp)
- [ToolSack .NET Script Host](https://web.archive.org/web/20041019083809/http://www.arcticlabs.com/documentation/dotnetscripthost/)
- [DOTNET Scripting Host](https://web.archive.org/web/20060415022541/http://www.dotnetframework.de/(wvcma52ktvclyyjb0kgwn0n2)/default2.aspx?start=http://www.dotnetframework.de/scripting/dotnetscripting/dsh.en.asp)


However, **this isn’t the same as a Microsoft blessing**. These little tools are all incompatible with each other, require an explicit installation step, and have quirks of their own. I have no idea why Microsoft hasn’t stepped up to the plate with a proper WSH.NET implementation. I did find [this cryptic post](https://web.archive.org/web/20090224083429/http://groups.google.com/groups?q=wsh.net&hl=en&lr=&selm=ux2Q%24VyWBHA.1776%40tkmsftngp05&rnum=1) dated late 2001 by Andrew Clinick of Microsoft:


> *WSH 5.x will remain with us for a long time to come (not least because it’s built into the operating system) We are working on plans for WSH.NET but don’t have concrete info we can share at present.
> To answer the question a bit more does .NET make WSH obsolete? No. It would be great to use VB .NET and JScript .NET in WSH and that’s something we’re working on but in the mean time having to compile exe’s etc. is more difficult than just writing a script and running it. We’re working on making that much simpler in WSH.NET*


Whatever those “plans” were... 3 years later, we’re still waiting.

[.net](https://blog.codinghorror.com/tag/net/)
[windows script host](https://blog.codinghorror.com/tag/windows-script-host/)
[scripting](https://blog.codinghorror.com/tag/scripting/)
[.net languages](https://blog.codinghorror.com/tag/net-languages/)
[software development practices](https://blog.codinghorror.com/tag/software-development-practices/)
