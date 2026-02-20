---
title: "A/B Testing Lightbox Screenshot vs. Screenshot + Download Link"
date: 2009-02-22
url: https://www.kalzumeus.com/2009/02/22/ab-testing-lightbox-screenshot-vs-screenshot-download-link/
slug: ab-testing-lightbox-screenshot-vs-screenshot-download-link
word_count: 418
---


Everybody paying attention to this blog recently knows I have an unhealthy fascination with Lightboxes, particularly my new favorite [iBox](http://www.ibegin.com/labs/ibox/).  I like them because they work really well at increasing conversions, [most recently in my shopping cart](http://www.bingocardcreator.com/articles/developing-shopping-cart.htm).  (Incidentally, guys, I went back and reset the test.  It really is about 100% improved over the old version.)


So this week I removed the old Lightbox lightbox from my home page and replaced it with an iBox.  I haven’t looked in any rigorous fashion whether that improved things or not — I just did it to cut a few kilobytes off all the Javascript people have to download to use my site, and also because I think the iBox looks cooler out of the box.


Then I noticed that the iBox introduces a loading screen, which the old lightbox did as well.  **I hate load screens**.  When I see them I think “This is me, losing money”.  Because if two seconds to load the shopping cart cost me half of my potential sales then 2 seconds to look at a screenshot must likewise be suboptimal, and MANY people look at the screenshot (something like 20% of the people who view the page, if CrazyEgg is counting right).


Also, unlike Lightbox, iBox can cause you to get dumped direct to image if you click before the script loads.  Bad news, bears, that means a bounce for most of my users.  I got around this by putting onclick=”false” on the relevant links.


Many, many moons ago (in late 2007!) I experimented with adding blue instructory text to the lightboxed image, exhorting people to download the trial.  That was a crashing failure — it looked like a link but if you clicked it, wham, the image vanished.  But I sort of like the general idea, so it is time for a new split test — take a gander at the [screenshot behavior here](http://www.bingocardcreator.com/index-alternate.htm) and tell me if you like it.


You could see the old version of the behavior on my homepage but, well, only if you flip heads the first time you load it.  It is basically the stock lightbox effect — brings up an image, click anywhere to dismiss the image.


I’m hoping for a lift in trial downloads, particularly from clicks coming from advertising.  My worry is that the people are going to get stuck in the lightbox and bounce, since it is much harder to dismiss now.  Oh well, that is what testing is for.  Bring on the visitors!
