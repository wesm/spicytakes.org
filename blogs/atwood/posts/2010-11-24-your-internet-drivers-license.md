---
title: "Your Internet Driver’s License"
date: 2010-11-24
url: https://blog.codinghorror.com/your-internet-drivers-license/
slug: your-internet-drivers-license
word_count: 815
---

Back in summer 2008 when we were building Stack Overflow, I chose OpenID logins for reasons documented in [Does The World Really Need Yet Another Username and Password](https://blog.codinghorror.com/openid-does-the-world-really-need-yet-another-username-and-password/):


> I realize that OpenID is far from an ideal solution. But right now, the one-login-per-website problem is so bad that I am willing to accept these tradeoffs for a partial [worse is better](https://blog.codinghorror.com/is-worse-really-better/) solution. There’s absolutely no way I’d put my banking credentials behind an OpenID. But there are also dozens of sites that I don’t need anything remotely approaching banking-grade security for, and I use these sites far more often than my bank. The collective pain of [remembering all these logins](https://blog.codinghorror.com/the-login-explosion/) – and the way my email inbox becomes a de-facto collecting point and [security gateway](https://blog.codinghorror.com/please-give-us-your-email-password/) for all of them – is substantial.


It always pained me greatly that **every rinky-dink website on the entire internet demanded that I create a special username and password *just for them***. Yes, if you’re an alpha geek, then you probably use a combination of special software and USB key from your [utility belt](https://blog.codinghorror.com/whats-on-your-utility-belt/) to generate secure usernames and passwords for the dozens of websites you frequent. But for the vast, silent majority of normals, who know nothing of security but desire convenience above all, this means one thing: *using the same username and password over and over*. And it’s [probably a simple password](https://blog.codinghorror.com/dictionary-attacks-101/), too.


This is the status quo of identity on the internet. It is deeply and fundamentally broken.


But it doesn’t have to be this way. If you [open your wallet](https://blog.codinghorror.com/optimizing-your-wallet/) (or purse, or man-purse, or whatever), I bet you’ll find a variety of credentials you use to prove your identity wherever you go.


![](https://blog.codinghorror.com/content/images/2025/04/image-501.png)


The average wallet contains a few different forms of identity with varying strengths:

- Strong: California driver’s license, student ID
- Moderate: credit cards, health insurance card, video rental membership, gym card
- Weak: Albertson’s Preferred Card, Best Buy Rewards Zone Card, Coffee loyalty card


(and sometimes even, uh, cards for free lap dances, apparently)


**In the real world, we don’t regularly hold two dozen forms of identity like we expect people to on the web.** Not only would you be carrying around the [freaking Constanza wallet](https://web.archive.org/web/20110620072713/http://www.seinology.com/scripts/script-168.shtml) at that point, it would be *insane*. In the real world, we somehow manage to get by with about two or three strong forms of identity, complemented by a few other weaker forms to taste.


I’m proposing that our web wallets begin to mimic our physical wallets. **Whenever a website needs to know who I am, they should ask to see my Internet Driver’s License.**


![](https://blog.codinghorror.com/content/images/2025/04/image-500.png)


Now, I don’t *literally* mean a driver’s license. I’m using this term figuratively to mean online credentials that I can re-use in more than one place on the internet. If all I want to do is leave a comment on a blog – like, say, [*this one*](https://blog.codinghorror.com/welcome-back-comments/) – then one of the weaker forms of identity will surely do. If I’m starting a new bank account, or setting up a profile on a dating website, then maybe a stronger credential from my virtual wallet is necessary.


The core concept that users need to get used to is **logging in to a website by showing a third party credential** to validate their identity. This idea isn’t nearly as crazy as it seemed in 2008. How many websites can you log into by showing your Facebook, Google, or Twitter credentials now? *Lots!*


![](https://blog.codinghorror.com/content/images/2025/04/image-499.png)


The whole online identity situation may seem as impossible as peace in the Middle East at this point. But when faced with a problem that appears intractable, is your solution to throw your hands up, mindlessly embrace the status quo, and wearily sigh “*whaddaya gonna do?”*


Some people do that. It’s their right. Personally, I prefer to **be the change I want to see**. So for us, on Stack Overflow and the [Stack Exchange network](http://stackexchange.com/), that means *aggressively promoting the concept of the Internet Driver’s License*. Including educating users as necessary.


For example, consider this ATM machine. To use it, **do I need to sign up for an account at Shanghai Peking Development Bank?** No. I can use any form of trusted third-party credentials the machine supports.


![](https://blog.codinghorror.com/content/images/2025/04/image-498.png)


Similarly, to log into any Stack Exchange site, including Stack Overflow, **present any OpenID or OAuth 2.0 compliant identity provider as your Internet Driver’s License.**


![](https://blog.codinghorror.com/content/images/2025/04/image-497.png)


When we founded Stack Overflow, we set out with the explicit mission to make the internet better. Adding yet another meaningless username and password to the fabric of the web does not make it better. **What *does* make the internet better is continued pursuit of better, simpler, re-usable forms of third party online identity.**


That’s why I urge you to join me in supporting [OpenID](http://openid.net/), [OAuth 2.0](https://oauth.net/2/), and any other promising implementations of the Internet Driver’s License.

[authentication](https://blog.codinghorror.com/tag/authentication/)
[user experience](https://blog.codinghorror.com/tag/user-experience/)
[openid](https://blog.codinghorror.com/tag/openid/)
[security](https://blog.codinghorror.com/tag/security/)
[login](https://blog.codinghorror.com/tag/login/)
