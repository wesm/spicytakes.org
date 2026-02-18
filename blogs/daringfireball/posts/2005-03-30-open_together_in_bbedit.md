---
title: "Opening Files Together in a New BBEdit Text Window, Redux"
date: 2005-03-30
url: https://daringfireball.net/2005/03/open_together_in_bbedit
slug: open_together_in_bbedit
word_count: 310
---


Back in September, after BBEdit 8.0 shipped, [I posted an
AppleScript](https://daringfireball.net/2004/09/bbedit_open_together) you could use to open a bunch of files together in a
single new window, which was something you couldn’t do out-of-the-box
with BBEdit’s new documents drawer. The choices in BBEdit 8.0 were to
either open each document in its own window (i.e. the traditional
multi-window behavior BBEdit has always offered), or you could always
have documents open within the current frontmost window.


I use the script with [Ranchero’s Big Cat Scripts](http://ranchero.com/bigcat/) plug-in, so
that I can invoke it from the Finder’s contextual menu simply by
Control-clicking on the files I wish to open together.


In my original script, I had to go through a few minor contortions to
work around some of the limitations of BBEdit 8.0’s scripting support
for the documents drawer. [BBEdit 8.1](http://www.barebones.com/support/bbedit/arch_bbedit81.shtml) (released two days ago) makes
this a lot easier, by adding an optional `opening in` parameter to the
`open` command. Your choices for the `opening in` target are
`front_window`, `separate_windows`, and the one we want: `new_window`.


Here’s the new version of the script:


```
on main(file_list)
   tell application "BBEdit"
      open file_list opening in new_window
      tell text window 1
         set show documents drawer to true
         set show navigation bar to true
         activate
      end tell
   end tell
end main

```


(The `main` handler is a Big Cat Scripts idiom; see the [previous
article](https://daringfireball.net/2004/09/bbedit_open_together) for more details on using this with Big Cat.)


This script is not only more concise and intuitive than the version
from September, but executes a bit quicker as well.


## Update


[Chris Nandor has updated his Perl version](http://use.perl.org/~pudge/journal/23958) of the same script, and also offers a bunch of tips for making use of the `bbedit` command-line tool.



| **Previous:** | [Pre-Order Tiger From Amazon](https://daringfireball.net/2005/03/preorder_tiger) |
| **Next:** | [Point, Counterpoint: Mac OS X Is Great for Fortysomething Unix Hackers](https://daringfireball.net/2005/04/point_counterpoint) |


PreviousNext