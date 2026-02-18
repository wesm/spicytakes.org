---
title: "Electron and the Decline of Native Apps"
date: 2018-12-07
url: https://daringfireball.net/2018/12/electron_and_the_decline_of_native_apps
slug: electron_and_the_decline_of_native_apps
word_count: 1423
---


[SwiftOnSecurity, regarding Microsoft’s switch to Chromium as Windows’s built-in rendering engine](https://twitter.com/SwiftOnSecurity/status/1069776335336292352):


> This isn’t about Chrome. This is about ElectronJS. Microsoft
> thinks EdgeHTML cannot get to drop-in feature-parity with Chromium
> to replace it in Electron apps, whose duplication is becoming a
> significant performance drain. They want to single-instance
> Electron with their own fork.
> Electron is a cancer murdering both macOS and Windows as it
> proliferates. Microsoft must offer a drop-in version with native
> optimizations to improve performance and resource utilization.
> This is the end of desktop applications. There’s nowhere but
> JavaScript.


I don’t share the depth of their pessimism regarding native apps, but Electron is without question a scourge. I think the Mac will prove more resilient than Windows, because the Mac is the platform that attracts people who care. But I worry.


In some ways, the worst thing that ever happened to the Mac is that it got so much more popular a decade ago. In theory, that should have been nothing but good news for the platform — more users means more attention from developers. The more Mac users there are, the more Mac apps we should see. The problem is, the users who really care about good native apps — users who know [HIG](https://developer.apple.com/design/human-interface-guidelines/macos/) violations when they see them, who care about performance, who care about Mac apps being *right* — were mostly already on the Mac. A lot of newer Mac users either don’t know or don’t care about what makes for a good Mac app.


There have always been bad Mac apps. But they seldom achieved any level of popularity because Mac users, collectively, rejected them. Microsoft Word 6.0 is the canonical example. Word 5 for Mac was a beloved app and solid Mac citizen. Word 6 was a cross-platform monstrosity. Mac users rejected it, and its rejection prompted Microsoft — at the height of its mid-’90s power and arrogance — to completely re-think its Mac strategy and create a new business unit devoted to the Mac. [Microsoft’s Rick Schaut wrote a terrific piece on the whole saga back in 2004](https://blogs.msdn.microsoft.com/rick_schaut/2004/02/26/mac-word-6-0/):


> OK, so Mac Word 6.0 was big and slow relative to the memory that
> most computers had available at the time we shipped it, but that’s
> not the reason why Mac Word 6.0 was such a crappy product, or at
> least not directly. [...]
> Moreover, while people complained about the performance, the
> biggest complaint we kept hearing about Mac Word 6.0 was that it
> wasn’t “Mac-like.” So, we spent a lot of time drilling down into
> what people meant when they said it wasn’t “Mac-like.” We did
> focus groups. Some of us hung out in various Usenet newsgroups. We
> talked to product reviewers. We talked to friends who used the
> product. It turns out that “Mac-like” meant Mac Word 5.0.
> We spent so much time, and put so much effort into, solving all
> the technical problems of Mac Word 6.0 that we failed to make the
> UI of Mac Word 6.0 behave like Mac Word 5.0. [...]
> The other thing we figured out as a result of coming to understand
> what “Mac-like” meant was that we weren’t going to be able to
> deliver “Mac-like” products if Office remained a singular product
> from which both the Win and Mac versions were built. The mere fact
> that “Mac-like” was an issue at all meant that there were some
> fundamental differences between the Win Word market and the Mac
> Word market. If we were to understand both those markets, then our
> Mac products and Win products needed separate marketing and PGM
> organizations. The lessons we learned from Mac Word 6.0 are some
> of the reasons that Mac BU exists today.


I disagree, strongly, with one aspect of this: what Mac Word users saw as Mac-like wasn’t whatever Word 5 was — it was that Word 5 really was Mac-like in design. Word 6 wasn’t objected to for being different, it was objected to for being literally un-Mac-like. It looked and worked like Word for Windows.


As un-Mac-like as Word 6 was, it was far more Mac-like then than Google Docs running inside a Chrome tab is today. Google Docs on Chrome is an un-Mac-like word processor running inside an [ever-more-un-Mac-like web browser](https://twitter.com/gruber/status/1062419383350448128). What the Mac market flatly rejected as un-Mac-like in 1996 was better than what the Mac market tolerates, seemingly happily, today. Software no longer needs to be Mac-like to succeed on the Mac today. That’s a tragedy.


Even Apple, of all companies, is shipping Mac apps with glaring un-Mac-like problems. The “Marzipan” apps on MacOS 10.14 Mojave — News, Home, Stocks, Voice Memos — [are dreadfully bad apps](http://benjaminmayo.co.uk/marzipan). They’re functionally poor, and design-wise foreign-feeling. I honestly don’t understand how Apple decided it was OK to ship these apps.


Another one I just ran into on Mojave is the new Mac App Store app. It certainly looks nice, [but I noticed a few days ago that it doesn’t support the Page Down and Page Up keys for scrolling](https://twitter.com/gruber/status/1070339868184797184) (nor the Home and End keys for jumping to the top and bottom) in *any* of its views.1 Open an article and hit Page Down, and instead of scrolling down, it just beeps. Beeps, I say. The only way to scroll is with a mouse or trackpad. In an app from Apple, used by nearly everyone. Even the Marzipan apps support these keys for scrolling, which shouldn’t be surprising, because support for these keys and other standard behavior comes for free with the underlying developer frameworks. The Mojave App Store app must be doing something [very strange](https://twitter.com/lapcatsoftware/status/1070346157442981890) for these keys *not* to work.2


The Mojave App Store app certainly isn’t written using Electron. But the problem with Electron apps isn’t really Electron — it’s the decline in demand for well-made native Mac apps. And that is ominous. The biggest threat to the Mac isn’t iPads, Chromebooks, or Windows 2-in-1’s — it’s apathy towards what makes great Mac apps great. [As I tweeted regarding this Page Down/Up thing](https://twitter.com/gruber/status/1070349550387380225):


> Things like this are canaries in the coal mine regarding the state
> of the Mac. If even Apple doesn’t get basic fundamentals — like
> supporting Page Up/Down, things which should work in a scrolling
> view out of the box — how are we to expect any developer to?


The new App Store app on Mojave certainly looks better. But developers at Apple, of all companies, should know that [design is how it works](https://daringfireball.net/linked/2007/01/23/how-it-works).


---

1. After posting about this to Twitter, a couple of people argued that it should be no surprise that these keys don’t work because modern Apple keyboards don’t have these keys. First, that’s wrong — the large Magic Keyboard has these keys. But even if you’re using a MacBook or a smaller keyboard you can use them using the Fn key. Fn↓ = Page Down; Fn↑ = Page Up; Fn← = Home; Fn→ = End. Enjoy. ↩︎
2. While I’m in full-on **you-kids-get-the-hell-off-my-lawn** mode here, let me mention another Mojave gripe that is clearly the work of young developers at Apple. The Finder’s File → Show Original command has had the shortcut ⌘R since, I think, System 6. (Select an alias or symlink and this command will reveal the original file.) File → Make Alias was ⌘L. In Mojave, ⌘R has inexplicably been remapped to Rotate Right and ⌘L to Rotate Left. (These seem to be invisible menu items in the Edit menu? They’re not menu items, but the Edit menu highlights when you invoke them.) The shortcut for Make Alias is now ⌃⌘A and Show Original is now ⌃⌥⌘A. In and of themselves these new shortcuts aren’t bad, I suppose, but these are awfully longstanding shortcuts to change. And, I’ll add, the new shortcuts don’t even match the ones in Photos, where they’re named Rotate Counterclockwise (⌘R) and Rotate Clockwise (⌥⌘R). Photos’s shortcuts, where rotating in the other direction is an Option-key variant rather using an entirely different letter, seem more Mac-like to me. Preview, on the other hand, uses the commands names Rotate Left and Rotate Right, and the same ⌘L and ⌘R as the Mojave Finder. I give up. ↩︎︎



| **Previous:** | [The World’s Shortest Review of Apple’s $40 iPhone XR Clear Case](https://daringfireball.net/2018/12/worlds_shortest_review_of_apples_iphone_xr_clear_case) |
| **Next:** | [Opening New Tabs Next to the Current Tab in Safari](https://daringfireball.net/2018/12/safari_new_tab_next_to_current_tab) |


PreviousNext