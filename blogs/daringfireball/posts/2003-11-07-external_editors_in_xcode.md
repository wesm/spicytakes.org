---
title: "External Editors in Xcode"
date: 2003-11-07
url: https://daringfireball.net/2003/11/external_editors_in_xcode
slug: external_editors_in_xcode
word_count: 500
---


Some programmers grow very attached to their favorite text editor. (Yours truly: guilty as charged.) It’s not a phenomenon particular to any one editor; there are adherents for just about every serious programming editor: Emacs, Vim, BBEdit, [jEdit](http://jedit.sourceforge.net/) — hell, even [Alpha](http://bumppo.net/archives/2003/11/index.html#000321). The list is long.


Many other programmers — maybe most, in fact — don’t have any particular allegiance to a single text editor. They’ll happily use whatever is handy.


Most modern-day programming IDEs contain a built-in text editor. (*IDE* = Integrated Development Environment.) The two most significant IDEs for Mac OS X are CodeWarrior and Xcode (née Project Builder). CodeWarrior’s IDE contains a very BBEdit-ish editor. But it’s not BBEdit, and CodeWarrior has long-supported external editors, so that you can use your own preferred editor instead of their built-in jobby.


Project Builder, on the other hand, did not support external editors when Mac OS X debuted. Most programmers were satisfied using Project Builder’s built-in editor, but others — the aforementioned ones who are attached to their own very favorite editor — were not. You could *use* an external editor alongside Project Builder, using drag-and-drop to drag source files onto another editor’s Dock icon, for example. But that’s a far cry from explicit built-in external editor support.


And so these programmers would ask Project Builder’s developers, “Please add external editor support to Project Builder, so that I can use my favorite editor instead of Project Builder’s.”


The response from Project Builder’s developers was — and admittedly this is paraphrasing — “What features in your favorite editor would you like to see us add to Project Builder?”


“I’m not asking you to add features from my favorite editor to Project Builder; I just want to write code using my favorite editor.”


“What features in your favorite editor would you like to see us add to Project Builder?”


And so forth.


Eventually the requests wore Project Builder’s development team down, and last year, they added external editing support to Project Builder, and it’s still there in Xcode.


But, are any Project Builder/Xcode users actually *happy* with this external editor support? *Anyone?* It’s not like I’m in contact with hundreds of developers, but I do know several, and I don’t know one who is happy with it.


And, as described by [Nat Irons](http://bumppo.net/archives/2003/11/index.html#000321) and [Michael Tsai](http://mjtsai.com/blog/2003/11/06/xcode_external_editors.html), external editor support is *worse* in Xcode than it was in Jaguar’s Project Builder.


*Good* external editor support in Xcode would make a lot of programmers very, very happy. And so it’s hard to understand why it hasn’t happened. It’s not because Xcode’s built-in editor is like totally rad, because it’s really rather pedestrian (e.g. no support for regular expression searching in the single-file Find dialog). It would be a lot less work to add terrific external editor support to Xcode than it would be to turn Xcode’s built-in editor into a terrific text editor.


If I’m wrong, please, let me know.



| **Previous:** | [Run Panther Run](https://daringfireball.net/2003/11/run_panther_run) |
| **Next:** | [SmartyPants 1.4.1](https://daringfireball.net/2003/11/smartypants_141) |


PreviousNext