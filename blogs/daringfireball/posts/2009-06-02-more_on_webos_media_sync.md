---
title: "More on Palm’s WebOS ‘Media Sync’"
date: 2009-06-02
url: https://daringfireball.net/2009/06/more_on_webos_media_sync
slug: more_on_webos_media_sync
word_count: 1126
---


In [yesterday’s piece](http://daringfireball.net/2009/06/webos_itunes_integration) on Palm’s WebOS “media sync” iTunes integration I mostly avoided the legal aspects. When I say that the WebOS media sync feature is not “legit”, I mean that it is not supported by Apple, not something Apple intends for third-parties to do, and (if [Jon Lech Johansen’s theory](http://nanocr.eu/2009/05/28/syncing-music-and-video-to-the-palm-pre/) is correct) a violation of the USB specification.


But is it illegal? And would it be illegal for Apple to take countermeasures against it? My guess is “no” to both questions.


WebOS’s media sync is clearly a hack, but hacks generally don’t violate any laws. I’m not a lawyer and I’m not an expert on the DMCA, but I don’t see how masquerading as an Apple iPod over USB would violate it. If Palm were doing something to strip DRM from music or video files, that would be another story. But they’re not.


Legality aside, is Palm doing anything wrong in a moral sense? Matthew Paul Thomas, on Twitter [here](http://twitter.com/mpt/status/2004140357) and [here](http://twitter.com/mpt/status/2004249740), draws the analogy between WebOS masquerading as an iPod via USB and Safari masquerading as “Gecko” via its HTTP user-agent string so as to identify itself as being compatible with certain poorly-coded web sites. That’s an interesting analogy, but there are differences, including that [Safari’s complete user-agent string](http://developer.apple.com/internet/safari/faq.html#anchor2) still uniquely and honestly identifies it as Safari. Safari and other WebKit-based browsers [such as Chrome](http://www.useragentstring.com/pages/Chrome/) include the word “gecko” in their user-agent strings on the assumption that web sites that look for “gecko” in the UA string do so not because they’re trying to serve specific content only to actual Gecko-based browsers, but because they’re trying to serve specific content only to browsers with Gecko-like rendering features. I.e. when Safari or Chrome “just work” when rendering some web site that checks for “gecko” in the UA string, it is almost certainly in accordance with the intentions of whoever developed the web site. When the Pre “just works” with iTunes, it is not in accordance with Apple’s intentions. That’s not to say it is *wrong*, particularly since in both cases — browser UA strings and Palm’s media sync — the primary purpose is to do what the *user* wants. But it’s not a great analogy.


I don’t think WebOS’s media sync is a mistake on Palm’s part because it is wrong, I think it’s a mistake because it is risky and unnecessary.


I think where Palm is weakest, legally, is with regard to all of the former Apple engineers now working on the Pre and WebOS. Even if Palm could prove that no former Apple employees used their knowledge of Apple trade secrets to implement this feature, I don’t know [whether Palm is in good enough financial shape](http://www.marketwatch.com/story/palm-banks-future-on-pre-and-new-operating-system) to risk such a suit.1


The flip side is the question of whether Apple would risk legal trouble by shipping a future release of iTunes that blocks WebOS from syncing. On the surface, one might think that Apple can do whatever it wants with its own software. The question some are raising, though, is whether Apple should be legally constrained from anti-competitive behavior as the holder of a monopoly.


[Nick Forge writes](http://forgecode.net/2009/06/why-palms-webos-media-sync-itunes-integration-can-be-legit/):


> It’s one thing for Apple not to facilitate syncing with 3rd-party
> (non-Apple) players, but another altogether to actively go out of
> their way to stop it happening. Can you imagine the fallout if
> Microsoft were to add code into the SMB protocol that blocked access
> to non-Microsoft systems?
> Apple effectively monopolises the portable media player market, and
> if they resort to Microsoft-in-the-90s style tactics to hold on to
> that monopoly, they could find themselves on the wrong side of the
> U.S. Department of Justice.


I disagree with Forge that an analogy to Microsoft and [SMB](http://en.wikipedia.org/wiki/Server_Message_Block) is apt. Being the clear market leader doesn’t necessarily mean that Apple holds a [monopoly](http://en.wikipedia.org/wiki/Monopoly), a term which has been thrown around far too loosely in the aftermath of Microsoft’s court cases in the U.S. and E.U. Many markets have a clear leader, but very few market leaders hold a monopoly.


What monopoly does Apple hold, specifically? A monopoly in “portable media players” wouldn’t seem relevant — it is iTunes, the Mac and Windows software, that WebOS interfaces with, not iPods. Does iTunes (not the store, but the desktop app) constitute a monopoly? I would say no, not even close.


Often overlooked is that Apple already provides a way for third-party software to access the contents of your iTunes library: [the iTunes Music Library.xml file](http://support.apple.com/kb/HT1660). The legit way for a third-party portable device to sync music and video with iTunes is for the device makers to write or license their own software to read the iTunes Music Library.xml file and copy the media from the library. That’s what [Nokia Multimedia Transfer](http://europe.nokia.com/A4423139) and RIM’s [BlackBerry Media Sync](http://na.blackberry.com/eng/services/media/mediasync.jsp) do, and it’s what [DoubleTwist](http://www.doubletwist.com/dt/Home/Index.dt) does for a wide variety of non-Apple portable devices, [including the Pre](http://www.palmprevideo.com/). Yes, DoubleTwist is Jon Lech Johansen’s company,2 but that doesn’t render invalid his opinion that WebOS’s media sync is a hack. DoubleTwist (without any official relationship with Palm) syncs media between the Pre and iTunes legitimately; Palm’s “media sync” does not.


What it comes down to is that third-party (i.e. non-Apple) devices and software *already have* legitimate access to the contents of your iTunes library. The XML file describes the audio and video files and your playlists. The media files themselves are stored out in the open as regular files inside the “iTunes Music” folder.


What they don’t have is legitimate access to iTunes’s built-in automatic “just plug in the device via USB and iTunes will see it” syncing. I don’t see that as the basis for government anti-trust action against Apple. Rather than write their own Mac and Windows software to recognize when a Pre is plugged in and sync media with the iTunes library, Palm is piggybacking on the software Apple wrote to support iPods.


Ultimately, my guess is that Apple won’t take any immediate action — technical or legal — against Palm. I think Apple will treat it more or less the way they’ve treated iPhone jailbreaking.


---

1. And, when judging the likelihood of Apple filing such a lawsuit, consider the perspective of a certain highly-competitive quasi-paranoid Apple founder and CEO who is famously sensitive to what he perceives as being “ripped off”. The one and only company to ship a product that successfully masquerades as an iPod via USB is the company whose engineering division is run by a former Apple senior VP and has hired a slew of former Apple engineers. ↩︎
2. And [a previous sponsor](http://daringfireball.net/linked/2008/05/02/doubletwist) of this site. ↩︎



| **Previous:** | [Why Palm’s WebOS ‘Media Sync’ iTunes Integration Can’t Be Legit](https://daringfireball.net/2009/06/webos_itunes_integration) |
| **Next:** | [Palm Saturday](https://daringfireball.net/2009/06/palm_saturday) |


PreviousNext