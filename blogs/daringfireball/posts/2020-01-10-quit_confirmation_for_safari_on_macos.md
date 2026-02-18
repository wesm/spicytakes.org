---
title: "Quit Confirmation for Safari on MacOS"
date: 2020-01-10
url: https://daringfireball.net/2020/01/quit_confirmation_for_safari_on_macos
slug: quit_confirmation_for_safari_on_macos
word_count: 1072
---


Here’s a quick little AppleScript I wrote recently that I’ve found helpful.


Backstory: When you quit a web browser on MacOS, they just quit. Whatever windows and tabs are open, boom, they just go away. In the old days, quitting a browser *closed* all windows, so when you relaunched your browser, you were sitting there staring at a new empty browser window. This sucked if you needed to restart, and it really sucked if you quit your browser accidentally. How do you quit accidentally? Typically, by pressing ⌘Q by mistake when you meant to press Q’s neighbor W to close the current tab.


A few years ago all modern browsers added a feature that restores your previously-open windows and tabs automatically upon relaunching. This restoration of previously open windows and tabs is so useful that in the current version of Safari, there isn’t even an option *not* to do it. The only choices in Safari’s General preferences tab for “Safari opens with” are “All windows from last session” and “All non-private windows from last session”. Quitting Safari and closing tabs are completely discrete, and it’s clear to me that’s the correct design.


[**Update:** The above is not the whole story. *I* only see two options because in System Preferences: General, I have the [“Close windows when quitting an app” checkbox](https://daringfireball.net/misc/2020/01/system-prefs-general-close-windows.png) turned off. If you have that checkbox turned on, you’ll see four options in Safari for “Safari opens with”: the two mentioned above, along with “A new window” and “A new private window”. If you have the system-wide “Close windows when quitting an app” turned off and choose “A new window” or “A new private window” in Safari, you will in fact start fresh with a single empty window upon relaunching Safari. (But even then, you can go to History → Reopen All Windows from Last Session to re-open all of your previous windows and tabs.)]


But, even with this automatic session restoration, it can still be disruptive if you quit your browser accidentally. When windows come back, sometimes you lose your place on a page, or you get logged out, or a dozen other potential hiccups.


Chrome addresses this by blocking ⌘Q by default. If you press and release ⌘Q in Chrome, with default settings, instead of quitting, [Chrome displays a message in a temporary notification banner](https://daringfireball.net/misc/2020/01/chrome-hold-cmd-q.png): “Hold ⌘Q to Quit”. With this setting enabled — and it’s on by default — you have to *hold* ⌘Q to quit Chrome. Other Chromium-derived browsers, like the excellent [Brave](https://brave.com/) (which I heartily recommend as an alternative to Chrome), do the same thing. This does solve the problem of having your entire browser quit when you just meant to close the current tab with ⌘W, but it’s a decidedly unidiomatic solution. Press-and-hold to invoke a menu key shortcut just isn’t a thing on the Mac. It’s weird.


If you want to disable this feature in Chrome, don’t bother looking in Chrome’s labyrinthian Preferences window. You control this setting with the [“Warn Before Quitting (⌘Q)” menu item above the “Quit Chrome” command in the Chrome menu](https://daringfireball.net/misc/2020/01/chrome-warn-before-quitting.png).


That’s not even a good description for the setting. You don’t get *warned* before quitting when it’s enabled — you’re instead required to press-and-hold the ⌘Q shortcut.


But a confirmation warning is exactly what you *should* get. This is how the Mac has protected against quitting when you might lose data or state since the dawn of time — like when you try to close a document window with unsaved changes.


I don’t accidentally quit Safari often, but it does happen. And it’s mildly annoying every time. The last time it happened, I resolved to fix it myself. That’s where my AppleScript comes in:


```
use AppleScript version "2.4" -- Yosemite (10.10) or later
use scripting additions

tell application "Safari"
    set _window_count to count windows
    set _tab_count to 0

    repeat with _w in every window
        set _tab_count to _tab_count + (count tabs of _w)
    end repeat

    -- Make a string like "1 window containing 3 tabs."
    if _window_count is 1 then
        set _msg to _window_count & " window containing " as string
    else
        set _msg to _window_count & " windows containing " as string
    end if
    if _tab_count is 1 then
        set _msg to _msg & _tab_count & " tab." as string
    else
        set _msg to _msg & _tab_count & " tabs." as string
    end if

    display alert ¬
        "Are you sure you want to quit Safari?" message _msg ¬
        buttons {"Cancel", "Quit"} ¬
        giving up after 60
    if button returned of result is "Quit" then quit
end tell

```


Run this script, and it shows an alert like this:


Last step: how do we get this script to run when we press ⌘Q in Safari? I use [FastScripts](https://red-sweater.com/fastscripts/), Red Sweater Software’s excellent alternative to Apple’s own system-wide scripts menu. Among numerous other features, FastScripts allows you to assign custom keyboard shortcuts to scripts — and FastScripts will “see” those shortcuts before the application you’re using does.


So I’ve saved this script as “Quit With Confirmation” and placed it in the “Safari” folder in the “Applications” folder inside my “Scripts” folder. [See FastScripts’s excellent documentation](https://help.red-sweater.com/fastscripts/faq/) for more information on where to place application-specific scripts. Then in FastScript’s preferences, I assigned it ⌘Q. When I press ⌘Q in Safari, the script runs instead of Safari’s menu command.


Now I can wildly stab at ⌘W to close tabs without a care in the world.1 Enjoy.


---

1. If the only thing you want to do is disable ⌘Q in Safari (or any other shortcut, in any other app, for that matter), the easiest thing to do is use the Keyboards panel in System Prefs (then go to Shortcuts: App Shortcuts) to either set Safari’s shortcut for File → Quit to nothing at all, or to something you won’t hit accidentally, like, say, Control-Option-Shift-Command-Q. Almost no work at all, no third-party software required. This ability to fully customize every menu key shortcut in every single app on the system is one of the best power-user tips I know of. But that’s not what I want. I want to defend against hitting ⌘Q accidentally, but I also want to be able to use ⌘Q on purpose when I really do want to quit Safari. That means a confirmation alert. ↩︎



| **Previous:** | [Front and Center](https://daringfireball.net/2020/01/front_and_center) |
| **Next:** | [Regarding Reuters’s Report That Apple Dropped Plan for Encrypting iCloud Backups](https://daringfireball.net/2020/01/reuters_report_on_apple_dropping_plan_for_encrypted_icloud_backups) |


PreviousNext