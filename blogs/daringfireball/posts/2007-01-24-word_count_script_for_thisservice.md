---
title: "‘Word Count’ Script for ThisService"
date: 2007-01-24
url: https://daringfireball.net/2007/01/word_count_script_for_thisservice
slug: word_count_script_for_thisservice
word_count: 521
---


Back in October my friend Jesper wrote a nifty little utility called [ThisService](http://wafflesoftware.net/thisservice/). You give ThisService a script — either AppleScript or any Unix scripting language such as Perl, Python, or Ruby — and it generates a system-wide service based on that script, right there in the Services menu, available in any app. No Xcode or Cocoa required. You just write the script.


When I [linked to it](http://daringfireball.net/linked/2006/october#mon-30-thisservice), I promised a couple of example scripts. I’m a few months late, but here we go.


This one is about as simple as it gets, but I use it quite often. It takes as input the currently selected text in the frontmost app, and then displays an alert showing the number of words in the selection.


Here’s the AppleScript source code:


```
on process(_str)
    tell application "System Events"
        set _appname to name of first process whose frontmost is true
    end tell
    tell application _appname
        display alert "Word count: " & (count words of _str)
    end tell
end process

```


That’s the entire script.


The `process` handler is ThisService’s idiom for passing in the selected text, which I assigned to a variable named `_str`. We ask System Events for the name of the frontmost application, and then do a `display alert` within that app’s context. You might be tempted to take a shortcut and just do this:


```
on process(_str)
    display alert "Word count: " & (count words of _str)
end process

```


But that won’t work, because the `display alert` command needs to appear in the context of some visible application, otherwise it runs in the context of the service itself, and you’ll never see it.


AppleScript’s `count words` command isn’t particularly clever. It won’t work as you’d like with HTML input (the tags count as words), and it considers most punctuation characters as word delimiters, which means a URL like “http://www.example.com/foo/” counts as five words. But it’s a good approximation, and the service works just about anywhere, including web browser form fields in Camino and Safari.


To create your own Word Count service using this script, copy the source to a new window in Script Editor, and save the script (using the “script” file format). It doesn’t really matter what you name it or where you save it; your desktop is fine. Open [ThisService](http://wafflesoftware.net/thisservice/) and drag the script into the ThisService window. Give your service a name (I used “Word Count…”), make sure “Acts on input” is selected, and, if you’d like, assign a keyboard shortcut.


Keyboard shortcuts for services are limited to combinations of Command and Shift; this limitation is from Mac OS X, not ThisService. I chose Command-Shift-K (*K* for *kount*; Command-Shift-C is the standard shortcut for the Show Colors command). Feel free to leave the shortcut field empty.


Click “Create Service”, and ThisService will create your service and install it in your *~/Library/Services/* folder. You can throw your script file away now, if you’d like — ThisService creates a copy of the script in the service’s bundle.



| **Previous:** | [OS X](https://daringfireball.net/2007/01/os_x) |
| **Next:** | [Sometimes I Wonder Whether Rob Enderle Is Just Pulling Our Legs](https://daringfireball.net/2007/01/enderle_leg_pulling) |


PreviousNext