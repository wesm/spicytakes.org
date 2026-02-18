---
title: "Twitter’s Shit Sandwich"
date: 2011-05-18
url: https://daringfireball.net/2011/05/twitter_shit_sandwich
slug: twitter_shit_sandwich
word_count: 1150
---


[Twitter today announced](http://blog.twitter.com/2011/05/mission-permission.html) new finer-grained control over third-party API access to direct messages:


> Beginning today, we’re giving you more control over what
> information you share with third-party applications. Apps that you
> use to access your direct messages will ask for your permission
> again. By the end of the month, applications that do not need
> access to your direct messages will no longer have it, and you can
> continue to use these apps as usual.


That’s good news on the surface — it means you can use services and apps that require your Twitter credentials without granting those services/apps access to your private direct messages. For services/apps that are entirely public, this makes sense.


But there’s a big shit sandwich attached: Twitter is implementing this change by requiring *all* third-party clients that want or need access to direct messages to use the cumbersome OAuth login flow for authentication. [Here’s the developer-level announcement on the Twitter API Announcement group](http://groups.google.com/group/twitter-api-announce/browse_thread/thread/e954fc0f8b5aa6ec).


OAuth is complicated and hard to summarize, but in a nut, Twitter currently offers third-party developers two ways to do authentication, [OAuth](http://en.wikipedia.org/wiki/OAuth) and [xAuth](http://dev.twitter.com/pages/xauth). xAuth allows the developer to simply ask the user for their Twitter username and password. If you use any of the popular third-party Twitter clients for the Mac or iOS — Twitterrific, Tweetbot, Hibari, etc. — you’ve seen xAuth in action. You launch the app, the app shows you a dialog box with fields for your Twitter username and password, you enter them, and then you’re in. Behind the scenes, the apps using xAuth do not store your username and password. Instead, they use them once to authenticate with Twitter’s API, and in return they receive from Twitter a key granting that app authenticated access to your account. The app needs only to store that key.


With OAuth, on the other hand, authentication *must* take place through a web browser and a session on twitter.com. The app forwards you to a web page at Twitter, you sign in to your Twitter account on the twitter.com website, and then you’re prompted, by Twitter on their website, to grant permission to the app in question to access your account.


OAuth makes perfect sense for web-based services that seek access to your Twitter credentials. For example, consider “favorite” aggregators like [Favstar](http://favstar.fm/) and Jason Kottke’s excellent new [Stellar](http://stellar.io/). These services require authenticated access to your Twitter account. Thanks to OAuth, you never need to give these sites your Twitter password, let alone allow them to store your password. Instead, they forward you to twitter.com, you grant them access to your account there, and then twitter.com forwards you back to the website where you started. It’s common sense: a web-based authentication flow works naturally *from within a web browser*.


But the same web-based authentication flow is jarring for native apps. When you open a native app — Mac, Windows, iOS, Android, WebOS — you don’t expect to be forwarded out of the app and into your web browser. Developers can alleviate some of the context switching by using an embedded web view inside their native app for the OAuth authentication handshake, but at that point, why not just use xAuth and simply allow the user to enter their username and password in a native dialog box? So long as you remain within the app, there’s no security advantage for OAuth in an embedded web view over xAuth — but there’s a huge decrease in usability, simplicity, and clarity to the user.


I’m currently testing a review unit of HP’s new [Veer 4G](http://hp.com/veer), and for whatever reason, the WebOS Twitter clients I’ve tried and liked the best ([Bad Kitty](http://www.superinhuman.com/badkitty/) and [Carbon](http://carbonwebos.com/)) use OAuth, not xAuth, and account creation is a huge pain in the ass compared to any of the iOS apps I’ve used — all of which use xAuth for a simple “username/password in a dialog box” flow.


And OAuth is even worse for setting up multiple accounts in a native client (and good multiple account support is surely one of the leading reasons to use a native Twitter client instead of the twitter.com web site). Because then, not only do you need to go through the cumbersome OAuth login process for each additional account, but you must *first* sign out of the Twitter account you’re already signed into in the web browser. The twitter.com web interface is inherently single-account. To use a different Twitter account in the same web browser, you have to first sign out, then sign back in using the other account. With xAuth, to add an additional account you merely enter another username and password. With OAuth, you have to start by signing *out* of whatever account you previously signed into. You only have to do this when first creating each new account in the client app — the app can save the OAuth credentials for multiple accounts — but it’s still far more complicated and annoying than simply entering a username and password.


Full Twitter clients require access to DMs. Everyone using, say, Twitterrific and Tweetbot and TweetDeck, knows that these apps have access to their DMs *because they’re using these apps to read and write DMs*. This is very different from a web-based service like Favstar or Stellar, where you signed up to grant the service access to your Twitter favorites (which are public) and have no reason to grant the service access to your direct messages (which ought to be private). The whole point of native Twitter clients is that some users want the sort of experience that only native apps can provide. OAuth cannot be made to feel like a native experience, and account authentication is the very first thing you do when trying a new client.


With both xAuth and OAuth, you, the user, have control over each application and service to which you’ve granted any sort of access to your Twitter account. On twitter.com, go to [Settings: Applications](https://twitter.com/settings/applications) to see a list of all the apps with access to your account. I can’t think of any reason why Twitter would force native apps through OAuth other than to create a hurdle that steers users toward Twitter’s own official native clients. Because Twitter’s official clients [aren’t going to force users to jump through OAuth to authenticate](http://twitter.com/#!/rsarver/status/70917459078680577) — they’re still going to simply ask for your username and password in a simple native dialog box.


If you use a third-party Twitter client that currently uses xAuth, and Twitter does not reconsider this policy change, you’re not going to like it when they flip the switch that requires OAuth. If you don’t want to take my word for it that OAuth provides a crummy experience for users of native apps, [take it from Loren Brichter](http://blog.atebits.com/2009/02/fixing-oauth/) — back in 2009, when Tweetie was just another third-party Twitter client.



| **Previous:** | [Wolf!](https://daringfireball.net/2011/05/wolf) |
| **Next:** | [Measure Twice, Cut Once](https://daringfireball.net/2011/05/measure_twice) |


PreviousNext