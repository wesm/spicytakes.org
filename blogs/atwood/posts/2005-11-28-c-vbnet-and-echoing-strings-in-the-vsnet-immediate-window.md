---
title: "C#, VB.NET, and echoing strings in the VS.NET Immediate Window"
date: 2005-11-28
url: https://blog.codinghorror.com/c-vbnet-and-echoing-strings-in-the-vsnet-immediate-window/
slug: c-vbnet-and-echoing-strings-in-the-vsnet-immediate-window
word_count: 163
---

I’ve become rather agnostic on the whole topic of [C# versus VB.NET](https://blog.codinghorror.com/vbnet-vs-c-round-two/), but there are still those annoying little differences that sneak up behind you and rabbit-punch you in the kidneys. Like, say, using the VS.NET 2003 [command window in immediate mode](http://msdn2.microsoft.com/en-us/library/c3a0kd3x.aspx) to print a string:


![](https://blog.codinghorror.com/content/images/2025/03/image-359.png)


![Printing text in the Immediate window in a VB.NET project](https://blog.codinghorror.com/content/images/uploads/2005/11/6a0120a85dcdae970b0128776fcb03970c-pi.png)


Usually VB.NET is guilty of handling things in odd and unexpected ways, but this time it’s C#. **I expect newlines to appear in the immediate window as, oh, I don’t know... NEW LINES?** It’s a bit difficult to read text filled with a bunch of rn notation instead of human readable whitespace. What’s worse is that *even the variable tooltips in C# behave this way!*


How can I work around this annoying “feature” of the C# IDE? I thought about creating a macro to use `?System.Diagnostics.Debug.WriteLine(s)`, which behaves appropriately, but the Diagnostics class isn’t always in scope at a breakpoint.

[c#](https://blog.codinghorror.com/tag/c-2/)
[vb.net](https://blog.codinghorror.com/tag/vb-net/)
[vs.net](https://blog.codinghorror.com/tag/vs-net/)
[debugging](https://blog.codinghorror.com/tag/debugging/)
[immediate window](https://blog.codinghorror.com/tag/immediate-window/)
