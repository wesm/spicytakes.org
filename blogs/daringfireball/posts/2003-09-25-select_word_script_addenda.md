---
title: "‘Select Word’ Script Addenda"
date: 2003-09-25
url: https://daringfireball.net/2003/09/select_word_script_addenda
slug: select_word_script_addenda
word_count: 333
---


A few short follow-up points regarding Tuesday’s “[‘Select Word’ Script for BBEdit](http://daringfireball.net/2003/09/select_word_script_for_bbedit.html)”:


## Option-Arrowing


A slew of people emailed to question the need for a Select Word script, when one can simply use Opt-Shift-LeftArrow and Opt-Shift-RightArrow to select words, which shortcuts work in almost all applications.


Point conceded, but by the same logic, BBEdit’s built-in Select Line command is also superfluous, given that you can use Cmd-Shift-LeftArrow/RightArrow to select lines. The point is not that the Select Line command and Select Word script are *essential* or *necessary*, but simply that they’re very small conveniences.


Opt-Shift-Arrowing is only equivalent to the Select Word script when the insertion point is already at a word boundary; if it’s in the middle of the word you wish to select, you need to first Opt-Arrow in one direction, then Opt-Shift-Arrow in the opposite direction. That’s two quick keystrokes, whereas the script only needs one.


So, yes, I completely agree that my Select Word script is not a big
deal. It’s just a nice little deal. And, also, a nice example for
teaching how to script BBEdit.


## Which Shortcut?


Another question asked by numerous readers is what keyboard shortcut I use to invoke the script. I actually meant to mention this in the original article, but forgot.


I use Control-L, because: (1) it’s analogous to the default shortcuts for BBEdit’s Select Line and Select Paragraph commands (Cmd-L and Cmd-Opt-L, respectively); (2) it’s very easy to type; and (3) it’s available.


(To set a keyboard shortcut for a script in BBEdit [or Mailsmith or TextWrangler], open the Scripts palette and use the Set Key button.)


## Cocoa Keybindings


Sven-S. Porst has an incredibly useful tip for enabling [custom text-editing keybindings for all Cocoa apps](http://earthlingsoft.net/ssp/blog/2003/09/23/selecting_words). Following his advice, you can bind “select word” to Control-L in all Cocoa apps. This has nothing to do with AppleScript — it’s a built-in but hidden feature in Cocoa text-editing fields.



| **Previous:** | [Interview: Michael Tsai](https://daringfireball.net/2003/09/interview_michael_tsai) |
| **Next:** | [Miscellanea](https://daringfireball.net/2003/09/miscellanea) |


PreviousNext