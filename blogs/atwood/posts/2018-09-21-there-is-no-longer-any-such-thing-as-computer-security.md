---
title: "There is no longer any such thing as Computer Security"
date: 2018-09-21
url: https://blog.codinghorror.com/there-is-no-longer-any-such-thing-as-computer-security/
slug: there-is-no-longer-any-such-thing-as-computer-security
word_count: 1729
---

Remember “cybersecurity”?


![its-cybersecurity-yay](https://blog.codinghorror.com/content/images/2018/09/its-cybersecurity-yay.jpg)


Mysterious hooded computer guys doing mysterious hooded computer guy... things! Who knows what kind of naughty digital mischief they might be up to?


Unfortunately, we now live in a world where this kind of digital mischief is literally rewriting the world’s history. For proof of that, you need look no further than this single email that was sent March 19th, 2016.


![podesta-hack-email-text](https://blog.codinghorror.com/content/images/2018/09/podesta-hack-email-text.png)


If you don’t recognize what this is, it is a [phishing email](https://blog.codinghorror.com/phishing-the-forever-hack/).


![](https://blog.codinghorror.com/content/images/2025/02/image-31.png)


This is by now a very, very famous phishing email, arguably the most famous of all time. But let’s consider how this email even got sent to its target in the first place:

- An attacker slurped up lists of any public emails of 2008 political campaign staffers.
- One 2008 staffer was *also* hired for the 2016 political campaign.
- That particular staffer had non-public campaign emails in their address book, and one of them was a powerful key campaign member with an extensive email history.


On successful phish leads to an even wider address book attack net down the line. Once they gain access to a person’s inbox, they use it to prepare to their next attack. They’ll harvest existing email addresses, subject lines, content, and attachments to construct plausible looking boobytrapped emails and mail them to all of *their* contacts. How sophisticated and targeted to a particular person this effort is determines whether it’s so-called “spear” phishing or not.


![phishing-vs-spear-phishing](https://blog.codinghorror.com/content/images/2018/09/phishing-vs-spear-phishing.png)


In this case is it was not at all targeted. This is a remarkably unsophisticated, absolutely generic routine phishing attack. There is zero focused attack effort on display here. But note the target did *not* immediately click the link in the email!


![podesta-hack-email-link-1](https://blog.codinghorror.com/content/images/2018/09/podesta-hack-email-link-1.png)


Instead, he did exactly what you’d want a person to do in this scenario: **he emailed IT support and asked if this email was valid.** But IT made a [fatal mistake in their response](https://www.nytimes.com/2016/12/13/us/politics/russia-hack-election-dnc.html).


![podesta-it-support-response](https://blog.codinghorror.com/content/images/2018/09/podesta-it-support-response.png)


Do you see it? Here’s the kicker:


> Mr. Delavan, in an interview, said that his bad advice was a result of a typo: He knew this was a phishing attack, as the campaign was getting dozens of them. He said **he had meant to type that it was an “illegitimate” email, an error that he said has plagued him ever since.**


One word. He got *one* word wrong. But what a word to get wrong, and in the first sentence! The email did provide the proper Google address to reset your password. But the lede was already buried since the first sentence said “legitimate;” the phishing link in that email was then clicked. And the rest is literally history.


What’s even funnier (well, in the way of gallows humor, I guess) is that public stats were left enabled for that bit.ly tracking link, so you can see exactly what crazy domain that “Google login page” resolved to, and that it was clicked exactly twice, on the same day it was mailed.


![bitly-podesta-tracking-link](https://blog.codinghorror.com/content/images/2018/09/bitly-podesta-tracking-link.png)


As I said, these were not exactly sophisticated attackers. So yeah, in *theory* an attentive user could pay attention to the browser’s address bar and notice that after clicking the link, they arrived at


`http://myaccount.google.com-securitysettingpage.tk/security/signinoptions/password`


instead of


`https://myaccount.google.com/security`


Note that the phishing URL is carefully constructed so the most “correct” part is at the front, and weirdness is sandwiched in the middle. Unless you’re paying very close attention and your address bar is long enough to expose the full URL, it’s… tricky. See this 10 second video for a dramatic example.


(And if you think that one’s good, check out this one. Don’t forget all the Unicode look-alike trickery you can pull, too.)


I originally wrote this post as a presentation for the Berkeley Computer Science Club back in March, and at that time I gathered a list of public phishing pages I found on the web.


`nightlifesofl.comehizaza-limited.comtcgoogle.comappsgoogie.comsecurity-facabook.com`


Of those five examples from 6 months ago, one is completely gone, one loads just fine, and three present an appropriately scary red interstitial warning page that strongly advises you not to visit the page you’re trying to visit, courtesy of Google’s [safe browsing API](https://developers.google.com/safe-browsing/). But of course this kind of shared blacklist domain name protection will be completely useless on any fresh phishing site. (Don’t even get me started on how [blacklists have never really worked](https://blog.codinghorror.com/blacklists-dont-work/) anyway.)


![google-login-phishing-page](https://blog.codinghorror.com/content/images/2018/09/google-login-phishing-page.png)


It doesn’t exactly require a PhD degree in computer science to phish someone:

- Buy a crazy long, realistic looking domain name.
- Point it to a cloud server somewhere.
- Get a free HTTPS certificate courtesy of [our friends at Let’s Encrypt](https://blog.codinghorror.com/lets-encrypt-everything/).
- Build a realistic copy of a login page that silently transmits everything you type in those login fields to you – perhaps even in real time, as the target types.
- Harvest email addresses and mass mail a plausible looking phishing email with your URL.


I want to emphasize that although clearly mistakes were made in this specific situation, none of the people involved here were amateurs. They had training and experience. They were working with IT and security professionals. Furthermore, they [knew digital attacks were incoming](https://www.apnews.com/dea73efc01594839957c3c9a6c962b8a).


> The… campaign was no easy target; several former employees said the organization put particular stress on digital safety.
> Work emails were protected by two-factor authentication, a technique that uses a second passcode to keep accounts secure. Most messages were deleted after 30 days and staff went through phishing drills. Security awareness even followed the campaigners into the bathroom, where someone put a picture of a toothbrush under the words: “You shouldn’t share your passwords either.”


The campaign itself used two factor auth extensively, which is why personal Gmail accounts were targeted, because they were less protected.


The key takeaway here is that **it’s basically impossible, statistically speaking, to prevent your organization from being phished.**


Or is it?


![](https://blog.codinghorror.com/content/images/2025/02/image-32.png)


Nobody is doing better work in this space right now than Maciej Ceglowski and Tech Solidarity. Their list of [basic security precautions](https://techsolidarity.org/resources/basic_security.htm) for non-profits and journalists is pure gold and has been vetted by many industry professionals with security credentials that are actually impressive, unlike mine. Everyone should read this list very closely, point by point.


Everyone?


Computers, courtesy of smartphones, are now such a [pervasive part of average life](https://blog.codinghorror.com/can-software-make-you-less-racist/) for average people that **there is no longer any such thing as “computer security.” There is only *security*.** In other words, these are normal security practices *everyone* should be familiar with. Not just computer geeks. Not just political activists and politicians. Not just journalists and nonprofits.


*Everyone.*


It is a fair bit of reading, so because I know you are just as lazy as I am, and I am *epically* lazy, let me summarize what I view as the three important takeaways from the hard work Tech Solidarity put into [these resources](https://techsolidarity.org/resources.html). These three short sentences are the 60 second summary of what you want to do, and what you want to share with others so *they* do, too.


**1) Enable Two Factor authentication through an app, and *not SMS*, everywhere you can.**


![google-2fa-1](https://blog.codinghorror.com/content/images/2018/09/google-2fa-1.png)


Logging in with only a password, now matter how long and unique you attempt to make that password, will never be enough. A password is what you know; you need to add the second factor of something you *have* (or something you *are*) to achieve significant additional security. [SMS can famously be intercepted](https://www.wired.com/story/phone-numbers-indentification-authentication/), social engineered, or sim-jacked all too easily. If it’s SMS, it’s not secure, *period*. So install an authenticator app, and use it, at least for your most important credentials such as your email account and your bank.


Have I mentioned that Discourse added [two factor authentication support](https://blog.discourse.org/2018/05/discourse-2-0-released/) in version 2.0, and our just released 2.1 adds printed backup codes, too? There are two paths forward: you can *talk* about the solution, or you can *build* the solution. I’m trying to do both to the best of my ability. Look for the 2FA auth option in your user preferences on your favorite Discourse instance. It’s there for you.


(This is also a company policy at Discourse; if you work here, *you 2FA everything all the time*. No other login option exists.)


**2) Make all your passwords 11 characters or more.**


It’s [a long story](https://blog.codinghorror.com/hacker-hack-thyself/), but anything under 11 characters is basically the [same as having no password](https://blog.codinghorror.com/your-password-is-too-damn-short/) at all these days. I personally recommend at least 14 characters, maybe even 16. But this won’t be a problem for you, because...


**3) Use a password manager.**


If you use a password manager, you can simultaneously avoid the pernicious danger of password re-use and the difficulty of coming up with [unique and random passwords](https://blog.codinghorror.com/password-rules-are-bullshit/) all the time. It is my hope in the long run that cloud based password management gets deeply built into Android, iOS, OSX, and Windows so that people don’t need to run a weird mélange of third party apps to achieve this essential task. Password management is foundational and should not be the province of third parties on principle, because you never outsource a core competency.


**Bonus rule! For the particularly at-risk, get and use a U2F key.**


In the long term, two factor through an app isn’t quite secure enough due to the very real (and growing) specter of real-time phishing. Authentication apps offer timed keys that expire after a minute or two, but if the attacker can get you to type an authentication key and relay it to the target site fast enough, they can still log in as you. If you need ultimate protection, look into [U2F keys](https://en.wikipedia.org/wiki/Universal_2nd_Factor).


![u2f-keys](https://blog.codinghorror.com/content/images/2018/09/u2f-keys.jpg)


I believe U2F support is still too immature at the moment, particularly on mobile, for this to be practical for the average person right now. But if you do happen to fall into those groups that will be under attack, you *absolutely* want to set up U2F keys where you can today. They’re cheap, and the good news is that they *literally make phishing impossible* at last. Given that Google had 100% company-wide [success against phishing with U2F](https://krebsonsecurity.com/2018/07/google-security-keys-neutralized-employee-phishing/), we know this works.


In today’s world, computers are now so omnipresent that there is no longer any such thing as cybersecurity, online security, or computer security – there’s only *security*. You either have it, or you don’t. If you follow and share these three rules, hopefully you too can have a modicum of security today.

[cybersecurity](https://blog.codinghorror.com/tag/cybersecurity/)
[phishing](https://blog.codinghorror.com/tag/phishing/)
[hacking](https://blog.codinghorror.com/tag/hacking/)
[password security](https://blog.codinghorror.com/tag/password-security/)
