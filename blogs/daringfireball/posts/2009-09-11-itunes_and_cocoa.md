---
title: "iTunes and Cocoa"
date: 2009-09-11
url: https://daringfireball.net/2009/09/itunes_and_cocoa
slug: itunes_and_cocoa
word_count: 1766
---


John Nack posted [a good devil’s advocate piece](http://blogs.adobe.com/jnack/2009/09/why_do_you_want_a_64-bit_itunes.html) regarding whether and why iTunes should ever go 64-bit. Nack asks:


> Do people really have performance problems* with iTunes as it
> is? I never have. It filters my 3,000-item library as fast as I
> can type, does a lovely job with HD video, and whips through
> album art in Cover Flow. I can’t recall others complaining,
> either.
> Do they want iTunes to use more than 4GB of RAM? I think we can
> safely say “No.”
> Do they complain about the UI (e.g. [non-standard
> scrollbars](http://macenstein.com/default/2009/09/is-itunes-9-sporting-marble/)) and think that Cocoa will make iTunes more “Mac-
> like”? Again, I haven’t heard complaints (or rather, only
> [ridiculous ones](http://blogs.adobe.com/jnack/2008/06/future_photoshop_ui.html#c1397794)).
> So what, then? Let me put it another way: If you were directing
> the iTunes team’s efforts, why would you — as a customer — tell
> them to spend their time on Cocoa and/or 64-bit, at the expense of
> doing other things customers want?


I, of all people, have certainly [never been one](http://daringfireball.net/s/carbon%20cocoa) to argue for Carbon-to-Cocoa rewrites just for the sake of Cocoa being better just because it’s Cocoa. And the same goes for 64-bit-ness. What really matters are features and user experience, not the developer technologies used to make them.


When I say it seems inevitable that Apple will eventually move iTunes to Cocoa and 64-bit, it’s not because those two things in and of themselves will dramatically improve the features and experience of the software. I say it seems inevitable because Apple has moved almost all of their “system apps” to 64-bit. Check out the first footnote on [Apple’s Snow Leopard Technology page](http://www.apple.com/macosx/technology/):


> All system applications except DVD Player, Front Row, Grapher, and
> iTunes have been rewritten in 64-bit.


Almost everything else that ships with Mac OS X is 64-bit now.1 Were customers demanding a 64-bit Dock? Has anyone’s life been changed now that the Dictionary app is 64-bit? Of course not. For some apps there really have been tangible performance improvements in the move to 64-bit, but the reason Apple has moved almost all their apps to 64-bit is simply because it’s now what they consider the best way to build Mac software. They are leading by example, preparing for the future.


The Finder is the best example to compare against iTunes. The Snow Leopard Finder didn’t just have to be ported from 32-bit to 64, it had to be ported from Carbon to Cocoa. In the early years of Mac OS X the Finder was the app Apple held up at WWDC as its Carbon “dog food” example — proof that it was using the Carbon APIs for an essential app. It was the Carbon poster child.


No matter how modern a Carbon app the Finder was (insofar as that it was written specifically for the then-new Carbon APIs on Mac OS X, not a port of old classic Mac OS code), it must have been a lot of engineering work to port it to Cocoa — with the result being an app that most users won’t notice being any different at all from the Carbon Finder in 10.5. [John Siracusa described the new Snow Leopard Finder](http://arstechnica.com/apple/reviews/2009/08/mac-os-x-10-6.ars/18) thus:


> The conversion to Cocoa followed the Snow Leopard formula: no new
> features… except for maybe one or two. And so, the “new” Cocoa
> Finder looks and works almost exactly like the old Carbon Finder.
> The biggest indicator of its “Cocoa-ness” is the extensive use of
> Core Animation transitions.


[Sven-S. Porst was a bit harsher](http://earthlingsoft.net/ssp/blog/2009/08/mac_os_x6_part2#finder):


> In short, people probably put a lot of effort into creating a
> Finder that sucks just as much as the old one but which can tag
> itself with the labels ‘64bit’ and ‘Cocoa’.


Cocoa was not magic pixie dust that inherently made the Finder radically better. But so why did Apple bother? Because Cocoa and 64-bit are the future of Mac OS X. And, for many new APIs, they are the *present*. [As Siracusa noted](http://arstechnica.com/apple/reviews/2009/08/mac-os-x-10-6.ars/5) in the 64-bit section of his Snow Leopard review:


> The second big carrot (or stick, depending on how you look at
> it) is the continued lack of 32-bit support for new APIs and
> technologies. Leopard [started the trend](http://arstechnica.com/apple/reviews/2007/10/mac-os-x-10-5.ars/6#clean-break), leaving
> deprecated APIs behind and only porting the new ones to 64-bit.
> The improved Objective-C 2.0 runtime introduced in Leopard was
> also 64-bit-only.
> Snow Leopard continues along similar lines. The Objective-C 2.1
> runtime’s non-fragile instance variables, exception model unified
> with C++, and faster vtable dispatch remain available only to 64-bit
> applications. But the most significant new 64-bit-only API is
> QuickTime X.


In short, there are new APIs and features in Mac OS X which are *only* available to 64-bit apps, and because there are no 64-bit Carbon APIs, *64-bit apps* implicitly means *64-bit Cocoa apps*.


Carbon has not been deprecated. There have been no warnings that the existing Carbon APIs will be going away in a future version of Mac OS X. Some of the biggest and most popular third-party apps, like Microsoft Office and the Adobe CS suite, are Carbon. Even if the next major releases of these apps are all ported to Cocoa, there are an awful lot of Mac users who are going to want to keep using the versions they’ve already bought. And, even if you’re not persuaded by Apple’s motivation to support third-party Carbon developers, note that nearly all of Apple’s own “Pro Apps”, like those in [Final Cut Studio](http://www.apple.com/finalcutstudio/), remain Carbon apps.


Maybe the Carbon APIs will never go away, but I wouldn’t bet on that. They’re certainly not going away *soon*, but *never* is a long time. And Apple’s new stuff is all 64-bit.


The writing has been on the wall ever since the planned-for 64-bit Carbon [was unceremoniously canned at WWDC 2007](http://daringfireball.net/2008/04/64000_question). The Classic Mac OS environment went away after just a few years. Rosetta (the PowerPC emulator) is no longer installed by default with Snow Leopard, and my guess is that it won’t be included at all in 10.7. Apple doesn’t just add things to Mac OS X — they remove old things. Carbon hasn’t been deprecated but Apple clearly considers it legacy technology, and Apple has demonstrated a strong institutional aversion to *legacy* anything.


The single most remarkable thing about Snow Leopard is that it is smaller than the previous version of the system. It is an operating system that is — and, going back to its roots at NeXT, has always been — evolving, not just growing. Apple doesn’t just add to it. They prune. They churn. And the track record shows that when it comes to ushering old technology out the back door, they err on the side of *too soon* rather than risk letting it linger too long. Apple worries about the way things *should be* far more than it worries about continuity with the way things *used to be*.


## The Cocoa Advantage for Users


A 64-bit Cocoa version of iTunes isn’t going to sync with your iPod faster just because of 64-bit Cocoa magic. But the new Snow Leopard Finder *does* show the subtle ways that a Cocoa rewrite has tangible advantages for users. System-wide services work in both Carbon and Cocoa apps via the Services menu, but only Cocoa apps pick up [the new-to-Snow-Leopard contextually-aware services](http://www.macosxautomation.com/services/download/index.html) in contextual menus. This is something Apple added to Cocoa, so all Cocoa apps get it “free”, including the new Finder. iTunes 9, because it’s Carbon, does not.


Another example. Long-time DF readers may remember “[Highly Selective](http://daringfireball.net/2006/08/highly_selective)”, a piece I wrote three years ago regarding the two UI models for selecting multiple items in a list using the keyboard: anchored and unanchored. I argued (successfully, it turns out) in favor of the anchored model, and lamented the fact that Cocoa, and therefore most Mac software, used the unanchored model. That [changed in Leopard](http://daringfireball.net/2008/02/anchored_selection), when Apple improved the Cocoa standard list control (NSTableView) to use the anchored model. All of a sudden, *all* Cocoa apps switched from the inferior unanchored selection model to the superior anchored model. But list selection in Carbon apps like iTunes and the Finder remained unchanged (and, alas, unanchored).


The Snow Leopard Finder, now that it’s a Cocoa app, offers anchored selection. iTunes 9, still Carbon, does not. These little bits of functionality and system-wide consistency constitute the Cocoa advantage.


The big difference between iTunes and the Finder is that iTunes is cross-platform. There is no Windows version of the Finder. (And even on the Mac, iTunes 9 still runs on 10.4 and 10.5, whereas the 10.6 Finder only has to run in 10.6.) As with most Mac/Windows cross-platform apps, the Mac version is Carbon, not Cocoa. Much, if not most, of the reason for this is historical — most of the big cross-platform apps date back to a decade ago, when the Mac version couldn’t be written in Cocoa because Mac OS X wasn’t out yet. That’s true for Microsoft Office, it’s true for Adobe’s CS suite, it’s true for Firefox, and it’s even true for iTunes.


One great counterexample is, in fact, from Adobe. [Lightroom](http://www.adobe.com/products/photoshoplightroom/) is a cross-platform app and the Mac version isn’t just Cocoa, it was the [first mainstream Cocoa app I’m aware of to support 64-bit mode](http://blogs.oreilly.com/lightroom/2008/05/lightroom-2-and-64bits.html) (ahead of even Apple itself). If and when iTunes does make the move to 64-bit Cocoa, I expect it to resemble Lightroom architecturally: relatively thin UI layers written with the native Mac and and Windows APIs, with most of the code residing in cross-platform compiled libraries and scripting runtimes. But whereas Lightroom uses [Lua](http://www.lua.org/) as a cross-platform scripting runtime, my money says Apple would use WebKit for iTunes.


The growing use of WebKit in iTunes today could be a step in that direction. Apple didn’t have to write separate Mac and Windows renderers for the new iTunes LP content or the new iTunes Store — they just used WebKit, which already works great on both OSes.


And, of course, Apple itself has a big cross-platform app that’s a 64-bit Cocoa app on Snow Leopard. It’s called Safari.


---

1. Ends up Podcast Capture (in the */Applications/Utilities/* folder, is still 32-bit, too. Not sure if there are any others Apple’s footnote neglects to mention. ↩︎



| **Previous:** | [It’s Only Rock and Roll Event Prelude](https://daringfireball.net/2009/09/rock_and_roll_prelude) |
| **Next:** | [Snow Leopard Compatibility Tweaks for That Thing I Wrote in January About Writing AppleScripts That Dynamically Target Either Safari or WebKit](https://daringfireball.net/2009/09/snow_leopard_applescript_perl_safari_webkit) |


PreviousNext