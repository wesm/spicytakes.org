---
title: "Can I Get an ‘Hallelujah’ for Auto-Completion With the Esc and F5 Keys?"
date: 2006-10-27
url: https://daringfireball.net/2006/10/hallelujah_autocompletion
slug: hallelujah_autocompletion
word_count: 592
---


Here’s one of those tips that’s not new — it’s been around for at least the last few major releases of Mac OS X, and probably even dates back to NeXTStep — but is very useful, and, I think, not widely known.


The Cocoa text system has a built-in auto-complete feature that is tied to the system-wide spelling checker dictionary. Start typing a word in an app that uses a Cocoa text editing field, hit the Esc key, and you’ll get a drop-down list of suggested completions.


I’ve known about this feature for years, but [I keep forgetting to use it](http://www.flickr.com/photos/textdriveinc/280932458/), even though it’s really quite handy.1 For example, *hallelujah* is one of those words I can never remember how to spell, but I do know that it starts with “halle”. Type that, whack Esc, and you get this:


You can cancel the drop-down list by hitting the Esc key again. You can navigate the drop-down list using the arrow keys, and you can make your selection using the Tab, Return, or Right Arrow keys. Even better, you can use the Space Bar and you’ll get the completion you selected and a space character — i.e. arrow down to the completion you want and then just continue typing (this works with punctuation characters like period and comma, too). It’s pretty clever.


You can also trigger this feature using the F5 key instead of Esc. If I recall correctly, adding the Esc key as an additional binding for this feature was introduced in Mac OS X 10.4; previously, it was only bound to F5. I suspect one reason Apple added Esc as a synonym for F5 is that they’ve started using most of the lower F-keys for hardware features on notebooks; F5, sans the Fn modifier, is bound to Volume Up on all recent iBooks, PowerBooks, and MacBooks.


The F5 shortcut has one significant advantage over Esc — it can be used in contexts where Esc means “Cancel”. For example, in just about any dialog box with a Cancel button, hitting the Esc key invokes that button. The Esc key also closes certain windows, like the default Find window for Cocoa apps. The F5 key still works for invoking the auto-completion feature in these contexts.


[**Update:** Option-Esc seems to work, too — including in all the contexts where just plain Esc doesn’t.]


The suggested completion list is generated from the same word list used by the system-wide spelling checker. Unfortunately, however, the completion feature doesn’t look at your custom word list — i.e. the words you’ve added using the Learn Spelling command. The feature is extensible, however — programmers [can control the list of suggested completions](http://developer.apple.com/documentation/Cocoa/Reference/ApplicationKit/Classes/NSControl_Class/Reference/Reference.html#//apple_ref/occ/instm/NSObject/control:textView:completions:forPartialWordRange:indexOfSelectedItem:). For example, Xcode and SubEthaEdit enhance this feature to allow programmers to use it for auto-completing variable and function names.


---

1. One probable reason why I seem to have a hard time building a habit for this feature is that I spend so much time writing in BBEdit and Mailsmith, neither of which support it. TextMate doesn’t either, for what it’s worth. Michael Tsai’s freeware [BBAutoComplete](http://c-command.com/bbautocomplete/) works with BBEdit and Mailsmith (and any other app with decent support for the AppleScript Text Suite) to add an auto-complete feature based on the words that are already in your open documents, and TextMate has a similar auto-complete feature built-in, but neither of these implementations are tied to the spelling dictionary. ↩︎



| **Previous:** | [Yet More Jackasses: Neal Mueller and the Business Editors of The Washington Post](https://daringfireball.net/2006/10/neal_mueller_washington_post) |
| **Next:** | [Why Is Adobe Soundbooth Intel-Only?](https://daringfireball.net/2006/11/soundbooth_intel) |


PreviousNext