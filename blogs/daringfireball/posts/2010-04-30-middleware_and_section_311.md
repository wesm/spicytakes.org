---
title: "Middleware and Section 3.3.1"
date: 2010-04-30
url: https://daringfireball.net/2010/04/middleware_and_section_311
slug: middleware_and_section_311
word_count: 1647
---


[Miguel de Icaza wrote a thoughtful, informative piece](http://tirania.org/blog/archive/2010/Apr-28.html) this week regarding how [MonoTouch](http://monotouch.net/) works, and how it might avoid conflicting with Apple’s [new Section 3.3.1](http://daringfireball.net/2010/04/why_apple_changed_section_331). It was published two days ago, thus, *before* [Steve Jobs’s “Thoughts on Flash”](http://www.apple.com/hotnews/thoughts-on-flash/) essay was published. De Icaza’s theory on the business case for the new, more restrictive Section 3.3.1 was pretty much flat-out confirmed by Jobs — Apple doesn’t want cross-platform lowest-common-denominator apps built on top of Cocoa Touch.


De Icaza’s second theory regards the UI case for the new Section 3.3.1:


> As I mentioned before, using cross-platform solutions like Flash
> or Silverlight would make every application look alien. But also
> like Steve Jobs alluded to, developers would not have access to
> new features on the iPhone OS if they had chosen a technology that
> did not expose it.
> For example, when Apple introduced in iPhone OS 3.2 the new split
> views that the iPad uses extensively when rotating your screen,
> that functionality would have taken too long to bring in a
> satisfactory way to say Silverlight on iPhone or Flash on iPhone.
> Or when Apple introduced the UIView that can be used to render
> maps, it would also have been challenging to embed this control.
> Or when Apple introduced GameKit, an API to connect iPhones and
> exchange messages between them.


Flash’s cross-compiler, we know, is explicitly ruled out by the new Section 3.3.1. Where MonoTouch stands, however, is not yet clear. As de Icaza explains, MonoTouch, unlike Flash, isn’t about creating write-once run-anywhere cross platform UIs:


> MonoTouch brings the C# language and the core of .NET to the
> iPhone, but does nothing to provide a cross-platform UI
> experience or for that matter any sort of mobile device
> cross-platform APIs. […]
> We released the iPad support 24 hours after Apple released the
> SDK. We released the iPhoneOS 4.0 support within days of the
> release (mostly because every one of us was pretty bummed out).
> [Our APIs are a 1:1 mapping to the iPhone APIs](http://go-mono.com/docs/monodoc.ashx?link=root%3a%2fMonoTouch-lib).
> Just like C and C++, if developers want to reuse code between
> MonoTouch, Windows 7 or MonoDroid, they will have to split their
> UI and device-specific code from their business logic. MonoTouch
> does not provide such an abstraction layer.


MonoTouch is *not* in the same boat as Flash’s iPhone compiler, as it’s not a cross-platform framework. It’s a lighter shade of gray, if you will. But it’s still a layer of middleware between developers and Apple’s own APIs. Yes, MonoTouch is keeping up to date with Apple’s native APIs today, but what happens three, four, five years from now if MonoTouch *stops* keeping up and hundreds (or thousands) of popular iPhone OS apps are dependent upon it? That’s the scenario Apple wants to avoid.


Here’s a bit from Jobs’s “Thoughts on Flash”:


> We know from painful experience that letting a third party layer
> of software come between the platform and the developer ultimately
> results in sub-standard apps and hinders the enhancement and
> progress of the platform. If developers grow dependent on third
> party development libraries and tools, they can only take
> advantage of platform enhancements if and when the third party
> chooses to adopt the new features. We cannot be at the mercy of a
> third party deciding if and when they will make our enhancements
> available to our developers.


One such “painful experience”, from Apple’s perspective, would be [Metrowerks’s PowerPlant framework](http://en.wikipedia.org/wiki/PowerPlant). PowerPlant was a GUI toolkit and application framework for the classic Mac OS, which shipped with Metrowerks’s CodeWarrior compiler and IDE. It was very good, and very popular — many popular Mac apps were built using the PowerPlant framework.


The problem came several years later, with the move to Mac OS X.1 PowerPlant wasn’t designed with Mac OS X in mind, and didn’t take advantage of Mac OS X’s latest advances. For example, Carbon Events support didn’t come to PowerPlant until 2004. There was no easy or straightforward way for PowerPlant-based apps to make the transition to best-of-breed native Mac OS X apps. Leaving Cocoa aside, PowerPlant apps couldn’t take advantage of the latest and greatest the Mac OS X Carbon APIs had to offer.


Now, the comparison isn’t quite apples-to-apples, because one of the biggest differences between classic Mac OS and Mac OS X is that classic Mac OS didn’t have a built-in One True App Framework like Mac OS X does with Cocoa. (And, it’s worth emphasizing that Carbon was a first class toolkit for Mac OS X for the first half of the decade — Cocoa wasn’t really officially positioned as the One True Framework until, arguably, WWDC 2007, when Apple abruptly cancelled 64-bit Carbon, which had been announced for Mac OS X 10.5 just 9 months earlier [at WWDC 2006](http://www.macworld.com/article/52233/2006/08/liveupdate.html).) The Metrowerks developers who created PowerPlant couldn’t have foreseen Carbon and Mac OS X, let alone foresee Cocoa, and the Mac developers who decided to use PowerPlant weren’t spurning any sort of “No, this is what you should be doing” advice from Apple.


But because PowerPlant (a) was popular and (b) didn’t keep up with the latest platform advances in Mac OS X, it became an anchor attached to Apple, which slowed them down. Apple expended significant time, money, and effort trying to support PowerPlant developers and bring them forward to where Apple wanted to take the platform.


So my comparison here isn’t to say that PowerPlant was bad or that developers who depended upon it did anything wrong. Rather, it’s that Apple learned that there were significant risks to letting any technology get between Apple’s APIs and third-party developers. Apple couldn’t fix PowerPlant. They couldn’t port it to Mac OS X themselves. It was out of their hands, and Motorola ([which bought Metrowerks in 1999](http://en.wikipedia.org/wiki/Metrowerks)) had other priorities.


De Icaza argues that this is the sort of decision that should be up to third-party developers:


> As a developer, I feel that I should be responsible for my
> technological choices. If I pick a cross-platform toolkit that
> looks horrible on the iPhone, it will just leave the space open
> for a competitor to do a better job. Or if my application does not
> take advantage of a new API in iPhone OS, I am also leaving a flank
> open for a competitor to take over. Apple does not need to
> intervene with guidelines as the application quality, the
> App Store, magazines, reviews and word of mouth are creating the
> conditions for an all-out darwinian survival of the fittest.


I think the above paragraph expresses very well the sentiment of many developers who strongly oppose, and in many cases are downright offended by, Apple’s new Section 3.3.1 restrictions. “*Let me take the risk of a chasm opening between the middleware I want to use and the underlying Cocoa Touch frameworks*,” more or less.


And that’s totally reasonable. But Apple’s perspective is reasonable too — they have suffered in the past when popular developer tools and frameworks have been out of their control. At this moment, Apple has the clout to forbid these “third party layers of software between the platform and the developer” by fiat. If they waited until actual compatibility problems arise in the future, it might be too late — at that point, if the incompatible middleware systems are popular enough, the clout will reside with the collective third-party developers relying upon the middleware, not with Apple. Apple can ban them by fiat now; they can’t ban them by fiat in a future where they’re in widespread use.


With middleware layers, the underlying platform can get stuck with the way things are. Apple wants to maintain as much control over native iPhone apps as it can, and it’s using this control to push forward on, in Jobs’s words, “the enhancement and progress of the platform”.


John Siracusa hit these same points two weeks ago, in a piece titled “[Apple’s Wager](http://arstechnica.com/staff/fatbits/2010/04/apples-wager.ars)”:


> Like the Mac, the iPhone debuted with a huge technical lead over
> its competitors. But this time, Apple is determined not to
> squander its advantage. Instead, it’s front-running as hard as it
> possibly can. Anything that has any chance of slowing down “[the
> progress of the platform](http://www.taoeffect.com/blog/2010/04/steve-jobs-response-on-section-3-3-1/)” has simply got to go. And the best way
> Apple knows to ensure platform progress is by controlling its own
> destiny in every way that it can. That means, among other things,
> no middleware vendors, no encouragement of cross-platform
> development (either explicit or implicit), and complete, arbitrary
> control over every application’s presence on the platform.
> It’s Apple’s contention that other mobile platforms that allow
> these things, most of which developers adore, do so at the cost of
> slowing the speed with which they advance upon their competitors.


I don’t know that Apple is right. As I said above, de Icaza’s perspective — that these decisions and risks should be up to individual developers to make — is utterly sensible. Siracusa is exactly right that this is a wager from Apple. Apple is betting its entire mobile future that their developer platform is better than everyone else’s.


---

1. The original version of this piece stated, incorrectly, that PowerPlant wasn’t compatible with Carbon at all: “PowerPlant wasn’t Carbon-compatible. There was no easy or straightforward way for PowerPlant-based apps to make the transition to Carbon. These were apps that were stuck running in Classic mode on Mac OS X.” That is incorrect, e.g., [see this PR from May 1999](http://findarticles.com/p/articles/mi_m0EIN/is_1999_May_12/ai_54620340/). I regret error, but the example, I think, still stands. ↩︎



| **Previous:** | [Gizmodo and the Prototype iPhone](https://daringfireball.net/2010/04/gizmodo_prototype_iphone) |
| **Next:** | [Apple-Verizon Political Calculus, 2010 Edition](https://daringfireball.net/2010/05/apple_verizon_political_calculus) |


PreviousNext