---
title: "If a Third-Party App Store Falls in the Forest and No One Uses It, Does It Make a Sound?"
date: 2022-12-14
url: https://daringfireball.net/2022/12/third_party_app_store_forest
slug: third_party_app_store_forest
word_count: 2009
---


Mark Gurman dropped a seemingly-explosive report yesterday at Bloomberg, now under the headline “[Apple to Allow Outside App Stores in Overhaul Spurred by EU Laws](https://www.bloomberg.com/news/articles/2022-12-13/will-apple-allow-users-to-install-third-party-app-stores-sideload-in-europe)”. I say *now* because the original headline was a little less assertive: “Will Apple Allow Users to Install Third-Party App Stores, Sideload in Europe?” I suspect the original headline was more accurate, because most of this seems up in the air.


The Bloomberg report starts:


> Apple Inc. is preparing to allow alternative app stores on its
> iPhones and iPads, part of a sweeping overhaul aimed at complying
> with strict European Union requirements coming in 2024.
> Software engineering and services employees are engaged in a major
> push to open up key elements of Apple’s platforms, according to
> people familiar with the efforts. As part of the changes,
> customers could ultimately download third-party software to their
> iPhones and iPads without using the company’s App Store,
> sidestepping Apple’s restrictions and the up-to-30% commission it
> imposes on payments.


That last bit — that any of this will allow developers to avoid Apple’s commissions on purchases and subscriptions — is the first of my quibbles with Gurman’s report. I don’t think that’s mandated by the EU, and everyone knows it’s not what Apple wants. I think whatever Apple is devising to comply with this law, they’re still going to demand a commission on digital purchases. That last sentence surely strikes many of you as nutty. In most people’s minds, whether they’re personally invested (because, say, they’re developers whose apps are subject to Apple’s App Store commission fees) or just following the saga as interested observers or enthusiasts, these commission fees are seemingly among the most controversial issues, and thus must surely be square in the bullseye of the E.U. regulators who drafted the [Digital Markets Act](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32022R1925&qid=1671035664732&from=EN) (DMA).


But that’s what many interested observers thought about [Dutch regulators mandating new rules for dating apps](https://daringfireball.net/2022/02/going_dutch), yet Apple’s policy changes to comply with the rules from the Netherlands ACM simply instituted a new 27 percent commission rate for dating apps that use alternate in-app payment processors or links to the web. I suspect Apple has something similar in mind for compliance with the DMA. The commission rate [might be lower](http://www.fosspatents.com/2022/07/googles-new-european-in-app-payment.html), but Apple is going to want a commission. Tim Cook’s testimony in the Epic lawsuit revealed that [Apple doesn’t see its App Store commissions as a fee for the App Store itself](https://www.theguardian.com/technology/2021/may/20/apple-epic-games-trial-tim-cook-testimony), but for being on the iOS platform at all. Collecting those commissions through the App Store is just the easiest and most direct way to do it.


Gurman:


> The changes underway within Apple are being led by Andreas
> Wendker, a longtime software engineering vice president who
> reports to Craig Federighi, the company’s top software executive.
> Jeff Robbin — Apple’s top engineering manager for its services,
> who reports to head of services Eddy Cue — is also involved.
> Apple is applying a significant amount of resources to the
> companywide endeavor. It hasn’t been a popular initiative within
> Apple, considering that the company has spent years decrying the
> need for “sideloading” — the process of installing software
> without using the official App Store. In lobbying against the new
> European laws, Apple has argued that sideloading could put unsafe
> apps on consumers’ devices and undermine privacy.
> Some engineers working on the plan also see it as distraction from
> typical day-to-day development of future features, according to
> the people. The company is aiming for the changes to be ready as
> part of an update to next year’s iOS 17, which would be in line
> with requirements.


That Apple is working on this for next year’s iOS 17 is one of those “surprising yet not surprising” stories, much like the rumors that at least some of next year’s new iPhone models will switch from Lightning ports to USB-C. Surprising, because Apple clearly doesn’t want to do these things — at least not at the behest of regulators. But not surprising, because [of course Apple is going to comply with E.U. laws](https://daringfireball.net/linked/2022/10/26/stern-federighi-joz), whether it agrees with those laws or not.


Given that the DMA requires compliance by March 2024, Apple would have to make these changes part of its plans for iOS 17, which is almost certainly going to be released in September 2023.


Gurman:


> To help protect against unsafe apps, Apple is discussing the idea
> of mandating certain security requirements even if software is
> distributed outside its store. Such apps also may need to be
> verified by Apple — a process that could carry a fee. Within the
> App Store, Apple takes a 15% to 30% cut of revenue.
> Apple hasn’t made a final decision on whether to comply with a
> component of the Digital Markets Act that allows developers to
> install third-party payment systems within their apps. That
> would let users sign up for subscriptions to a travel app, for
> example, or buy in-app content from a game maker — without
> involving Apple.


Again, I don’t think the DMA requires Apple or Google to allow third-party in-app payment processing from which they don’t require a commission. I say “think” because the DMA is well over 100 pages, and, well, to my eyes, [written in opaque bureaucratic language](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32022R1925&qid=1671035664732&from=EN). One way to glean through the passages you might find interesting is to search for the terms “application store” and “payments”.


As for sideloading apps and allowing for third-party app stores, here’s the relevant passage from the DMA (Chapter III, Article 6, section 4):


> The gatekeeper shall allow and technically enable the installation
> and effective use of third-party software applications or software
> application stores using, or interoperating with, its operating
> system and allow those software applications or software
> application stores to be accessed by means other than the relevant
> core platform services of that gatekeeper. The gatekeeper shall,
> where applicable, not prevent the downloaded third-party software
> applications or software application stores from prompting end
> users to decide whether they want to set that downloaded software
> application or software application store as their default. The
> gatekeeper shall technically enable end users who decide to set
> that downloaded software application or software application store
> as their default to carry out that change easily.
> The gatekeeper shall not be prevented from taking, to the extent
> that they are strictly necessary and proportionate, measures to
> ensure that third-party software applications or software
> application stores do not endanger the integrity of the hardware
> or operating system provided by the gatekeeper, provided that such
> measures are duly justified by the gatekeeper.
> Furthermore, the gatekeeper shall not be prevented from applying,
> to the extent that they are strictly necessary and proportionate,
> measures and settings other than default settings, enabling end
> users to effectively protect security in relation to third-party
> software applications or software application stores, provided
> that such measures and settings other than default settings are
> duly justified by the gatekeeper.


Right in the first sentence, there’s a big *or*: “third-party software applications *or* software application stores”. I *think* what the E.U. means here is that “gatekeepers” are required to support both sideloading individual apps *and* entire third-party app stores (which, I think would really just be front ends to sideloading), but all it says is “or”, which perhaps means a gatekeeper can choose to support one or the other. (The DMA seems overly concerned with users being able to specify defaults, but I don’t even know what a default app store would mean. I guess that it means when you search on the home screen or ask Siri for an app, the home screen or Siri must be allowed to default to providing search results from a third-party app store?)


The second paragraph above seems to be ripe for years of legal squabbling. The E.U.’s intent, I think, is to say that Apple can still require apps be submitted for approval, whether they’re going to be distributed outside the App Store or not. But doesn’t that defeat the entire point? Anyone who is hoping that the DMA is going to force Apple to allow any and all third-party software you can imagine — more or less requiring Apple to treat iOS like it does MacOS — is, I think, setting themselves up for disappointment. That’s certainly not what Apple wants or thinks would be best for (most) iOS users, and I don’t think it’s what the DMA mandates.


Back to that “or”. Riley Testut is the developer behind [AltStore](https://altstore.io/), a no-jailbreak alternative iOS app store that works by distributing apps as developer betas. [Testut wrote a concise Twitter thread](https://twitter.com/rileytestut/status/1602803031984279552) arguing in favor of sideloading but, more or less, *against* third-party app stores:


> If, for example, Meta made an app store, they’d want exclusive
> apps. Unfortunately these apps don’t exist yet, so what can
> they do in the meantime? Pay App Store devs to leave the App
> Store of course!
> And it wouldn’t be just Meta — *every* app store would want
> exclusive apps to compete. And because literally all iOS apps
> are currently in the App Store, there’s simply no way to amass
> a competitive app library fast enough without poaching App
> Store apps.
> Here’s what I see happening:
> Instagram? They moved to Meta’s store for obvious reasons, so you
> can no longer receive updates unless you also install Meta’s store.
> That note taking app you’ve been using for years? They’re tired of
> paying Apple 30%, so they’re now in Epic’s store!
> Now you HAVE to use 3 different app stores, or else you’ll lose
> access to the apps you’re already using!
> So yes, it’s a choice — but the choice is NOT “do I use 3rd party
> stores to get cool new apps”
> Instead it’s: do I use 3rd party stores *just to keep using my
> current apps*.


Which leads me to my biggest question: who would get to run these third-party app stores? As far as I can tell, the DMA doesn’t say. Anyone and everyone with an Apple developer account in good standing? Or just anyone and everyone? (Apple has banned Epic Games from publishing games through the App Store, but might be required to allow Epic Games to run an entire app store?)


If this comes to pass, I foresee a byzantine approval system imposed by Apple *even if Apple comes into it with nothing but the best intentions*. That is to say, even if Apple’s attitude is to make third-party app stores as appealing and useful as possible, the approval process would still come with requirements and contractural obligations that very few companies could comply with. And I somehow doubt that Apple’s attitude would be “let’s make third-party app stores as appealing and useful as possible”. What happens if Apple makes both running and using third-party app stores as unappealing as possible under the law?


After more than a day of digging through the DMA, I conclude mostly that while it might be well intentioned, it’s horribly written. (And, to be honest, I question its intentions.)


[I disagree](https://daringfireball.net/2021/09/why_still_lightning) with the European Commission’s USB-C mandate, but at least it’s clear: If you make certain types of devices and those devices have charging ports, those charging ports need to be USB-C. The DMA’s third-party app store mandate is not only unclear, it’s like house-building regulations written by people who have no experience with architecture or carpentry — and who apparently don’t think that architecture or carpentry expertise are necessary for dictating how houses should be built.



| **Previous:** | [Two Weeks Later and Twitter Is Still Up](https://daringfireball.net/2022/12/twitter_still_up) |
| **Next:** | [I Wish I Could Tell You This One Is Not All About Twitter](https://daringfireball.net/2022/12/i_wish_i_could_tell_you_this_is_not_all_about_twitter) |


PreviousNext