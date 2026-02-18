---
title: "In the Background"
date: 2008-10-06
url: https://daringfireball.net/2008/10/in_the_background
slug: in_the_background
word_count: 524
---


I’ve [written before](http://daringfireball.net/2008/03/one_app_at_a_time) about which apps are allowed to run in the background on the iPhone, but I’ve gotten a few emails about it in response to [this footnote](http://daringfireball.net/2008/10/the_fear#fn2-2008-10-02) in my “The Fear” piece last week:


> Even if Apple were to come to its senses and allow third-party
> developers to write competing email clients, the built-in Mail app
> would hold one significant technical advantage, which is that it
> runs in the background. In fact, background processing is the one
> factor that unites the four dock apps. Phone, Mail, Safari, and
> iPod all continue running in the background; no other apps,
> including those from Apple, do.


Everyone knows that the iPhone SDK doesn’t yet allow for third-party apps to run in the background. But what’s misleading is that several other of Apple’s built-in iPhone apps seems to run in the background. Calendar event reminders and incoming SMS messages display pop-up alerts system-wide. And the Clock app’s timers and alarms continue running even after you’ve closed the Clock app.


But as I wrote back in March, these apps — the Cocoa Touch apps themselves — don’t run in the background. They post and set notifications through other means, system-level OS services that aren’t available (to my knowledge) through the iPhone SDK.


Another example is the App Store app. Its icon badge updates with a count of the number of updates available for the apps you’ve already installed. This icon badge updates automatically, without your having to launch the App Store app. I’m pretty sure Apple is doing this via the push notification system that was announced at WWDC, but which hasn’t yet appeared in the public SDK.


The system does stuff in the background, and some of Apple’s apps take advantage of these features in ways that aren’t available in the SDK, but the only Cocoa Touch applications that run in the background are Phone, Mail, Safari, and iPod.


Phone, I believe, runs all the time, for obvious reasons. (I wouldn’t be surprised if it’s the Phone app that posts incoming SMS message alerts.) Mail runs in the background to allow for periodic new message checking. The iPod app only stays running in the background when it’s playing audio. Safari doesn’t really *do* anything in the background, but it stays running after you close it so that when you come back, the web pages you’ve already loaded in tabs remain loaded. By staying active, it also takes less time to activate.


The iPhone (and iPod Touch) only have 128 MB of RAM, and WebKit can use a lot of memory. When memory gets tight, the system sends low memory warnings to running applications, telling them to purge what they can. Eventually, the system will start forcing apps to quit in order to free more memory. That’s why sometimes when you relaunch Safari, it remembers the URLs, but has to reload the content for all of your open web pages — that’s what happens when Safari is asked to quit while it’s running in the background.



| **Previous:** | [The Fear](https://daringfireball.net/2008/10/the_fear) |
| **Next:** | [The iPhone 3G](https://daringfireball.net/2008/10/iphone_3g) |


PreviousNext