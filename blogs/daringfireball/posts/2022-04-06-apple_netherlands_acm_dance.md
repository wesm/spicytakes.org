---
title: "Apple’s Dance With the Netherlands ACM Continues"
date: 2022-04-06
url: https://daringfireball.net/2022/04/apple_netherlands_acm_dance
slug: apple_netherlands_acm_dance
word_count: 847
---


Apple last week adjusted its proposed plan for compliance with the Netherlands ACM’s regulations on dating apps. [Three changes were announced](https://developer.apple.com/news/?id=jmps5hyj):


> Removal of the Separate Binary Requirement: Apple is eliminating
> the requirement that developers of dating apps in the
> Netherlands who choose to use the above entitlements must create
> and use a separate binary. This change means that developers may
> include either entitlement in their existing dating app, but
> still must limit its use to the app in the Netherlands
> storefront and on devices running iOS or iPadOS.
> Payment Service Provider Criteria: Apple is providing updated
> and more-specific criteria to evaluate non-Apple payment
> service providers that developers of dating apps in the
> Netherlands may use.
> Consumer Disclosures: Apps that use either entitlement need to
> include an in-app modal sheet that explains to users that
> they’re going to make purchases through an external payment
> system, and the potential impact that choice could have on the
> user. Apple is adjusting the language on the modal sheet and
> reducing the number of times the sheet must be displayed.


None of these proposed changes are earth-shattering, but they’re all for the better.


Apple’s initial proposal that apps using these entitlements in the Netherlands would need to do so using a separate binary — meaning, a second Netherlands-only version of the app — seemed deliberately confusing. One problem with requiring a separate binary, for example, is that Dutch users who already have one or more dating apps installed might not have gotten updated versions that use these new entitlements via software update. There are some popular apps in the App Store with multiple binaries, but it’s unusual. Sometimes it’s a split between a free/lite version and a paid/pro version, but that’s less common these days, where the typical strategy is a free-to-download-and-use version that contains an in-app purchase to unlock additional features or remove ads.


The other notable change is to the required language in the warning screen users must be presented before making purchases via non-Apple payment processors or being sent to the web. Here’s the *previous* version of the warning screen ([which I wrote about two months ago](https://daringfireball.net/2022/02/going_dutch)):


> **Title:** This app does not support the App Store’s private and
> secure payment system
> **Body:** All purchases in the <App Name> app will be managed by
> the developer “﹤Developer Name﹥.” Your stored App Store payment
> method and related features, such as subscription management and
> refund requests, will not be available. Only purchases through the
> App Store are secured by Apple.
> Learn More
> Action 1: Continue


Here’s the updated version, from Apple’s [developer page for the StoreKit External Purchase Entitlement](https://developer.apple.com/support/storekit-external-entitlement/):


> **Title:** This app doesn’t support the App Store’s payment system.
> **Body:** All purchases in this app will be managed by the developer
> “<Developer Name>.” You will no longer be transacting with
> Apple. Your stored App Store payment method and related features,
> such as subscription management and refund requests, will not be
> available. Apple is not responsible for the privacy or security of
> transactions made with this developer.
> Learn More
> Action 1: Continue 
> Action 2: Cancel


The changes to this language are subtle, but good. “This app doesn’t support the App Store’s payment system” is simply true. As I wrote in February, the old title sort of implied not just that Apple’s payment system is private and secure, but that *only* Apple’s payment system is private and secure. The new language is more matter-of-fact, which feels appropriate.


As far as I can tell, though, Apple still hasn’t said what’s supposed to happen if a user taps on “Learn More”.


---


[Apple also last week announced an update](https://developer.apple.com/news/?id=grjqafts) on “reader” app distribution, [pursuant to their agreement last September with the Japan Fair Trade Commission](https://daringfireball.net/linked/2021/09/01/apple-anti-steering-relaxation). Apple:


> Last year, Apple [announced](https://www.apple.com/newsroom/2021/09/japan-fair-trade-commission-closes-app-store-investigation/) an update coming to the App Store
> in early 2022 that would allow developers of “reader” apps to
> include an in-app link to their website for account creation and
> management purposes. Starting today, with the update of [App Store
> Review guideline 3.1.3(a)](https://developer.apple.com/app-store/review/guidelines/#reader-apps), developers of reader apps can now
> request access to the External Link Account Entitlement. This
> entitlement lets reader apps link to a website that is owned or
> maintained by the developer, so that users can create or manage
> their account outside of the app. Reader apps are apps that
> provide one or more of the following digital content types — magazines, newspapers, books, audio, music, or video — as the
> primary functionality of the app.
> [Learn about the External Link Account Entitlement](https://developer.apple.com/support/reader-apps/)


Baby steps, but all of these changes are in the direction of decreasing regulatory pressure. Apple can be stubborn but they’re not stupid.



| **Previous:** | [The D.O.J. Goes After Google’s ‘Communicate With Care’ Program](https://daringfireball.net/2022/03/doj_google_communicate_with_care) |
| **Next:** | [Play Ball: Apple Announces More Details About ‘Friday Night Baseball’ on Opening Day](https://daringfireball.net/2022/04/more_friday_night_baseball_details) |


PreviousNext