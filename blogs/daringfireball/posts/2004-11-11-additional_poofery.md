---
title: "Additional Poofery"
date: 2004-11-11
url: https://daringfireball.net/2004/11/additional_poofery
slug: additional_poofery
word_count: 960
---


Thanks to the numerous readers who sent in additional observations on
Mac OS X poofery, I offer the following addendum to last week’s bit on
[poof consistency](https://daringfireball.net/2004/11/poof_consistency).


## Safari’s Bookmarks Bar


Safari doesn’t have a poofable Cocoa-style toolbar, but it does offer
poofing from its Bookmarks Bar. You can drag URLs to the Bookmarks Bar
to add bookmarks, and you can drag them off to poof them.


This, however, is perhaps the most inconsistent use of poofing in any
application — because when you poof a Safari bookmark, you are deleting
the actual bookmark itself. In every other instance of poofing, you’re
only removing a reference to something, not deleting actual data. E.g.,
when you poof from the Dock, the original app isn’t deleted; when you
poof from the Finder Sidebar, the original file/folder isn’t deleted;
when you poof from a Cocoa-style toolbar, you can always add the button
back using the Customize Toolbar dialog. But when you poof a Safari
bookmark, it’s gone.


The only good thing about this is that Safari makes poofing undoable.
Otherwise, it’s a bad idea because it breaks the unwritten rule that
poofing is non-destructive, removing only a *reference* to a thing, not
the thing itself.


OmniWeb 5, on the other hand, gets this right. If you attempt to poof a
bookmark from OmniWeb’s Favorites Bar, it just snaps back into place in
the bar. To delete a bookmark from the Favorites Bar, you drag it to the
Trash (or you can use the contextual menu.)


[**Update #1:** Lots of email from readers making the argument that
bookmarks aren’t data, but rather references to web sites, and thus that
Safari’s poofing is appropriate. That’s reasonable, but doesn’t take
into consideration bookmarklets/[favelets](http://tantek.com/favelets/) — which are little bits
of JavaScript code, not references to web sites.]


## Menu Extras


Menu extras are the little iconic menus at the right side of the menu
bar — e.g. iChat’s status menu, or the [system-wide Script menu](http://www.apple.com/applescript/scriptmenu/).
To remove one of these menus from the menu bar, you can poof it by
Command-dragging it anywhere off the menu. (You can Command-drag within
the menu bar to rearrange them.)


One difference between menu extras and other poofables is that you can’t
use drag-and-drop to get them there in the first place. The way to
turn a menu extra on varies widely from extra to extra. iChat’s is
controlled by a checkbox in iChat’s preferences window. The AirPort
status menu can be turned on in two places: the Network panel of System
Prefs, or the AirPort panel in the Internet Connect app. The Script menu
extra is turned on by launching the Install Script Menu applet in the
‘/Applications/AppleScript/’ folder. This isn’t a complaint, per se,
just an observation.


[**Update #2:** A few readers emailed to point out that you can install
Apple’s menu extras using the .menu bundles located at
‘/System/Library/CoreServices/Menu Extras’. But using the Finder, you
can’t install them by drag-and-drop — you need to double-click them.
Oddly enough, however, is that you *can* install them by drag-and-drop
using CocoaTech’s [PathFinder](http://www.cocoatech.com/index.php).]


## Disk Utility Sidebar


Apple’s Disk Utility app has a sidebar listing all of your currently
mounted disks. The sidebar can also contain recently-used disk image
files, and you can drag a disk image file into the sidebar to keep it
there. But how do you remove an image from Disk Utility’s sidebar?


There is no menu command to remove a selected image. Nor is there a
contextual menu command. Dragging an image from Disk Utility’s sidebar
to the Trash seems like a good guess — and the Trash even highlights to
indicate it will accept the drop — but when you let go, the image
simply snaps back to the Disk Utility sidebar.


Poofing is the only way to remove a disk image file from the Disk
Utility sidebar. Judging from my email, this is utterly non-intuitive.
Worse, the only way to poof an image in Disk Utility is to drag it out
of the sidebar, and then drop it anywhere else *within the main Disk
Utility window*. In all other poof implementations, you can drop
anywhere on screen, like, say, the desktop.


Curious side note: Disk Utility’s poof animation is huge — perhaps
double the diameter of the normal Dock and toolbar poof animation.


## The Finder’s Find Dialog


Last but not least, here’s a spot where poofing ought to work, but
doesn’t — with potentially disastrous results.


The Finder’s Find dialog (in 10.3) has several search panels. The most
flexible is the “Specific places” panel, which allows you maintain a
list of frequently-searched folders and/or volumes.


The “Add” and “Remove” buttons do just what you think — adding and
removing places to the list. You can also add items to the list by
drag-and-drop. Drop a folder in the list, and it stays there for future
searches.


But, bizarrely, [drag-and-drop does *not* work for removing items from
the list](http://www.macosxhints.com/article.php?story=20040926174147305). Instead, dragging a folder out of the list *moves the
original folder to wherever you drop it*. This includes dropping items
on the Trash — a gesture one might reasonably assume would simply
remove the folder reference from the list.


Remember, this is not the *results* window of a search — it’s the Find
dialog itself. This list of specific search places is exactly the sort
of list-of-references where Apple typically uses poofing to remove
items. That you’re instead dragging a reference to the original folder
is both unexpected and dangerous.


Drag-and-drop works to add items to the list, but the only way to remove
an item from the list is to use the Remove button.



| **Previous:** | [Examining the Consistency of Your Poofs](https://daringfireball.net/2004/11/poof_consistency) |
| **Next:** | [The True Story of Audion](https://daringfireball.net/2004/11/audion_story) |


PreviousNext