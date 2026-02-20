---
title: "Drop-Dead Simple Update Checking"
date: 2006-07-27
url: https://www.kalzumeus.com/2006/07/27/drop-dead-simple-update-checking/
slug: drop-dead-simple-update-checking
word_count: 350
---


I just had this brainstorm and wanted to share.  It should be live in my program by, oh, the end of today:


Checking for updates is a wonderful thing to enable, both because it makes sure your customers have the best-and-brightest version of your product available, and because it lets you see on your web logs “Ahah, that install actually succeeded”.  I wanted to have it ready for my first release (there have been at least 10 mini-releases since then, all with the same version number) but couldn’t figure out a way to do it simply.


Enter the drop-dead simple version checking solution: make a directory on your website (I’d put it in robots.txt too with an exclusion, as its going to have duplicate content and you don’t want it to be a search result anyway).  Populate it with a bunch of HTML files corresponding to your version numbers (e.g. v1.0.htm, v1.01a.htm, beta_release.htm, whatever you want).  All the ones but the “latest” one say “You need to update your software.  Here’s how:”, with your favorite tracking code embedded.  The latest one says “Yep, your software is up to date”, has the tracking code, and maybe gives a bit of advice or something (hey, why miss an opportunity to sell to people).  Every time you add a new version, you change the version number in the executable/resource file/wherever, rename your up-to-date page to the new number, and put an out-of-date page in place of the old page.


BAM.  This takes only 10 seconds per update, requires no additional programming, and can be done in 100% static HTML (no need to query a CGI script or anything).  Then you put a Check for Updates item in your Help menu, and perhaps pop up a window on program execution the first time its executed (“Thank you for using X.  Would you like to check for updates now?”) and perhaps every 2 weeks or a month after the program is installed.  Its not quite as seemless to the user as, say, Firefox’s automatic updating, but it’s a heck of a lot simpler for you.
