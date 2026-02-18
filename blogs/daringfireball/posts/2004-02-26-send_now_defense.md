---
title: "Mailsmith ‘Send Now’ Menu Key Defense"
date: 2004-02-26
url: https://daringfireball.net/2004/02/send_now_defense
slug: send_now_defense
word_count: 975
---


One of Mailsmith’s most significant charms is that its text editing features are extraordinarily similar to those of BBEdit. They look similar, they feel similar, and they’re similarly scriptable.


It’s for this reason alone that I’ve been using Mailsmith ever since version [1.0 shipped in 1998](http://www.barebones.com/company/press.php?news_id=63). Mailsmith 1.0 was glacially slow at storing messages in mailboxes, and lacking in many features. “1.0” software tends to be that way. But its BBEdit-like text editing capabilities were its saving grace.


But while similar editors, they are not identical. Certain differences are necessarily inherent between a text file editor and an email client. One such difference, which has bitten me dozens of times in the past five years, is the menu key shortcut Cmd-E.


In BBEdit, Cmd-E is bound to Search → Enter Search String. If you select some text in the front window, then invoke Enter Search String, the selected text becomes the text in the Search For field of the Find dialog. Thus, you can use this command to enter a search string, then use commands like Find Again or Replace All, without actually opening the Find dialog itself.


In Mailsmith, Cmd-E is bound to Message → Send Now.


Do you see how this could be a problem? I’m writing in Mailsmith; I select a word; I hit Cmd-E with the intention of entering a search string — but *fuck*, by hitting Cmd-E, I just sent the message before it was finished.


This happens to me rarely — I’d say maybe two or three times a year, tops. But it’s been happening to me two or three times a year for nearly six years. It’s not a catastrophe, but it’s embarrassing enough that I wanted to find a way to stop it from happening again.


BBEdit and Mailsmith both allow you to customize their menu keys, but I don’t want to change either of these shortcuts. Cmd-E has been the standard shortcut for Enter Search String in Mac text editors since before BBEdit existed, and it’s still a de facto standard shortcut. (It’s even supported in new editors like Xcode and SubEthaEdit, although they call the command “Use Selection for Find”; I think “Enter Search String” is a better name, since it makes mnemonic sense with the Cmd-E shortcut.)


There is no standard shortcut for a mail client’s Send command, but Cmd-E is as good a shortcut as any. The obvious shortcut would be Cmd-S, but of course that’s reserved for Save. (Even if your app doesn’t actually save or print anything, you should never reappropriate deeply ingrained shortcuts like Cmd-S or Cmd-P.) Cmd-E is certainly a better shortcut for sending a message than Apple Mail’s contorted Shift-Cmd-D. And, Eudora uses Cmd-E for Send, which makes it as close to an established standard for Mac email clients as you’re going to get.


The problem isn’t the shortcuts themselves — it’s the fact that I have muscle memory for both of them. 99.9 percent of the time when I hit Cmd-E in Mailsmith, I really do want to send the current message. What I want to defend against is that one time in a thousand when I hit Cmd-E in Mailsmith with the intention of invoking Enter Search String.


## The Menu Script Solution


Last month, a solution finally occurred to me: I could attach a menu script to Mailsmith’s Send Now command, and in the script, try to detect if it has been invoked when I really meant to invoke Enter Search String.


To attach a menu script to a Mailsmith menu command, you save the script in the Menu Scripts folder inside your Mailsmith Support Folder. (Same for BBEdit.) The name of the script needs to be in the form *Menu_name•Command_name*; so in this case, the name will be “Message•Send Now”.


The question is, how can I detect when I’ve invoked this command with the intention of entering a search string? Well, to enter a search string, you need to select some text first. But when I’m actually ready to send a message, I almost never have a selection in the message window — just a blinking insertion point.


So, here’s the idea for how the script should work:

- When “Send Now” is invoked, check to see if there is a range of
selected text in the current message window.
  - If not, tell Mailsmith to go ahead and send the message,
as usual.
  - If there *is* a text selection, display a confirmation
dialog to ask if I really want to send the message.


Here’s the script:


```
on menuselect()
  tell application "Mailsmith"
    tell message window 1
      if (selection as text) is not "" then
        try
          display dialog ¬
            "Are you sure you want to send this message?" buttons ¬
            {"Cancel", "Send"} default button 2
        on error
          -- User hit Cancel; tell Mailsmith not to proceed
          -- with sending the message:
          return true
        end try

        -- User hit Send, so tell Mailsmith to send the message:
        return false

      end if
    end tell
  end tell
end menuselect

```


It would be nice if the confirmation dialog offered an “Enter Search String” button in addition to the “Send” and “Cancel” buttons, but Mailsmith’s search string properties are read-only from AppleScript.


Admittedly, this is a bit esoteric. But it has completely solved a rare but highly annoying problem I’ve suffered for over five years. In the two months that I’ve had this script in place, it has saved me from prematurely sending a message once, and it has never gotten in my way when I actually wanted to send a message.


**Update:** [Michael Tsai wrote a version of this script](http://mjtsai.com/blog/2004/02/26/enter_search_string_and_s.html) that *can* enter the search string if there is a text selection — by using Mac OS X’s new-fangled GUI Scripting. Neat trick.



| **Previous:** | [48 Hours](https://daringfireball.net/2004/02/48_hours) |
| **Next:** | [For Real](https://daringfireball.net/2004/03/for_real) |


PreviousNext