---
title: "Cold Water on the iPad 2 Retina Display Hype"
date: 2011-01-18
url: https://daringfireball.net/2011/01/cold_water_ipad_retina_display
slug: cold_water_ipad_retina_display
word_count: 1162
---


Rumors are [rampant](http://www.macrumors.com/2011/01/15/ipad-2-screen-likely-to-have-2048x1536-resolution/) that the upcoming iPad 2 will feature a higher-resolution retina display. Long story short: No, it won’t.


The current iPad has a 1024 × 768 display; a double-resolution retina display iPad would have a 2048 × 1536 display. At the same physical size, that would be about 260-270 pixels per inch. Apple, I suspect, [could legitimately call such a display a “retina display”](http://www.tuaw.com/2011/01/18/ipads-and-retina-displays-doing-the-math/) on the grounds that the typical viewing distance for an iPad is further away from your eyes than with an iPhone. (The iPhone 4 display is around 330 pixels per inch.)


Lending a hint of credence to the rumors, [MacStories](http://www.macstories.net/ipad/evidence-of-ipad-retina-display/) (and [others](http://www.macrumors.com/2011/01/15/ipad-2-screen-likely-to-have-2048x1536-resolution/)), poking around in the iOS iBooks app bundle, found double-resolution UI graphics for the iPad. Then, last week, [Engadget’s Josh Topolsky posted a report on the iPad 2 and iPhone 5](http://www.engadget.com/2011/01/14/exclusive-the-future-of-the-ipad-2-iphone-5-and-apple-tv-and/). Regarding the iPad 2, Topolsky wrote:


> From what we’ve been told, the thinner, sleeker tablet will sport
> a new screen technology that is akin to (though not the same as)
> the iPhone 4’s Retina Display and will be “super high resolution”
> (unlike reports to the contrary). The device will remain at 10
> inches but will now feature both front and rear cameras (not a
> huge surprise), and… there’s an SD slot.


Those “reports to the contrary” regard [these UI images found by 9 to 5 Mac](http://www.9to5mac.com/47070/ipad-2-will-take-pics-shoot-flicks) in the iPad camera framework for the recent iOS 4.3 beta — which images are 1024 × 768. Such images must be for a new iPad, because the existing iPad has no camera.


So:

- Engadget reports the iPad 2 has a new display with “super high resolution”.
- The math on increasing the pixel density for iOS touchscreen devices is such that it only works out perfectly if the resolution doubles, like when the iPhone and iPod Touch went from 480 × 320 to 960 × 640. Trust me, it’s double or nothing.
- There are double-resolution UI elements for the iPad in the iBooks app bundle.


But:

- There are camera app UI images in iOS 4.3b1 which are only 1024 × 768.
- A 2048 × 1536 iPad display would seemingly be cost prohibitive today. Not just for the display itself, but for the RAM. The current iPad has 256 MB of RAM, which is shared between the CPU and GPU. I don’t think 512 MB of RAM would be enough for an iPad with a 2048 × 1536 display.1 That’s almost as many total pixels as on [a 27-inch Cinema Display](http://www.apple.com/displays/specs.html) (resolution: 2560 × 1440).


Sounds too good to be true, though, right? When I linked to Engadget’s report, I wrote:


> I hope it’s true, because it’d be beautiful, but I’ll
> believe it when I see it.


I asked around, and according to my sources, it *is* too good to be true: the iPad 2 does *not* have a retina display. I believe the iPad 2’s display will remain at 1024 × 768. Its display may be improved in other ways — brighter, better power consumption, thinner, perhaps. Maybe it uses the new manufacturing technique Apple introduced with the iPhone 4 display, which brings the LCD closer to the surface of the touchscreen glass — making it look more like pixels *on* glass rather than pixels *under* glass. But my sources are pretty sure that it’s not 2048 × 1536 or any other “super high resolution”.


But so what’s the deal with those double-resolution UI graphics in iBooks? I don’t know, but my guess is that it’s just the work of a UI designer thinking ahead. Sooner or later, the iPad *will* get a retina display, and I remain convinced that it will be exactly double the current resolution. (There are 2048 × 1536 iPad prototypes in Cupertino. They’re not the iPad 2, though.) Double-resolution graphics created now are double-resolution graphics that don’t have to be created under a tight deadline later, when such an iPad actually ships. (I suspect it’s an oversight that these graphics were actually included in the app bundle at this point.)


Consider the timeline for the iPhone (and iPod Touch): three model years at the original resolution (iPhone, iPhone 3G, iPhone 3GS). Then came the iPhone 4 with the retina display. From what I’ve gathered about the iPad 2, it’s more analogous to the iPhone 3GS than the 3G. Spec-wise, the iPhone 3G differed from the original iPhone in only one significant way: the 3G networking support. The iPad 2 is more like the 3GS: faster processor, more RAM, better graphics performance — but, like the 3GS, still with the same display resolution as the original model.


Am I certain the iPad 2 remains at 1024 × 768? No. But I’d wager on it — heavily.2


It seems perverse to begin speculating about the iPad 3 when we’re still months away from the iPad 2, so I’m going to file “retina display for the iPad” away until 2012.


**Update:** On Twitter, [Josh Topolsky stands by Engadget’s source](http://twitter.com/joshuatopolsky/status/27595159646507008), and Engadget editor [Nilay Patel tries to square the circle](http://twitter.com/reckless/status/27598858255073280) (addressed to me):


> I think the key here is that you’re saying it’s 2× or nothing, but
> we’re not making the same claim.


I.e., what if the iPad 2 has a display resolution of, say 1280 × 960 — a scaling factor of 1.25? Or 1536 × 1152 (scaling factor 1.5)? In that case, Engadget is right, that the iPad 2 has a higher resolution display, but my sources are also right, that the iPad 2 does not have a retina display. I think that’s unlikely for reasons pertaining to UI scaling math (the same reason that the iPhone display resolution didn’t increase incrementally) — but it’s worth noting that my sources only claim “no retina display”, not that the resolution is unchanged. The “double or nothing” line is my opinion, not information from any source.


As for why I think anything short of 2048 × 1536 is unlikely, and putting the scaling math aside, consider this: If Apple were to issue a second iPad resolution now, developers would have to create *three* sets of graphics to get pixel-perfect UI designs across all iPads once the iPad does get a retina display — and it will. Supporting multiple resolutions with pixel-perfect UIs is hard.


---

1. Note, for example, that the 27-inch iMac [ships with a graphics card with 512 MB of RAM](http://www.apple.com/imac/specs.html). Even the MacBook Air [has 256 MB of RAM on its graphics card](http://www.apple.com/macbookair/specs.html). ↩︎
2. That I’m now convinced that Engadget’s sources are wrong about the iPad 2’s display resolution makes me even more skeptical regarding the rest of their report, like with the purported SD card slot. (My sources had nothing to say about that, either way.) ↩︎



| **Previous:** | [The Leave](https://daringfireball.net/2011/01/the_leave) |
| **Next:** | [Oceania: We Have Always Required Books From the Eurasian E-Bookstore to Be Sold Through Our In-App Purchasing System](https://daringfireball.net/2011/02/oceania_in_app_purchases) |


PreviousNext