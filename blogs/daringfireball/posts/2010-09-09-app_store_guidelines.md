---
title: "A Taste of What’s New in the Updated App Store License Agreement and New Review Guidelines"
date: 2010-09-09
url: https://daringfireball.net/2010/09/app_store_guidelines
slug: app_store_guidelines
word_count: 1347
---


Apple today [announced](http://www.apple.com/pr/library/2010/09/09statement.html) several significant changes to the iOS developer agreement, and a new document called the [App Store Review Guidelines](http://developer.apple.com/appstore/guidelines.html). The latter is intended as a plain-English guide to the rules and guidelines Apple is using to determine which apps to accept into the store — a guide that has been sorely lacking to date.


These documents are only available to registered iOS developers, however, so here’s a look at some of what’s new.


## Section 3.3.1 — Third-Party Developer Tools and Languages


This is the section that was [changed a few months ago](http://daringfireball.net/2010/04/why_apple_changed_section_331), with the release of iOS 4.0, to ban the use of third-party developer tools. In the 4.0 version of the agreement, section 3.3.1 read (italics added):


> 3.3.1 Applications may only use Documented APIs in the manner prescribed
> by Apple and must not use or call any private APIs. *Applications
> must be originally written in Objective-C, C, C++, or JavaScript
> as executed by the iPhone OS WebKit engine, and only code written
> in C, C++, and Objective-C may compile and directly link against
> the Documented APIs (e.g., Applications that link to Documented
> APIs through an intermediary translation or compatibility layer or
> tool are prohibited).*


In today’s updated agreement, the entire italicized section has been removed. There’s no longer any mention of specific programming languages, nor any prohibition against “intermediary translation or compatibility layers”. This means, I believe, that tools such as Adobe’s Flash cross-compiler are no longer banned from use. If you can produce a binary that complies with the guidelines, how you produced it doesn’t matter.


## Section 3.3.2 — Interpreters


Old:


> 3.3.2 An Application may not itself install or launch other
> executable code by any means, including without limitation through
> the use of a plug-in architecture, calling other frameworks, other
> APIs or otherwise. Unless otherwise approved by Apple in writing,
> no interpreted code may be downloaded or used in an Application
> except for code that is interpreted and run by Apple’s Documented
> APIs and built-in interpreter(s). Notwithstanding the foregoing,
> with Apple’s prior written consent, an Application may use
> embedded interpreted code in a limited way if such use is solely
> for providing minor features or functionality that are consistent
> with the intended and advertised purpose of the Application.


New:


> 3.3.2 An Application may not download or install executable code.
> Interpreted code may only be used in an Application if all
> scripts, code and interpreters are packaged in the Application and
> not downloaded. The only exception to the foregoing is scripts and
> code downloaded and run by Apple’s built-in WebKit framework.


I don’t think this new language is a change in policy. It’s just a shorter, more direct explanation. So, for example, games that include a Lua interpreter are OK, but only if they use the Lua interpreter to run scripts that are hard-coded into the app bundle itself — it can’t be used to interpret script that users can download or install later. This change in language matches the de facto policy that has been applied by the App Store reviewers.


## Section 3.3.9 — Privacy and Analytics


Old:


> 3.3.9 You and Your Applications may not collect, use, or disclose
> to any third party, user or device data without prior user
> consent, and then only under the following conditions:
> The collection, use or disclosure is necessary in order to
> provide a service or function that is directly relevant to the use
> of the Application. For example, without Apple’s prior written
> consent, You may not use third party analytics software in Your
> Application to collect and send device data to a third party for
> aggregation, processing, or analysis.
> The collection, use or disclosure is for the purpose of serving
> advertising to Your Application; is provided to an independent
> advertising service provider whose primary business is serving
> mobile ads (for example, an advertising service provider owned by
> or affiliated with a developer or distributor of mobile devices,
> mobile operating systems or development environments other than
> Apple would not qualify as independent); and the disclosure is
> limited to UDID, user location data, and other data specifically
> designated by Apple as available for advertising purposes.


New:


> 3.3.9 You and Your Applications may not collect user or device
> data without prior user consent, and then only to provide a
> service or function that is directly relevant to the use of the
> Application, or to serve advertising. You may not use analytics
> software in Your Application to collect and send device data to
> a third party.


Again, shorter and sweeter. The language that seemed written specifically to ban AdMob — the mobile ad network purchased by Google, a purveyor of mobile operating systems — has been removed.


That’s it for the significant changes to the developer license agreement.


## App Store Review Guidelines


This new document is written in remarkably casual language. For example, a few bullet items from the beginning:


> We have over 250,000 apps in the App Store. We don’t need any
> more Fart apps.
> If your app doesn’t do something useful or provide some form of
> lasting entertainment, it may not be accepted.
> If your App looks like it was cobbled together in a few days, or
> you’re trying to get your first practice App into the store to
> impress your friends, please brace yourself for rejection. We have
> lots of serious developers who don’t want their quality Apps to be
> surrounded by amateur hour.
> We will reject Apps for any content or behavior that we believe
> is over the line. What line, you ask? Well, as a Supreme Court
> Justice once said, “I’ll know it when I see it”. And we think that
> you will also know it when you cross it.
> If your app is rejected, we have a Review Board that you can appeal to. If you run to the press and trash us, it never helps.


Much of the introduction [sounds as though](http://twitter.com/jsnell/status/24015510853) it were [written by](http://twitter.com/drwave/status/24014716480) Steve Jobs.


Most importantly:


> This is a living document, and new apps presenting new questions
> may result in new rules at any time. Perhaps your app will
> trigger this.


Some examples of rules that were enforced, but never previously codified:


> 10.4 Apps that create alternate desktop/home screen environments or
> simulate multi-app widget experiences will be rejected
> 10.5 Apps that alter the functions of standard switches, such as the
> Volume Up/Down and Ring/Silent switches, will be rejected


And some interesting ones:


> 2.11 Apps that duplicate apps already in the App Store may be
>   rejected, particularly if there are many of them
> 3.10 Developers who attempt to manipulate or cheat the user
>   reviews or chart ranking in the App Store with fake or paid
>   reviews, or any other inappropriate methods will be removed from
>   the iOS Developer Program […]
> 11.11 In general, the more expensive your app, the more thoroughly
> we will review it […]
> 14.1 Any app that is defamatory, offensive, mean-spirited, or
> likely to place the targeted individual or group in harms way will
> be rejected
> 14.2 Professional political satirists and humorists are exempt
> from the ban on offensive or mean-spirited commentary


(Not sure why “professionals” qualify for an exemption here, nor what it is that qualifies someone as a “professional”.)


The existence of this document is a very welcome change, and it goes a long way to answering much of the criticism regarding prior controversial App Store rejections, by putting in writing the rules that are actually used by the reviewers.



| **Previous:** | [Miscellaneous Observations Regarding the Gadgets That Were (and Were Not) Announced at Last Week’s Apple Event](https://daringfireball.net/2010/09/ipod_observations) |
| **Next:** | [What’s Next for Nokia?](https://daringfireball.net/2010/09/nokia_next) |


PreviousNext