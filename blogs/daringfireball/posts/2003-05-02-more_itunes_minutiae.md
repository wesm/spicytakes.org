---
title: "More iTunes Minutiae"
date: 2003-05-02
url: https://daringfireball.net/2003/05/more_itunes_minutiae
slug: more_itunes_minutiae
word_count: 346
---


## Window Resizing


Yesterday I pointed out that on faster Macs, when you resize windows, iTunes uses live resizing, but on slower Macs, it uses old-fashioned outline resizing. I guessed that the determining factor between “fast” and “slow” was the presence of Quartz Extreme. Email from readers indicates this is wrong; instead, the cut-off seems to be your processor. If you have a G4, iTunes uses live resizing; if you have a G3, it uses outline resizing.


Russ Harlan and E.J. Campbell both emailed an interesting tip: even on a G4, you can suppress live resizing in iTunes by holding down the Command key. This would be quite useful system-wide.


## Ugly Fonts


Several readers have sent email inquiring about “ugly” fonts in iTunes 4. I don’t see this problem, but I think I know what’s going on. See [Nat Irons’s description and solution](http://bumppo.net/archives/2003/05/index.html#000254) for details. (The very short answer is that you need to set your anti-aliasing threshold in System Prefs’ General panel to the default 8 points.)


## Hidden Menu


Mac OS X Hints yesterday published an item pointing to [a hidden menu in iTunes 4](http://www.macosxhints.com/article.php?story=20030429125015757#comments):


> To access the menu and see the shortcuts, click the Window menu, and then press the right arrow. You can move to the Search field, Preferences, Home, Back, and Forward.


This is definitely a little squirrelly. My guess, however, is that this is not a bug, per se, but rather it’s how iTunes is implementing keyboard shortcuts for commands that aren’t regular menu items. E.g. they wanted to allow Cmd-Opt-F to take you to the Search field, but didn’t want to put “Target Search Field” in one of the normal menus. The duplicate Preferences command is there because they wanted to continue supporting the old shortcut (Cmd-Y) but also support the official new standard shortcut (Cmd-,) for the “real” Preferences command in the application menu. I think they would have been better off just getting rid of the old prefs shortcut.



| **Previous:** | [Et Tu iTunes?](https://daringfireball.net/2003/05/et_tu_itunes) |
| **Next:** | [The Problems With Click-Through](https://daringfireball.net/2003/05/the_problems_with_click-through) |


PreviousNext