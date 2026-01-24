---
title: "A Celebration of The Windows Key"
date: 2005-09-01
url: https://blog.codinghorror.com/a-celebration-of-the-windows-key/
slug: a-celebration-of-the-windows-key
word_count: 562
---

I’m sure everyone knows that the Windows key brings up the Start Menu, but there are also a bunch of standard Windows key shortcuts built into Windows:


![](https://blog.codinghorror.com/content/images/2025/03/image-257.png)


Set focus to first tray icon


![](https://blog.codinghorror.com/content/images/2025/03/image-256.png)


Show Desktop


![](https://blog.codinghorror.com/content/images/2025/03/image-259.png)


Windows Explorer


![](https://blog.codinghorror.com/content/images/2025/03/image-260.png)


Find Files or Folders (aka Search)


![](https://blog.codinghorror.com/content/images/2025/03/image-261.png)


Minimize All windows


![](https://blog.codinghorror.com/content/images/2025/03/image-262.png)


Undo minimize all windows


![](https://blog.codinghorror.com/content/images/2025/03/image-263.png)


Run...


![](https://blog.codinghorror.com/content/images/2025/03/image-264.png)


Select Task


![](https://blog.codinghorror.com/content/images/2025/03/image-265.png)


System Properties


![](https://blog.codinghorror.com/content/images/2025/03/image-266.png)


Windows Help


![](https://blog.codinghorror.com/content/images/2025/03/image-267.png)


Lock workstation


![](https://blog.codinghorror.com/content/images/2025/03/image-268.png)


Utility manager (accessibility)


Where the default Windows key shortcuts end, [WinKey](http://www.google.com/search?q=download+winkey)* begins. Winkey lets you map additional Windows key shortcuts. It can’t override the existing shortcuts, unfortunately, but you’re free to map any key that isn’t already mapped.


The advantage of the Windows key approach is that **all of my most frequently used applications are exactly one key combination away**; for example:


![](https://blog.codinghorror.com/content/images/2025/03/image-269.png)


Launches [Notepad](https://blog.codinghorror.com/revenge-of-notepad/)


![](https://blog.codinghorror.com/content/images/2025/03/image-270.png)


Launches [command shell](https://blog.codinghorror.com/stupid-command-prompt-tricks/)


Of course, you can go a lot further with hotkeys than just overloading the Windows key. That’s where something like [AutoHotKey](http://www.autohotkey.com/) comes in. However, I find that leveraging the built-in Windows key shortcuts, plus a handful of Windows key shortcuts I set up myself, covers 98% of my daily computer use.


But then there’s that other 2%...


When I can’t launch something with the Windows key, **I fall back to the Start, Run (Windows+R) dialog**. Run is passable, but not as helpful as it could be. Trying to perform a Start, Run, “word” won’t launch Microsoft Word, for example. There are a number of third party replacements for Run that attempt to rectify that:

- [ActiveWords](http://www.activewords.com/)
- [AppRocket](http://www.candylabs.com/approcket/) (written in .NET!)
- [SlickRun](http://www.bayden.com/SlickRun/)
- [Dave’s Quick Search Taskbar](https://web.archive.org/web/20050905075359/http://www.dqsd.net/)


I’ve tried each and every one of these solutions, but nothing “stuck.” I couldn’t get myself out of the reflexive habit of Windows+R. Each of these apps has a nice set of additional features far beyond what the run dialog provides, but I never really used them.


In lieu of all these fancy solutions... **wouldn’t it be nice if the Start, Run dialog was just a little bit smarter?** That’s when I stumbled across [this blog post](http://snarkhunt.blogspot.com/2005/04/dirt-cheap-macros.html) describing a very clever hack:

1. Create a folder for your shortcuts under your user folder, e.g., c:documents and settingsusernameshortcuts
2. Right click My Computer, click properties.
3. Click the advanced tab.
4. Click the Environment Variables button at the bottom of the tab.
5. Under user variables, add a new variable named “Path.”
6. Enter %homedrive%%homepath%shortcuts for the variable value.**
7. Create shortcuts and plop them in the shortcuts folder you created.


Here’s a quick snapshot that shows how to set up the per-user Path environment variable for the shortcuts folder:


![](https://blog.codinghorror.com/content/images/2025/05/image-133.png)


Now that I’ve set this up, I can type **Windows+R, 2k3, Enter and Visual Studio 2003 launches!** The only disadvantage – and it’s a minor one – is that there’s no autocomplete until you’ve typed the shortcut at least once. But for me, it’s the best of both worlds: I can leverage the default Windows key accelerators and also have an unlimited number of “smart keywords” via my workhorse Run menu.


*Every time I see WinKey, I think of [Winky Dinky dog](http://www.imdb.com/title/tt0093200/). And I say it in that... voice. I can’t help myself.


**Here’s a complete list of [Windows XP/2000 environment variables](https://web.archive.org/web/20050923175729/http://kennethhunt.com/archives/000933.html) the system can populate for you (e.g., %date%). [Gotta catch ’em all!](https://web.archive.org/web/20051210101755/http://harvardbusinessonline.hbsp.harvard.edu/b01/en/common/item_detail.jhtml?id=502092)

[shortcuts](https://blog.codinghorror.com/tag/shortcuts/)
[keyboard shortcuts](https://blog.codinghorror.com/tag/keyboard-shortcuts/)
[windows key](https://blog.codinghorror.com/tag/windows-key/)
[windows key shortcuts](https://blog.codinghorror.com/tag/windows-key-shortcuts/)
[software development](https://blog.codinghorror.com/tag/software-development/)
