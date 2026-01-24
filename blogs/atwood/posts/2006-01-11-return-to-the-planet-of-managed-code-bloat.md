---
title: "Return to the Planet of Managed Code Bloat"
date: 2006-01-11
url: https://blog.codinghorror.com/return-to-the-planet-of-managed-code-bloat/
slug: return-to-the-planet-of-managed-code-bloat
word_count: 423
---

I just updated my post [The Bloated World of Managed Code](https://blog.codinghorror.com/the-bloated-world-of-managed-code/) with baseline memory footprints for Console and Winforms apps in .NET 2.0.


I’ll admit **I am a bit of a hypocrite when it comes to managed code apps**. Now that tiny, native BitTorrent clients are available such as [uTorrent](http://www.utorrent.com/) and [BitComet](http://www.bitcomet.com/), I just can’t force myself to suffer through the Java ([Azeureus](http://azureus.sourceforge.net/)) and Python ([ABC](http://pingpong-abc.sourceforge.net/)) clients. They’re nice enough, but I want small, clean and fast for this kind of app. And where’s the .NET BitTorrent client, anyway?


Managed code can be [plenty](https://blog.codinghorror.com/on-managed-code-performance/) [fast](https://blog.codinghorror.com/on-managed-code-performance-again/), but I’ve always said that managed code isn’t appropriate for [every kind of application](https://blog.codinghorror.com/despite-the-incredible-slowness-and-the-sparseness-of-features-this-is-really-really-cool/). It’s another tool in your toolbox, but not the only one.


One particularly egregious example of **managed code misuse**, however, is in [ATI’s Catalyst video card drivers](http://www.anandtech.com/video/showdoc.aspx?i=2188&p=2). The “control center” is a client app which allows you to manipulate the settings. It’s written in .NET 1.1 and launched via a button in the graphics driver tab.


![ATI Catalyst launcher](https://blog.codinghorror.com/content/images/uploads/2006/01/6a0120a85dcdae970b0128776fd705970c-pi.jpg)


It’s a reasonable *concept*, but in practice – it sucks. Even on a clean Pentium 4 3.2 machine with 1gb of RAM, loading the control center for the first time feels like almost a full minute of waiting for something to happen. As commenters on [Junfeng Zhang’s log](https://web.archive.org/web/20060323223615/http://blogs.msdn.com/junfeng/archive/2004/09/19/231628.aspx) point out, this is likely due more to poor coding than anything else. But what really irks me is that **all I want to do is adjust a few minor video card settings**. Is it really appropriate to have such a heavyweight app for such a simple task?


Which brings me back to using managed code in appropriate places. Although there was a bit of a hubbub about managed code and Vista last year, Microsoft is pursuing managed code aggressively, as Dan Fernandez notes in debunking the [Microsoft’s not using Manged Code Myth](https://web.archive.org/web/20060208090241/http://blogs.msdn.com/danielfe/archive/2005/12/16/504847.aspx). He provides a succinct list of recent Microsoft products and the number of lines of managed code in each one:

- Visual Studio 2005: 7.5 million lines
- SQL Server 2005: 3 million lines
- BizTalk Server: 2 million lines
- Visual Studio Team System: 1.7 million lines
- Windows Presentation Foundation: 900K lines
- Windows Sharepoint Services: 750K lines
- Expression Interactive Designer: 250K lines
- Sharepoint Portal Server: 200K lines
- Content Management Server: 100K lines


Managed code is great. But a world where everything is managed code – including the operating system and essential utilities – is still pretty far off.

[.net](https://blog.codinghorror.com/tag/net/)
[managed code](https://blog.codinghorror.com/tag/managed-code/)
[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[technology trends](https://blog.codinghorror.com/tag/technology-trends/)
