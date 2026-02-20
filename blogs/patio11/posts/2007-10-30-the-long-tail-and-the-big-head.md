---
title: "The Long Tail and the Big Head"
date: 2007-10-30
url: https://www.kalzumeus.com/2007/10/30/the-long-tail-and-the-big-head/
slug: the-long-tail-and-the-big-head
word_count: 180
---


I just implemented the popular bingo cards feature on Daily Bingo Cards.  There are about a hundred cards on there, 30 of them just uploaded five minutes ago.  In two weeks, with very little promotion on my part, that has generated about 300 downloads.  If you want to see the distribution of how many of those are due to the top five pages and how many are not, why not [mosey on over](http://www.dailybingocards.com/popular).


Fair warning: At the moment, because my caching logic is apparently broken, that page is regenerated for every request.  Since doing that requires it to iterate over hundreds of objects in Ruby, it is *slow*.  (It about five hundredths of a second to grab the data from the DB,  a second to chug the math, and another five hundredths of a second to render the page.  Yeah, I know, I know, fix the cache or do the math at the DB, but I’m lazy and its late.)  You won’t notice unless you have the misfortune to hit it when several other people are hitting the site, thankfully.
