---
title: "Massive Frontal PR is incompatible with Ship Early and Often"
date: 2005-11-02
url: https://www.joelonsoftware.com/2005/11/02/massive-frontal-pr-is-incompatible-with-ship-early-and-often/
word_count: 595
---


Microsoft’s new (beta!) portal page, [live.com](http://www.live.com), doesn’t work in Firefox, and doesn’t work too great in IE either. The first thing I used it for was to search for “firefox market share.”


Like every search engine, you get a list of search results. I clicked on the first one, read the article, and then clicked “back” to find the next result.


Oops! What happened to the search results?


Live.com uses dynamic HTML in a broken way such that clicking “back” takes you all the way back to the home page, not the search results. Which makes it pretty unusable as a search engine. I noticed this right away, because just yesterday we spent a lot of time thinking about this very issue in our own product, FogBugz.


I played around with the RSS subscription feature for a minute or two. It crashed IE. Oh well. I don’t remember Microsoft ever shipping anything quite this half-baked. Maybe that means that they’re moving firmly into the “agile” camp: ship early and often.


Does ship-early-and-often really work for a huge company doing massive PR pushes that’s going to get millions of people checking out their early release?


I don’t think it does. This is a classic example of what I’ve always called the [Marimba Phenomenon](https://www.joelonsoftware.com/articles/VC.html). The Marimba Phenomenon is what happens when you spend more on PR and marketing than on development. “Result: everybody checks out your code, and it’s not good yet. These people will be permanently convinced that your code is simple and inadequate, even if you improve it drastically later.”


The Marimba Phenomenon is very hard to avoid when you spend too much money trying to launch a new product. It’s easy to spend on marketing and PR, since that just takes cash, but it’s hard to spend on software development, because that actually takes time and talent. So cash-rich companies, whether Microsoft or VC-backed startups, run the risk of launching to a bigger audience than they really should have, getting millions of people to be thoroughly unimpressed by version 1.0 and never bothering to come back again to see if 2.0 might have gotten it right.


By contrast, small companies that don’t have great marketing budgets are in a great position to launch early and often. In the first few weeks after we launched our remote assistance product, [Fog Creek Copilot](https://www.copilot.com), we found some pretty serious bugs handling proxy servers that affected about 5% of our customers. But we only had a few customers every day, since the service was new and didn’t have a superbowl ad. We fixed the bugs in a matter of days and now there are only a tiny number of people wandering around who had a bad experience with Copilot. And now as the service builds in popularity we’ve rolled out dozens of new builds and fixed hundreds of bugs and even added some major cool features, like automatic screen resizing, which makes it easy to control a computer with a large monitor from a computer with a smaller monitor.


By the way, Firefox is probably around 10%.


[Jason Lefkowitz](http://www.jasonlefkowitz.net/blog1archive/2005/11/microsoft_live.html): “Live.com is the perfect example: as far as I can tell, it’s just a customizable portal page. We had those in 1998 and they sucked then. Seven years later, they haven’t gotten any better.”


PS. I don’t get the difference between start.com and live.com, two remarkably similar Microsoft websites. Start.com already works in Firefox, launches search results in a new browser window, which is awkward but not as bad as what live.com does, and seems to be more polished.
