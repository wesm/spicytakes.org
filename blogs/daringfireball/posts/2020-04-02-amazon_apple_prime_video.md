---
title: "Amazon and Apple Strike Deal for Prime Video In-App Purchases and Subscriptions"
date: 2020-04-02
url: https://daringfireball.net/2020/04/amazon_apple_prime_video
slug: amazon_apple_prime_video
word_count: 1911
---


[Benjamin Mayo, writing for 9to5Mac](https://9to5mac.com/2020/04/01/purchases-amazon-prime-video/) yesterday:


> In a significant shift, the Amazon Prime Video app on iOS and
> Apple TV now features a built-in content store. This means users
> can now buy or rent TV shows and movies directly inside the app on
> Apple platforms. The change was [first spotted by The Verge](https://www.theverge.com/2020/4/1/21203294/amazon-prime-video-ios-in-app-purchases-iphone-ipad-apple-tv-change).
> For the longest time, Amazon did not support this because of
> Apple’s App Store rules which require the developer to use Apple’s
> In-App purchase system for digital content and give 30% of the
> revenue to Apple. The app now seems to use Amazon payment method
> if you have a card on file, otherwise it uses Apple In-App
> Purchase.


I’ve been digging into this since the news broke, and I think it’s even more significant than Mayo suggests. It’s not about whether Amazon has a credit card on file for your account — it’s about whether you’re already a Prime subscriber.


Here’s Apple’s official statement, which I was given yesterday:


> Apple has an established program for premium subscription video
> entertainment providers to offer a variety of customer benefits —
> including integration with the Apple TV app, AirPlay 2 support,
> tvOS apps, universal search, Siri support and, where applicable,
> single or zero sign-on. On qualifying premium video entertainment
> apps such as Prime Video, Altice One and Canal+, customers have
> the option to buy or rent movies and TV shows using the payment
> method tied to their existing video subscription.


I’ve never heard of [Altice One](https://www.optimum.com/appletv) prior to this (it’s a regional cable provider), and [Canal+](https://www.canalplus.com/) I only know as a service popular in France. (So the “+” is pronounced *plooce*, not *pluss*.) So while Apple is technically correct that this program isn’t new, with the addition of Prime Video it’s *effectively* new to most of us.


Here’s how it seems to work.


First, Amazon’s Prime Video app only works if you’re signed in with an Amazon account. You can create a new account in the app, but you need to be signed in before you can proceed. ([Screenshot](https://daringfireball.net/misc/2020/04/prime-video-01-signup.png).) I’m using *app*, singular, and showing screenshots from iOS, but everything here applies equally to the Prime Video apps for iOS, iPadOS, and tvOS.


## If Your Amazon Account Has an Existing Prime Subscription


If you already subscribe to Prime (full Prime or just Prime Video), when you rent or purchase a movie in the app, the transaction is now handled by Amazon, using your credit card on file with Amazon. This is, in plain English, an in-app purchase insofar as you are making a purchase within the app, but it is *not* an Apple In-App Purchase. The interface is Amazon’s, and the transaction is processed by Amazon.


Amazon’s permission to do this — to process credit card transactions on its own, right in the app — is new as of yesterday. And while Altice One and Canal+ have apparently been in the same program for some time, for most of us this is unprecedented. Apple’s insistence that all in-app purchases of digital content go through Apple’s official In-App Purchase mechanism — giving Apple its significant cut of each transaction — has been so steadfast ever since the inception of the App Store in 2008 that many observers genuinely wondered if Amazon had gone rogue yesterday, and was doing this without Apple’s permission, hoping to provoke a high-stakes fight.


But this is completely sanctioned by Apple. If you have an existing Prime account — one you signed up for at Amazon’s website — you can now purchase and rent movies and TV shows in the Prime Video app directly through Amazon. Apple doesn’t see a dime.


## If Your Amazon Account Does Not Have a Prime Subscription


If the Amazon account you’re signed into does *not* have a Prime subscription, you can purchase or rent movies in the Prime Video app, and they will be processed as Apple In-App Purchases. *This is true even if Amazon has a credit card on file for your account.* If you are not subscribed to Prime, in-app purchases are Apple’s In-App Purchases.


That’s not even the *most* interesting part. If you don’t subscribe to Prime, *you can subscribe to Prime Video in-app for $9/month and it’s an Apple iTunes subscription*. Apple gets a cut and your subscription to Prime Video is managed like any other iTunes subscription.


[
](https://daringfireball.net/misc/2020/04/prime-video-subscribe.png)


You get the same one-month free trial, and pay the same $9/month price thereafter, that you get when you sign up for Prime Video directly on Amazon.com. And it’s a full cross-platform Prime Video account — you can use it to watch Prime Video content on the web, on Android devices — anywhere. (If you sign up through iTunes and subsequently buy or rent a movie from an Android or Fire TV device, it gets billed directly to your credit card, not through iTunes.)


On Amazon’s website, if you go to Prime Video → Settings, it is very clear that your account is managed through iTunes, and Amazon provides a very clear “Edit in iTunes” button.


[
](https://daringfireball.net/misc/2020/04/prime-video-web-settings.png)


On MacOS 10.15 Catalina, clicking the “Edit in iTunes” button takes you to the subscriptions management section of your account settings in Apple’s Music app; on iOS, it takes you to the subscriptions management section in the iTunes Store app.


In the Payment Settings section pictured above on Amazon’s website, you can add a credit card payment method for “rentals or purchases”. However, if your Prime Video subscription is through iTunes, in-app purchases on Apple devices will still go through Apple. This payment option only applies when buying or renting movies in Prime Video on non-Apple platforms. (I tested it on the web and Android.)


If you do not have a saved payment method in your Amazon account, when you attempt to purchase or rent a movie in the Prime Video app on Android, you will be prompted for your credit card info.


## What Happens If You Sign Up for Full-Fledged Prime If You’re Subscribed to Prime Video Via iTunes


There are two ways to get Prime Video content: a full-fledged Prime subscription (which includes all the free/discounted shipping benefits from real-world Amazon purchases, Amazon Music, etc.) or a Prime Video subscription. Full-fledged Prime costs $13/month; Prime Video costs $9/month. So what happens if you subscribe to Prime Video through iTunes, but subsequently decide to upgrade to a full-fledged Prime subscription at Amazon?


Well, you don’t really get to “upgrade”. You subscribe to Prime at Amazon.com as though you’re altogether new to Prime. You must have a saved credit card on your account, and after your one-month trial, you’ll be charged the full $13/month in addition to your existing $9/month iTunes subscription to Prime Video.


When you then visit your Prime Video settings — either on Amazon’s website or in the Prime Video app — Amazon displays a prominent warning in red: “You might be charged twice for Prime Benefits.” (Screenshots: [web](https://daringfireball.net/misc/2020/04/prime-video-web-warning.png) and [app](https://daringfireball.net/misc/2020/04/prime-video-app-warning.png).)


## The Quid Pro Quo


Let’s return to Apple’s statement on this program:


> Apple has an established program for premium subscription video
> entertainment providers to offer a variety of customer benefits —
> including integration with the Apple TV app, AirPlay 2 support,
> tvOS apps, universal search, Siri support and, where applicable,
> single or zero sign-on.


What Apple is saying here is that for a video subscription service — pardon me, a *premium* video subscription service — to qualify for this program, the service has to support all of Apple’s features for video content apps: AirPlay 2 support, a native tvOS app, single sign-on if applicable, universal search and Siri support (so if you search in the TV app for a show or movie, results from Amazon Prime Video show up). This includes integration with the TV app for features like Up Next — start watching a TV series in Prime Video and when you go to Apple’s TV app (on any device) your next episode should appear in Up Next. Supporting all of these features is a *lot* of work, and Amazon has done it all.


So the deal seems to be this:

- The Prime Video app supports every feature that makes a third-party subscription video service a first-class citizen in Apple’s multi-device TV ecosystem.
- For users with existing Prime subscriptions, or new subscriptions made on Amazon’s website, Amazon now gets to bill them directly for movie rentals and purchases made in the app, giving Apple no cut of the transactions.
- Users can subscribe to Prime Video in-app using an iTunes subscription, giving Apple a recurring cut, and leaving subscription management in Apple’s hands.
- For users without a Prime subscription, or with a Prime subscription made through the app, Amazon now bills them for purchases and rentals through Apple’s In-App Purchase mechanism, giving Apple a cut.


Why would Apple agree to this? Financially, Apple now gets a cut of *some* Prime Video rentals and purchases, and a recurring cut of new Prime Video subscriptions made in-app. And Apple TV users get all the benefits from the Prime Video app supporting AirPlay 2, universal search, and integration with the TV app that Apple is trying to make the default interface for watching shows and movies. Prior to this deal, Apple made *nothing* from Prime Video — it was a free app with no in-app purchases, and there was no way to subscribe to Prime Video through iTunes.


Why would Amazon agree to this? Amazon now gets to sell movies and TV shows directly in the Prime Video app for iOS and tvOS users. For existing Prime subscribers, they get to keep all of the money from these purchases and rentals. The tricky question is why would Amazon agree to allow people to subscribe to Prime Video through iTunes, giving Apple a cut of the recurring subscription. Apple’s standard terms for subscriptions are a 70/30 percent split for the first year, and 85/15 thereafter. I would bet that Amazon negotiated more favorable terms than this, but no one outside Amazon and Apple know that. (It is widely understood that Netflix negotiated more favorable terms with Apple back when Netflix supported subscriptions through iTunes — they had an 85/15 split for the first year, too.) But even if Amazon is getting the standard 70/30-then-85/15 terms — I doubt that, but let’s just say even if they are — I can see why they’d agree to it if they think they’ve already saturated the potential market for Prime subscribers they can get on their own.


If their new sign-ups for Prime are tapering off in the U.S. — which seems very possible, given how popular Prime is and how long it’s been around — any new subscriptions they can get through in-app iTunes subscriptions may well be worth the recurring cut Apple will take. There’s practically zero risk that any existing Prime Video subscribers are going to cancel just to resubscribe using iTunes, and even *less* risk that any full-fledged Prime subscribers would downgrade to Prime Video only. It’s all upside for Amazon, even with Apple’s cut of in-app transactions.


It’s a win for Apple, a win for Amazon, and a win for users in the Apple TV ecosystem.


Amazon has, effectively, pulled a [reverse Netflix](https://techcrunch.com/2018/12/31/netflix-stops-paying-the-apple-tax-on-its-853m-in-annual-ios-revenue/).



| **Previous:** | [Regarding Zoom](https://daringfireball.net/2020/03/regarding_zoom) |
| **Next:** | [COBOL, Programming, and Coding](https://daringfireball.net/2020/04/cobol_programming_coding) |


PreviousNext