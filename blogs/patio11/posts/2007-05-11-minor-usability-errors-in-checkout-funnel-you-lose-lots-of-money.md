---
title: "Minor Usability Errors In Checkout Funnel = You Lose Lots Of Money"
date: 2007-05-11
url: https://www.kalzumeus.com/2007/05/12/minor-usability-errors-in-checkout-funnel-you-lose-lots-of-money/
slug: minor-usability-errors-in-checkout-funnel-you-lose-lots-of-money
word_count: 728
---


Recently I discovered that I have been inadvertently making it very difficult for customers to order CDs, which are a very popular item.  They’re so popular that I think a significant portion of my customers would walk away if they couldn’t get them.  Here is the percentage of orders I’ve had which requested a CD since I made the CD an easy and obvious item to get:


February (CDs offered prominently midmonth) : 6 / 17 = 35% (its over 50% if you count only the orders past when I started offering CDs prominently)


March: 2 / 30 = 6%


April: 4 / 26 = 15%


May: 3 / 12 = 25%


Now, granted, part of this is natural variation and small numbers throwing things for a loop.  Part of it in March was a bug in my webpage which made it flatly impossible to order CDs through the two most obvious links.  I expected the CD rate to recover to 50% or so after fixing that, but it has been fairly low in April/May, and I recently discovered the reason why.


The problem was the e-junkie cart.  Basically, to ship a CD you have to mark it as a Shipping item.  If you have a Shipping item in your cart, the cart interface changes.  [Try it out now on my website](http://www.bingocardcreator.com/purchasing.htm).


If you don’t have a shipping item in your cart, your cart looks like this:


You hit one of the two checkout buttons and you are instantly whisked to the checkout page in Paypal or Google Checkout.  Brilliant, you now have something approaching a 60% chance of giving me money (guesstimate from available analytics data).


If you do have a shipping item in your cart, you get


So you click on the checkout button and are instantly whisked to… **an error message**.


Thats not good news, but being a computer user you don’t actually read the error message.  Roughly half of you abandon the checkout instantly.  The other half of you input your zipcode again and slam on the checkout button.  Where you get whisked to **another error message**.


Yep folks, like the old public service announcement said, reading is fundamental.  You have to click update cart then click checkout.  Only 20% of the people who reach this stage of the game are capable of completing those two steps in order.  For those keeping track, thats 50% lost at the first error message times, then 80% of the remainder lost at the second error message, means a total of 10% of the people who wanted to buy CDs make it through The Cart Gauntlet.  Then its on to checkout where the slightly miffed survivors convert at a 60% rate, meaning **I lose NINETY FOUR PERCENT of the people who have expressed interest in buying a CD**.


Clearly, this is a suboptimal state of affairs for me.  Luckily, my shopping cart was created by the best guys in the business, [e-junkie](http://www.e-junkie.com).  I swapped a pair of mails with Robin detailing the problem and they’ll have a fix pushed out to all their carts in the world (hosted web apps: so nice) by the end of the weekend.  Other e-junkie users who sell to non-technical customers, I hope you enjoy your magically increased sales as much as I will.


So here’s the take-away lesson: you’ve got to sand down the rough edges in your checkout funnel or they’ll bleed you to death.


Many people might say “Wait a second, isn’t the cart itself a rough edge, since you go directly to the checkout button?”  Oddly enough, no.  I can substantiate that with conversion numbers — the page performs much better with the cart than with buttons taking folks directly to Google Checkout and Paypal.  My guess is that this is psychology — you get one choice to make “Download or CD?”, you make it, and after you’ve committed to that the virtual salesman gives you another minor little prompt “So, how do you intend to pay for it?” and we’re off to the races.  If, however, you offer a bewildering array of options at the start of the process (“Would you like to buy the downloadable version from Paypal for $24.95, the downloadable version from Google for $24.95, the CD version from Paypal for $29.95, or the CD version from Google for $29.95?”), customers can get decision paralysis.
