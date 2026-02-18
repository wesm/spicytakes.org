---
title: "BBEdit Soft Wrap Toggling"
date: 2004-10-04
url: https://daringfireball.net/2004/10/bbedit_soft_wrap_toggling
slug: bbedit_soft_wrap_toggling
word_count: 678
---


In BBEdit’s parlance, *soft wrapping* is what happens when long lines of
text are automatically wrapped to the next line. If soft wrapping is
off, long lines scroll off the right side of the window instead of
wrapping.


There are two ways to toggle soft wrapping in the front window using the
regular UI — a checkbox in the Edit → Text Options dialog, and a menu
item in the Text Options drop-down menu in the Status Bar. One common
question is whether there’s a way to toggle soft wrap using a keyboard
shortcut.


Prior to BBEdit 8, the answer was to use an AppleScript, and then assign
a keyboard shortcut to the script. Here’s a script that simply toggles
soft wrap on and off in the frontmost window:


```
tell application "BBEdit"
    tell window 1 to set soft wrap text to not soft wrap text
end tell

```


BBEdit 8 now provides a built-in way to assign keyboard shortcuts to
Status Bar menu items. Open the BBEdit → Set Menu Keys dialog, and near
the bottom of the list is an entry for Status Bar, containing items from
the Text Options, Markers, and File Options drop-down menus. This is now
the easiest way to add keyboard shortcuts for frequently-used status bar
items.


However, I still use an AppleScript for toggling soft wrap via the
keyboard. The reason is that depending upon the context, I use three
different soft-wrap states:

- off
- wrapped to a fixed width
- wrapped to the width of the window


When I’m writing source code, I typically leave soft wrap off. When I’m
writing prose, I turn soft-wrapping on, with the wrapping width set to
80 characters. When I’m editing HTML markup, however, I tend to turn
soft-wrapping on, but wrapped to the entire width of the window
instead
of a fixed width.


Another new wrapping-related feature in BBEdit 8 is the Page Guide — a
subtle light gray vertical indicator at a specified character width. The
Page Guide replaces BBEdit’s old Philip Bar. You can specify the
character width for the Page Guide in BBEdit’s Text Status Display
preferences panel; the default is 80.


The Page Guide isn’t necessarily light gray; it’s a slightly darker
shade of whatever color you’ve specified as your text window background
color. So if your text window background is pale green, the Page Guide
will be a slightly darker shade of green. (If your background color is
black, the Page Guide is slightly *lighter*.) I use a light gray
background color — `rgb(225, 225, 217)` — so with the Page Guide
displayed, it looks like this:


The following script switches between the aforementioned three soft-wrap
modes. When wrapped to a fixed width, it displays the Page Guide and
uses it as the wrap width. In the other two modes — off and wrapped to
the width of the window — the Page Guide is hidden. Thus the Page Guide
provides a visual indication of the current soft wrapping status.


```
tell application "BBEdit"
    tell window 1
        if not (soft wrap text) then
            set soft wrap text to true
            set soft wrap mode to page guide
            set show page guide to true
        else if (soft wrap mode is page guide) then
            set soft wrap mode to window width
            set show page guide to false
        else
            set soft wrap text to false
        end if
    end tell
end tell

```


I’ve assigned the keyboard shortcut Ctrl-W to this script (using the
Scripts palette). By default, my new BBEdit documents open with soft
wrap turned off (as specified in the Editor Defaults preferences
panel). So if I want to turn soft wrap on, I hit Ctrl-W, and then the
Page Guide appears and the text is wrapped to the Page Guide. If I hit
Ctrl-W again, the Page Guide disappears and the text is wrapped to the
width of the window. Once more and I’m back where I started, with
wrapping turned off.



| **Previous:** | [‘Rename Active Document’ Script for BBEdit](https://daringfireball.net/2004/10/rename_active_document) |
| **Next:** | [T-shirts Redux](https://daringfireball.net/2004/10/tshirts_redux) |


PreviousNext