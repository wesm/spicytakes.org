---
title: "Introducing A/Bingo: Rails Split Testing"
date: 2009-08-15
url: https://www.kalzumeus.com/2009/08/15/introducing-abingo-rails-split-testing/
slug: introducing-abingo-rails-split-testing
word_count: 331
---


Regular readers of this blog know I’m a bit obsessive about testing and measuring small, iterative improvements to my website.  Previously I used [Google Website Optimizer](http://www.google.com/websiteoptimizer) but I found it had some annoying limitations.  In particular, it was too much work to start tests, too much work to code tests, and too much work to maintain expired URLs after tests were over.


So I went away to the code salt mines for the last week, and coded my own A/B testing framework in Ruby on Rails.  It is called [A/Bingo](http://www.bingocardcreator.com/abingo/) .  (The name sort of popped into my head and wouldn’t leave.  It is a pun, it relates to my business and personal brand, and it gives the impression of Hitting the Target that successful testing should give you.  My designer took that and ran with it for the logo.  I’m very impressed with the results.


A/Bingo is, without question, the most technically impressive code I’ve ever written.

- Setting up a test takes one line of code.  It is so easy you’ll find yourself doing it automatically when writing copy or making new features.
- It tracks absolutely any event as a conversion, in one line of code.
- It does statistical significance testing for you, producing human-readable output which tells you exactly how confident you can be that the test results are accurate.
- It is fast.  No, it is ***fast***.  Like, “A/Bingo could handle being linked from the front page of a social news site.  Heck, it could be *used on* the front page of many social news sites.”


If you want to read any more about it, I encourage you to take a look at [the website](http://www.bingocardcreator.com/abingo/).  A/Bingo is already powering all the Bingo Card Creator A/B tests.  I expect that the ease of use and copious features will mean I run a lot more tests.  I’ll continue sharing what I learn through them.


P.S. Incidentally, I scored a [16.9% improvement](http://www.bingocardcreator.com/articles/tracking-with-mixpanel.htm#results) to funnel completion thanks to [Mixpanel](http://www.mixpanel.com).
