---
title: "Google Mobile Uses Private iPhone APIs"
date: 2008-11-19
url: https://daringfireball.net/2008/11/google_mobile_uses_private_iphone_apis
slug: google_mobile_uses_private_iphone_apis
word_count: 1092
---


Google’s just-released and much-publicized update to their Google Mobile iPhone app features some very clever interaction design for the voice search feature. There is an on-screen button you can tap to initiate a voice search manually, but, as illustrated in their [example video](http://googlemobile.blogspot.com/2008/11/google-mobile-app-for-iphone-now-with.html), you can initiate a voice search just by lifting your iPhone to your ear.


In order to trigger this automatic voice prompt, you must:

1. Move the iPhone.
2. Trigger the proximity sensor next to the speaker at the top of the iPhone.


You need to do both, in that order.1 The voice prompt is never triggered by motion alone, nor by covering the proximity sensor without first having moved the phone. The only way it is triggered is by moving the phone and then triggering the proximity sensor. It’s very clever, and the resulting user experience is very nice.


But here’s the intrigue: There is no public API in the iPhone SDK for using the proximity sensor in this way.


As you might imagine considering the number of accelerometer-driven games in the App Store, there are plenty of public API calls to access data from the iPhone’s accelerometer. But the only thing apps can do with the proximity sensor is turn it on and off. When the proximity sensor is on, the screen turns off and stops accepting touch input when you cover the sensor (typically with your head, when holding the phone to your ear to, say, make a phone call, but you can just as easily trigger it by covering the sensor with your finger). By default, the proximity sensor is turned off, and the overwhelming majority of apps leave it that way.


If you’re a registered iPhone developer, you can read the relevant documentation [for the `proximitySensingEnabled` property](https://developer.apple.com/iphone/library/documentation/UIKit/Reference/UIApplication_Class/Reference/Reference.html#//apple_ref/doc/uid/TP40006728-CH3-DontLinkElementID_15) in the UIApplication Class Reference. An app can check the status of this property (is it on or off?), and can toggle it, but that’s it. After an app has turned the proximity sensor on, the app never finds out when or if it has actually been engaged. There is no way for an app to be notified when the proximity sensor has been triggered.


No way, that is, via the public APIs.


If you use something like the command-line `strings` utility to examine the UIKit framework, you can see that there’s an undocumented (and therefore private to Apple) method named `proximityStateChanged`. And if one were to strip the FairPlay DRM from the current Google Mobile application binary — which, of course, you wouldn’t do, because you’re not supposed to strip FairPlay DRM, but I’m just saying *if* one were to do this — a class dump of the application binary would show that Google Mobile does in fact implement `proximityStateChanged`.


So, (a) Google Mobile is using an undocumented API, and (b) to my knowledge, there is no way to duplicate the behavior of Google Mobile’s “just lift the phone to your ear to trigger the voice prompt” feature using only the public APIs in the iPhone SDK. Needless to say, using undocumented APIs violates the iPhone SDK Guidelines. A developer that plays by the rules cannot do what Google is doing.


---


I can think of three explanations for how Google got away with this:

1. Whoever at Apple approved this Google Mobile update did not realize that it was using the private `proximityStateChanged` method.
2. Whoever at Apple approved it knew that it used a private API, but approved it anyway.
3. Google sought and obtained permission from Apple to use this method.


I do not believe #3 is the case. I’m pretty sure that the App Store approval process is as much of a black box for Google as it is for everyone else.


That leaves #1 and #2, either of which suggests that the Google Mobile team followed the adage that it’s easier to ask for forgiveness than for permission. If this is the case — *if* — it might explain why Google started publicizing the voice search feature [several days before](http://www.nytimes.com/2008/11/14/technology/internet/14voice.html?partner=rss&emc=rss&pagewanted=all) it actually appeared in the App Store. The publicity from John Markoff’s feature in The New York Times put [pressure](http://www.techcrunch.com/2008/11/15/more-apple-iphone-search-weirdness-and-embarrassment-for-google/) on Apple to accept the app. If there was any internal debate within Apple about whether to allow this, it might explain why the app took several days longer to appear in the store than Markoff’s story indicated Google expected.


#1 is possible. There is no technical barrier that prevents a third-party iPhone app from making calls to undocumented APIs, and I have heard that several apps that do so have slipped past the App Store approval process. But I would presume the Apple employees who examine App Store submissions are well-versed regarding which hardware features are exposed through the official public APIs.


If it’s #2, though, this stinks. Third-party iPhone development is purportedly a level playing field. If regular developers are forced to play by the rules, but Google is allowed to use private APIs just because they’re Google, the system is rigged.


So here’s to hoping that it’s #1. Even in that case, the situation just highlights the problem that a lot of cool features are behind the iPhone’s private APIs — private APIs which Apple’s own apps make full use of. I understand the reason why the developers of Google Mobile used this method — without it, the feature isn’t possible (and, frankly, the proximity sensor isn’t of much use). The downside to third-party use of any undocumented APIs, however, is that undocumented APIs can change or vanish in future iPhone OS updates, which situations inevitably lead some users to be outraged that Apple doesn’t [support the unsupported](http://daringfireball.net/2007/10/un_in_unsupported).


---


*My thanks to [Robert Marini](http://hiddengalaxy.net/) for assistance researching certain of the technical aspects of this article, including going so far as to build an iPhone app to test whether any documented application delegates are triggered when the proximity sensor is engaged. (The answer is no.)*


---

1. This explains why, if you turn on Google Mobile’s off-by-default setting to allow the UI to rotate, the automatic voice search prompt is disabled. By default Google Mobile tracks motion to see if you’ve moved the phone to your ear; turning the UI rotation option on means it instead tracks motion to see if the display orientation should be changed. I suspect the two uses conflict, in that when you rotate the iPhone, your thumb is likely to cover the proximity sensor. ↩︎



| **Previous:** | [iPhone-Optimized Google Search Results](https://daringfireball.net/2008/11/iphone_optimized_google_results) |
| **Next:** | [Treating URL Protocol Schemes as Cruft](https://daringfireball.net/2008/11/treating_url_protocol_schemes_as_cruft) |


PreviousNext