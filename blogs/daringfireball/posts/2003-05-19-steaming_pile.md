---
title: "Steaming Pile"
date: 2003-05-19
url: https://daringfireball.net/2003/05/steaming_pile
slug: steaming_pile
word_count: 584
---


[Chris Nandor:](http://use.perl.org/~pudge/journal/12258)


> I do not want new operating system or application features. I want
> 	the existing features to work properly. People talk about all the cool
> 	stuff in Mac OS X 10.3, and I just don’t care, when iTunes is still
> 	breaking MP3s, my computer is still crashing if I forget to unmount a
> 	network volume before disconnecting the network, passwords with “@” in
> 	them don’t work for remote Apple events, and the Finder is still slow
> 	and buggy all over … 
>  Great, so I will be able to have more transparent graphics. Yippee.
> 	I just don’t care.


[Buzz Andersen:](http://www.scifihifi.com/weblog/mac/AppleComplaint9.html)


> Forget [piles](http://www.eweek.com/article2/0,3959,1036539,00.asp),
> 	journaling file systems, and other showy upgrades: if Apple really wants
> 	to put the user at the center of Panther, they need to fix the
> 	Finder’s problem with [non-sticking
> 	view options](http://www.personal.kent.edu/~blukens/viewoptions.html) (one of the perennial OS X bugs), its inability
> 	to auto-refresh file listings, its lackluster performance, and a number of
> 	other issues.  I think it’s safe to say that these fundamental
> 	problems have affected my personal user experience far more than my
> 	inability to stack files on top of each other!


For all my [griping](http://daringfireball.net/2002/12/finder_reflux.html) about the OS X Finder’s fundamental design problems, I’d probably shut the fuck up about it if it weren’t for all the bugs. The OS X Finder isn’t just a poor design — it’s a poor design poorly implemented.


The hype cycle for upcoming major Mac OS X revisions inevitably includes rumors that the Finder will see huge performance improvements. And then the update ships, and the improvements are less than encouraging. But, hey, why gripe when we can start speculating about the *next* major Mac OS X update? *Surely the Finder will be improved eventually* the thinking goes. Guess what — it’s been seven years since Apple started the project. They don’t deserve any slack whatsoever regarding the quality of the Finder.


Example. One thing that’s been botched in the OS X Finder ever since
10.0 shipped is getting the current selection via AppleScript or Apple
events. (They’re the same bugs — AppleScript is just a scripting
language that sends Apple events.) There might have been a few
revisions in the 10.1.x cycle where this worked perfectly, but it’s been broken again in every revision of 10.2.


Here’s the deal. You want to know what’s selected in the Finder. Here’s the request in AppleScript:


```

tell application "Finder"
    get selection
end tell

```


That’s it. The Finder returns a list of every item (files, folders, disks, etc.) in the current selection.


In Jaguar, the bug is that you can’t get the selection if you have a folder (or disk) selected in column view. What happens is that the Finder returns an empty list, as though you have nothing selected. My guess is that it’s returning the selection of the right-most column that opens up after you select the folder, rather than the column that has focus and which contains the selected folder.


Getting the Finder selection has been at least partially broken for almost all of Mac OS X’s lifespan. I don’t remember it ever being broken in the old Mac OS. Sure, this is a specific example, but the OS X Finder is chock full of minor bugs like this. Maybe you didn’t like the old Finder, but you sure couldn’t call it “buggy”.



| **Previous:** | [JackAssassin](https://daringfireball.net/2003/05/jackassassin) |
| **Next:** | [Waferbaby Interview](https://daringfireball.net/2003/05/waferbaby_interview) |


PreviousNext