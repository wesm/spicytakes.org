---
title: "What’s the Deal With Sensor Tower?"
date: 2023-08-05
url: https://daringfireball.net/2023/08/whats_the_deal_with_sensor_tower
slug: whats_the_deal_with_sensor_tower
word_count: 2443
---


[Hayden Field, reporting for CNBC last month](https://www.cnbc.com/2023/07/13/meta-threads-engagement-has-dropped-off-sensor-tower-similarweb.html):


> Last week, the text-based social media platform reported a record
> 100 million sign-ups in just five days, but according to data from
> Sensor Tower and Similarweb, the service has seen some dropoff in
> growth and engagement.
> “The Threads launch really did ‘break the internet,’ or at least
> the Sensor Tower models,” Anthony Bartolacci, managing director at
> Sensor Tower, a marketing intelligence firm, told CNBC. “In the
> 10-plus years Sensor Tower has been estimating app installs, the
> first 72 hours of Threads was truly in a class by itself.”
> But, he added, Sensor Tower data suggests a significant pullback
> in user engagement since Threads’ launch: On Tuesday and
> Wednesday, the platform’s number of daily active users were down
> about 20% from Saturday, and the time spent for user was down 50%,
> from 20 minutes to 10 minutes.


[I wrote earlier this week](https://daringfireball.net/2023/07/nobody_uses_threads_anymore) about the onslaught of “*turns out Threads is a bust*” news stories following in the wake of “*Threads launches as a sensational hit*” stories. One thing that’s struck me while following this is [just how many of these stories cite Sensor Tower data](https://duckduckgo.com/?q=threads+sensor+tower&iar=news&ia=news). But how much should we take Sensor Tower’s usage data at face value? Sensor Tower can only estimate these numbers, it can’t *know* them. They aren’t Apple or Google (the owners of the app stores through which Threads remains exclusively distributed, and mobile OSes that report back analytics data from all users who opt-in), nor do they have any access to Meta’s own copious data.


Here’s what Sensor Tower claims about their data collection, under “[Where our data comes from](https://sensortower.com/responsibly-sourced-data)”:


> Our data scientists and algorithms process and enrich trillions of
> aggregated data points contributed to us from millions of devices,
> to cultivate our one-of-a-kind data estate. They get this data
> from a statistical panel of consumers we have built to
> continuously learn from millions of people around the world. Our
> panelists provide us data as they use our popular
> privacy-compliant mobile apps. We employ best practices to ensure
> that our panelists understand what data they are providing us in
> exchange for the use of our apps.
> The team in our app studio publishes apps in several categories:
> Wellbeing [*sic*] apps aid in improving our users’ quality of life, such
> as ActionDash and StayFree
> Games provide entertainment and escape for users, such as
> Melodies Run [*sic*, sort of1]
> Advanced apps and browser plugins provide convenience, such as
> Friendly Streaming, Friendly Retail, Stayfocusd and Adblock Luna


So Sensor Tower’s information comes from analytics it collects from its own apps. They name these apps, but don’t link to them, so I will:

- ActionDash — [Exclusive to Android](https://play.google.com/store/apps/details?id=com.actiondash.playstore), ActionDash is described as a “screen time helper” that is “trusted globally by over 1 million users to break their phone addiction”. The developer is listed as “ActionDash”, not Sensor Tower, but the [app’s website](https://actiondash.com) says “Copyright © 2020 Sensor Tower, Inc” in the footer. As a screen-time monitor, you can see how this app would, by definition, provide Sensor Tower with information about everything a user does on their phone.
- StayFree — Another “screen time tracker”, available for both [Android](https://play.google.com/store/apps/details?id=com.burockgames.timeclocker) and [iOS](https://apps.apple.com/us/app/stayfree-web-stay-focused/id1631132311). The Android description:

StayFree - Screen Time & Limit App Usage is a self control, productivity and phone addiction controller app that allows you to show how much time you spend on your smartphone and helps you focus by restricting the usage of apps. You can set usage limits for your apps and receive alerts when exceeding those usage limits.

The iOS description:

StayFree - Web Analytics & Screen Time Tracker is an analytics, self control, productivity, and web addiction controller extension. This app works with the Safari web browser on your iOS device. StayFree provides analytics to help you understand how you are using the internet (daily website usage statistics) and focus your time by restricting the usage of distracting websites.

That’s a very different description. But the latest iOS release, version 2.2, claims:

We are introducing usage monitoring for applications in addition to websites! This marks the first stage of the feature, which is currently in beta. Although it may initially be somewhat sluggish and prone to errors, we anticipate ongoing improvements in future updates.

StayFree observes your Safari usage through an extension that prompts for permission to observe every single website you visit. [Here’s the alert I OK’d to permit this](https://daringfireball.net/misc/2023/08/stayfree-safari-permission-confirmation.jpeg). It monitors your app usage by asking for access to your Screen Time. I installed StayFree last week and, in the name of science, granted it access to both my web browsing and Screen Time. (I plan to delete it as soon as I publish this story.) I have found it to be exactly as described: very slow and prone to errors. What it does report can be viewed faster and with a better presentation in the Screen Time section of Settings. The StayFree Safari extension keeps many web pages from even loading for me.
- [Melody Run](https://melodiesrun.apppage.net/) — An infinite runner game, where you slide the hero left/right to hit squares, and each square you hit plays the note from a song. You score gems that can be cashed in to unlock new songs, and you can collect hundreds of gems at a time by watching video ads, which seem to all be for other games. It strikes me as neither fun nor challenging but it is a real game, and there’s apparently a level editor you can unlock if you play more than I was willing to. The game seems identical on both [iOS](https://apps.apple.com/us/app/melodies-run/id1599540626) and [Android](https://play.google.com/store/apps/details?id=com.creativetechnology.melodies3d&hl=en&gl=us), but only the iOS app asks whether you agree to let the game track you while using other apps. Even with tracking permitted, though, I fail to see how this game is able to collect the sort of detailed usage data Sensor Tower reports, except for your usage of other apps that embed the same tracking frameworks. There’s no way, for example, that playing Melody Run would allow Sensor Tower to gain any information about Threads. Not how long you use it, not how often you launch it, not even whether you have it installed. That’s the whole point of [sandboxing](https://support.apple.com/guide/security/security-of-runtime-process-sec15bfe098e/web).
- Friendly — Sensor Tower mentions apps named Friendly Streaming and Friendly Retail. I can’t find any apps with those exact names, but I believe they’re referring to a small suite of apps from [a company called Friendly](https://friendly.io), which publishes apps for [iOS](https://itunes.apple.com/app/apple-store/id400169658?pt=2051617&ct=friendly.io&mt=8), [MacOS](https://itunes.apple.com/us/app/friendly-streaming/id553245401?mt=12), and [Android](https://play.google.com/store/apps/dev?id=7399185471421849469). [Friendly’s privacy policy](https://friendly.io/insights/privacy/) declares that they’re “an affiliate of Sensor Tower Inc.” Friendly Social Browser is a web browser with built-in bookmarks for sites like Facebook, Twitter, and Instagram. Friendly Streaming Browser is a Mac app that’s just a web browser with built-in bookmarks for YouTube and major streaming sites. (Somehow Friendly Streaming Browser was deemed by Apple worthy of [this App Store feature story](https://apps.apple.com/us/story/id1655204439).) [Friendly Shopping Browser](https://apps.apple.com/us/app/friendly-shopping-browser/id6443906359) is, you guessed it, a web browser with built-in bookmarks for shopping sites like Amazon, Walmart, Costco, and Target. [Friendly Shopping Insights](https://apps.apple.com/us/app/friendly-shopping-insights/id6444090373) is an app dedicated to Amazon — you log in with your Amazon credentials and it shows you your spending history and habits. Basically it’s an app that, I think, lets Sensor Tower see everything you buy or look at in Amazon, along with your purchase history. I say “I think” because I didn’t actually log into my Amazon account after installing it. Why anyone would ever use any of these apps I have no idea.
- [StayFocused](https://www.stayfocusd.com/) — “a productivity extension for Google Chrome that helps you stay focused on work by restricting the amount of time you can spend on time-wasting websites.”
- [Adblock Luna](https://adblockluna.com/) — Adblock Luna is a VPN promoted specifically for ad blocking. When a VPN is installed and active, all network traffic is tunneled through the VPN. Your VPN provider can see (and thus track) *everything* you do on the internet, whether it’s through a browser (including private/incognito tabs) or an app. Sensor Tower claims “more than 15 million users have already installed Luna”. These users are an incredibly rich source of information for Sensor Tower.
Adblock Luna [is in Google’s Play Store](https://play.google.com/store/apps/details?id=com.sensortower.luna), but when you tap the “Install for Android” button on the Luna website, instead of linking to the Play Store, they instead [show this popover](https://daringfireball.net/misc/2023/08/adblock-luna-android-install.png) instructing you to (1) enable the Android setting to allow apps to be installed from unknown sources (a.k.a. sideloading); then (2) install the .apk app bundle that was just downloaded to your device. I don’t know why they steer users to sideloading rather than the version of Adblock Luna in the Play Store, but to me that’s a red flag.
Adblock Luna is not in Apple’s App Store. For iOS devices, they direct you to [this page](https://adblockluna.com/install). First, they require you type the year you were born to “prove” you’re over 18. Then you download a VPN profile and they walk you through the steps in Settings to enable their root trust certificate. It’s obvious why this isn’t in the App Store. This is about as close as you can get to installing third-party system software on iOS.


---


So, I see three ways Sensor Tower collects usage information for apps and websites that aren’t their own: (1) ad-blocking web browser extensions, (2) screen-time monitoring apps for Android and iOS, which on iOS requires access to Screen Time, and (3) the Adblock Luna VPN. (Perhaps I’m underestimating how much data they can collect from users who play Melody Run.)


These apps may well be popular — again, they claim that Adblock Luna has been installed by over 15 million users — but is the data they collect from them representative of the general public? ActionDash and StayFree are advertised for people who are looking to “break their phone addiction”. Data collected from these apps might be accurate for those users, but are users who self-identify as having an “addiction” to their devices representative of typical users? This seems a bit like trying to glean beverage consumption statistics by polling self-professed alcoholics — neither those actively struggling with an addiction, nor those who are successfully managing one, strike me as likely to be representative of the general public.


The user base for these apps must be comprised largely of technically naive, uninformed users. (Also: cheapskates, given that Sensor Tower’s tools are free of charge. Quite literally, their users are their product.) Both iOS and Android have built-in screen-time monitoring features, [Screen Time](https://support.apple.com/en-us/HT208982) on iOS, [Digital Wellbeing](https://support.google.com/android/answer/9346420?hl=en) on Android. Both allow you to track usage and set limits. If there’s a single advantage to installing ActionDash or StayFree instead of using the built-in system features, I don’t know what it is. Ad blocking, of course, is very popular, but using a VPN for ad blocking, instead of a web browser extension, is like using a chainsaw to remove the kernels from a cob of corn — not just overkill but dangerous. There’s a reason why it’s not in the iOS App Store, and why Sensor Tower steers Android users to a self-hosted version that’s not in the Play Store.


The vast majority of the public would never even think to install a third-party screen-time monitor. And by most estimates, only [40 percent of people use ad blockers](https://duckduckgo.com/?q=what+percentage+of+people+use+ad+blockers). Anyone looking for screen-time monitoring and controls should use the built-in features on their device. I find it hard to believe that anyone who truly understands the nature of a VPN, when looking for an ad-blocking tool, would choose to use a free VPN from a data analytics company. But those are the people whose internet usage Sensor Tower tracks, and thus the people whom the mainstream news media blindly cites, by way of Sensor Tower’s pronouncements,2 as representative of the world at large.


The installation instructions for Adblock Luna are surely scary to non-technical laypeople, and they’re downright terrifying to anyone expert enough to understand how VPNs work. So who is left? The ignorant but brazen. Perhaps such people’s web and app usage really is representative of the public at large. But there’s no way to know. We can judge the accuracy of, say, political pollsters by comparing their data to the actual results of elections. There’s no such reckoning for the usage data published by Sensor Tower and their ilk. It’s all unverifiable, but never reported as such. The news media so badly wants to know usage data that they just accept Sensor Tower’s and other such firms’ pronouncements at face value, without ever describing — let alone questioning — how they ostensibly know what they claim to know about very private data.3


Color me dubious.


---

1. There’s a 2-star review in the Play Store that starts, “I rated 2 cause of this: you changed your name to melody run when its supposed to be melodies run. I can’t get to the level editor!” So I guess that explains why Sensor Tower’s website claims the game’s name is “Melodies Run” — that actually [used to be the name](https://melodiesrun.apppage.net/). And at least one user is upset about the name changing to Melody Run. ↩︎
2. There are other companies in the same racket as Sensor Tower. The next-most-frequently cited, at least in my reading, is Similarweb. [Similarweb’s own description of how they source their data](https://www.similarweb.com/corp/ourdata/) is far more opaque than Sensor Tower’s, and thus strikes me as even more dubious. ↩︎︎
3. Here’s a thought exercise. Imagine if Apple and Google issued weekly reports revealing how many people used, say, the most popular 1,000 apps in their respective App Stores, along with how much time, on average, they spent using them. That would be data that could fairly be assumed to be accurate. But would not the major news media — publications such as The New York Times, that generally [report on “Big Tech” in an unflattering light](https://www.nytimes.com/search?query=big+tech) — object to such reporting as a violation of users’ collective privacy? As further proof that these companies know too much about us? But yet they echo the same information, when reported by Sensor Tower and Similarweb, without batting an eye or ever raising a question as to how this very private data is collected. ↩︎︎



| **Previous:** | [Oh to Be a Fly on the Wall During the Conversation Where Elon Musk Asks Tim Cook to Help X Corp Replace iOS as the Bedrock Everything Platform](https://daringfireball.net/2023/08/fly_on_the_wall_musk_cook) |
| **Next:** | [Was Trump Using Twitter Direct Messages? (Please Let the Answer Be Yes.)](https://daringfireball.net/2023/08/trump_dms) |


PreviousNext