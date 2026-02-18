---
title: "Turns Out the Telephoto Camera on the iPhone 11 Pro Does Not Support Night Mode"
date: 2019-10-01
url: https://daringfireball.net/2019/10/night_mode_telephoto
slug: night_mode_telephoto
word_count: 543
---


From [The Verge’s story on Deep Fusion](https://www.theverge.com/2019/10/1/20893516/apple-deep-fusion-camera-mode-iphone-11-pro-max-ios-13-beta), coming in iOS 13.2 beta 1 (which, I’ve been informed, is now scheduled to drop *tomorrow* or maybe even later this week, not today as originally planned):


> With Deep Fusion, the iPhone 11 and 11 Pro cameras will have three
> modes of operation that automatically kick in based on light
> levels and the lens you’re using:
> The standard wide angle lens will use Apple’s enhanced Smart HDR
> for bright to medium-light scenes, with Deep Fusion kicking in
> for medium to low light, and Night mode coming on for dark
> scenes.
> The tele lens will mostly use Deep Fusion, with Smart HDR only
> taking over for very bright scenes, and Night mode for very dark
> scenes.
> The ultrawide will always use Smart HDR, as it does not support
> either Deep Fusion or Night mode.


Until yesterday, I was under the same impression as the above. But Sebastiaan de With — co-creator of the excellent iPhone camera app Halide — [pointed out on Twitter](https://twitter.com/sdw/status/1178472295989276672) that Night Mode only works with the regular wide-angle lens. You can shoot with 2× zoom with Night Mode, but when you do, it uses the wide angle camera and digitally, rather than optically, zooms to the 2× field of view.


You can see this yourself in the EXIF data. Shoot an image using Night Mode at 2× zoom, and look at the lens information in Photos on the Mac. It will say “iPhone 11 Pro back triple camera 4.25mm f/1.8”. That’s the wide-angle camera. The telephoto camera is “6mm f/2”, and the ultra-wide is “1.54mm f/2.4”. (The front-facing camera is “2.71mm f/2.2”.)


It’s even easier to see it for yourself by simply obscuring the lenses one at a time with a fingertip or piece of paper. Cover the telephoto and you can still shoot “2×” Night Mode shots; cover the regular wide lens and you can’t.


0.5× always uses the ultra-wide camera, because you can’t get that field of view otherwise. 1× always uses the wide angle, because that camera has the best sensor and fastest lens. But 2× doesn’t mean you’re always using the telephoto camera — in low light it will use the wide-angle camera and digital zoom. Previous iPhones with dual camera systems have done the same thing in low light conditions, but a lot of us — myself included — made the wrong assumption about Night Mode and “2× zoom”.


It occurs to me that this is why Apple has been somewhat obfuscatory about Night Mode working only with the regular wide angle camera, despite being very forthcoming about explaining other technical details (like Deep Fusion) at great length: it means the iPhone 11 can shoot the *exact* same “2×” Night Mode shots as the iPhone 11 Pro, because on both phones 2× Night Mode shots are cropped and digitally zoomed from the 1× camera sensor. There’s nothing scandalous about this — everyone loves Night Mode, including for 2× field-of-view photos. But it’s yet another way that the iPhone 11 is the technical equal to the significantly more expensive 11 Pro.



| **Previous:** | [Richard Stallman’s Disgrace](https://daringfireball.net/2019/09/richard_stallmans_disgrace) |
| **Next:** | [Apple and Hong Kong](https://daringfireball.net/2019/10/apple_hong_kong_map) |


PreviousNext