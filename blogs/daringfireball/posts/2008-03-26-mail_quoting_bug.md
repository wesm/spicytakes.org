---
title: "Quoting Attribution Bug in Apple Mail After Upgrading to Safari 3.1"
date: 2008-03-26
url: https://daringfireball.net/2008/03/mail_quoting_bug
slug: mail_quoting_bug
word_count: 613
---


Longtime readers are perhaps aware that I’m somewhat particular about the formatting of the email I send. About a week ago, I noticed that Apple Mail had changed the way it formats replies.


The way it used to work, and the way it *should* work, is that there should be a blank line between the attribution and the quoted text, like this:


```
On Mar 25, 2008, at 8:36 PM, Jane Doe wrote:

> First quoted line of reply here.

```


What I noticed a week ago is that it now looked like this:


```
On Mar 25, 2008, at 8:36 PM, Jane Doe wrote:
> First quoted line of reply here.

```


[**Update:** This bug was introduced by Safari 3.1, and was fixed with Safari 3.1.1 on 16 April 2008.]


I hadn’t changed any settings in Mail (and, in fact, am not aware of any settings in Mail that could effect such a change). I asked on Twitter if anyone else had seen this, and several others confirmed it, albeit with [widely varying estimations](http://quotably.com/gruber/statuses/776338413) of when they first noticed it, including several who thought it began with 10.5.0. The weird part, though, is that some users, even on 10.5.2, didn’t see the bug.


Here’s [the clue that broke the case](http://twitter.com/secretaboutbox/statuses/776358010) wide open:


> There’s a blank line on a 10.4.11 machine in my office here, but
> it does *not* have the new WebKit update. Mail uses WebKit.


The steps to reproduce the bug:

1. Install Safari 3.1.
2. Make sure Mail’s “Message Format” preference is set to Plain Text, not Rich Text. The bug doesn’t occur with Rich Text messages.


I tested the behavior on both Mac OS X 10.5.2 and 10.4.11, before and after upgrading to Safari 3.1. Neither system exhibited the bug with Safari 3.0.4 installed. Both systems exhibited the bug after upgrading to Safari 3.1 and the corresponding new version of WebKit.1


Many of you might be thinking that this is crazy — how could a new version of WebKit introduce a bug into Mail? Easy: Mail’s message editing view is an editable WebKit control.


## AppleScript Workaround


Most people aren’t even affected by this bug because Apple Mail defaults to the rich text message format. Among those who prefer to send plain text, most people will ignore the bug. For those few who, like me, prefer plain text and cannot ignore the bug, I have a solution.


Back in July when I first switched to Mail, I published [this AppleScript to change the format of replies](http://daringfireball.net/2007/07/non_top_posting_scripts) to one that doesn’t presume you’ll be engaging in the uncouth, illiterate practice of top-posting. With the modifications below, the script now adds the proper blank line after the attribution line.


```
tell application "Mail" to activate

tell application "System Events"
    tell process "Mail"
        tell menu bar 1
            click menu bar item "Message"'s menu "Message"'s ¬
                menu item "Reply"
        end tell
        delay 0.5
        key code 117 -- Forward Delete to nuke top blank line

        -- Add blank line after attribution line:
        key code 124 using command down -- Cmd-RightArrow
        key code 36 -- Return

        -- Fix trailing whitespace
        key code 125 using command down -- move to bottom
        key code 123 using option down -- Option-LeftArrow
        key code 124 using command down -- Cmd-RightArrow
        key code 117 using option down -- Option-ForwardDelete
        key code 36 -- Return
        key code 36
    end tell
end tell

```


See [the original article](http://daringfireball.net/2007/07/non_top_posting_scripts) for installation instructions, how to assign the script to run when you invoke Command-R, and a few caveats.


---

1. And, yes, I filed a bug: [rdar://5820749](rdar://5820749). ↩︎



| **Previous:** | [Update](https://daringfireball.net/2008/03/update) |
| **Next:** | [T-Shirts and Memberships, 2008](https://daringfireball.net/2008/03/tshirts_and_memberships) |


PreviousNext