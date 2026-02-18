---
title: "Two Excellent New iPhone Camera Apps: Not Boring’s !Camera and Adobe’s Project Indigo"
date: 2025-10-21
url: https://daringfireball.net/2025/10/not_boring_camera_and_adobe_project_indigo
slug: not_boring_camera_and_adobe_project_indigo
word_count: 1675
---


[
](https://daringfireball.net/misc/2025/10/sjt-june-2025.jpeg)


I took the above photo on Monday, June 9, [this year at WWDC](https://glass.photo/gruber/series/2skCCKMH4LYm8HAuxeoMHo-wwdc-2025-apple-park). Keynote day, around 1:30pm PT. I captured it using my iPhone 16 Pro and [Not Boring’s !Camera app](https://notbor.ing/product/camera), using the built-in Mono Tokyo LUT. Like the other apps in Not Boring’s growing suite, !Camera can be mistaken by the too-cynical as a toy. It is fun and colorful, and some of its features exist for the sake of fun alone. But, just like Not Boring’s other offerings (my favorites: [!Weather](https://notbor.ing/product/weather), [!Calculator](https://notbor.ing/product/calculator), and [!Habits](https://notbor.ing/product/habits)), it’s a genuinely serious tool. And of the bunch, I think !Camera is the most innovative. The fact that it’s fun makes me want to use it — a vastly underestimated attribute of tool design. [From Not Boring’s website](https://notbor.ing/product/camera):


> Go from snap to sharing without any editing. !Camera is the first
> camera app to enable professional-level color grading with 3D LUTs
> (“lookup tables”) used in high-end workflows by pro photographers
> to achieve realistic film simulations and unique cinematic looks.
> Use !Camera’s designed presets, add LUTs from your favorite
> creators, or make and import your own! New Styles and
> collaborations released every season.


!Camera *looks* gimmicky but I assure you it’s not — and what might strike you as gimmicky is really just plain fun and whimsical. My affection for it, and my use of it, has grown, not shrunk, as the months have gone by. While my hardware Camera Control buttons (plural, as I’m currently testing multiple iPhones) remain set to open Apple’s own Camera app, which I continue to use by default, I keep !Camera’s simple widget on my iPhones’ Lock Screens to launch it quickly after unpocketing my iPhone.


!Camera’s use of LUTs for filter-like effects opens the app to a wide world of non-proprietary looks. The best source I’ve found for new LUTs to import is the [Panasonic LUMIX Lab](https://apps.apple.com/us/app/panasonic-lumix-lab/id6499262377) app — Panasonic’s built-in LUTs are boring, but the app has a whole community of user-submitted LUTs and I’ve found several of them that are lovely. !Camera’s custom “SuperRAW” format, is, in my opinion, key to the appeal of the app:


> No more flat lifeless photos, no AI processing, no weird
> artifacts. Our SuperRaw™ photo processing has been crafted to
> showcase more film-like tones and preserve a photo’s beautiful
> natural grain.


Rather than fighting the nature of the small (and thus, noisy) sensors in the iPhone camera systems, SuperRAW processing embraces the noise, imbuing images with [natural-looking grain](https://x.com/asallen/status/1947321942127845853). The results, to my eyes, are genuinely film-like. If you want, you can configure !Camera to save a raw DNG file alongside each capture, for post-processing in an app like Darkroom, Lightroom, or Photoshop. I’m glad that option is there, but I just shoot in SuperRAW, which saves ready-to-share HEIC files with the LUT applied in my camera roll, so what I see is what I get.


Each of Not Boring’s apps is available for a $15/year subscription, but the way to go is [Not Boring’s $50/year “Super !Boring” subscription](https://notbor.ing/plans), which grants you a license to their entire suite of apps. I was already a Super !Boring subscriber when !Camera launched, so, effectively, I got it for free. $50/year isn’t nothing, but it’s not much, and subscriptions have proven to be the best monetization strategy for indie developers in today’s world.


## Project Indigo


Marc Levoy, Adobe fellow, and Florian Kainz, principal scientist, [on the Adobe Research blog back in June](https://research.adobe.com/articles/indigo/indigo.html):


> Second, people often complain about the “smartphone look” — overly
> bright, low contrast, high color saturation, strong smoothing, and
> strong sharpening. To some extent this look is driven by consumer
> preference. It also makes photos easier to read on the small
> screen and in bad lighting. But to the discerning photographer, or
> anybody who views these photos on a larger screen than a phone,
> they may look unrealistic. [...]
> What’s different about computational photography using Indigo?
> First, we under-expose more strongly than most cameras. Second, we
> capture, align, and combine more frames when producing each photo — up to 32 frames as in the example above. This means that our
> photos have fewer blown-out highlights and less noise in the
> shadows. Taking a photo with our app may require slightly more
> patience after pressing the shutter button than you’re used to,
> but after a few seconds you’ll be rewarded with a better picture.
> As a side benefit of these two strategies, we need less spatial
> denoising (i.e. smoothing) than most camera apps. This means we
> preserve more natural textures. In fact, we bias our processing
> towards minimal smoothing, even if this means leaving a bit of
> noise in the photo. You can see these effects in the example
> photos later in this article.
> One more thing. Many of our users prefer to shoot raw, not JPEGs,
> and they want these raw images to benefit from computational
> photography. (Some big cameras offer the ability to capture
> bursts of images and combine them in-camera, but they output a
> JPEG, not a raw file.) Indigo can output JPEG or raw files that
> benefit equally from the computational photography strategy
> outlined here. [...]
> In reaction to the prevailing smartphone look, some camera apps
> advertise “zero-process” photography. In fact, the pixels read
> from a digital sensor must be processed to create a recognizable
> image. This processing includes at a minimum white balancing,
> color correction to account for the different light sensitivity of
> the red, green and blue pixels, and demosaicing to create a
> full-color image. Based on our conversations with photographers,
> what they really want is not zero-process but a more natural look — more like what an SLR might produce. To accomplish this, our
> photos employ only mild tone mapping, boosting of color
> saturation, and sharpening. We do perform semantically-aware
> mask-based adjustments, but only subtle ones.


You may recognize Levoy’s name. After a distinguished career [at Stanford teaching computer science](https://graphics.stanford.edu/~levoy/), Levoy spent 2014 to 2020 leading the computational photography team at Google [for their highly-regarded-as-cameras Pixel phones](https://www.youtube.com/watch?v=-h7Is5MA3Ng). In 2020 [Levoy left Google for Adobe](https://daringfireball.net/linked/2020/07/20/levoy-adobe), and Indigo is one of the first fruits of his time there.


Allison Johnson of The Verge — notably, she came to The Verge by way of [DPReview](https://www.dpreview.com/) — wrote a splendid piece on Indigo shortly after the app debuted, under the headline “[Adobe’s New Camera App Is Making Me Rethink Phone Photography](https://www.theverge.com/tech/694014/adobe-project-indigo-camera-app-hands-on-hdr)”:


> If you hate the overly aggressive HDR look, or you’re tired of
> your iPhone sharpening the ever-living crap out of your photos,
> Project Indigo might be for you. It’s available in beta on iOS,
> though it is *not* — and I stress this — for the faint of heart.
> It’s slow, it’s prone to heating up my iPhone, and it drains the
> battery. But it’s the most thoughtfully designed camera experience
> I’ve ever used on a phone, and it gave me a renewed sense of
> curiosity about the camera I use every day.
> You’ll know this isn’t your garden-variety camera app right from
> the onboarding screens. One section details the difference between
> two histograms available to use with the live preview image (one
> is based on Indigo’s own processing and one is based on Apple’s
> image pipeline). Another line describes the way the app handles
> processing of subjects and skies as “special (but gentle).” This
> is a camera nerd’s love language.


Slow and battery-draining is exactly why Apple hasn’t pursued these sorts of advanced computational photography techniques in the built-in Camera app. Apple’s Camera app is super-fast and takes extraordinary effort to go easy on the battery. Apple is making entirely different trade-offs — correctly — for the default Camera app. Pro and prosumer photographers may want to make completely different trade-offs when it comes to image processing time and energy.1 (For the last few years, Apple has shot its keynote events using iPhone cameras exclusively, but they use apps like [Blackmagic Camera](https://www.blackmagicdesign.com/products/blackmagiccamera), not the built-in Camera app, to shoot them.)


I’m deeply intrigued by Indigo, and I have a few friends who’ve shown me some extraordinary photographs taken with the app. If they hadn’t told me, I’d have wagered their photos were taken with dedicated large-sensor digital cameras, not phones. Johnson described Indigo as “not for the faint of heart”, and I’m just faint-hearted — or perhaps lazy — enough that, when venturing to a third-party camera app during the past few months, I’ve reached for !Camera, not Indigo, mainly because I don’t want to bother with any sort of manual post-processing for any but my very favorite of favorite images. But Indigo — available [free of charge from the App Store](https://apps.apple.com/us/app/project-indigo/id6742591546) — is well worth your attention.2 I hope it’s an app that Adobe is serious about maintaining and developing into the future.


---

1. Johnson also interviewed Levoy last month on The Vergecast. [The interview starts at 30m:22s](https://www.youtube.com/watch?v=bQI6G0cbZKY&t=1822s). ↩︎
2. Indigo is currently iOS-only, but [in their introductory blog post](https://research.adobe.com/articles/indigo/indigo.html), Levoy and Kainz write: “What’s next for Project Indigo? An Android version for sure. We’d also like to add alternative ‘looks’, maybe even personalized ones. We also plan to add a portrait mode, but with more control and higher image quality than existing camera apps, as well as panorama and video recording, including some cool computational video features we’re cooking up in the lab.” Also worth noting: Indigo’s computational photography is so tied to specific hardware that it [doesn’t yet support](https://community.adobe.com/t5/lightroom-ecosystem-cloud-based-discussions/p-introducing-the-project-indigo-camera-app/m-p/15513112#M108265) any of the iPhones 17 nor the iPhone Air. ↩︎︎



| **Previous:** | [The Just Plain M5 Chip Launches in Three Updated Products: 14-Inch MacBook Pro, iPad Pro (Both Sizes), and Some Sort of Headset Thingamajig Called Vision Pro](https://daringfireball.net/2025/10/m5_chip_launches_with_macbook_pro_ipad_pro_vision_pro) |
| **Next:** | [Apple Loses Landmark U.K. Lawsuit Over App Store Commissions](https://daringfireball.net/2025/10/apple_uk_lawsuit_app_store_commissions) |


PreviousNext