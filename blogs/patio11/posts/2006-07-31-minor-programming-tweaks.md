---
title: "Minor Programming Tweaks"
date: 2006-07-31
url: https://www.kalzumeus.com/2006/07/31/minor-programming-tweaks/
slug: minor-programming-tweaks
word_count: 235
---


I’m actually cracking open the IDE today.  Nice to get away from marketing for a bit.  I have a bunch of stuff which is neither sexy nor fun but will improve the customer experience:


1)  Currently I pop up a visible JFrame when I print for a split second, which is annoying to the customers (it causes what is perceived as a gray flicker over the application window).  I moved this offscreen, which half solves the problem in one line of code.  The other problem is a new JFrame immediately grabs focus from my window, even if it only lives for a fraction of a second, which causes the title bar to flash a lot.  Going to play around with that some more.


2)  Also related to printing, if you print, say, 30 cards all of them get created before they are spooled out to the print, and they are only garbage collected after the printer reports that it has gotten them.  While this isn’t a problem on my souped-up development machine at least some of my customers are on P3s with 128 MB of ram, so I’ll optimize that (its the only significant use of resources in the program, to my knowledge).


3)  I’m going to give it an icon rather than the default Java cup of coffee.


4)  Maybe, maybe if I have time before dinner I’ll get the math facts thing working.
