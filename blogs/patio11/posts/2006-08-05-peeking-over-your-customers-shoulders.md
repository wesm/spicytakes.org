---
title: "Peeking Over Your Customers' Shoulders"
date: 2006-08-05
url: https://www.kalzumeus.com/2006/08/05/peeking-over-your-customers-shoulders/
slug: peeking-over-your-customers-shoulders
word_count: 388
---


I’m going to assume there are multiple possible paths to get your your Buy Now button in your trial software.  Pop quiz: which one gets used most often?


Oh, you weren’t tracking that?  Well, it seems like its fairly useful information to you — after all, from your perspective thats the most important mouse click in your program there is.  And if you know that information, you can test the placement of the link — does a nag screen produce appreciable results?  How about an exit screen?  Do people click the button more when the menu item is highlighted in blue (*cough* yes *cough*)?  Is your idea to put a [tip-of-the-day to put another opportunity to buy](http://discuss.joelonsoftware.com/default.asp?biz.5.372471.10) a sound one (nice idea, Peter Muys)?  If your product is feature limited, what feature is the one that people can’t stand not having?


Yeah yeah yeah, nice to know but its excessively hard to implement, right?  You’re probably thinking you need to have some sort of shopping cart application and pass it a parameter and parse the output and and and…   No.  We’re computer programmers because we are too lazy to do things like that when there are **10 second solutions**.


Step #1: Append a dummy parameter to your static HTML page which you send folks too.  e.g. Instead of accessing www.bingocardcreator.com/purchasing.htm access www.bingocardcreator.com/purchasing.htm?source=trial&location=menubar.  (Did you know that your web server will happily take any number of parameters to a request for a static HTML file and promptly log and ignore them?  Yeah, who knew.)


Step #2:  Using your favorite Analytics software, take a gander at the “dynamic content” for your file of choice.  Under Google Analytics this is under Content Optimization -> Content Performance -> Dynamic Content.  For example, I can see instantly that roughly half of the hits on my purchasing.htm page come from referals from my application.  My application has 3 paths to get to the purchasing screen (nag screens on two disabled features and the Purchase Now button), and if I wanted I could segment on those.  Something to try for v1.04.


P.S. Keep in mind its generally poor web design to include lots of dynamic parameters, because they confuse search engine spiders.  But since GoogleBot isn’t spidering your *application*, you can go hog wild with referrals from there and it will never be the wiser.
