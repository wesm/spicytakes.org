---
title: "Using FastScripts as a Lightweight Alternative to Growl"
date: 2008-02-08
url: https://daringfireball.net/2008/02/fastscripts_display_message
slug: fastscripts_display_message
word_count: 408
---


[Growl](http://www.growl.info/about.php) is an interesting idea — a system-wide notification system with self-dismissing messages. Unlike a dialog box alert that (a) pops up in the center of your display and (b) you must dismiss manually, a Growl message can appear off to the side and will disappear on its own after a few seconds, no user action required.1


When I upgraded to Leopard full-time a few months ago, I started with a clean installation and only added back third-party UI utilities one-by-one, when I actually missed them. It ended up I didn’t miss Growl much, and didn’t get around to re-installing it until last week.


The one thing I really missed about Growl was using it to display status messages from certain of my own scripts — scripts from which I want to see the results, but which I don’t want to interrupt me with an alert dialog. Using Growl just for the occasional message from a script seemed like overkill; on my machine Growl typically consumes at least 30 MB of real memory.


I’ve found a good alternative: the “`display message`” command from [FastScripts](http://www.red-sweater.com/fastscripts/), the $15 script menu utility by Daniel Jalkut at Red Sweater Software.2 FastScripts’s message window is a simple, dark, slightly tranclucent HUD-style floating window that accepts a single string as a parameter. You also get to specify where it should appear (e.g. “top left”, “center”, “bottom right”) and how many seconds it should remain on screen until dismissing itself. You can click on the message window to dismiss it manually.


Here’s an example:


```
tell application "FastScripts"
    display message "I drink your milkshake!" at screen position ¬
        top left dismissing after delay 10
end tell

```


Which produces:


It’d be nice if, like the Standard Additions “`display alert`” command, you could specify an optional second string parameter that would be displayed in a smaller font. For example:


```
set my_title to "This is the title"
set my_message to "This is the message"
display alert my_title message my_message

```


Produces this dialog:


It’d also be nice if you could specify a different icon (or none at all). But it’s a nice lightweight alternative to Growl as-is.


---

1. Growl messages *can* be persistent, remaining on screen until dismissed manually with a click, but most aren’t. ↩︎
2. This feature is only part of FastScripts, not the freeware FastScripts Lite. ↩︎



| **Previous:** | [Devil’s Advocate](https://daringfireball.net/2008/02/devils_advocate) |
| **Next:** | [News Flash: No Flash](https://daringfireball.net/2008/02/news_flash_no_flash) |


PreviousNext