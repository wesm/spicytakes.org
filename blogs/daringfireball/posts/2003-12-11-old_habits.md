---
title: "Old Habits"
date: 2003-12-11
url: https://daringfireball.net/2003/12/old_habits
slug: old_habits
word_count: 942
---


I have two habits from the old Mac OS that I simply cannot seem to shake.


First, when I go to quit an application while using the mouse, I tend to open the File menu instead of the Application menu. Logically, I agree with Apple that the Quit command belongs in the Application menu. But my instincts, after so many years using the old Mac OS, where the Quit command was always at the bottom of the File menu, tell me otherwise. It’s only a minor inconvenience — especially since I usually quit apps via the Cmd-Q keyboard shortcut — so I don’t mind much.


Second, I cannot convince my fingers not to use Cmd-N as the Finder shortcut for making a new folder. Over and over, time after time, I end up with a new Finder window instead of the new folder I wanted.


This one I do mind. I think Apple was wrong to change the shortcut for this command in the OS X Finder. If they were starting from scratch, perhaps one could make an argument that Cmd-N ought to be the shortcut for New Finder Window. *But they weren’t starting from scratch.* Millions of Mac users had been using Cmd-N to create new folders for years. This shouldn’t even have been on the table.


This is why it’s important for developers to carefully consider keyboard shortcuts from the outset. Once users get accustomed to existing shortcuts, they get irritable if the shortcuts subsequently change. If the default shortcuts do change in a new version of the app, there really ought to be a way for users to reconfigure them. The whole point of keyboard shortcuts is that you commit them to memory.


Now, I think the most important thing to keep in mind when switching to Mac OS X is this: *When in Rome, do as the Romans.* I.e., don’t try to use Mac OS X just like you did Mac OS 9. You can fight it if you want, using third-party software to mimic Mac OS 9 behavior in all sorts of places, but you’ll be happier if you open your mind and learn the Mac OS X way.


It is beside the point whether you prefer the Mac OS 9 way. Mac OS X is offering you a round hole. Third party hacks will let you put your square peg inside, but it’s not going to work as smoothly as using the round peg designed for the hole.
My dad has a saying: *People in hell want ice water, but they’re not going to get it.* Better to deal with Mac OS X as it is than to pretend it’s something else. In that spirit, I’ve weened myself away from Make-OS-X-Act-Like-OS-9 system hacks. Unsanity’s [WindowShade X](http://www.unsanity.com/haxies/wsx/) was the last to go — I used it up until Panther, but the addition of Exposé made it easy to abandon.


But, then, what to do about my Finder Cmd-N habit? What I want is to swap the shortcuts for New Folder and New Finder Window. Can I justify this desire with my *When in Rome…* motto? Yes, I think so. This isn’t a case of stubbornly trying to stick with the OS 9 way of doing things; it’s just a deeply ingrained keyboard shortcut.


So, how to swap them? I tried using Panther’s new “set your own keyboard shortcuts” feature in the Keyboard & Mouse System Prefs panel, but, alas, it doesn’t seem to let you change the Finder’s shortcut for New Finder Window. Based on the tips contained in [this article at Mac OS X Hints](http://www.macosxhints.com/article.php?story=20031125022312849), however, I’ve put together an AppleScript that does the trick:


```
tell application "Finder" to quit
do shell script ¬
    "defaults write com.apple.finder NSUserKeyEquivalents " & ¬
    "-dict-add 'New Finder Window' '@$N' 'New Folder' '@N';"
delay 1 -- pause 1 second
tell application "Finder" to launch

```


It’s a hack, but I consider it a *clean* hack, because it doesn’t modify the Finder itself or any of its resources. Instead, it simply adds two keyboard shortcut entries to the Finder’s “com.apple.finder.plist” preference file. (Thus, if you want to play it safe, you can simply make a backup of that file before running the script.)


The script itself is fairly simple. First, it tells the Finder to quit. Then it uses the command-line `defaults` tool to add the new settings to the Finder’s preferences. Then it tells the Finder to relaunch. It pauses one second before relaunching the Finder; without the delay, the launch Apple event might be sent to the Finder before it has had time to quit.


## Other Habits


I’ve been running the Finder with these swapped shortcuts for a few days. What’s funny is that I’m now slightly annoyed by an unexpected problem: I keep hitting Cmd-N to make a new Finder window. I.e., what’s happened to me is that I’ve developed muscle memory for two separate commands for the same shortcut in the Finder. But even after just a few days, I’m starting to get accustomed to it — Cmd-N for making a new folder is wired into a much deeper part of my mind than it is for making a new window.


Your mileage, of course, may vary. I’m curious what other old habits continue to plague long-time Mac users who’ve switched to Mac OS X. If you have any, send them to me at [oldhabits@daringfireball.net](mailto:oldhabits@daringfireball.net) and I’ll compile a list. (If you don’t want your name published, be sure to say so.) I’ll even consider comments from Windows switchers.



| **Previous:** | [PHP Syntax Checking in BBEdit](https://daringfireball.net/2003/12/php_syntax_checking_in_bbedit) |
| **Next:** | [Losers, Weepers](https://daringfireball.net/2003/12/losers_weepers) |


PreviousNext