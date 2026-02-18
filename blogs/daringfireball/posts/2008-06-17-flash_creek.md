---
title: "Up Flash Creek Without a Paddle"
date: 2008-06-17
url: https://daringfireball.net/2008/06/flash_creek
slug: flash_creek
word_count: 713
---


So there’s been a surge in speculation today regarding Adobe’s efforts to get Flash support on the iPhone, after Adobe CEO Shantanu Narayen [said the following](http://www.alleyinsider.com/2008/6/adobe_flash_apple_iphone_maybe_someday) during Adobe’s quarterly finance conference call yesterday:


> “We have a version that’s working on the emulation. This is still
> on the computer and you know, we have to continue to move it from
> a test environment onto the device and continue to make it work.
> So we are pleased with the internal progress that we’ve made to
> date.”


In addition to [my comments this morning](http://daringfireball.net/linked/2008/june#tue-17-adobe_flash) regarding how, at a technical level, getting Flash running in the simulator in and of itself isn’t worth much, the more I think about it, the more baffled I am that Narayen said anything specific at all.


Talking about technical progress only serves to focus attention on the fact that it is Apple’s decision, and by all appearances, Apple does not want Flash on the iPhone. Even if Adobe eventually gets Flash running well — by any standard for “running well” — on actual iPhone hardware, rather than just in the iPhone simulator, they can’t ship it without Apple’s explicit permission.


What most people imagine when they think of “Flash for the iPhone” is a browser plugin that executes and displays Flash content inside web pages, just like how it works in desktop browsers like Safari, Firefox, and IE. That requires a content plugin for the browser, and MobileSafari does not support plugins of any kind. There is no way for third-party developers to modify MobileSafari or the content it is capable of displaying via the iPhone SDK.


It is possible, of course, that Adobe is developing a Flash plugin for MobileSafari *outside* the confines of the APIs in the official iPhone SDK, with the permission and tacit approval of Apple. But at least [as recently as March](http://www.informationweek.com/news/mobility/messaging/showArticle.jhtml?articleID=206904789), Adobe indicated that no such deal was in place:


> In an emailed statement, Adobe said it had evaluated the iPhone
> software development kit Apple had released March 6 in beta, and
> could now “start to develop a way to bring Flash player to the
> iPhone.”
> “However, to bring the full capabilities of Flash to the iPhone
> Web-browsing experience, we do need to work with Apple beyond and
> above what is available through the SDK and the current license
> around it,” the company said.


But it’s worth taking a step back to consider that Apple doesn’t even support playing inline *QuickTime* content in MobileSafari web pages — clicking a QuickTime movie in MobileSafari takes you to a standalone QuickTime player. The iPhone is simply too performance sensitive to allow for inline media playback.


So, if not a MobileSafari browser plugin, then perhaps Adobe is working on a standalone Flash player app for the iPhone. But if that’s the case, (a) it would still require help from Apple in order to allow users to tap on Flash links in MobileSafari to launch the standalone Flash player; and (b) it would contravene this portion of the [iPhone SDK Agreement](http://developer.apple.com/iphone/):


> An Application may not itself install or launch other executable
> code by any means, including without limitation through the use of
> a plug-in architecture, calling other frameworks, other APIs or
> otherwise. No interpreted code may be downloaded and used in an
> Application except for code that is interpreted and run by Apple’s
> Published APIs and built-in interpreter(s).


Again, Apple could grant Adobe an explicit exception to this, but, as I’ve written before, [it is not in Apple’s interests to do so](http://daringfireball.net/2008/02/flash_iphone_calculus).


Lastly, if not a standalone Flash content player, the only other option would be for Adobe to build an entire iPhone web browser with Flash support built in. But, in addition to being an extraordinary amount of work (MobileSafari is a lot more than a “simple” wrapper around WebKit), this would contravene the exact same “no interpreted code” iPhone SDK terms that a standalone Flash player app would. Plus it would require Apple to allow for MobileSafari to be replaced as the default handler for the “http:” and “https:” URL schemes.



| **Previous:** | [The iPhone 3G Upgrade Question](https://daringfireball.net/2008/06/iphone_3g_upgrade) |
| **Next:** | [WWDC 2008 Miscellany](https://daringfireball.net/2008/06/wwdc_miscellany) |


PreviousNext