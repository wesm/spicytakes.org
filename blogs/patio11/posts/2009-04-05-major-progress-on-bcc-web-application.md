---
title: "Major Progress on BCC Web Application"
date: 2009-04-05
url: https://www.kalzumeus.com/2009/04/05/major-progress-on-bcc-web-application/
slug: major-progress-on-bcc-web-application
word_count: 536
---


I did some more work on the upcoming BCC 3.0 this weekend, which is going to coexist on the desktop and the Internet.  (Feel the power of Web 2.0… several years late!)


The biggest challenge with BCC coding-wise has always been laying out the bleeping cards.  Mostly, this is because Java has very primitive printing facilities.  I render everything to a Swing canvas and then essentially print the canvas, and Swing is most definitely not designed as a printable format.  This exacerbates some issues which are always going to be hard, such as “How do I automatically size text so that it looks visually appealing without requiring user input?”


Since printing in a web application is sort of hard to control (CSS and usability issues galore), I’ve opted to generate PDFs, which is a quite common choice.  The [Prawn library](http://prawn.majesticseacreature.com) (a new-ish alpha-quality Ruby library for PDF printing) is an absolute lifesaver — I’ve got better behavior out of it in 8 hours of playing around then I’ve been able to coax out of BCC in 2 years.  There is still some ugly spaghetti code hiding in the bowels of it, but its literally a quarter of the size of the stuff in BCC itself, and much, much more comprehensible.


Feast your eyes:


(I know, Roald Dahl’s name is screwed up due to some sort of encoding issue.)


Here’s the [same card](http://www.bingocardcreator.com/bingo-cards/literature/children-authors) printed in Bingo Card Creator:


I really prefer the Prawn version to the Java version for out of the box behavior:

- prettier autosizing (particularly for the column headers)
- better line breaking logic
- better centering of the words in the squares
- capability to add titles (often requested by customers, never implemented in Java because it would essentially require a rewrite of code that I scarce dare to tread in)
- capability to add watermarks/footers (often requested by, erm, me)


Printing is, by my estimation, about 90% accomplished.  (I still need to work out some internationalization kinks and then figure out how I’m going to generate the PDFs and store them outside of the web request/response cycle — I don’t want someone printing 800 cards for a Fortune 500 retreat to lock up the server accidentally, but I do want to support that use case.)


After I get printing done I still need to:

- Code GUIs for word entry, loading/saving lists, etc.
- Figure out user management (usernames/passwords, forgot password, restricting access appropriately, etc)
- Extend my admin interface so that I can address issues that people have, should they have any.
- Figure out how to integrate the web app into my site without confusing the heck out of people.
- Rewrite a whole lot of copy.  (See the above point.)
- Sprinkle my pages with copious sign-up-for-webapp-now calls to action.
- Adjusting the BCC client for close-to-seemless integration with the website (save to/load from Internet)


Now that printing is mostly working the technical issues are all downhill from here.  My biggest worry is the perinneal one for web applications: can I convince non-technical users that “web sites” are worth paying money for?  This is one of the main reasons I’m not planning on deprecating the downloadable version anytime soon.
