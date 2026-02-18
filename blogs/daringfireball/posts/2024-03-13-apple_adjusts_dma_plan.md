---
title: "Apple Adjusts DMA Plan to Offer Direct Downloading of Apps From the Web (With a Big Asterisk), Custom Link-Out Screens, and Marketplaces Solely for the Distribution of a Developer’s Own Apps"
date: 2024-03-13
url: https://daringfireball.net/2024/03/apple_adjusts_dma_plan
slug: apple_adjusts_dma_plan
word_count: 1948
---


[Apple Developer News](https://developer.apple.com/news/?id=8c1m8hqt), yesterday:


> Developers who’ve agreed to the Alternative Terms Addendum for 
> Apps in the EU have new options for their apps in the EU: 
> Alternative app marketplaces. Marketplaces can choose to offer a 
> catalog of apps solely from the developer of the marketplace. 
> Linking out to purchase. When directing users to complete a 
> transaction for digital goods or services on an external 
> webpage, developers can choose how to design promotions, 
> discounts, and other deals. The Apple-provided design templates, 
> which are optimized for key purchase and promotional use cases, 
> are now optional.


These two tweaks follow [three others from a week ago](https://developer.apple.com/news/?id=0yrn1puh). The first new one, above, means a company like, say, Adobe or Microsoft, can offer a marketplace just for their own suite of apps. The second is a bigger concession — effectively, the elimination of mandatory Apple-designed scare sheets for link-outs to the web. It sounds like the second truly eliminates anti-steering provisions for developers who opt into the new EU rules.


And then, boom, the big one:


> Web Distribution, available with a software update later this 
> spring, will let authorized developers distribute their iOS apps 
> to EU users directly from a website owned by the developer. Apple 
> will provide authorized developers access to APIs that facilitate 
> the distribution of their apps from the web, integrate with system 
> functionality, back up and restore users’ apps, and more. For 
> details, visit [Getting ready for Web Distribution in the 
> EU](https://developer.apple.com/support/web-distribution-eu/).


So direct downloads — single-app sideloading from developers’ own websites — are now an option. The devil is [in those details though](https://developer.apple.com/support/web-distribution-eu/):


> To be eligible for Web Distribution, you must: [...]
> Be a member of good standing in the Apple Developer Program for 
> two continuous years or more, and have an app that had more than 
> one million first annual installs on iOS in the EU in the prior 
> calendar year. 
> Agree to, among other things, 
> Only offer apps from your developer account. 
> Be responsive to communications from Apple regarding your 
> apps distributed through Web Distribution, particularly 
> regarding any fraudulent, malicious, or illegal behavior, 
> or anything else that Apple believes impacts the safety, 
> security, or privacy of users. 
> Publish transparent data collection policies and offer 
> users control over how their data is collected and used. 
> Follow applicable laws of the jurisdictions where you 
> operate (for example, the Digital Services Act, the 
> General Data Protection Regulation, and consumer 
> protection laws). 
> Be responsible for handling governmental and other 
> requests to take down listings of apps.


The eligibility requirement of having an app with over 1 million annual installations in the EU is a high barrier. The intention, obviously, is to limit web distribution to ostensibly trustworthy developers. But it’s sort of a catch-22: the entire feature is by definition intended for developers who want to distribute their apps outside Apple’s App Store (or anyone else’s EU app marketplace) — but the only way to qualify is to have at least one very popular app in the App Store or an app marketplace.


If this change is at the behest of the EC, via back-channel feedback, the EC is seemingly only concerned with large developers. And to me it makes no sense that this change — a huge one — came from anywhere *but* back-channel communications with the EC. Apple’s presentation of its original compliance plan, [just six weeks](https://daringfireball.net/2024/01/apples_plans_for_the_dma) ago, went out of its way to emphasize that requiring all apps to go through a marketplace — and requiring stricter eligibility requirements for marketplace providers than regular developer accounts — was in the name of user security. If Apple had wanted to offer direct downloads of individual apps from developers’ own websites, they would have included this from the start. But given that the feature will be available “later this spring” — which I take to mean before WWDC — they were seemingly already working on it, preparing for the EC to say, publicly or privately, that the DMA requires it. But if Apple had wanted to allow web distribution, it would have been part of the initial announcement.


Almost all the changes Apple has made to its compliance plan, so far, are merely policy changes. Marketplace providers no longer necessarily need to obtain a million-dollar stand-by letter of credit. Developers who opt into the new EU rules can now change their minds and go back to the original business terms. Corporations with multiple developer accounts can opt into the new rules on an account-by-account basis, instead of all-or-none. Companies can create marketplaces solely for their own apps. All just policy changes. And all of those policy changes quite likely are the result of direct feedback from *developers*. It’s easy to imagine that Apple never considered that a company with multiple developer accounts might want only to move *some* of those accounts to the new business terms. I don’t see why Apple would begrudge any of these changes, even an iota. They can be filed under “*Sure, we just didn’t think of that.*”


That link-out screens may now contain promotional and pricing information, and don’t need to follow Apple’s templates — that’s a mere policy change too, but one I suspect Apple *does* begrudge. And it’s obviously something developers want. Do you want a very plain-looking, totally unbranded screen, that emphasizes more than anything that you’re leaving the safe confines of the Apple ecosystem? Or would you like to design your own screen, in your own style, with your own emphasis? This, to me, reeks of a change at the behest of the EC.


But then there’s web distribution — that’s both a major policy change *and* a major technical one. (How will software updates work for web downloaded apps? For that matter, how will software updates work for marketplace apps themselves? Will the Foobar Marketplace app be able to somehow update itself? That doesn’t seem possible without running a background process.) And as I noted earlier, Apple specifically described direct web downloads of apps as a bad idea just six weeks ago.


I have no little birdie information on this, but Apple changing policy on this issue *only* makes sense if they have reason to believe the EC considers it mandatory under the DMA. That it will only be available to longstanding developers with at least one million-EU-downloads app may well be completely compatible with the DMA. There’s nothing at all in the DMA about the interests of small or indie developers.


And as Steven Sinofsky expounded upon at length [in his analysis of the DMA](https://hardcoresoftware.learningbyshipping.com/p/215-building-under-regulation), the DMA wants to have its cake and eat it too. It requires Apple both to open up iOS to additional methods of software distribution *and* to keep iOS as secure as possible. Allowing direct downloads, but only from already-successful developers, aligns with that. I suspect Apple was ready to go from the start with web downloads — they knew the EC *might* demand it — and so they opened their hand January 25 with the compliance plan they hoped would fly, and are ratcheting out, piecemeal, with additional changes in the direction of more openness, as they obtain feedback — both from developers, and whatever EC back channels they may have. (Officially, the EC doesn’t provide issue-by-issue feedback to its regulatory subjects.)


The other change that suggests Apple is in unofficial contact with the EC regarding compliance is [the “never mind” on PWAs](https://9to5mac.com/2024/03/01/apple-home-screen-web-apps-ios-17-eu/). Beta versions of iOS 17.4 in the EU changed Home Screen web apps into bookmarks that open in a new tab in the user’s [default browser](https://daringfireball.net/linked/2024/03/06/ios-17-default-browser-nag). Apple made this change not because they want to “kill” web apps,1 but because they were under the impression that the DMA required them to either (a) have no Home Screen web app support at all in the EU, or (b) allow all third-party rendering engines to save PWAs to the Home Screen using their rendering engines. Option (c) — the status quo, WebKit-only PWA support on the Home Screen — is seemingly disallowed under the DMA, as it would constitute preferencing WebKit over third-party engines. Apple doesn’t have a system in place in iOS to allow third-party rendering engines to save web apps to the Home Screen, so, alas, (a) it was — no more PWAs in the EU. The DMA is not clear about much, but it is seemingly clear that gatekeepers cannot preference their own web browser or rendering engine. Allowing PWAs — but only via WebKit — is, obviously, showing preference to WebKit. Apple’s initial decision to remove PWAs in the EU sucked, but that’s because the DMA sucks, not because Apple hates or fears web apps. But I think what happened is that when the EC realized the DMA was going to result in a *worse* PWA experience, they let Apple know that WebKit-only PWAs would not be penalized.2


So my gut feeling is that we’re seeing Apple adopt changes in response to unofficial feedback from the EC. If so, that suggests that the things Apple *isn’t* changing — like the Core Technology Fee — are either OK with the EC, or, if not, that Apple is willing to fight for them. Or perhaps we’ll be right back here with additional compliance plan changes every Tuesday for the next few weeks.


---

1. If Apple wanted to kill web apps they’d have made this change worldwide in iOS 17.4, not limited to the EU. And they wouldn’t have been adding new web app features to WebKit, on both iOS and [especially MacOS](https://support.apple.com/en-us/104996), just in the last year. But there exists a contingent of tinfoil-hat-wearing web app zealots who think PWAs are like *this close* to taking over mobile app development — the dream of write-once/run-everywhere just within grasp — and it’s mean old monopolistic walled-garden-defending Apple that’s holding them back, [because PWAs threaten the App Store](https://open-web-advocacy.org/blog/did-apple-just-break-web-apps-in-ios17.4-beta-eu/). That’s just nonsense. The truth is PWAs just aren’t popular. Almost no normal people use them, or even know they exist. *“That’s because Apple is holding PWAs back by withholding features from WebKit*”, goes the conspiracy thinking. Most recently, it was mobile push notification support. [Then WebKit added that](https://webkit.org/blog/13878/web-push-for-web-apps-on-ios-and-ipados/). It’s like desktop Linux getting popular, or Bluetooth getting reliable: always “next year”. Except with PWAs, web developers can imagine it’s somehow Apple’s fault, not the fact that users prefer idiomatic native apps from app stores — including on Android, which has always used Chrome’s web rendering engine, and which has all the features PWA advocates want from WebKit. ↩︎
2. I also suspect that Apple, eventually, will support PWAs in iOS in the EU using third-party browser engines, if possible. But it’s easy to see how complicated that could be. What happens if a user installs Chrome, then uses Chrome to install a PWA using Chrome’s Blink rendering engine, and then deletes Chrome from their iPhone? How does that PWA continue to function after its rendering engine has been removed from the system? It can’t just automatically fall back to using WebKit because (a) the PWA might be using features only available in Chrome (that’s the whole reason web developers are clamoring for third-party rendering engines); and (b) the PWA’s stored data is tied to the rendering engine that created it. This is not a simple problem to solve. ↩︎︎



| **Previous:** | [Once More Unto the Apple / Epic / European-Commission Breach, Dear Friends, Once More](https://daringfireball.net/2024/03/once_more_unto_the_apple-epic-european-commission_breach) |
| **Next:** | [Quickly Toggling Closed Captions on Apple TV (But Not in Netflix)](https://daringfireball.net/2024/03/quickly_toggling_closed_captions_on_apple_tv) |


PreviousNext