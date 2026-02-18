---
title: "The Whole Thing About Adobe’s Flash Player Not Having Access to H.264 Hardware Acceleration on Mac OS X"
date: 2010-02-20
url: https://daringfireball.net/2010/02/flash_hardware_acceleration
slug: flash_hardware_acceleration
word_count: 430
---


[Wil Shipley on Twitter](http://twitter.com/wilshipley/status/9363515820), presumably in response to [this](http://daringfireball.net/linked/2010/02/19/coldeway) (and where by “other platforms”, Shipley apparently means “Microsoft Windows”):


> Hmm, @gruber ignores that Flash on other platforms can and does
> use hardware H.264 decoding, but Apple won’t give Adobe access.


I didn’t mention the issue yesterday, no, but I wrote [a whole section about it in this piece](http://daringfireball.net/2010/01/apple_adobe_flash#performance) a few weeks ago, and I specifically linked to Adobe’s own [FAQ](http://labs.adobe.com/technologies/flashplayer10/#FAQ) and [weblog entry](http://theflashblog.com/?p=1641) on the issue.


I think the issue is a red herring, spin from Adobe intended to share the blame for Flash’s Mac OS X performance with Apple. First, Flash performance gripes are not limited to H.264 video playback. *Everything* Flash Player does is slower on Mac OS X than Windows. What’s Adobe’s excuse for Flash’s performance on non-H.264 video?


Second, even Apple’s own [QuickTime on Snow Leopard](http://www.apple.com/macosx/specs.html) only [makes use of H.264 hardware acceleration with a single graphics card](http://www.macrumors.com/2009/06/10/snow-leopard-h-264-hardware-acceleration-and-opencl-requirements/): the Nvidia 9400M. If you don’t have that graphics card in your Mac, you don’t get H.264 hardware acceleration, period. That card is used across the board in current MacBooks and Mac Minis, but there are an awful lot of older Macs in use — a majority I’d wager — which don’t have that card. It’s also not present in current brand-new Mac Pros and most iMacs.


Third, no one is complaining about the lack of hardware acceleration for other video playback software on Mac OS X, like [VLC](http://www.videolan.org/vlc/download-macosx.html), [Movist](http://code.google.com/p/movist/), [Perian](http://perian.org/), or even (as mentioned in the previous paragraph) QuickTime itself on machines without the Nvidia 9400M. Even if we concede the point that Flash Player’s lack of access to H.264 hardware acceleration on Mac OS X inherently blocks it from matching its H.264 playback performance on Windows, I fail to understand how that blocks it from matching the performance of other video playback software on Mac OS X itself.


**Update:** Fourth, hardware accelerated H.264 support is [a new feature in the as-yet-unreleased Flash Player 10.1](http://labs.adobe.com/technologies/flashplayer10/releasenotes.pdf). It in no way explains the performance difference in Flash Player 10.0 on Mac OS X and Windows.


Lastly, does anyone really think it would be a good idea for web content plugins to have direct access to graphics card hardware? Is it absurd to think that it’s a reasonable OS design to limit *plugins* to higher-level APIs? Should Flash Player be a kernel extension, so that it can ensure it gets plenty of CPU cycles and have direct access to whatever hardware it wants?



| **Previous:** | [Macworld Expo Prelude](https://daringfireball.net/2010/02/macworld_expo_prelud) |
| **Next:** | [Tits and Apps](https://daringfireball.net/2010/02/tits_and_apps) |


PreviousNext