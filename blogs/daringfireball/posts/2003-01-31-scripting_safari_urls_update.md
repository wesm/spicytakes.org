---
title: "Scripting Safari URLs Update"
date: 2003-01-31
url: https://daringfireball.net/2003/01/scripting_safari_urls_update
slug: scripting_safari_urls_update
word_count: 335
---


Two updates on “[Scripting Safari URLs](http://daringfireball.net/2003/01/scripting_safari_urls.html)”.


## Open Location


Previously, I complained about Safari’s lack of support for any of the standard  browser commands for opening a URL (such as `GetURL` or `OpenURL`). The best workaround I could come up with, and which I’ve seen elsewhere, is something like this:


```

tell application "Safari"
    make new document at end of documents
    set url of document 1 to "http://www.example.com/"
end tell

```


I figured there had to be a better way. Safari is obviously capable of opening web pages via Apple events. For example, if you have Safari set as your default web browser, it responds to Apple events from your email client when you click links in messages, and it opens web pages when you double-click web location clipping files in the Finder. Those are Apple events, and there’s no way those applications are sending complicated Apple events to Safari — they’re sending 
an open URL event.


Jim Correia provided the solution via email. Although Safari doesn’t have an entry in its dictionary for the standard GetURL Apple event, it is defined in the Standard Additions OSAX as `open location`. So, to open a URL in Safari, you can simply use:


```

tell application "Safari"
    open location "http://www.example.com"
end tell

```


Much nicer, no?


## Insert URL from Safari


Bill Hoffman wrote to ask why our script to insert a URL from Safari into BBEdit used this:


```

set url_list to {}

tell application "Safari"
    set doc_list to every document
    repeat with d in doc_list
        copy URL of d to end of url_list
    end repeat
end tell 

```


to build a list of Safari’s open URLs, instead of this:


```

tell application "Safari"
    set url_list to URL of every document
end tell

```


No reason, except that I didn’t think of it.  Hoffman’s code is shorter and more direct. We’ve revised the script in last week’s article accordingly.



| **Previous:** | [Scripting Safari URLs](https://daringfireball.net/2003/01/scripting_safari_urls) |
| **Next:** | [Save and Restore Safari URLs](https://daringfireball.net/2003/02/save_and_restore_safari_urls) |


PreviousNext