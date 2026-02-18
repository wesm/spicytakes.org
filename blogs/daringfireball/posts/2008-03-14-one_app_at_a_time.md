---
title: "One App at a Time"
date: 2008-03-14
url: https://daringfireball.net/2008/03/one_app_at_a_time
slug: one_app_at_a_time
word_count: 833
---


One week in, the most controversial aspect of the iPhone SDK seems to be the limitation that third-party apps can only run when frontmost — once the user goes back to the home screen or switches to another app, the frontmost app needs to quit.


There are many reasons you might want an app to continue running in the background. (Or, at least, to have a faceless helper process continue to run in the background. But this too is disallowed in the current iPhone SDK.)


Some of these reasons are made clear by the built-in apps from Apple that *do* run in the background: Phone, Mail, Safari, and iPod. In other words, the apps in the iPhone’s default dock. So, a third party app won’t be able to check for new messages from a server periodically in the background like Mail does. Nor will it be able to continue playing an audio file in the background, like iPod does.


The rest of Apple’s current iPhone apps, though, don’t run in the background either. (Contrary to [my speculation last week](http://daringfireball.net/linked/2008/march#fri-07-background), the SMS and Clock apps do not run in the background. They post and receive notifications while not frontmost via other means; however, I do not know whether these means are currently exposed in the iPhone OS APIs to third parties.) One of the [first things I noticed](http://daringfireball.net/2007/06/iphone_first_impressions) with the iPhone was that there’s no indication in the UI regarding which apps are currently running, or what happens to the current app when you hit the home button. There is no concept of launching or quitting — there is only switching. This illusion is maintained by keeping launch and quit times as brief as possible. General rule: When an iPhone app quits, whatever you’re currently doing is saved; when it re-launches, whatever you were doing is restored.


Why has Apple imposed this limitation? Easy: the iPhone is severely resource constrained. Battery, RAM, and CPU cycles are all severely limited. If third-party apps could run in the background, all three could suffer. RAM would suffer for sure; all running apps consume memory. The iPhone has just 128 MB of RAM, and no swap space. CPU performance and battery life would suffer when background apps do something — and if they’re not doing anything, what’s the point of keeping them running? I noticed a significant increase in battery life after I switched the Mail app’s auto-checking interval from 15 minutes to 60 minutes. That’s just one app.


The profound simplicity of the iPhone user interface stems in part from the complete lack of interface elements for managing processes.1 There is no task manager or memory meter; if you want to know what’s running, the answer is simply whatever app it is that you’re looking at. Even the blessed apps that *do* run in the background, like Mail and Safari, must be prepared to quit at any time if the system requires more memory for the frontmost app. (That’s why Safari’s tabs occasionally blank out — the URLs for each tab are remembered, but the contents must be reloaded the next time Safari launches.)


And, the iPhone engineering team has gone to extraordinary lengths to make sure these background apps have a minimal CPU/battery/memory footprint while they are running. Call them hypocrites if you will for disallowing third parties from creating background-capable apps, but Apple only uses background processes itself for a handful of flagship apps. (The iPod app, for example, *only* runs in the background if you switch to another app while it’s playing an audio track. Otherwise, it too quits on switch.)


*Could* Apple allow third-party apps to run in the background? Of course. This is a trade-off, one in which technically advanced users pay the price for the benefit of typical users. Said benefit is simply this: users will not have to worry that by installing new apps from the App Store they’re going to slow down their phone or screw up its battery life. What’s the alternative? A “don’t install or launch too much crap” policy?


That this is how it is now does not mean this is how it will always be. Five months ago there wasn’t yet even official word from Apple that there would even be a native iPhone SDK. Also, keep in mind that it is far easier to set harsh restrictions first and relax them later than the other way around.2


In short, your iPhone will not be doing much while it’s in your pocket. The iPhone is driven by your actions, and, by design, for the purposes of resource conservation, does very little in the background, period.


---

1. A lack of “computer administrative debris”, to borrow [Edward Tufte’s parlance](http://katidev.com/blog/?p=20). ↩︎
2. For what it’s worth, though, I don’t expect this “no background apps” policy to be rescinded until iPhones ship with significantly more RAM and significantly faster CPUs. ↩︎



| **Previous:** | [More Questions](https://daringfireball.net/2008/03/more_questions) |
| **Next:** | [Confusion Regarding iPhone Developer Beta Program](https://daringfireball.net/2008/03/iphone_sdk_confusion) |


PreviousNext