---
title: "Cutting the Gordian Knot of Web Identity"
date: 2011-09-06
url: https://blog.codinghorror.com/cutting-the-gordian-knot-of-web-identity/
slug: cutting-the-gordian-knot-of-web-identity
word_count: 1337
---

Perhaps you’ve seen [this recent XKCD](http://xkcd.com/936/) about password choice?


![](https://blog.codinghorror.com/content/images/2025/04/image-546.png)


It prompted a spirited debate – even on our very own [Security Stack Exchange](http://security.stackexchange.com/questions/6095/xkcd-936-short-complex-password-or-long-dictionary-passphrase) – about the merits of the argument presented there. Now, to be clear, I’m *completely* on Randall’s side here; I’m all for passphrases over passwords, and [I have been](https://blog.codinghorror.com/passwords-vs-pass-phrases/) for [years](https://blog.codinghorror.com/passphrase-evangelism/).


But this is merely **one symptom of a much larger disease: identity on the internet**. Every time you touch a website that actually cares who the heck you are – and this is an increasingly large list of sites as the web matures – you have to, *sigh*, “log in.” And logging in inevitably requires you to create a username and a password. Over and over and over and *over*. And, oh by the way, you’ll be logging in again each and every time on every browser and every computer and every device you own. It’s a *great* system. And by “great” I mean fracking terrible.


This isn’t just tedious busywork for us, the poor web users, it’s also downright *dangerous* as I explained in [The Dirty Truth About Web Passwords](https://blog.codinghorror.com/the-dirty-truth-about-web-passwords/). It’s a near-impossible problem, an intractable [Gordian Knot](http://en.wikipedia.org/wiki/Gordian_Knot). So I’m going to answer one comic [with another.](http://en.wikiquote.org/wiki/Watchmen#Adrian_Veidt.2FOzymandias)


![](https://blog.codinghorror.com/content/images/2025/04/image-545.png)


The problem is not choosing *better* passwords for the dozens or hundreds of web sites we have to log in. The problem is *passwords*.


Thus, the only real cure to the disease of identity on the web is to ***get rid of passwords altogether***.


Yes, you read that correctly. But “Jeff,” you might say, “how can we *possibly* log in to websites without our beloved, mile-long list of site-specific usernames and passwords?” I’m so glad you asked! Try to make time in your busy schedule of account and password creation to read a few more paragraphs into this post and I’ll attempt to explain my crazy scheme.


We could use [our internet driver’s license](https://blog.codinghorror.com/your-internet-drivers-license/) and log in to a particular website using our existing Google, Facebook, Twitter, or OpenID credentials. This works, but it assumes a lot; is the website *enlightened* enough to accept third party logins, or is there a political agenda (or delusions of grandeur) preventing them from recognizing any form of identity other than *their own*? To be fair, accepting third party identity is *hard* and undeniably adds complexity. There are a million ways to get it wrong, and only a handful of sites that get it right. I like to think [Stack Exchange](http://stackexchange.com/sites) is one of the websites that gets this right, but I’ll fully acknowledge that it is challenging to get there. Unfortunately, the path of least resistance for web identity leads inexorably to one sad, depressing, dysfunctional place:


![](https://blog.codinghorror.com/content/images/2025/04/image-544.png)


Yep. Get used to it. Username. Password. For every single website you’ll ever visit. On every single device you’ll ever own. Forever. Until the end of time. *Oh God.*


Lately I’ve begun to hope there might be a viable solution, even outside the third-party logins I’ve championed for the last 3 years. A way of absolving users of username and password selection. Like Alexander’s solution to the Gordian Knot, it might be a bit scary in its… absolutism. But anything has to be better than the unspeakable terror of a million logins on a million different websites on a million different devices. Right? *Right?*

kg-card-begin: html

(Warning, Extreme Hand Waviness Ahead: while I *do* honestly believe the techniques described below would work, I am glossing over many of the technical implementation details. This is absolutely *not* intended to be a spec but an “I Have a Dream” outline. Feel free to help me clarify and expand on the necessary details by blogging a more technical plan for this in any form you like.)

kg-card-end: html

Imagine, if you will, visiting a new website and deciding you’d like to create an account there. You click the “Create New Account” link and then…

- The website presents a secure account creation page decorated with specific `meta` tags that indicate this page supports automated account creation with a standard(ish) set of user info HTML form fields.
- The browser, seeing these `meta` tags in the page, *does not present the page to the user* but retrieves the user’s standard information fields like name, email address, etcetera from some form of secure https cloud storage, and readies them. The browser will also **automatically select a completely random, cryptographically secure password for the new account**.
- The browser must, unfortunately, prompt the user with a confirm dialog containing a CAPTCHA at this point to ensure that the signup process isn’t being scripted in any way, and that a real human being actually wants to create an account on this website. While we’re there, we might as well confirm the identity data we’re about to send to the website (though hopefully the defaults should suffice). Once confirmed, the user credentials and password will be sent to the site and stored securely in the cloud.
- The website redirects the newly created account to an appropriate page.


There may be some more information that the browser (or the site) needs to ask the user for in there somewhere. But account creation is a one-time event, and in the typical case where you’re signing up for some simple website, your preferred defaults should suffice. Caveats aside, look what we have wrought: **you clicked “Create New Account,” completed a single captcha and clicked OK** – now you’re logged in to your brand new account on any website.


Once you *have* an account, it’s even simpler. Imagine clicking the “Sign In” link, and then…

- The website presents a secure login page decorated with specific `meta` tags that indicate this page supports automated login with a standard set of username and password HTML form fields.
- The browser, seeing these `meta` tags in the page, *does not present the page to the user* but retrieves the user’s credentials from some form of secure https cloud storage, and sends them to the site.
- The site receives the credentials via https, validates them, and returns a valid login cookie to the browser.
- The browser redirects the now logged-in user to the page they originally wanted to see as a logged in user.


From the perspective of this weary citizen of the web, at least, a miracle just happened. **You clicked “Sign In,” and you’re *immediately* signed in** without having to look at a *single* stinking username and password field!


Seems like magic, yes? Gotta be a catch, yes? Well, there is. Two catches, to be precise.

1. **Web browsers will have to be rewritten to understand basic identity protocols.** I suppose it *could* be a browser plugin as well, but I’d rest a lot easier knowing basic identity protocols are officially “baked in” to the browser and supported by the Powers That Be, perhaps even as accepted W3C standards. And yes, you will need to log in to your browser at a minimum.
2. **You have to trust “The Cloud” at least a little**. There has to be some trusted, secure location on the internet for all your usernames, passwords, and basic identity information to reside. Otherwise this scheme can’t possibly work, because how would you log in from your (insert favorite device name here) if it has no access to the secret, hidden list of account information and automagically generated secure passwords created on your behalf?


Identity is fundamental to the modern internet; more and more websites need to know something about *who you are* to work. The current status quo of thousands of websites with thousands of differing ideas about identity and passwords and account information is beyond broken. We want – no, we *demand* – that the browser understand and standardize identity the same way it does HTML and CSS. Maybe it’s crazy, but **I dream of the day when I never need to see another password field in my browser ever again**.


I hope you can too.

[security](https://blog.codinghorror.com/tag/security/)
[web identity](https://blog.codinghorror.com/tag/web-identity/)
[user experience](https://blog.codinghorror.com/tag/user-experience/)
[authentication](https://blog.codinghorror.com/tag/authentication/)
[passwords](https://blog.codinghorror.com/tag/passwords/)
