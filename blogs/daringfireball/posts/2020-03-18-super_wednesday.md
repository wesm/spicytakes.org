---
title: "Super Wednesday"
date: 2020-03-18
url: https://daringfireball.net/2020/03/super_wednesday
slug: super_wednesday
word_count: 2269
---


Big news drop today from Apple. Long story short:

- [New iPad Pros](https://www.apple.com/newsroom/2020/03/apple-unveils-new-ipad-pro-with-lidar-scanner-and-trackpad-support-in-ipados/). Same sizes and shapes (11 and 12.9 inches), faster CPUs and GPUs.
- iPadOS 13.4 — coming this Tuesday — will include full system-wide pointer support for mice and trackpads.
- A new $299 Magic Keyboard folio case for iPad Pros with an integrated trackpad and backlit keys.
- New MacBook Air. Storage has doubled, performance is much improved, and prices have dropped significantly.


Long story longer:


## Mouse and Trackpad Pointer Support in iPadOS 13.4


Above and beyond any of the hardware announcements, this is the most exciting news of the day for me. First, this is *not* the sort of feature one expects Apple to drop in a late-in-the-annual-cycle mid-March OS update. Clues suggesting serious mouse pointer support in iOS were gleaned from some sort of leak of iOS 14 (I presume, [from the way 9to5 Mac has written about it](https://9to5mac.com/2020/03/09/sophisticated-mouse-cursor-support-coming-to-ios-14-new-ipad-smart-keyboard-models-with-trackpad/), a device running an early build of iOS 14) but no one had any inkling this was coming *now*. (Steven Troughton-Smith came closest, [with this prescient tweet](https://twitter.com/stroughtonsmith/status/1239950345989693441) yesterday.)


This mouse pointer support is rich and deep — it is *far* more than a simplistic virtual finger tip, and far more thoughtful and graceful and direct than a port to iOS of Mac-style mouse cursors.


First, when just mousing around, the main cursor is a circle instead of an arrow. A circle feels right; an arrow would definitely feel wrong. Similarly, it would feel all wrong for the Mac to change its primary cursor from the arrow to a circle. For me it boils down to the *je ne sais quoi* of the fundamental differences between iPad and Mac.


When you hover over a tappable button, the pointer disappears and instead you get a hover-state highlight around the button. Hover over an app icon in the Dock or on your homescreen, and instead of seeing the mouse pointer on top of the icon, you see a highlight around the icon, much like the way icons are popped on tvOS. When text editing, the cursor changes to an I-beam, of course, but it’s an all-new I-beam cursor, not the one you get in iOS while using the on-screen keyboard as a virtual trackpad (after a tap-and-hold on the spacebar or two-finger tap-and-drag on the key area). This new I-beam cursor is smart. It adjusts to the size of the text you’re editing — if you’re editing 16-point text you’ll get a smaller cursor; if you’re editing 48-point text you’ll get a larger cursor. (Lo these 35+ years after the original Macintosh, it suddenly strikes me as a bit silly that the I-beam cursor stays small even when editing very large text.) The new iPadOS I-beam cursor also is aware of where lines are in text fields, and “snaps” to the line.


These effects — hover states and size-appropriate I-beam cursor — should just work for existing iPad apps using standard UIKit controls. New APIs are rolling out now for developers who want to take additional advantage of mouse and trackpad support (like, say, if their apps use non-standard text layout engines).


These features are not exclusive to the new Magic Keyboard’s trackpad. iPadOS 13.4 [lets you use these features](https://www.apple.com/ipados/features/) with any iPad, using any (or almost any — I’m sure there are some weird exceptions) Bluetooth or USB mouse or trackpad, including Apple’s Magic Trackpad and Magic Mouse. It’s coming to everyone this coming Tuesday, March 24, and a new beta for developers was released earlier today.


## Magic Keyboard for iPad Pro


This thing looks amazing. Real keys (with backlighting). It floats the iPad above the keyboard surface. You can [apparently](https://www.youtube.com/watch?v=09_QxCcBEyU) tear off the iPad from the keyboard with a single hand. And there’s no kickstand. It’s strong enough to hold the iPad Pro in place, adjustable to any angle from 90° to 130° — a significant range of motion.


Basically, this makes a “docked” iPad Pro a true clamshell laptop. It’s still going to be very top-heavy compared to a pure laptop, but that’s inherently true for any dockable tablet. On a pure laptop, the top part is *only* a display, and the display surface is lightweight plastic, not glass. On a tablet, the whole “computer” is in the top part, and the display is (relatively) heavy glass.


Apple’s Smart Keyboard covers have been… fine. But they’ve clearly been — if not afterthoughts, per se — at least sorta kinda on the afterthought spectrum. They seemed designed only for *typing*, and yet for typing alone, weren’t that great because they use those fabric-covered squishy keys. One of Apple’s decade-old arguments against touchscreen Macs is about the ergonomics of reaching up and out to touch a vertical or near-vertical display. And they’re right — it *is* uncomfortable to poke at a vertical display for more than a few seconds. But without a trackpad (and, of course, without trackpad support in the OS) that is the only way to do many things on an iPad in a Smart Keyboard. Clamoring for touchscreen support on Macs is unlikely ever to stop, but I feel strongly that iPads *needed* trackpad support — both for ergonomic comfort and for precision. Touchscreen support for Macs is, at best, a nice-to-have idea. (And if you ask me, it’s a feature that only *sounds* good.)


Apple’s Smart Keyboard covers have always been very limited in terms of viewing angles. The current ones have two slots; the older ones had just one angle. A proper laptop, of course, uses a hinge, with a range of motion that lets you adjust the display angle until it’s *just right* for you.


Put another way, with its Smart Keyboard covers, it has never seemed like Apple was even *trying* to be in the game for the best way to turn a tablet into a laptop form factor. With this new Magic Keyboard, if it works as well as it looks like it does, Apple quite possibly has jumped to the head of the pack. This is a setup that someone might consider even if they are primarily looking for a laptop, not a tablet. It turns it into a matter of OS preference, not form factor.


Magic is better than smart, at least when it comes to iPad keyboard covers.


There is no aspect of today’s product announcements that more makes me wish it had been feasible for in-person briefings and hands-on time than the hinge on the Magic Keyboard.1 It simply looks too good to be true that it’s strong enough to suspend the iPad Pro above the keyboard without flopping. Real keys, a real trackpad, no kickstand. It even has its own USB-C port to charge your connected iPad Pro via the Smart Connector, freeing the iPad’s own USB-C port for peripherals. It’s the first attempt from Apple at a way to use an iOS device *primarily* as a laptop. Talking to Apple about it, they claim the hinge and magnetic connection are more than sturdy enough to actually use it on your lap.


There’s no special name for the one and only color option, but judging from photos ([and AR](https://daringfireball.net/linked/2020/03/18/ipad-pro-ar)) it’s a very cool near-black. It makes me wish they’d switch the dark option for MacBooks from “space gray” to this near-black color — if you’re going to offer a darker option, go a lot darker. They’ve even added an Apple logo to the back — oriented for landscape. Put an iPad Pro in this case and it’s a laptop.


The only downsides: the Magic Keyboards are not available until “May”, and they cost $300/350 respectively for the 11/12.9-inch iPad Pros. That’s not cheap, but these don’t look cheap. And a bonus: they’re fully compatible with the previous generation 11- and 12.9-inch iPads Pros, including the camera cutouts on the back.


---


As an addendum to this section, I’ll also point out that Apple has collaborated with Logitech on a [$150 Combo Touch Keyboard Case](https://www.logitech.com/en-us/product/combo-touch.html) for the current (7th generation) 10.2-inch iPad and the 10.5-inch iPad Air (which also works with the 10.5-inch iPad Pro). It features both a trackpad and backlit keys, but it requires putting the iPad into a case and settles on a kickstand for support.


The Logitech keyboard features a row of function keys, for things like home, brightness, volume, and media playback; Apple’s Magic Keyboard does not. Neither keyboard features an Escape key.2


## New iPad Pros


Other than the cameras, from the outside these look identical to the previous generation. (As noted above, the previous generation models are compatible with the new Magic Keyboard.) On the inside, the highlights of what’s new include:

- Faster CPU and graphics performance with the A12Z chip. (Why A12*Z* instead of A12*X*? Because they needed a letter “better than X”. Not sure what they’ll do next time, though, since Z is the end of the alphabet. And as I’ve long held, no letter in the alphabet is *cooler* than X.)
- Dual lens rear-facing camera system with wide and ultra-wide lenses.
- A [LiDAR](https://en.wikipedia.org/wiki/Lidar) sensor in the camera system — a first for Apple.
- A five-microphone “studio quality” microphone array based on the same technology as the excellent microphone array introduced with [November’s 16-inch MacBook Pro](https://daringfireball.net/2019/11/16-inch_macbook_pro_first_impressions).


This is a solid update. I don’t think it’s enough to tempt most owners of the previous generation iPad Pros, but for a single generation, just about everything that could be faster is faster. In addition to CPU and GPU, that includes Wi-Fi (support for 802.11ax) and the latest and greatest LTE bands. The A12Z (I almost typed X, dammit) is now an 8-core design.


Prices are unchanged, starting at $800 for the 11-inch and $1,000 for the 12.9-inch. Entry model storage is now 128 GB, up from 64 GB. The largest storage option is 1 TB, which carries a $500 premium. Cellular connectivity remains a $150 upgrade.


The LiDAR sensor is — at least for now — specifically for AR. (I say “at least for now” because it seems possible to me that, come iOS 14, the LiDAR sensor could also be used as an aid for still photography and video.) LiDAR should make AR *much* faster on these new iPad Pros than other iOS devices — specifically when you first start and ARKit is mapping your environment.


One curious omission: Portrait mode photography is only available with the selfie camera. I call this curious because the combination wide/ultra-wide rear-facing camera system is seemingly *very* similar to that of the iPhone 11, which offers Portrait mode. (And again, Portrait mode in particular is a feature that could, in theory, make great use of a LiDAR sensor — the *whole point* of LiDAR is to create a depth map. A LiDAR-aided Portrait mode could come a *lot* closer to DSLR-quality bokeh, blurring background elements based on how far away they are from the lens.)


## New MacBook Air


Last but absolutely not least. This is truly the MacBook Air we’ve been waiting for. Changes from the previous generation:

- Much better base model performance.
- Additional CPU options with even better performance, including quad-core Core i5 and i7 options.
- Increased storage capacity, with the base model now starting at 256 GB.
- The base model starts at $999 — with education pricing starting at $899.


As a general rule, I tend to round prices up a dollar. E.g. I wrote above that the new 11-inch iPad Pro starts at $800, when in fact it starts at $799. I do this because for me at least, it makes comparison math far more clear. I find the difference between $799 and $1,299 far more difficult to compute at a glance than the difference between $800 and $1,300. But I make an exception here for $999, because I think that’s such a psychologically powerful price point. From a consumer advocate perspective, there’s zero practical difference between $999 and $1,000. But $999 is magic.


When the retina MacBook Air [debuted](https://daringfireball.net/2018/11/the_2018_retina_macbook_air), it didn’t hit that magic price. It started at $1,199, with the old non-retina MacBook Air hanging around in the lineup. And that $1,199 model had only 128 GB of storage.


Today’s new MacBook Air models are terrific in two regards: they’re noticeably better computers at noticeably lower prices. Before today, a 256 GB retina MacBook Air cost $1,299 and came with a butterfly mechanism keyboard. Today, a 256 GB MacBook Air costs $999 and comes with the same scissor-switch keyboard as the 16-inch MacBook Pro. You save $300, get a much better keyboard, faster performance, and there is no tradeoff. It’s just better and costs less.


Or, you could spend that same $1,299 (it’s hurting me here not to type “$1,300” but I figure I ought to stay consistent within this section) and get a model with a quad-core Core i5 (instead of dual-core i3) and 512 GB of storage. Same price, *way* better performance, better keyboard, double the storage.


---

1. I saw a prerecorded video briefing/presentation on the new products, and I had an off-the-record phone call Q&A with a few Apple folks. For obvious reasons no one in the media had an in-person briefing. ↩︎
2. It’s well worth pointing out that in iPadOS 13.4, you can remap hardware modifier keys in Settings → General → Keyboards → Hardware Keyboard → Modifier Keys. So if you’re using one of these Escape-less keyboards and wish you had an Escape key, just remap the Caps Lock key to Escape. ↩︎︎



| **Previous:** | [Tot](https://daringfireball.net/2020/02/tot) |
| **Next:** | [The 2020 MacBook Air](https://daringfireball.net/2020/03/the_2020_macbook_air) |


PreviousNext