---
title: "The Tragedy of Safari 15 for Mac’s ‘Tabs’"
date: 2021-10-01
url: https://daringfireball.net/2021/10/the_tragedy_of_safari_15_quote_unquote_tabs
slug: the_tragedy_of_safari_15_quote_unquote_tabs
word_count: 2371
---


Our [long national iOS 15 Safari nightmare ended last month](https://daringfireball.net/linked/2021/08/18/ios-15-safari-beta-6), praise be, but the lesser of the two bad Safari designs unveiled at WWDC persists and [actually shipped](https://daringfireball.net/linked/2021/09/25/try-safari-15-tech-preview): the new tabs in Safari 15 for Mac. Safari 15 on iPad suffers similarly, but it’s the Mac version I’ll concentrate on here.


The most controversial Mac Safari changes shown at WWDC — compressing tabs and the URL location field into a single row at the top of each window, and coloring the entire window with the accent color of the currently frontmost web page — are settings that (thankfully) can be turned off in Safari’s Preferences window (under “Tabs”, natch). The “Compact” layout that puts tabs and the location field in the same row — by using the tabs themselves as the text editing fields for URLs — is, thankfully, off by default. But the “Show color in tab bar” option is *on* by default:


[
](https://daringfireball.net/misc/2021/10/safari-15-default-tab-prefs.png)


Here’s what it looks like as you switch back and forth between tabs with this option on. (Note that I’ve done nothing, explicitly, to support this feature on Daring Fireball.)


Apple, in [the “What’s New in Safari” alert](https://daringfireball.net/misc/2021/10/whats-new-in-safari.png) that’s shown upon first run after upgrading to Safari 15, describes the new tabs thus:


> **Redesigned tabs**


This is nonsense. The color matching does not extend web pages at all. It just *looks* like it does. Who, for example, owns this button?


Is that Defector’s button? Or is it Safari’s? It sure as shit looks like it’s Defector’s — but it’s Safari’s. Click that thinking it’s a menu for Defector and you’ll be surprised to be dumped to your Safari Start Page.


I despise the new tabs even when the “Show color in tab bar” and “Compact” layout settings are turned off. *They don’t look like tabs.* They look like buttons. Here are four full-window screenshots, in order from worst to best to my liking:

1. [“Compact” tab layout / “Show color in tab bar” on](https://daringfireball.net/misc/2021/09/safari-15-mac-tabs-compact-with-colors.png)
2. [“Compact” tab layout / “Show color in tab bar” off](https://daringfireball.net/misc/2021/09/safari-15-mac-tabs-compact-no-colors.png)
3. [“Separate” tab layout / “Show color in tab bar” on](https://daringfireball.net/misc/2021/09/safari-15-mac-tabs-with-colors.png)
4. [“Separate” layout / “Show color in tab bar” turned off](https://daringfireball.net/misc/2021/09/safari-15-mac-tabs-no-colors.png)


The “Separate” layout, with “Show color in tab bar” off, is the closest you can get to Safari’s previous tab design. These new “tabs” waste space because, like buttons, they’re spaced apart. Tabs that look like real-world tabs aren’t just a decorative style. They’re a visual metaphor. My brain likes visual metaphors. It craves them. And my brain is very much comfortable with the particular visual metaphor of tabs in a web browser window. Buttons do not work as a metaphor for multiple documents within a single window. Thus, trying to use the new Safari 15 on Mac (and iPadOS 15, alas), I feel somewhat disoriented working within Safari. I have to *think*, continuously, about something I have *never had to think about* since tabbed browsing became a thing almost 20 years ago.1 The design is counterintuitive: What sense does it make that no matter your settings, the active tab is rendered with *less* contrast between the tab title and the background than background tabs? The active tab should be the one that pops.


Safari actually debuted as a public beta in January 2003 without any support for tabbed browsing (which, humorously, [I was OK with](https://daringfireball.net/2003/01/safari) — the tab habit hadn’t gotten its grips on me yet), but within a few weeks [it had tabs](https://daringfireball.net/2003/05/safaris_unscriptable_tabs). Apart from that brief weeks-long stint when it debuted as a public beta in 2003, Safari for Mac has always had tabs. And those tabs have always looked like tabs, because why would anyone want to make them look like anything other than tabs? There are certainly a lot of ways to style tabs in a UI. Try different browsers, try different windowing OSes, and you’ll see many different takes on tabs. Even the Safari team at Apple has experimented with various different tab styles — most famously, in 2009, when they put the tabs at the top of the window for Safari 4’s public beta. It was an experiment Apple wound up abandoning, but they didn’t need to — it could have worked well with some tweaking, as I explored [in a copiously illustrated post](https://daringfireball.net/2009/03/safari_4_public_beta) at the time.


Google Chrome — and Chrome-derivatives like [Brave](https://brave.com/) and [Microsoft Edge](https://www.microsoft.com/en-us/edge/features) — now use tabs-on-top layouts very much like what the Safari team experimented with in 2009. It’s a fine design that confuses no one. They work because they both look like tabs and embrace the tab metaphor.


Not so with Safari 15. Consider a window with two tabs, perhaps both from the same website. A very common scenario, I think it’s fair to say. With Safari 15, it’s almost a guessing game, a coin flip, when you want to determine which tab is active:


[
](https://daringfireball.net/misc/2021/10/safari-15-two-tabs-light.png)


It’s even more ambiguous in dark mode:


[
](https://daringfireball.net/misc/2021/10/safari-15-two-tabs-dark.png)


In Safari 14 — as well as Safari versions 1–13, and *every other browser I’m aware of* — there’s never any ambiguity about which tab is active, in either light mode or dark mode:


[
](https://daringfireball.net/misc/2021/10/safari-14-two-tabs-light.png)


[
](https://daringfireball.net/misc/2021/10/safari-14-two-tabs-dark.png)


There’s no ambiguity because the tabs are visually connected to the rest of the browser chrome, and the browser chrome is rendered in a way to make it visually distinct from the web page content. There’s no ambiguity because the first job of any tab design ought to be to make clear which tab is active. I can’t believe I had to type that sentence. But here we are.


Yes, it gets easier to discern the active tab with more than two tabs in a window, because any confusion as to whether darker or lighter indicates “active” is alleviated by having only one tab shaded differently than the others. But the utter failure of the new Safari tab design with exactly two tabs should have been reason enough to scrap this idea while it was experimental. Replacing an interface that doesn’t require you to think at all with an interface that requires you to think — even a little — is a design sin of the first order. Designs should evolve over time in the *other* direction.


Does the Safari 15 tab design look cooler, particularly with the default coloring? I say no. I think it’s novel, obviously, but suspect it’s going to get old quickly. But even if you think it looks cool as fuck, that’s not what user interface design is about. A good user interface needs to *work* first, then worry about looking cool.


The Safari 15 tab design is a blatant violation of [Steve Jobs’s oft-cited “Design is how it works” axiom](https://www.nytimes.com/2003/11/30/magazine/30IPOD.html?ex=1386133200&en=750c9021e58923d5&ei=5007&partner=USERLAND):


> Most people make the mistake of thinking design is what it looks
> like. People think it’s this veneer — that the designers are
> handed this box and told, “Make it look good!” That’s not what we
> think design is. It’s not just what it looks like and feels like.
> Design is how it works.


If I were preparing a lecture for design students about what Jobs meant, I’d use Safari 14 and 15’s tab designs as examples. If anything, Safari 15 feels like a ginned-up example — too obviously focused solely on how it looks, too obviously callous about how it works. If it hadn’t actually shipped to tens of millions of Mac users as a software update, you’d think it was a straw man example of misguided design.


Functionality? Here’s functionality. In Safari 14, the close tab button is just to the left of each tab’s [favicon](https://daringfireball.net/linked/2018/09/17/safari-12-favicons). In Safari 15, bizarrely, the favicon turns into a close button on hover. First, hiding functionality behind unguessable hover states is a bad idea, but [a hallmark of Apple’s current HI team’s fetish for visual minimalism](https://daringfireball.net/2021/07/document_proxy_icons_macos_11_and_12). But turning an icon into a close button? Good god. [Guy English, back on June 18](https://twitter.com/gte/status/1405893048635174919):


> Safari beta on macOS 12 tabs have a real anti-pattern: the favicon
> in the tab turns out to be the close tab button on hover. So if
> you aim at the favicon you’ll close the tab. The only place in the
> entire OS where clicking an icon will delete the object you were
> interested in.


It’s hard to express in words how perverse this is. The icon that represents the web page is a destructive button for that web page. Imagine clicking a document icon in the Finder to trash it.


Speaking of close buttons, if you open a dozen or so tabs in a window in Safari 15, the “tabs” shrink to just show the favicons. When this happens, close boxes stop appearing on non-frontmost tabs, even on hover. So how can you close these tabs without first activating them? To close them while they’re not frontmost, you need to hold down the Command key while you move the mouse over them. Guess how many people are going to figure that out? (Not many.) Safari 14 does this too, but because its actual *tab* tabs are more space efficient, you have to open *way* more tabs in a window to get to the point where close boxes only appear for non-frontmost tabs while holding down the Command key.


From a usability perspective, every single thing about Safari 15’s tabs is a regression. Everything. It’s a tab design that can only please users who do not use tabs heavily; whereas the old tab design scaled gracefully from “*I only open a few tabs at a time*” all the way to “*I have hundreds of tabs open across multiple windows*”. That’s a disgrace. The Safari team literally invented the standard for how tabs work on MacOS. The tabs that are now available in the Finder, Terminal, and optionally in all document-based Mac apps are derived from the design and implementation of Safari’s tabs. Now, Apple has thrown away Safari’s tab design — a tab design that was not just best-of-platform, but arguably best-in-the-whole-damn-world — and replaced it with a design that is both inferior in the abstract, and utterly inconsistent with the standard tabs across the rest of MacOS.


The skin-deep “looks cool, ship it” nature of Safari 15’s tab design is like a fictional UI from a movie or TV show, like [*Westworld*’s foldable tablets](https://duckduckgo.com/?q=westworld+tablet+ui) or [Tony Stark’s systems from *Iron Man*](http://www.johnkoltai.com/IRON-MAN-2-UI-Design), where looking cool is the entirety of the design spec. Something designed not by UI designers but by graphic designers, with no thought whatsoever to the affordances, consistencies, and visual hierarchies essential to actual usability. Just what looks cool. This new tab design shows a complete disregard for the familiarity users have with Safari’s existing tab design. Apple never has been and should not be a company that avoids change at all cost. But proper change — change that breaks users’ habits and expectations — is only justifiable when it’s an improvement. Change for change’s sake alone is masturbatory. That with Safari 15 it actually makes usability *worse*, solely for flamboyant cosmetic reasons, is downright perverse.


[Safari debuted in 2003](https://www.apple.com/newsroom/2003/06/23Apple-Releases-Safari-1-0/) as the only major browser on Mac OS X with a first-class Mac interface.2 It remains the only major browser with a truly native Mac interface 18 years later. Safari hasn’t just been a Mac-assed Mac app, it’s been one of the best Mac apps, period — the sort of app UI designers turn to when they need to study how a proper Mac app implements something in its interface.


As someone who depends upon my web browser and relishes Mac apps that do things the Macintosh way, I’m angry. But I can only imagine how furious the WebKit team at Apple is. Safari is the app and WebKit is the rendering engine, but from a practical perspective they’re one and the same, because — again — Safari is the only major WebKit browser for the Mac. Not because there couldn’t be other great Mac WebKit browsers, but because Safari has been so good *as a Mac app* for so long, it left no room for a third-party Mac WebKit browser to gain traction.


The team that came up with these Safari redesigns shown at WWDC [almost destroyed](https://daringfireball.net/2021/07/safari_15_public_betas_for_mac_and_ios) iOS Safari. Apple [changed course](https://daringfireball.net/linked/2021/07/27/safari-15b4-toolbar-viticci) over the summer and [avoided that disaster](https://daringfireball.net/linked/2021/08/18/ios-15-safari-beta-6). But though good design sense prevailed and iOS Safari was spared, the same design team has been allowed to disfigure Mac (and iPad) Safari. It’s one thing when a bad UI design ships in a new or obscure Mac app from Apple; it’s another thing altogether for what’s almost certainly, by any measure, the *single most-used app* on the platform.


Web developers argue endlessly about the underlying differences in capabilities of rendering engines. Users don’t think like that, though. They just want to use a browser that works, and that feels familiar and gets out of their way. Safari 15 for Mac is the opposite — it is unfamiliar and in your face.


Safari 15 for Mac is a tragic own goal — a de facto gift to Chrome and [its growing browser hegemony](https://gs.statcounter.com/browser-market-share). The option to turn off “Show color in tab bar” is an admittedly appreciated glass of ice water in hell. But true relief from the boiling hot sun of these craptacular “tabs” is just a download away. Google could and should run ads targeting Safari users, with a simple welcoming message: *Switch to Chrome, the Mac browser where tabs look like tabs.*


---

1. I decided to check on this, and I’m glad I did. Tabbed browsing didn’t go mainstream until after the year 2000, but there were tabbed browsers as early as 1994, [in a Windows web browser named NetCaptor written by Adam Stiles](https://www.buzzfeednews.com/article/josephbernstein/meet-the-man-who-invented-tabs). Look closely for the tabs in those screenshots — they’re at the bottom of the windows. ↩︎
2. The team behind [Camino](https://caminobrowser.org/), an open source Mac browser based on Mozilla’s Gecko rendering engine that debuted under the name Chimera [all the way back in 2002](https://www.macworld.com/article/153763/chimera.html), did yeoman’s work to make Camino [as Mac-like as it was](https://daringfireball.net/search/camino). They could not out-Mac Safari though. ↩︎︎



| **Previous:** | [Why Does the iPhone Still Use Lightning?](https://daringfireball.net/2021/09/why_still_lightning) |
| **Next:** | [Apple Watch Series 7](https://daringfireball.net/2021/10/apple_watch_series_7) |


PreviousNext