---
title: "Improving the Clipboard"
date: 2005-10-30
url: https://blog.codinghorror.com/improving-the-clipboard/
slug: improving-the-clipboard
word_count: 326
---

In this era of 3ghz processors, 1gb memory, and 500gb hard drives, **why is the Windows clipboard only capable of holding a single item?** Sure, you have fancy multi-level undo and redo in applications like Microsoft Word and Visual Studio. Did you know that the humble Windows textbox supports a surprisingly deep undo/redo queue via the CTRL+Z (undo) and CTRL+Y (redo) keys?


But not the clipboard. It holds exactly one item. Copy another item to the clipboard and your previous clipboard item is irrevocably lost.


The clipboard is a model of simplicity. And that’s admirable. But I think it’s too simple. Adding a basic FIFO queue of clipboard items wouldn’t affect typical usage – but it would provide much richer functionality for intermediate and advanced users. Here’s one such clipboard utility that I use, [clcl](http://www.nakka.com/soft/clcl/index_eng.html). This lightweight utility launches when I press the ALT+C key, and presents a straightforward menu of recent clipboard items:


![](https://blog.codinghorror.com/content/images/2025/03/image-342.png)


Of course, CTRL+C and CTRL+V still work as you would expect. I can’t even tell you how many times I’ve been editing code in Visual Studio and accidentally overwritten the code I copied to the clipboard. Now I don’t have to worry; I can just press ALT+C and then use the arrow keys or the number to select the clipboard item I want to paste. **The clipboard is a heck of a lot more useful to me when I don’t have to constantly worry about losing the one item on it**. Clcl even persists the clipboard items to disk so they survive a reboot.


I liked clcl’s simplicity, but there are [dozens of similar clipboard utilities](https://web.archive.org/web/20051107092400/http://zdnet.com.com/3150-2384-0.html). To me, that’s is a sign that **better clipboard functionality really should be built into the operating system**. Unfortunately, I can’t find any reference to clipboard improvements in Vista. It’d be a darn shame if we’re stuck with the archaic single item clipboard for another five years.

[clipboard](https://blog.codinghorror.com/tag/clipboard/)
[software development](https://blog.codinghorror.com/tag/software-development/)
[user experience](https://blog.codinghorror.com/tag/user-experience/)
[technology trends](https://blog.codinghorror.com/tag/technology-trends/)
[productivity](https://blog.codinghorror.com/tag/productivity/)
