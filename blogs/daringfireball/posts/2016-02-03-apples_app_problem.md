---
title: "Apple’s App Problem"
date: 2016-02-03
url: https://daringfireball.net/2016/02/apples_app_problem
slug: apples_app_problem
word_count: 700
---


Following up on [Walt Mossberg’s column](http://www.theverge.com/2016/2/3/10900612/walt-mossberg-apple-iphone-ios-mac-osx-app-problems) regarding the quality of Apple’s first-party apps, [Jim Dalrymple writes](http://www.loopinsight.com/2016/02/03/about-walt-mossberg-and-apples-app-problem/):


> I understand that Apple has a lot of balls in the air, but they
> have clearly taken their eye off some of them. There is absolutely
> no doubt that Apple Music is getting better with each update to
> the app, but what we have now is more of a 1.0 version than what
> we received last year.
> Personally, I don’t care much about all the celebrities that Apple
> can parade around — I care about a music service that works.
> That’s it.
> If Apple Music (or any of the other software that has
> problems) was the iPhone, it would never have been released in
> the state it was.


Software and hardware are profoundly different disciplines, so it’s hard to compare them directly. But it seems obvious to me that Apple, institutionally, has higher standards for hardware design and quality than it does for software.


Maybe this is the natural result of the fact hardware standards *must* be high, because they can’t issue “hardware updates” over the air like they can with software. But the perception is now widespread that the balance between Apple’s hardware and software quality has shifted in recent years. I see a lot of people nodding their heads in agreement with Mossberg and Dalrymple’s pieces today.


We went over this same ground a year ago in the wake of Marco Arment’s “[Apple Has Lost the Functional High Ground](https://marco.org/2015/01/04/apple-lost-functional-high-ground)”, culminating in a really interesting (to me at least) [discussion with Phil Schiller at my “Live From WWDC” episode of The Talk Show](http://daringfireball.net/thetalkshow/2015/06/09/ep-123). That we’re still talking about it a year later — and that the consensus reaction is one of agreement — suggests that Apple probably does have a software problem, and they *definitely* have a perception problem.


I’ll offer a small personal anecdote. Overall I’ve had great success with iCloud Photo Library. I’ve got over 18,000 photos and almost 400 videos. And I’ve got a slew of devices — iPhones, iPads, and Macs — all using the same iCloud account. And those photos are available from all those devices. Except, a few weeks ago, I noticed that on my primary Mac, in Photos, at the bottom of the main “Photos” view, where it tells you exactly how many photos and videos you have, it said “Unable to Upload 5 Items”. Restarting didn’t fix it. Waiting didn’t fix it. And clicking on it didn’t do anything — I wanted to know *which* five items couldn’t be uploaded, and why. It seems to me that anybody in this situation would want to know those two things. But damned if Photos would tell me.


Eventually, I found [this support thread](https://discussions.apple.com/thread/7174772?start=0&tstart=0) which suggested a solution: you can create a Smart Group in Photos using “Unable to upload to iCloud Photo Library” as the matching condition. Bingo: five items showed up. (Two of them were videos for which the original files couldn’t be found; three of them were duplicates of photos that were already in my library.)


My little iCloud Photo Library syncing hiccup was not a huge deal — I was even lucky insofar as the two videos that couldn’t be found were meaningless. And I managed to find a solution. But it feels emblematic of the sort of nagging software problems people are struggling with in Apple’s apps. Not even the bug itself that led to these five items being unable to upload, but rather the fact that Photos knew about the problem but wouldn’t tell me the details I needed to fix it without my resorting to the very much non-obvious trick of creating a Smart Group to identify them. For me at least, “silent failure” is a big part of the problem — almost everything related to the whole [discoveryd/mDNSresponder fiasco](http://daringfireball.net/s/discoveryd) last year was about things that just silently stopped working.


Maybe we expect too much from Apple’s software. But Apple’s hardware doesn’t have little problems like this.



| **Previous:** | [Why Apple Assembles in China](https://daringfireball.net/2016/01/why_apple_assembles_in_china) |
| **Next:** | [On the San Bernardino Suspect’s Apple ID Password Reset](https://daringfireball.net/2016/02/san_bernardino_password_reset) |


PreviousNext