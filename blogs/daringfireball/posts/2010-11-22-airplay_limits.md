---
title: "Video Support for AirPlay Is Limited in iOS 4.2"
date: 2010-11-22
url: https://daringfireball.net/2010/11/airplay_limits
slug: airplay_limits
word_count: 478
---


AirPlay is the killer feature for Apple TV. But perhaps we’d better keep that in the future tense for now: it’s *going to be* the killer feature for Apple TV. After installing today’s various software updates for iOS devices, the only apps I’ve seen where AirPlay works for video are the built-in iPod app (a.k.a. “Video” on the iPad and iPod Touch) and YouTube. In other apps, AirPlay is audio-only.


The most obvious shortcoming: You can’t use AirPlay to play videos shot on your iPhone. That’s an obvious feature, right? Shoot a video on your iPhone, then play it back for family and friends on your big TV via AirPlay. No syncing, no docking, no moving files around. Just hit play. But it doesn’t work in iOS 4.2.1 — even though you *can* use AirPlay to show still photos from the Photos app. I can’t get AirPlay video to work from Apple’s iMovie app for the iPhone, either. (Audio over AirPlay works just fine.)


[I asked](http://twitter.com/gruber/status/6898534456500224) about this on Twitter tonight, and one reasonable theory was that it was a problem with encoding bandwidth. HD movies rented or bought from iTunes tend to be encoded with bitrates of about 5 Mbit/s. Video clips shot on the iPhone 4 have bitrates of about 10-11 Mbit/s — the iPhone doesn’t have the processing power to compress movies tighter than that. But that means video shot on your iPhone is “bigger” than video downloaded from iTunes, or video converted on your computer to a format optimized for devices like the iPhone and Apple TV. So, the theory goes, maybe AirPlay doesn’t support video clips shot on your iPhone because they’re not compressed well enough to stream at a reasonable rate.


But that doesn’t seem to be the case. If you take a video shot on your iPhone, import it to your Mac, then put that clip in iTunes and sync it back to iPhone, you can then play that same video file over AirPlay using the “iPod” (on iPhone) or “Video” (on iPad/iPod Touch) app. I do not believe that iTunes re-compresses video when syncing it to your device. The same video streams over AirPlay from one app (iPad/Video), but not another (Photos).


AirPlay video streaming also doesn’t work from Mobile Safari. Tap the AirPlay button while playing a video in Safari and the options are all audio-only.


So my best guess is that Apple *really* wanted to ship iOS 4.2 in November — especially for the sake of the iPad — and some features didn’t make the cut. Widespread AirPlay video support, I suspect is one of those things — and that we’ll see a lot more places where AirPlay works for video in future iOS updates.



| **Previous:** | [News Corp’s Upcoming iPad App ‘The Daily’ to Pioneer New Recurring Subscription Billing](https://daringfireball.net/2010/11/the_daily_and_recurring_subscription_billing) |
| **Next:** | [Viber](https://daringfireball.net/2010/12/viber) |


PreviousNext