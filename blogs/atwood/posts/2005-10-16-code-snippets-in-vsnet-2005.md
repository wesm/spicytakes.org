---
title: "Code Snippets in VS.NET 2005"
date: 2005-10-16
url: https://blog.codinghorror.com/code-snippets-in-vsnet-2005/
slug: code-snippets-in-vsnet-2005
word_count: 299
---

One of the most enjoyable new features in Visual Studio .NET 2005 is Code Snippets. This animated GIF illustrates how it works:


![VS.NET 2005 code snippets in action](https://blog.codinghorror.com/content/images/uploads/2005/10/6a0120a85dcdae970b0128776fc971970c-pi.gif)


I’m demonstrating three types of snippets here:

- simple expansion
- template expansion (with variables)
- surround


The easiest way to enter a code snippet is to **begin typing part of the snippet shortcut name**, e.g. “prop” for property expansion. Once you’ve typed enough to uniquely select the snippet shortcut name, press:


![](https://blog.codinghorror.com/content/images/2025/03/image-316.png)


... and the snippet will appear. If it’s a templated snippet:


![](https://blog.codinghorror.com/content/images/2025/03/image-317.png)


If you want to enclose code in a surrounding snippet (e.g., you have code highlighted for a region), you must **manually invoke snippet intellisense** by pressing:


![](https://blog.codinghorror.com/content/images/2025/03/image-318.png)


VB.NET’s implementation of snippets is a bit more robust than the one in C#.

1. VB.NET has a zillion snippets shipping in the box where C# has maybe... two dozen?
2. VB.NET supports code snippets that automatically add any necessary Import statements.


The VB IDE team has a helpful [code snippets FAQ](https://web.archive.org/web/20051215092615/http://blogs.msdn.com/vbide/archive/2005/07/22/441923.aspx) that covers the language differences in detail.


There’s a snippet management UI you can invoke via the **Tools, Code Snippets Management** menu, or by pressing:


![](https://blog.codinghorror.com/content/images/2025/03/image-319.png)


From here you can import and export snippet files, but there’s no editor for creating new ones. Snippets are [just XML files](https://web.archive.org/web/20060102025159/http://msdn2.microsoft.com/en-us/library/ms171418(en-us,vs.80).aspx) with a “.snippet” extension that live in these language specific folders:

- c:Program FilesMicrosoft Visual Studio 8VBSnippets1033
- c:Program FilesMicrosoft Visual Studio 8VC#snippets1033


Assuming you don’t enjoy editing raw XML files, it might be easier to go with Microsoft’s [Snippy](https://web.archive.org/web/20051212084211/http://www.gotdotnet.com/codegallery/codegallery.aspx?id=b0813ae7-466a-43c2-b2ad-f87e4ee6bc39), a GUI for creating VB.NET and C# code snippets. There’s also Michael Palermo’s new [website for sharing code snippets](https://web.archive.org/web/20051101221207/http://www.gotcodesnippets.net/Default.aspx), although there don’t seem to be many there at the moment.

[visual studio](https://blog.codinghorror.com/tag/visual-studio/)
[code snippets](https://blog.codinghorror.com/tag/code-snippets/)
[programming concepts](https://blog.codinghorror.com/tag/programming-concepts/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
