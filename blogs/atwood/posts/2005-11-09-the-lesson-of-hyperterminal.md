---
title: "The Lesson of HyperTerminal"
date: 2005-11-09
url: https://blog.codinghorror.com/the-lesson-of-hyperterminal/
slug: the-lesson-of-hyperterminal
word_count: 666
---

In response to [My Giant Calculator](https://blog.codinghorror.com/my-giant-calculator/), Joost commented:


> *I’ll jump to the defense of trusty old calc.exe. Even though it’s crappy, **we know it’s on every Windows box we touch.***


He’s got a point. The applets that ship in the box with the operating system are, like it or not, the defaults. There might be a dozen better third-party alternatives, but that requires manual intervention and special customization. Which means on any particular computer you happen to use, the odds of double-clicking a text file and getting Notepad are about... 99.9 percent.


The really unfortunate thing about Notepad is that – at the risk of stating the obvious – it sucks. Notepad was minimalist by Windows 95 standards. I just read that Windows Vista will ship with a virtually unchanged version of Notepad, ten years later. The idea that we’ll be viewing readme.txt files into 2010 with nothing but no-frills Notepad is unconscionable.


I know it sounds trivial. **But isn’t the fit and finish of little applets like these – Notepad, Calculator, Character Map, Paint, Disk Cleanup, Compressed Folders, and dozens of others – indicative of the care and design that goes into the entire operating system?** If Microsoft can’t be bothered to bundle a version of Notepad that has basic amenities like a toolbar, what hope does the rest of the operating system have?


I understand that there are a finite number of developer hours available to work on Vista. If it’s a choice between new versions of Windows Explorer and Internet Explorer and a bigger, better Notepad, that’s not a choice at all. The core OS should have priority.


But why does it have to be this kind of either-or dilemma? **Why doesn’t Microsoft simply license a better notepad and bundle it with Vista? **They’ve gone this route before. Do you remember HyperTerminal?


![](https://blog.codinghorror.com/content/images/2025/03/image-351.png)


Rather than write their own terminal emulation app, Microsoft chose to [license one from Hilgraeve](http://www.hilgraeve.com/htpe/) and bundle it with Windows 95. As a guy who used to write a whole lot of serial communication code in a past life, I can tell you that HyperTerminal was* a pretty damn robust terminal applet. Certainly far more application than we’d have ever gotten from Microsoft.


Why doesn’t Microsoft similarly license “lite” versions of the most popular third-party calculator, notepad and paint replacements for inclusion in Vista? This seems like a win-win situation for everyone:

- **Microsoft customers** get far more functionality in the box. For example, because of the massive deficiencies in Windows XP’s Compressed Folder support I still have to install WinZip, even though my needs are quite modest. Why not just license WinZip?
- **Third party application developers** get huge sales opportunities from upselling the full version of their applet to the massive base of Windows users. Hilgraeve still has a web page hawking HyperTerminal upgrades many, many years after the fact.
- **Microsoft developers** can focus on the core operating system. That’s one less thing they have to worry about coding. And given the sorry state of the current Windows applets, would you really want a Microsoft developer to code it anyway? A third party whose entire business revolves around a calculator replacement will have a deeper, more vested interest in building a great calculator applet than any Microsoft employee ever will.


I’m not advocating blindly dumping dozens of different applets from dozens of different vendors into the core operating system. Microsoft would still have to be intimately involved with the source code they’re shipping. After all, it has their name on it, so the quality control would have to be extreme. I’m guessing most applet vendors would give their eyeteeth for a sales opportunity like this, and thus would bend over backwards to whip their code into shape.


*HyperTerminal is still in Windows XP under the Programs | Accessories | Communications menu. Hilgraeve’s name, however, was banished to a “portions copyright” footnote in the about dialog.

[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[user experience](https://blog.codinghorror.com/tag/user-experience/)
[technology trends](https://blog.codinghorror.com/tag/technology-trends/)
[default applications](https://blog.codinghorror.com/tag/default-applications/)
[windows applications](https://blog.codinghorror.com/tag/windows-applications/)
