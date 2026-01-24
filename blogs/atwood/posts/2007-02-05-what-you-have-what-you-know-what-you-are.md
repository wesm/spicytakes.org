---
title: "What You Have, What You Know, What You Are"
date: 2007-02-05
url: https://blog.codinghorror.com/what-you-have-what-you-know-what-you-are/
slug: what-you-have-what-you-know-what-you-are
word_count: 749
---

I’m no fan of the classic login/password scheme. I can barely remember any of the [zillion logins and passwords](https://blog.codinghorror.com/the-login-explosion/) I have. More often than not, I end up using the “forgot password” link. Which means, in effect, that **my email account is my global password**. And if you’re like most people, your email [password isn’t very secure](https://blog.codinghorror.com/passphrase-evangelism/). As Bruce Schneier recently [observed](http://www.schneier.com/essay-144.html):


> We used to quip that “password” is the most common password. Now it’s “password1.” Who said users haven’t learned anything about security?


It’s a depressing state of affairs. [Switching to passphrases helps](https://blog.codinghorror.com/passwords-vs-pass-phrases/), but is a band-aid at best.


The relentless increase in phishing attacks may soon force some changes on this front. I saw in the news that PayPal is switching to [two-factor authentication](http://www.cnet.com/news/paypal-to-offer-password-key-fobs-to-users/). Specifically, they’re providing users with a keyfob that produces a new six-digit code every 30 seconds. Users will now have to type in their name, password, *and* a valid code from the keyfob.


![](https://blog.codinghorror.com/content/images/2025/06/image-122.png)


The PayPal system isn’t [SecurID](http://en.wikipedia.org/wiki/SecurID), but I’m sure the implementation is very similar. There’s a matching seed value stored on the server for each keyfob, so the server can calculate what the correct code should be. If the user enters the correct password *and* the correct code (within 30 seconds), they’re allowed in.


So what’s the value in doing this? It’s more hassle and more expense. Well, consider that all security is based on three things:


#### What you have


#### What you know


#### What you are


We all use logins and passwords. That’s *something we know*. When we enter the code from the keyfob, we’ve added *something we have* to the mix. That’s [two factor authentication](https://en.wikipedia.org/wiki/Two-factor_authentication), and it increases security dramatically.


But even with the keyfob, we haven’t quite removed the risk of phishing entirely. All we’ve done is make the window of opportunity smaller. If a phishing site can relay the user-provided data to the server in real time (or close enough), they will still be authenticated.


A common form of *local* two-factor authentication is the Smart Card.


![](https://blog.codinghorror.com/content/images/2025/06/image-121.png)


Smart cards have an embedded microprocessor that uniquely identifies each card, a private key of sorts. Some even have the ability to store data. The secrets on each card stay secret because it’s impossible to extract the data without destroying the chip in the process. Since smart cards are read by hardware on your PC, they’re of no use online. But they can dramatically enhance security locally. For example, Windows has embedded support for smart cards; **it’s possible to log into the operating system using nothing but a smart card and a short PIN code**. The PIN code is still a password of sorts, but it’s much shorter and easier to remember.


Once you switch over to smart cards, it’s no longer possible to log in using a traditional username and password. Your underlying password becomes a randomly generated 64-character string. As you can imagine, this is a *huge* boon for local security [compared to user-selected passwords](http://www.schneier.com/essay-144.html). I don’t personally care for smart cards, but I can certainly understand why organizations choose to use them.


But two-factor authentication, although more secure, isn’t a panacea. Bruce Schneier is quick to remind us that [two-factor authentication is vulnerable](http://www.schneier.com/blog/archives/2005/03/the_failure_of.html) to two primary forms of attack:


> **Man-in-the-Middle attack**. An attacker puts up a fake bank website and entices user to that website. User types in his password, and the attacker in turn uses it to access the bank’s real website. Done right, the user will never realize that he isn’t at the bank’s website. Then the attacker either disconnects the user and makes any fraudulent transactions he wants, or passes along the user’s banking transactions while making his own transactions at the same time.
> **Trojan attack**. Attacker gets Trojan installed on user’s computer. When user logs into his bank’s website, the attacker piggybacks on that session via the Trojan to make any fraudulent transaction he wants.


We already knew about the man-in-the-middle attack; we refer to it as real-time phishing. As for trojans, it might be a little unfair to blame two-factor authentication for not protecting the user from a compromised system. I’m not sure *any* security measures can work on a compromised system with trojan keyloggers and screenloggers installed.


Despite Schneier’s skepticism, I think two-factor authentication is worthwhile. Anything that moves the security bar beyond the **hopelessly insecure and ineffective username/password combos** we’re currently stuck with is a welcome change.

[security](https://blog.codinghorror.com/tag/security/)
[authentication](https://blog.codinghorror.com/tag/authentication/)
[password security](https://blog.codinghorror.com/tag/password-security/)
[two-factor authentication](https://blog.codinghorror.com/tag/two-factor-authentication/)
[phishing](https://blog.codinghorror.com/tag/phishing/)
