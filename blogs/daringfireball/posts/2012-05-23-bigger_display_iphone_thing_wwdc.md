---
title: "How Apple Could Play the Bigger-Display iPhone Thing at WWDC, Which I Swear, I’m Still Not Convinced Is for Real But We’re Getting to the Point Where There’s an Awful Lot of Smoke for There Not to Be a Fire So Let’s Run With It"
date: 2012-05-23
url: https://daringfireball.net/2012/05/bigger_display_iphone_thing_wwdc
slug: bigger_display_iphone_thing_wwdc
word_count: 1040
---


For the sake of argument let’s take it as a given that the next iPhone will sport an 1136 × 640 display﻿, with the same 326 pixels-per-inch resolution as the iPhone 4 and 4S, the same width, but an extra 176 pixels in height, changing the aspect ratio from 3:2 to 16:9.


Let’s further assume that this new iPhone will not be announced until later this year, say, around October, just like the 4S last year. How might Apple get developers on the right track to support a new aspect ratio at WWDC next month while maintaining their standard radio silence regarding as-yet-unannounced products?


The easiest way: By doing nothing at all. iOS 6 could be announced next month without Apple saying a word about supporting multiple aspect ratios. Then they could just announce the new iPhone in October and expect developers to get on board ASAP. Apple says “Jump”; iOS developers ask “How high?”


But, keep in mind, iPhone apps are *already* expected to be at least somewhat flexible in height. Use a well-written app while you’re on a phone call or making a recording with the Voice Memos app, and you get a double-height status bar (green for phone calls, red for recordings). But the double-height status bar doesn’t cover the content of most apps. Springboard tightens the spacing between its rows of app icons. Apps like Mail, Safari, and Calendar move the top of the window — the [UINavigationBar](http://developer.apple.com/library/ios/#documentation/uikit/reference/UINavigationBar_Class/Reference/UINavigationBar.html) — down to account for the double-sized status bar. The same is true [for third-party apps](https://daringfireball.net/misc/2012/06/double-height-status-bar.png).


In short, “windows” on iOS resize like windows on a Mac. Except instead of the user being able to resize the window in both dimensions to any arbitrary size, on iOS “windows” are expected to resize only in one dimension. ([Will Hains is thinking](http://willhains.com/post/23401520339/wishful-thinking) along similar lines.)


What has occurred to me, though, is that Apple could, with the (presumed) upcoming WWDC introduction of iOS 6, further encourage developers to be flexible in this regard by changing the way notification banners are displayed. As it stands, notification banners are shown one at a time, and cover the content of the underlying app. WebOS seemed1 more elegant in this regard — [WebOS notification banners stacked on screen](http://www.google.com/search?q=webos+notifications&hl=en&prmd=imvns&tbm=isch&tbo=u&source=univ&sa=X&ei=VBK9T-r5NqX56QGY1_Up&ved=0CGIQsAQ&biw=1123&bih=918), and the current app shrunk to fit the remaining space.


If Apple introduced something like this in iOS 6, they could encourage iOS developers to adopt the recommended APIs to be responsive to changes in available vertical screen space. For now, they could pitch this in the context of *shrinking* screen space in response to on-screen notification banners, but, come October, apps that do the right thing would automatically be responsive to, say, a new device with 176 *more* pixels.


## Why Bother?


We can argue about just how difficult supporting a new iPhone screen size would be for developers, just how much complexity it would introduce, but no matter how easy you think it may wind up being, there’s no doubt that it would add *some* extra work, and *some* extra complexity. So why do it?


I suspect the answer is, why not? The design tension in post-iPhone mobile phones is between screen size (where bigger is better) and device size (where smaller is better). You want a physical device that is small enough to fit easily in your pockets and is comfortable and easy to use while holding it in one hand. But you want a screen that’s as big as feasible, so you can see more content — more words in email messages, web pages, and e-books; bigger pictures and video.


If Apple indeed increases the size of the next iPhone’s display to 4 inches, *I do not expect them to increase the physical size of the device itself.* There is plenty of room on the current iPhone for the rumored 4-inch display — just shrink the non-display areas on the front face. On the iPad, the thick bezel area surrounding the display serves an essential purpose — it gives you a place to rest your thumbs while holding the device. The non-display “forehead” and “chin” on the front face of the iPhone serve no such practical purpose. All Apple needs is enough room for a home button at the bottom, and the speaker, camera, and proximity sensor at the top.2


Why didn’t they start with a 16:9 display at the outset, in 2007? Who knows? They’ll never explain themselves. Maybe they couldn’t pull it off technically at the time. Maybe they’ve simply changed their minds. If Apple’s designers think 16:9 would be better today, they’ll switch. It’s that simple.


## What Apple Won’t Do With Those Extra Pixels


Judging from my email, the most common theory out there about what Apple might do with those extra pixels is to make the app-switching dock a persistent system-wide presence. That way developers wouldn’t need to do a damn thing — apps would still get the same 960 × 640 screen area, and the switching dock (the thing you see when you double-press the home button) would be on screen all the time.


I say no way.


First, this would be antithetical to the iOS aesthetic. iOS apps get the whole display, minus only (and optionally!) the status bar. When you launch an app, the device, conceptually, *is* the app. A persistent app dock would ruin that.


Second, practically, this would be a disaster. An erroneous tap on the icons in the dock would instantly zap you out of the current app. Think about where it would be — right under the keyboard. Miss the space bar by a few pixels and *pop* — you’re zapped to another app, mid-sentence. I’ve experienced this problem firsthand with Android phones with soft keys underneath the display. It’s a usability disaster.


Third, making the switching dock a persistent on-screen element would solve no problem. Needing to double-press the home button to invoke it is not a hardship.


---

1. Too soon to speak of WebOS in the past tense? ↩︎
2. And maybe some of those things [can be hidden behind the display](http://arstechnica.com/apple/2009/01/apple-patent-application-shows-isight-behind-notebook-screen/). ↩︎



| **Previous:** | [iOS Low-Hanging Fruit](https://daringfireball.net/2012/05/ios_low_hanging_fruit) |
| **Next:** | [More on Apple’s Removal of Airfoil Speakers Touch From the App Store](https://daringfireball.net/2012/05/more_on_airfoil_speakers_touch) |


PreviousNext