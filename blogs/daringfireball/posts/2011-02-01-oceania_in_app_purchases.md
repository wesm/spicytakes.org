---
title: "Oceania: We Have Always Required Books From the Eurasian E-Bookstore to Be Sold Through Our In-App Purchasing System"
date: 2011-02-01
url: https://daringfireball.net/2011/02/oceania_in_app_purchases
slug: oceania_in_app_purchases
word_count: 1010
---


When I went to bed last night, [this NYT story had just hit](http://www.nytimes.com/2011/02/01/technology/01apple.html). Sony went to The Times with the story that their iOS e-book reader app had been rejected by Apple, because book purchases weren’t made through Apple’s in-app purchasing system. (Which system, let’s be clear up front, gives Apple a 30 percent cut of the revenue.)


It remains unclear from The Times’s story just how Sony’s app, as submitted to Apple, works. Amazon’s Kindle app and Barnes & Nobles’s Nook app don’t use Apple’s in-app purchasing system, either — but they don’t allow purchasing within their apps, period. You purchase books through a web browser, then you can access those books through the apps.


In short, it wasn’t clear at all, from Sony’s story, whether anything had changed:


> Some application developers, including Sony, say Apple has told
> them they can no longer sell content, like e-books, within their
> apps unless the transactions go through Apple’s system.


Taken literally, that paragraph implies nothing has changed, because no third-party iOS e-book apps allow in-app purchases that circumvent Apple’s system.


Today, Apple has clarified, to some degree, what’s going on. [Jim Dalrymple reports](http://www.loopinsight.com/2011/02/01/apple-responds-to-sony-in-app-purchase-report/):


> “We have not changed our developer terms or guidelines,” Apple
> spokesperson, Trudy Muller, told The Loop. “We are now requiring
> that if an app offers customers the ability to purchase books
> outside of the app, that the same option is also available to
> customers from within the app with in-app purchase.”


Translation: *We haven’t changed the rules, but what used to be allowed is no longer allowed.*


Yeah, that makes total sense.


[Jason Kincaid has a good rundown](http://techcrunch.com/2011/02/01/apple-nothing-has-changed-except-for-this-one-thing/) of how this is, indeed, a change in de facto policy, regardless of whether there’s been any change to Apple’s *written* policies. Kincaid points to section 11.2 in Apple’s iOS developer guidelines, which state:


> Apps utilizing a system other than the In App Purchase API (IAP)
> to purchase content, functionality, or services in an app will be
> rejected.


Kincaid writes:


> Now, Amazon’s Kindle app doesn’t conduct its purchases through
> the app itself — users are instead kicked off to a browser where
> they actually buy their books, and that content is then synced to
> the Kindle app. Apple’s rule is worded vaguely enough that it
> can claim this workaround is in violation of the guidelines. But
> it obviously hasn’t been enforced like this before now, so the
> notion that nothing has changed is clearly false.


I.e., Apple’s official stance seems to be that the rules haven’t changed, but they weren’t enforcing them until now. Sony’s iOS app may well act exactly like Amazon’s Kindle app, but apparently that behavior is no longer permitted.


Even if you take aside the double-speak “We have not changed our developer terms” preface, Apple’s stated explanation of the new rules leave several unanswered questions.


Does the new policy really only apply to “books”, specifically? Apple gave the identical statement to several publications, each time specifically saying “books”. I would assume, though, that this applies to any purchased content, not just books. Books are simply the first type of content for which these rules are being applied.


What about pricing? Can Amazon comply with these new rules by selling its Kindle books through Apple’s in-app purchasing system with a 43 percent markup, to account for Apple’s 30 percent cut through the in-app API? Consider a Kindle book that Amazon sells for $10. Can they sell it for $14.30 through in-app purchasing? That way Amazon’s cut would remain $10. Or will Apple insist on price matching, meaning Amazon can only comply by accepting 30 percent less revenue on books purchased in-app compared to those purchased from Amazon directly?1


My guess is that Sony is getting hurt because they were late to the game. Amazon’s Kindle app precedes the existence of Apple’s in-app purchasing API. I thoroughly doubt Apple is going to pull the Kindle (or Nook) app from the App Store, but I’ll bet they’re already in discussions with Amazon (and Barnes & Noble) about how these apps need to change going forward. It’s easier to reject Sony’s app as a first step toward the application of new rules because Sony’s app is brand-new — Apple isn’t taking anything away from users that was previously available to them.


This sucks for Sony because, for now, they’re locked out of the App Store. It sucks for Amazon and Barnes & Noble too, if I’m right that, going forward, they’re going to have to offer in-app purchasing as an option. But you can’t say it’s surprising that the rules are evolving toward more money for Apple while *improving* the experience for users — that’s win-win from Apple’s perspective. Here’s the de facto rule, in a nut: If you have an app in the App Store, Apple gets a cut of the dough from the app.


It’s hard to imagine Amazon accepting a 70/30 split from Apple. But I can’t see Amazon pulling their iOS Kindle apps, either. Amazon could switch to mobile web app clients for Kindle-reading on iOS, but I don’t think they could do so without taking a hit in terms of user experience. And users simply expect that apps come from the App Store. My guess is that Amazon will bite the bullet and adopt Apple’s in-app purchasing APIs.


Don’t forget, either, that [tomorrow is Apple’s joint appearance with News Corp.](http://www.electronista.com/articles/11/01/27/the.daily.official.for.feb.2.with.apples.eddy.cue/) to announce The Daily, and new in-app *subscription* purchasing APIs for native iOS apps. I wouldn’t be surprised if Apple has more to say about in-app purchasing rules for books and periodicals at or after tomorrow’s event.


---

1. It’s worth noting that [Amazon isn’t above strong-arm pricing tactics](http://www.nytimes.com/2010/03/18/technology/internet/18amazon.html?partner=rss&emc=rss) — they insist on price matching for titles in the Kindle store. And [it’s not like you can buy iBooks (or Sony) e-books on Kindle devices](http://parislemon.com/post/3051758905/apple-states-the-obvious-and-inevitable). ↩︎



| **Previous:** | [Cold Water on the iPad 2 Retina Display Hype](https://daringfireball.net/2011/01/cold_water_ipad_retina_display) |
| **Next:** | [Push Pop Press](https://daringfireball.net/2011/02/push_pop_press) |


PreviousNext