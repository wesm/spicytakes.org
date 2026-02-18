---
title: "Let’s Consider Some of the Implications of Third-Party Payment Processing for In-App Purchasing on iOS and Android"
date: 2021-08-31
url: https://daringfireball.net/2021/08/implications_of_third-party_payment_processing_for_iap
slug: implications_of_third-party_payment_processing_for_iap
word_count: 2031
---


Apple, [in a statement to MacRumors](https://www.macrumors.com/2021/08/31/south-korea-passes-app-store-bill/) (and other media outlets), regarding [South Korea’s just-passed “Google power-abuse-prevention law”](https://daringfireball.net/linked/2021/08/31/south-korea-app-store-payment-law) which will forbid Apple and Google from requiring the use of their respective in-app purchasing systems:


> The Telecommunications Business Act will put users who purchase
> digital goods from other sources at risk of fraud, undermine
> their privacy protections, make it difficult to manage their
> purchases, and features like “Ask to Buy” and Parental Controls
> will become less effective. We believe user trust in App Store
> purchases will decrease as a result of this legislation — leading to fewer opportunities for the over 482,000 registered
> developers in Korea who have earned more than KRW8.55 trillion
> to date with Apple.


Apple defines in-app purchases as “App Store purchases”, which I disagree with. I see a clear difference between purchasing an app or game from the App Store and making an in-app purchase within an app or game after having installed it. My understanding of the new South Korean law is that it only pertains to in-app purchases, so the distinction, I believe, is more than just semantics.


I think the latter half of Apple’s statement is true — user trust in in-app purchases will decline. The gist of these legislative proposals — like this month’s “[Open App Markets Act](https://www.blumenthal.senate.gov/download/81121_-open-app-markets-act---bill-text)” from U.S. Senators Richard Blumenthal (D-CT), Marsha Blackburn (R-TN), and Amy Klobuchar (D-MN) — is, effectively, to require iOS and Android to be, to some degree, more like Mac and Windows. Setting aside the specific details, that’s what these laws are saying: phones should work like PCs in terms of loosening the control of the platform owners (Apple and Google) over what software can be installed, and what that software can do.


You may like the sound of that, or you may not. But there’s no denying that the result of any of these laws would be to make iOS and Google’s Android more like Macs and PCs. There’s also no denying that people make far more digital purchases and install far more apps on their mobile devices (iOS or Android) than their PCs (Mac or Windows).


In my experience, only two specific types of people want their phones to work significantly more like PCs, permission-wise. The first group is comprised of the technically-savvy — like many of you reading this — who feel confident in their own ability to gauge the trustworthiness of third-party software. The second group is business-minded people, who are thinking only about what percentage of purchases goes to whom, and are only thinking about the money. (I believe the legislators behind these proposals are swayed entirely by the business arguments, and do not understand the technical implications at all.)


But I am confident that the overwhelming majority of typical users are more comfortable installing apps and making in-app purchases on their iOS and Android devices than on their Mac and Windows PCs not *despite* Apple and Google’s console-like control over iOS and Android, but *because of* it. And if these measures come to pass and iOS and Android devices are forced by law to become pocket PCs, I think there’s a high chance it’ll prove unpopular with the mass market. The masses are not clamoring for the app stores to be opened up. These arguments over app stores are entirely inside baseball for the technical and business classes. I’ve had non-technical friends and relatives complain to me about all sorts of things related to their iPhones over the last 10 years, but never once have any of them said to me, “*Boy, I sure wish iPhone apps and games could ask me for my credit card number to make purchases, and that the overall experience of using apps was more like the anything-goes nature of using the web or my desktop computer.*” Never. It doesn’t just seem that the unintended consequences of such legislation is being under-considered; it seems as though it’s not being considered or acknowledged *at all*.


Perhaps I’m wrong, and it’ll all work out just fine. Anyone who claims to *know* how such a scenario will turn out is full of shit.


But from what I’ve seen over the last few decades, the quality of the user experience of *every* computing platform is directly correlated to the amount of control exerted by its platform owner. The current state of the ownerless world wide web speaks for itself.


---


The part of Apple’s statement about “Ask to Buy” and parental controls, though, I think is sophistry. It’s certainly true that the “Ask to Buy” feature *currently* wouldn’t work with third-party in-app payment processing, but that’s because nothing in iOS is built to support outside payment processing for in-app purchases. If required to support third-party payment processing, Apple could and should create APIs to support them through the existing “Ask to Buy” process, and the App Store guidelines could and should be expanded to require supporting all parental control APIs regardless of how payments are processed.


Most kids don’t have credit cards, either, when you think about it. I suppose a workaround for a wily kid could be to use cash to purchase a prepaid debit card, then use that debit card to make in-app purchases. Keep in mind too that apps which act as stores for physical goods *only* use third-party payment processing. When you sell physical goods through an app, not only *can* you process credit cards without going through Apple and Google’s in-app processing, you *have* to. Neither Apple nor Google allow in-app purchasing to be used for physical goods, because it wouldn’t even make sense for any retailer to pay a 30 percent processing fee for physical goods. This state of affairs for purchasing physical goods through apps doesn’t seem to have caused any problems for parents different from what kids can do purchasing physical goods on the web.


But the main thing to keep in mind about the South Korean legislation is that it has nothing to do with sideloading or third-party app stores, which *would* enable the sidestepping not just of all parental controls, but of all privacy controls — for children and adults alike — system-wide.


Adding support for third-party payment processing for in-app purchases in no way prevents Apple and Google from providing robust parental controls to approve kids’ in-app purchases. The rules that are enforced by policy matter, and in large part have worked.


---


My biggest concern regarding third-party payment processing for IAP is subscriptions, which I think Apple’s statement hints at only obliquely, with the phrase “[will] make it difficult to manage their purchases”.


*The* best feature of Apple’s in-app subscription system is that subscriptions are easy for users to manage, and impossible for developers to hide. In iOS, go to Settings → *Your iCloud Account* → Subscriptions. On the Mac, it’s somewhat less obvious. From the Music (née iTunes) app, go to Account → View My Account, and scroll down. Subscriptions is listed under Settings on the Account Information page. Or, in the App Store app, go to Store → View My Account, then click “View Information” in the window header. That gets you to the same Account Information page as in Music.


On either iOS or Mac, you can also get to the subscription management page by going to [this Apple support document](https://support.apple.com/en-us/HT202039) and tapping/clicking the prominent “See or cancel subscriptions” button at the top, which is currently just a link to [https://apple.co/2Th4vqI](https://apple.co/2Th4vqI) — but I’m not sure how permanent that URL is. Apple has had several such URLs to bounce you to the subscription management page on your current device over the years.


Once on this page, you get a comprehensive list of every active subscription you’ve made through Apple. You can manage each subscription (switching, say, from monthly to yearly), or, most essentially, *easily cancel any of them without one iota of undue hassle*.


My go-to counterexample is The New York Times. To cancel a subscription to The New York Times, [you need to call them on the phone or engage in an online chat](https://help.nytimes.com/hc/en-us/articles/360003499613-Cancel-your-subscription) with a “customer service representative” whose full-time job is convincing people *not* to cancel their subscription. And the Times makes it *easier* to cancel a subscription than many other publications and services do.


Apple’s subscription system makes it easy to track all of your subscriptions in a single list that isn’t hard to find, and makes it easy to cancel any of them. (Google Play offers something similar: in the Play Store app, tap your account avatar → Payments & Subscriptions → Subscriptions.) I can think of ways to improve this list for the benefit of users,1 but even as it stands it is exemplary compared to the alternative of managing each and every subscription — each publication, each streaming service, each subscription-based app — on a provider-by-provider basis, wherein each subscription provider can make cancellation or downgrading as hidden, obfuscated, and [dark-patterned](https://www.wired.com/story/lawmakers-take-aim-insidious-digital-dark-patterns/) as they choose.


Apple’s subscription system is so useful, so trustworthy, and so beneficial to my peace of mind that as a general rule I *only* subscribe to anything through it. Of course I make exceptions, but only for subscription providers whom I inherently trust.2 I just pored through my list, and of 27 active subscriptions from third-party services (i.e. not counting Apple’s own service like Apple One), I would *at most* have subscribed to only 9 of them. And I’m being generous; there are a few of those 9 that I’d have thought long and hard about subscribing to outside the App Store. In many cases it’s not about trusting the app developer, per se, but simply my reluctance to subscribe to something I’m likely to lose track of and forget about.


If3 Apple winds up acceding to these demands for third-party in-app payment providers — whether nation-by-nation as legislation passes, or by washing their hands of the entire controversy and making a worldwide policy change — I *really* hope they add APIs and mandate the use of them such that *however* you pay in-app, any subscription made in-app must show up in this list, and the provider must support no-hassle cancellation from within the system interface. Renewal receipts and upcoming renewal reminders should be mandatory, too.


Otherwise, this would be a huge loss for users — and one that never seems to be considered in debates over legislation such as South Korea’s.


---

1. To name a few: (1) the list of subscriptions should display how much you’re paying — as it stands you have to tap into each subscription to see the amount; (2) [the sort order varies by device](https://twitter.com/gruber/status/1432802433017815045) — on some of my devices the list is sorted by renewal/expiration date, but on others, the order is seemingly random; (3) [there are some really weird bugs](https://twitter.com/rzara/status/1432829680218955777) in how the list is displayed; (4) the list is *really* slow to load. ↩︎
2. I can’t *not* mention my own [Dithering](https://dithering.fm/) podcast, cohosted with Ben Thompson, and Thompson’s own [Stratechery](https://stratechery.com/) newsletter. We only sell subscriptions directly. To name one reason: because we don’t have (or want to have) apps through which to sell in-app subscriptions. Unsubscribing from Dithering (and/or Stratechery) is very easy (but, admittedly, I don’t recommend it). [Substack](https://substack.com/), too, makes managing subscriptions easy and obvious. In general, the larger and more corporate a publication, the harder they tend to make it to unsubscribe. ↩︎︎
3. I still say it’s a big *if* as to whether Apple and Google wind up acceding to this law in South Korea, at least as it seems to be intended. Just spitballing ideas, I think they’d be compliant if they made “Allow third-party payment processing for in-app purchases” an off-by-default preference in the system-wide security settings, with warnings that must be OK’d when enabled, *a la* the options on MacOS and Android to allow installing apps from outside the platforms’ respective app stores. That’s actually not a bad middle ground, in my opinion, but it sure as shit is not what, say, Epic is looking for. ↩︎︎



| **Previous:** | [Charlie Watts](https://daringfireball.net/2021/08/charlie_watts) |
| **Next:** | [Initial Details on Using Driver’s Licenses and State ID’s in Apple Wallet](https://daringfireball.net/2021/09/initial_details_on_ids_in_apple_wallet) |


PreviousNext