---
title: "Conjecture Regarding the Precise Details of the iPhone D22 Display Resolution"
date: 2017-08-05
url: https://daringfireball.net/2017/08/d22_display_conjecture
slug: d22_display_conjecture
word_count: 1862
---


Thanks to last week’s [inadvertent release of an unredacted build](https://daringfireball.net/linked/2017/08/01/homepod-os-release) of HomePod’s version of iOS, we know some things that we didn’t know before. One of those things is that the new edge-to-edge iPhone is codenamed D22, and that [the OS explicitly supports an iPhone display with hardware resolution of 2436 × 1125 pixels](https://twitter.com/stroughtonsmith/status/892042013297790977).


For reference, all 4.7-inch iPhones to date (6, 6S, and 7) have a display resolution of 1334 × 750, at 326 PPI. All Plus models to date have a display resolution of 1920 × 1080, at 401 PPI. Apple publishes these numbers on the [iPhone tech specs comparison page](https://www.apple.com/iphone/compare/).


Back in 2014, in the lead-up prior to the announcement of the iPhone 6 and 6 Plus, [I tried to guess the pixel dimensions of both phones](https://daringfireball.net/2014/08/larger_iphone_display_conjecture):


> But after giving it much thought, and a lot of tinkering in a
> spreadsheet, here is what I think Apple is going to do:
> 4.7-inch display: 1334 × 750, 326 PPI @2x
> 5.5-inch display: 2208 × 1242, 461 PPI @3x
> @2x means the same “double” retina resolution that we’ve seen on
> all iOS devices with retina displays to date, where each virtual
> *point* in the user interface is represented by two physical
> pixels on the display in each dimension, horizontal and vertical.
> @3x means a new “triple” retina resolution, where each user
> interface point is represented by three display pixels. A single
> @2x point is a 2 × 2 square of 4 pixels; an @3x point is a 3 × 3
> square of 9 pixels.
> I could be wrong on either or both of these conjectured new
> iPhones. I derived these figures on my own, and I’ll explain my
> thought process below. No one who is truly “familiar with the
> situation” has told me a damn thing about either device. I have
> heard second- and third-hand stories, though, that lead me to
> think I’m right.


My guess about the 4.7-inch display was exactly correct. My guess about the 5.5-inch display was wrong, but my logic was right. All 5.5-inch iPhone Plus models have hardware 1920 × 1080 displays at 401 PPI, but at their default scaling (“Standard” as opposed to “Zoomed” in the Display section of Settings) they *pretend* to be 2208 × 1242 displays at 461 PPI, exactly as I predicted. (Actually, it’s better to think of it as 462 pixels per inch, because 462 is evenly divisible by 3, which is what you need to do convert pixels into points on an @3x retina display. So let’s use 462 henceforth. I should have thought of this back in 2014.)


iOS scales the user interface on the Plus models from the virtual resolution of 2208 × 1242 to the actual hardware resolution of 1920 × 1080 on the fly. The upside of this is that the display is less expensive and consumes less power. The downside is that the UI is not rendered pixel perfectly — the scaling uses anti-aliasing to fake it. But because the pixels are so very small, almost no one has sharp enough eyes to notice it, and because the physical resolution is so high (401 PPI), it looks sharper than the 4.7-inch displays which are running at their “true” resolution, with no scaling. But pixel-perfect “true” @3x would look even better.


Using similar logic, and considering all of the rumors and purported part leaks, I have a highly-educated guess as to the dimensions of the D22 display:


5.8 inches, 2436 × 1125, 462 PPI, true @3x retina with no scaling.


We’ve seen the numbers 2436 × 1125 before. Supply-chain rumor savant Ming-Chi Kuo suggested those numbers in a report back in February, which was summarized by both [MacRumors](https://www.macrumors.com/2017/02/15/2017-iphone-edge-to-edge-display-virtual-buttons/) and [9to5Mac](https://9to5mac.com/2017/02/16/iphone-8-higher-pixel-density/). But what Kuo has predicted is different from what I’m suggesting. Kuo said the OLED display in this year’s new OLED iPhone will measure 5.8 inches diagonally and will have a total hardware resolution of 2800 × 1242. That’s corner to corner, the entire front face of the device, minus the bezels on the sides, top, and bottom. Within this 5.8-inch display, Kuo said there would be a 5.15-inch “display area” with resolution 2436 × 1125. The remaining area at the bottom of the display would be a “function area” (his term) where, presumably, a virtual home button would appear.


[Here is the actual image from Kuo’s report](https://daringfireball.net/misc/2017/08/kuo-d22.jpg), illustrating this.


I think Kuo has it wrong, and is conflating the pixel dimensions of two different iPhones. I think this year’s new flagship iPhone, D22, has a 5.8-inch 2436 × 1125 display. I wouldn’t be surprised if Kuo heard about a 2800 × 1242 display, too, but if so I think that phone is a Plus-sized version of this new form factor, with the same 462 PPI density and a size of around 6.6 inches diagonally. Such a display, with the reduced bezel design of D22, would be exactly as tall as an iPhone 7 Plus and slightly narrower. I wouldn’t be surprised [if such a phone is in the pipeline for 2018](https://www.macrumors.com/2017/05/23/iphone-9-rumored-display-sizes/).


From what I’ve seen, Kuo specified the size (5.8 inches) and the pixels (2800 × 1242), but he didn’t specify the PPI density. But given the size and the horizontal and vertical pixel counts, you can work out the PPI. [Benjamin Mayo did so](https://9to5mac.com/2017/02/16/iphone-8-higher-pixel-density/), and the result is 521 PPI.


*A 521 PPI display doesn’t actually make sense though.* I didn’t really think about this until today, but that number should have stuck out like a sore thumb back in February. Here’s the thing. It matters how big a *point* is, because it directly affects the real-world size of on-screen elements.


All non-Plus iPhones to date — every one of them from the original iPhone in 2007 through the iPhone 7 — has a display with 163 *points* per inch. In the pre-retina era, that meant 163 *pixels* per inch, too. Each pixel was a point, each point was a pixel. All @2x iPhone retina displays have 326 pixels per inch. Divide by 2 and you get 163 *points* per inch. That means that a 44-point touch target is exactly the same physical size on screen on all non-Plus iPhones. 16-point type renders at exactly the same size, and so on.


The 6/6S/7 Plus phones have a slightly lower *points* per inch density: take 462 (the number of pixels per inch in the *scaled* version of the UI), divide by 3 (because it’s an @3x retina display) and you get 154 points per inch. That’s OK, though, because fewer points per inch means that a, say, 44-*point* touch target will be slightly bigger on screen. 16-point type will render slightly larger, and so on. Larger tap targets are easier to hit, and larger type is easier to read. The iPhones Plus use most of their extra pixels (compared to their non-Plus siblings) to show more content on screen. But they also use them to make all content slightly larger.


A 521-PPI display doesn’t make sense because if you divide by 3 (because it’s @3x retina), you get around 174 *points* per inch. That’s not a huge difference, but everything would appear smaller on screen compared to an iPhone 7, and quite a bit smaller than on an iPhone 7 Plus. The only two natural pixel-per-inch densities for an @3x iPhone display are 462 PPI (154 × 3) and 489 PPI (163 × 3).


“*What about scaling?*” you might be thinking. Couldn’t the resolution of the display be 521 PPI and Apple could make the points per inch work out by scaling the interface dynamically, like they do on the Plus models? They *could*, but that would be really dumb. For one thing, if it’s @3x, they’d have to scale the UI *up*, not *down*. They’d be using a smaller image to fill a bigger screen. With the Plus, they use a larger image to fill a smaller screen. Scaling down is a reasonable and interesting compromise. Scaling up would be stupid. Surely a 521-PPI display would cost more to manufacture than a 462-PPI display. So why would Apple pay more for a display and use scaling when they could pay less for a 462 PPI display on which they don’t have to do any scaling at all? It would cost less, look better, and be more efficient.


---


So we know that [iOS 11 has support for a 2436 × 1125 iPhone display](https://twitter.com/stroughtonsmith/status/892042013297790977). We know that 462 PPI is the “natural” (no scaling) resolution for @3x retina on iPhone. We know that a 2436 × 1125 display with 462 PPI density would measure 5.8 inches diagonally. We know that all rumors to date about the D22 iPhone claim it has a 5.8-inch display. We know that a 5.8-inch display with a 2.17:1 aspect ratio (2436/1125), combined with 4-5mm bezels on all sides, would result in a phone whose footprint would be just slightly taller and wider than an iPhone 7. And we know that all rumors to date say that D22 is slightly bigger than an iPhone 7.


We also know that the same section of iOS 11 that specifies the 2436 × 1125 display does *not* mention anything about a 2800 × 1242 display. Further, that same section of iOS refers to the iPhone Plus as having a 1920 × 1080 display — this is part of the OS that deals with the actual hardware resolution of the displays, not the virtual scaled display size.


We also know that a 2800 × 1242 display would have a slightly different aspect ratio: 2.25:1. [Stephen Troughton-Smith noted today with a mockup](https://twitter.com/stroughtonsmith/status/893625588891701249) that a purported schematic of D22 made from precise blueprints, which was [leaked on Twitter by Benjamin Geskin](https://twitter.com/VenyaGeskin1/status/856073055701020673) back in April of this year, shows a display that *exactly* matches the 2.17:1 aspect ratio of a 2436 × 1125 display. A 2800 × 1242 display [doesn’t come close to fitting](https://daringfireball.net/misc/2017/08/2800.png) that schematic.


We *know* these things. All of these facts point to the same conclusion: D22’s display is 5.8 inches, 2436 × 1125, 462 PPI. The only reason to think otherwise is that Ming-Chi Kuo reported otherwise back in February. The simplest explanation is that Kuo got this [wrong](https://www.ped30.com/2016/04/24/apple-ming-chi-kuo-truthiness/), and either he or his sources conflated the displays of two different iPhones.1


---

1. It also never made sense to me how Kuo would know about the precise dimensions of a single display that would be split into separate “display” and “function” areas. That’s something that would be handled by iOS in software, not something in the hardware. Kuo’s sources seem to be exclusively or almost exclusively in the Asian supply chain. I can’t recall him ever getting a major scoop related to software. My understanding is that Apple does not even send prerelease builds of iOS to China. Instead, Apple employees fly prototype iPhones from China back to the US for testing with development builds of iOS. ↩︎



| **Previous:** | [On Apple Removing VPN Apps From the App Store in China](https://daringfireball.net/2017/07/apple_china_vpn_apps) |
| **Next:** | [Safari Should Display Favicons in Its Tabs](https://daringfireball.net/2017/08/safari_should_display_favicons_in_its_tabs) |


PreviousNext