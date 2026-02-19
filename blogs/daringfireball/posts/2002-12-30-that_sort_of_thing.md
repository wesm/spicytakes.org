---
title: "That Sort of Thing"
date: 2002-12-30
url: https://daringfireball.net/2002/12/that_sort_of_thing
slug: that_sort_of_thing
word_count: 866
---


One of the complications of using a Carbonized application on Mac OS X is that if the app supports plug-ins, the plug-ins need to be Carbonized as well. BBEdit is one such application.


However, the heyday for BBEdit plug-ins was back in the mid-90’s. Take a look at the [third party plug-ins](http://www.barebones.com/support/bbedit/bbedit-plugins.html) listed at Bare Bones’s web site, and you’ll see that many of them are quite long in the tooth. I don’t think the relative dearth of recent plug-ins is because there is any less developer interest in BBEdit — I think it’s simply that Perl filters and AppleScripts have become so much easier to write. Most of the older BBEdit plug-ins had no user interface and simply manipulated text in certain ways; those types of tasks are *much* easier to write in Perl than in C.


One exception is Craig Maynard’s excellent and popular LineSort plug-in. [Previously available](http://www.uccs.edu/~cmaynard/linesort/) in both lite (free) and full (shareware) versions, LineSort was the easiest and most common way for BBEdit users to perform complicated line sorting and duplicate removal. But it was not Carbonized, and BBEdit users sorely missed it (especially BBEdit users who don’t write Perl).


Bare Bones took matters into their own hands with BBEdit 7, which ships with two new plug-ins: Sort Lines and Process Duplicate Lines. (BBEdit’s previous Sort plug-in was quite simple, offering little more than ASCII sorting and an option to sort in reverse.)


The plot thickens, however, because [LineSort is now freeware](http://linesort.sourceforge.net/) (and open source to boot, released under the GPL), and version 5 finally runs under Mac OS X. It also still runs on Mac OS 9.


The Bare Bones plug-ins and LineSort pretty much offer the same features. When sorting lines, both optionally allow for natural sort order (so that “12” sorts after “7”, for example). Both allow you to sort by a grep pattern. Both allow you to specify whether the sorted lines should replace the text in the current window, or go to a new window.


Their user interfaces, however, are quite different. Bare Bones’s plug-ins use several modal dialog boxes; LineSort uses a single floating palette.


Modal dialogs get a bad rap from many users, so you might find it curious that Bare Bones would choose to use them for new plug-ins. But there are in fact several advantages to modal dialogs. One is that they can be driven by the keyboard. Bring up BBEdit 7’s Sort Lines dialog, then hold down the Command key, and a moment later you will see shortcuts appear for each of the checkboxes in the dialog. These shortcuts don’t conflict with normal menu command shortcuts, because most menu commands are disabled when a modal dialog is open. A floating palette such as LineSort’s can only be driven using the mouse.


I definitely wouldn’t describe LineSort’s interface as pretty, but it seems more straightforward, mainly because it doesn’t offer as many checkboxes as do Bare Bones’s plug-in dialogs. It’s also somewhat convenient to be able to sort lines and remove duplicates in one action; with BBEdit 7’s plug-ins, you need to bring up the Sort Lines and Process Duplicates dialogs separately.


(Then again, when I need to sort lines and remove duplicates, I use the following Perl filter:


```

#!/usr/bin/perl -wl
use strict;

my %seen;
while (<>) {
    chomp;
    $seen{$_}++;
}

foreach (sort keys %seen) {
    print;
}

```


but that’s beside the point.)


## Scripting


BBEdit’s new plug-ins and LineSort are all AppleScriptable (and recordable). Neither allow you to specify a target — they only work on the front window. If there is a selection, only the selected lines are sorted; otherwise, the entire text of the window.


When scripting LineSort, you simply issue the `sort` command along with any optional parameters. Here’s an example LineSort script:


```

tell application "BBEdit"
    sort with natural order and keep one duplicate
end tell

```


BBEdit’s plug-in scripting syntax is more verbose, but I prefer it (if for no other reason than that it’s more similar to scripting the BBEdit application itself). Here’s an example, slightly modified from one of the example scripts that ships with BBEdit 7:


```

tell application "BBEdit"
    -- first, sort the items
    set outputOptions to {replace selection:true}
    set sortOptions to {sort digits numerically:true}
    sort lines sort options sortOptions output options outputOptions
    
    -- then, process them for duplicates
    set matchOptions to {matching mode:leaving one}
    set outputOptions to {kill matched lines:true}
    process duplicate lines match options matchOptions ¬
        output options outputOptions
end tell

```


## Sorting It Out


It’s great that LineSort is alive and kicking on Mac OS X. It’s great that BBEdit now ships with powerful sorting and duplicate processing tools. There’s no reason not to declare the situation a win for everyone.


Since LineSort is now free, BBEdit’s new tools aren’t pinching a revenue stream for Maynard. If anything, the reverse is true — given that LineSort is now free and works on both sides of the Mac OS divide, it lessens the impact of BBEdit 7’s new sorting tools, since LineSort works with older versions of BBEdit, as well as BBEdit Lite.



| **Previous:** | [Rascal](https://daringfireball.net/2002/12/rascal) |
| **Next:** | [Last Minute MWSF Predictions](https://daringfireball.net/2003/01/last_minute_mwsf_predictions) |


PreviousNext