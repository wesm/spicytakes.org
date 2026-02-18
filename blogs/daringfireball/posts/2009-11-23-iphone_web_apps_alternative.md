---
title: "iPhone Web Apps as an Alternative to the App Store"
date: 2009-11-23
url: https://daringfireball.net/2009/11/iphone_web_apps_alternative
slug: iphone_web_apps_alternative
word_count: 1155
---


Peter-Paul Koch (a long-time, highly-regarded expert on web standards and rendering engine compatibility), argues forcefully that developers who wish to write software for the iPhone [should skip the App Store and write iPhone-optimized web apps instead](http://www.quirksmode.org/blog/archives/2009/11/apple_is_not_ev.html). His essay, perhaps because it is so strongly-worded, seems to have polarized the responses. The truth, as usual, lies somewhere in the middle.


His piece is definitely worth reading, and his primary point is true:


> In order to release an iPhone application without having to submit
> it to Apple’s insane App Store process, developers could just
> use Web technologies and create Web apps instead of native apps.


iPhone web apps are not in any way restricted by Apple. And I think he’s correct that the technique is currently under-utilized, and it’s a huge benefit to developers that such apps should also work just as well on Android and WebOS, with minimal additional work.


But he’s also very much wrong about just what’s possible in an iPhone web app, in terms of user experience. Koch writes:


> I reviewed the apps I have on my iPhone, and most can be released
> as a Web app *right now*. The exceptions are complex games that are
> both graphically and programmatically intensive, and apps that
> depend on device functions such as the accelerometer or GPS.
> As I said, Safari supports geolocation, and maybe Apple is working
> on other device APIs. That would solve all problems for the second
> category. Complex games will remain very hard to release as a Web
> app in the near future.
> Still, the graphically simple games such as sudoku and chess, the
> interactive shopping lists, the dictionaries and bible citation
> apps, the beer appreciation apps, the firmware Yahoo weather app,
> and most importantly *all* social network clients could have been
> written as a Web app without any loss of quality whatsoever. (Most
> have fairly little quality to lose in any case.)


I don’t know about “social network clients” in general, because I don’t use many social networks. But I do use two of them heavily: Twitter and Flickr.


There is no way anyone could write an iPhone web app that works as well or feels as good as any of the top native iPhone Twitter clients. You can make *an* iPhone Twitter client as a web app. You can even make a *good* one. In fact, Dean Robinson *did* — it’s called [Hahlo](http://blog.hahlo.com/). It’s a good iPhone Twitter client. It’s a web app. It’s also slower, less graceful, and less useful than any of the popular native iPhone Twitter clients.


With Flickr, it’s even worse. For just viewing existing Flickr content, Flickr’s own [m.flickr.com](http://m.flickr.com/) web site is great. But you can’t write an iPhone web app Flickr client that lets you upload new photos or videos. It isn’t technically possible, because iPhone web apps don’t have access to the device’s image library or the camera.


The argument that you can make iPhone web apps that are “good enough” misses the entire point of iPhone apps — the entire point of the iPhone itself, even — all of the things that drive Twitter users to pay $3, $4, or $5 for apps that do the same things that can be done for free by loading Twitter’s web site in MobileSafari. “Good enough” is not good enough on the iPhone.


There’s a serious [dog food factor](http://en.wikipedia.org/wiki/Eating_one%27s_own_dog_food) at play. Apple’s own apps for the iPhone OS are written using Cocoa Touch. The only iPhone web app I can think of from Apple is the RSS reader at [reader.mac.com](http://reader.mac.com/), and the domain name alone tells you just how important that app is to Apple.


Koch writes (childish Jesus-caps on the pronouns his):


> Apple’s original plan for iPhone development was to use Web
> technologies. This plan caught both Mac developers and Web
> developers by surprise because it was totally unexpected.
> The plan failed. Jobs Himself ordered His developers to create Web
> applications with Web standards, but a deafening silence ensued.
> Then He hurriedly thought up the App Store. Too hurriedly, as it
> now turns out.


I can’t prove that this isn’t true. But [my theory has always been](http://daringfireball.net/2007/06/wherefore_art_thou_iphone_sdk) that Apple’s initial “[sweet solution](http://daringfireball.net/2007/06/wwdc_2007_keynote)” for third-party iPhone development — to just write web apps — was never intended as a long-term solution. I think the plan was always to allow native Cocoa Touch development eventually, and I don’t think there was anything rushed about it. The delay between the debut of the original iPhone and announcement of the SDK was, I think, simply due to the SDK not being ready in June 2007. Everyone who followed iPhone OS 1.x jailbreak development noted that the Cocoa Touch APIs changed *significantly* between iPhone OS 1.0 and 2.0.


But the best proof is what I pointed out above: Apple itself created almost no iPhone web apps. Successful iPhone developers don’t just want to write software that works on the iPhone. They want to write software for the iPhone that’s just as good as Apple’s. Today that means using Cocoa Touch and the native SDK.


When you write a Cocoa Touch app for the iPhone, you’re not starting from scratch. You’re starting with the Cocoa Touch framework. As Faruk Ateş astutely points out [in his response to Koch](http://farukat.es/journal/2009/11/347-iphone-developers-arent-stupid-ppk), to discount the framework is to discount everything that sets the iPhone apart as a development platform. Not only are native iPhone apps faster and more capable than their web-app equivalents, but they’re easier to write.


This may change. A combination of increasing CPU performance, further improvements to WebKit and the Nitro JavaScript interpreter, more RAM, and additional web app capabilities in the iPhone OS (things like access to the camera and image library) could, combined, make for a future where some types of iPhone web apps aren’t just “good enough” but are truly indistinguishable from native Cocoa Touch apps. The hardware performance improvements are inevitable, but it remains to be seen whether Apple will provide deeper and more significant iPhone OS-specific hooks for web apps. I hope they do. I think it would be good for everyone — Apple, developers, and iPhone users — if unrestricted web apps became a serious alternative to the restricted App Store. But it isn’t credible to argue that they already are.1


---

1. But even then, iPhone optimized web apps in this hypothetical future would *still* lack the commerce features provided by the App Store. Web app developers can charge for subscriptions to their software, sure — but it would be difficult to match the App Store in terms of the “just click ‘Buy’ and type your iTunes password” experience. ↩︎



| **Previous:** | [Maybe Instead of Two Cars, You Just Need a Car and a Bicycle](https://daringfireball.net/2009/11/a_car_and_a_bicycle) |
| **Next:** | [A Liberal, Accurate Regex Pattern for Matching URLs](https://daringfireball.net/2009/11/liberal_regex_for_matching_urls) |


PreviousNext