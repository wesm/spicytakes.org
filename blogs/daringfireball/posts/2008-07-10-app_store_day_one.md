---
title: "The App Store, Day One"
date: 2008-07-10
url: https://daringfireball.net/2008/07/app_store_day_one
slug: app_store_day_one
word_count: 1058
---


Observations regarding the App Store and some of the apps:


## Download Counts


On the iPhone’s App Store app, at the bottom of the details page for every app is a downloads count. Given that the only way to download a non-free app is to buy it, it more or less puts sales figures out in the open. These download numbers are not visible in iTunes — only in the App Store app.


[**Update, 11 am EDT:** At some point overnight, Apple reset the download counts to zero, and they’ve stayed there. Second thoughts regarding the open kimonos? Also, it’s unclear whether the download counts that were visible yesterday (and reported below) were U.S.-only or worldwide.]


This is interesting for a couple of reasons. First, obviously, you can look at popular apps and figure out how much money they (and Apple) have made. As I type this, Sega’s Super Monkey Ball game has been downloaded 10,955 times, and costs $9.99. That’s $109,440 in revenue in under a day — about $76K for Sega, and $33K for Apple.


Second, for the handful of apps with free and paid counterparts, we can see how many people are willing to pay for the non-free versions. The Iconfactory’s [Twitterrific](http://iconfactory.com/home/permalink/2009) and Fraser Speirs’s Flickr client [Exposure](http://connectedflow.com/exposure/) share a very similar model: both apps are available through the App Store in two forms: (a) a free version, supported by occasional ads from [The Deck](http://decknetwork.net/)1, and a paid ad-free version for $9.99. As of this writing, here’s how the download counts look:



| Exposure | 3,638 |
| Exposure Premium | 76 |
| Twitterrific | 13,638 |
| Twitterrific Premium | 322 |



So the ratios are very similar: 48-1 for Exposure, and 42-1 for Twitterrific. These numbers very well may change over time — for example, perhaps some users are treating the free ad-supported versions as the equivalent of demo versions, and, if they continue using and enjoying the apps, will spring for the paid premium versions in a few weeks.


The download numbers don’t seem to be live, and a few developers who’ve been (understandably) obsessing over their numbers all day have told me that they’ve seen them fluctuate — both up and down. I suspect both the non-live updates and downward fluctuations are related to caching.


It’ll be interesting to see if Apple continues displaying these numbers going forward. And it’ll be interesting to see what happens tomorrow, after the iPhone 3G goes on sale in Europe and North America, and after (I presume) the iPhone 2.0 OS update is officially released for existing iPhone users.


## Reliability


Given the high daily traffic of the iTunes Store (for music and video), I’m not surprised, but the App Store seemed perfectly responsive all day long. Again, though, tomorrow — after the worldwide launch of the iPhone 3G and the 2.0 OS — will be the real test.


I even bought and downloaded an app over EDGE, no problem at all. (Apps purchased over the phone network — EDGE or 3G — are limited to 10 MB, but most apps are well under that.)


## Re-Downloads


If you accidentally delete an app you’ve bought, you can re-download it for free. The App Store UI doesn’t make this clear, but Apple describes it in [this KBase article](http://support.apple.com/kb/TS1702). What you do is act like you’re buying it again — tap the app’s price, and the App Store will recognize that you’ve already purchased it and ask if you wish to download it again. You can also do this from iTunes, to re-download an app to your computer that you originally purchased on your iPhone.


## Sandboxing


Each app *and its data* are stored together, at least conceptually. When you delete an app from your phone, all of the files belonging to that app are deleted as well — preferences, data, support files — all of it is removed. Further, apps are not able to install files in the system behind your back. Delete an app from the home screen and there’s no sign of it left behind.


This doesn’t mean data files are stored within an application’s bundle — they’re not. What it means is that because you, the user, don’t manage anything at the file system level, iTunes and the iPhone OS take care of all of it for you. Foolproof, almost — a very friendly conceptual design for typical users.


## AOL’s AIM App, and Third-Party Prefs in the System-Wide Settings App


I’d sort of forgotten about it after the early demo back at the SDK announcement event in March, but one of today’s top downloads is an official AIM client from AOL — 43,226 downloads at this writing. I found it to be buggy as hell. At one point it was crashing for me on launch, endlessly, until I deleted it and re-installed. It doesn’t do links — URLs in a message aren’t tappable. Some messages came in blank — I could see who they were from, but there was no visible text.


One other thing I noticed might prove important when using other applications, as well. AIM’s settings are not accessed within the app itself; rather, AIM adds a settings panel to the system-wide Settings app. What makes this so confusing, though, is that the first time you launch AIM, it (logically) prompts you for an AIM username and password. However, if you make a typo entering either, there’s no visible way to correct it — the account setup screen goes away after your first attempt. To change them, you need to leave AIM and open Settings, then scroll down (third-party panels are at the bottom).


AOL is not being untoward in this regard; this is actually what Apple encourages iPhone developers to do. Based on the apps I’ve seen today, though, most developers aren’t doing it. That’s a bad combination — if most third-party apps display their settings screens themselves, then when users do encounter an app that uses the system-wide Settings app, they’re very likely to assume that the app simply doesn’t have any settings.


---

1. Disclosure: Daring Fireball has been part of The Deck ad network since February 2006. ↩︎



| **Previous:** | [Android Expectations](https://daringfireball.net/2008/06/android_expectations) |
| **Next:** | [iPhone Display Color Temperature, and the Difference Between Builds 5A345 and 5A347 of the iPhone OS](https://daringfireball.net/2008/07/iphone_display_color_temperature) |


PreviousNext