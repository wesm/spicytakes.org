---
title: "Catalyst, Two Months In"
date: 2019-12-19
url: https://daringfireball.net/2019/12/catalyst_two_months_in
slug: catalyst_two_months_in
word_count: 1015
---


Jack Wellborn, “[Catalyst and Cohesion](https://wormsandviruses.com/2019/12/catalyst-and-cohesion/)”:


> The crux of the issue in my mind is that iOS and Mac OS are so
> fundamentally different that the whole notion of getting a
> cohesive experience through porting apps with minimal effort
> becomes absurd. The problem goes beyond touch vs pointer UX into
> how apps exist and interact within their wider OSes. While both
> Mac OS and iOS are easy to use, their ease stem from very
> different conventions.
> The more complicated Mac builds ease almost entirely through
> cohesion. Wherever possible, Mac applications are expected to
> share the same shortcuts, controls, windowing behavior, etc… so
> users can immediately find their bearings regardless of the
> application. This also means that several applications existing in
> the same space largely share the same visual and UX language.
> Having Finder, Safari, BBEdit and Transmit open on the same
> desktop looks and feels natural.
> By comparison, the bulk of iOS’s simplicity stems from a single
> app paradigm. Tap an icon on the home screen to enter an app that
> takes over the entire user experience until exited. Cohesion
> exists and is still important, but its surface area is much
> smaller because most iOS users only ever see and use a single app
> at a time. For better and worse, the single app paradigm allows
> for more diverse conventions within apps. Having different
> conventions for doing the same thing across multiple full screen
> apps is not an issue because users only have to ever deal with one
> of those conventions at a given time. That innocuous diversity
> becomes incongruous once those same apps have to live
> side-by-side.


I’m just not seeing it with Catalyst apps. They almost all look and feel and work wrong. I’ll pick on Twitter because they’re a big company. They’ve made a bunch of improvements to [their Catalyst Mac](https://apps.apple.com/us/app/twitter/id1482454543?mt=12) app in the two months or so since it shipped. Some really [preposterous](https://twitter.com/wongmjane/status/1182672138291032068) [shortcomings](https://twitter.com/gruber/status/1197405159111966720) in the initial release have been fixed in a short amount of time, and I get the impression — both through their public comments and some private ones I’ve exchanged with developers on their team — that they’re trying to do the right thing and make Twitter for Mac a good Mac app, not just the iPad app running in a window on the Mac. But [the release notes for the latest update](https://daringfireball.net/misc/2019/12/twitter-mac-release-notes.png) this week include new features like support for scrolling with the Page Up, Page Down, Home, and End keys. It’s kind of crazy that support for those keys wasn’t there from the start. 15 years ago you’d almost never find a Mac app that didn’t support them.


I think part of the problem is Catalyst itself — it just doesn’t feel like nearly a full-fledged framework for creating proper Mac apps yet. But I think another problem is the culture of doing a *lot* of nonstandard custom UI on iOS. As Wellborn points out, that flies on iOS — we UI curmudgeons may not like it, but it flies — because you’re only ever using one app at a time on iOS. It cracks a bit with split-screen multitasking on iPadOS, but I’ve found that a lot of the iPad apps with the least-standard UIs don’t even support split-screen multitasking on iPadOS, so the incongruities — or incoherences, to borrow Wellborn’s well-chosen word — don’t matter as much. But try moving these apps to the Mac and the nonstandard UIs stick out like a sore thumb, and whatever work the Catalyst frameworks do to support Mac conventions automatically doesn’t kick in if the apps aren’t even using the standard UIKit controls to start with. E.g. scrolling a view with Page Up, Page Down, Home, and End.1 An iOS app using standard UIKit controls for scrollable views should, in theory, pick up support for those keys automatically. But a lot of apps don’t because they’re not using standard controls.


In short, I remain unconvinced that *standard* UIKit iPad apps are a good starting point for good Mac apps. But it’s pretty obvious — and should have been right from the start — that *nonstandard* not-really-using-UIKit iPad apps make for a terrible starting point for a good Mac app. Developers can make it work — as a programmer friend once told me, “It’s all just typing” — but it’s so much work it seems to defeat the entire “Just click a checkbox in Xcode” premise and promise of Catalyst.


---

1. At some point a while back I wrote about Page Up/Down and Home/End keys and some wiseacre responded that almost no one has those keys on their keyboards, because most people use MacBooks and regular Magic Keyboards, which don’t have those keys. And Twitter’s aforementioned release notes [describe these features](https://daringfireball.net/misc/2019/12/twitter-mac-release-notes.png) as “extended keyboard support”. But *every* Apple keyboard does have the ability to invoke the same functions: Fn↑ = Page Up, Fn↓ = Page Down, Fn← = Home, and Fn→ = End. These are great shortcuts to know.
On the Mac at least.
On iOS, it seems only Fn↑ = Page Up and Fn↓ = Page Down are standard in UIKit — the Fn←/Fn→ shortcuts for Home/End seem to be supported nowhere. But even some of Apple’s own iPad apps — like Mail and Notes to name two — don’t support Fn↑ / Fn↓ either. In a read-only view you can get Home/End behavior (jumping to the very top/bottom of the view) with ⌘↑ and ⌘↓, but in an *editing* view those shortcuts will move the insertion point to the beginning/end, not just scroll the view port, as true Home/End behavior should.
Neither Twitter nor Slack for iPad — two apps that frequently irritate me with their nonstandard non-native UIs — support any of the Fn-arrow key shortcuts for scrolling. ↩︎



| **Previous:** | [Bluesky: Twitter Announces Effort to Build ‘Decentralized Standard for Social Media’](https://daringfireball.net/2019/12/bluesky) |
| **Next:** | [David Ruddock on the State of Chrome OS](https://daringfireball.net/2020/01/ruddock_chrome_os_stalled_out) |


PreviousNext