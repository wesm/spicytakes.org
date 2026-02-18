---
title: "The Ins and Outs of Snow Leopard"
date: 2008-06-08
url: https://daringfireball.net/2008/06/ins_and_outs_of_snow_leopard
slug: ins_and_outs_of_snow_leopard
word_count: 738
---


Here’s what I expect regarding “Snow Leopard”, the in-progress version of Mac OS X 10.6 which I expect Apple to announce in some fashion tomorrow at WWDC.


## Dropping PowerPC Support


This is not going to be popular, and it does seem too soon, but my sources indicate that it is the case. Why would Apple do this, when it is clearly going to antagonize owners of late model PowerPC hardware? A few factors: (a) Snow Leopard won’t ship until next year, at which point even the newest PowerPC Macs will be at least three years old; (b) dropping PowerPC would significantly simplify the development and QA testing for Snow Leopard; and (c) perhaps Apple will present technical merits, i.e. that by dropping PowerPC support, they’re able to implement certain performance improvements that can only work on Intel hardware.


## 64-Bit


64-bit support is a talking point for Snow Leopard, but I *do not* believe it means Apple is dropping 32-bit support from the OS. For one thing, many Intel-based Macs (those based on the older Core Duo, as opposed to the Core 2 Duo) don’t even support 64-bit. Dropping PowerPC support would be aggressive; dropping support for 18-month-old Intel machines would be insane.


Plus, unlike PowerPC, 32-bit support isn’t weighing down the 64-bit support in OS X — I’m not aware of a single good reason why Apple would even consider dropping 32-bit support, and there are thousands of good reasons not to (to wit, the thousands of 32-bit Mac apps already in existence).


## ‘100 Percent Pure Cocoa Apps’


That’s a phrase that is circulating leading up to WWDC, regarding the supposed outline for tomorrow’s keynote. Some have interpreted it as meaning that the Carbon APIs will be dropped from Snow Leopard. I don’t buy that. Last year Apple dropped 64-bit Carbon from Leopard, clearly a sign that the Cocoa side of the aisle is where Apple’s attention lies. But dropping a planned future feature like 64-bit Carbon is a far cry from dropping Carbon completely.


Even if you consider no apps other than Microsoft’s and Adobe’s, a Carbon-less Mac OS X 10.6 doesn’t seem feasible. If you thought it was bad when Photoshop and Excel only ran under Rosetta, imagine if they didn’t run at all. Crazy talk.


My interpretation of the “100 percent pure Cocoa apps” line is that it’s an admonition for developers — not that they *must* use “pure” Cocoa APIs for their apps, but that they *should*, that there are performance and efficiency benefits to doing so that will not be available in other APIs. (Perhaps something to do with the LLVM compiler architecture? Optimizations to the Cocoa libraries to offload more computation to the GPU “for free”?)


## Multi-Touch


This stuff with multi-finger gestures on this year’s MacBook trackpads is not multi-touch, at least in the iPhone sense. The marvel of the iPhone UI is the touch screen. I don’t expect to ever see touchscreen Macs. Touchscreen computers from Apple running OS X? Yes, I think, probably someday soon. But not *Mac* OS X. The user interface simply isn’t designed or optimized for it. Adding touchscreen support to a user interface designed for traditional mouse-and-keyboard access is a lipstick-on-a-pig design (cf. recent demos from Microsoft of Windows 7).


## The ‘No New Features’ Thing


Major version upgrades, whether for an application or an entire operating system, have traditionally been about adding new features, not improving existing ones. Why? Because new features are what people pay for. So how could Jobs sell this no-new-features idea in the keynote? One way would be by not selling anything, and announcing that Snow Leopard will be a free (or inexpensive) update.


But I can see it being sold another way. The appeal of Mac OS X versus Windows is what? That it has more features? No. It’s that it is more elegant, simpler, more efficient, and more reliable. So I can imagine Jobs on stage announcing that Apple has assigned their best engineers to a year-long project to focus on just those things. Vista may or may not be getting an unfair rap in the press, but the public perception is that these are exactly the areas where Vista is most disappointing. Apple could press their current advantage by emphasizing efficiency, elegance, simplicity, and reliability.



| **Previous:** | [‘Snow Leopard’ at WWDC](https://daringfireball.net/2008/06/snow_leopard) |
| **Next:** | [Twice as Fast, Half the Price](https://daringfireball.net/2008/06/twice_as_fast) |


PreviousNext