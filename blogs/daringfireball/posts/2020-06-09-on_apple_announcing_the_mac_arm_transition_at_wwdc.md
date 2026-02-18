---
title: "On Apple Announcing the ARM Mac Transition at WWDC This Month"
date: 2020-06-09
url: https://daringfireball.net/2020/06/on_apple_announcing_the_mac_arm_transition_at_wwdc
slug: on_apple_announcing_the_mac_arm_transition_at_wwdc
word_count: 1662
---


[Mark Gurman](https://www.bloomberg.com/news/articles/2020-06-09/apple-plans-to-announce-move-to-its-own-mac-chips-at-wwdc):


> The company is holding WWDC the week of June 22. Unveiling the
> initiative, codenamed Kalamata, at the event would give outside
> developers time to adjust before new Macs roll out in 2021, the
> people said. Since the hardware transition is still months away,
> the timing of the announcement could change, they added, while
> asking not to be identified discussing private plans.


I’m not sure what the hedging is about there, other than the fact that *anything* reported about anyone’s future plans could, in theory, change. If ARM-based Macs are coming in 2021, and by all accounts they are, Apple almost *has* to announce them at WWDC.


I know there are some folks who think Apple might simultaneously announce the transition while unveiling ARM-based Macs for immediate availability, but that just doesn’t make much sense. If Apple could do it that way, they would, because they do like surprises and they do not like pre-announcing future products ([a lesson recently relearned the hard way](https://daringfireball.net/linked/2019/03/29/airpower-canceled)), but developers need time to get Mac apps ready. Some developers — the smart ones — are effectively ready to go, and will be able to recompile their apps for ARM as soon as Apple makes a new version of Xcode available. But others will need time. I mean just look at all the consternation this past year over MacOS 10.15 Catalina [dropping support for 32-bit software](https://tidbits.com/2019/09/18/moving-to-catalina-keep-your-32-bit-mac-apps-running-with-parallels/) — a transition Apple announced [several years in advance](https://support.apple.com/en-us/HT208436). I don’t think the transition from x86 to ARM will be nearly as rocky as the 32-bit to 64-bit transition, but for some apps it will take time. (Really, the deprecation of 32-bit software was the first step of a multi-year transition to 64-bit ARM software on all platforms.)


Gurman:


> At WWDC in 2005, Steve Jobs announced a move from PowerPC to
> Intel, and Apple rolled out those first Intel-based Macs in
> January 2006. Like it did then, the company plans to eventually
> transition the entire Mac lineup to its Arm-based processors,
> including the priciest desktop computers, the people said.


There’s been some reasonable speculation that Apple might use ARM chips only for portable Macs and consumer desktops, and stick with high-end Intel chips for pro desktops, but I think that’s simply based on our never having seen Apple even *try* its hand at high-performance chips. If you’re going to switch, switch.


If you want to see how this is going to play out, just [rewatch Steve Jobs’s 2005 announcement of the PowerPC-Intel transition](https://www.youtube.com/watch?v=ghdTqnYnFyg&feature=share). As [I wrote](https://daringfireball.net/linked/2018/11/06/jobs-powerpc-intel) back in 2018, it’s uncanny how similar the explanation could be: Apple’s in-house ARM-based chips offer vastly superior performance-per-watt compared to Intel’s, and Apple has ideas for future Macs that they can’t build without that superior performance-per-watt. *All* computers benefit from superior performance-per-watt, not just portables. That was the story in 2005, and it should be the story in 2020.


There are other reasons too. It’s cheaper for Apple to make its own chips than to buy Intel’s. They already make [a $400 iPhone that out-benchmarks a $3,000 top-of-the-line MacBook Pro](https://daringfireball.net/2020/04/the_2020_iphone_se) in single-core CPU performance. That’s bananas when you think about it. And there is a cross-platform developer story. With one consistent set of system-on-a-chip designs, all software for all Apple platforms can target the same Metal APIs for the GPUs, and the same Neural Engine APIs for machine learning and AI tasks.


The rumor mill currently leaves some big questions unanswered, though:


## Emulation?


Will ARM Macs run older x86 software via emulation? Apple shipped [a rather amazing emulator](https://en.wikipedia.org/wiki/Mac_68k_emulator) in the transition from Motorola 680x0 chips to PowerPC in the 1990s, and again in the 2000s with the PowerPC to Intel transition ([Rosetta](https://en.wikipedia.org/wiki/Rosetta_%28software%29)). There are seemingly no rumors one way or the other regarding emulation for the Intel-to-ARM transition. If I had to bet right now, I’d say no, there will be no x86 emulation on ARM Macs — and that factors into why Apple is pre-announcing this transition months ahead of releasing hardware. But that’s just my guess. In the 90s in particular, and the 2000s to a lesser degree, there was a lot of important third-party software that wasn’t easily ported. I don’t think that’s as much the case today.


## Developer Transition Hardware


In 2005 Apple made available [Developer Transition Kits](https://daringfireball.net/2008/04/big_fan) — Intel-based PC hardware housed in Power Mac cases. They “sold” them to developers for $1000 but under terms that required them to be sent back by the end of 2006; when developers returned the Developer Kits, they were [offered first-generation Intel iMacs](https://appleinsider.com/articles/06/01/11/apple_offers_transition_developers_free_imac_core_duo) to keep. (It was a good deal for developers.)


What’s the story on how developers will build and test ARM Mac software during this transition? I’ve seen a lot of people speculating that Apple will use iPad Pros for this. I don’t buy that (and in fact bet a friend a nice steak dinner that it won’t happen). Technically it seems possible, but iPad Pros only have 6 GB of RAM — no Mac has shipped with less than 8 GB in many years, and developers aren’t buying machines with 8 GB of RAM. Honestly, I think the RAM is a deal-breaker on the iPad Pro-as-ARM-Mac-dev-kit idea. Plus there are philosophical barriers. Even though they’re moving to the same chip platform, I think Apple sees iPads as iPads and Macs as Macs, and never the twain shall meet.1 A version of MacOS for iPad would be tantamount to shipping an official jailbreak kit for iPad in some ways. The whole notion just doesn’t feel like something Apple would do — it feels like something some users would *like* Apple to do. It feels wrong, for example, to run an OS without touchscreen support on a touchscreen tablet. And if you think or even just hope that part of this transition might include Apple adding touchscreen support to MacOS, that doesn’t strike me as something Apple would announce now — that’s something Apple would hold until it had actual touchscreen Mac hardware to unveil.


Basically, Apple likely wants ARM Mac developer transition hardware to be practical but boring. iPad Pros running MacOS would be neither.


My best guess would be Mac Minis or iMacs with ARM chips inside, rented rather than sold, like in 2005. Or maybe a MacBook? At this point, a MacBook might be the canonical generic form factor for developer hardware. There must be a lot of developers out there who’ve never bought a desktop Mac, and whose workspaces might not accommodate one.


## Boot Camp and Virtualization


What happens with [virtualization software](https://www.macworld.co.uk/feature/mac-software/best-virtual-machine-software-3671133/) like Parallels and VMware Fusion? The obvious answer is they emulate x86 or they go away. How will that perform? My understanding is that however good the performance of ARM chips is, the instruction set differences make it slow for ARM to emulate x86. This is no little thing — there are a lot of developers whose workflows depend on virtualization software.


Boot Camp is a related question — but one that’s entirely up to Apple to answer. Microsoft has a version of [Windows 10 for ARM PCs](https://support.microsoft.com/en-us/help/4521606/windows-10-arm-based-pc), so in theory, Boot Camp could continue to officially support booting Macs into Windows. Does Apple care enough to support that? I’d bet no — but it feels like a coin flip, given how many people have a professional need for it. Is Windows where the puck is going?


And if your interest in Boot Camp is for running games, support for Windows on ARM [almost certainly isn’t a great solution](https://www.zdnet.com/article/windows-10-on-arm-what-you-need-to-know-before-you-buy-a-surface-pro-x/).


## The Osborne Effect


What happens to current Intel-based Mac sales after Apple announces this big exciting transition months in advance? My guess: not much. Enthusiasts might wonder who would buy an Intel-based Mac after they’re essentially deprecated, but most people have no more idea what the difference is between Intel and ARM CPUs than they do 32-bit vs. 64-bit software. You might as well tell them you’re “switching from gizmos to widgets under the hood”.


I think the story is basically, again, [the same as the one from 2005](https://daringfireball.net/2005/06/bombs_away): “*Our current hardware is great and will be supported for many years to come; we’re making this transition for the future.*”


Today’s MacBook lineup is in fact in great shape: the Air and both sizes of MacBook Pro have been updated in the last six months, and they’re all good machines. The long-awaited Mac Pro is also new, and the Mac Mini is fine.


The iMac models and iMac Pro, however, are long in the tooth. The iMac Pro, in fact, has never been updated — [it’s 908 days old and counting](https://buyersguide.macrumors.com/#mac). Tipster Sonny Dickson claimed, just today, [that new iMacs are coming at WWDC](https://twitter.com/SonnyDickson/status/1270339867491184644):


> New iMac incoming at WWDC. iPad Pro design language, with Pro
> Display like bezels. T2 chip, AMD Navi GPU, and no more
> fusion drive.


As for the iMac Pro, maybe pro-level configurations get folded into one cohesive range of just-plain iMacs? Or, long in the tooth though it may be, perhaps the roadmap for iMac Pro is just “wait for ARM”.


---

1. It’s fun to think about iPads running MacOS and touchscreen MacBooks running iPadOS, but the names alone seemingly throw a monkey wrench in the idea. Although it’s worth noting that Apple used the PowerPC-to-Intel transition to rename PowerBooks to MacBooks. Names can change, and with Apple they often do. As weird as “MacBook” sounded at first, in hindsight it seems odd that until 2006 there had never been a Mac laptop with “Mac” in its name. The 16-pound (!) [Macintosh Portable](https://en.wikipedia.org/wiki/Macintosh_Portable) was definitely a Mac but only arguably portable. ↩︎



| **Previous:** | [Translation From VC-Backed PR Jargon to English of Magic Leap CEO Rony Abovitz’s Statement That He’s ‘Stepping Down’](https://daringfireball.net/2020/05/abovitz_magic_leap_translation) |
| **Next:** | [The Flimsiness of ‘Business vs. Consumer’ as a Justification for Apple’s Rejection of Hey From the App Store for Not Using In-App Purchases](https://daringfireball.net/2020/06/hey_app_store_rejection_flimsiness) |


PreviousNext