---
title: "The New App Store: Subscription Pricing, Faster Approvals, and Search Ads"
date: 2016-06-08
url: https://daringfireball.net/2016/06/the_new_app_store
slug: the_new_app_store
word_count: 2125
---


“We’re doing something a little different this year. We’ve got a bunch of App Store/developer-related announcements for WWDC next week, but frankly, we’ve got a busy enough keynote that we decided we’re not going to cover those in the keynote. And rather, just cover them in the afternoon and throughout the week. We’re talking to people today for news tomorrow about those things, in advance of WWDC, and then developers can come and be ready for sessions about these things, with knowledge about them *before* the conference. We haven’t done this before, but we figured, what the heck, let’s give it a try.”


So started my phone call with Phil Schiller yesterday.1 Doing something a little different, indeed.


These changes and improvements to the App Store — or App Store*s*, if you prefer, because they all apply to iOS (and thus WatchOS), Mac OS X, and tvOS — are no little things. These changes fundamentally change the App Store, for users and especially for developers.


A quick summary:

- App Store review times are now *much* shorter. These changes are already in place, and have been widely noted in recent weeks. Apple is today confirming they’re not a fluke — they’re the result of systemic changes to how App Store review works.
- Subscription-based pricing was heretofore limited to specific app categories. Now, subscription-based pricing will be an option for *any* sort of app, including productivity apps and games. This is an entirely new business model for app developers — one that I think will make indie app development far more sustainable.
- Changes to app discovery, including a smarter “Featured” tab, the return of the “Categories” tab, and, yes, [as rumored](http://daringfireball.net/linked/2016/04/14/bloomberg-app-store-search), paid search ads.


## Subscription-Based Pricing for All


Until now, subscription pricing was reserved for apps that served media content: streaming audio and video, news, etc. Apple is now opening it to apps from *any* category, which effectively solves the problems of recurring revenue *and* free trials. Even better, Apple is changing the revenue split for all subscriptions: for the first year of any subscription, the revenue split remains 70/30; after the first year, the revenue split changes to 85/15.


In Schiller’s words, this is “in recognition that the developer is doing most of the work” with any app that is so good that the user remains a paid subscriber for over a year. This change is effective starting this Monday — any app that already has subscribers will start splitting revenue with Apple 85/15 on subscriptions that are at least a year old.


This dramatically changes the economics of the App Store. Until now, productivity apps could charge up front as paid downloads and that was it. Updates had to be free, or, to charge for major new versions, developers would have to play confusing games by making the new version an entirely new SKU in the app store. Twitter clients like Tweetbot and Twitterrific, for example, did this, to justify years of ongoing development. Now, apps like this can instead charge an annual/monthly/etc. subscription fee.


This could be the change that makes the market for professional-caliber iPad apps possible. On the Mac, there has long been a tradition of paying a large amount of money for a pro app, then paying a smaller amount of money for major updates. The App Store has never allowed for that sort of upgrade pricing — but upgrade pricing is what enabled ongoing continuous development of pro software. Paying for each major new version, however, is arguably a relic of the age when software came in physical boxes. Subscription-based pricing — “software as a service (SaaS)” — is the modern equivalent. That’s the route both Microsoft and Adobe have taken. In the old world of boxed software and installation disks, the natural interval was the version. In today’s world where everything is a download, months or years are more natural payment intervals.


Now, it’s available to all app categories in the App Store. I think this is terrific news both for developers and users.


Other changes:

- There are now more than 200 price points available to subscription-based apps.
- Apps can now change subscription prices easily. This was a huge pain in the ass previously. When an app changes subscription pricing, existing subscribers will be notified automatically and given the option to agree to the new pricing or unsubscribe.
- Subscription-based apps can now offer multiple tiers. Think bronze/silver/gold. Again, previously, Apple’s app subscription APIs made this difficult if not impossible. Now, it should be easy. And it should be easy for users to change tiers on the fly.
- Territory-based pricing is now possible. Developers can use this to charge lower prices in countries like China and India. This was not possible before.
- Most subscription-based apps use either monthly or annual renewal intervals. But apps have the option of renewing every two months, three months, or six months as well.


Developers have been asking for a way to do free trials and to sustain long-term ongoing development ever since the App Store opened in 2008. This is Apple’s answer. I think all serious productivity apps in the App Store should and will switch to subscription pricing.


You might argue that people don’t want to subscribe to a slew of different apps. But the truth is most people don’t want to pay for apps, period. Nothing will change that. But for those people willing to pay for high quality apps, subscriptions make sustainable-for-developer pricing more palatable, and more predictable.


## App Store Review Times


This is mostly a benefit to developers, who get a quicker turnaround time. Users don’t really see the review process — it’s hidden from them. Users just see when updated apps are available to them in the App Store. But there is a benefit to users of faster turnaround times — when developers fix bugs, users will get those bug fixes much sooner.


According to Schiller, 50 percent of submitted apps are now approved within 24 hours; 90 percent in 48 hours. For years, turnaround time was measured in days, not hours, and was generally in the range of a week.


Schiller told me this change can be attributed to three things:

1. Tool improvements internal to Apple.
2. Staffing changes.
3. Policy changes.


I asked for details regarding those “policy changes”, and Schiller demurred. One thing he emphasized, however, is that the rules for apps haven’t changed at all. If anything, Schiller claimed, with the new tooling at the disposal of reviewers, reviews are even better at identifying apps with quality problems than before. The impression I’m left with is that reviewers are now given more discretion to fast track apps from long-time trusted developers, once their binaries have passed Apple’s automated tests.


One can argue that this is long overdue, but better late than never.


## Ads in Search Results


I was [against this](http://daringfireball.net/linked/2016/04/14/bloomberg-app-store-search) when it first leaked, and I remain skeptical. But now that I’ve [seen the details](https://developer.apple.com/app-store/search-ads/), I’m OK with it. Here’s what Schiller told me:

- One and only one ad will be shown at a time.
- [Ads are clearly marked](https://daringfireball.net/misc/2016/06/app-store-ad-example.jpeg). They’re always at the top, have a light blue background, and a blue “Ad” tag.
- Ads will be relevant to the search terms from the user. We shall see if Apple succeeds here, but the intention is good.
- Ads are *only* shown in search results. There is no pay-for-placement in the Featured section.
- Ads are paid for in a [second-price auction](https://en.wikipedia.org/wiki/Generalized_second-price_auction) system. This means the winning bid only pays “just enough” more than the second-place bid for a keyword.
- No ads will be shown to children 13 or younger.
- Ads are pay-for-click. (Or pay-for-*tap*, on iOS.) Developers only pay when actual users actually tap their paid placement.


Apple has been leaving a lot of money on the table for Google and Facebook, both of which have been raking in money hand over fist from developers paying for ads that lead to app downloads. Schiller only mentioned “search engines” and “social networks”, but the truth is they should have been singulars, not plurals. It’s Google and Facebook.


Apple’s system does not use tracking. No profiles are kept of users, and no user-identifying information is sent to advertisers. And users can opt out of things like location-based ads with the system level preferences for location privacy. Downloads are already being driven by paid ads, so they might as well be in the App Store itself, where Apple can take some of the money *and* deliver ads that live up to its standards for privacy.


It’s also important to note that the ads are the same as the regular App Store listings. What you’ll see is the same exact content, vetted through the same approval process, as the regular app store listing. Developers are not paying to get a discrete “ad” displayed, per se, but paying to get their regular App Store listing displayed as an ad.


My concern when word first leaked about this is that the system would be geared toward large developers. Schiller emphasized to me that Apple designed this system with small indie developers in mind. 65 percent of app downloads start with searches in the App Store, according to Schiller — effectively two out of every three downloads. App Store search is absolutely essential to discovery. These ads should help small developers gain exposure — and they should be more efficient than ad spends at Google or Facebook, because they only appear in the context of a user who is already searching for an app.


## The Big Picture


Collectively, these changes should put to rest any notion that the App Store is neglected or in any way an afterthought for Apple. I’m certainly glad about the vastly improved turnaround time for App Store submission reviews, and I have a certain “wait and see” ambivalence regarding the App Store search ads.


But I am genuinely excited about subscription pricing being an option for all apps. I think it’s truly win-win-win, for Apple, its users, and most importantly for developers.


For Apple, [Ben Thompson nailed it back in 2013](https://stratechery.com/2013/adobes-subscription-model-why-platform-owners-should-care/):


> What makes monetizing productivity apps so tricky is that they are
> indispensable to some consumers, yet overwhelming to others. It’s
> that indispensable part, though, that should matter to platform
> owners. If a user comes to depend on certain productivity apps
> that are only available on one platform — and, in general, mobile
> productivity apps are much more likely to be monogamous — then
> that user is effectively bound to the platform, and won’t even
> consider another platform when it comes time to upgrade.
> The opportunity for growth in smartphones is increasingly
> previous-smartphone owners (as opposed to new smartphone owners).
> Keeping those owners around should be a top priority for every
> platform, and one of the best ways to do so is fully supporting a
> subscription model for productivity apps. It will make them more
> successful and thus stickier, ultimately to the platform’s
> long-term benefit.


For users, the benefit is that they should see more high quality productivity apps. And they’ll only have to pay for them as long as they’re actually using them.


For developers, I think this is the first time the App Store supports a business model that sustains long-term ongoing development of deep applications. The proof of the pudding is in the eating, and so we’ll have to wait and see if this actually changes the economic dynamics of developing for the App Store. But Phil Schiller’s enthusiasm for small indie developers is undeniable. It’s palpable. The new 85/15 revenue split after the first year of a subscription is proof of it. He’s trying, and [now that the entire App Store is under his leadership](http://www.apple.com/pr/library/2015/12/17Apple-Names-Jeff-Williams-Chief-Operating-Officer.html), that means Apple is trying. I would argue that the App Store has changed more in the last six months than it did in the previous eight years. Throw in a “finally” if you want, but again, I say better late than never.2


---

1. [Déjà vu](https://daringfireball.net/2012/02/mountain_lion). ↩︎︎
2. Last but not least, the fact that these significant — dare I say *dramatic* — changes to the App Store didn’t make the cut for the WWDC keynote makes me damn curious about what *did* make the cut for the keynote. The optimist in me foresees a keynote full of great new features in iOS 10, Mac OS X (MacOS 12?), WatchOS 3, and tvOS. The cynic in me foresees a repeat of last year’s interminable Apple Music segment. ↩︎︎



| **Previous:** | [Headlines Matter](https://daringfireball.net/2016/06/headlines_matter) |
| **Next:** | [App Store Subscription Uncertainty](https://daringfireball.net/2016/06/app_store_subscription_uncertainty) |


PreviousNext