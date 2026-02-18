---
title: "Apple Announces Sweeping but Complicated Policy Changes for Apps in the EU, Attempting to Comply With the Latest Dictums Regarding the DMA"
date: 2025-06-28
url: https://daringfireball.net/2025/06/apple_app_store_policy_updates_dma
slug: apple_app_store_policy_updates_dma
word_count: 1611
---


Let’s start with [Apple’s own announcement at Apple Developer News](https://developer.apple.com/news/?id=awedznci):


> The European Commission has required Apple to make a series of
> additional changes under the Digital Markets Act:
> Communication and Promotion of Offers
> Today, we’re introducing updated terms that let developers with
> apps in the European Union storefronts of the App Store
> communicate and promote offers for purchase of digital goods or
> services available at a destination of their choice. The
> destination can be a website, alternative app marketplace, or
> another app, and can be accessed outside the app or within the
> app via a web view or native experience.
> App Store apps that communicate and promote offers for digital
> goods or services will be subject to new business terms for
> those transactions — an initial acquisition fee, store services
> fee, and for apps on the StoreKit External Purchase Link
> Entitlement (EU) Addendum, the Core Technology Commission (CTC).
> The CTC reflects value Apple provides developers through ongoing
> investments in the tools, technologies, and services that enable
> them to build and share innovative apps with users. [...]
> Update to Business Terms for Apps in the European Union
> By January 1, 2026, Apple plans to move to a single business
> model in the EU for all developers. Under this single business
> model, Apple will transition from the Core Technology Fee (CTF)
> to the CTC on digital goods or services. The CTC will apply to
> digital goods or services sold by apps distributed from the App
> Store, Web Distribution, and/or alternative marketplaces.
> Apps currently under the Alternative Terms Addendum for Apps in
> the EU continue to be subject only to the CTF until the
> transition to the CTC is fully implemented next year. At that
> time, qualifying transactions will be subject to the CTC, and
> the CTF will no longer apply. Additional details regarding this
> transition will be provided at a later date.


Amongst other policy and API changes, Apple also announced a new, seemingly simplified, experience on iOS/iPadOS [for installing apps and alternative app marketplaces in the EU](https://developer.apple.com/support/alt-distribution-ux-in-the-eu/).


As for the other policy changes, [here’s Jason Snell’s summary](https://sixcolors.com/link/2025/06/apple-makes-big-app-store-changes-in-the-eu/), which I think captures the gist as well as possible:


> *Tiered App Store fees.* For today’s full-service App Store,
> developers will now pay 13% on sales, reduced to 10% for Small
> Business Program members. Or developers can opt into “Tier One”,
> which comes with a 5% fee but does not support a raft of App Store
> features we’ve come to expect, like automatic app updates, App
> Store promotions, placement in search suggestions, ratings and
> reviews on product listings (!), and more.
> *Core Technology Commission.* Apple is going to move all
> developers over to a new tax called the Core Technology
> Commission, in which developers who opt to sell apps outside the
> App Store will pay 5% of sales made through in-app promotions. The
> €0.50-per-install Core Technology Fee will be dropped as of
> January 1.
> *Free linking.* Developers can promote offers broadly, are no
> longer limited to a single static URL without tracking parameters,
> and can freely design the interfaces for those links and
> promotions.
> *New business terms.* Developers have to pay a 2% fee for digital
> goods and services purchased by new users for the first six months
> after a user first downloads an app; members of the Small Business
> Program don’t have to pay this fee.


And [here’s Chance Miller’s summary at 9to5Mac](https://9to5mac.com/2025/06/26/apple-announces-sweeping-app-store-changes-in-the-eu/), which includes the following statement from Apple (which statement was provided to me, as well):


> “The European Commission is requiring Apple to make a series of
> additional changes to the App Store. We disagree with this outcome
> and plan to appeal.”


The new fee structure is undeniably convoluted, and I think downright confusing. [Seemingly no one can figure out](https://x.com/rjonesy/status/1938354627155501219) exactly what commissions apps that use alternative payments or distribution are going to pay. It’s a natural consequence that an overly complicated law (the DMA) has resulted in an ever-more-complicated set of guidelines and policies (from Apple): byzantine compliance with a byzantine law.


Because it’s so complicated and hard to understand, it’s difficult even to summarize with a headline describing what’s new. Even if you understand it enough to just want to express anger at Apple for spiteful compliance and greed, it’s hard to sum up why you’re angry in a succinct headline or tweet.


---


The bottom line, as I understand it, is the following (but I could be wrong about some of this1 — if I am, let me know, and I’ll try to correct it):

- Developers who just do the simplest thing possible — distribute through the App Store and process all payments using Apple’s IAP — will continue to pay the same commissions, 30% by default, or 15% for Small Business Program developers and recurring subscriptions after the first year. Of course this is what Apple would prefer developers do.
- Big developers, distributing through the App Store but processing their own payments, will still owe Apple a commission of around 20% on non-IAP purchases: 13% for “store services”, 5% for the new Core Technology Commission (replacing the €0.50 per-download Core Technology Fee), and 2% for “initial acquisition”. Small Developer Program members and recurring subscriptions after the first year pay 15% — no “initial acquisition fee” and a reduced “store services” fee of 10%. But everyone’s on the hook for the 5% CTC.
- Apps distributed through the App Store can pay a reduced rate of 5% for “store services” (down from 13%) by opting into a reduced “Tier 1”. Rather than this “Tier 1” being an appealing choice for any developers, I think the point of it is for Apple to assert that those App Store features justify 8 percent of Apple’s commission on purchases: automatic software updates, reviews and ratings, surfacing through search for anything other than an exact name match, [and a whole lot more](https://developer.apple.com/help/app-store-connect/reference/store-services-tiers/).
- One consequence of the €0.50 per-download Core Technology Fee (CTF) being replaced by a 5% Core Technology Commission (CTC) is that there will no longer be a penalty for small developers who have a free-to-download app that hits over one million EU downloads. That was a legitimate problem with the CTF — an app with 5 million EU downloads would owe Apple €2 million for the CTF, but might be generating far less than that (or even nothing at all) in revenue. But another consequence of switching to the CTC from the CTF is that super-popular apps from super-big companies that don’t sell digital goods from their apps will continue to pay nothing at all. E.g. unless Meta starts selling digital goods from within their apps, they’ll continue to pay nothing at all to Apple for zillion-download apps like Instagram, Facebook, and WhatsApp. That was a shortcoming with the App Store’s model that the CTF was designed to correct.
- All of this additional complication is, I believe, just for apps distributed through the App Store. Feel free to blame Apple as much as you want for spiteful compliance (especially when it comes to payments made on the web, from links in apps), but part of this is on the European Commission for demanding not only that Apple allow apps to be distributed outside the App Store (which is somewhat reasonable), but also for requiring Apple to allow outside payments for apps distributed through the App Store. Apps and games distributed through alternative EU app marketplaces or web downloads are only on the hook for the 5% CTC (by the end of the year, when it replaces the CTF). But there is no free lunch — iOS apps and games distributed outside the App Store that require a purchase, or offer digital content for sale, must pay the 5% CTC.


There are a lot of people [who think](https://9to5mac.com/2025/06/26/tim-sweeney-slams-apples-unlawful-eu-app-store-changes/) what Apple is “supposed” to do is collect no commission or fees at all on anything other than IAP from apps and games that are distributed through the App Store. That Apple should collect no commission or fees from apps distributed outside the App Store, nor any commission or fees from apps in the App Store that offer their own payment processing — and, thus, that Apple should set their own IAP commission accordingly, as something akin to Stripe or PayPal, in the single-digit percentage range. That’s obviously not in Apple’s interest. But it’s also *not* what the European Commission has suggested the DMA demands.


---

1. One thing I might be wrong about is that these new terms could be read to suggest that developers who stick with the App Store and Apple’s IAP now pay just 20 percent commission under the new EU terms. That’d be really weird, insofar as it would mean that developers in the EU get an 80/20 split for App Store distribution + IAP, but apps everywhere else in the world still get 70/30 for the same thing. That doesn’t make sense unless there’s another shoe to drop, and Apple is going to reduce IAP to 80/20 worldwide soon. (Which would be a great move on Apple’s part — something that would actually earn them back some developer goodwill.) ↩︎



| **Previous:** | [More on Apple’s Trust-Eroding ‘F1 The Movie’ Wallet Ad](https://daringfireball.net/2025/06/more_on_apples_trust-eroding_f1_the_movie_wallet_ad) |
| **Next:** | [Full-Screen Ad for ‘F1 The Movie’ in Apple’s TV App Linked Directly to the Web, and Nothing Bad Seemed to Happen](https://daringfireball.net/2025/07/full-screen_ad_for_f1_the_movie_in_apples_tv_app_linked_directly_to_the_web) |


PreviousNext