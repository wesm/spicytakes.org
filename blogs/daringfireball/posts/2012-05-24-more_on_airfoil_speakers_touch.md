---
title: "More on Apple’s Removal of Airfoil Speakers Touch From the App Store"
date: 2012-05-24
url: https://daringfireball.net/2012/05/more_on_airfoil_speakers_touch
slug: more_on_airfoil_speakers_touch
word_count: 1042
---


After some interesting back-and-forth with a few informed sources, I think [Apple’s removal of Airfoil Speakers Touch from the iOS App Store](http://daringfireball.net/linked/2012/05/24/airfoil-speakers-touch) is not as mysterious or capricious as I first thought. The key is to focus on [what’s new in version 3 of the app](http://rogueamoeba.com/utm/2012/04/25/turn-any-ios-device-into-an-airplay-receiver-with-Airfoil-speakers-touch-3/):


> The other major feature in Airfoil Speakers is the new Enhanced
> Audio Receiving option. With an inexpensive in-app purchase, your
> iOS device becomes a full-fledged mobile AirPlay receiver! That
> means you can stream audio from one iOS device to another, or even
> send from iTunes directly to iOS. Why spend hundreds on a costly
> third-party AirPlay device, when you can use the iOS device you
> already have?


As I understand it, it’s not that Apple yanked Airfoil Speakers Touch after it had been in the store for three years. It’s that they yanked version 3 after it had been in the store for a month, and the issue is the above-quoted new feature.


Apple doesn’t provide APIs for apps to serve as AirPlay receivers. Rogue Amoeba backwards-engineered the protocol, and coded their own iOS AirPlay receiver implementation using (they claim, and I have no reason to doubt them) only public APIs. I think the bottom line is that Apple is saying that apps are not allowed to act as AirPlay receivers on iOS, but there’s no App Store guideline that explicitly forbids that. So they’re citing [App Store Review Guideline 2.5](https://developer.apple.com/appstore/resources/approval/guidelines.html):


> Apps that use non-public APIs will be rejected.


And rule 3.3.1 from the [iOS Developer Program License Agreement](https://developer.apple.com/programs/terms/ios/standard/ios_program_standard_agreement_20111004.pdf):


> Applications may only use Documented APIs in the manner prescribed
> by Apple and must not use or call any private APIs.


“Non-public APIs” and “private APIs” are the same thing. Rogue Amoeba claims — and I don’t doubt them — that they’re not using private APIs in this app. So perhaps it’s better to focus on this clause in rule 3.3.1: “in the manner prescribed by Apple”. That’s a pretty broad stick to swing. As I read it, rule 3.3.1 effectively means “*You may not use private APIs, and you may not use public APIs to do things we don’t want you to do.*”


That’s simultaneously unsurprising, and, a little crazy. Unsurprising because the implicit rule 0 of the App Store has always been that Apple isn’t going to publish an app they don’t want in the store, and that’s that. Crazy, though, because if Apple has a problem with the potential uses of a *documented public API*, is that not an indication that there’s something wrong with the API?


None of this is new, though. My favorite — no sarcasm intended — App Store rules are the plain-English “broader themes to keep in mind” at the top of the [App Store Review Guidelines](https://developer.apple.com/appstore/resources/approval/guidelines.html), and the last one of those seems apt:


> This is a living document, and new apps presenting new questions
> may result in new rules at any time. Perhaps your app will
> trigger this.


It’s not enough to comply with the letter of the rules; developers must comply with the spirit of them as well. Finding a loophole in the letter of the rules doesn’t grant you a Get Out of Jail Free card in the App Store. It will (hopefully) just lead to Apple adding a new rule to close the loophole. (This is not to imply that Rogue Amoeba saw themselves as taking advantage of a loophole; rather, I think it was a reasonable misunderstanding of the spirit of the guidelines. But that’s the heart of the problem for third-party developers: nobody who didn’t write the rules knows what the “spirit” of the rules is.)


Considering that the only Apple-sanctioned way to play an AirPlay audio stream from iTunes or an iOS device is with the use of a “Made For iPhone” authentication hardware chip that requires an approval process and licensing agreement with Apple, it doesn’t take a deep thinker to suspect that a reverse-engineered software AirPlay receiver might be something Apple doesn’t want in the App Store. But it’s also easy to see how this slipped through the App Store review process — the app (correctly) passed Apple’s automated tests that check for private API calls, and to anyone who isn’t particularly familiar with the encrypted and undocumented nature of AirPlay audio streams, Airfoil Speakers Touch’s new “Enhanced Audio Receiving” option simply looked like a cool new feature added to an app that had been in the store since 2009. After hitting the store, though, eventually it was bound to be noticed by someone at Apple who *is* intimately familiar with AirPlay. The app may not be using a “non-public API”, but it *is* decrypting a non-public streaming audio format, and Apple perhaps considers “non-public API” to cover all “non-public Apple technologies”, not merely literal application programming interfaces. I think that’s the bottom line.


Lastly, I’ve seen a few people speculate that perhaps Apple removed Airfoil Speakers Touch from the App Store because it’s about to be obviated by a built-in “use your device as an AirPlay receiver” feature in iOS 6. That, so I have heard from several well-perched little birdies, is not the case.1 It certainly doesn’t sound like how Apple works. Apple *does* add features to iOS (and Mac OS X) that obviate/compete with third-party software. But when they do so, they let the chips fall where they will. E.g., if Apple adds [offline support to Safari’s Reading List feature](http://www.marco.org/2012/05/23/safari-reading-list-offline-support) in iOS 6, they’re not going to remove Instapaper from the App Store.


---

1. To be clear, what I’ve “heard”, is that the reasons for Airfoil Speakers Touch’s removal from the store have nothing to do with any features that may or may not be in iOS 6. I did not hear whether such a feature actually *is* in iOS 6. ↩︎



| **Previous:** | [How Apple Could Play the Bigger-Display iPhone Thing at WWDC, Which I Swear, I’m Still Not Convinced Is for Real But We’re Getting to the Point Where There’s an Awful Lot of Smoke for There Not to Be a Fire So Let’s Run With It](https://daringfireball.net/2012/05/bigger_display_iphone_thing_wwdc) |
| **Next:** | [A Few Words About The Talk Show](https://daringfireball.net/2012/05/about_the_talk_show) |


PreviousNext