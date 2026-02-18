---
title: "Return and Enter Are Two Different Keys"
date: 2020-07-20
url: https://daringfireball.net/2020/07/return_and_enter
slug: return_and_enter
word_count: 442
---


A New York Times mini crossword clue over the weekend [was based on the notion that “Enter” is just a synonym for the Return key](https://twitter.com/gruber/status/1284970232415768581). It’s not. They’re two different keys that usually perform the same action, but not always.


All keyboards have a dedicated Return key — it’s the big key you’re thinking of above the right Shift key. On a Mac, the [key code](https://manytricks.com/keycodes/) when you press Return is 36, and the glyph for the key is ↵.


A dedicated Enter key is generally only present on extended keyboards with a numeric keypad — it’s the key in the lower-right corner and is generally the only oversized key on the keyboard that is larger vertically, not horizontally. Its Mac key code is 76 and its glyph is ⌅. [Just look at such a keyboard](https://www.apple.com/shop/product/MRMH2LL/A/magic-keyboard-with-numeric-keypad-us-english-space-gray): the Return key says “Return”, and the Enter key says “Enter”.


If your keyboard doesn’t have a dedicated Enter key, you can type the Enter key by pressing Fn-Return. That’s why some Return keys have “Enter” printed in small type above the word “Return”. If your keyboard has neither a dedicated Enter key nor an Fn modifier key, I don’t think you can type Enter, without resorting to sorcery.1


Return and Enter do usually perform the same action, but not always:

- In Tweetbot for Mac, when you’re editing a tweet, Return will insert a newline character; Enter will immediately send the tweet.
- In Script Editor and [Script Debugger](https://latenightsw.com/), Return inserts a newline, but Enter will compile the script.
- In a [BBEdit shell worksheet](http://www.barebones.com/products/bbedit/benefitsintegrate.html#worksheet), Return inserts a newline, but Enter will execute the current line.
- In some spreadsheets (but not Numbers), Return will confirm the contents of the cell you’re editing and move the selection to the next row; Enter will just confirm the contents of the current cell.


As a general rule, when they differ, Return is simply the key for typing a newline character (which, on classic Mac OS, was literally a return character, but let’s not get into that here), whereas Enter *enters* what you’ve already typed without adding a new line.2


---

1. [Keyboard Maestro](https://www.keyboardmaestro.com/main/) is the easiest-to-use and most powerful way to attain such sorcery. You can use Keyboard Maestro to create a macro to simulate typing the Enter key and then assign the macro to whatever keyboard shortcut you want. ↩︎︎
2. In contexts where even the Return key means “send this”, common in chat-type apps such as Messages and Slack, you can use Option-Return to insert a newline character. ↩︎



| **Previous:** | [Refer This](https://daringfireball.net/2020/07/new_york_times_refer_this_dickbar) |
| **Next:** | [Good Sudoku by Zach Gage](https://daringfireball.net/2020/07/good_sudoku_by_zach_gage) |


PreviousNext