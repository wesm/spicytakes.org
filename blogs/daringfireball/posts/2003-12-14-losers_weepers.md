---
title: "Losers, Weepers"
date: 2003-12-14
url: https://daringfireball.net/2003/12/losers_weepers
slug: losers_weepers
word_count: 1754
---


Looks like I was sort-of wrong [Thursday](https://daringfireball.net/2003/12/old_habits) when I claimed Panther’s new custom keyboard shortcut feature didn’t work with the Finder’s New Folder and New Finder Window commands. It does work, but (a) you need to quit and relaunch the Finder for the changes to take effect; and (b) it won’t let you use Cmd-N for a custom shortcut.


The Keyboard & Mouse prefs panel gives you no clue that you need to quit an app before making changes to its shortcuts, but the Help Center info for “Setting custom keyboard shortcuts for applications” does say so. With regard to the Finder, however, that’s a problem: there’s no obvious way to quit it. Logging out and logging back in will do the trick, but that’s a lot of inconvenience just to change a menu shortcut in the Finder. As shown in yesterday’s article, however, you can quit the Finder via AppleScript:


```
tell application "Finder" to quit
delay 2 -- wait 2 seconds for it to quit
tell application "Finder" to launch

```


You can also use Mac OS X’s Force Quit command, which knows the Finder is special and changes its button from “Force Quit” to “Relaunch” when the Finder is selected.


**Update**: If you Option-click on the Finder’s Dock icon, you can choose Relaunch from the pop-up menu. Thanks to Tommy Hulme for the tip.


But forcing you to relaunch applications, which admittedly sucks, is in fact among the *least* of the problems with Panther’s new custom keyboard shortcuts feature. Even worse:

- **You need to type the names of the menu items you want to
change.** Think about how bizarre this is. You can’t even use
copy and paste, because you can’t select text in a menu. Typing
menu item names correctly is harder than you might think, because
you’ve got specify them precisely, including punctuation. Quoting
from the Help Center:

Tip: You must type the command exactly as it appears in the
application menu, including ellipses and any other punctuation. (An
ellipsis is a special character that looks like three periods. To
type an ellipsis, you can use the Character Palette. For more
information, search Mac Help for “Typing special characters.” It may
be difficult to tell whether the command is written in the menu with
a real ellipsis or with three periods, so if one does not work, try
the other.)

An application knows what its own menu items are, so,
quite obviously, you ought to be able to choose menu items from
a list.
Oh, and if you think it’s hard guessing whether “…” is an
ellipsis or three dots, good luck guessing how many spaces
prefix the menu items in Safari’s View menu.
What could be less Mac-like than needing to type the exact name
of something to use it? Nothing else in the entire Mac OS works
like this. (And don’t say the command-line. When the human
interface starts following the lead of the command-line
interface, we might as well pack up our bags and move to
Redmond.)
- **Confusing restrictions on shortcuts allowed.** Although I
can’t find this documented anywhere, Panther’s Keyboard
Shortcuts features doesn’t seem to allow you to set a shortcut
using just the Command key and a letter. You can set shortcuts
like Cmd-Shift-N and Cmd-Option-N, but not just Cmd-N. If you try, it
just beeps. It will even let you set a keyboard shortcut using
*only* the Option key modifier, which is insane, because Option,
by itself, is used to type extended characters. For example,
it let me set the shortcut for the Finder’s Minimize Window
command to Option-8:

Which means when I type a bullet in the Finder, the front window is
sent into the Dock. Nice.
So, you’re *not* allowed to set useful shortcuts like Cmd-N, but you
*are* allowed to set ridiculous shortcuts like Option-N. This
restriction is the reason I thought the Finder’s shortcut for
New Folder couldn’t be changed via the Keyboard & Mouse prefs panel
— it *can* be changed, but not to Cmd-N.
- **No conflict management.** The System Prefs keyboard shortcuts
feature does nothing — nothing — to prevent conflicts. It’ll
happily allow you to set the same shortcut to multiple menu
items. If you use the Keyboard & Mouse panel to set a shortcut
that conflicts with another shortcut you’ve already set in the
panel, it will warn you — but it won’t stop you. But if your
new shortcut conflicts with one of the app’s built-in (i.e. not
customized) shortcuts, you don’t even get a warning.
- **There’s no way to remove default shortcuts.** For example,
three or four times in the last six months, Safari has started
allowing pop-up windows to appear on my machine. Each time this
has happened, I check, and lo, the Allow Pop-Up Windows option
in Safari’s application menu is turned off. The keyboard
shortcut for this command is Cmd-K, which happens also to be my
shortcut in Mailsmith for checking mail. So my best guess is
that every once in a while, I type Cmd-K while I’m in Safari,
thinking that I’m in Mailsmith.
I *never* want to turn off Safari’s pop-up blocking, so I have
no need for a menu shortcut for this. What I’d like to do isn’t
to change the shortcut, but remove it entirely. (Not remove the
command, just the keyboard shortcut.) Panther’s Keyboard
Shortcuts feature won’t let you do that. Best I could do is change
it to Cmd-Shift-Opt-Ctrl-K, which is less likely to be invoked
inadvertently (to say the least).


There are so many ways setting a shortcut through the Keyboard & Mouse prefs panel can fail: you can mistype the menu name; you can inadvertently set a shortcut that conflicts with another menu item; you can forget to relaunch an already-running application (or, more likely, you can not even realize that you need to relaunch the app, since the Keyboard & Mouse prefs panel doesn’t tell you so).


## Craptacular


I’m spoiled by apps like [BBEdit](http://www.barebones.com/products/bbedit/), [Mailsmith](http://www.barebones.com/products/mailsmith/), and [Script Debugger](http://www.latenightsw.com/), which not only allow you to customize menu key shortcuts, but also apply shortcut changes immediately, present a list of all available menu commands for you to choose from, and identify and prevent keystroke conflicts. But “spoiled” isn’t the right word — this is quite obviously the way changing shortcuts *should* work.


A few readers wrote to complain about my script from Thursday, pointing out that on any non-English localized system, you’d need to customize the menu item names in the script. But that’s no worse or different than trying to do so via the approved human interface in the Keyboard & Mouse prefs panel. And since the prefs panel won’t let you set a shortcut to Cmd-N, but the command-line {defaults} tool will, the script is in fact more capable than the prefs panel.


Perhaps you’re willing to accept all of this, on the grounds that Panther’s custom menu keys feature is better than nothing at all. Wrong. A half-assed feature usually *is* worse than none at all, and half-assed might be a generous description in this case.


What Apple has done is implement a new user-customizable architecture for storing and determining menu key shortcuts, but instead of *replacing* the old architecture, the new way is just sitting *on top of* the old one.


The new, user-customizable architecture stores your custom keyboard shortcuts in Mac OS X’s system-wide *defaults* database, which information is stored in those [cruftily](http://mpt.phrasewise.com/stories/storyReader$374)-named files like “com.apple.finder.plist” in your Preferences folder. The defaults system is just a system-provided standard mechanism for software to store preferences data, and thus it’s a fine place to store custom menu key bindings.


The old architecture — which, it’s essential to note, has not been replaced — is for each app to define its menu key shortcuts in its internal resources. For older Carbon apps, they’re defined as resources in the application file’s resource fork. For newer Carbon apps and all Cocoa apps, they’re defined in [nib files](http://developer.apple.com/documentation/DeveloperTools/Conceptual/ToolsOvr_Book/IDE/chapter_3_section_4.html) inside the application package. But for the purposes of user-customization, the implementation details — resource fork data vs. nib files — makes no differences. The point is that the keyboard shortcuts are defined inside the application, and, thus, if you want to modify them, you need to hack the app itself.


Needless to say, modifying an application’s internal resources is not a tenable solution to the problem of providing user-configurable keyboard shortcuts.


The problem is that the only keyboard shortcuts that are stored in the new architecture are the ones you customize. All of an app’s default shortcuts, the ones you haven’t changed, are still only defined the old way, in the app’s internal resources.


This explains just about all of the aforementioned flaws in Panther’s Keyboard Shortcuts feature. You have to type the menu item names because there’s no way for the Keyboard & Mouse prefs panel to ask each app what its menu items are. They’re there, in the nib files, but just because a menu exists in a nib file doesn’t mean it’s being used. There is no way for the prefs panel to ask every app, “Tell me all your menu items and their shortcuts.”


This is the same reason why the Keyboard & Mouse prefs panel offers no conflict detection between your custom shortcuts and an apps’s built-in shortcuts. It not only doesn’t know the app’s built-in shortcuts, it *can’t know*. And so my guess is this is also the reason why the prefs panel refuses to let you set shortcuts using just Command and one letter — those are the shortcuts that are the most likely to collide with existing built-in shortcuts.


As it stands, the prefs panel can’t offer you a list of every app’s menu commands, nor can it detect conflicts. But, obviously, it should do both. If that’s not possible given the current underlying implementation, it’s not an argument for forcing users to tolerate these limitations — it’s an argument that we need a new underlying implementation.


If Apple wants to provide a useful, standard, system-wide human interface for user-customizable keyboard shortcuts — and I think they should — they need to provide a system-wide mechanism for applications to register *all* of their menu key shortcuts. It would mean that this hypothetical new menu key customization feature would only be available for applications which explicitly support it, but there’s simply no other way it can be done well.



| **Previous:** | [Old Habits](https://daringfireball.net/2003/12/old_habits) |
| **Next:** | [Inflammable Means Flammable?](https://daringfireball.net/2003/12/inflammable_means_flammable) |


PreviousNext