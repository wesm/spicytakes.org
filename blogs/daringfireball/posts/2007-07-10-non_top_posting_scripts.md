---
title: "Non-Top-Posting Reply Scripts for Apple Mail"
date: 2007-07-10
url: https://daringfireball.net/2007/07/non_top_posting_scripts
slug: non_top_posting_scripts
word_count: 532
---


For the email accounts that I want to read on my iPhone, I need IMAP, so I’m switching those accounts to Apple Mail. I’ve been dreading this for years.


My first must-fix annoyance is that Mail’s Reply feature is hard-wired to encourage [top-posting](http://www.catb.org/~esr/jargon/html/T/top-post.html), an uncouth and illiterate practice.


Here’s an AppleScript I ginned up to fix this by removing the blank line at the top of each response and moving the insertion point to the bottom of the message. (It uses GUI Scripting, and so requires [Access for Assistive Devices](http://www.apple.com/applescript/uiscripting/01.html) to be turned on.)


```
tell application "Mail" to activate
tell application "System Events"
    tell process "Mail"
        tell menu bar 1
            click menu bar item "Message"'s menu "Message"'s ¬
                menu item "Reply"
        end tell
        delay 0.5
        key code 117 -- Forward Delete
        key code 125 using command down -- down arrow
        key code 36 -- Return
    end tell
end tell

```


Here’s how the script works:

1. First, manually invoke the Reply menu item. This creates a
new message window with the quoted text of the message you’re
responding to, with the insertion point at the beginning of a
blank line at the top.
2. Wait for half a second. Without this `delay` statement, the
following lines sometimes fire before the new message window
has been created and is ready to receive events.
3. Send three `key code` events: forward delete (to remove the
blank line at the top); Command-DownArrow (to move the
insertion point to the end of the message); and Return (to
insert a blank line at the bottom).


I also created a second version of the script to replace Mail’s Reply All command. The only difference is to change `menu item "Reply"` to `menu item "Reply All"`.


I saved both scripts in *~/Library/Scripts/Applications/Mail/* and I assigned them the same menu key shortcuts as Mail’s built-in commands. I use [Red Sweater Software’s FastScripts](http://www.red-sweater.com/fastscripts/) to provide a system-wide scripts menu; when you assign a keyboard shortcut in FastScripts, FastScripts “sees” the shortcut before the current application does, which means that if a script has the same shortcut as a regular menu item — Command-R in the case of Mail’s Reply menu item — the script gets called, not the menu item.


So, in other words, if I manually choose Message → Reply or click the Reply button in Mail’s toolbar, I still get Mail’s standard top-posting style response. To run my script, I use the Command-R shortcut or choose the script from the FastScripts menu.


## Update: Signatures


One shortcoming to this script is that it doesn’t quite work well with mail signatures; it’ll put the insertion point below your signature, rather than between the message and the signature. This problem hadn’t occured to me because I’ve long used [TextExpander](http://www.smileonmymac.com/textexpander/) to include email signatures, rather than the built-in signature feature in Mailsmith (or, now, Mail).


One simple way to work around this would be to add a few up-arrow `key code 126` events to the end of the script. This won’t work, though, if you use multiple signatures with differing numbers of lines.



| **Previous:** | [Jackass of the Week: MSNBC’s Bob Sullivan](https://daringfireball.net/2007/07/bob_sullivan_jackass) |
| **Next:** | [On Top](https://daringfireball.net/2007/07/on_top) |


PreviousNext