---
title: "Please Give Us Your Email Password"
date: 2008-06-04
url: https://blog.codinghorror.com/please-give-us-your-email-password/
slug: please-give-us-your-email-password
word_count: 1168
---

A number of people whose opinions I greatly respect have turned me on to [Yelp](http://www.yelp.com/) over the last six months or so. Yelp is a community review site, and a great way to discover cool new places in whatever neighborhood you happen to be in.


I’ve enjoyed using Yelp, and I wanted to participate by submitting my first review, so I created a new account there. As part of the account creation process, I was presented with this.


![](https://blog.codinghorror.com/content/images/2025/04/image-137.png)


The idea is that I tell Yelp what email service I use, then provide my login and password information so Yelp can determine if any of my email contacts are Yelp members. How convenient!


Here’s how I see that page.


![](https://blog.codinghorror.com/content/images/2025/04/image-136.png)


I’m willing to give Yelp the benefit of the doubt here, but let’s think about what it means to give out your email account and password to *anyone*, no matter how ostensibly trustworthy they may be:

1. Number one with a bullet: **your email account is a de-facto master password for your online identity**. Most – if not all – of your online accounts are secured through your email. Remember all those “forgot password” and “forgot account” links? Guess where they ultimately resolve to? If someone controls your email account, they have nearly unlimited access to every online identity you own across every website you visit.
2. If you’re anything like me, **your email is a treasure trove of highly sensitive financial and personal information**. Consider all the email notifications you get in today’s highly interconnected web world. It’s like a one-stop-shop for comprehensive and systematic identity theft. How do I know Yelp isn’t going to dip into other areas of my email?
3. Even if I trust Yelp absolutely, **how do I know they’re not going to store my email password**, [perhaps insecurely](https://blog.codinghorror.com/youre-probably-storing-passwords-incorrectly/), in a place some disgruntled programmer or hacker can eventually get to it? Giving out your password puts the recipient in the highly unfortunate position of having to secure your password. Give that email password out enough, and you’re now vulnerable in *dozens* of places spread across the face of the web. The odds start to look [pretty dire](https://blog.codinghorror.com/a-question-of-programming-ethics/).


I’m sure Yelp means well. They just want to help me find my friends, doggone it! But the very nature of the request is *incredibly *offensive; **they have effectively asked for the keys to my house in order to riffle through my address book.**


I don’t think so.


Frankly, it’s irresponsible to even ask this question. Naïve internet users may not understand why it is such a profoundly bad idea to give out their email credentials to random websites. Worse, they might eventually get the idea that giving out their email credentials is typical or normal.


It’s not. This is outlined quite literally in most privacy policies:


> The security of your account also depends on keeping your account password confidential, and you should not share your account name or password with anyone. If you do share your account information with a third party, they will have access to your account and your personal information. – [Google Checkout](https://web.archive.org/web/20081023045010/https://checkout.google.com/files/privacy.html)
> If a password is used to help protect your accounts and personal information, it is your responsibility to keep your password confidential. Do not share this information with anyone. If you are sharing a computer with anyone you should always choose to log out before leaving a site or service to protect access to your information from subsequent users. – [Microsoft Passport](https://web.archive.org/web/20081216014954/http://privacy.microsoft.com/en-us/fullnotice.mspx)
> Your Yahoo! ID and password are confidential information. A Yahoo! employee will never ask you for your password in an unsolicited phone call or email. Do not respond to any message that asks for your password. – [Yahoo](https://web.archive.org/web/20081027144741/http://security.yahoo.com/article.html?aid=2006102510)


How did we end up in a world where it’s even remotely acceptable to ask for someone’s email credentials? What happened to all those years we spent establishing privacy policies to protect our users? What happened to the fundamental tenet of security common sense that says **giving out your password, under any circumstances, is a bad idea?**


I can understand the cutthroat desire to build monetizable “friend” networks by any means necessary. Even if it means encouraging your users to cough up their login credentials to competing websites. But how can I take your privacy policies seriously if you aren’t willing to treat your competitors’ login credentials with the very same respect that you treat your own? That’s just lip service.


Email is the de-facto master password for a huge swath of your online identity. Tread carefully:

- As a software developer, you should *never* ask a user for their email credentials. It’s unethical. It’s irresponsible. It is wrong. If someone is asking you to code this, why? For what purpose?
- As a user, you should *never* provide your email credentials to anyone except your email service. Sites that ask you for this information are to be regarded with extreme suspicion if not outright distrust.


Beyond those ethical guidelines, I do wonder why the technological solution to this problem has barely been addressed. If all Yelp wants is my address book, **why can’t I grant them temporary access to my public email address book *without* giving out the keys to my email kingdom?**


If even a fraction of the coding effort that regularly goes into convincing people to cough up their email or website login credentials went into finding other, more reasonable solutions to this problem – perhaps we could have arrived at a saner solution by now. And we can start by **taking obnoxious, utterly inappropriate credential requests completely off the table.**

kg-card-begin: html

UPDATE: Several commenters brought to light some efforts underway to address this pernicious problem:

kg-card-end: html
- [Google Contacts API](http://code.google.com/apis/contacts/) (related [documentation](http://code.google.com/apis/accounts/docs/AuthForWebApps.html))
- [Yahoo! Contact API](https://web.archive.org/web/20081204000502/http://developer.yahoo.com/addressbook/) (related [documentation](https://web.archive.org/web/20081202120041/http://developer.yahoo.com/auth/user.html))
- [Windows Live Contact API](https://web.archive.org/web/20081204020718/http://msdn.microsoft.com/en-us/library/bb463989.aspx) (as publicized in [Angus Logan’s blog](https://web.archive.org/web/20080609073334/http://blogs.msdn.com/angus%5Flogan/))


A more general solution may be [OAuth](http://oauth.net/), billed as an open standard for API access delegation. In other words, [a valet key for websites](http://oauth.net/about/):


> Many luxury cars today come with a valet key. It is a special key you give the parking attendant and unlike your regular key, will not allow the car to drive more than a mile or two. Some valet keys will not open the trunk, while others will block access to your onboard cell phone address book. Regardless of what restrictions the valet key imposes, the idea is very clever. You give someone limited access to your car with a special key, while using your regular key to unlock everything.


Chris Messina of the OAuth project was kind enough to provide a number of related links in the comments and [a follow up post](https://web.archive.org/web/20080608003246/http://blog.oauth.net/2008/06/05/an-opportunity-for-oauth-jeff-codinghorror-atwood-highlights-the-password-anti-pattern/) on the OAuth blog as well.


I was encouraged to learn about some of the recent progress we’ve made on this front. If you were looking for a way to be part of the solution, instead of the problem, read up on these solutions and participate!

[security](https://blog.codinghorror.com/tag/security/)
[email](https://blog.codinghorror.com/tag/email/)
[privacy](https://blog.codinghorror.com/tag/privacy/)
[user experience](https://blog.codinghorror.com/tag/user-experience/)
