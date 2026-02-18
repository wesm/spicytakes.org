---
title: "Charger Nerdery"
date: 2020-12-31
url: https://daringfireball.net/2020/12/charger_nerdery
slug: charger_nerdery
word_count: 953
---


Joe Rossignol, MacRumors, “[HomePod Mini Now Works With Select 18W Chargers Following 14.3 Software Update](https://www.macrumors.com/2020/12/28/homepod-mini-update-adds-18w-charger-support/)”:


> As noted in [a Reddit thread](https://www.reddit.com/r/HomePod/comments/klmdoj/since_homepod_mini_can_do_18w_now_i_can_use_my/) spotted [by The 8-Bit](https://the8-bit.com/homepod-software-14-3-secretly-added-support-for-charging-through-18w-adapters/), and
> confirmed by MacRumors, the HomePod mini now works with Apple’s
> own 18W USB-C power adapter and select third-party 18W power
> adapters from brands like Aukey. One user was even able to power
> the HomePod mini with an 18W battery pack from Cygnett, allowing
> for portable use.
> Previously, when attempting to use the HomePod mini with a power
> adapter rated below 20W, the speaker would simply display an
> orange light and not function. This may still be the case with
> certain 18W power adapters, as certain power profiles may be
> required.


If you don’t know a little about how AC adapters work, it might seem crazy that the difference between an 18W charger and 20W charger could be significant. If you think it’s all about wattage, they sound so similar — how could 2 watts make a difference? And Apple’s own 20W charger (that they started selling this year, and which is included with the HomePod Mini) looks identical to Apple’s previous 18W charger (which was included with some iPads and the iPhones 11 Pro). The only way to tell Apple’s new 20W charger apart from their old 18W charger is to look at the hard-to-read small print (light gray text on a white background, a veritable crime against accessibility). And even when you read the small print, you have to know that [Apple’s 20W chargers say “20W” on them and their 18W chargers aren’t labeled with a wattage](https://daringfireball.net/misc/2020/10/apple-18w-20w-adapters.jpeg). Seriously, Apple’s 18W charger doesn’t say “18W” — the only way to know it’s an 18W charger is to examine the even-harder-to-read smallest-of-small print and know or calculate that its stated maximum output of “9V × 2A” is 18W. (Their 20W charger is 9V × 2.2A, so it’s really a 19.8W charger.)


So on the one hand, because the HomePod Mini includes the 20W charger, it was fine that it didn’t work with the old 18W charger. But on the other hand, if you ever toss the 20W charger into a bag or drawer along with an Apple 18W charger, you needed an extraordinary amount of knowledge to know which charger the HomePod Mini required. Not sure how much work Apple had to put into the 14.3 software update to make the HomePod Mini work with the 18W charger too, but I’m glad they did. It’s too confusing otherwise.


---


This exact same sort of confusion — conflating two lookalike Apple-branded chargers — bit me earlier this year. [In my April review of the iPad Magic Keyboard](https://daringfireball.net/2020/04/the_ipad_magic_keyboard#miscellany), I originally wrote that passthrough charging via the Smart Connector was slow. But other reviewers saw passthrough charging speeds that were as fast or nearly as fast as connecting the iPad directly to the charger. I checked with Apple and they confirmed that passthrough charging should not be slow, and I should make sure I was using the power adapter that came with the iPad Pro.


My mistake was using Apple’s slightly older 29W USB-C power adapter, [which looks exactly like Apple’s more recent 30W USB-C power adapter](https://support.apple.com/en-us/HT201700#usbc). We’ve had that adapter plugged into our kitchen island for years, and it’s never before mattered. But with the Magic Keyboard, it did.


Turns out Apple’s 29W USB-C adapter is weird and limited. It only outputs two configurations: 14.5V × 2A = 29W (the maximum), or 5.2V × 2.4A = 12.48W.1 For high-power input, the iPad Magic Keyboard accepts 9V × 3A = 27W, but Apple’s 29W adapter can’t supply that. Apple’s 30W USB-C adapter, on the other hand, supplies a slew of output options:

- 20V × 1.5A = 30W
- 15V × 2A = 30W
- 9V × 3A = 27W (bingo for the Magic Keyboard)
- 5V × 3A = 15W


So the 29W adapter *looks* exactly like the 30W adapter, and if you make the perfectly reasonable but totally wrong assumption that the stated maximum wattage is all that matters, it *sounds* like it’s about 97% as powerful (29 ÷ 30), but what really matters when an adapter is negotiating with a device are the various voltage/amp configurations that the charger can supply as output, and the device can accept as input.


Plug the iPad Magic Keyboard into an Apple 30W adapter and the adapter can supply it with 27W (9V × 3A). Plug the Magic Keyboard into Apple’s 29W adapter, however, and the best output the charger can supply that the keyboard will accept is a measly 12.48W (5.2V × 2.4A). That closely jibes with [my own observed estimate back in April](https://daringfireball.net/2020/04/the_ipad_magic_keyboard#miscellany), that the iPad Pro only charges at about 40 percent speed via passthrough when the Magic Keyboard is plugged into Apple’s 29W charger.


That 29W charger now lives in a drawer with a salty note attached.


---

1. I’m oversimplifying here. [Kevin van Haaren, on Twitter](https://twitter.com/kvanh/status/1344760791417954314), before I added this footnote: “It isn’t correct to say a charger outputs ‘14.5V × 2A’. The amp rating is a maximum and is dictated by what the device draws. So a 14.5V × 2A charger supports all 14.5V devices that draw up to 2A, it supports 14.5V × 1A just fine.” My simplification of *volts times amps equals watts* is about maximum charging speeds, not minimal compatibility. My thinking is that you don’t need to worry about whether your stuff will charge at all, but whether it’s going to charge as fast as it should. ↩︎



| **Previous:** | [Facebook’s Unknowable Megascale](https://daringfireball.net/2020/12/facebook_unknowable_megascale) |
| **Next:** | [Incoming CEO of a Sand-Polishing Company in Oregon Makes Curious Remark](https://daringfireball.net/2021/01/incoming_ceo_of_a_sand-polishing_company_in_oregon_makes_curious_remark) |


PreviousNext