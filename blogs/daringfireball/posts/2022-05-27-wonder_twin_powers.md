---
title: "Wonder Twin Powers"
date: 2022-05-27
url: https://daringfireball.net/2022/05/wonder_twin_powers
slug: wonder_twin_powers
word_count: 472
---


Nothing like a good AppleScript mystery to get the weekend off to a celebratory start. If you have two or more windows open in an application — let’s say TextEdit, just for the sake of example — and run this AppleScript:


```
tell application "TextEdit" to activate

```


That’s it. That’s the whole script. What I expect to happen, and what I believe should happen, is that TextEdit becomes the active application and all of its windows come forward. That’s what happens when you click on an app’s Dock icon, or switch to it using Command-Tab — all of the app’s open windows come forward.


On MacOS 12 Monterey (and apparently MacOS 11 Big Sur), what happens instead is that TextEdit becomes the active application but only its frontmost window comes forward.


On MacOS 10.15 Catalina, and all previous versions of MacOS back to Mac OS X 10.0, all of the open windows in an app come forward when you tell that app to activate in AppleScript, or with the equivalent in [JavaScript for Automation](https://developer.apple.com/library/archive/documentation/LanguagesUtilities/Conceptual/MacAutomationScriptingGuide/index.html#//apple_ref/doc/uid/TP40016239):


```
Application('TextEdit').activate();

```


Again, this has nothing to do with TextEdit specifically — it’s true for any scriptable Mac app. This seems like it must be a bug, but it’s now been around for two major releases of MacOS, so *maybe* it’s a bizarre change in intended behavior? If anyone knows what’s going on here, let me know.1 [I asked on Twitter earlier today](https://twitter.com/gruber/status/1530273273816162304) and the best answer was [a *Fletch* reference from Andrew Laurence](https://twitter.com/atlauren/status/1530290474610614272). Helpful, no. Funny, always.


The irony here is that I stumbled upon this apparent bug while *trying* to activate an app (Safari) while bringing only one specific open window forward, like this:


```
tell application "Safari" to tell window 1 to activate

```


I thought it was working, because Safari activated and only window 1 was brought forward. But when I changed the AppleScript call to:


```
tell application "Safari" to tell window 2 to activate

```


it was still Safari’s frontmost window, and only that window, that came forward. It turns out you can put any integer you want after `window`, even if it doesn’t refer to a valid index number for a window, and it will compile and run:


```
tell application "Safari" to tell window 1138 to activate

```


and the front window of that app will come forward. Effectively, it’s just telling the app to activate, even inside a tell block for a window, even if the window doesn’t exist. All ball bearings nowadays, indeed.


---

1. Yes, of course I filed a radar, or a “feedback”, or whatever we’re calling them nowadays: FB10029990. ↩︎



| **Previous:** | [The Grave Insult of Being Sent the Proper Tools to Perform a Complicated Task](https://daringfireball.net/2022/05/grave_insult) |
| **Next:** | [Basic Apple Guy’s Prescient Reimagining of System Preferences on MacOS](https://daringfireball.net/2022/06/basic_app_guy_mac_settings) |


PreviousNext