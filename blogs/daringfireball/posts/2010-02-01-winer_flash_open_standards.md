---
title: "What if Flash Were an Open Standard?"
date: 2010-02-01
url: https://daringfireball.net/2010/02/winer_flash_open_standards
slug: winer_flash_open_standards
word_count: 652
---


Some good questions [from Dave Winer regarding Apple, Adobe, and Flash](http://www.scripting.com/stories/2010/01/31/whatIfFlashWereAnOpenStand.html):


> What if Apple were trying to erase something that’s not
> company-owned? Either a formal or de facto standard? Further, what
> if their alternative were something that was locked-down and owned
> by a company? Further, what if the company was Apple?


I’d say that’d be a different ball of wax entirely. It would depend, for one thing, on the specific open / de facto standard technology.


But as for open *web* standards, the evidence — actions and shipping code, not just words — strongly indicate that Apple is a major proponent of them. Apple didn’t have to release WebKit as an open source project — they could have kept their extensions atop the LGPL-licensed WebCore private.1 They’ve re-written WebKit’s JavaScript engine from scratch at least twice, and released it all as open source. (Apple has also been aggressive about releasing its advanced non-web developer technology, [like blocks and LLVM](http://developer.apple.com/mac/library/DOCUMENTATION/Cocoa/Conceptual/Blocks/Articles/00_Introduction.html), as liberally-licensed open source.) All of Apple’s top competitors in the mobile space have either already adopted WebKit or soon will: Android, WebOS, even BlackBerry. Members of Apple’s WebKit team have been helping drive HTML5 since its inception. In short, I’d say Apple likes its technology open and its products closed.


E.g., it makes all the difference in the world that Apple is pushing H.264 rather than, say, QuickTime as the way forward for embedded web video.2


I do understand [the fear](http://www.guardian.co.uk/technology/2010/jan/31/ipad-review-comments-naughton). It’s indisputable that Apple seeks large amounts of control over its products. So it’s a reasonable question to ask whether Apple sees the web itself, which they have no control over, as a problem. I don’t think that’s the case at all, though. The web, as a whole, is arguably the single most entrenched computer technology ever created. So where Apple seeks control with regard to the web is in the technology to render it — HTML, CSS, JavaScript. No one can tell them what to do with WebKit; they wait for no one to shape and bend WebKit to suit their needs.


My feeling is not that Apple seeks total control over all content and software in iPhone OS. I’d say it’s more like they’re providing two well-defined, nice, neat, easily-understood extremes: the totally controlled native Cocoa Touch, and the totally open web.


Winer ends with a suggestion for Adobe:


> Adobe might want to consider, right now, very quickly, giving
> Flash to the public domain. Disclaim all patents, open source all
> code, etc etc. That would throw the ball squarely back into
> Apple’s court and would frame the question right now in its most
> stark terms.


That’d be an interesting move, and it would certainly shake things up. But what if the source code to Flash Player is  — as many would wager — a huge steaming pile of convoluted C++ horseshit? It’s sort of like what if Microsoft open-sourced the Internet Explorer rendering engine. It’s not like anyone who is now using WebKit or Gecko would switch to that just because it was opened — or that WebKit, Mozilla, and Opera would suddenly be obligated to or even interested in adopting IE-specific web features.


The problem for Flash is just like the problem for IE — the web has already moved on.


---

1. An earlier version of this article stated that the entirety of WebKit is BSD-licensed. That’s wrong; the [KHTML library](http://en.wikipedia.org/wiki/KHTML) that Apple started with is LGPL-licensed, and so therefore is the WebCore component in WebKit. We regret the error. ↩︎
2. H.264 is an open standard, but admittedly and unfortunately [not a free standard](http://shaver.off.net/diary/2010/01/23/html5-video-and-codecs/), hence Mozilla’s opposition to it. My point here is simply that H.264 is not owned by Apple or any other single company. ↩︎



| **Previous:** | [Who Can Do Something About Those Blue Boxes?](https://daringfireball.net/2010/01/blue_boxes) |
| **Next:** | [Macworld Expo Prelude](https://daringfireball.net/2010/02/macworld_expo_prelud) |


PreviousNext