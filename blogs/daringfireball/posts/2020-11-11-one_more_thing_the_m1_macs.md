---
title: "One More Thing: The M1 Macs"
date: 2020-11-11
url: https://daringfireball.net/2020/11/one_more_thing_the_m1_macs
slug: one_more_thing_the_m1_macs
word_count: 1952
---


My basic theory, since the announcement during [this year’s WWDC keynote](https://developer.apple.com/videos/play/wwdc2020/101/) that Apple was — finally — moving the Mac platform from Intel’s x86 architecture to their own custom silicon, has been that they would not merely be using A-series chips for this. That Macs wouldn’t be sharing chips with iPhones and iPads. Apple *could* have gone this route, performance-wise, at least for the consumer grade devices, but the Apple Silicon segment of the WWDC keynote sounded to me like they were suggesting a far more ambitious endeavor. I was right. It’s the difference between using their amazing mobile chips in desktops, and using their chip expertise to design desktop-focused chips.


Apple billed [yesterday’s event](https://www.apple.com/apple-events/november-2020/) as “One More Thing”, and while they announced three new Macs, it really was about *one* new thing: the M1. The new M1-based MacBook Air, 13-inch MacBook Pro, and Mac Mini are best thought of not as three different computers, but rather three different manifestations of the same computer.


These are, by all accounts and measures, far faster machines than the Intel-based Macs they’re replacing. But the big win, and clear focus from Apple, isn’t speed but battery life. Apple’s quoted battery life times for [the Intel-based MacBook Air from March of this year](https://support.apple.com/kb/SP813?viewlocale=en_US&locale=en_US) for “wireless web browsing” and “Apple TV app movie playback” were [11 and 12 hours, respectively](https://support.apple.com/kb/SP813?viewlocale=en_US&locale=en_US). The [new M1 MacBook Air pushes those times](https://www.apple.com/macbook-air/specs/) to 15 and 18 hours. The difference is even more striking with Apple’s [specs for the new M1 MacBook Pro](https://www.apple.com/macbook-pro-13/specs/), which claim battery life of 17 and 20 hours for web browsing and movie playback. The current Intel-based 13-inch MacBook Pro gets just 10 hours on each of those tests. That’s very close to double the battery life. Double!


This is the sellable bullet point for the mass market consumer who has no idea what “Apple Silicon” means: battery life is now truly all-day. Charge your MacBook Air or Pro overnight, and you can use it hard all day without ever once being near a power outlet. You’re clearly intended to be able to use these new MacBooks like iPads in that regard — where *charging* them and *using* them are entirely different actions. There’s no question in my mind that Apple could have made this transition to Apple Silicon a few years ago, but they clearly wanted to wait until the advantages were overwhelming and undeniable. And nowhere is that more evident than with these figures for battery life.


[The M1](https://www.apple.com/mac/m1/) really is an entire system on a chip. *Everything* is on the M1. The various processors, of course: the CPU cores, the GPU cores, the Neural Engine cores. But everything else is on the M1 too: the storage controller, the Secure Enclave, the memory controller, and, yes, the memory itself. The DRAM for M1-based Macs is on the package (“on the substrate”, I believe, is the technical lingo).


The downside of this design is that DRAM is not something you can configure after the fact. But this has been true for Apple’s entire MacBook lineup, from consumer Airs to high-end 16-inch Pro models, for years. But with the M1, memory isn’t just soldered onto a board, it’s integrated into the SoC — just like it has been for A-series SoCs. Apple calls this “unified memory architecture”, [or UMA](https://www.apple.com/mac/m1/):


> M1 also features our unified memory architecture, or UMA. M1
> unifies its high‑bandwidth, low‑latency memory into a single pool
> within a custom package. As a result, all of the technologies in
> the SoC can access the same data without copying it between
> multiple pools of memory. This dramatically improves performance
> and power efficiency. Video apps are snappier. Games are richer
> and more detailed. Image processing is lightning fast. And your
> entire system is more responsive.


There’s no separate “video memory” and “system memory” — just memory. “Shared memory” and “integrated graphics” have gotten a bad name historically, because they signified cheap low-performance compromises. Apple’s chip team is really *proud* of this UMA system and the integrated GPU on the M1. It’s a design that increases performance and power efficiency.


These systems are, according to Apple’s stated numbers, fast. They’ve more than earned our trust on that. We know, for a fact, that the A14 chip in the iPhones 12 and new iPad Air is both faster and far more power efficient than all but the very highest end Intel and AMD x86 laptop chips. [AnandTech published a detailed comparison yesterday](https://www.anandtech.com/show/16226/apple-silicon-m1-a14-deep-dive) showing just that. And we also know that Apple has promised that the M1’s high-performance cores are faster than the A14’s — *and* the M1 has four high performance cores, while the A14 only has two.


So if the A14 clearly outperforms all but the latest and greatest x86 laptop chips — and holds its own even against those — it would be rather shocking if Apple’s boasting that the M1 is the fastest CPU on the market is *not* true.


The mind-blowing part of all this is that the M1 is only being used in Apple’s less expensive consumer Macs.


*Wait, wait, wait*, you might be saying, the MacBook Pro is *pro*. But as I’ve written numerous times, *pro*, in Apple’s product-naming parlance, doesn’t always stand for *professional*. Much of the time it just means *better* or *nicer*. The new M1 13-inch MacBook Pro is *pro* only in the way, say, AirPods Pro are. This has been true for Apple’s entry-level 13-inch MacBook Pros — the models with only two USB ports — ever since the famed [MacBook “Escape” was suggested as a stand-in for the then-still-missing retina MacBook Air four years ago](https://www.theverge.com/circuitbreaker/2016/10/27/13434046/new-apple-macbook-pro-air-announced-release-date-specs-price).


The new M1 MacBook Pro is the same basic computer as the M1 MacBook Air, but adds:

- Brighter screen (500 nits vs. 400)
- Bigger battery (58 watt-hours vs. 50)
- Fan (increasing thermal headroom)
- Better speakers and microphones
- Touch Bar
- 0.2 pounds of weight (3.0 pounds vs. 2.8 — not much)


The M1 13-inch MacBook Pro will outperform the MacBook Air in sustained performance, not because it has a better CPU or GPU, but because it has a fan that allows the high performance cores to run faster for longer stretches. (The M1 Mac Mini has even more thermal headroom, because it’s a bigger enclosure and isn’t battery-powered, and thus is the fastest machine of the three. But because it isn’t battery powered, it seemingly has the fewest advantages over its equivalent Intel predecessor.) Also noteworthy: the $999 entry-level MacBook Air only has 7 GPU cores, not 8. It’s logical to conclude that this is the result of [chip binning](https://www.tomshardware.com/reviews/glossary-binning-definition,5892.html), but Apple, unsurprisingly, has no comment on the matter.


But fundamentally these are the same two MacBooks — the Pro version just has a bit more *oomf* thanks to its cooling system. And the M1 Mac Mini is just the same computer in a desktop enclosure.


The fact that these machines all share the same limitations, as well — a maximum of 16 GB of RAM and 2 TB of SSD storage — is not in any way an indication that Apple is regressing an iota on professional memory and storage needs. Intel-based 13-inch MacBook Pros [support up to 32 GB of RAM and 4 TB of storage](https://support.apple.com/kb/SP819?viewlocale=en_US&locale=en_US). Intel Mac Minis [support up to 64 GB of RAM](https://support.apple.com/kb/SP782?viewlocale=en_US&locale=en_US). And then there’s the 16-inch MacBook Pro, which [supports up to 64 GB of RAM and *8* TB of SSD storage](https://support.apple.com/kb/SP809?viewlocale=en_US&locale=en_US).


The only Intel-based Macs that have been completely replaced by M1 models are the MacBook Airs — the Intel models of which have never offered specs of any kind that aren’t met or exceeded by the new M1 models. Apple continues to sell Intel-based 13-inch MacBook Pros and Mac Minis. That doesn’t betray a lack of confidence in Apple Silicon; it’s simply the result of the M1 only being intended for “low-power systems or small size and power efficiency”, per Apple’s keynote. Apple hasn’t yet unveiled its professional-grade M-series chips. (I’m guessing “M1X” as the name for the first *high*-power Mac SoC. The “M2”, when you think about it, would be the name of the next-generation SoC for MacBook Airs and lower-end MacBook Pros and Mac Minis. And I’m thinking the Mac Pro and iMac Pro might get their own series of SoCs, say, the “X1”.)


I don’t know if the upcoming higher-end Apple Silicon MacBook Pros are going to include four USB/Thunderbolt ports — this *is* the company that sold a 12-inch semi-premium-priced MacBook with just one port for years — but I’m damn certain that they’ll support more than 16 GB of RAM and 2 TB of storage. My sincere, and I think technically reasonable, hope is that the 13-inch high-end MacBook Pros will reach spec-parity with the 16-inch models, supporting up to 64 GB of RAM and 8 TB of SSD storage, and perhaps offering equivalent graphics performance. But 32 GB of RAM and 4 TB of storage in future Apple Silicon-based 13-inch MacBook Pros should be considered a given.


What Apple announced yesterday was *an* Apple Silicon-based MacBook Pro, not the *only* Apple Silicon-based MacBook Pro. And I would bet that future high-end configurations *will* have four USB/Thunderbolt ports — two on each side — as well.


## Addenda

- Initial coverage of Apple’s M1 announcement [in the greater tech sphere](https://www.techmeme.com/201110/p28#a201110p28) — the cross-platform perspective, if you will — seems to tend to place the Mac’s transition to Apple Silicon in the same context as ARM-based Windows laptops. I think that’s the wrong way to look at it — and it’s only going to lead to bad assumptions right out of the gate. Apple Silicon is in an entirely different class than the ARM chips from companies like Qualcomm, with a phone-focused background. Asking if M1 Macs are going to face the same problems as ARM-based Windows laptops is like asking if Teslas are going to hit the same limits as electric scooters. ARM-based Windows PCs necessitate significant trade-offs — you get high efficiency and small form factors, but you lose performance and suffer from severely limited software compatibility. The promise of Apple Silicon is that Mac users get higher performance, longer battery life, *and* lots of native software and high-performance compatibility with legacy software thanks to [Rosetta](https://developer.apple.com/documentation/apple_silicon/about_the_rosetta_translation_environment). It’s like having your cake, eating it too, *and* getting to share your cake with your friends.
- Apple remains more enamored with the Touch Bar than many Mac enthusiasts are. There are a lot of Mac users who *despise* the Touch Bar, but if you want an M1 MacBook with a fan, your only choice is the MacBook Pro. There is no M1 MacBook with a fan but without a Touch Bar — and a lot of people would buy one if there were.
- The new M1 Mac Mini is only available in Silver. The current Intel Mac Mini that remains available for sale is only available in Space Gray.
- No touchscreen support in these initial Apple Silicon Macs, which is exactly as I both expected [and hoped](https://twitter.com/gruber/status/1326236328019759104). However, this is a disappointment and seemingly a surprise [to others](https://twitter.com/ditheringfm/status/1326545401936187401). There are certainly elements of Big Sur that look more iOS-y, no question, but I don’t know why so many people think they look designed for touch. They don’t and they aren’t — and, says me, they shouldn’t be.


The bottom line is that for over a decade, iPhones and iPads have had Apple-designed chips the competition could not and still cannot match. Now the Mac does too.



| **Previous:** | [The iPhone 12 Mini and iPhone 12 Pro Max](https://daringfireball.net/2020/11/the_iphone_12_mini_and_iphone_12_pro_max) |
| **Next:** | [The HomePod Mini](https://daringfireball.net/2020/11/the_homepod_mini) |


PreviousNext