---
title: "That EU App Store Warning About External Purchases Is Not New, and Apple Proposed Improving It Nine Months Ago"
date: 2025-05-15
url: https://daringfireball.net/2025/05/that_eu_app_store_warning_about_external_purchases_is_not_new
slug: that_eu_app_store_warning_about_external_purchases_is_not_new
word_count: 659
---


Some interesting follow-up on [that piece yesterday](https://daringfireball.net/linked/2025/05/14/app-store-eu-payment-warning) about the warning — with a prominent red “!” icon — in App Store listings for apps in the EU that use their own payment processing. Apple told me that exact same warning has been in place since the very beginning of their DMA compliance, in March 2024.


Jacob Eiting, CEO of RevenueCat, [tweeted on X](https://x.com/jeiting/status/1922010640539123921):


> I think this is EU only and might have been around for a while, I
> just assumed nobody bothered with the DMA implementation for
> external purchases since they were pointless.
> Fewer than 100 developers have availed themselves of this option
> for obvious reasons.


I think this blew up a bit yesterday because, despite the fact that it had been around since March 2024, few of us had ever seen it before because so few apps in the App Store use it. Eiting includes a link to [Apple’s own developer documentation for its DMA compliance features](https://developer.apple.com/support/alternative-payment-options-on-the-app-store-in-the-eu/#user-disclosures), which makes this clear:


> To help users understand whether an app contains an alternative
> payment option, the App Store will display an informational banner
> on the app’s product page to identify the developer’s enablement
> of this entitlement. When downloading an app, users are also
> informed if an app uses PSPs or links out on the purchase
> confirmation sheet. Apps that contain an alternative payment
> option are required to present users with a disclosure prior to
> each transaction or link out to purchase to help them understand
> that the purchase isn’t backed by Apple.


I actually think that’s very useful information that *should* be on an app’s App Store listing. Users should know what to expect, and iPhone users’ expectations are that digital goods transactions go through Apple’s IAP. The problem with this disclosure, as it stands, is the way it looks: like a big scary warning. It should be something more akin to the privacy “nutrition label” information.


And, it turns out, [Apple itself publicly proposed exactly such a change back in August](https://developer.apple.com/support/alternative-payment-options-on-the-app-store-in-the-eu/#user-disclosures). Apple’s proposed updated disclosure uses a small gray *i*-in-circle “info” icon (replacing the bigger red !-in-triangle “warning” icon), and the following text ([screenshot](https://daringfireball.net/misc/2025/05/user-disclosures-eu-transactions.png)):


> Transactions in this app are supported
> by the developer and not Apple.
> [Learn More](https://apps.apple.com/hu/story/id1726640865)


I would quibble with the fact that Apple’s proposal places that disclosure at the very top of the listing page in the App Store, above even the app’s name and icon, but visually and verbally it’s good. Clear, informative, and non-judgmental.


Per what I’ve been told by Apple, they were (and still are) prepared to implement these changes, including the new disclosure screen. The EC raised no objection to the new disclosure proposal, but insisted that Apple *not* implement the changes at the time. Then, according to Apple, the EC never provided further guidance, until last month when they fined Apple €500M for noncompliance. (And the EC [still hasn’t told Apple](https://daringfireball.net/linked/2025/04/23/ec-clear-as-mud) what it wants the company to do.)


This seems to be the exact dynamic [Politico reported on last week](https://www.politico.eu/article/apple-to-appeal-e500m-digital-fine-over-eus-silence-in-compliance-talks/) (and that [I just linked to earlier today](https://daringfireball.net/linked/2025/05/15/apple-ec-proposals-feedback)):


> According to correspondence seen by Politico, Apple offered last
> summer [to drop its rules](https://developer.apple.com/news/?id=szrqxadx) on how app developers can
> communicate with users, but was told by the Commission to hold
> off, pending feedback from developers.
> By late September and following a round of consultations with
> Apple critics like Spotify, Match Group and Epic Games, executives
> at the U.S.-based firm began worrying that a lack of feedback from
> the Commission meant it was teeing up a potential fine and
> noncompliance decision.


Heads, Apple was going to get fined by the EC. Tails, Apple was going to get fined by the EC.



| **Previous:** | [Single-Story a’s in Very Early Versions of Macintosh System 1](https://daringfireball.net/2025/05/single_story_a_classic_mac_system_1) |
| **Next:** | [15 Years Later: ‘Very Insightful and Not Negative’](https://daringfireball.net/2025/05/15_years_later_very_insightful_and_not_negative) |


PreviousNext