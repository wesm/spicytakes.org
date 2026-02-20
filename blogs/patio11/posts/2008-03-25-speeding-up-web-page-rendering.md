---
title: "Speeding Up Web Page Rendering"
date: 2008-03-25
url: https://www.kalzumeus.com/2008/03/25/speeding-up-web-page-rendering/
slug: speeding-up-web-page-rendering
word_count: 620
---


I have the good fortune to be on a fast, fast, fast Japanese connection and as a result don’t typically wait too long to view webpages.  This makes me forget sometimes that the rest of the world doesn’t get nigh-instantaneous page loads, which means I don’t often design with this factor in mind.  However, somebody pointed out that the new sidebar buttons were loading last for them, and as my front page can potentially take 4 seconds to load (longer than a significant portion of visitors stay!) I didn’t want that.


Why is a bit of a long story.  First off, the sidebar is literally the last thing in the HTML body element (with the exception of various bits of Javascript).  This is to push up the main content area in the document, because search engines treat stuff near the top as more important and I want pages to rank for their own content not the content of pages they happen to link to on the sidebar.  This means that, if you parse the webpage starting at the top and going down, you come across those IMG tags pretty much dead last after everything else on the page.


Now, how do browsers download assets (images, Javascript, CSS, and whatnot)?  Basically, there is a FIFO (first-in, first-out) queue maintained per host name.  For example, if I have the web page reference 10 images on [www.bingocardcreator.com](http://www.bingocardcreator.com/), then those are listed from first occuring to last occuring in the queue.  The browser then, following HTTP specifications, starts downloading two at a time *per queue*.  This means that if you have, say, 25 objects to grab from your own domain and 1 offsite Javascript the offsite Javascript will start downloading about as soon as its discovered while the last object from your domain waits in line.


So that is the technical explanation.  What was happening was my front page loads 2 fairly sizeable screenshots totaling 200kb of the total 350kb required to load the page, and as these are both ABOVE the sidebar when you’re reading HTML linearly, they were blocking the download of the buttons.  That is certifiably ungood, *particularly* as one of the screenshots isn’t even visible when you open the page (it is far below the fold, most people won’t even see it!)


However, since the queue is maintained *per hostname*, if I could only host on a hostname other than [www.bingocardcreator.com](http://www.bingocardcreator.com/), I could have things download in parallel.  Happily, my webserver (Nginx) makes it really simple to set up extra names like, say, images1.kalzumeus.com which are essentially the same as the main domain in every way except they are, well, named differently.  Thus tricking your browser to download from them in parallel.  I set up 4 domains this way and used that to do a bit of manual queue optimization to ensure that the images with the highest payoff (*big beautiful buttons!*) load fastest.


And to think I was wondering why so few folks tracked in CrazyEgg were hitting the images compared to before.  Now I know — they were waiting so long they had already found a text link before engaging the image.  The results are visibly different even on my monster Japanese connection.  (Its like the Godzilla of latency… in a good way?)


Rails offers a [way to do this automatically](http://spattendesign.com/2007/10/24/setting-up-multiple-asset-hosts-in-rails), but I wouldn’t recommend it if you have only a few pages to hand optimize.  The reason is simple — randomizing access to domains results in good average case load orders but if you can hand-optimize things you blow it out of the water.  (For example, there is about a 40% chance that the large image would block one of my conversion buttons with random host names.)
