---
title: "Simple Inbox Archiving Script for Apple Mail"
date: 2007-07-16
url: https://daringfireball.net/2007/07/simple_inbox_sweeper
slug: simple_inbox_sweeper
word_count: 521
---


[**Update 4 July 2011:** The script in this post has been updated slightly to work around a bug in Apple Mail in Mac OS X 10.7.0. You can use the version history on [this script’s Gist page](https://gist.github.com/1063605) to see what changed. I’ve tested the version below on both 10.6.8 and 10.7.0.]


I’m using a fairly simple mailbox structure in Apple Mail. In each of my IMAP accounts, I’ve created an [“Archive” mailbox](http://daringfireball.net/misc/2007/07/mailbox-list.png). Once a day or so, I move all the unflagged, read messages from each inbox to the corresponding Archive mailbox for that account.


Here’s an AppleScript that automates this inbox sweeping. It assumes that every IMAP account (including .Mac accounts) has an Archive mailbox.


```
-- The following should be one long line:
set _description to "All unflagged, read messages in each IMAP account 
    inbox will be moved to the “Archive” mailbox corresponding to that  
    account. This action is not undoable."

tell application "Mail"
    display alert "Archive read messages from IMAP inboxes?" buttons ¬
        {"Cancel", "Archive"} cancel button 1 message _description

    repeat with _acct in imap accounts
        set _acct_name to name of _acct
        set _inbox to _acct's mailbox "INBOX"
        try
            set _archive_box to _acct's mailbox "Archive"
        on error
            display alert "No “Archive” mailbox found for account “" & ¬
                _acct_name & "”."
            return -- Stop the script
        end try

        -- Begin update for OS X 10.7.0
        set _msgs_to_move to (a reference to ¬
            (every message of _inbox ¬
                whose flagged status is false and read status is true))
        set _msg_list to contents of _msgs_to_move
        if (_msg_list's length > 0) then
            move _msgs_to_move to _archive_box
        end if
        -- End update for 10.7.0

    end repeat
end tell

```


The point is to make it as easy as possible to keep my inboxes clear of everything other than unread and flagged messages.


Notes:

- This is a nice example of using a `whose` clause to
create a filtered reference to a list of items that meet
certain criteria — in this case, the read, unflagged
messages of each inbox. Mail’s scripting support also allows
us to move the entire list of messages en masse. I.e. we
don’t need to loop through each message in the inboxes one at
a time to find the read unflagged ones, and we don’t need to
move them one at a time to the Archive mailboxes.
- The script itself seems to run pretty fast in my use (mainly
because of the aforementioned point that it doesn’t loop
through messages one at a time), but it might take a few
seconds for Mail to finish moving the messages out of your
inboxes. Use Mail’s Activity Viewer to watch the progress
of the messages being moved.
- If you’d instead prefer to move messages to a mailbox on
your Mac rather than on your IMAP server, just change this
line:
`move _msg_list to _archive_box
`
to something like:
`move _msg_list to mailbox "Archive Mailbox Name"
`
or, if it’s a sub-mailbox in a hierarchy:
`move _msg_list to mailbox "Top-Level Mailbox/Archive Mailbox Name"
`



| **Previous:** | [‘OS X iPod’ Nonsense](https://daringfireball.net/2007/07/os_x_ipod_nonsense) |
| **Next:** | [iPhone Fonts](https://daringfireball.net/2007/07/iphone_fonts) |


PreviousNext