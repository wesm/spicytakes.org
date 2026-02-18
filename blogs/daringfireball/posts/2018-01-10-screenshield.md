---
title: "ScreenShield — a Third-Party SDK That Somehow Allows iOS Apps to Prevent Screenshots"
date: 2018-01-10
url: https://daringfireball.net/2018/01/screenshield
slug: screenshield
word_count: 550
---


[From the announcement of a new version of Confide, a “confidential messenger” app](https://blog.getconfide.com/introducing-screenshield-ios-screenshot-prevention-for-confide-and-beyond-692bbae2c31d):


> ScreenShield is a patent-pending technology that allows you to
> view an app’s content on your screen but prevents you from taking
> a screenshot of it. If you try to take a screenshot on Confide,
> you will now simply capture a blank screen¹. ScreenShield also
> protects against other forms of screen capture, including iOS 11
> screen recording, AirPlay screen mirroring, QuickTime screen
> recording as well as taking screenshots from the app switcher or
> by using Xcode.
> We initially developed ScreenShield for Confide, but quickly
> realized that it could be used in a large number of apps — far
> more than we could build ourselves. That’s why we created
> [ScreenShieldKit](https://screenshieldkit.com/) — to offer the ScreenShield technology to
> 3rd-party developers for use in a variety of different apps and
> categories.
> While there’s a lot of technology under the hood that makes
> ScreenShield possible, the great news is that there are no strange
> gimmicks for users (e.g., it doesn’t require them to hold their
> finger on the screen) — it just works as expected. And
> ScreenShieldKit is simple for developers to integrate into their
> iOS apps, providing easy to use replacements for UITextView and
> UIImageView.


It’s an interesting puzzle trying to figure out how they’re doing this. Detecting that a screenshot *has* been taken is easy — [iOS has an API](https://developer.apple.com/documentation/uikit/uiscreencaptureddidchangenotification) that apps can use to get notified when the screen is recorded in any way. But ScreenShield is detecting it *before* the screenshot gets taken, so they can blank out the content in their text and image views.


I wasn’t familiar with Confide, so I downloaded it and kicked the tires, and the screenshot prevention works as advertised. Confide *also* sends a notification to whomever you’re messaging with to warn them that you *tried* to take a screenshot, *a la* Snapchat, and they immediately delete the message you tried to capture (I presume so that you can’t try to capture it another way, like, say, by taking a photo of the screen — see below).


My best guess as to how they’re doing this is that they’re using AVPlayer and somehow using [FairPlay Streaming](https://www.reddit.com/r/iOSProgramming/comments/6h1nkc/how_are_apps_like_netflix_hbo_go_blocking_screen/) to block screenshots and recording. (Where by “my” best guess I mean the best guess of [a smart friend](http://bitsplitting.org/) who poked around the Confide app bundle.) Have you ever noticed how you can’t take screenshots of streaming video content in apps like Netflix and HBO Go/Now? That’s a feature in iOS (and MacOS — try taking a screenshot of Netflix video playing in Safari) for skittish video providers who don’t want us to capture even a still frame of their precious content. I *think* ScreenShieldKit is somehow using this to prevent screenshots or video captures of text or images.


If anyone out there has a better or more informed guess, please let me know.


If I’m reading their application correctly, Confide has also filed for a patent [for a way to identify when you’re using another device to take a photo of your screen](http://patft.uspto.gov/netacgi/nph-Parser?Sect1=PTO2&Sect2=HITOFF&p=1&u=%2Fnetahtml%2FPTO%2Fsearch-bool.html&r=1&f=G&l=50&co1=AND&d=PTXT&s1=9648001&OS=9648001&RS=9648001).



| **Previous:** | [Pressing the Side Button to Confirm Payments on iPhone X](https://daringfireball.net/2017/12/side_button_to_confirm_payments_on_iphone_x) |
| **Next:** | [Dean Allen](https://daringfireball.net/2018/01/dean_allen) |


PreviousNext