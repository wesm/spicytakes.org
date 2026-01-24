---
title: "Let’s Encrypt Everything"
date: 2016-11-23
url: https://blog.codinghorror.com/lets-encrypt-everything/
slug: lets-encrypt-everything
word_count: 568
---

I’ll admit I was [late to the HTTPS party](https://blog.codinghorror.com/should-all-web-traffic-be-encrypted/).


![](https://blog.codinghorror.com/content/images/2025/02/image-47.png)


But post Snowden, and particularly after the result of the last election here in the US, it’s clear that **everything on the web should be encrypted by default**.


Why?

1. You have [an inalienable right to privacy](https://blog.codinghorror.com/an-inalienable-right-to-privacy/), both in the real world and online. And **without HTTPS you have zero online privacy** – from anyone else on your WiFi, from your network provider, from website operators, from large companies, from the government.
2. **The performance penalty of HTTPS is gone**, in fact, HTTPS arguably [performs *better* than HTTP](http://blog.httpwatch.com/2015/01/16/a-simple-performance-comparison-of-https-spdy-and-http2/) on modern devices..
3. **Using HTTPS means nobody can tamper with the content in your web browser.** This was a bit of an abstract concern five years ago, but these days, there are more and more instances of upstream providers actively mucking with the data that passes through their pipes. For example, if Comcast detects you have a copyright strike, they’ll [insert banners into your web content](http://arstechnica.com/tech-policy/2013/02/heres-what-an-actual-six-strikes-copyright-alert-looks-like/)… *all* your web content! And that’s what the good guy scenario looks like – or at least a corporation trying to follow the rules. Imagine what it looks like when someone, or some large company, decides the rules don’t apply to them?


So, how do you as an end user “use” encryption on the web? Mostly, you lobby for the websites you use regularly to adopt it. And it’s working. In the last year, the use of HTTPS by default on websites [has doubled](https://snyk.io/blog/https-breaking-through/).


![](https://blog.codinghorror.com/content/images/2016/11/https-share-top-500k-sites.png)


Browsers can help, too. By January 2017, Google Chrome will show this alert in the UI when a login or credit card form is displayed on an unencrypted connection:


![](https://blog.codinghorror.com/content/images/2016/11/chrome-insecure.jpg)


Additionally, Google is throwing their considerable weight behind this effort by [ranking non-encrypted websites lower](https://webmasters.googleblog.com/2014/08/https-as-ranking-signal.html) in search results.


But there’s another essential part required for encryption to work on *any* websites – **the HTTPS certificate**. Historically these certificates have been [issued by certificate authorities](https://blog.codinghorror.com/digital-certificates-do-they-work/), and they were at least $30 per year per website, sometimes hundreds of dollars per year. Without that required cash each year, without the SSL certificate that you must re-purchase every year in perpetuity – you can’t encrypt *anything*.


That is, until [Let’s Encrypt](https://letsencrypt.org/) arrived on the scene.


![](https://blog.codinghorror.com/content/images/2025/02/image-48.png)


Let’s Encrypt is a 501.3(c)(3) non-profit organization supported by the Linux Foundation. They’ve been in beta for about a year now, and to my knowledge they are the only reliable, official free source of SSL certificates that has ever existed.


However, **because Let’s Encrypt is a non-profit organization**, not owned by any company that must make a profit from each SSL certificate they issue, they need our support:


As a company, we’ve donated a [Discourse hosted support community](https://community.letsencrypt.org/), and a cash amount that represents how much we would have paid in a year to one of the existing for-profit certificate authorities to set up HTTPS for all the [Discourse](https://discourse.org/) websites we host.


I urge you to do the same:

- Estimate how much you would have paid for any free SSL certificates you obtained from Let’s Encrypt, and [please donate that amount](https://letsencrypt.org/donate/) to Let’s Encrypt.
- If you work for a large company, urge them to [sponsor Let’s Encrypt](https://letsencrypt.org/become-a-sponsor/) as a fundamental cornerstone of a safe web.


If you believe in an unalienable right to privacy on the Internet for every citizen in every nation, *please* support Let’s Encrypt.

[encryption](https://blog.codinghorror.com/tag/encryption/)
[https](https://blog.codinghorror.com/tag/https/)
[privacy](https://blog.codinghorror.com/tag/privacy/)
[data protection](https://blog.codinghorror.com/tag/data-protection/)
[cybersecurity](https://blog.codinghorror.com/tag/cybersecurity/)
