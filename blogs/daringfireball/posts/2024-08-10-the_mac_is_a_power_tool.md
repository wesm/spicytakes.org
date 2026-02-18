---
title: "The Mac Is a Power Tool"
date: 2024-08-10
url: https://daringfireball.net/2024/08/the_mac_is_a_power_tool
slug: the_mac_is_a_power_tool
word_count: 1343
---


Back in the day, on classic Mac OS, there were no “privileges” for software. If you launched an app, or installed a system extension, that software just did what it wanted. Something as ([seemingly](https://tidbits.com/1992/07/06/disinfectant-2-9-released/)) innocuous as a game or as necessarily powerful as a disk formatting utility just ... ran. If that disk utility had a bug that overwrote every byte of your startup disk with zeroes, well, tough luck. If you were unfortunate enough to install malicious software that spread like a virus, well, even tougher luck. That sounds awful, but in practice, it was fine. I’ve been using a Mac since 1991 and I don’t recall ever once — not once — having a problem with malware or scamware.1


That was a long time ago.


Such a laissez-faire approach to software privileges obviously wouldn’t fly today. I want most applications on my Mac to run within a sandbox. I want applications to require explicit permission to access the camera and microphone, or to capture the content of my display. I want applications to be cryptographically signed by known developers and notarized by Apple by default. But I also want to be able to grant trusted applications non-sandboxed access to my entire file system, access to cameras and microphones, and the ability to capture my screen.


I posted a [spate](https://daringfireball.net/linked/2024/08/07/macos-15-sequoia-weekly-permission-prompts) [of](https://daringfireball.net/linked/2024/08/07/mac-os-15-sequoia-gatekeeper) [links](https://daringfireball.net/linked/2024/08/08/snell-mac-permission-balance) this week about how the anti-malware/anti-scamware protections in MacOS are increasingly crossing the line from “this is a reasonable balance” to “this is infuriating”. It really is turning into [exactly what Apple once mocked](https://www.youtube.com/watch?v=FxOIebkmrqs).


The Mac is a platform where you need to be able to shoot yourself in the foot. Increased protections that make it less likely that you’ll shoot yourself in the foot are, obviously, a good idea. Many of them are downright necessary. But such protections are only undeniably good ideas when they don’t get in the way of sophisticated users using software that requires a high level of system privileges. Then they become a trade-off. There are some power users who’ve been annoyed every step of the way as Apple has increased such protections in MacOS, but I think, until recently, Apple has managed this balance well. MacOS, on the whole, has been welcoming and safe for unsophisticated users while remaining powerful and efficient for experts. But in recent years MacOS has clearly started slipping down the slippery slope of being too protective.


It’s good to be reminded of the software you have installed that requests, or outright requires, access to private data and sensitive hardware APIs. It’s very good to be alerted to any software you might have installed that has acquired such permissions without your knowledge or recollection. (Like, say, if an abusive partner has installed some sort of monitoring software unbeknownst to you.) But it’s infuriating to play whack-a-mole to dismiss a barrage of permission prompts to confirm the same permissions you’ve previously granted to the same software, and it’s even worse when you need to dig three or four levels deep into System Settings to do it.


Consider real-world power tools. No one wants to get hurt. For sure, no one wants to lose a finger. But serious tool users still have holes to drill, wood to cut, and nails to hammer. There’s a [fascinating saga](https://www.motherjones.com/politics/2013/05/table-saw-sawstop-safety-finger-cut/) around the company [SawStop](https://www.sawstop.com/), which invented a technology for table saws that uses capacitive sensors to prevent saws from slicing through fingers (or, say, for demo purposes, [hot dogs](https://www.youtube.com/watch?v=fq3o0VGUh50)). As of a decade ago, in the U.S. alone, over 4,000 fingers were sliced off in table saw accidents annually. That’s a lot of fingers. SawStop’s technology prevents almost all such accidents. But also: *it doesn’t make table saws worse for cutting wood*. The company [has a FAQ about cutting wet or “green” wood](https://www.sawstop.com/sawstop_faq/will-cutting-green-or-wet-wood-activate-the-sawstop-safety-system/):


> SawStop saws cut most wet wood without a problem. However, if the
> wood is very green or wet (for example, wet enough to spray a mist
> when cutting), or if the wood is both wet and pressure treated,
> then the wood may be sufficiently conductive to activate the
> brake. If you are unsure whether the material you need to cut is
> conductive, you can make test cuts using Bypass Mode to determine
> if it will activate the safety system’s brake. The red light on
> the control box will flash to indicate conductivity. If the
> material is conductive, you can choose to operate the saw in
> Bypass Mode which will disengage the saw’s safety system’s brake
> feature and allow you to continue cutting the material.


This sounds like exactly the right balance for MacOS — a balance MacOS until recently had achieved. Safety by default, but don’t get in the way of power users doing their jobs. And when the user needs an override for the safety features, there is an override, and the situation will make clear to the user that needing to use the override is justified by the safety concerns. MacOS is veering into the territory of power users needing to flip override switches *all the time*.


At the two extremes of the Mac’s user base are gullible technically unsophisticated naifs, and skeptical expert power users. It’s fair for Apple to present *some* protections that aren’t necessary for expert power users, in the name of bolstering the guardrails for the technically unsophisticated. But at a certain point, a hammer needs to hammer whatever it strikes, and sometimes, alas, that’s the user’s thumb. That’s the Mac. It’s a Unix workstation that’s friendly enough to be used by the mass market. It is not an appliance intended to prevent any possible malware or scamware from running.


Apple makes such appliances. They run iOS. I’d go so far as to say that one problem facing the Mac has nothing to do with the Mac itself but instead is a downstream effect of the iPad’s weaknesses. I believe in the 1984 slogan that the Mac is “the computer for the rest of us”, where “the rest of us” is very much inclusive of non-expert users. But there’s a certain point of unsophistication and [okey-doke](https://greensdictofslang.com/entry/fksqmty) gullibility where the Mac becomes an inappropriate platform for some users. There are many construction-professional power tools that shouldn’t be used by non-expert users, too.


Computers are such an essential part of the modern world — and almost everyone’s daily lives — that computers-that-work-like-computers aren’t for everyone. The world needs locked-down can’t-cut-your-fingers-off-no-matter-what-you-do platforms like the iPad. And Apple sells significantly more iPad units than Macs. But any Mac user who isn’t sufficiently served by the anti-malware/scamware protections already in MacOS shouldn’t be using a Mac at all. They should be using iPads, or something else similarly locked-down, instead. Some of these users are using Macs instead of iPads out of ignorance. Their technical needs could be met by an iPad but they don’t know it. (They are, by definition, technically unsophisticated.) But surely some of them know they’d prefer to be using an iPad instead of a Mac but can’t, because an iPad can’t do one or more things they need to do, or run software they need to run.


Power tools and user-safety features aren’t mutually exclusive. But they need to be in balance. Apple is clearly [losing that balance](https://sixcolors.com/post/2024/08/apples-permissions-features-are-out-of-balance/) with MacOS, and I think a big part of that is the iPad’s weaknesses tipping the scale.


---

1. That viruses, malware, and scamware weren’t significant problems for classic Mac OS users doesn’t mean such things didn’t exist. There was, in fact, a spate of viruses in the [late 1980s](https://en.wikipedia.org/wiki/ANTI_(computer_virus)) and [early 1990s](https://tidbits.com/1990/10/01/anti-b/), which were splendidly addressed by a freeware anti-virus system extension called [Disinfectant, by John Norstad](https://en.wikipedia.org/wiki/Disinfectant_(software)). But on the whole, the entire two-decade era of classic Mac OS passed without much malware. Part of that was by design, part by security-through-relative-obscurity, and part, perhaps, by good luck. ↩︎



| **Previous:** | [Apple’s Profits From Services Are on the Cusp of Surpassing Its Profits From Device Sales](https://daringfireball.net/2024/08/apple_services_profit) |
| **Next:** | [The iOS Continental Drift Widens](https://daringfireball.net/2024/09/the_ios_continental_drift_widens) |


PreviousNext