---
title: "App Store Subscription Uncertainty"
date: 2016-06-08
url: https://daringfireball.net/2016/06/app_store_subscription_uncertainty
slug: app_store_subscription_uncertainty
word_count: 1680
---


From [Lauren Goode’s interview with Phil Schiller for The Verge](http://www.theverge.com/2016/6/8/11880730/apple-app-store-subscription-update-phil-schiller-interview), specifically regarding the new 85/15 revenue split after the first year of a subscription (italic emphasis mine):


> But Schiller insisted that it wasn’t any kind of “Apple tax”
> backlash or companies encouraging users to go to their own
> websites that drove Apple’s new subscription model: “It wasn’t
> done from a negative like that,” he says. When I asked about this,
> he stresses that it was “absolutely done because we recognize that
> developers do a lot of work to retain a customer over time in a
> subscription model, and we wanted to reward them for that by
> helping them to keep more of the revenue.” Apple can help drive
> customers to the original download, Schiller argues, but only the
> developer can keep the customer over time and “we want to incent
> them to do that.”
> Schiller imagines scenarios where many kinds of apps that were
> previously single-time purchases could move to the model. Games
> that have an ongoing subscription-like program, ones that have a
> massive online playing world that require upgrades of game worlds,
> might make sense. *He suggests many enterprise apps could move to
> subscription, and that professional apps that require “a lot of
> maintenance of new features and versions” would be a good fit.*


That’s pretty much exactly what Schiller told me yesterday too, which colored my take on the breadth of apps that could take advantage of subscription pricing. [I wrote](http://daringfireball.net/2016/06/the_new_app_store):


> This dramatically changes the economics of the App Store. Until
> now, productivity apps could charge up front as paid downloads and
> that was it. Updates had to be free, or, to charge for major new
> versions, developers would have to play confusing games by making
> the new version an entirely new SKU in the app store. Twitter
> clients like Tweetbot and Twitterrific, for example, did this, to
> justify years of ongoing development. Now, apps like this can
> instead charge an annual/monthly/etc. subscription fee.


But Apple’s own “[What’s New in Subscriptions](https://developer.apple.com/app-store/subscriptions/whats-new/)” web page makes this uncertain:


> Starting this fall, apps in all categories on the App Store will
> be eligible to offer in-app purchases for auto-renewable
> subscriptions to services or content. Users enjoy the reliability
> that comes with subscribing to a service that they love, and the
> experience must provide ongoing value worth the recurring payment
> for an auto-renewable subscription to make sense. Although all
> categories of apps will be eligible, this business model is not
> appropriate for every app.
> Like many freemium apps, successful auto-renewable subscription
> apps operate as services that are continuously supported, and
> often require sustained content development or feature
> enhancements to retain users. Whether updating content on a
> regular basis, providing on-demand use of a service, or giving
> access to a large collection of content, successful auto-renewable
> subscription apps are equipped to offer continued utility and
> enjoyment to their subscribers.


In a sidebar titled “Types of Auto-Renewable Subscriptions”, Apple lists only two, “Content” and “Services”:


> Content 
> Services 
> Provide paid access to an ongoing service within your app, such as
> cloud storage or massive multiplayer online games (MMOGs).


Professional apps that require “a lot of maintenance of new features and versions” don’t fit either of those categories. *Would* Twitter clients like Tweetbot and Twitterrific qualify for subscription pricing? After talking to Schiller yesterday, I thought so. Now, I don’t know. Developers are definitely confused.


[Brent Simmons](http://inessential.com/2016/06/08/seeking_clarification):


> I have a side project, a Mac app, that I could also do as an iOS
> app. I have no plans to do so — but the news about subscriptions
> and free trials makes me reconsider.
> It *might* be sustainable with this new model.
> But here’s the thing: the app is a stand-alone thing. I’m not
> running a backend web service for it. Would it be okay to use the
> subscription-based pricing? […] What does “not appropriate”
> mean? Does that mean rejection? Or is that just a warning that
> it’s maybe not the best fit, but it’s okay to try it anyway?


---


Schiller obviously knows what he’s talking about, but what he’s said seems to be outside the new written rules. So I think what Apple is trying to do here is discourage *frivolous* use of subscriptions. I think it’s obvious from Apple’s own description that while apps from any *category* are now allowed to offer subscription, that doesn’t mean every *app* will be allowed to. Like with many App Store rules, Apple doesn’t spell things out in detail in order to preserve control and flexibility. Like Justice Potter Stewart’s “[I know it when I see it](https://en.wikipedia.org/wiki/I_know_it_when_I_see_it)” definition of “obscenity”, I think Apple wants to define “good use of the subscription business model” as “we know it when we see it”.


The problem with that is that developers don’t know whether they’re going to be approved or not. As it stands, they would need to do all the engineering (and design) work to support subscriptions, submit the app, and wait to see if it’s approved and perhaps appeal if it isn’t. That’s bad enough for an existing app whose developer wants to switch to subscription pricing. But this uncertainty is downright untenable for a new app whose developer sees subscription pricing as the only sustainable business model to justify the app’s development in the first place.


The letter of the rules Apple has posted creates counterintuitive incentives for developers. An app with its own proprietary sync service can use the subscription model, but a competing app that provides the same features using CloudKit cannot. But Apple *wants* developers to use iCloud.


I think Apple should just allow any app to offer subscription pricing, period. Apple’s role should be as the trusted platform vendor, making sure users can easily cancel subscriptions, requiring opt-in to any pricing changes, and making sure no one is being tricked or confused in any way. Otherwise Apple should allow developers to define their use of subscriptions as they see fit. In the same way that developers with paid-up-front apps can pick their own price, and users determine whether it’s worth it or not, developers of subscription-based apps should be able to define their own “here’s what you get when you subscribe” features and let users decide whether they’re worth the price or not. I don’t think Apple ought to control this — the market will work itself out. People won’t sign up for a bad subscription offering for the same reasons they don’t sign up for bad subscription deals in the world outside the App Store.


Apple needs to clarify this to remove the uncertainty.


---


Another question: If an app is deemed qualified to use subscription pricing, must it be functional in some limited way without a subscription? Apps that use in-app purchases *must* be functional without the IAP. Is that true for subscription-based apps too?


My understanding is that if an app gets approved for subscription pricing, then it is up to the developer whether the app is useful without a subscription. A simple comparison: Spotify and Netflix. Spotify plays music for free (with ads) even if you don’t pay them a nickel. Netflix, on the other hand, doesn’t offer any content to non-subscribers. I’d like to see Apple clarify this too.


---


I should add that I don’t think subscription pricing — even if Apple clarified that subscriptions are open to any app, period — are a panacea. There is no perfect way to sell software. The old way — pay up front, then pay for major upgrades in the future — has problems, too, just a different set of problems. If I had my druthers Apple would enable paid upgrades in the App Store(s), but I get the feeling that’s not in the cards. That leaves us with subscriptions.


DF reader Sean Harding framed the problems with subscription pricing well, [in a short series of tweets](https://twitter.com/sharding/status/740649776882950144):


> I think the new stuff is good, but I don’t think it really solves
> the upgrade pricing problem from a customer standpoint. A sub
> forces me to effectively always buy the upgrade or stop using even
> the old version. I don’t dislike subscriptions because I don’t
> want to pay. I just want freedom to decide if the new features are
> worth paying for.


[Tapbots developer Paul Haddad](https://twitter.com/tapbot_paul/status/740616701625044992):


> I’d probably be fine with a subscription model, if they degraded
> nicely. Stop paying, app still works but no more upgrades. That
> seems fair.


That’s a nice notion, but I’m pretty sure the App Store doesn’t allow for that and never will. A nice side effect of paid downloads is that you, the user, can keep using an old version of an app until it technically no longer runs, because of an OS update or something like that (e.g. a PowerPC binary that no longer runs on Intel-based Macs — a scenario that could happen again if Apple starts putting ARM chips in Macs). With software-as-a-service, when you stop paying for the service, you don’t get to keep using the current version of the app — or if it’s a freemium model, you don’t get to keep using the non-free features that were previously enabled via the subscription.


I can see why some people don’t like this. I personally have a few not-the-latest-version apps that I’m glad still work for me. But this is the way the software economy is moving. Nobody expects a subscription web app/service to continue working if you stop paying for it. With Adobe and Microsoft leading the way, that’s the way the economics of app development are shifting too.



| **Previous:** | [The New App Store: Subscription Pricing, Faster Approvals, and Search Ads](https://daringfireball.net/2016/06/the_new_app_store) |
| **Next:** | [Brief Thoughts and Observations Regarding Today’s WWDC 2016 Keynote](https://daringfireball.net/2016/06/thoughts_and_observations_wwdc_2016) |


PreviousNext