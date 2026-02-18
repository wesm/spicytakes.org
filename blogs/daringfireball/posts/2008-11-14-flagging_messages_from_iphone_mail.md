---
title: "Flagging Messages From iPhone Mail"
date: 2008-11-14
url: https://daringfireball.net/2008/11/flagging_messages_from_iphone_mail
slug: flagging_messages_from_iphone_mail
word_count: 944
---


My email “system”, such that it is, is pretty simple. For each of my main accounts I use just two mailboxes: an inbox and an archive. The inbox is for new mail, and the archive is where all messages go when I’m done with them. I can’t say I follow [Inbox Zero](http://www.43folders.com/izero), Ringo, but I’m trying. I’m tryin’ real hard to be a shepherd.


One habit I’ve found to be harmful is using “unread” to mean anything other than “new message”. For years, I’d let email I didn’t want to deal with immediately sit “unread” in my inbox, and I’d eventually wind up with hundreds of “unread” messages. I put quotes around *unread* because most of those messages weren’t literally unread — I’d looked at them, but then marked them unread because I didn’t want to deal with them yet. Breaking myself of this habit significantly increased my email efficiency.


I have three main accounts, and at this moment, they have 2, 24, and 18 messages in their inboxes. Not zero, but not out of control. At one point about two years ago, I had over 4,000 unread messages in the inbox for my public contact address for Daring Fireball. I had actually read, or at least skimmed, most of those, but at that point there was no way to catch up, and no way to identify the older messages that I’d truly never even looked at.


What I do for messages I want to keep in my inbox after reading, for whatever reason, is mark them as flagged. In my system, all that flagging implies is that I want to keep the message in my inbox. Of those aforementioned 2, 24, and 18 messages in my inboxes at this moment, all of them are flagged, and *none* of them are marked unread. So while I’m not — and to be honest, never am — at *inbox* zero, I am almost always, at the end of each day, at *unread* zero.


In one regard, the iPhone has been a tremendous boon to keeping my email manageable. Pre-iPhone, I’d often fall woefully behind on email from DF readers while I was traveling. The iPhone makes it easy to read messages here and there, a few minutes at a time, throughout the day. Have a few minutes? Read a few messages.


But the iPhone Mail app’s lack of support for flagging has been a constant irritation. The primary thing I want to do with email on the iPhone is *triage* — most messages I can read once and forget. I’ve written before about [the AppleScript I wrote that moves read, unflagged messages](http://daringfireball.net/2007/07/simple_inbox_sweeper) from my inboxes to their corresponding archive mailboxes. I don’t bother moving messages from the inbox to the archive folder one at a time, either on my Mac or on my iPhone. I just let that script move them all at once a few times a day.


The problem with the iPhone’s lack of support for flagging is what to do with messages I read on the iPhone, but which I want to deal with later. Most times it’s simply a case of a message which demands a response that would be too long to peck out on the iPhone keyboard. Without flagging, I took to marking such messages unread. But that never sat right with me — both because I’d already broken the habit of using “unread” in this way on the desktop, and because it completely throws off the utility of the unread message count in Mail’s icon badge. I really want the number in that badge to represent *new* messages, not *new messages and all the old ones marked unread because you didn’t want to deal with them on the iPhone*.


What I really want is to be able to mark messages as flagged using the iPhone. But, absent that, I’ve come up with a simple workaround that’s worked well for me. Here’s how it works:

1. In each IMAP account I access from my iPhone, I’ve created a new
top-level mailbox named “[Flag]” — one mailbox with the same
name in each account. The name isn’t special — I added the
brackets because most of my accounts are hosted at Gmail, and
“[Flag]” sorts alphabetically before the magic server-side
“[Gmail]” folder.
2. From the iPhone, whenever I read a message I want to flag, I move
it to that account’s “[Flag]” mailbox. It takes just two quick taps.
3. When next I read email on my Mac, I run the AppleScript shown
below. The script is very simple — it looks through every IMAP
account looking for mailboxes named “[Flag]”. When it finds one,
it sets the flag status for every message therein and moves them
back to that account’s inbox.


Here’s the source to the AppleScript. If you want to use a mailbox name other than “[Flag]”, just change the string on line 6.


```
tell application "Mail"
    set _imap_accts to every imap account
    set _count to 0
    repeat with _acct in _imap_accts
        try
            set _flagbox to mailbox "[Flag]" of _acct
            set _count to _count + (count messages of _flagbox)
            set flagged status of every message of _flagbox to true
            move every message of _flagbox to mailbox "INBOX" of _acct
        end try
    end repeat

    if _count is 1 then
        set _msg_string to " message."
    else
        set _msg_string to " messages."
    end if
    display alert "Flagged and moved " & _count & _msg_string
end tell

```


To use it, copy the source, paste it into Script Editor, and save the script in your *~/Library/Scripts/Applications/Mail/* folder.



| **Previous:** | [Executive Scuttlebutt](https://daringfireball.net/2008/11/executive_scuttlebutt) |
| **Next:** | [iPhone-Optimized Google Search Results](https://daringfireball.net/2008/11/iphone_optimized_google_results) |


PreviousNext