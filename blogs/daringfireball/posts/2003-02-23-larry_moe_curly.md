---
title: "Larry, Moe, Curly"
date: 2003-02-23
url: https://daringfireball.net/2003/02/larry_moe_curly
slug: larry_moe_curly
word_count: 891
---


In “[Short and Curlies](http://daringfireball.net/2003/02/short_and_curlies.html)” yesterday, I posted a short AppleScript for BBEdit (and Mailsmith) that converts curly quotes, ellipses, and en- and em-dashes to their corresponding plain ASCII equivalents (three dots for an ellipsis, two hyphens for an em-dash, etc.).


[Dan Pouliot](http://www.webmastermac.com/) asked via email why I didn’t write the script using BBEdit’s “Convert to ASCII” plug-in. The answer: because I forgot that the Convert to ASCII plug-in is scriptable.


My original 14-line script can be replaced by just three lines:


```

tell application "BBEdit"
    convert to ASCII with change in place and selection only
end tell

```


The `change in place` and `selection only` options give the script the same behavior as my original script: if there is a selection, only the selected text will be converted; if there’s no selection, the entire front window will be converted. In addition, the new script has the following advantages:

- It’s faster. The old script wasn’t slow, per se, but the repeated
search-and-replace operations took a fraction of a second each. The
Convert to ASCII plug-in works nearly instantaneously.
- It doesn’t screw up your undo stack. When the original script runs, each search-and-replace action counts as a separate action in BBEdit’s multiple undo stack. So after running the script, you’d need to Undo five times to get back to where you were before running the script. The Convert to ASCII command is atomic, so you can just hit Undo once.
- It converts way more characters to ASCII. The original only converted quotes, em- and en-dashes, and ellipses. The Convert to ASCII command translates just about any character you can throw at. Trademark ™ and copyright © symbols are converted to “(TM)” and “(c)”. Accented characters like “é” are converted to their unaccented counterparts. And so on.


Note also that the same script can be used in Mailsmith by simply changing the `tell application` target to “Mailsmith”.


## Translate Text to HTML


OK, so now we have a one-keystroke solution for converting curly quotes to plain ASCII. But what if you don’t want plain ASCII, but instead you want to convert non-ASCII characters to their corresponding HTML entities? Instead of, say, turning literal curly quotes into straight quotes, you want to turn them into curly quote HTML entities.


BBEdit’s Translate command is the answer. In the menus, it’s “Markup → Utilities → Translate…”, but it’s so useful that you’ll want to remember the keyboard shortcut: by default, Command-Option-T.


The Translate command is so useful, and so convenient, that it’s easy for an old BBEdit user like yours truly to forget that many people might not know about it. The Translate command works in both directions: “Text to HTML” turns non-ASCII characters into entities; “HTML to Text” translates entities back to normal characters.


When translating text to HTML, turning on the “Paragraphs” checkbox tells BBEdit to wrap `<p>` tags around each block of lines. Turn this off if your input already has `<p>` tags. Likewise, if your input text already has HTML tags of any kind, turn on the “Ignore < and >” checkbox; otherwise, the angle brackets will be translated into `&lt;` and `&gt;` entities.


If you apply the same Translate settings on a regular basis, you can
skip the dialog box by creating an AppleScript to perform the
translation. Unfortunately, like many of BBEdit’s Markup commands, Translate is not recordable. But its syntax is fairly straightforward. Here’s a script I use frequently when writing HTML (including when I write Fireballs):


```

tell application "BBEdit"
    translate text to html entity encoding method entity name value ¬
        with entity conversion, ignore angle brackets and selection only ¬
        without create new document and paragraph conversion
end tell

```


“`entity encoding method entity name value`” tells BBEdit to use named HTML entities, such as `&trade;` for the trademark symbol. If you want decimal- or hexadecimal-encoded entities instead (which for the trademark symbol would produce `&#8482;` and `&#x2122;`, respectively), just specify `entity decimal value` or `entity hex value` instead of `entity name value`.


The next two lines set the boolean options for the command. I definitely want `entity conversion` on, because that’s the main purpose of the script. I want `ignore angle brackets` on also, because my text already contains HTML tags; I don’t want my angle brackets turned into `&lt;` and `&gt;` entities. `selection only` limits the translation to the selected text, but if there is no selection, it translates the entire document.


I want `create new document` off; when it’s on, the translated text goes to a new untitled document window instead of replacing the text in the current window. Lastly, I do not want `paragraph conversion`, because my markup already contains `<p>` tags.


I’ve assigned this script the keyboard shortcut Shift-Command-Option-T; just like the shortcut for the built-in Translate command, plus the Shift key. I use it all the time. The only entity values I have committed to memory are the most common ones. Instead of typing them by hand or using BBEdit’s HTML Entities palette, I just type the actual character. For example, to generate a copyright entity, I type a real © symbol (Option-g), then run my script. So instead of dealing with entities manually, I just type real characters, then run my script.



| **Previous:** | [Short and Curlies](https://daringfireball.net/2003/02/short_and_curlies) |
| **Next:** | [Install Like It’s 1991](https://daringfireball.net/2003/02/install_like_its_1991) |


PreviousNext