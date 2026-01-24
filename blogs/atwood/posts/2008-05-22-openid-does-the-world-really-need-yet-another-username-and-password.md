---
title: "OpenID: Does The World Really Need Yet Another Username and Password?"
date: 2008-05-22
url: https://blog.codinghorror.com/openid-does-the-world-really-need-yet-another-username-and-password/
slug: openid-does-the-world-really-need-yet-another-username-and-password
word_count: 1741
---

As we continue to work on the code that will eventually become stackoverflow, we belatedly realized that **we’d be contributing to the glut of username and passwords on the web**. I have fifty online logins, and I can’t remember [any of them!](https://blog.codinghorror.com/the-login-explosion/) Adding that fifty-first set of stackoverflow.com credentials is unlikely to help matters.


With some urging from my friend [Jon Galloway](http://weblogs.asp.net/jgalloway/), I decided to take a look at [OpenID](http://en.wikipedia.org/wiki/OpenID). OpenID aims to [solve the login explosion problem](http://openid.net/what/):


> OpenID eliminates the need for multiple usernames across different websites, simplifying your online experience.
> You get to choose the OpenID Provider that best meets your needs and most importantly that you trust. At the same time, your OpenID can stay with you, no matter which Provider you move to. And best of all, the OpenID technology is not proprietary and is completely free.


In the spirit of [Show, Don’t Tell](https://blog.codinghorror.com/show-dont-tell/), here’s how it works:


Let’s say you’re visiting a new website for the first time. As you browse around, eventually you’ll do something that requires more than anonymous guest access. So you’ll get shunted to the “create a new account” page, in whatever form that takes. I’m sure everyone reading this knows the drill. But if the website is OpenID enabled, you *don’t* have to go through all the typical rigamarole necessary to create a new account. Instead, you can **enter your OpenID login**:


![](https://blog.codinghorror.com/content/images/2025/04/image-126.png)


I’m going to indulge in a bit of hand waving here and assume that you already have an OpenID login. It’s not such a terrible stretch, honestly; every AOL and Yahoo user already has an OpenID login even if they don’t know it yet.


OpenIDs are technically URLs. Here are a few examples:

- http://claimid.com/yourname
- http://yourname.signon.com
- https://me.yahoo.com/yourname


That’s one usability problem with OpenID: you have to remember a relatively complete personal URL that no two OpenID providers define the same way. Which compares unfavorably to, say, remembering your email address. There are shortcuts around this that I’ll describe later, but for now, there’s ID selector, which provides a reasonably friendly UI for building an OpenID login URL.


![](https://blog.codinghorror.com/content/images/2025/04/image-125.png)


If you enter the right URL, you’ll get redirected back to your OpenID provider, where you’ll enter your single set of login credentials.


![](https://blog.codinghorror.com/content/images/2025/04/image-124.png)


You’ll be prompted to add this site to your provider’s list of “trusted sites” for your account. Once you do this, you can bypass all of these steps the next time you’re on the site.


![](https://blog.codinghorror.com/content/images/2025/04/image-123.png)


And, finally, you’re logged in for the first time!


![](https://blog.codinghorror.com/content/images/2025/04/image-122.png)


If that seems like extra work – and remember, I’m not counting the time it took to set up the initial account at ClaimID, either – well, I won’t lie to you. It is more work. But it’s worth noting that:

1. The cost of account creation at your OpenID provider can eventually be **amortized across dozens of sites which will all accept those same credentials**.
2. After the first OpenID login at a particular site, assuming you’ve added that site to your trust list, **subsequent logins are literally one-click operations**.


It’s not exactly frictionless, but it’s a heck of an improvement over having to remember 50 different usernames and passwords for 50 different websites, wouldn’t you say? I think it compares quite favorably with the current champion of frictionless communication: anonymous comment boxes. They typically have three fields to fill out: username, URL, and email. OpenID requires only *one*. Your provider can proxy your URL and email back to the blog automatically from your provider profile, if you choose a smart provider with [attribute exchange](http://blogs.gnome.org/jamesh/2007/11/26/openid-ax/) support.


Which brings me to the other problem with OpenID. **The quality of your OpenID experience is heavily influenced by the provider you choose**. For example, Yahoo! is smart enough to work even if you enter nothing but “yahoo.com” as your OpenID URL. That is, assuming you’ve enabled OpenID support for your Yahoo! login. Providers can also offer unique functionality that sets them apart, too. For example, SignOn.com allows the use of Information Cards in Windows, so you can log into a website without ever typing in a password! It’s a bit of work, as you have to associate the Information Card with your provider account first, but I tried it, and it works as advertised.


My experiments with OpenID were quite positive, but all is not wine and roses in the land of OpenID. Stefan Brands identifies some [potentially large problems with OpenID](https://web.archive.org/web/20080701054638/http://idcorner.org/2007/08/22/the-problems-with-openid/), backed by exhaustive references:

1. **Phishing**. A malicious site could visit the OpenID provider URL you gave it, screen-scrape your login form, and present it locally, intercepting your login and password. However, if you choose a quality OpenID provider, they’ll use SSL and a high-grade certificate so you’ll have some confidence you’re not being fooled. Yahoo also offers [anti-phishing image watermarks](https://web.archive.org/web/20080703163539/http://security.yahoo.com/article.html?aid=2006102507) for OpenID logins, as well.
2. **Privacy**. Your OpenID provider will know, by definition, every site you log into using its credentials. So I hope you trust your provider.
3. **Centralized Risk**. If your OpenID account is compromised, every site you used to access it is also compromised. I’m not sure how much riskier this is than having your email credentials compromised, as many (most?) sites allow you to send a password reset to your email address.
4. **Lack of Trust**. The OpenID providers provide no identity checking whatsoever. It’s sort of like those generic “identity cards” you can obtain online, which are pretty useless next to, say, your Driver’s License, which was issued by a local governmental authority. What if Fake Steve Jobs created a fake OpenID purporting to be Steve Jobs, or a fake OpenID provider?
5. **Additional Complexity**. Your login now involves two completely different entities: the website you’re attempting to gain access to, *and* your OpenID provider. You have to understand this new relationship to troubleshoot any problems with your login – and the OpenID provider has to be up and running for you to log in at all.
6. **Adoption Inequality**. It’s easy for AOL, Yahoo!, Six Apart, and Technorati to become OpenID *providers* – but what good does that do you when there are very few OpenID *consumers*? As Dare points out, there are no financial incentives to [accept credentials from your competitors](http://www.25hoursaday.com/weblog/2007/08/13/AProposalForSocialNetworkInteroperabilityViaOpenID.aspx), but there are certainly plenty of incentives for driving account creation on your own site. For now, I expect OpenID to be driven primarily by small applications and sites that don’t have millions of dollars of skin in the game.


As I mentioned above, I feel most of these criticisms can be mitigated by picking a quality, trustworthy OpenID Provider. Particularly one that uses SSL. Since it’s an open ecosystem, I’d hope the more reputable and reliable OpenID providers would rise to the top. And consider the advantages: as an application developer, you **no longer have to store passwords!** That’s a *huge* advantage, because [storing passwords](https://blog.codinghorror.com/youre-probably-storing-passwords-incorrectly/) is the last business you want to be in. Trust me on this one.


I also found Jan Miksovsky’s [criticisms of the user experience](http://miksovsky.blogs.com/flowstate/2007/08/openid-great-id.html) of OpenID – as of 6 months ago – fairly damning:


> And all this is for – what, exactly? To save me from having to pick a user name and password? As annoying as that can be, it’s just not that hard! Remembering an arbitrary user name does cause real trouble, but simply allowing email addresses to be used as IDs can solve almost all of that problem. As more and more sites allow email addresses as IDs, the need for OpenID becomes less compelling to a consumer.
> For the time being, I can’t imagine a sane business operator forcing their precious visitors through this gauntlet of user experience issues just for the marginal benefits that accrue to a shared form of ID. I’ve read numerous claims that all it will take is for someone big like Google to support OpenID to crack this problem open. Unfortunately, there’s no business of any size that can afford to direct their traffic down a dead end.
> Most service operators will, at best, offer users a choice between using a proprietary ID or an OpenID, creating a terrible economic proposition for a consumer. Faced with the proposition of: 1) struggling once for thirty minutes to struggle through a process they can barely understand, or 2) spending two minutes on every new site breezing through a familiar process they’ve done countless times before, **normal busy people will choose the familiar route time and time again.** I’ll bet anything that most people will keep going for proprietary IDs, further deferring the network effects possible from OpenID adoption.


Perhaps the most compelling point Jan makes is this one: it *is* a bit odd to ask users to associate themselves with an arbitrary URL instead of an email address. I definitely saw some rough edges in today’s experimentation, but I’d say the user experience has improved since Jan looked at OpenID. That’s encouraging.


I realize that OpenID is far from an ideal solution. But right now, the one-login-per-website problem is so bad that I am willing to accept these tradeoffs for a partial [worse is better](https://blog.codinghorror.com/is-worse-really-better/) solution. There’s absolutely no way I’d put my banking credentials behind an OpenID. But there are also dozens of sites that I don’t need anything remotely approaching banking-grade security for, and I use these sites far more often than my bank. The collective pain of remembering all these logins – and the way my email inbox becomes a de-facto collecting point and security gateway for all of them – is substantial.


If you’re a software developer building an application that requires user accounts, please consider using OpenID rather than polluting the world with yet another login and password. I also encourage you to [experiment with OpenID](http://openid.net/) as a user. Create one. Try logging in somewhere with one. If you don’t like the experience, or if you agree with one (or more) of the criticisms I listed above, **how can we collectively fix it?** We desperately need a solution to the login explosion, and right now the only thing I’ve seen on the horizon that has any kind of critical mass whatsoever is OpenID.


If we can’t **make OpenID work, at least for run of the mill, low-value credentials that litter the web in increasing numbers** – what hope do we have of ever fixing the login explosion problem?

[authentication](https://blog.codinghorror.com/tag/authentication/)
[oauth](https://blog.codinghorror.com/tag/oauth/)
[openid](https://blog.codinghorror.com/tag/openid/)
[security](https://blog.codinghorror.com/tag/security/)
[user experience](https://blog.codinghorror.com/tag/user-experience/)
