---
title: "Writing AppleScripts That Dynamically Target Either Safari or WebKit"
date: 2009-01-30
url: https://daringfireball.net/2009/01/applescripts_targetting_safari_or_webkit
slug: applescripts_targetting_safari_or_webkit
word_count: 1265
---


First, a bit of background information. “WebKit”, in addition to being the name of the HTML/CSS/JavaScript web rendering engine at the heart of Safari (and, now, numerous other browsers like [Chrome](http://www.google.com/chrome)), is also the name of an application for the Mac that is, more or less, just like Safari but uses the latest nightly build of the WebKit rendering framework instead of the standard system-wide version of the WebKit framework that ships as part of Mac OS X. You can download the latest WebKit nightly build [here](http://nightly.webkit.org/).


The WebKit app is so much like Safari that its application menu — the one right next to the Apple menu — even says “Safari”. It reads and writes the same preferences and bookmarks as Safari. It’s more like a phantom copy of Safari than a separate application.1 But WebKit *does* run as its own distinct process. You can, for example, run Safari and WebKit at the same time. WebKit has its own app icon, too. And, with regard to AppleScript, WebKit needs to be addressed specifically.


This script will launch or activate Safari:


```
tell application "Safari" to activate

```


This script will launch or activate WebKit:


```
tell application "WebKit" to activate

```


I have a handful of AppleScripts I’ve written that do things with Safari. They’re saved in a folder at *~/Library/Scripts/Applications/Safari/*, and when Safari is the current application, they appear at the top of my system-wide Script menu. (I use [FastScripts](http://www.red-sweater.com/fastscripts/) rather than the Script menu from Apple because FastScripts allows you to assign keyboard shortcuts to scripts.)


What I’d like, when I’m running WebKit, is to have access to the exact same set of scripts I created for use within Safari. The obvious solution is tedious:

1. Make a copy of my Safari scripts folder and name it “WebKit”.
2. Change the `tell application` target in each of those scripts from “Safari” to “WebKit”.


It’s worth noting that because WebKit is just a phantom version of Safari, it shares the exact same scripting dictionary. A script that works with Safari should work exactly the same with WebKit — except that you need to make WebKit the target of the `tell` block. The problem with this obvious solution is that every time I change a script or create a new one, I’d have to maintain two separate copies.


A better solution is to use what I’ll call *dynamic tell targets* — instead of making the `tell` target a hard-coded application name, make it a variable that is determined at runtime. When I first set out to do this, I couldn’t find examples of it being done before. Perhaps that’s because it’s something you so rarely need to do in AppleScript. When you say `tell application "Foo"` in AppleScript, you’re telling the script that the current block is using terms from Foo’s scripting dictionary. And a big part of the entire point (and pain) of AppleScript is that each app provides its own unique dictionary.


Safari and WebKit are an exception. (The technique I outline below might, hypothetically, also be of use if you found yourself needing to write scripts that work against multiple versions of the same app, provided both versions use the same scripting terms.)


## The Solution


There are two main contexts from which you’d want to run a script that dynamically targets either Safari or WebKit:

1. A script that targets the current “default” web browser, assuming the default browser is either Safari or WebKit.
2. A script that targets whichever of the two is currently the active application. This is most useful for scripts that you intend to run from the system-wide Script menu.


The framework I’ve created supports both of these. Even for scripts I only intend to use from the Script menu (therefore using technique #2, dynamically targeting the current active application), it’s useful to include technique #1 as a fallback so that the script works while editing and debugging it — when you run a script from within Script Editor, Script Editor is the frontmost application.


Here’s the basic framework:


```
set _browser to GetCurrentApp()
if _browser is not in {"Safari", "WebKit"} then
    set _browser to GetDefaultWebBrowser()
end if
using terms from application "Safari"
    tell application _browser
        -- do stuff with Safari or WebKit here
    end tell
end using terms from

on GetCurrentApp()
  tell application "System Events" to ¬
    get short name of first process whose frontmost is true
end GetCurrentApp

on GetDefaultWebBrowser()
    -- First line of _scpt is a workaround for Snow Leopard issues
    -- with 32-bit Mac:: Carbon modules
    set _scpt to "export VERSIONER_PERL_PREFER_32_BIT=yes; " & ¬
        "perl -MMac::InternetConfig -le " & ¬
        "'print +(GetICHelper \"http\")[1]'"
    return do shell script _scpt
end GetDefaultWebBrowser

```


There are two utility handlers, `GetCurrentApp()` and `GetDefaultWebBrowser()`, both of which return the name of an app as a string. My thanks to Christopher Masto [for the bit of Perl code](http://twitter.com/masto/statuses/946428410) that gets the user’s current default web browser.2 The script first gets the name of the frontmost app. If it’s “Safari” or “WebKit”, then it assumes that’s the app you’re targeting. If not, it gets the name of the user’s default web browser and uses that. **There is a big assumption here:** if neither the frontmost app *nor* the default web browser is Safari or WebKit, the script will target whatever the current default web browser actually is, and it almost certainly won’t work. If you use something other than Safari or WebKit as your default browser, you’ll want to change this.


So at this point the variable `_browser` is a string set to either “Safari” or “WebKit”. And you can use this variable as the target of a `tell application` block. But, if you use any Safari/WebKit-specific scripting terms inside the `tell` block — and you almost certainly will, since that’s the entire point of writing a script that targets these apps — the script will not compile without the outer `using terms from` block.


There’s a two-step processing to running AppleScript source code: first it compiles, then it can run. But AppleScript can’t compile terms from a specific application dictionary without knowing exactly which application that is, and the whole point of this exercise is that we don’t want to determine the target of the `tell` block until runtime. The `using terms from` block lets us work around that. We still have to hard-code the name of a specific application, but by putting it in the `using terms from` block rather than the `tell` block, it’s just information for AppleScript to use at *compile* time. (We could just as easily use WebKit as the target of the `using terms from` block, but I figure it’s better to use Safari since every Mac ships with Safari installed.)


After re-writing all my Safari-targeting AppleScripts to use this framework, I simply made an alias to my *~/Library/Scripts/Applications/Safari/* folder, and named the alias “WebKit”. I now have one set of scripts that work in (and appear at the top of my Script menu in) both apps.


---

1. The WebKit.app bundle is really just two things: updated WebKit frameworks, and an executable binary that launches an instance of the regular Safari binary with a directive to use the new WebKit frameworks rather than the standard system frameworks. So as applications, Safari and WebKit are truly identical — the only difference is the rendering engine. ↩︎
2. I updated the Perl bit slightly in September 2009 for compatibility with Mac OS X 10.6 (Snow Leopard). ↩︎



| **Previous:** | [The Truth](https://daringfireball.net/2009/01/the_truth) |
| **Next:** | [‘Do Shell Script’ and Premature Optimization](https://daringfireball.net/2009/02/do_shell_script_premature_optimization) |


PreviousNext