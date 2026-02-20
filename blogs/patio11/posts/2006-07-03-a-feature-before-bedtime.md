---
title: "A Feature Before Bedtime"
date: 2006-07-03
url: https://www.kalzumeus.com/2006/07/03/a-feature-before-bedtime/
slug: a-feature-before-bedtime
word_count: 295
---


I wasn’t exactly happy with the amount of steps it took to get people to use my pre-loaded word lists. You had to learn how to open a file, then navigate through two directories, then pick the list. Sure, four steps is nothing for a computer programmer, but my users… aren’t. So I just put in another, simpler way to do the same thing — a Wizards menu. It automagically parses my data directory and extracts the available templates, then puts them in easy-breezy menu form. Plus it makes for a great screenshot.


[Edit:


The screenshot in question now leads my screenshot page: [check it out](http://www.bingocardcreator.com/screenshots.htm).


Incidentally, total development time for this feature was about 20 minutes of planning, 20 minutes of coding, and 20 minutes of testing.  This was mostly because I started at 10 PM at night and lost 30 minutes to the JMenu.setName and JMenu.setText *not* being equivalent, which isn’t a mistake I would make in daylight hours.  If you start with extensibility and code reuse in mind, Java or any other OO language can be used to rapidly code in new features almost as quickly as Rails or the other new hotness these days.  If you don’t, you end up with hundreds of classes full of totally unmaintainable spaghetti code.  Here’s an example: I spent an extra 10 minutes during this part of the project coding a Factory class.  Why code a factory when I could have just subclassed JMenuItem for a single purpose?  Because with a Factory I can decide tomorrow to make another type of wizard that isn’t just an alias for “read this file” — for example, I can make ones to autogenerate math problems.  Hey, wait, I think there could be a market for that one…


]
