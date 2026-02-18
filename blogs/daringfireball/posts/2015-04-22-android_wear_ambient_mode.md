---
title: "Android Wear’s Low-Power Ambient Mode"
date: 2015-04-22
url: https://daringfireball.net/2015/04/android_wear_ambient_mode
slug: android_wear_ambient_mode
word_count: 531
---


Josh Lowensohn, [writing for The Verge on Google’s latest update to Android Wear](http://www.theverge.com/2015/4/20/8447971/android-wear-update-wifi-support-emoji-smartwatch):


> Two other changes Google’s made in the update impact what you see
> on screen, and how you interact with it. One is a new low-power
> mode for the screen when you’re not actively looking at it. It
> allows apps to ambiently display just a minimal amount of data,
> usually in black and white, without a gesture to turn the screen
> on. Google already does this for your watch face, but is opening
> up the feature for apps too. This is especially useful for things
> like shopping lists, fitness apps, and music controls, Chang says.
> Developers will now be able to tweak how often the information you
> see gets updated in the low-power mode, but it could ultimately
> mean less fiddling.


This is a significant difference between Android Wear and Apple Watch. Apple Watch and most1 Android Wear watches use OLED displays, on which black pixels consume little power. Apple Watch embraces its OLED display by presenting an “on” UI where almost everything has a black background — its watch faces, the app home screen, and all of the built-in apps have black backgrounds. When you read email on Apple Watch, it’s white text on a black background. It’s a very different aesthetic from iOS and Mac OS, where the default has always been black text on a white background. The other thing worth noting is that when Apple Watch is “off”, the screen turns off completely. It’s just black.


Android Wear has a colorful Material Design-style UI for its “on” state — white backgrounds and lots of primary colors, very much the same aesthetic design as Google’s apps for Android and iOS. It looks like what its name implies: a version of Android running on a watch. Its “off” state, though, uses a black background and a small amount of static (non-animated) status information. Like, say, the hour and minute hands of an analog clock face, and/or the text of your most recent notification. Like with Pebble, something is displayed on screen unless the device is truly powered off. This is undeniably useful, and something like this ambient mode for Apple Watch would address [my complaint](http://daringfireball.net/2014/09/apple_watch) about not being able to glance the time without moving my wrist at all.


Apple’s approach is more conservative energy-wise in both “on” and “off” states. Google’s leaves something informative on screen at all times.


Apple’s decision to have the screen display nothing while “off” was clearly a concession to battery life. But I’m convinced that Apple chose the black-background look for the “on” state more for aesthetic reasons than for battery life — a fundamental aspect of Apple Watch’s design is that you can almost never see where the screen ends and the surrounding bezel begins. It’s a compelling, elegant effect. The battery-life advantages of this design are just a nice side effect.


---

1. The Moto 360 uses an LCD display, which is [why ambient mode is turned off by default on it](http://www.droid-life.com/2014/09/08/moto-360-ambient-screen-mode/). ↩︎︎



| **Previous:** | [Custom Watch Faces](https://daringfireball.net/2015/04/custom_watch_faces) |
| **Next:** | [Watch, Apple Watch](https://daringfireball.net/2015/04/watch_apple_watch) |


PreviousNext