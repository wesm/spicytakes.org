---
title: "Opening New Tabs Next to the Current Tab in Safari"
date: 2018-12-11
url: https://daringfireball.net/2018/12/safari_new_tab_next_to_current_tab
slug: safari_new_tab_next_to_current_tab
word_count: 673
---


The way Safari tabs work on the Mac:

- If you ⌘-click a link or use the contextual menu to open a link in a new tab, that new tab will be created next to your current tab.
- If you make a new tab with File → New Tab (⌘T), the new tab will be created at the rightmost end of the tabs in the current window.


This is the way Safari tabs have worked as long as I can remember, and it matches the way tabs work on other browsers on the Mac.


It’s fine if you don’t have a lot of tabs. But I always do, and the behavioral mismatch has long bothered me. If I have, say, 10 tabs open in a window and I’m currently using, say, tab 2, when I type ⌘T to open a new tab it feels like the rightmost end of the row of tabs is “way over there”, but what I want is the new tab to open “right next to where I am” — like what happens when I ⌘-click a link.


A few months ago [I asked on Twitter](https://twitter.com/gruber/status/1050157023650811904) if there was a secret preference in Safari that would change this to what I want — which is for new tabs to always open right next to the current tab. There is no such preference. I set about trying to figure out if this could be done using AppleScript, but I couldn’t figure it out.


[Jeff Johnson](http://lapcatsoftware.com/main/Resume.html) figured it out, though, and [was kind enough to share the solution and explain the rather ungainly syntax required](https://twitter.com/lapcatsoftware/status/1050191702156345344).


Here’s my slightly modified version of Johnson’s solution:


```
tell application "Safari"
    tell front window
        set _old_tab to current tab
        set _new_tab to make new tab at after _old_tab
        set current tab to _new_tab
    end tell
end tell

```


What tripped me up is that in Safari’s AppleScript object model, `tabs` have an `index` property. The leftmost tab in a window has an `index` of 1; the next tab 2, etc. But `index` is a read-only value — you can’t change the `index` to move a tab, and you can’t create a new tab with a specific `index` value.


As Johnson notes:


> Here’s the somewhat unintuitive AppleScript. It’s “at [location
> specifier]”, where “after [item]” is a location specifier.


Which gives us “`make new tab at after _old_tab`”. [AppleScript’s English-Likeness Monster](https://daringfireball.net/2005/09/englishlikeness_monster) rears its head.


Ungainly syntax aside,1 this simple script works exactly how I want it to. I use Red Sweater Software’s excellent [FastScripts](https://red-sweater.com/fastscripts/) to provide a system-wide scripts menu, and assigned this script the shortcut ⌘T in Safari. FastScripts “sees” the ⌘T shortcut before Safari does, so when I invoke it, the script runs instead of the File → New Tab menu command. One could set it up using [Keyboard Maestro](https://www.keyboardmaestro.com/) just as easily. If you don’t use either FastScripts or Keyboard Maestro, I don’t know what to tell you other than that you’re missing out.


I’ve been using this for two months, and at this point it feels indispensable. I was using a different Mac the other day where I hadn’t yet set this up, and it felt like Safari was broken. Which, yes, also means that ⌘T in Safari on iPad now feels broken.


---

1. Given my complaints about AppleScript’s goofy syntax here, I thought this might be a good example to try to recreate in [JavaScript for Automation](https://developer.apple.com/library/archive/releasenotes/InterapplicationCommunication/RN-JavaScriptForAutomation/Articles/OSX10-10.html#//apple_ref/doc/uid/TP40014508-CH109-SW1) (JXA). Apple added JXA as an alternative to AppleScript back in MacOS 10.10 (which, yes, was called OS X 10.10 at the time). Maybe I’m missing something, but I’ll be damned if I could get it to work. Maybe the problem is me being a JavaScript dummy, but I sort of think this might not be possible in JXA because [JXA might be an unsupported hot mess](https://stackoverflow.com/questions/27746418/send-email-with-attachment-using-javascript-for-automation). If someone can prove me wrong, let me know. ↩︎



| **Previous:** | [Electron and the Decline of Native Apps](https://daringfireball.net/2018/12/electron_and_the_decline_of_native_apps) |
| **Next:** | [Apple’s Terrible No Good Very Bad Earnings Warning](https://daringfireball.net/2019/01/apples_terrible_no_good_very_bad_earnings_warning) |


PreviousNext