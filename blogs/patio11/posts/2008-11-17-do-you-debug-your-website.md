---
title: "Do You Debug Your Website?"
date: 2008-11-17
url: https://www.kalzumeus.com/2008/11/17/do-you-debug-your-website/
slug: do-you-debug-your-website
word_count: 1600
---


I can’t say that the bug this post is about is my worst bug ever.  Or even my most embarassing bug ever.  But it is certainly my most costly bug ever.  But first, a picture.  You can click it to see the full-sized version.


The above graph shows two years and change of monthly visitor counts to my business.  There are a bunch of milestones I could have put up there — the new versions of my software, the key events in my market’s annual cycle, the redesign of my website, the time I quadrupled my advertising budget.  And they all pale in comparison to *squashing one stupid little bug*.


**What Could Possibly Have Done That?**


Well, like many bugs, the impact of this one rose in direct proportion to how clever you are.  My business website runs on a custom-designed CSS which cranks out [free printable bingo cards](http://www.bingocardcreator.com/bingo-cards).  The home page, shopping cart, main level navigation, all of these things are valuable towers which sit on a gigantic foundation of free content.  That content attracts me links, traffic, and searchers.  The [bright idea](http://kalzumeus.com/2007/10/21/developing-linkbait-for-a-non-technical-audience/) to make the production of this content scale is probably the single biggest thing I’ve ever done to grow my business.


And scale it does.  I pay a terrifically talented freelancer to write the actual word lists that become the bingo cards, and provide a little bit of color commentary.  I feed her input into the CMS, and *bam* web page, downloadable PDF, and GIF are created.  Now multiply this times a couple hundred, for very little additional work on my part.


**The Best Laid Plans of Mice and Men**


One design decision I made when building this automated marketing machine was to give it a time-based element: one bingo card got featured a day.  Originally this was largely because I had the site separate from my main site and wanted to call it [Daily Bingo Cards](http://www.dailybingocards.com).  I figured, hey, if a new card pops up to the “front” page every day then it will always be fresh, and that makes it stickier for folks.  (And, as it turns out, I do have a handful of folks who a year later are still loading the page several times a week to see what is new.)


However, I had (totally unfounded) performance worries about Rails when I wrote this application.  I thought hitting the database for every pageview was needlessly taxing on my server (bzz, I only get a few thousand a day, why the heck would the server complain?)  So I decided to turn on caching.


Caching is a wonderful tool.  You can use it to solve just about any performance problem.  It solves it by replacing the problem with a cache expiration problem.  (No performance problem?  Oh, you get to deal with cache expiration anyway, don’t worry.)


**How Hard Can It Be?**


Now, if you want to refresh your content on your website once a day, and you’re not really particular when you do it, caching should be dead easy: purge the cache once a day.  Which I did.  Sort of.


You see, Rails stores cached pages in the same directory your static HTML is being served out of, as static HTML.  Your web server treats the cached pages as it would any other web page if they exist, and just slurps them right out of the directory and spits them out at whoever is requesting that page.  This is blazingly, bugs-in-your-teeth fast.


And to clear the cache?  Simple — delete the HTML file and it is like it never existed.  Your web server, seeing no file matching the user’s request, will fallback to calling Rails to see what to do with the request, and after Rails does its magic there might be a new HTML file deposited into that directory.


And how to delete a file once a day?  Stick task in chrontab… done.


**Your Testing Protocol Leaves Something To Be Desired**


Now normally a line which is, roughly speaking, the complexity of *rm -rf /some/file/name/goes/here* is pretty hard to screw up.  But knowing well my pechant for screwups I tested those lines before I wrote them into the crontab.  As root (do you see where this is going?)  And they worked swimmingly.


Of course, when I wrote them into the crontab, I did not set them to execute as Root.  No, I set them to execute as the user that I thought would be dropping the files — clearly the web server, right?  (WRONG.  The web server proxies requests to Rails, but Rails operates under another user to write the cached html.  I knew that on an intellectual level, but it did not occur to me one fateful evening when writing that cron file.)


**Compounding Errors**


So, as a result, large portions of my website were not getting refreshed when I thought they were.  As a result, instead of a dynamic bingo card publishing empire, with constantly refreshed content that was added to, content on the website was fixed at first generation and then went stale.


Had it stayed stale, I would have eventually figured things out.  But no — I was developing the site, occasionally, and every time I deployed a new version of it, one of the deployment steps had the side effect of nuking the cache directory.  And since the only reason I would be trolling on my own bingo cards pages was to see that my changes were taking effect, I never saw the bug.


Meanwhile, between bursts of development activity, the page would look like an unattended ghost town for weeks or months at a time.


**Diagnosing The Error, or, Reality Bites Your Hindquarters**


Periodically I check what bingo cards my users find most appealing, both for curiosity’s sake and to guide development of new content.  Typically this is largely seasonal in nature — in November, for example, I can tell you without looking that [bingo cards for Thanksgiving](http://www.bingocardcreator.com/bingo-cards/holidays/thanksgiving) are going to have a total lock on the most popular crown.  But sometimes I’ll notice other patterns — a church sends my site out in their weekly flier and Bible Bingo gets popular for a week, some school has a unit on Chaucer and suddenly I see a surge in searches about the Canterbury Tales, and the like.


And then sometimes you see things that can’t be explained.  Insects being on the top 10 list for two months.  But you ignore it — maybe some people like bugs.  Cat Breeds for two weeks?  Maybe some people like cats.  But the one that finally clued me in was The Moon.  Because either NASA camp was playing Moon bingo every single day in July or something was up.


The Game Is Afoot


So I checked the database to see what card was scheduled for that day, because the card that gets top billing should typically be at or near the top of the most popular list.  And the database dutifully reported: none.  Which is impossible — had I run out of cards?  I thought I would still have about 100 in reserver.  I checked the database and saw, hmm, closer to 200.  Meaning either I was off on my mental count or about 100 had not been assigned.


One quick Ruby script later, iterating through all the days in summer, and I realized that only 6 days in summer had seen a new card assigned.  The error log showed nothing out of the ordinary for the other days.  As a matter of fact, it showed… *nothing* for them.  It was like the website wasn’t getting generated at all… or if it was, it was being served 100% out of cache.


*Shoot.*


Five minutes later I found and fixed the bug.  I was so mad I nearly posted a note about it here, but figured no one would care.  Had I known at the time how bad the impact was, I would have had apoplexy.


**Fast Forward Three Months**


If you know what happened, this seems like a pretty teeny bug conceptually.  Google sure didn’t see it that way — this bug made a live, growing website look largely dead to the world, and Google accordingly sent most of their searchers to get their bingo cards elsewhere.  (Ever wondered if Google values “fresh” web content?  This is my most convincing experience that says the answer is YES, although there are a couple of reasons why the pages are better with the daily updates happening which go a bit deeper than “they smell fresh that way”, which are out of the scope of this post.)  After the website was restored to vibrant life, Google opened the long-tail floodgates.


And the difference?  I’ve more than doubled most types of traffic, both search related and otherwise.  (Funny, while no user thought this was important enough to email about — and would you email if a favorite website went dead for a while during the summer?  — many sure thought it important enough when it was fixed to take notice.)  There are a few confounding factors in there (increased advertising budget, seasonal fluctuations, etc) but nothing accomodates for anything like the huge run-up you see in the graph.  My [sales graph](http://www.bingocardcreator.com/stats/sales-by-month) also shows a bit of a bump, to put it mildly.


**Word to the wise**


1)  Test your website with the same diligence you test your application.  Or, in my case, improved diligence.


2)  Pay attention to your website.  Even the boring bits.  *Especially* the boring bits that make you money.


3)  Never send a commited Windows programmer to do a Unix sysadmin’s job.
