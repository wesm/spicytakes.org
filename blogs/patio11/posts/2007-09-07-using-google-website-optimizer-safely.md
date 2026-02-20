---
title: "Using Google Website Optimizer Safely"
date: 2007-09-07
url: https://www.kalzumeus.com/2007/09/07/using-google-website-optimizer-safely/
slug: using-google-website-optimizer-safely
word_count: 417
---


In my recent post about [Paypal’s new icons](http://microisvjournal.wordpress.com/2007/09/07/new-paypal-buttons/) I mentioned that I was going to use CrazyEgg to check whether the icons were more loved or not than the old ones, and I am, but I decided to go the extra mile and use Google’s Website Optimizer to do a split test.  A split test is when you randomly send half of all prospects to one version of a page and half to another to determine, in a rigorously scientific and statistical manner, which of two alternatives is better.  They’re typically a pain in the hindquarters to accomplish, but this one wasn’t so bad, thanks mainly to a new feature that Website Optimizer includes.


Previously, you had to markup the bejeezus out of your web pages to Optimize them, which harms some user experience (if the bracketed portion of the page loaded slowly, congrats, you lose) and took far too long.  Now, while thats still an option for multivariate tests, Google has a simpler option — make two pages, put two bits of Javascript in the first (front and end of the file) and one in the second, and then put a tracking code on your conversion page, and Google takes care of the rest via transparently redirecting folks who hit the first page into the second with 50% probability.


They recommend that you leave the second page up indefinitely, because folks could conceivably link or bookmark it.  I first thought that was good advice.  Then I realized **DANGER WILL ROBINSON** having two pages on your site with 95% similar HTML is an excellent way to get smacked down by the duplicate content penalty, and that would hurt me oh-so-much more than getting a modest bump in conversions from rigorous testing.


Happily, there was a simple one line fix to my robots.txt file that I could make to ward off any possibility of that:


> #Somewhere above here we have the “User-agent: *” or “User-agent: Googlebot” line


> Disallow: /name-of-my-file.htm


After I’m done with the test, I’m going to use .htaccess to 302 redirect the alternate page to the main page rather than leaving the alternate up forever, which will keep any links or bookmarks good without forcing me to keep an outdated page around and consistent with the rest of my site for eternity.  Why do more work?


Anyhow, if you want to see the site, take a gander at my [purchasing page](http://www.bingocardcreator.com/purchasing.htm) which has a fifty-fifty shot of actually showing you the [old purchasing page](http://www.bingocardcreator.com/purchasing-alternate.htm).
