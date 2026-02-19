---
title: "‘Grab HTML’ Script for BBEdit, Redux"
date: 2003-07-21
url: https://daringfireball.net/2003/07/grab_html_script_for_bbedit_redux
slug: grab_html_script_for_bbedit_redux
word_count: 853
---


At least in terms of incoming traffic from Google, one of the most popular articles at Daring Fireball is “[‘Grab HTML’ Script for BBEdit](https://daringfireball.net/2002/08/grab_html_script_for_bbedit.html)”, which I wrote last August. I use this script all the time, and realized recently that I’ve added a bunch of small improvements to the script since writing the original article.


So, here’s an updated version.


## History


Way back in 1996, Dan Crevier wrote a nifty freeware plug-in for BBEdit called [HTML Grabber](http://www.barebones.com/support/bbedit/plugin_library.shtml#plugin_b20). It’s a simple but useful little thing: choose its menu item and it pops up a dialog box into which you enter a URL; click a button and the plug-in fetches the contents of the URL via HTTP, then presents the results in a new BBEdit text window.


Sort of like the View Source command in a web browser, except much more convenient if you’re already working in BBEdit. Even better, HTML Grabber also gives you the option of seeing the HTTP headers, which can be very useful when debugging CGIs.


Mr. Crevier’s plug-in still works in BBEdit 7.0, but only in Mac OS 9. However, a Mac OS X version is a cinch to write in AppleScript, passing the HTTP work off to the command-line `curl` utility. (Thus, the script won’t work in Mac OS 9.)


Here’s the script. Paste it into your script editor, and save it as a compiled AppleScript in the “Scripts” folder in your “BBEdit Support” folder.


```

property my_url : ""

tell application "BBEdit"
    set my_result to display dialog ¬
        "URL:" default answer my_url ¬
        buttons {"Cancel", "With Headers", "Grab Source"} default button 3
    set my_url to the text returned of my_result
    
    if button returned of my_result is "With Headers" then
        set my_text to do shell script ("curl -i " & my_url)
    else
        set my_text to do shell script ("curl " & my_url)
    end if
    
    make new text window with properties {contents:my_text, name:my_url}
    select insertion point before character 1 of text window 1
end tell

```


And here’s the result:


(Note to careful readers of the [HIG](http://developer.apple.com/documentation/UserExperience/Conceptual/AquaHIGuidelines/index.html): I’m aware that “With Headers” is an awkward name for a button because it isn’t a verb; but the `display dialog` command insists on making all three buttons the same width, so if we make the middle button longer by adding a verb, the other two buttons end up looking ridiculous.)


This sort of AppleScript/shell hybrid shows Mac OS X at its best. The `do shell script` command puts the whole Unix command-line toolset at your fingertips — while a command line by itself does not make for a good user interface, it can be an amazingly easy-to-use *programming* interface.


It’s also worth noting that `curl` is forgiving enough to accept URLs without a protocol specifier; you can just type “daringfireball.net” instead of “http://daringfireball.net”.


## How It Works


`my_url` is a string that holds the URL we’re fetching. Because it’s a property, the last URL you enter will be remembered the next time you run the script. It defaults to the empty string.


`display dialog` pops up a dialog box with a text input field. The content of the text input field is initialized with the value of `my_url`. After the dialog is dismissed, the `my_result` variable contains a record of values, including the name of the button that was clicked and the text in the input field. We don’t need to check if the Cancel button was clicked, however, because the `display dialog` command is smart enough to know what a Cancel button means — if you run the script and choose Cancel, the script terminates as soon as the dialog is closed.


After updating the contents of `my_url`, we use the `do shell script` command to invoke the command-line utility `curl`. If the With Headers button was clicked, we include the `-i` option to include the HTTP headers in the result; otherwise, we simply call `curl` with no options. The `do shell script` command returns the command output as a string.


Finally, we create a new BBEdit text window with the contents of the `curl` output. What’s cool about setting the contents of the window as a property is that if you’re using BBEdit 6.5 or later, BBEdit will guess the source language of the text, and will apply HTML syntax coloring (assuming the URL you fetched was for an HTML document), even if HTML isn’t your default language for new windows. We also set the name of the window to the URL for the source we just grabbed; thus instead of the new window being named “Untitled 4”, it’ll be named “http://daringfireball.net/index.xml”. This makes it much easier to find the window via the Window menu later on.


If instead we had written something like this:


```

    make new text window
    set contents of text window 1 to my_text

```


then BBEdit wouldn’t guess the language automatically. (It would if you saved the new window, but typically the results of this script aren’t going to be saved, so you’d have to set the language to HTML manually.)



| **Previous:** | [Finding Avie](https://daringfireball.net/2003/07/finding_avie) |
| **Next:** | [Market Share](https://daringfireball.net/2003/07/market_share) |


PreviousNext