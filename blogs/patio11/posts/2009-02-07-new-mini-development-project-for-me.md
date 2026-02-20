---
title: "New Mini-Development Project For Me"
date: 2009-02-07
url: https://www.kalzumeus.com/2009/02/07/new-mini-development-project-for-me/
slug: new-mini-development-project-for-me
word_count: 574
---


I have a deep, abiding affection for [e-junkie](http://www.e-junkie.com), which is my payment processor of choice.  So much so that I’ve been called their Local Sales Rep on the Business of Software forums.  Probably true — have I mentioned they’re the best $5 a month you will EVER spend in your life?  Sorry, had to do some shillin’ like a villain to make up for what I’m about to say.


I’m thinking of not using their shopping cart anymore.  Not because it isn’t an amazing piece of technology which manages to work for thousands of people without writing code, because it is all of that and more.  The lift I got in conversions from using it has made me thousands, which for about 5 minutes of integration work means the hourly effective wage is sweet indeed.  Its just that my web programming abilities are improving these days, and I’m starting to chafe at a few of the necessary restrictions from using a third party solution.


My big issues:


1)  Forcing people who buy a CD to put in their zip code twice — once in the cart, once at the actual checkout screen.  I’m working on the assumption that that probably kills CD conversions, and I’m not sure those conversions come back


2)  It is slow.  Clicking on the cart gives you a loading message for two or three seconds.  I still think it beats the pants off of a pageload when updating a shopping cart, I just want the perceived speed to be “bugs in my teeth fast”.  (This is where people ask me “Well, why do you need a shopping cart at all when you can just have a Buy Now button?” and where I say “I’ve tested both alternatives and the cart makes me oodles of money by simplifying the customer experience.”)


I was partially inspired to do this by my buddy Yakob at [Mixed In Key](http://www.mixedinkey.com), who a) has something really cool coming down the pipe which if you are reading this blog will interest you intensely and b) has a really sweet shopping cart implementation.  Try it, you’ll like it.  That’s what I want mine to work like.


I think I can repurpose some of the Widget Factory Javascript code to achieve it fairly easily.  The actual transaction will still be handled by e-junkie, but I want the cart constructed locally.  If I can do it fairly cleanly, I’ll open source this so that anybody else can apply it to their sites — otherwise, I’ll just do the usual kludging and split test it against the genuine e-junkie cart on mine.  I’m thinking the lift in conversions is going to be sizeable enough to justify a few hours of fighting with Javascript (once).


Sidenote: My dashboard informs me that I might hit $3,000 in sales this month.  Whee for new records!  Recession, what recession, [73%](http://www.bingocardcreator.com/stats/sales-by-month) year over year growth.  (Watch me jinx myself.)


What’s doing it?  Same old same old:

- AdWords doing well as it always does near secularized holidays ([Valentine’s Day bingo](http://www.bingocardcreator.com/bingo-cards/holidays/valentines-day) is always hot, and while I’m not winning that SERP the people who are thankfully slap AdWords all over the place)
- organic SEO efforts on website paying off (~1,200 visitors from Google on average weekday these days)
- version 2.51 converts pretty decently (subtle changes, big difference in effects, tell you about it later)
- a few tweaks to the website are paying nice dividends
