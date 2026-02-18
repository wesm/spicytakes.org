---
title: "Why Palm’s WebOS ‘Media Sync’ iTunes Integration Can’t Be Legit"
date: 2009-06-01
url: https://daringfireball.net/2009/06/webos_itunes_integration
slug: webos_itunes_integration
word_count: 827
---


There seems to remain some confusion regarding Palm’s recently announced “media sync” feature in WebOS, the brand-new OS that powers their soon-to-be-released Pre. [Here’s how Palm describes it](http://investor.palm.com/releasedetail.cfm?ReleaseID=386488):


> Palm media sync is a feature of webOS that synchronizes seamlessly
> with iTunes, giving you a simple and easy way to transfer DRM-free
> music, photos and videos to your Palm Pre.(2) Simply connect Pre
> to your PC or Mac via the USB cable, select “media sync” on the
> phone, and iTunes will launch on your computer desktop. You can
> then choose which DRM-free media files to transfer.


The “(2)” is a footnote which states:


> (2) Compatible with iTunes 8.1.1 on Windows XP/Vista and Mac OS X
> version 10.3.9-10.5.7.


Last week I linked to [Jon Lech Johansen’s analysis](http://nanocr.eu/2009/05/28/syncing-music-and-video-to-the-palm-pre/) as to how they might be achieving this. His theory, which I believe is correct, is that when a Pre enters “media sync” mode, it masquerades as an iPod by using Apple’s USB vendor ID and a USB device ID that matches that of some specific iPod model. I.e. that the Pre is telling iTunes Helper (the background process that looks for USB-attached iPods and iPhones), “Hey, I’m an iPod.”


Several readers emailed to ask whether Palm might be doing this legitimately, using the iTunes plugin API for third-party MP3 players. Apple has a support web page that lists such players [here](http://support.apple.com/kb/HT2172).


Palm is clearly not using this method, however. First and foremost, this API requires device-specific iTunes plugins, and it *has only ever worked on the Mac*. Pre’s “media sync”, which apparently at this point only means “iTunes sync”, does not require the installation of any software on your computer, and it works on Windows.


Second, this API is *old* and Apple no longer licenses it to third-party device makers. Look at the list of players — they’re from the MP3 player stone age. In fact, this API is so old that it dates back not just to Mac OS 9, not just to before there was a Windows version of iTunes, not just to before Apple introduced the first iPod, but all the way back to before there was even *iTunes*. It dates back to [SoundJam](http://www.panic.com/extras/audionstory/popup-sjstory.html), the Mac MP3 player published by Casady & Greene that Apple bought to create the foundation for what became iTunes.


Third, if you’re still holding out any sort of hope that Palm is using some sort of heretofore sanctioned, semi-sanctioned, or even maybe-sorta-kinda-sanctioned-if-you-squint-your-eyes means for a third-party device to sync with iTunes via USB, note that the Pre, when connected to iTunes, [is labelled as an “iPod”](http://video.allthingsd.com/video/d7-video-jon-rubinstein-and-roger-mcnamee-highlights/2EA37224-CF59-4066-9850-C37FD407A770). If you think Apple would ever allow the use of “iPod” to describe anything other than an actual iPod, you’re nuts.


There is no method sanctioned by Apple for WebOS to do what it is doing, and Johansen’s theory is the only one I’ve seen which matches what we know about how it works.


There’s no question that what Palm has done is clever. With the exception of DRM-encrypted music and video, it provides Pre owners with the regular iTunes media syncing experience — which is to say the *best* media syncing experience. And so I can see why Palm was tempted to do this.


But it seems risky and unbecoming for a company of Palm’s stature. It’s a hack, and if they’re really using Apple’s USB vendor and/or device IDs, it’s a duplicitous hack. It could well break with a future iTunes upgrade. (For all I know, it’s already broken with the iTunes 8.2 update [released earlier today](http://support.apple.com/downloads/iTunes_8_2_for_Mac).) If Apple finds a way that Palm’s iTunes integration hack differs from that of the actual iPod it is masquerading as, Apple could change iTunes to block it. At that point, an advertised Pre feature would be broken. What does Palm do then? Start a cat-and-mouse game? Advise Pre users against updating their copies of iTunes?


In terms of legal risk, this move almost makes me think that Palm is *trying* to provoke Apple into filing a lawsuit. The danger for Palm in such a suit is with all of the former Apple engineers now working for Palm. (There are many.) Did they use inside knowledge of the iPod/iTunes USB interface to implement the WebOS “media sync” feature? Palm’s not stupid — or at least Jon Rubinstein is not — so I would wager that Palm was careful to [“clean-room” reverse-engineer](http://en.wikipedia.org/wiki/Clean_room_design) the protocol. But if Apple sues, Palm would be forced to prove this in court, and in the meantime, they could be faced with the public perception that they’ve stolen Apple’s IP.


I know Palm is now the underdog, and I’m rooting for the Pre to be a success. Competition is good for the industry. But this move strikes me as more desperate than scrappy.



| **Previous:** | [Excerpts From the Diary of an App Store Reviewer](https://daringfireball.net/2009/05/diary_of_an_app_store_reviewer) |
| **Next:** | [More on Palm’s WebOS ‘Media Sync’](https://daringfireball.net/2009/06/more_on_webos_media_sync) |


PreviousNext