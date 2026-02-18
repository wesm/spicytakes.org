---
title: "Examining the Consistency of Your Poofs"
date: 2004-11-02
url: https://daringfireball.net/2004/11/poof_consistency
slug: poof_consistency
word_count: 1778
---


A little over a week ago, I posited that the inconsistent use of brushed
metal windows [doesn’t really matter](https://daringfireball.net/2004/10/does_brushed_metal_matter). The idea being that the sort
of consistency that does matter in interface design is in terms of
meeting user expectations.


And so one reason not to waste more time on brushed metal windows is
that Mac OS X has plenty of other consistency problems, real ones,
which aren’t about subjective aesthetic tastes. One example is
click-through, which I wrote about extensively over a year ago, and
which situation hasn’t gotten any better since then:

- [The Problems With Click-Through](https://daringfireball.net/2003/05/the_problems_with_clickthrough)
- [Much Ado About Click-Through](https://daringfireball.net/2003/05/much_ado_about_clickthrough)


Another area of behavioral inconsistency is the conflict between
*poofing* and normal drag-and-drop.


In the old Mac OS, there was one clear way to delete something using a
mouse gesture, that being to drag it to the Trash. This worked
remarkably well for the Finder: users were able to easily and safely
delete files and folders. Easily because the semantics behind dragging
items to the Trash icon are easy to grasp. Safely because using
the Trash is a two-step process — first drag to the Trash, then invoke
the Empty Trash command to actually delete the Trash’s contents.


Everyone knows how the Trash works now, and every desktop OS uses a
similar metaphor for deleting files and folders. But at one point it was
new, and it was Apple that pioneered it. In those days end users were
expected to use command-line tools such as Unix’s `rm` or DOS’s `del` to
delete files, and catastrophic mistakes were common — you were never
more than one bad wildcard away from wiping out essential files.


With Mac OS X, however, Apple introduced a second way to delete certain
types of items using a mouse drag: the poof. E.g. when you drag a
non-running application’s icon off the Dock, it poofs, and it’s removed
from the Dock.


It’s a cute effect, made for demoing how cool Mac OS X looks — but it’s
shitty user-interface design, and Apple has implemented it
inconsistently.


One thing that is sort of consistent about poofing is in the sort of
item it’s used for. Apple only uses poofing as a technique for deleting
proxy icons. When you poof an app off your Dock, you haven’t deleted the
app itself, you’ve simply removed its proxy icon from your Dock. Apple
never uses poofing for the deletion of actual data or files.


## Dock Poofing


Many long-time Mac users consider the Dock to be the single worst
interface change from the old Mac OS to Mac OS X. I’ve never felt the
outright hatred toward the Dock that some do, but it is a confounding
little bugger.


Most complaints about the Dock boil down to the fact that it’s neither
optional nor replaceable. Even if you kill it — literally, using the
`kill` command-line tool — it comes right back. While technically just
an application (/System/Library/CoreServices/Dock.app), it receives
special treatment by the system itself.


Much of this initial revulsion, however, was just resistance to the Dock
because it was new and different. People who’d been working a certain
way with their Macs for many years simply didn’t want to deal with
something new.


In certain of its details, however, the Dock remains frustrating and
irritating to long-time Mac users because it works in unexpected — dare
I say “un-Mac-like”? — ways. Such as poofing.


Icons in the Dock are a unique breed of proxies. When you drag them,
they are not direct representations of the items themselves. But neither
are they aliases, which is what they should be — and which is how app
proxies are handled in third-party “dock” utilities such as [DragThing](http://www.dragthing.com/).


What is it that you’re dragging when you drag an icon in the Dock? It’s
just a proxy icon, and pertains *only* to the Dock itself. You can drag
it within the Dock to rearrange the order of the icons. And you can drag
it off the Dock, and it poofs — which removes the app from the Dock,
but leaves the actual app itself in place in your file system. (Same
with folders or files or whatever other icons you store in your Dock.)


Unless the app is already running. In which case when you drag it off
the Dock and let go, it just shoots right back into the Dock, no poof.
But that doesn’t mean the drag-off-the-Dock didn’t take — when you
eventually quit that app, its Dock icon disappears, sans poof, in the
same way icons do for apps that aren’t permanent Dock residents. This is
just a confusing side-effect of the Dock’s conflated roles as both
a launcher and process manager.


But what if you want to drag a useful representation of the app itself?
For example, the easiest way to open an app’s AppleScript dictionary in
Script Editor is to drag the app onto Script Editor’s icon. Thus, a Mac
user’s instincts would be to drag an app’s icon in the Dock and drop it
onto Script Editor’s icon in the Dock. But that doesn’t work, because
dragging within the Dock only allows for rearranging the icons.


The answer is to Command-drag: press and hold the Command key on your
keyboard while you drag an app’s icon in the Dock. When you do this,
instead of the usual Dock proxy icon, you get a real reference to the
application itself. You can see the difference — when you just plain
drag Dock icons, the icons are translucent; when you Command-drag them,
the icons are opaque.


Thus, you can Command-drag a Dock icon and drop it onto Script Editor,
and Script Editor will open that app’s dictionary. (This works for any
application that can “open” another application, e.g. BBEdit, which will
open a disk browser window displaying the contents of an app’s package
— a useful shortcut for peeking at application resources.)


If you Command-drag an icon off the Dock, you’re effectively dragging
the application itself, just as though you had initiated the drag from
the Finder. E.g., Command-drag an app icon from the Dock to the desktop,
and instead of a poof, you’ll move the application itself from wherever
it was installed to your desktop folder. Command-Option-drag, and you’ll
create an alias to the application.


Knowing this Command-drag shortcut makes the Dock much more useful.
However, it’s very much counter-intuitive. Much better is the behavior
of DragThing, where regular (no modifier key) drags are aliases to the
original application. You can thus just plain drag one app’s icon from a
DragThing palette and drop it onto Script Editor, and it does the right
thing. If you just plain drag an app icon and drop it on the desktop, it
doesn’t move the original application, but instead creates an alias to
it.


In other words, instead of poofing on unmodified drags, the Dock should
allow you to drag an alias to the app. How would you delete an icon from
your Dock? Well, obviously: you’d drag it to the Trash. The Dock already
*does* support dragging icons to the Trash, and upon doing so, pops up
text next to the Trash reading, “Remove From Dock”.


And indeed, dragging to the Trash is how one uses the mouse to remove
icons from a DragThing palette — and when you do, you still get the
cool poof animation, if that matters to you.


In short, the Dock’s poofing gets in the way of dragging Dock icons
(without modifier keys) to do useful things, and it’s unnecessary, since
it would be easy and obvious to drag-to-the-Trash to remove icons from
the Dock.


## Finder Poofing


As of 10.3, the Finder now supports poofing in its metal-window-mode
sidebar. The Finder’s sidebar acts quite a bit like the Dock, in fact.
Items in the sidebar are purely proxies, which are usable only within
the sidebar itself. Drag them within the sidebar to rearrange, drag them
out of the sidebar to poof.


The Finder’s sidebar poofing is very much like the Dock’s, in that it
only removes the item from the sidebar, but has no effect on the actual
item itself. One significant difference, however, is that when you’re in
mid-poof in the Finder, it switches to a special poof cursor:


This is rather helpful, as it gives you instant feedback that you’re not
really dragging the item itself, or an alias to it, but rather that
you’re simply removing the item from the Finder’s sidebar. The Dock
would do well to use a poof cursor as well.


Alas, the poof cursor is not the only inconsistency between the Finder’s
and Dock’s poofing behavior. In the Finder’s sidebar, poofing is the
*only* available dragging action — no combination of modifier keys will
allow you to drag an actual reference to the item itself. Sidebar items
can act as drag targets (you can drop items onto them), but can never
serve as draggable items themselves.


Thus, in the Finder sidebar, the entire concept of dragging — one of
the most useful actions of the Mac’s UI vocabulary — is wasted entirely
on poofing.


Much better would be if sidebar items were aliases (or at least acted
like aliases). Then they could serve both as drop targets and draggable
items. And if you wanted to remove an item from the sidebar you could —
*you can see this coming from a mile away* — just drag it to the Trash.


## Toolbar Poofing


Mac OS X also uses poofing when you remove items from Cocoa-style
toolbars (which aren’t limited to Cocoa apps, but which I can’t think of
a better name for).


When you configure such a toolbar (using the View → Customize Toolbar
command), the toolbar icons act similarly to Dock icons: drag within the
toolbar to rearrange, drag out of the toolbar to poof.


You can also invoke these features without opening the Customize Toolbar
dialog by Command-dragging at any time.


In neither case do you get a poof cursor like you do in the Finder; it’d
be a nice touch for Cocoa to steal this idea from the Finder.
Context-sensitive cursors — e.g. the “you’re making a copy” cursor
shown below — ought to be used consistently throughout the system:


Toolbars are the one place Apple uses poofing where it is wholly
appropriate. Toolbar icons aren’t representative of actual items such as
folders or files. They only have meaning within the toolbar itself.
Dragging-to-poof in a toolbar isn’t coming at the expense of any other
useful dragging actions, unlike with the Dock or the Finder’s sidebar.



| **Previous:** | [iPod Mania](https://daringfireball.net/2004/10/ipod_mania) |
| **Next:** | [Additional Poofery](https://daringfireball.net/2004/11/additional_poofery) |


PreviousNext