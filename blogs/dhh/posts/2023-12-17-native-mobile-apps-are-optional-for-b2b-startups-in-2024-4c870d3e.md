---
title: "Native mobile apps are optional for B2B startups in 2024"
date: 2023-12-17
url: https://world.hey.com/dhh/native-mobile-apps-are-optional-for-b2b-startups-in-2024-4c870d3e
slug: native-mobile-apps-are-optional-for-b2b-startups-in-2024-4c870d3e
word_count: 985
---

I continue to see new B2B software startups struggle with native mobile apps. Consumer software makers can usually start by going all-in on a single platform, but for business tools, that’s rarely an option. So they must face the tall task of tackling web, iOS, and Android at the same time. Hence the proliferation of toolkits like React Native,
[Turbo Native](https://github.com/hotwired/turbo-ios)
, and a hundred other frameworks vying to ease the pain. But it still hurts.
And it’s practically impossible for a single developer to be able to do it all anyway. The problem space is just too large. Which means the barrier to becoming competitive require
[ropes of external funding](https://signalvnoise.com/posts/3972-reconsider)
to scale. If technical founder teams can’t do it themselves, they have to hire, and if they have to hire, they have to raise capital.
I hate that. We built
[Basecamp](https://basecamp.com/)
back in 2003 because we could do it ourselves. A single developer and a couple of designers was all it took. No external capital, no daunting payroll. That would be hard to do today, if you needed a competent native effort on iOS and Android out the gate while also serving the web.
I know this all too well, because we make some great native apps for
[Basecamp](https://play.google.com/store/apps/details?id=com.basecamp.bc3&hl=en_US&gl=US)
and
[HEY](https://apps.apple.com/us/app/hey-email/id1506603805)
, and it requires a team of nine native developers to be able to do it well (which is well below the industry average for huge apps like Basecamp with hundreds of screens). Everything just takes longer on mobile because the materials are harder to work with than the web. The pay-off is a higher potential for fidelity and (the mixed blessing of) distribution via the app stores.
But I think we’re finally seeing another route for these B2B software startups in
[Progressive Web Applications](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps)
(or PWAs) going into 2024.
PWA is an awkward term, but a tantalizing prospect. Basically it’s the idea that instead of multiple, distinct native applications, you can package one web application that feels (almost) native across all platforms. One code base, one deployment path. Massively simplified development.
It’s not a new concept. Google and Microsoft have been trying to push PWAs for years and years, since they both have a strategic interest in the web and avoiding platform lock-in (i.e. dealing with iOS exclusives). But it all remained a bit niche, because the biggest player in native, Apple, wasn’t playing ball.
That finally changed this year. In macOS Sonoma, Safari gained Add to Dock. In iOS and iPadOS 16.4,
[Safari gained two crucial features](https://webkit.org/blog/13878/web-push-for-web-apps-on-ios-and-ipados/)
: Badge Counting and Web Push Notifications.
It’s especially that last one that has unlocked the viable path for PWAs as a mainstream alternative to native apps. The inability to trigger mobile push notifications on iPhones was
*the*
blocker for many teams to even consider a PWA for their B2B application. And now it’s gone.
It’s not perfect. The
[standard for Web Push Notifications](https://datatracker.ietf.org/doc/html/rfc8030)
was proposed by Microsoft back in 2016, and with Apple dragging their feet on support, we’re now seven years later, and the last bits of finesse that Android and iOS has acquired in later years is missing (like recalling notifications and advanced grouping). But it’s more than good enough not to serve as a blocker any more.
But what has surprised me the most about Apple’s PWA support is just how good the Safari implementation of
[Add To Dock in macOS Sonoma](https://support.apple.com/en-us/104996)
and the updated
[Add To Homescreen](https://www.youtube.com/watch?v=I4e1aoi0P-o)
with badging really is. Apple may have taken their sweet time, but in typical fashion, they’ve also brought the best implementation.
You don’t have to be much of a conspiracy theorist to ponder why it took Apple almost a decade to bring web push notifications to the iPhone, though. Apple makes billions of dollars in toll fees from charging app makers 30% of their revenue to live in the App Store, and gating push notifications behind that toll has been an incredibly effective tool to enforce
[that distribution monopoly](https://www.hey.com/apple/)
.
But with the incoming
[Digital Markets Act](https://techcrunch.com/2023/11/08/apple-says-it-expects-to-make-app-store-policy-changes-due-to-eu-dma/?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAAGxEUsTW_p99bBYW10h5KUWp3BHXI98aY4famhW-h__kDYkJJgmy2k_NmDV0QiUx1v_Ki8RQZr7NiZ9Nh2ugJPPhdSPtRltXm2CU1xzBKMHx50tgzFRlBkntfETzqeMW55CnB-achuYf_-RlxbEe_55VadH2m504wy2hpW8aKTKI)
in Europe, and increasing scrutiny from antitrust regulators around the world, it doesn’t take a strategic genius to see why Apple would seek to appease the lawmakers by throwing the web a bone.
That’s not to cast any shade on the Safari team. I think they legitimately want to make the best browser out there, and I’m eternally grateful for their amazing work on
[CSS nesting, :has selectors](https://twitter.com/dhh/status/1735435171342737866)
,
[import maps](https://world.hey.com/dhh/hey-is-running-its-javascript-off-import-maps-2abcf203)
, and now PWA support. I get the sense that it’s a relatively small team, at least compared to Google’s Chrome effort, but they try real hard, and the result is a great browser that I use every day (not that you have a choice on the iPhone, but that’s another story!).
However we got there, here we are. The hallowed promise of web applications being viable and competitive alternatives to native efforts is finally here. Fans of the open web have been clamoring for this day for so long that it’s perhaps easy to miss that it’s finally here. But it is.
This means that I’m now going to recommend that every B2B software startup begins by targeting the web first. Unless you’re swimming in a
[red ocean](https://www.amazon.com/Blue-Ocean-Strategy-Expanded-Uncontested-ebook/dp/B00O4CRR7Y/)
of competitors who are winning the market by stellar native apps, you can and should focus on getting to product-market fit on the web first. Then, once you’re minting money, and can afford the large teams required for multiple native applications, you can always explore the mixed blessings of App Store distribution.
At 37signals, we’re going all-in on PWAs for our new
[ONCE](https://once.com)
products. It’s just a perfect pairing with allowing customers to run their own applications on their own servers. They’ll be sending their own web push notifications, and we’ll never even be in the middle of it. It’s beautiful.
So cheers to 2024 actually, really, finally, definitely being The Year of PWAs 🎉
