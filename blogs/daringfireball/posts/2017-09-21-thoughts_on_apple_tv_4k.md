---
title: "Thoughts on Apple TV 4K"
date: 2017-09-21
url: https://daringfireball.net/2017/09/thoughts_on_apple_tv_4k
slug: thoughts_on_apple_tv_4k
word_count: 1494
---


I’ve been testing the new Apple TV 4K for a few days, but I don’t own a 4K TV, so there’s no way I can pretend to write a full-on review when I can’t make use of the tentpole new feature. I do have a few thoughts, though:

- Initial setup was amazingly simple. Plug it in, it boots up quickly, and it asks if you want to share setup information like your Wi-Fi network info from your iPhone. Hold your iPhone near the Apple TV and boom, Apple TV is on your network, and it knows some information like your iTunes Apple ID. This is true too for setting up a new iOS 11 device — you can get a headstart on setting up a new iPhone just by holding your old iPhone next to it. But this is especially helpful on Apple TV, where entering passwords and email addresses through the on-screen keyboard felt like a form of punishment. When you do need to type things, Siri dictation works like a charm — fast and accurate.
- It is baffling to me that Apple didn’t redesign the remote control to make it obvious at a touch which way it’s oriented. The raised white ring around the Menu button is an improvement, but it’s truly the least Apple could have done. I really wish they’d either made it asymmetric (wedge-shaped, perhaps) or used texture to denote orientation along the back and sides. Nobody loves this remote. Most people I know outright dislike it. And Apple left it almost unchanged.
- It seems to me that navigating around the Apple TV 4K interface is improved over the previous generation. Everything feels snappier, Siri seems to be faster and more accurate, and even navigation via the remote control feels more accurate. I’m not sure if that last one is thanks to improvements in the Apple TV 4K hardware itself, improvements to the remote control touchpad, improvements to tvOS 11, the reviewer’s placebo effect (I *want* navigation to be more precise), or some combination of the above. My guess is that it’s a change to tvOS to change the on-screen physics of navigation.
- Apple TV 4K is tiny compared to a Mac Mini, but judging by Geekbench scores ([Mac Mini](http://browser.geekbench.com/v4/cpu/search?dir=desc&q=mac+mini&sort=score); [iPad Pro](https://browser.geekbench.com/v4/cpu/search?dir=desc&q=ipad+pro&sort=score), which uses the A10X in the Apple TV1) it’s a slightly faster computer than even the maxed-out Mac Mini configuration. Apple TV 4K probably has better GPU performance too. In addition to all the performance problems stemming from the fact that the Mac Mini hasn’t been updated in three years, it’s also inarguable that it’s no longer even “mini”. You could arrange four Apple TV units in a 2 × 2 square and they’d take up the same volume as one Mac Mini.
- I did get to see Apple TV 4K in action last week in California, in a product briefing with Apple. They had it connected to a gorgeous 70-inch display from LG. Apple’s remastered videos for the Aerial screensaver look amazing. There’s a daytime flyover in Dubai in which you can now see that one of the skyscrapers has a pool on the roof with two sharks in it. It’s on the left-hand side of the street. That’s some serious James Bond villain’s lair shit.
- Upgrade advice: I often don’t give upgrade advice in reviews, because everyone’s situation is different. Instead, I try to write reviews that help *you* decide on your own whether it’s worth upgrading to this new thing from whatever you’re using now. But with Apple TV 4K, upgrade advice for people who already own the previous Apple TV is easy. If you have a 4K TV, you should upgrade (especially if you watch a lot of movies and TV shows from iTunes). If you don’t own a 4K TV, you shouldn’t.


In short, it’s the Apple TV you know and love (and/or hate), only faster, and with 4K support I can’t test.


## [Nilay Patel’s Review for The Verge](https://www.theverge.com/2017/9/21/16341876/new-apple-tv-4k-review-2017)


> Apple is firmly at the high end of the market: the Apple TV 4K
> starts at $179, much more than competing 4K HDR-capable devices
> like the $89 Roku Premiere+ or the $69 Google Chromecast Ultra. I
> was really expecting — *hoping!* — this thing would blow me away.
> But the new Apple TV doesn’t support Atmos. And it doesn’t support
> YouTube in 4K HDR. And it doesn’t have Disney or Marvel movies in
> 4K HDR. And it makes some 1080p content look less than great.
> I’m going to explain why these limitations exist, but you’ll have
> to bear with me. I suspect most reviewers will focus on the
> interface, the TV app and the various content deals that populate
> it, and the bare fact that the Apple TV now supports 4K HDR
> playback. But I need to tell you about video format arcana,
> because Apple’s decisions around some very wonky specs directly
> influence what it’s like to use the new Apple TV 4K.
> Put some tape on your glasses. This is going to be nerdy.


This is a great review, and I really enjoyed the focus on the technical aspects. In terms of user-interface, Apple TV is clearly the best, because Apple is the only company in the game that values the user experience so highly. ([Matthew Panzarino](https://twitter.com/panzer/status/910890071779196928): “Interface and OS still best in class. All other TV box interfaces are like sticking a fork in your eye and swizzling it around.”)


The omission of [Atmos](https://www.dolby.com/us/en/brands/dolby-atmos.html) support seems baffling. As Patel points out, for the premium price Apple charges — at $179 for the 32 GB model, it’s double the price a Roku Premium Plus — you expect support for premium features like Atmos. According to Patel, though, [Atmos support is coming in a future update](https://twitter.com/reckless/status/910822732287356928).


It’ll be interesting to see how the lack of 4K YouTube support plays out. The issue is that YouTube encodes its 4K content using [the VP9 codec](https://en.wikipedia.org/wiki/VP9). No Apple device supports this format. Apple has thrown its weight behind H.265.


With regular HD content, YouTube supports H.264. If YouTube dropped H.264 support for HD content, you couldn’t play HD YouTube videos on any Apple device. There’s no way YouTube is going to do that — the iOS market is too big and too valuable. And you don’t need 4K to play at native resolution on iPhones — HD is enough. And even on iPads, the displays are small enough that upscaled HD is still good. But on a 70-inch (or bigger) 4K display, 4K content matters.


Unlike the iPhone and iPad, Apple TV doesn’t have enough market share to force Google’s hand. I think Google can stick to its VP9 guns and it’ll be Apple that pays the price. YouTube’s enormous popularity is more likely to force Apple into supporting VP9 than the Apple TV’s middling popularity is to force YouTube into supporting H.265. Even worse for Apple, the whole point of Apple TV is that — like with all Apple products — its entire reason for existence is to provide a premium experience for discerning users. Apple TV users are more likely to notice and be annoyed by upscaled 1080p content on their 4K TV than users of generic set top boxes are.


Apple may well have good technical or legal reasons for not supporting VP9. Apple TV users don’t care. They just want YouTube videos to look great on their TVs.


Another non-ideal aspect of Apple TV 4K — rather than have your TV switch modes from 4K to 1080p when playing 1080p content, Apple TV upscales the 1080p on the fly itself:


> If you have a previous Apple TV, this lack of mode switching is
> familiar, but remapping SDR content into HDR is a whole new
> ballgame, and unfortunately, Apple’s HDR video processing is hit
> or miss. It was great when I watched HD content from iTunes, but
> it fell down in other apps. I watched *The Dark Knight* in HD on HBO
> Go with our video team, and the Apple TV 4K HDR processing blew
> out all the contrast in the image, sharpened everything to hell,
> and turned the film grain into noise. The same movie looked fine
> on iTunes, but it just looked bad from HBO Go. I checked on my
> older 1080p Apple TV, and HBO Go looked fine. So there’s
> definitely work to be done here.


[Matthew Panzarino noted the same thing](https://twitter.com/panzer/status/910895751923884032), again, from content that wasn’t from the iTunes Store.


---

1. There’s no Geekbench app for Apple TV, unfortunately. If anything, Apple TV 4K might be faster than iPad Pro, because iPad Pro runs on battery and Apple TV is always plugged in. ↩︎



| **Previous:** | [Apple Watch Series 3](https://daringfireball.net/2017/09/apple_watch_series_3) |
| **Next:** | [Google and Levi’s ‘Commuter Trucker Jacket with Jacquard’](https://daringfireball.net/2017/09/google_levis_jacket) |


PreviousNext