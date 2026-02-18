---
title: "‘Like the Sixth Finger in an AI-Rendered Hand’"
date: 2024-01-18
url: https://daringfireball.net/2024/01/the_sixth_finger
slug: the_sixth_finger
word_count: 1574
---


Brent Simmons, “[Corporations Are Not to Be Loved](https://inessential.com/2024/01/17/corporations_are_not_to_be_loved)”:


> Apple doesn’t care about you personally in the least tiny bit, and 
> if you were in their way somehow, they would do whatever their 
> might — effectively infinite compared to your own — enables them 
> to deal with you. 
> Luckily, Apple has just provided us all with a reminder. Just like 
> the sixth finger in an AI-rendered hand, Apple’s policies for 
> [Distributing apps in the U.S. that provide an external purchase 
> link](https://developer.apple.com/support/storekit-external-entitlement-us/) are startlingly graceless and a jarring, but not 
> surprising, reminder that Apple is not a real person and not 
> worthy of your love.


[I wrote yesterday](https://daringfireball.net/2024/01/coming_to_grips_with_apples_seemingly_unshakable_sense_of_app_store_entitlement) about Apple damaging their brand and reputation with this policy. I’m friends — close friends, in many cases, perhaps [especially](https://daringfireball.net/search/vesper+brent+simmons) in Brent’s case — with many longtime indie Mac developers. I’m up to at least half a dozen instances now where group chat discussions have turned to concerns that Apple might assert the same demand for a 27 percent cut of all Mac software. Meaning not just apps in the Mac App Store, but apps from outside the Mac App Store — even apps that are *only* available outside the Mac App Store. Even apps from developers who don’t have any apps in the Mac App Store. There’s now genuine concern that Apple is going to declare that they want a 27/12 percent revenue cut from all Mac software, full stop.


I’m disappointed by Apple’s decision to demand their commission from sales on the web linked from within iOS apps, but not surprised. But I can’t emphasize enough how flabbergasted many developers are — nor how offended. (Brent was too polite to point out that Apple’s external links policy is also a proverbial third finger.)


Prior to MacOS 10.12 Sierra, MacOS had three options in the Security & Privacy panel of System Preferences (as it was [then named](https://daringfireball.net/2022/06/basic_app_guy_mac_settings)1) for the sources of apps permitted to run: “App Store”, “App Store and identified developers”, and “Anywhere”. *Identified developers* means apps from outside the App Store that are cryptographically signed by both Apple and a developer with an Apple developer account. Starting with 10.12 Sierra, [the “Anywhere” option was removed](https://512pixels.net/projects/aqua-screenshot-library/macos-10-12-sierra/#jp-carousel-16675). You can still re-enable the ability to run unsigned software, but [you need to run an administrator-authenticated command](https://macpaw.com/amp/how-to/allow-apps-anywhere) in Terminal (`sudo spctl --master-disable`).


So, practically speaking, commercial Mac software must be signed, and Apple controls signing. That means Apple *could*, technically, attempt to demand such a commission (along with the arduous monthly accounting of sales, and the profoundly intrusive option to demand an audit at any time).


I am convinced that Apple has no such intention. I think I understand how Apple views iOS (including its sibling derivatives iPadOS, tvOS, and now VisionOS) as an altogether different type of platform than the Mac. If it were up to Apple, the External Purchase Link Entitlement on iOS wouldn’t exist, because they’re only allowing external purchase links in apps because a court decision demanded it — and thus isn’t an indication of what they want to do with the Mac. The general-purpose-computing flexibility and power of the Mac is *necessary*, not just *nice to have*, or *the way things have always been*.


Back in 2010, when the iPad was just six months old (and ran “iOS”), I wrote a piece titled “[The Future of the Mac in an iOS World](https://daringfireball.net/2010/12/future_of_the_mac_in_an_ios_world)”. The whole thing holds up and is worth a re-read (or first read, if you didn’t read it then). But I’ll quote the nut of it here:


> For all the aforementioned growth in Mac sales — remarkable by 
> any measure, but especially so for a 25-year-old platform — the 
> iPad, just six months old, is already outselling the Mac. Here’s 
> the short version of the “Mac is doomed” scenario: iOS is the 
> future, Mac OS X is the past, and Apple, unlike most major tech 
> companies, is strongly inclined to abandon the past in the name of 
> the future. 
> You can’t really argue with that, can you? But the premise that 
> the end is near for the Mac presupposes quite a bit about the 
> near-term future of iOS. [...] 
> The central conceit of the iPad is that it’s a portable computer 
> that does less — and because it does less, what it does do, it 
> does better, more simply, and more elegantly. Apple can only begin 
> phasing out the Mac if and when iOS expands to allow us to do 
> everything we can do on the Mac. It’s the heaviness of the Mac 
> that allows iOS to remain light. 
> When I say that iOS has no baggage, that’s not because there is 
> no baggage. It’s because the Mac is there to carry it. Long term — say, ten years out — well, all good things must come to an 
> end. But in the short term, Mac OS X has an essential role in an 
> iOS world: serving as the platform for complex, 
> resource-intensive tasks.


If there’s one thing I wish I had added to that description of the Mac’s essential role in the entire Apple ecosystem, it’s that it’s also *the* platform for whatever software developers can imagine and build, with no limits or rules other than the APIs — public or private — available in the system itself. And the only mistake I made in that column was thinking the Mac might have then only had a 10-year window of relevance remaining. The Mac today, at 40 years old,2 is if anything stronger and more essential than it was at 25. The move from Intel to Apple silicon is proof to my mind that Apple remains fully committed to the Mac. I now think it’s a forever platform, where *forever* is at least as far into the future as I can imagine. Decades, plural.


Essential to the Mac’s continuing relevance is that it is continuously evolving. Much has changed since 2010, and much will surely change between now and the Mac’s 50th anniversary in 2034. But one thing that can’t change without destroying it is its openness to software outside Apple’s control. The Mac is a PC. The others, to borrow a term, are post-PC devices. I am convinced that every executive at Apple who needs to understand that does, and that a scheme along the lines of iOS’s [External Purchase Link Entitlement](https://developer.apple.com/support/storekit-external-entitlement-us/) has never even been *considered* for the Mac. Everyone I know at Apple, from the trenches to the executive ranks, *loves* the Mac. Most of them went to work at Apple because of the Mac. They know that the Macintosh without Adobe, without Microsoft, without the indie developers who craft software that can only exist outside the Mac App Store, wouldn’t be the Macintosh at all. And there’s zero chance Adobe, Microsoft, or any of the indie shops I know would agree to *any* sort of mandatory revenue share, let alone a hefty one.3


But I don’t sell Mac software. Among those who do, not only do they not share my confidence that Apple would do no such thing — they’re genuinely concerned that it might be inevitable. “You don’t need a weatherman to know which way the wind blows” is one of Bob Dylan’s best lines, and this week’s External Purchase Link Entitlement policy for iOS is a gust of foul-smelling wind so strong it demands a weather advisory.


Developer uncertainty regarding the viability of selling Mac software is the last thing needed for a platform that is already facing a dearth of new original native software. Apple doesn’t have to make a platform-destructive money-grab policy change to ruin the Mac. They can ruin it simply by planting the seed of doubt that they *might*.


---

1. Not only has System Preferences been renamed (and redesigned) as Settings, the panel then called “Security & Privacy” is now “Privacy & Security”. Details. ↩︎︎
2. Lost in the hubbub surrounding the imminent launch of the Vision spatial computing platform is the fact that the Mac’s 40th anniversary comes next week, Wednesday January 24. I am to understand that this anniversary will be celebrated by Apple [much like the Mac’s 30th was](https://techcrunch.com/2014/01/24/apple-reflects-on-the-mac-at-30-with-new-video-and-website-retrospective/), and that Apple might also use the occasion to reveal its compliance plans for the E.U.’s Digital Markets Act, which comes into effect March 7.  ↩︎
3. I am heartened too by [Apple’s avowed interest in reinvigorating AAA gaming on the Mac](https://www.inverse.com/tech/mac-gaming-apple-silicon-interview) in the Apple silicon era. Sure, they’d love for all the best Mac games to be in the Mac App Store, but they must know that just as with productivity apps, some PC game publishers are only willing to sell directly to customers. That’s not to mention the essential role of third-party game stores like [Steam](https://store.steampowered.com/). The Mac’s chances of becoming a serious gaming platform may well be slim, but those chances would be nil — zilch, zero, non-existent, nada — in a world where Apple attempted to extract console-like sales commissions from Mac software outside the App Store. Executives at Apple might be greedy, but they’re not stupid. ↩︎︎



| **Previous:** | [Coming to Grips With Apple’s Seemingly Unshakable Sense of Entitlement to Its Commissions From Third-Party iOS Apps](https://daringfireball.net/2024/01/coming_to_grips_with_apples_seemingly_unshakable_sense_of_app_store_entitlement) |
| **Next:** | [Apple’s Plans for the DMA in the European Union](https://daringfireball.net/2024/01/apples_plans_for_the_dma) |


PreviousNext