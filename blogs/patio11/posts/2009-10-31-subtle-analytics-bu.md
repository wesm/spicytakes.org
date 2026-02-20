---
title: "Tracking Down A Subtle Analytics Bug"
date: 2009-10-31
url: https://www.kalzumeus.com/2009/10/31/subtle-analytics-bu/
slug: subtle-analytics-bu
word_count: 1541
---


I have a confession to make: I often trust code that I thinks works.  For example, after I’ve got analytics code up and running, and verify to my satisfaction that it in fact increments the count of registrations by one when I sign up, I generally assume “OK, that is the last time I have to worry about that.”


This is, perhaps, a weakness.  For the last several months, for example, I’ve periodically checked in to Mixpanel or my A/Bingo stats and thought “Hmm, that is a lot less conversions than I expected over that time interval”, but I *knew* my conversion code worked and it wasn’t displaying zeroes, so I mentally pushed it out of mind.


Today, I was finally motivated into checking what was up when I reviewed the statistics for my recent [Halloween promotions](https://www.kalzumeus.com/2009/10/14/holiday-promotion/).  Portions of these did exceptionally well: for example, in the week before Halloween, I had [over 2,000 trial signups](http://www.bingocardcreator.com/stats/signups-per-day).  In the course of writing a blog post about this, I tried to figure out how many of those trial signups were caused by the Halloween promotion, and to do this I opened my statistics at Mixpanel.  ([Mixpanel](http://www.mixpanel.com) is an analytics service with a wonderful API.  I highly recommend them. They’re blameless for the bug I’m about to talk about.)


Mixpanel, however, reported that over the same week, I only had 375 people open the sign up form and some 180 of them actually sign up.  While it is quite common for multiple analytics sources to disagree about exact numbers, a discrepancy that large meant that there was probably a bug somewhere.


Having previously had some issues with my Mixpanel integration, the first place I looked was my log files, to see if I was actually calling the Mixpanel API.  Some light grepping suggested that I was, in about the frequencies I expected to.  Then I thought “Hmm, I wonder if the unique IDs I am passing with each visitor are, in fact, unique?”


A quick check on the command line suggested, no, I was in fact duplicating IDs.  By the scads.  This resulted in me pulling out the code which assigned Mixpanel IDs:


I was flummoxed, because the code appeared correct, if a little convoluted on first glance. The idea is to persist the Mixpanel ID for a given user — first, by stuffing it in their session cookie, and second, by stuffing it in Memcached so that if they bounce between multiple different machines I can still track them after they log in. If they don’t have an ID set anywhere, it gets randomized — that is the rand (10 ** 10) call.


Given that my user login code was correct (or there would be much, much more serious problems than analytics failing — people would be seeing my admin screens, bingo cards would bleed across accounts, cats and dogs would be friends, etc) and I trust Memcached not to have critical data-corruption bugs, the only place that made sense for introducing the error was the random statement. Which, of course, makes no sense at all — 10 digit random numbers should, by definition, not routinely collide. (There is the birthday paradox to worry about, I know, but the odds of that happening with only 15,000 accounts on the system were fairly slim and the odds of it causing the current issue were too low to measure.)


So I dropped into my Rails console and used it to inspect the memcached IDs, to see if I could find any patterns.


For those of you not fluent in Ruby, these are just some quick, basic operations on data sets. Ruby excels at them and the ability to do them in real time on the console is fantastic. (I don’t suggest doing them with truly massive data sets but when you count things in thousands, oh well, Slicehost gave me 8 cores for a reason.)


Anyhow, this exploration showed that the most common IDs were repeated literally hundreds of times each. However, it wasn’t a uniform distribution — instead, it looked like exponential decay, from the most repeated ID having 800 copies to a long tail of truly unique unique IDs.


As soon as I saw that pattern, I knew what had to be causing it: an srand bug. srand sets the random seed for your process. The random seed is used to generate what random number the next call to rand gives you. Two pieces of code which execute rand with the same random seed will always get the same random number. Since this is not desirable 99% of the time, if you execute rand before setting a seed through srand, srand is initialized to a string composed of the current time, process ID, and a sequence number. This virtually guarantees that you’ll get a unique random seed, and thus you get mostly unique streams of random numbers.


This narrowed down the possible causes of my bug quite precipitously: either there was a bug in Ruby’s srand (unlikely) or I was setting srand determinalistically somewhere. So I did a quick search through my code base and, yep, there is was:


This lovely bit of poorly thought out code is in the code which controls printing bingo cards. Each card has the words scrambled, but trial users (whose options[:good_randomize] gets set to false) don’t get truly scrambled cards. They get a sequence of cards which is always the same, capped at 15 cards, so that no many how many times they try to print they can never create more than 15 unique cards. This encourages them to purchase the software, which removes that limitation.


Since that code snippet is executed for every print job, every user either sees a properly random random seed or the fixed random seed. However, after the code finishes, the random seed lives on in the Mongrel process. This was the ultimate cause of my bug.


Imagine a sequence of events like so:


1) Trial user Bob prints out a single bingo card, which sets the random seed to the deterministic value and uses 25 calls to rand.


2) Jane comes to the site for the first time and has a random number assigned to her. It is guaranteed to be the 26th element (call it R26) in the sequence from a fresh call from the deterministic random seed.


3) Bob prints out another bingo card, which sets the random seed to the deterministic value and uses 25 calls to rand.


4) Frederick comes to the site for the first time and has a random number assigned to her. It is guaranteed to be the 26th element (call it R26) in the sequence from a fresh call from the deterministic random seed.


Thus, Jane and Frederick end up getting the same “random” ID assigned to them. Thus, when I report that both Jane and Frederick signed up for the free trial, Mixpanel decides “Patrick’s conversion code is reporting the same event twice, OK, no biggie: I’m going to discard that second funnel event.”


In addition, since both Jane and Frederick shared the same ID for their A/Bingo identity, both of them would always see the same A/B test alternatives. That wouldn’t be too bad, except they also were counted as the same person for conversion purposes, so if Jane converted Frederick’s conversion wouldn’t be counted.


In actual practice, many users still end up getting random IDs, since any particular Mongrel’s random seed got unborked when a paying user printed out a bingo card… at least until the next trial user printed out a bingo card on that Mongrel. (Random seeds are maintained at the process level in Ruby, and each Mongrel is a separate process.)


Anyhow, long story short:


1) No users except me were adversely affected by this bug — it only affected analytics and A/B test results.


2) Other folks using my public Mixpanel APIs and A/Bingo A/B testing code were unaffected — it was only the interaction of this code with the srand(12345678) code that caused the issue.


3) Two months of my analytics and A/B test data is corrupted.


I’m not sure it matters to the bottom line of the A/B test results, which are *shockingly* robust against programming errors like this: as long as the source of error doesn’t correlate with your A/B choices, the errors will be evenly distributed across both alternatives, so it just washes out. For example, it is likely upwards of 60% of data for the A/B tests was thrown out as “duplicate” erroneously, but since the “duplicates” were evenly distributed across A and B this borks the measured totals and percentages but not the measured significances. That’s some comfort to me, cold as it is.


The moral of the story: **don’t use srand(constant) anywhere in your production code**, even if it is the easiest way to get what you want, because sooner or later you will use rand() in some unrelated code called by the same process and now you have extraordinarily subtle bugs caused by reuse of random numbers. If you absolutely must use srand(constant), call srand() on a per-request basis to clear out anything which may be lurking around from previous requests. (For example, in a application-wide before filter.)
