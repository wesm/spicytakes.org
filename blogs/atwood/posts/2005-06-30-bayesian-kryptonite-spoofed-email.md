---
title: "Bayesian Kryptonite – spoofed email"
date: 2005-06-30
url: https://blog.codinghorror.com/bayesian-kryptonite-spoofed-email/
slug: bayesian-kryptonite-spoofed-email
word_count: 423
---

I use [POPFile Bayesian filtering](https://blog.codinghorror.com/some-plans-for-spam/) to keep email spam at bay. With a little training, this works amazingly well – I’m at 99.8% accuracy, and that’s with a little over a month of “training” precipitated by a recent server migration. But Bayesian filtering has one big weakness that I’m seeing more and more: [spoofed emails](https://web.archive.org/web/20050701080748/http://www.cert.org/tech_tips/email_spoofing.html).


You know what I mean – emails titled **Your Account Has Been Violated** from, ostensibly from [[email protected]](https://blog.codinghorror.com/cdn-cgi/l/email-protection). The body is a direct cut and paste from a real PayPal email:


> *Security Center Advisory!
> We recently noticed one or more attempts to log in to your PayPal account from a foreign IP address and we have reasons to believe that your account was hacked by a third party without your authorization. If you recently accessed your account while traveling, the unusual log in attempts may have been initiated by you.
> If you are the rightful holder of the account you must click the link below and then complete all steps from the following page as we try to verify your identity.*


Of course, the spoofer is desperately hoping you won’t notice that the crazy URLs in their email...

kg-card-begin: html

```

http://paypaldemo.com.previewyoursite.com/source/service/ema/helpextsourcepage/PaypalISAPIruhttp3A2F2Fmyebamcom3A802Fws2FeBayISAPIdll3FMyeBay26ssPageName3DH253AH253A/
http://ebay.doubleclick.net/clk;13012399;10693575;h?
http://cardsavetransfer.com/cmdr_login/index.htm
http://ebay.doubleclick.net/clk;13012399;10693575;h?
http://paypalcardstraznact.com/cmdr_login/index.htm

```

kg-card-end: html

... aren’t actually pointing to paypal.com (or ebay.com), and you'll key in your account and password on their servers.


These spoof emails contain so-called “kryptonite” because they so closely mimic actual emails from PayPal with valid words and phrases. Bayesian filtering is useless against this type of spam; if the spammer knows what any email in your actual inbox looks like, he can construct one that will [beat any Bayesian filter](https://blog.codinghorror.com/popfile-vs-popfile/). This is a a strict requirement at the very heart of Bayesian filtering itself; any knowledge of valid contents (e.g., things that “get through”) *has to be strictly eliminated*.


I usually just delete these emails from my inbox; what else can I do? One thing is for sure: **popular web-based services can no longer communicate via email with their customers**. That’s like giving spoofers a free pass; once they have the “template” email they can copy and paste it into a spoof email that is almost guaranteed to get past Bayesian filtering for users of that service.


eBay, for example, has almost [given up altogether on email](https://web.archive.org/web/20070211004438/http://news.com.com/eBay+fights+back+against+phishers/2100-1029_3-5512182.html) communication. You have to visit eBay.com and check your web-based “message center” to communicate with them. I can’t say I blame them; what other choice do they have?

[email security](https://blog.codinghorror.com/tag/email-security/)
[bayesian filtering](https://blog.codinghorror.com/tag/bayesian-filtering/)
[spoofed emails](https://blog.codinghorror.com/tag/spoofed-emails/)
[spam detection](https://blog.codinghorror.com/tag/spam-detection/)
[phishing emails](https://blog.codinghorror.com/tag/phishing-emails/)
