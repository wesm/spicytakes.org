---
title: "How to Enable ‘Your Watch Is Fully Charged’ Notifications in WatchOS 7 and iOS 14"
date: 2021-03-08
url: https://daringfireball.net/2021/03/your_watch_is_fully_charged_notifications
slug: your_watch_is_fully_charged_notifications
word_count: 780
---


One of my favorite new features in WatchOS 7 and iOS 14 is an option to have your iPhone display a notification when your paired Apple Watch is fully charged. This feature was announced at WWDC 2020, and [Juli Clover at MacRumors wrote a story about it the next day](https://www.macrumors.com/2020/06/23/ios-14-notification-apple-watch-charged/). It’s simple.


I didn’t start using this feature until the fall, when I began testing an Apple Watch Series 6, which I [reviewed here](https://daringfireball.net/2020/09/graphite_is_the_new_black). Eventually, I switched from that Series 6 review unit back to my personal Apple Watch, a Series 5 I bought last year. I didn’t give it much thought until this weekend, but I stopped getting those charging notifications when I switched watches, and I couldn’t figure out why. [So, I asked about it on Twitter](https://twitter.com/gruber/status/1368259561300385805):


> When I was using my Series 6 review unit, I got these
> notifications every time it charged. Now that I’m back on my own
> Series 5 watch, I never get them. Anyone else not getting these
> “Your watch is fully charged” notifications?


A lot of people who responded in that thread were as confused as I was about the feature. But it didn’t take long to figure out what was going on. It turns out that the setting to enable these notifications is in the “Sleep” section of the Apple Watch app on your phone. That makes some sense — the idea is that the people who most need these notifications are people who are tracking their sleep with Apple Watch, and thus can’t charge their watch overnight because they’re wearing it.


The problem is, if you haven’t set up your watch to track sleep in the Health app, the setting for these battery notifications doesn’t appear in the Apple Watch app. This is what the Sleep section in the Apple Watch app looks like if you have not set up Sleep in the Health app:


[
](https://daringfireball.net/misc/2021/03/apple-watch-sleep-settings-before.jpeg)


After you enable Sleep in the Health app (a multi-step process that requires going through a few screens to set sleep goals and a schedule), the Sleep section in the Apple Watch app looks like this, and the battery notification setting is obvious:


[
](https://daringfireball.net/misc/2021/03/apple-watch-sleep-settings-after.jpeg)


When I was testing my Series 6 review unit watch, I set all this up so I could try the new built-in sleep tracking features. I wound up not liking any of it, and I turned it all off by the time I stopped wearing the review unit. But because I had enabled Sleep tracking in Health for that watch, the option to get charging notifications remained available and enabled. I didn’t know it was there, and was only available because I had at least initially turned on Sleep in Health.


When I switched back to my Series 5 watch, I never enabled Sleep in Health for that watch, because I knew I didn’t like WatchOS 7’s sleep features.1 But the charging notifications I *did* want were never made available, because they only appear in the Apple Watch app after you enable Sleep in the Health app.


After I figured this out, it was easy to start getting “fully charged” notifications from my watch again. I just turned on Sleep in Health, then disabled all the actual WatchOS 7 Sleep features, and left the option enabled for battery notifications.


It’s all a bit confusing, because I don’t think it makes intuitive sense that these notifications are filed under “Sleep”. Nor that you need to set up Sleep in one app (Health) to get features enabled in another app (Apple Watch). I get why people who use the built-in Sleep features would be interested in the charging notification, but I never would have figured this out on my own. And it feels a bit convoluted that the solution involved me turning on a bunch of Sleep features I didn’t want to get a battery notification setting to appear.


---

1. I actually do use my Apple Watch for sleep tracking — but with [David Smith’s excellent Sleep++ app](https://apps.apple.com/us/app/sleep/id1038440371). My pal Merlin Mann turned me onto Sleep++ [during an episode of my podcast back in May 2019](https://daringfireball.net/thetalkshow/2019/05/14/ep-251). What I love about using Sleep++ is that it’s entirely passive. I don’t set a schedule, Sleep++ doesn’t tell me when to go to sleep, and I don’t have to do anything when I go to bed other than just wear my Apple Watch while I sleep. Sleep++ just looks at my biometric data and it figures out when I’m asleep, and sends me a simple report in the morning after I wake up. ↩︎



| **Previous:** | [iA Writer](https://daringfireball.net/2021/03/ia_writer) |
| **Next:** | [Intel Goes Long](https://daringfireball.net/2021/03/intel_goes_long) |


PreviousNext