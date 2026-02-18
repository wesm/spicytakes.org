---
title: "Why Apple Changed Section 3.3.1"
date: 2010-04-08
url: https://daringfireball.net/2010/04/why_apple_changed_section_331
slug: why_apple_changed_section_331
word_count: 918
---


We’re still in the early days of the transition from the PC era to the mobile era. Right now, Apple is winning. There are other winners right now too — RIM is still growing, and Android has grown a ton in the past year.


The App Store platform could turn into a long-term de facto standard platform. That’s how Microsoft became Microsoft. At a certain point developers wrote apps for Windows because so many users were on Windows and users bought Windows PCs because all the software was being written for Windows. That’s the sort of situation that creates a license to print money.


I don’t think Apple even dreams of a Windows-like share of the mobile market. Microsoft’s mantra was (and remains) “Windows everywhere”. Apple doesn’t want *everywhere*, they just want *everywhere good*. The idea though, is to establish the Cocoa Touch APIs and the App Store as a de facto standard for mobile apps — huge share of both developers *and* users.


So what Apple does not want is for some other company to establish a de facto standard software platform *on top* of Cocoa Touch. Not Adobe’s Flash. Not .NET (through MonoTouch). If that were to happen, there’s no lock-in advantage. If, say, a mobile Flash software platform — which encompassed multiple lower-level platforms, running on iPhone, Android, Windows Phone 7, and BlackBerry — were established, that app market would not give people a reason to prefer the iPhone.


And, obviously, such a meta-platform would be out of Apple’s control. Consider a world where some other company’s cross-platform toolkit proved wildly popular. Then Apple releases major new features to iPhone OS, and that other company’s toolkit is slow to adopt them. At that point, it’s the *other* company that controls when third-party apps can make use of these features.


So from Apple’s perspective, changing the iPhone Developer Program License Agreement to prohibit the use of things like Flash CS5 and MonoTouch to create iPhone apps makes complete sense. I’m not saying you have to like this. I’m not arguing that it’s anything other than ruthless competitiveness. I’m not arguing (up to this point) that it benefits anyone other than Apple itself. I’m just arguing that it makes sense from Apple’s perspective — and it was Apple’s decision to make.


Flash CS5 and MonoTouch aren’t so much *cross*-platform as *meta*-platforms. Adobe’s goal isn’t to help developers write iPhone apps. Adobe’s goal is to encourage developers to write Flash apps that run on the iPhone (and elsewhere) instead of writing iPhone-specific apps. Apple isn’t just ambivalent about Adobe’s goals in this regard — it is in Apple’s direct interest to thwart them.


So consider how this change affects the various parties involved:


**Apple**: Good, they maintain complete control over native iPhone OS app development.


**Adobe and other producers of cross-device mobile meta-platforms:** Terrible, because they can’t target today’s leading mobile platform. And they’ve wasted a tremendous amount of effort creating tools to generate iPhone apps.


**Web developers:** No change. The iPhone remains completely open to web apps. The difference between the web, as a competitor to native iPhone apps, from something like Flash is that the web is not controlled by anyone. There is no platform vendor for the web — and Apple has complete control over WebKit, its implementation for the web.


**iPhone developers:** No change. If you’re a developer and you’ve been following Apple’s advice, you will never even notice this rule. You’re already using Xcode, Objective-C, and WebKit. If you’re an iPhone developer and you are *not* following Apple’s advice, you’re going to get screwed eventually. If you are constitutionally opposed to developing for a platform where you’re expected to follow the advice of the platform vendor, the iPhone OS is not the platform for you. It never was. It never will be.


(And, in one sense, this is good news for existing iPhone developers: their skill set is now in even greater demand.)


**Flash and C# developers:** Bad news, if you were hoping to target the App Store with your products. If you want to write iPhone OS software, follow Apple’s advice, not Adobe’s or Microsoft’s.


**iPhone users:** I can see two arguments here. On the one side, this rule should be good for quality. Cross-platform software toolkits have never — ever — produced top-notch native apps for Apple platforms. Not for the classic Mac OS, not for Mac OS X, and not for iPhone OS. Such apps generally have been downright crummy. On the other hand, perhaps iPhone users will be missing out on good apps that would have been released if not for this rule, but won’t now. I don’t think iPhone OS users are going to miss the sort of apps these cross-platform toolkits produce, though.


My opinion is that iPhone users will be well-served by this rule. The App Store is not lacking for quantity of titles.


Consider, for one example, Amazon’s Kindle clients for iPhone OS and Mac OS X. The iPhone OS Kindle app is excellent, a worthy rival in terms of experience to Apple’s own iBooks. The [Mac Kindle app is a turd](http://daringfireball.net/linked/2010/03/18/kindle-mac) that doesn’t look, feel, or behave like a real Mac app. The iPhone OS Kindle app is a native iPhone app, written in Cocoa Touch. The Mac Kindle app [was produced using the cross-platform Qt toolkit](http://www.flickr.com/photos/gruber/4443592894/).



| **Previous:** | [New iPhone Developer Agreement Bans the Use of Adobe’s Flash-to-iPhone Compiler](https://daringfireball.net/2010/04/iphone_agreement_bans_flash_compiler) |
| **Next:** | [Reading Between the iPhone OS 4.0 Lines](https://daringfireball.net/2010/04/reading_between_the_iphone_os_4_lines) |


PreviousNext