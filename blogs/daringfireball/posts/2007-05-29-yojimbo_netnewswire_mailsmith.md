---
title: "Yojimbo Import Scripts for Mailsmith and NetNewsWire"
date: 2007-05-29
url: https://daringfireball.net/2007/05/yojimbo_netnewswire_mailsmith
slug: yojimbo_netnewswire_mailsmith
word_count: 541
---


The central point of [Yojimbo](http://barebones.com/products/yojimbo/), as I see it, is that you can just throw bits of information into it without really thinking much at all. It’s a deceptively simple application, and most of the places where it gets particularly clever — like, say, [the Drop Dock and the Quick Input window](http://barebones.com/products/yojimbo/tour-input.shtml) — share the same fundamental purpose: to make it as easy and frictionless as possible to add new bits of information.


But even with those built-in conveniences, when I repeatedly send bits of information into Yojimbo from the same source application, I find that it’s worthwhile to write AppleScripts to make it even easier. Here are some examples for [Mailsmith](http://barebones.com/products/mailsmith/) and [NetNewsWire](http://www.newsgator.com/Individuals/NetNewsWire/).


(These scripts are relatively long, so rather than include their source code in the article itself, I’ve created a separate page for the source for each script. To use the scripts, click the script names to view the source, then copy and paste into your AppleScript editor of choice.)


## [Create Yojimbo Notes From Mailsmith Messages](http://daringfireball.net/misc/2007/05/mailsmith-to-yojimbo)


This script creates a new Yojimbo note for each selected message in Mailsmith, with the note title set to the message subject.


By default, the content of each Yojimbo note is the entire body of the email message. If only one message is selected in Mailsmith, however, you can select a portion of the message body before running the script, and only the selected text of the message will be sent to Yojimbo. The Yojimbo notes begin with four of the header fields: From, To, Date, and Subject.


## [Create Yojimbo Bookmark From NetNewsWire, With Tags](http://daringfireball.net/misc/2007/05/nnw-to-yojimbo-bookmark)


(Based heavily on [this script by Fraser Speirs](http://www.speirs.org/wiki/Scripts#Add_selected_NetNewsWire_headlines_to_Yojimbo).)


When invoked, a new Yojimbo bookmark will be created based on the currently selected headline in NetNewsWire.


The primary difference from Fraser Speirs’s original version is that my script uses a simple dialog box to prompt for tags, which must be separated by “, ” — that is, comma-space. In other words, if you enter “foo, bar” in the tag dialog, the bookmark will have two tags applied, “foo” and “bar”. But if you enter “foo,bar”, there will be just one tag, “foo,bar”, including the literal comma.


Here’s the section of the script that prompts for tags:


```
set _tags to {}
try
    display dialog "Tags:" default answer ""
    set _answer to text returned of result
    if _answer is not "" then
        set AppleScript's text item delimiters to ", "
        set _tags to text items of _answer
    end if
end try

```


This creates an AppleScript list, `_tags`, containing one item for each tag. To apply these tags, we first create the new item in Yojimbo, then add the tags to the newly created item:


```
tell application "Yojimbo"
    set _new_item to (make new bookmark item ¬
        with properties {name:newItemTitle, location:h_URL})
    add tags _tags to _new_item
end tell

```


(Creating a version of the Mailsmith script that prompts for tags, or which uses Growl for notifications, is left as an exercise for the reader.)


## [Create Yojimbo Web Archive From NetNewsWire, With Tags](http://daringfireball.net/misc/2007/05/nnw-to-yojimbo-web-archive)


Nearly identical to the previous script, but it creates Yojimbo web archives instead of bookmarks.



| **Previous:** | [Enjackass](https://daringfireball.net/2007/05/enjackass) |
| **Next:** | [iPhone SDK, iPhone SDK! Wherefore Art Thou iPhone SDK?](https://daringfireball.net/2007/06/wherefore_art_thou_iphone_sdk) |


PreviousNext