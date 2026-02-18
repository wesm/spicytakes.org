---
title: "The Threat to the Mac: The Growing Popularity of Non-Native Apps"
date: 2018-02-12
url: https://daringfireball.net/2018/02/non_native_apps_threat_to_mac
slug: non_native_apps_threat_to_mac
word_count: 550
---


Peter Ammon, former AppKit engineer at Apple, [in a comment in a Hacker News thread](https://news.ycombinator.com/item?id=16350277) regarding [a report](https://krausefx.com/blog/mac-privacy-sandboxed-mac-apps-can-take-screenshots) positing that the ability of Mac apps — even sandboxed ones — to capture screenshots of the entire screen is a security problem:


> IMO the app sandbox was a grievous strategic mistake for the Mac.
> Cocoa-based Mac apps are rapidly being eaten by web apps and
> Electron pseudo-desktop apps. For Mac apps to survive, they must
> capitalize on their strengths: superior performance, better system
> integration, better dev experience, more features, and higher
> general quality.
> But the app sandbox strikes at all of those. In return it offers
> security inferior to a web app, as this post illustrates. The
> price is far too high and the benefits too little.
> IMO Apple should drop the Mac app sandbox altogether (though
> continue to sandbox system services, which is totally sensible,
> and maybe retain something geared towards browsers.) The code
> signing requirements and dev cert revocation, which has been
> successfully used to remotely disable malware, will be sufficient
> security: the Mac community is good at sussing out bad actors. But
> force Mac devs to castrate their apps even more, and there won’t
> be anything left to protect.


In a follow-up comment, [Ammon enumerates *why*](https://news.ycombinator.com/item?id=16352284) truly native Cocoa apps are both worth creating and better to use.


I’m with Ammon: I think the Mac’s (relatively) recent move to cryptographically signed applications — with certificates that can be revoked by Apple — has been a win all around for security. But I don’t think the Mac sandbox has. The sandboxed nature of all iOS apps works because that’s how iOS was designed from the ground up. That’s why iOS is a better platform than the Mac for non-expert users in most ways. But the Mac was not designed with sandboxing in mind, and in many ways sandboxing works against what keeps the Mac relevant alongside iOS. [As I wrote seven years ago](https://daringfireball.net/2010/12/future_of_the_mac_in_an_ios_world): “It’s the heaviness of the Mac that allows iOS to remain light.”


The whole point of the Mac is to be a great platform for native Mac apps. Sandboxing doesn’t help Mac apps do more. If the Mac devolves into a platform where people just use web browsers and cross-platform Electron apps, it might as well not exist, because the only remaining thing that would distinguish it from other desktop OSes is iCloud integration.


Mac apps have been able to “see” the entire display ever since the Mac debuted. The Mac needs the power to allow the user to shoot themselves in the foot. Or perhaps better said, the Mac needs the power for apps to shoot the user in the foot. On the Mac, you need to trust any software you install, particularly from outside the App Store. A Mac where all apps are guaranteed “safe” is no longer a Mac. Further restricting sandboxed Mac apps would be solving a problem the platform doesn’t have. The real problems facing the Mac are the number of developers creating non-native “Mac” apps and the number of users who don’t have a problem with them.



| **Previous:** | [HomePod](https://daringfireball.net/2018/02/homepod) |
| **Next:** | [Sponsoring Daring Fireball, Early 2018 Edition](https://daringfireball.net/2018/02/sponsoring_daring_fireball) |


PreviousNext