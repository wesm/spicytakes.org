---
title: "That Finder Thing"
date: 2002-11-26
url: https://daringfireball.net/2002/11/that_finder_thing
slug: that_finder_thing
word_count: 2834
---


Nicholas Riley continues his [accurate criticism of the OS X Finder](http://radio.weblogs.com/0100148/2002/11/20.html#a557):


> Someone should be sitting down with the OS 9 and OS X Finders,
> 	trying everything they can think of, comparing behavior, and keeping
> 	consistency where appropriate, and filing bugs. Better yet, that
> 	someone should have been the programmers implementing the OS X Finder
> 	in the first place. 
> For example, that it took until Mac OS X 10.2 for “replace all” to
> 	be an option in the Finder, though still not keyboard-accessible, when
> 	it was both easily keyboard-accessible and the default in Mac OS 9, is
> 	inexcusable. Who do they think has the patience to sit and click
> 	“Replace” repeatedly as the progress window resizes itself over and
> 	over again? 
> [...]
> That’s the essence of my complaint: either the people who write the
> 	Finder at Apple have an incredibly high tolerance for flaky software,
> 	they don’t use it at all, or are placed under pressure from management
> 	such that they don’t have a chance to deliver quality software.
> 	Anything I write - for my own use, even - I would fix if it were as
> 	broken as the Finder is, and if it were heading for use by potentially
> 	millions of users, I’d feel incredibly guilty to subject them to such
> 	garbage.


It’s my guess that the OS X Finder was designed and implemented by former NeXT engineers who neither used (nor liked) the original Finder nor understand the needs of Mac users who do.


The problem described by Mr. Riley above is just one of many examples supporting my theory: when you copy or move a bunch of files that are going to replace other files with the same names, pre-Jaguar versions of the OS X Finder required you to click a Replace button for *each file*, even if there were hundreds of them. Ridiculous.


The Finder is emblematic of everything wrong with Mac OS X. In the years leading up to the initial release of Mac OS X, Mac users only asked for two things from Apple’s next generation operating system:

- Improved stability
- Better performance


What we got:

- Improved stability
- *Worse* performance
- Changes to the user interface


When I talk about changes to the UI, I’m not referring to the cosmetic changes brought about by Aqua. I’m talking about *fundamental* changes — not just how it *looks*, but how it *works*. A minor example is the relocation of the zoom and minimize buttons in window title bars. That’s just change for change’s sake, and it disregards the expectations and habits of long-term Mac users for no good reason.


A major example is the Finder. No one asked for the old Finder to be replaced by NeXT’s file manager, but that’s what we got. The nomenclature in the OS X developer previews made this very clear — the file manager application wasn’t even called “Finder”, it was called “Desktop”.


Clearly, what Apple should have done was create a Mac OS X version of the classic Finder. Not a clone, but an update that remained faithful to the design and spirit of the original. Not having done so, however, Apple would have been better off keeping the “Desktop” moniker; calling it “Finder” just adds to the confusion, because it creates the expectation that it’s supposed to work the same as the old Finder.


It doesn’t. At one point early in the OS X Finder’s life, back when it was still called “Desktop”, it didn’t even offer icon or list views — only the NeXT-style column view. This is not a rant against the column view; it’s a great idea, very useful in certain situations. But it is not the best view for all situations, and it’s downright unsuitable for others. You can’t change the sort criteria in column view, for christ’s sake.


And so Apple was inundated with feedback complaining about the Desktop file manager. The complaints could be summed up as “Bring back the Finder.” But instead of bringing back the Finder, they simply brought back the name, along with a few superficial features.


## Wherein I Digress from the Finder, In an Attempt to Prove a Point About the UI Sensibilities of Former NeXT Engineers


Here’s a list of the valuable assets Apple got when it bought NeXT:

- Steve Jobs
- The Cocoa application framework
- Developer tools like Project Builder and Interface Builder
- A BSD-derived OS supporting all necessary buzzwords
- The Mach kernel


One thing *not* in that list, however, is top-notch user interface design. The NeXT system’s interface was wholly unremarkable. It wasn’t awful, but it wasn’t good, either. But that’s OK, because UI design was one of the areas where Apple was still way ahead of everyone else.


(It’s also the case that Apple did not need any help in kernel design; the [NuKernel](http://www.cocoadev.com/index.pl?NuKernel) project developed internally at Apple was, by all credible accounts, superior to the Mach kernel at the heart of NeXT system. But that’s another story.)


Once the NeXT regime stepped in and assumed top positions in Apple’s software division, they started putting their stamp on Apple’s UI design, despite the fact their input on such matters was neither wanted nor needed. The hallmarks of NeXT’s UI design are extravagant attention to cosmetic appeal, and nearly no attention whatsoever to actual usability. This is enough to fool many people, especially converts switching from other platforms, where the interfaces are both ugly *and* dysfunctional. If it looks better, it must *be* better, right? With that metric in mind, you can start to understand why the NeXTies think so highly of their own UI design skills.


Look no further than Mac OS X’s System Preferences. The icons looks nice, and the window smoothly slides around and redraws itself as you change from one panel to another. But because the list of preference panels occupies the same space as the panels themselves, you can’t switch directly from one panel to another, except for the handful of panels you put in the favorites list atop the window. Now you’re stuck with a favorites list that duplicates 7 or 8 of the icons. You have to figure out on your own that the top row of icons lives by a totally different set of rules than the rest of the icons in the window, even though they look exactly the same. Except for the Show All button, which looks like the other icons but does something unique. Things that look the same should act the same, in proper UI design.


Apple’s iApps provide a broader example. iTunes and iMovie were designed and implemented by Macintosh developers; both are runaway smash hits. iPhoto and iCal, however, were developed only for Mac OS X, and are not nearly as polished. iCal in particular is pretty much a stinkbomb, and bears all the hallmarks of NeXT UI design: looks good, feels clumsy.


## An Ode to the Finder


The most common question I’ve heard about the new OS X Finder is “Why doesn’t it remember the size and location of open windows?” The answer requires an examination of the profound differences in the design philosophies underlying the old and new Finders.


The hallmark of the classic Finder is *spatial orientation*. That’s a buzzword, to be sure, and even long-time Mac users have little idea what it really means, mainly because you don’t have to know what it means to use the Finder.


In the classic Finder, there is no abstraction between the actual file system and the view of the file system presented on screen. A folder is either open or closed. If it is open, it is represented on screen in its own window. The size, position, and viewing options for an open folder’s window are always remembered, and are unrelated to the size, position, and viewing options of parent, sibling, or child folders.


There is a clear, cohesive paradigm at work. An open folder *is* a window; a window *is* an open folder.


There are rules; laws of physics for the Finder universe. One such rule is that Finder items can only appear in one place at a time. For example, let’s say you have a Finder window in list view, and you use a disclosure triangle to display the contents of a folder within that same list. If you then double-click that folder to open it into its own window, the disclosure widget in the list view window will close automatically, preventing the folder’s contents from being displayed in both windows at once. The reverse is true as well — if you go back to the list view window, and click the disclosure triangle for the open folder, the folder window will close automatically before the folder’s contents are displayed in the other window.


This might sound constricting compared to the loose rules that govern the OS X Finder. But it’s been spectacularly successful. The classic Finder has grown tremendously from its original version circa 1984 (when disks were measured in kilobytes), but the underlying paradigm of spatial orientation hasn’t changed.


The key advantage to this design is the lack of abstraction. Direct manipulation is a key element of good UI design, and no application is more direct than the classic Finder. The Finder design is humble — the fact that it even *is* an application is lost on most Mac users. When you’re using the classic Finder, it doesn’t feel like you’re using a “file browser” application to view and manipulate the file system; it feels like you’re working with the file system directly.


The classic Finder is like using your own hands. The OS X Finder is like using a joystick to control a set of robot hands — clumsy and inherently less intuitive.


John Siracusa did an outstanding job describing spatial orientation in his [review of the Mac OS X Public Beta](http://www.arstechnica.com/reviews/4q00/macosx-pb1/macos-x-beta-14.html). The Public Beta release was two years ago, and many of his minor criticisms have been addressed in subsequent releases, but the fundamental problems he describes are still present in the Jaguar Finder:


> The problem is, the OS X Finder as of Public Beta is still
> 	*predominantly* non-spatial.  Even with all the classic-like
> 	options enabled, the behavior is still not even close to the spatial
> 	orientation of the classic Mac OS Finder.  Windows try to remember their
> 	view modes and screen positions, but this feature is easily, frequently,
> 	and often accidentally defeated through the use of basic Finder
> 	functionality.  For example, the folder hierarchy pop-up menu and the
> 	back button in the Finder toolbar always replace the contents of the
> 	current window when used, regardless of your preference settings for the
> 	double-click behavior.  An example scenario:
>  Your home directory is open in a square icon-view window in the
> 	upper-right of your screen.
>  Your documents folder is open in a tall rectangular list-view 
> 	window in the lower left of your screen.
>  You minimize your home directory window.
>  Some time later, you’re working with your documents folder and you
> 	want to go up one level to your home directory, so you select it from
> 	the hierarchy pop-up menu in the window toolbar.
>  This causes contents of your list-view window to be replaced with
> 	the contents of your home directory.  They’re in icon view, and the icon
> 	positions are the same, but the size and position of the window are that
> 	of the documents window whose contents they replaced.  Your minimized
> 	home directory window remains minimized in the Dock.
>  You maximize your home directory window.  It appears in its former
> 	position and size in the upper-right of your screen.  Now you’ve got two
> 	windows showing the contents of the same folder in two different places
> 	on your screen.
> This is but one of the many confusing, spatially inconsistent
> 	scenarios that is possible with the OS X Finder.  I was tempted to just
> 	chalk it up to understandable beta bugs, but the unavoidable question is
> 	this: how is it *supposed* to work then?  The combination of
> 	in-place browser-style functions and the totally new concept of creating
> 	a “New Finder Window” (which is incidentally bound to command-n,
> 	destroying 16 years worth of muscle memory in the millions of Mac users
> 	who expect that sequence to create a new folder) necessarily compromises
> 	the spatial nature of the Finder.
> Again, that’s not necessarily a bad thing, *provided* this
> 	time-tested and heavily evolved functional interface is replaced with
> 	something *better* (it’s not enough just to equal the old interface
> 	since a shift in something as fundamental as the Finder had better be
> 	worth throwing away almost two decades of familiarity for.)
> Unfortunately, the OS X Finder as it exists in Public Beta does not
> 	achieve this goal.  Worse, it not only removes all the evolutionary
> 	additions to the classic spatial Finder (pop-up tabbed folders,
> 	spring-loaded folders, etc.), it entirely compromises the spatial
> 	metaphor itself.  Just imagine if that folded newspaper you put on the
> 	corner of your desk *wasn’t* there a few hours later, or was there
> 	but unfolded, or was under your chair.  You’d start to think someone was
> 	toying with you, or maybe that you’re going senile.  For a spatially
> 	oriented system to be effective, it must be absolutely consistent.


## Wherein I Offer a Solution


The classic Finder is a paragon of consistency and intuitive design. In the OS X Finder, double-clicking on a folder produces completely different results depending on the visibility state of the current window’s toolbar. *This is madness.*


Many Mac users think the OS X Finder is merely ill, a nascent design in the still-new Mac OS X environment, and that with some elbow grease and Apple magic, it will someday soon be restored to its former glory.


But the Finder is not sick; it is *dead*, replaced by an entirely different application that’s been patched to bear a superficial, skin-deep resemblance to the real Finder.


And so we’re back to core question: *Why?*


Why replace the greatest and most beloved application in the history of the Macintosh with an ill-conceived “file browser”? The OS X Finder doesn’t just suffer from rough edges and poorly-worded error dialogs. It is broken from the outset — a poor design intended to replace a brilliant design.


The explanation is as sad as it is obvious. UI design decisions at Apple are now in the hands of people who do not understand good UI design. What makes it sad is not just that Apple’s standards used to be so much higher, but that there are still so many talented designers working there.


Which leads us back to Nicholas Riley’s admonition, excerpted at the beginning of this essay:


> Someone should be sitting down with the OS 9 and OS X Finders,
> 	trying everything they can think of, comparing behavior, and keeping
> 	consistency where appropriate, and filing bugs. Better yet, that
> 	someone should have been the programmers implementing the OS X Finder
> 	in the first place.


The fact is, the current Finder engineers are the least likely people at Apple to fix the Finder. (Where by “fix”, I mean “restore to greatness”.) If there’s a team of engineers at Apple that ought to be assigned the task of fixing the Finder, it’s the engineers behind the *classic* Finder.


Apple’s path is clear:

- Restore spatial orientation as the fundamental paradigm underlying the Finder’s UI. Bring back the one-to-one mapping between folders and open windows. Welcome Mac OS 9 holdouts with open arms.
- Keep the new column view, but *not* as an alternative to icon and list views for normal (spatial) Finder windows. Instead, create a distinct new “Column Browser” window class, which acts like the column view in the current OS X Finder. When you double-click a folder in a Column Browser, however, it should open in a regular (spatial) Finder window.


Let the Column Browsers live outside the spatial laws of the Finder universe — go ahead and display the same folder’s contents in six different Column Browsers. I see no reason why Column Browsers can’t gracefully live atop a spatially-oriented Finder (similar to how [Greg’s Browser](https://web.archive.org/web/20030210225311/http://www.kaleidoscope.net/greg/browser.html) works just fine alongside the classic Finder, but even better, since a single application could provide tighter integration between the two paradigms).
- Give Command-N back to “New Folder”. Use Shift-Command-N for “New Column Browser”. Make it easy to swap these keystrokes as a preference, for the benefit of the sad souls who have grown accustomed to the current OS X Finder.


Doable? Certainly.


But I’m not holding my breath.



| **Previous:** | [DMG](https://daringfireball.net/2002/11/dmg) |
| **Next:** | [Thanksfindering](https://daringfireball.net/2002/11/thanksfindering) |


PreviousNext