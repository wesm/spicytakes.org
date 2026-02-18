---
title: "Safari Content Blocker, Before and After"
date: 2015-07-08
url: https://daringfireball.net/2015/07/safari_content_blocker_imore
slug: safari_content_blocker_imore
word_count: 452
---


[Dean Murphy wrote an iOS 9 Safari Content Blocker](http://murphyapps.co/blog/2015/6/24/an-hour-with-safari-content-blocker-in-ios-9), and tested it against iMore:


> With no content blocked, there are 38 third party scripts
> (scripts not hosted on the host domain) running when the homepage
> is opened, which takes a total of 11 seconds. Some of these
> scripts are hosted by companies I know, Google, Amazon, Twitter
> and lots from companies I don’t know. Most of which I assume are
> used to display adverts or track my activity, as the network
> activity was still active after a minute of leaving the page
> dormant. I decided to turn them all off all third party scripts
> and see what would happen.
> After turning off all third party scripts, the homepage took 2
> seconds to load, down from 11 seconds. Also, the network activity
> stopped as soon as the page loaded so it should be less strain on
> the battery.


I love iMore. I think they’re the best staff covering Apple today, and their content is great. But [count me in with Nick Heer](http://pxlnv.com/linklog/safari-content-blockers-shit-ass-websites/) — their website is *shit-ass*. Rene Ritchie’s response acknowledges the problem, but a web page like that — Rene’s 537-word all-text response — should not [weigh 14 MB](http://d.pr/i/19HMF).1


It’s not just the download size, long initial page load time, and the ads that cover valuable screen real estate as fixed elements. The fact that these JavaScript trackers hit the network for a full-minute after the page has completely loaded is downright criminal. Advertising should have minimal effect on page load times and device battery life. Advertising should be respectful of the user’s time, attention, and battery life. The industry has gluttonously gone the other way. iMore is not the exception — they’re the norm. 10+ MB page sizes, minute-long network access, third-party networks tracking you across unrelated websites — those things are all par for the course today, even when serving pages to mobile devices. Even on a site like iMore, staffed by good people who truly have deep respect for their readers.


With Safari Content Blockers, Apple is poised to allow users to fight back. Apple has zeroed in on what we need: not a way to block ads per se, but a way to block obnoxious JavaScript code. A reckoning is coming.


---

1. This very article on Daring Fireball, the one whose footnote you’re reading right now, weighs between 125–175 KB — *kilobytes* — depending on the random ad from The Deck being served. ↩︎



| **Previous:** | [On Jony Ive’s Promotion to Chief Design Officer](https://daringfireball.net/2015/05/jony_ive_promotion_chief_design_officer) |
| **Next:** | [‘Which Is the Most Important Device You Use to Connect to the Internet?’](https://daringfireball.net/2015/08/most_important_device) |


PreviousNext