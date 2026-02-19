---
title: "Safari’s Unscriptable Tabs"
date: 2003-05-13
url: https://daringfireball.net/2003/05/safaris_unscriptable_tabs
slug: safaris_unscriptable_tabs
word_count: 736
---


Many of you have been asking over the last few weeks what I think of
Safari’s tabbed browsing. (Actually, it’s been months, since the
requests started coming when tabbed browsing first appeared in leaked
private betas; but it’s unsportsmanlike to comment publicly on
non-public software.)


Ignoring the larger issue of the merits of tabbed browsing in general, if you’re going to put tabbed browsing in your web browser, Safari’s strikes me as a fine implementation. The Safari tabbed browsing experience is better than any other I’ve tried. That Safari’s tabs are custom-made controls is just what the doctor ordered. Camino uses standard Aqua tabs, and while it’s admirable to use real Aqua widgets wherever appropriate, standard tabs are inappropriate for tabbed web browsing, and Camino suffers for it.


There’s nothing wrong with custom widgets, if the widgets are meant to provide features not provided by any standard controls. And tabs in a web browser serve a very different purpose than standard tabs in a dialog. Safari’s custom tabs are more usable than Camino’s Aqua standard tabs because they’re left-justified, open in a more intuitive order, and have close boxes.


One complaint about the close boxes in Safari’s tabs, however. I think they ought to more closely resemble the close boxes in window title bars. Widgets that act similarly should look similar. No argument that Safari’s little buttons for closing tabs look better than the standard Aqua close boxes, especially against the metal theme, and also no argument that making the “X” always visible is much preferable to the way you need to roll over the standard Aqua close button to see the “X” — but those are reasons for Apple to improve the standard close buttons, not for Safari to branch out on its own.


But regardless, there’s a huge problem with Safari’s tabbed browsing, and it has nothing to do with how they look. It’s that they’re utterly unscriptable. You can’t do anything with them via AppleScript — you can’t create them, you can’t close them, you can’t even tell if a window has one open tab or 100. In other words, Safari’s scripting dictionary is still constrained by the assumption that each browser window contains only one document.


Needless to say, this sucks.


Back in February I wrote a few scripts for Safari which depend on having access to all open web pages:

- [Scripting Safari URLs](http://daringfireball.net/2003/01/scripting_safari_urls.html) contains a script for use from BBEdit, displaying a dialog box listing every web page currently open in Safari. The URL of whichever one you choose is inserted in the frontmost BBEdit window. Great for linking to web pages you know you already have open, but without having to switch from BBEdit to Safari and then back to BBEdit to copy and paste the URL.
- [Save and Restore Safari URLs](http://daringfireball.net/2003/02/save_and_restore_safari_urls.html) contains a couple of scripts that allow you to save a list of all currently open Safari windows, and to re-open them later. You can use it when you need to quit Safari, but have a bunch of windows open you still want to read later.


Neither of these scripts work with web pages displayed in tabs, nor is there any way to update them so that they can. Safari uses the term `document` to refer to a displayed web page. With tabs turned off, you can get a list of all currently displayed URLs by asking for the URL of every document:


```

tell application "Safari"
    set url_list to URL of every document
end tell

```


When you have tabbed browsing enabled, `every document` only returns a list of the frontmost document in each window. So if you have two windows open, each containing 10 tabbed web pages, `every document` will only return two items: the frontmost tab in each of the two windows. The other 18 documents are unreachable and unknowable via AppleScript.


What I’d like to see is a hierarchical object model. Perhaps top level `browser window` objects, each containing a list of `documents` corresponding to each open tab (there’s no reason to call them “tabs” in the scripting dictionary).


## Postscript: Safari Anti-Aliasing


While Safari’s AppleScript support continues to frustrate, the WebCore rendering engine continues to impress. Most happily for me, public beta 2 fixes the [small monospaced font anti-aliasing bugs](http://daringfireball.net/2003/03/antiantialiasing.html) I complained about two months ago.



| **Previous:** | [Much Ado About Click-Through](https://daringfireball.net/2003/05/much_ado_about_click-through) |
| **Next:** | [SmartyPants 1.3](https://daringfireball.net/2003/05/smartypants_13) |


PreviousNext