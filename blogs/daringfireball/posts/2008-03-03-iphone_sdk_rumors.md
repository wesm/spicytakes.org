---
title: "iPhone SDK Rumors and Speculation"
date: 2008-03-03
url: https://daringfireball.net/2008/03/iphone_sdk_rumors
slug: iphone_sdk_rumors
word_count: 557
---


Jeremy Horwitz [reports at iLounge](http://www.ilounge.com/index.php/news/comments/iphone-ipod-sdk-apple-to-approve-distribute-apps-limit-add-ons/) that Apple’s plans for the iPhone SDK include using the iTunes Store as a hub for distribution (not surprising), and that Apple will act as a gatekeeper, approving every app on a case-by-case basis (also not surprising). If you’re hoping for an open “write whatever apps you want/install whatever apps you want” situation like the Mac (or, for that matter, the current underground jailbreak iPhone SDK), you’re almost certainly going to be disappointed.


For commercial developers, distribution through iTunes has the potential to be far more lucrative than the distribution model for the Mac. Once you’ve crossed the hurdle of getting Apple to list your app, all a potential user would need to do is click “Buy” in iTunes: the iTunes Store already has their billing info, and iTunes (the app) will handle downloading the software and installing it. The big unanswered question is whether an iTunes-only distribution model will afford for freeware.


Horwitz also reports:


> Under current plans, SDK developers will be prevented from
> interfacing directly with Dock Connector-based accessories
> connected to the iPhone or iPod touch—a decision that we are told
> could cripple development of new accessories such as physical
> keyboards, traditional add-ons, and more ambitious, creative
> accessories such as Delphi’s iPhone car control prototype. One
> source described this limit as a guarantee that SDK-developed
> applications would be nearly as limited as current web-based ones,
> while consuming more of the device’s storage capacity.


Horwitz’s source sounds like a would-be peripheral maker — if what you really want to do is write iPhone software to provide an interface to a hardware peripheral, yes, a complete lack of access to the dock connector port puts the native SDK in the same boat as writing a web app: the *S.S. Useless*. But for pure-software developers, there are a ton of potential advantages to a native SDK. [Craig Hockenberry’s benchmarks](http://furbo.org/2007/08/15/benchmarking-in-your-pants/) comparing JavaScript running in MobileSafari to the equivalent code compiled from Objective-C showed tremendous performance differences. Anyone who’s actually used an iPhone or iPod Touch has surely noticed that web apps are far less snappy and responsive to touch events than Apple’s native apps.


If it’s true that the dock connector is off-limits, that’s unfortunate, but also not surprising — clearly a big part of what Apple’s been working on in advance of this SDK are ways to sandbox applications for security and control of resources. (Expect “sandbox” to be an oft-repeated word.) Applications don’t talk directly to hardware ports in *Mac* OS X, either. That’s the realm of kernel extensions and other device drivers. Apple could, in theory, be on the cusp of announcing a very liberal *application* SDK but which still wouldn’t allow for third-party hardware drivers. I wouldn’t be surprised if the SDK severely limits direct access to the file system, let alone direct access to the hardware.


One announcement I expect is that access to the SDK will be tiered, and that one such tiering will be for network access: Wi-Fi for all, EDGE for only a privileged few, most likely very few indeed. The reasons for this are obvious, but I suspect won’t stop The Internet from proclaiming the SDK doomed from the start.


We’ll see [Thursday](http://arstechnica.com/journals/apple.ars/2008/02/27/apple-event-on-march-6-about-iphone-sdk-enterprise).



| **Previous:** | [Just the Internet](https://daringfireball.net/2008/02/just_the_internet) |
| **Next:** | [ExpanDrive](https://daringfireball.net/2008/03/expandrive) |


PreviousNext