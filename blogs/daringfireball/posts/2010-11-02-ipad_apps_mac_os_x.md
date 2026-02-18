---
title: "Regarding the Idea of iPad Apps Running on Mac OS X"
date: 2010-11-02
url: https://daringfireball.net/2010/11/ipad_apps_mac_os_x
slug: ipad_apps_mac_os_x
word_count: 868
---


[Dave Winer speculates](http://scripting.com/stories/2010/11/01/angryBirdsOnMacbookAir.html):


> The software we will buy from the Mac version of the App Store
> will be the actual software that runs on the iPad and iPhone.
> In other words, they’re teaching the developers, privately, how to
> write iPad software for an iPad with a keyboard. In other words,
> the MacBook Air.


[Rene Ritchie even wonders](http://www.tipb.com/2010/11/01/mac-app-store-run-ipad-apps/) if that’s what’s going on this week at the private iOS developer meeting in Cupertino. (It’s not — that event is a Game Center summit.)


There’s no doubt that iOS is where the developer mojo is. Not just Apple’s developer mojo, but the industry’s. It’s the hottest platform in the world, period. And I do think Apple sees the upcoming Mac App Store as an opportunity for iOS developers who’ve never written apps for the Mac to start. But I don’t think iPad apps are ever going to run on the Mac as-is, without any change or adaptation to account for the very different input methods. This isn’t about ARM vs. x86 code generation, or development frameworks. It’s about the fact that direct manipulation on a touchscreen is fundamentally different than moving a mouse cursor via a touchpad. (Secondarily: iPad apps can and do assume that they will run full-screen on a 9.7-inch 1024 × 768 display. What happens in Winer’s scenario when you launch an iPad app on a 27-inch iMac?)


I can prove it, practically, that iPad apps aren’t going to run on the Mac as a standard feature. iOS apps *do* run on Mac OS X, today, in the iPhone/iPad emulator that ships with the iOS developer kit. Ends up they’re just not that pleasant to use on a Mac. Gestures that are natural and fun with direct touch are awkward and clumsy using a mouse or touchpad. I never hear iPad developers — who run their own iOS apps on their Macs during development, for testing and debugging purposes — wish that they could ship them as-is to Mac users. Ever try a game like Pac-Man on the iPhone? A game that’s designed from the ground up around a hardware joystick or D-pad just isn’t very good on a device without a joystick. Everything about iOS apps is like that when you run them on a Mac. (And, conversely, popular iOS games like Angry Birds tend to feature controls that *only* really make sense with a touchscreen.)


That said, prior to the iPad’s official announcement, I was on the record predicting that the iPad (or, as I called it then, [The Tablet](http://daringfireball.net/2009/12/the_tablet)) would only run iPad-specific apps — apps written with the same APIs and frameworks as iPhone apps, but optimized for the tablet-sized display. I was wrong about that — the iPad supports running iPhone-sized apps. But everyone with an iPad knows that non-iPad-optimized iPhone apps stink on the iPad. Personally, I don’t use any of them. I still think the reason Apple allowed iPhone apps to run on the iPad is simply to make sure there were thousands of apps available on day one, whether they were ideal or not. The Mac doesn’t suffer that problem. (I wouldn’t be surprised if the iPad eventually drops support for non-iPad optimized apps.)


In short, I think Winer’s basic *notion* is correct, insofar as that Apple plans to make Mac OS X more iPad-like, and that they might be working on ways to make Mac development more like iOS development. But he’s wrong on exactly how this could happen. It can’t and won’t be as easy as somehow just letting iPad apps run on the Mac.


I think it would be something more like how native iPad apps are related to, but different than, iPhone apps. In Cocoa, Mac apps are based on the [AppKit](http://www.informit.com/articles/article.aspx?p=1353402) framework — and AppKit dates back to the original NeXT frameworks from the late 1980s. With the iPhone, Apple replaced AppKit with [UIKit](http://developer.apple.com/technologies/ios/cocoa-touch.html). I’m far (*very* far) from being a Cocoa expert, but I know enough to say that UIKit is different from AppKit in more ways than just issues related to mouse cursors vs. touchscreens. UIKit is in some ways a clean slate do-over — an “if we could do it all over again, we’d do a few things differently” successor to AppKit. Can I imagine iPad apps, exactly as we know them today, running on Mac OS X? No. Can I imagine a future variant of UIKit for the Mac, which results in native Mac apps that are inherently more iOS-like? Yes.1 That’s all conjecture about the future, though. The Mac App Store that’s scheduled to ship about two months from now is going to debut filled with nothing but good old-fashioned AppKit Mac apps.


The whole point of Apple’s success with iOS has been the opposite of “write once, run anywhere”. It’s more like “write a version that is specifically optimized for this particular device”.


---

1. Same goes for hypothetical future UIKit apps for the Apple TV. ↩︎



| **Previous:** | [An Anthropomorphized White iPhone 4 Is Confronted Regarding Its Inability to Be Shipped](https://daringfireball.net/2010/10/anthropomorphized_white_iphone_4) |
| **Next:** | [Going Flash-Free on Mac OS X, and How to Cheat When You Need It](https://daringfireball.net/2010/11/flash_free_and_cheating_with_google_chrome) |


PreviousNext