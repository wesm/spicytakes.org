---
title: "Using the Command Window"
date: 2004-09-05
url: https://blog.codinghorror.com/using-the-command-window/
slug: using-the-command-window
word_count: 193
---

One of the most underappreciated features of Visual Studio .NET 2003 is the Command Window. Did you know there are a bunch of command alias shortcuts available for use in the command window? I use ‘?’ all the time, but I didn’t know about the others. And then there’s the subtle distinction between immediate mode and command mode: enter **>cmd** and **immed** to switch between the two.


As I mentioned above, I frequently use **?(value)** to dump out the contents of structures in the Command Window. This works, but it’s kinda ghetto. A more sophisticated way to view data structures in real time will appear in Whidbey; [custom data visualizers](https://web.archive.org/web/20040612082359/http://blogs.msdn.com/scottno/archive/2004/04/17/115328.aspx), which automatically display structures in an easier to understand visual format. And naturally you can extend the visualizers with custom viewers for whatever crazy data structure you’re creating, too – even [the humble hashtable](https://web.archive.org/web/20041118085121/http://msdn.microsoft.com/msdnmag/issues/04/05/VisualStudio2005Debugging/).


You don’t have to wait for Whidbey, though. There are a handful of less integrated, but still useful, ad-hoc visualizers available for VS.NET 2003. For example, this [DataSet visualizer](https://web.archive.org/web/20041012002830/http://www.codeproject.com/csharp/DSWatch.asp), and Daniel Cazzulino offers this cool [visualization hack using VSTweak](http://weblogs.asp.net/cazzu/archive/2004/02/10/70658.aspx).

[debugging](https://blog.codinghorror.com/tag/debugging/)
[visual studio](https://blog.codinghorror.com/tag/visual-studio/)
[command window](https://blog.codinghorror.com/tag/command-window/)
[command alias shortcuts](https://blog.codinghorror.com/tag/command-alias-shortcuts/)
[data visualizers](https://blog.codinghorror.com/tag/data-visualizers/)
