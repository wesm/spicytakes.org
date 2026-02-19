---
title: "Scripting Safari URLs"
date: 2003-01-23
url: https://daringfireball.net/2003/01/scripting_safari_urls
slug: scripting_safari_urls
word_count: 725
---


In my [initial review of Safari](http://daringfireball.net/2003/01/safari.html), I complained about its lack of scriptability. Ends up that criticism was somewhat misguided — Safari actually is fairly scriptable.


What threw me off after first looking at the Safari scripting dictionary is that it doesn’t support the standard web browser Apple event commands, such as `OpenURL` or `GetURL` (both of which IE’s scripting dictionary supports). Safari does support the Standard and Text suites, and also something the called the Safari suite.


In the current beta, the Safari suite contains just a single entry: a `document` object, which contains useful properties such as `URL` and `source`. We used the `source` property a couple days ago in the [script to view source in BBEdit](http://daringfireball.net/2003/01/safari_source_in_bbedit.html).


In IE, you can simply use the OpenURL command to load a URL:


```

tell application "Internet Explorer"
    openURL "http://www.example.com/"
end tell

```


The equivalent code for Safari, uses the `URL` property:


```

tell application "Safari"
    make new document at end of documents
    set url of document 1 to "http://www.example.com/"
end tell

```


I’m not sure why the “`at end of documents`” part is necessary, but scripts won’t work without it. It would certainly be easier, and the syntax more obvious, to simply say “`make new document`”, but if you try that, you get an error when running the script. (And a rather unhelpful error, at that: “An error of type 6 has occurred.”) This “`at the end of documents`” detritus seems to be necessary when creating new document windows via AppleScript in any Cocoa application; you need to do the same thing when making a new window in TextEdit, for example. Unintuitive superfluous syntax like this, combined with unhelpful error messages, is what gives AppleScript a reputation for being hard to write.


In what should come as a surprise to no one, I do all of my Fireball writing in BBEdit. When I insert hyperlinks, I often have the about-to-be-linked-to-URL open in a browser window already. To get the URL from the browser into my BBEdit document, I must:

1. Switch to the browser.
2. Switch to the corresponding window in the browser.
3. Select the URL in the location field.
4. Copy.
5. Switch back to BBEdit.
6. Paste.


So why not use AppleScript to make this process shorter? What follows is an AppleScript intended to be called from within BBEdit (save it in the Scripts folder in your BBEdit Support folder). When invoked, it presents a dialog box listing every currently open URL in Safari. Choose the URL you want, then click the Insert button to insert that URL in the frontmost BBEdit window.


### Insert URL from Safari


```

tell application "Safari"
    set url_list to URL of every document
end tell

tell application "BBEdit"
    set the_url to choose from list url_list ¬
        with prompt ¬
        "Insert URL from Safari window:" OK button name "Insert"
    if the_url is not false then
        set selection of text window 1 to the_url
    end if
end tell

```


Here’s how it works.


First, we create `url_list`, a list to hold the URL of each open document window in Safari.


Then we tell BBEdit to display a listbox dialog. The `choose from list` command is part of the Standard Additions scripting addition. It takes a list as a parameter, and returns a string with the value of the list element that was selected, which we store in a variable named `the_url`. Before we use `the_url`, however, we need to check if its value is `false`, which will be the case if the user clicked the Cancel button.


There’s nothing unique to Safari about this script. With a few minor changes, we can have a version that works with IE (on both Mac OS 9 and Mac OS X):


### Insert URL from IE


```

set url_list to {}

tell application "Internet Explorer"
    set window_list to ListWindows
    repeat with w in window_list
        set r to GetWindowInfo w
        copy item 1 of r to end of url_list
    end repeat
end tell

tell application "BBEdit"
    set the_url to choose from list url_list ¬
        with prompt ¬
        "Insert URL from IE window:" OK button name "Insert"
    if the_url is not false then
        set selection of text window 1 to the_url
    end if
end tell

```



| **Previous:** | [Safari Source in BBEdit](https://daringfireball.net/2003/01/safari_source_in_bbedit) |
| **Next:** | [Scripting Safari URLs Update](https://daringfireball.net/2003/01/scripting_safari_urls_update) |


PreviousNext