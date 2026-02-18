---
title: "Vesper, Adieu"
date: 2016-08-23
url: https://daringfireball.net/2016/08/vesper_adieu
slug: vesper_adieu
word_count: 1901
---


## What Happened


In December 2012, I started a company with my friends Brent Simmons and Dave Wiskus. We named it Q Branch. In June 2013, we launched our first and only product: an iPhone notes app called Vesper.


Yesterday, [we announced](http://daringfireball.net/linked/2016/08/22/vesper-shutting-down) that development was ceasing, and we’ll soon be shutting down our sync server. I am terribly sad about this. I love Vesper. I use it every day. I mean that in the present tense. I still use it. When we pull the plug on the sync server, I’ll stop, but until then it’s my go-to notes app. In my career, the only things I’ve done that I’m prouder of are writing Daring Fireball and the creation of Markdown.


What went wrong was very simple. We never made enough money. Why we didn’t make enough money, what we should have done differently to make more money — those are complex questions (which I’ll tackle below). But what actually sunk Vesper was not complicated. Even as a relatively popular app at a relatively high price (for iOS), revenue was never high enough. Brent took a job at the excellent Omni Group [in September 2014](http://inessential.com/2014/09/29/omni), and from that point onward the writing was on the wall. We could have, and probably should have, shut Vesper down a year ago. But we loved it too much. Or at least I did.


When we started at the end of 2012, Brent still had a few months to go working on [Glassboard](http://inessential.com/2012/05/15/glassboard_2_0). Dave and I spent that time designing Vesper for iPhone. Our basic plan was:

1. Build Vesper for iPhone. Sell it for around $5.
2. Build a sync system, either on top of a service like iCloud or Dropbox, or by rolling our own system.
3. Build Vesper for Mac. Sell it for around $20.
4. Build Vesper for iPad.
5. Maybe build a web version. (Would depend largely on how we implemented syncing in step 2.)


In hindsight, I am now convinced this plan was fundamentally flawed. The market for paid productivity apps for iOS is simply too difficult. There *are* exceptions, of course. [Fantastical](https://flexibits.com/fantastical-iphone) and [Tweetbot](http://tapbots.com/tweetbot/) are two examples from my own iPhone’s first home screen. But paid apps for iOS are the exception. The norm is clearly free apps, with in-app purchases. This is completely clear now, but it should have been clear to me three years ago.


If I could do it all over again, here is what I would do differently. I would start the exact same way, with Dave and me designing Vesper for iPhone. But then, before Brent wrote a single line of code, we would immediately design Vesper for Mac.1 And *that’s* the product we’d have built and shipped first. There is downward pressure on pricing for Mac apps, but the market is still there for quality apps that cost $20–100 (or more). The plan would have looked like this:

1. Build Vesper for Mac. Sell it for around $20.
2. Build a sync system.
3. Build Vesper for iPhone.
4. Build Vesper for iPad.
5. Maybe build a web version.


The biggest advantage to this plan would have been that (I think) we’d have made far more money in step 1 than we actually made by doing Vesper for iPhone first. I can’t prove that, of course. I could be wrong. But I’m pretty sure I’m right. That would have made a big difference in terms of having revenue to continue working to turn Vesper into a multi-platform system.


We didn’t know it at the time (and couldn’t have), but this alternate schedule would have also saved us a lot of work. iOS 7 was introduced at WWDC 2013, just a few days after we shipped Vesper 1.0. In many ways, Vesper 1.0’s look and feel was ahead of the iOS 7 curve — [Charles Perry wrote a very kind piece](http://dazeend.org/2013/06/vesper-the-first-app-for-ios-7/) calling Vesper 1.0 “the first app for iOS 7”. But it wasn’t. iOS 7’s appearance was *so* different that even an app like Vesper that was designed with many of the same ideals needed a thorough redesign. So we spent the summer of 2013 not building a sync system, but rather [building an iOS 7 version of Vesper](http://daringfireball.net/2013/09/vesper_whats_new_whats_next). If we had built the Mac app first, we wouldn’t have had to build Vesper for iPhone twice.


iOS 7, in addition to looking all-new, introduced new architectural features like [size classes](https://developer.apple.com/library/ios/recipes/xcode_help-IB_adaptive_sizes/chapters/AboutAdaptiveSizeDesign.html). In the pre-iOS 7 era, building an iPad app was like building a second app. You could bundle it together with the iPhone version in a universal binary, but from a developer’s perspective it was nearly twice the work. If we had *started* with iOS 7, we might been able to natively support the iPad from day one on iOS, so the actual schedule might have looked like this:

1. Build Vesper for Mac. Sell it for around $20.
2. Build a sync system.
3. Build Vesper for iOS 7, with native support for iPhone and iPad.
4. Maybe build a web version.


I’m a firm believer that you always need some good luck to succeed. We would have been luckier, timing-wise, if we had done the Mac app first, because we would have been able to build the iOS version for iOS 7 right from the start.


We suffered an enormous chicken-and-the-egg problem with our decision to keep to a small team and self-fund our efforts through revenue from the app itself. A notes app is only of interest to many people if it’s available both on their desktop *and* mobile device. The number one reason, by a long shot, that people didn’t buy Vesper is because it wasn’t available for the Mac. I get that. It makes total sense. Hell, I even cheat, personally, and run Vesper on my Mac in the iOS Simulator. The bottom line is we needed revenue from the first version we built to fund development of the next version, and I think we would have made money from the Mac version.


Ultimately, what we should have done once we had versions of the app for both Mac and iOS is switch to a subscription model. Make the apps free downloads on all platforms, and charge somewhere around $15/year for sync accounts. That’s where the industry is going. It would have been more sustainable, and on iOS it would have solved the “free” barrier. What most people do when looking for, say, an iPhone notes app, is search the App Store for “notes”, and then start downloading free apps until they find one that seems good enough. There are so many free apps in a category like notes that paid ones — even if they’re just $1 — never get a look. Again, I’m not complaining. That’s just the way the App Store is.


It’s also entirely possible that a notes app was *never* going to work, financially. That it was a bad idea from the get-go, and no matter how nicely designed the app was, no matter how lovingly well-crafted, no matter what price point we had picked (higher or lower), it wasn’t going to work financially.2 But given how well Vesper *did* do, I firmly believe it was possible that we could have made it, if we’d done it differently. And I’m convinced the best chance would have been with free Mac and iOS apps and a paid sync service.3


## Miscellaneous Other Points

- We’ve been asked “Why now?” Why not just let Vesper and Vesper Sync keep going as they are? The biggest factor is that we have recurring costs: primarily, the sync server. We’re losing money every month.
- The most common comment I’ve seen since our announcement yesterday is something to the effect of “This is why I wish you had used iCloud instead of rolling your own sync service.” Long story short, we thoroughly investigated iCloud as a sync solution. And in 2013, iCloud just didn’t offer what we needed. I’ve never seen anyone say good things about iCloud Core Data. I know developers who had simply nightmarish experiences with iCloud Core Data. [CloudKit wasn’t announced until WWDC 2014](https://developer.apple.com/videos/play/wwdc2014/208/), and didn’t ship until later that year. If we were starting today, I’ll bet we’d wind up using CloudKit.
We also wanted to keep our options open for a web-based version of Vesper — or, less likely but still possible, Android or Windows versions. That’s possible in 2016 with [CloudKit Web Services](https://developer.apple.com/videos/play/wwdc2014/208/), but it wasn’t possible using iCloud in 2013. As delineated above, I have many regrets about Vesper, but creating our own sync system isn’t one. In 2013 it was the right thing to do. (And, I’ll add, Vesper Sync is the best sync system I’ve ever used. It was fast and reliable right from the moment we started testing it internally. I can brag about it because I had nothing to do with it — it was entirely Brent’s work.)
- [Vesper is now free in the App Store](https://itunes.apple.com/us/app/vesper/id655895325?mt=8). If you were ever curious about it, but were reluctant to pay, you might as well check it out.


## Q Branch


I quoted Brent Simmons [yesterday](http://daringfireball.net/linked/2016/08/22/vesper-shutting-down):


> I loved working on Vesper. It was one of the great software-making
> experiences of my life. We’d get on a roll and it was wonderful.
> And now it hurts to turn it off, but it’s time.


So short, but so true. I really enjoyed working with Brent and Dave. When we were on a roll I could tell that we were doing good work, and it was fun. I’ve spent the better part of my career working solo. It was great to be on a team. I don’t remember who came up with the names “Q Branch” (I think that was Brent), or “Vesper” (I’m pretty sure that one was Dave), but in both cases, as soon as the name was proposed, the whole team said, *Yes, that’s the name. That’s it.*


With “Vesper” we were thinking things like *beautiful, smart, clever, strong*. In the end, the name was more apt than we knew, because it also carries *heartbreak*.


---

1. The reason I think we were correct to *design* Vesper for iPhone first, before designing the Mac version, is because mobile is more limited. There are technical constraints and screen real estate constraints. A Mac app can do anything an iOS app can do; the opposite is not true. By designing the iPhone app first, we’d be far more likely to avoid the mistake of adding features in the Mac version that were difficult or impossible to do on iOS. Any app you intend to bring to mobile should be designed for mobile first. ↩︎
2. It certainly didn’t help Vesper’s chances that Apple put a lot of much-needed love into Apple Notes last year, especially the iOS version. I still have many complaints about Apple Notes, but overall it’s pretty good, both on Mac and iOS. ↩︎︎
3. If we had gone this route, where people had paid for the first version of Vesper as a paid app and we subsequently switched to a subscription plan and made the apps free downloads, we would have given existing users a free year or two of subscription service. ↩︎︎



| **Previous:** | [Bloomberg’s Report on Apple Watch 2](https://daringfireball.net/2016/08/bloomberg_apple_watch_2) |
| **Next:** | [iPhone 7: Jet Black vs. Black](https://daringfireball.net/2016/09/iphone_7_jet_black_vs_black) |


PreviousNext