---
title: "Should All Web Traffic Be Encrypted?"
date: 2012-02-23
url: https://blog.codinghorror.com/should-all-web-traffic-be-encrypted/
slug: should-all-web-traffic-be-encrypted
word_count: 1159
---

The prevalence of free, open WiFi has made it **rather easy for a WiFi eavesdropper to steal your identity cookie for the websites you visit while you’re connected to that WiFi access point**. This is something I talked about in [Breaking the Web’s Cookie Jar](https://blog.codinghorror.com/breaking-the-webs-cookie-jar/). It’s difficult to fix without making major changes to the web’s infrastructure.


In the year since I wrote that, a number of major websites have “solved” the WiFi eavesdropping problem by either making encrypted HTTPS web traffic an *account option* or *mandatory* for all logged in users.


For example, I just noticed that Twitter, transparently to me and presumably all other Twitter users, **switched to an encrypted web connection by default**. You can tell because most modern browsers show the address bar in green when the connection is encrypted.


![](https://blog.codinghorror.com/content/images/2025/04/image-588.png)


I initially resisted this as overkill, except for obvious targets like email (the skeleton key to [all your online logins](https://blog.codinghorror.com/please-give-us-your-email-password/)) and banking.


> Yes, **you can naively argue that every website should encrypt all their traffic all the time**, but to me that’s a “boil the sea” solution. I’d rather see a better, more secure identity protocol than ye olde HTTP cookies. I don’t actually care if anyone sees the rest of my public activity on Stack Overflow; it’s hardly a secret. But gee, I sure *do* care if they [somehow sniff out my cookie](https://blog.codinghorror.com/protecting-your-cookies-httponly/) and start running around doing stuff as me! Encrypting everything just to protect that one lousy cookie header seems like a whole lot of overkill to me.


Of course, there’s no reason to encrypt traffic for anonymous, not-logged-in users, and Twitter doesn’t. You get a plain old HTTP connection until you log in, at which point they automatically switch to HTTPS encryption. Makes sense.


It was totally painless for me, as a user, and it makes stealing my Twitter identity, or eavesdropping on my Twitter activity (as fascinating as I know that must sound), dramatically more difficult. I can’t really construct a credible argument *against* doing this, even for something as relatively trivial as my Twitter account, and it has some definite benefits. So perhaps Twitter has the right idea here; **maybe encrypted connections *should* be the default for all web sites**. As tinfoil hat as this seemed to me a year ago, now I’m wondering if that might actually be the right thing to do for the long-term health of the overall web, too.


![](https://blog.codinghorror.com/content/images/2025/04/image-587.png)


Why not boil the sea, then? Let us *encrypt all the things!*


## HTTPS isn’t (that) expensive any more


Yes, in the hoary old days of the 1999 web, HTTPS was quite computationally expensive. But thanks to 13 years of Moore’s Law, that’s no longer the case. It’s still *more work* to set up, yes, but consider the [real world case of Gmail](http://www.imperialviolet.org/2010/06/25/overclocking-ssl.html):


> In January this year (2010), Gmail switched to using HTTPS for everything by default. Previously it had been introduced as an option, but now all of our users use HTTPS to secure their email between their browsers and Google, all the time. In order to do this we had to deploy *no additional machines and no special hardware*. On our production frontend machines, SSL/TLS accounts for less than 1% of the CPU load, less than 10KB of memory per connection and less than 2% of network overhead. Many people believe that SSL takes a lot of CPU time and we hope the above numbers (public for the first time) will help to dispel that.


## HTTPS means The Man can’t spy on your Internet


Since all the traffic between you and the websites you log in to would now be encrypted, the ability of nefarious evildoers to either…

- steal your identity cookie
- peek at what you’re doing
- see what you’ve typed
- interfere with the content you send and receive


… is, if not [completely eliminated](http://security.stackexchange.com/questions/6290/how-is-it-possible-that-people-observing-an-https-connection-being-established-w), drastically limited. Regardless of whether you’re on open public WiFi or not.


Personally, I don’t care too much if people see what I’m doing online since the whole point of a lot of what I do is to… let people see [what I’m doing online](https://blog.codinghorror.com/when-in-doubt-make-it-public/). But I certainly don’t subscribe to the dangerous idea that “only criminals have things to hide”; everyone deserves the right to personal privacy. And there are lots of repressive governments out there who wouldn’t hesitate at the chance to spy on what their citizens do online, or worse. Much, much worse. Why not improve the Internet for all of them at once?


## HTTPS goes faster now


Security always comes at a cost, and encrypting a web connection is no different. HTTPS is going to be inevitably slower than a regular HTTP connection. But how *much* slower? It used to be that encrypted content wouldn’t be cached in some browsers, but [that’s no longer true](http://gent.ilcore.com/2011/02/chromes-10-caches.html?showComment=1297102528799#c5411401837359385517). And Google’s SPDY protocol, intended as a drop-in replacement for HTTP, even goes so far as to [bake encryption in by default](http://dev.chromium.org/spdy/spdy-whitepaper), and not just for better performance:


> [It is a specific technical goal of SPDY to] make SSL the underlying transport protocol, for better security and compatibility with existing network infrastructure. Although SSL does introduce a latency penalty, we believe that the long-term future of the web depends on a secure network connection. In addition, the use of SSL is necessary to ensure that communication across existing proxies is not broken.


There’s also [SSL False Start](http://blog.chromium.org/2011/05/ssl-falsestart-performance-results.html) which requires a modern browser, but reduces the [painful latency](https://web.archive.org/web/20120301120201/http://www.semicomplete.com/blog/geekery/ssl-latency.html) inherent in the expensive, but necessary, handshaking required to get encryption going. SSL encryption of HTTP will never be *free*, exactly, but it’s certainly a lot faster than it used to be, and getting faster every year.


Bolting on encryption for logged-in users is by no means an easy thing to accomplish, particularly on large, established websites. You won’t see me out there berating every public website for not offering encrypted connections yesterday because I know how much work it takes, and how much additional complexity it can add to an already busy team. Even though HTTPS is way easier now than it was even a few years ago, there are still plenty of tough gotchas: proxy caching, for example, becomes vastly harder when the proxies can no longer “see” what the encrypted traffic they are proxying is doing. Most sites these days are a broad mashup of content from different sources, and technically *all* of them need to be on HTTPS for a properly encrypted connection. Relatively underpowered and weakly connected mobile devices will pay a much steeper penalty, too.


Maybe not tomorrow, maybe not next year, but over the medium to long term, **adopting encrypted web connections as a standard for logged-in users** is the healthiest direction for the future of the web. We need to work toward making HTTPS easier, faster, and most of all, *the default* for logged in users.

[security](https://blog.codinghorror.com/tag/security/)
[user experience](https://blog.codinghorror.com/tag/user-experience/)
[encryption](https://blog.codinghorror.com/tag/encryption/)
[web development](https://blog.codinghorror.com/tag/web-development/)
[technology trends](https://blog.codinghorror.com/tag/technology-trends/)
