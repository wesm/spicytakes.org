---
title: "Bingo Card Creator Goes Web 2.0"
date: 2009-06-28
url: https://www.kalzumeus.com/2009/06/28/bingo-card-creator-goes-web-2-0/
slug: bingo-card-creator-goes-web-2-0
word_count: 638
---


Three years ago, on July 1st 2006, I released version 1.0 of [Bingo Card Creator](http://www.bingocardcreator.com).  It was ugly, underfeatured, and bug-ridden.  Now, it is ugly, underfeatured, and bug-ridden… with AJAX!


Feast your eyes at this very, very early [sneak peak](http://staging.bingocardcreator.com).  You’ll want to click one of the various “sign up now” text links rather than the download a free trial ones.  I haven’t gotten around to sitting down with my design guy and redoing the buttons and the sales pitch for the free download yet.


Featurewise, it isn’t quite competitive with the downloadable Bingo Card Creator, to be honest.  A few of the power-user features, particularly design-focused things like picking fonts, are *shockingly* difficult to implement in a good way in a web application.  Others, like consistent columns and call lists, I just quite haven’t had time to integrate yet.


I was really impressed that I got the live preview of the bingo cards to work as well as it does.  Check it out — I am *very* proud of that work, although it is rough around some edge cases.  It took probably half of the development time of the site but I think getting users super-responsive feedback to their actions is worth every minute of it.


## AJAX Technical Detail


How does it work?  While users are typing words into their text box, Prototype periodically checks it for changes and, if there are any, serializes the contents of the form and calls an AJAX function on the server.  The server takes the contents of the form and saves it to a “scratch” record in the database, which is not otherwise visible to the user.  The return value from this function overwrites part of the calling web page, including replacing the previous preview image with a new image if the scratch value has changed (same url, new query parameter — this tricks browsers into always requesting the image anew rather than checking their cache).


The path to the image on the server is actually just more Rails code, which checks to see if the scratch record has changed since the last time it produced an image.  If not, Rails tells Nginx “give them the last image we wrote, straight from the disk”.  If yes, then Rails uses Prawn plus a boatload of custom formatting logic to create a PDF, then calls out to ImageMagick to turn that into a GIF and resize it, then writes that to the storage area on the disk and tells Nginx to serve it.  Total time per request: on order of 300 to 800 ms.  My back of the envelope math suggests that my server, with two Mongrels, can probably support about 20 teachers simultaneously editing cards as fast as their fingers can go… after that I need to get worried (or upgrade to a bigger slice, which I might do anyway).


## Still To Come


I still have to:

- rewrite my copy to address the existence of the web version
- get Bingo Card Creator 3.0 tested, in particular the features where it links to the website
- give the user workflow a graphical upgrade, because pretty buttons sell B2C software
- rewrite my page templates to push both the trial and the online service — I sense a lightbox coming up…
- improve usage stats collection (can be pushed after release)
- test integration with the purchasing funnel to make sure it works right
- give some spit-and-polish to some usability issues


I’d love if you have any comments on it.  Take it for a spin and  let me know.  This sneak-peak is not using the production database, which means when the sneak-peak ends **you’ll lose anything you did with it**.  In the unlikely event you want to use this for something important, make sure you save your cards locally.
