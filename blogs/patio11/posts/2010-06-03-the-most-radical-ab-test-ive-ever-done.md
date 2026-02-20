---
title: "The Most Radical A/B Test I've Ever Done"
date: 2010-06-03
url: https://www.kalzumeus.com/2010/06/04/the-most-radical-ab-test-ive-ever-done/
slug: the-most-radical-ab-test-ive-ever-done
word_count: 1414
---


About four years ago, I started offering Bingo Card Creator for purchase.  Today, I stopped offering it.


That isn’t true, strictly speaking.  The original version of Bingo Card Creator was a downloadable Java application.  It has gone through a series of revisions over the years, but is still there in all its Swing-y glory.  Last year, I released an online version of Bingo Card Creator, which is made through Rails and AJAX.


My personal feeling (backed by years of answering support emails) is that my customers do not understand the difference between downloadable applications and web applications, so I sold Bingo Card Creator without regard to the distinction.  Everyone, regardless of which they are using, goes to the same purchasing page, pays the same price, and is entitled to use either (or both) at their discretion.  It is also sold as a one-time purchase, which is highly unusual for web applications.  This is largely because I was afraid of rocking the boat last summer.


The last year has taught me quite a bit about the difference between web applications and downloadable applications.  To whit: [don’t write desktop apps](https://www.kalzumeus.com/2009/09/05/desktop-aps-versus-web-apps/).  The support burden is worse, the conversion rates are lower, the time through the experimental loop is higher, and they retard experimentation in a million and one ways.


Roughly 78% of my sales come from customers who have an account on the online version of the software.  I have tried slicing the numbers a dozen ways (because tracking downloads to purchases is an inexact science in the extreme), and I can’t come up with any explanation other than “The downloadable version of the software is responsible for a bare fraction of your sales.”  I’d totally believe that, too: while the original version of the web application was rough and unpolished, after a year of work it now clocks the downloadable version in almost every respect.


I get literally ten support emails about the downloadable application for every one I get about the web application, and one of the first things I suggest to customers is “Try using the web version, it will magically fix that.”

- I’m getting some funky Java runtime error.  *Try using the web application.*
- I can’t install things on this computer because of the school’s policies.  *Try using the web application.*
- How do I copy the files to my niece’s computer?  By the way it is a Mac and I use a Yahoo.  *Try using the web application.*


However, I still get thousands of downloads a month… and they’re almost all getting a second-best experience and probably costing me money.


## Thus The Experiment


I just pushed live an A/B test which was complex, but not difficult.  Testers in group A get the same experience they got yesterday, testers in group B get a parallel version of my website in which the downloadable version never existed.  Essentially, I’m **A/B testing dropping a profitable product** which has a modest bit of traction and thousands of paying customers.


This is rather substantially more work than typical “Tweak the button” A/B tests: it means that I had to make significant sitewide changes in copy, buttons, calls to action, ordering flow, page architecture, support/FAQ pages, etc etc.  I gradually moved towards this for several months on the day job, refactoring things so that I could eventually make this change in a less painful fashion (i.e. without touching virtually the entire site).  Even with that groundwork laid, when I “flipped the switch”  just now it required changing twenty files.


## Doing This Without Annoying Customers


I’m not too concerned about the economic impact of this change: the A/B test is mostly to show me whether it is modestly positive or extraordinarily positive.  What has kept me from doing it for the last six months is the worry that it would inconvenience customers who already use the downloadable version.  As a result, I took some precautions:


**The downloadable version isn’t strictly speaking EOLed**.  I’ll still happily support existing customers, and will keep it around in case folks want to download it again.  (I don’t plan on releasing any more versions of it, though.  In addition to being written in Java, a language I have no desire to use in a professional capacity anymore, the program is a huge mass of technical debt.  The features I’d most keenly like to add would require close to a whole rewrite of the most complex part of the program… and wouldn’t generate anywhere near an uptick in conversion large enough to make that a worthwhile use of my time, compared to improving the website, web version, or working on other products like [Appointment Reminder](http://www.appointmentreminder.org).


I extended [A/Bingo](http://www.bingocardcreator.com/abingo) (my A/B testing framework) to give a way to override the A/B test choices for individual users.  I then used this capability to intentionally exclude from the A/B test (i.e. show the original site and not count) folks who hit a variety of heuristics suggesting that they probably already used the downloadable version.  One obvious one is that they’re accessing the site from the downloadable version.  There is also a prominent link in the FAQ explaining where it went, and clicking a button there will show it.  I also have a URL I can send folks to via email to accomplish the same thing, which was built with customer support in mind.


I also scheduled this test to start during the dog days of summer.  Seasonally, my sales always massively crater during the summer, which makes it a great time to spring big changes (like, e.g., new web applications).  Most of my customers won’t be using the software again until August, and that gives me a couple of months to get any hinks out of the system prior to them being seen by the majority of my user base.


## My Big, Audacious Goal For This Test


I get about three (web) signups for every two downloads currently, and signups convert about twice as well as downloads do.  (Checking my math, that would imply a 3:1 ratio of sales, which is roughly what I see.)  If I was able to convert substantially all downloads to signups, I would expect to see sales increase by about 25%.


There are a couple of follow-on effects that would have:

- I think offering two choices probably confuses customers and decreases the total conversion rate.  Eliminating one might help.
- Consolidating offerings means that work to improve conversion rates automatically helps all prospects, rather than just 60%.


## Magic Synergy Of Conversion Optimization And AdWords


Large systemic increases in conversion rates let me walk up AdWords bids.  For example, [I use Conversion Optimizer](http://www.google.com/adwords/conversionoptimizer/bingocard.html).  Essentially, rather than bidding on a cost per click basis I tell Google how much I’m willing to pay for a signup or trial download.  I tell them 40 cents, with the intention of them actually getting the average at around 30 cents, which implies (given my conversion from trials/signups to purchase) that I pay somewhere around $12 to $15 for each $30 sale.  Working back from 30 cents through my landing page conversion rate, it turns out I pay about 6 cents per click.


Now, assuming my landing page conversion is relatively constant but my trial to sale conversion goes up by 25%, instead of paying $12 to $15 a sale I’d be paying $9.60 to $12 a sale.  I could just pocket the extra money, but rather than doing that, I’m probably going to tell Google “Alright, new deal: I’ll pay you up to 60 cents a trial”, actually end up paying about 40 cents, and end up paying about 8 cents per click.  The difference between 6 and 8 will convince Google to show my ads more often than those of some competitors, increasing the number of trials I get per month out of them.  (And, not coincidentally, my AdWords bill.  Darn, that is a bloody brilliant business model, where they extract rent every time I do hard work.  Oh well, I still get money, too.)


We’ll see if this works or not.  As always, I’ll be posting about it on my blog.  I’m highly interested in both the numerical results of the A/B test as well as whether this turns out being a win-win for my customers and myself or whether it will cause confusion at the margin.  I’m hoping not, but can’t allow myself to stay married to all old decisions just out of a desire to be consistent.
