---
title: "Bingo Cards On Rails"
date: 2007-09-29
url: https://www.kalzumeus.com/2007/09/29/bingo-cards-on-rails/
slug: bingo-cards-on-rails
word_count: 699
---


No, despite what you might think, I haven’t decided to make Bingo Card Creator into a web application.


I was thinking about the full length of my conversion funnel today — from the very second someone gets on my webpage, to the instant they’ve clicked the “Send Patrick money!” button at Paypal or Google.  I was thinking “Is there any step in this process which could be easier or more streamlined?”  And of course there was — there always is.


The most prominent feature of my home page is a screenshot of [Bingo Card Creator](http://www.bingocardcreator.com), which is dead center and dominates the page.  I know that screenshot captures viewers’ attention instantly, because a) when I made the icons prettier on it I started selling a lot more and b) [CrazyEgg](http://www.crazyegg.com) tells me that something like a quarter of the people who so much as glance at the page click on it.  When they click on it, the screenshot expands in a [Lightbox](http://microisvjournal.wordpress.com/2007/04/14/lightbox-quick-pretty-screenshot-previews/) effect.


**What I would like to happen**: The visitor should, at this point, say “Wow, that is cool.  I want to try that.”  Then they click on the Free Trial button on the right, download the free trial, install the free trial, play around for a little while, click on Purchase Now, and come pay me money.


**What really happens**:  Exactly that, some of the time.


**What else happens**:  The visitor, not too computer-savvy and left without direction, just closes the browser, hits the back button, or ambles on to read more from my website.  Not that I mind reading, you understand, but I want to encourage folks who are ready to do more than read to skip the reading and proceed straight to the trial.


So, I hit upon an idea — put the whole process on rails (in the non-Ruby sense of the word).  I know what I want the customers to do, so why not tell them?  Plus, the screenshot as it is is busy — it isn’t exactly clear what message I’m sending, other than “This program exists, and look, it has pretty buttons”.  (Do **not** discount the effect of pretty buttons!  Doubled my sales!)  In particular, the bottom of the screenshot (where I put advise for new users) is offputting: its a wall of text and, as we all know, nobody reads on the Internet.


So here’s what I changed about the screenshot (only after clicking to view the screenshot, mind you).  (*WordPress may cut these off — click for full-sized.*)


became


You’ll note the second version gets rid of the ugly Wall-O’-Text and replaces it with a nice, hopefully readable instruction on what the person probably wants to do. I used the blue for the Download Free Trial text to mentally prepare them that the Download Free Trial button is blue, without having to say so (I tried, but it started to feel cramped).


**So let’s test it:**


1)  Create the two images.  D’uh.


2)  Create two versions of index.htm, one telling Lightbox to use image #1 and one telling it to use image #2.


3)  Upload them both (second one is [index-alternate.htm](http://www.bingocardcreator.com/index-alternate.htm)), check for errors.


4)  **IMPORTANT**: Ban index-alternate.htm in robots.txt to prevent Google from smacking me with the Duplicate Content penalty.


5)  Go to [Website Optimizer](http://microisvjournal.wordpress.com/2007/09/07/using-google-website-optimizer-safely/), get Javascript, insert, upload again.


6)  Identify conversion page.  Ideally, I would like a conversion to be actually downloading the trial.  Unfortunately, the trial download links go to an .exe and a .zip, and so I can’t exactly insert the conversion Javascript in them (for reasons beyond my ken, Website Optimizer won’t let you piggyback on Analytics’ use of a Javascript call to record clicks on non-html pages).  So, I punted and instead inserted it into the Free Trial page, because everyone downloading a trial needs to visit there and if I get 10% increase in the number of visitors there that is a good thing even if they don’t all necessarily grab the trial.


7)  Blast 5,000 4,200 visitors a week past my home page and see which one wins out.  (Edit: my original traffic estimate for September was off, so I updated it.)


8)  Do it again, and *again*, and ***again***.
