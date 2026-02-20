---
title: "Lightbox — Quick, Pretty Screenshot Previews"
date: 2007-04-14
url: https://www.kalzumeus.com/2007/04/14/lightbox-quick-pretty-screenshot-previews/
slug: lightbox-quick-pretty-screenshot-previews
word_count: 332
---


Every uISV has a screenshot page and, if you’re sane, a shot of your program above the fold on your front page.  These are generally teeny-tiny thumbnails which exist more to demonstrate the fact that there is a real purchasable product than anything else.  Of course, customers actually want to be able to read the text on your GUI, so you link that thumbnail to an image file… and bad stuff happens.


For the non-technical B2C market, “bad stuff” generally means “Prospective customer cannot find their way out of the image”.  Yes, I know, I know, they have a back button.  They may not KNOW they have a back button, though.  My screenshots, for the longest time, had 80%+ bounce rates until I figured this out.  So I’ve been using the _blank thing to pop the screenshot up in a new window, which is a decent compromise but it distracts unduly from the sales pitch.  They have to close that window to get back to reading, and I’d rather they have a visual reminder of what exactly they were doing so they don’t get distracted, switch to their email, and go away.


Luckily, there is this nice little Javascript widget called [Lightbox](http://www.huddletogether.com/projects/lightbox/) (introduced to me by the indispensable Nick Hebb, king of [flowchart software](http://www.breezetree.com/)).  Add two lines of code to your web page, tag screen shots with rel=”lightbox”, and you get a shiny Javascript preview effect which is quite similar to e-junkie’s [Fat Free Cart](http://www.e-junkie.com).  It grays out the rest of the page but keeps it visible, and directs your attention directly on the screenshot — a single click anywhere dismisses it, taking you back to the page.  (There is a [Lightbox2](http://www.huddletogether.com/projects/lightbox2/) which has more sophisticated behavior which is, for my customers, a usability nightmare.  I passed.)  You can take a quick gander at the home page for [Bingo Card](http://www.bingocardcreator.com) Creator — try playing with the main screen shot to see Lightbox and the purchasing page to use the Fat Free Cart.
