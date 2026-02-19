---
title: "‘Grab HTML’ Script for BBEdit"
date: 2002-08-22
url: https://daringfireball.net/2002/08/grab_html_script_for_bbedit
slug: grab_html_script_for_bbedit
word_count: 634
---


**Update:** I’ve written an [updated version of this article and the accompanying script](https://daringfireball.net/2003/07/grab_html_script_for_bbedit_redux.html).


Way back in 1996, Dan Crevier wrote a nifty plug-in for BBEdit called [HTML Grabber](http://www.barebones.com/support/bbedit/bbedit-plugins.html#plugin_b20). It’s a simple but useful little thing: choose its menu item and it pops up a dialog box into which you enter a URL; click a button and the plug-in fetches the contents of the URL via HTTP, then presents the results in a new BBEdit text window.


Sort of like the View Source command in a web browser, except much more convenient if you’re already working in BBEdit. Even better, HTML Grabber also lets you see the HTTP headers, which can be very useful when debugging CGI’s.


The plug-in still works in BBEdit 6.5, but only in Mac OS 9. However, a Mac OS X version is a cinch to write in AppleScript, passing the HTTP work off to the command-line `curl` utility. (Thus, the script won’t work in Mac OS 9.)


Here’s the script. Paste it into your script editor, and save it as a compiled AppleScript in the “Scripts” folder in your “BBEdit Support” folder.


```
property my_url : ""

tell application "BBEdit"
    display dialog ¬
        "URL:" default answer my_url ¬
        buttons {"Cancel", "Grab"} default button 2
    set my_url to the text returned of the result
    -- "-i" tells curl to include the headers
    set my_text to do shell script ("curl -i " & my_url)
    make new text window with properties {contents:my_text}
end tell

```


This sort of AppleScript/shell hybrid shows Mac OS X at its best. The `do shell script` command puts the whole Unix command-line toolset at your fingertips — while a command line by itself does not make for a good user interface, it can be an amazingly easy-to-use *programming* interface.


It’s also worth noting that `curl` is flexible enough to accept URLs without a protocol specifier; you can just type “daringfireball.net” instead of “http://daringfireball.net”.


## How It Works


`my_url` is a string that holds the URL we’re fetching. Because it’s a property, the last URL you enter will be remembered the next time you run the script. It defaults to the empty string.


`display dialog` pops up a dialog box with a text input field. The contents of the text input field are set to the value of `my_url`.
After the dialog is dismissed, AppleScript’s magic `result` variable contains a record of values, including the name of the button that was clicked and the text in the input field. We don’t need to check which button was clicked, however, because the `display dialog` command is smart enough to know what a “Cancel” button means — if you run the script and choose “Cancel”, the script terminates as soon as the dialog is closed.


After updating the contents of `my_url`, we use the `do shell script` command to invoke the command-line utility `curl`. If you don’t want to see the HTTP headers in the script’s output, remove the “-i” switch. The `do shell script` command returns the shell’s output as a string.


Finally, we create a new BBEdit text window with the contents of the `curl` output. What’s cool about setting the contents of the window as a property is that if you’re using BBEdit 6.5, BBEdit will guess the source language of the text, and will apply HTML syntax coloring (assuming the URL you fetched was for an HTML document), even if HTML isn’t your default language for new windows.


If instead we had written something like this:


```
    make new text window
    set contents of text window 1 to my_text

```


then BBEdit wouldn’t guess the language automatically. (It would if you saved the new window, but typically the results of this script aren’t going to be saved, so you’d have to set the language to HTML manually.)
