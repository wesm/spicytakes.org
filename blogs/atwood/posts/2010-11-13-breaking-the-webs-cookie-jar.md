---
title: "Breaking the Web’s Cookie Jar"
date: 2010-11-13
url: https://blog.codinghorror.com/breaking-the-webs-cookie-jar/
slug: breaking-the-webs-cookie-jar
word_count: 1209
---

The Firefox add-in [Firesheep](http://codebutler.com/firesheep) caused quite an uproar a few weeks ago, and justifiably so. Here’s how it works:

- Connect to a public, *unencrypted* WiFi network. In other words, a WiFi network that doesn’t require a password before you can connect to it.
- Install Firefox and the Firesheep add-in.
- Wait. Maybe have a latte while you’re waiting.
- Click on the user / website icons that appear over time in Firesheep to **instantly log in as that user on that website**.


Crazy! This guy who wrote Firesheep must be a world-class hacker, right?


Well, no. The work to package this up in a point-and-click way that is (sort of) accessible to power users is laudable, but what Firesheep actually *does* is far from magical. It’s more of an art project and PR stunt than an actual hack of any kind. Still, I was oddly excited to see Firesheep get so much PR, **because it highlights a fundamental issue with the architecture of the web.**


The web is kind of a primitive medium. The only way websites know who you are is through tiny, uniquely identifying strings your browser sends to the webserver on each and every click:

kg-card-begin: html

```

GET / HTTP/1.1
Host: diy.stackexchange.com
Connection: keep-alive
User-Agent: Chrome/7.0.517.44
Accept-Language: en-US,en;q=0.8
Cookie: diyuser=t=ZlQOG4kege&s=8VO9gjG7tU12s
If-Modified-Since: Tue, 09 Nov 2010 04:41:12 GMT

```

kg-card-end: html

These are the typical sort of HTTP headers your browser sends to a website on every click. See that little cookie in bright red? To a website, that’s your fingerprint, DNA, and social security number all rolled into one. **Some part of the cookie contains a unique user ID that tells the website you are *you***.


And guess what? That cookie is always broadcast in plain text every single time you click a link on any website. Right out in the open where anyone – well, technically, *anyone who happens to be on the same network as you and is in a position to view your network packets* – can just grab it out of the ether and **immediately impersonate you on any website you are a member of.**


![](https://blog.codinghorror.com/content/images/2025/04/image-496.png)


Now that you know how cookies work (and I’m not saying it’s rocket surgery or anything), you also know that what Firesheep does is relatively straightforward:

1. Listen to all HTTP traffic.
2. Wait for HTTP headers from a known website.
3. Isolate the part of the cookie header that identifies the user.
4. Launch a new browser session with that cookie. Bam! As far as the target webserver is concerned, you *are* that user!


All Firesheep has to do, really, is *listen*. That’s pretty much all there is to this “hack.” Scary, right? Well, then you should be positively quaking in your boots, because **this is the way the entire internet has worked since 1994**, when [cookies were invented](http://en.wikipedia.org/wiki/HTTP_cookie#History).


So why wasn’t this a problem in, say, 2003? Three reasons:

1. Commodity public wireless internet connections were not exactly common until a few years ago.
2. Average people have moved beyond mostly anonymous browsing and transferred significant parts of their identity online (aka the Facebook effect).
3. The tools required to listen in on a wireless network are slightly… less primitive now.


Firesheep came along at the exact inflection point of these three trends. And mind you, it is still not a sure thing – Firesheep requires a particular set of wireless network chipsets that support [promiscuous mode](http://en.wikipedia.org/wiki/Promiscuous_mode) in the lower level WinPcap library that Firesheep relies on. But we can bet that the floodgates have been opened, and future tools similar to this one will become increasingly a one-click affair.


The other reason this wasn’t a problem in 2003 is because **any website that truly *needed* security switched to encrypted HTTP – aka **[**Secure HTTP**](http://en.wikipedia.org/wiki/HTTP_Secure)** – long ago**. HTTPS was invented in 1994, at the same time as the browser cookie. This was not a coincidence. The creators of the cookie knew from day one they needed a way to protect them from prying eyes. Even way, way back in the dark, primitive ages of 2003, any banking website or identity website worth a damn wouldn’t even *consider* using plain vanilla HTTP. They’d be laughed off the internet!


The outpouring of concern over Firesheep is justified, because, well, the web’s cookie jar has always been kind of broken – and we ought to do something about it. But what?


![](https://blog.codinghorror.com/content/images/2025/08/broken-cookie-jar.jpg)


Yes, **you can naively argue that every website should encrypt all their traffic all the time**, but to me that’s a “boil the sea” solution. I’d rather see a better, more secure identity protocol than ye olde HTTP cookies. I don’t actually care if anyone sees the rest of my public activity on Stack Overflow; it’s hardly a secret. But gee, I sure *do* care if they [somehow sniff out my cookie](https://blog.codinghorror.com/protecting-your-cookies-httponly/) and start running around doing stuff as me! Encrypting everything just to protect that one lousy cookie header seems like a whole lot of overkill to me.


I’m not holding my breath for that to happen any time soon, though. So here’s what you can do to protect yourself, right now, today:

1. **We should be very careful how we browse on unencrypted wireless networks**. This is the great gift of Firesheep to all of us. If nothing else, we should be thanking the author for this simple, stark warning. It’s an unavoidable fact of life: if you must go wireless, seek out *encrypted* wireless networks. If you have no other choices except unencrypted wireless networks, browse anonymously – quite possible if all you plan to do is casually surf the web and read a few articles – and *only* log in to websites that support https. Anything else risks identity theft.
2. **Get in the habit of accessing your web mail through HTTPS**. Email is the de-facto skeleton [key to your online identity](https://blog.codinghorror.com/please-give-us-your-email-password/). When your email is compromised, all is lost. If your webmail provider does not support secure http, they are idiots. Drop them like a hot potato and *immediately* switch to one that does. Heck, the smart webmail providers already [switched to https by default!](http://gmailblog.blogspot.com/2010/01/default-https-access-for-gmail.html)
3. **Lobby the websites you use to offer HTTPS browsing**. I think we’re clearly past the point where only banks and finance sites should be expected to use secure HTTP. As more people shift more of their identities online, it makes sense to protect those identities by moving HTTPS from the domain of a massive bank vault door to just plain *locking the door*. [SSL isn’t as expensive](http://www.imperialviolet.org/2010/06/25/overclocking-ssl.html) as it used to be, in every dimension of the phrase, so this is not an unreasonable thing to ask your favorite website for.


This is very broad advice, and there are a whole host of technical caveats to the above. But it’s a starting point toward evangelizing the risks and responsible use of open wireless networks. Firesheep may indeed have broken the web’s cookie jar. But it was kind of an old, beat up, cracked cookie jar in the first place. I hope the powers that be will use Firesheep as incentive to **build a better online identity solution than creaky old HTTP cookies**.

[security](https://blog.codinghorror.com/tag/security/)
[web security](https://blog.codinghorror.com/tag/web-security/)
[hacking](https://blog.codinghorror.com/tag/hacking/)
[cyber security](https://blog.codinghorror.com/tag/cyber-security/)
[data privacy](https://blog.codinghorror.com/tag/data-privacy/)
