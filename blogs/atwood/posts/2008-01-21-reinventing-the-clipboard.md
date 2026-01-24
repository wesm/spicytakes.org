---
title: "Reinventing the Clipboard"
date: 2008-01-21
url: https://blog.codinghorror.com/reinventing-the-clipboard/
slug: reinventing-the-clipboard
word_count: 713
---

Over time, I’ve become something of a desktop minimalist. Sure, I’ll change a few settings to my liking, but I no longer spend a lot of time [customizing my desktop configuration](https://blog.codinghorror.com/the-problem-with-configurability/). I’ve learned that if the defaults aren’t reasonably close to correct out of the box, then the software is probably doomed anyway. For most users the default settings are [the only settings](https://blog.codinghorror.com/the-power-of-defaults/).


One of the things I *always* have to change, much to my chagrin, is the default clipboard behavior. I originally [wrote about this in 2005](https://blog.codinghorror.com/improving-the-clipboard/):


> In this era of 3 GHz processors, 1 GB memory, and 500 GB hard drives, **why is the Windows clipboard only capable of holding a single item?** Sure, you have fancy multi-level undo and redo in applications like Microsoft Word and Visual Studio. But not the clipboard. It holds *exactly one item*. Copy another item to the clipboard and your previous clipboard item is irrevocably lost.


The only improvement since then, sadly, is in the PC specifications. Three years later, we’re stuck with the same old single-item clipboard model. The clipboard isn’t some obscure operating system feature, either. People use it all the time. There’s actually hard data to back this up, at least for Word 2003:

kg-card-begin: html

> Top 5 Most-Used Commands in Microsoft Word 2003
> **Paste** 
> Save 
> **Copy** 
> Undo 
> Bold 
> Together, these five commands account for around 32% of the total command use in Word 2003. Paste itself accounts for more than 11% of all commands used, and has more than twice as much usage as the #2 entry on the list, Save.

kg-card-end: html

Granted, we’re talking about a word processing program here, but we live in a [copypasta](http://www.urbandictionary.com/define.php?term=copypasta) culture. I find that even when I’m not writing, per se, I rely on my clipboard throughout the day. The clipboard is so important that Walter Mossberg specifically mentioned it as a negative in [his iPhone review](https://web.archive.org/web/20080209220716/http://solution.allthingsd.com/20070626/the-iphone-is-breakthrough-handheld-computer/):


> There’s also no way to cut, copy, or paste text.


This is on a *phone*, mind you. I’m totally with Walt on this one; it applies to all smartphones. I was surprised how quickly I ran into situations where I wanted to copy and paste something on my Windows Mobile phone, but I couldn’t figure out how to. It’s not a crippling limitation, but it does illustrate how fundamental the clipboard is, even for the smallest of computers.


It always seemed strange to me that applications had to implement their own oddball per-app clipboard queues to **spackle over deficiencies in the operating system’s braindead “I can only remember one thing at a time” clipboard implementation**. We’ve long since left the days of applications writing their own quirky little file open dialog behind, but it’s somehow OK to implement your own wacky clipboard behaviors in Visual Studio, or Office?


If, like me, you’d prefer operating system level improvements in the clipboard, there are quite a few options out there. I’ve been quite happy with ClipX. After installing this lightweight little app, instead of pressing


![](https://blog.codinghorror.com/content/images/2025/03/image-438.png)


to paste a single item, you can opt to press


![](https://blog.codinghorror.com/content/images/2025/03/image-437.png)


whereupon you’re presented with a menu of recent clipboard items, in a nice visual menu browser format:


![](https://blog.codinghorror.com/content/images/2025/03/image-441.png)


Your clipboard history is dynamically saved to disk and will **survive a reboot**, so you can begin to rely on your clipboard as a sort of quick and dirty digital scrapbook. Isn’t that how it should have been all along?


I’ve become terribly reliant on this improved clipboard behavior, so I always install ClipX on any machine I’m working on. It has some additional default clipboard functions that I’ve also found quite useful:


![](https://blog.codinghorror.com/content/images/2025/03/image-439.png)


perform a Google search using the contents of the clipboard.


![](https://blog.codinghorror.com/content/images/2025/03/image-440.png)


open a browser and navigate to the address in the clipboard.


It doesn’t matter whether you specifically choose ClipX. It’s these **three key improvements in the operating system clipboard** that I think are important:

1. history
2. persistence
3. visual browser


It’s a mystery to me why none of the major operating systems have bothered improving the clipboard. It seems entirely possible to add these enhancements without breaking the simple clipboard paradigms that have been around since the days of Xerox PARC.

[operating systems](https://blog.codinghorror.com/tag/operating-systems/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[user experience](https://blog.codinghorror.com/tag/user-experience/)
