---
title: "Blocking Image Bandwidth Theft with URL Rewriting"
date: 2006-04-06
url: https://blog.codinghorror.com/blocking-image-bandwidth-theft-with-url-rewriting/
slug: blocking-image-bandwidth-theft-with-url-rewriting
word_count: 637
---

I like to periodically watch the [HTTP traffic on my server](https://blog.codinghorror.com/sniff-this/). I can see what I’m actually serving up over the wire, and how much bandwidth I’m using.


That’s how I noticed that I’ve become somewhat popular with **direct-link image bandwidth thieves**. In other words, people who thoughtlessly (or maliciously) embed these IMG links in their web page:


![](https://blog.codinghorror.com/content/images/2025/05/image-258.png)


That means the image qbert_regex_16.png is served by *my webserver* to every user who happens to request [this myspace profile page](https://web.archive.org/web/20070309132613/http://profile.myspace.com/index.cfm?fuseaction=user.viewprofile&friendid=27727152).


Warning: like all myspace pages, that page is

- Not really safe for work
- Incredibly, mind-bendingly ugly
- Filled with thousands of images, animated images, flash, MIDI samples, embedded MP3s
- Utterly and completely incomprehensible


In short, a train wreck. Every time I visit myspace, I feel a little bit stupider, ala [Billy Madison](http://www.imdb.com/title/tt0112508/):


> *Principal: Mr. Madison, what you’ve just said is one of the most insanely idiotic things I have ever heard. At no point in your rambling, incoherent response were you even close to anything that could be considered a rational thought. Everyone in this room is now dumber for having listened to it. I award you no points, and may God have mercy on your soul.
> Billy Madison: Okay, a simple no would’ve done just fine.*


I have no idea why myspace is so popular. I guess the best I can hope for is that those damn kids stay off my lawn.


Anyway, back to business. The most common technique for blocking direct image links is to **check the HTTP referer header**. Here’s the complete HTTP header set of an image request that just came through:

kg-card-begin: html

```

GET /blog/images/logitech_g15_keyboard.jpg HTTP/1.1
Accept: */*
Referrer: http://www2.gamelux.nl/forum/topics/10072/38/
Accept-Language: nl
Accept-Encoding: gzip, deflate
User-Agent: Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)
Host: www.codinghorror.com
Connection: Keep-Alive

```

kg-card-end: html

Prior to serving up the image, we should check the Referrer HTTP header, and make sure it’s either:

1. Blank
2. In a list of known whitelisted referring domains


If it isn’t, we will serve up either a 404 error, or a “hey, stop stealing our bandwidth” image of some kind. Because I’m a nice guy, I chose this image:


![](https://blog.codinghorror.com/content/images/2025/03/block.gif)


All this can be done through incredibly powerful [URL Rewriting](http://httpd.apache.org/docs/2.0/misc/rewriteguide.html), which has been standard on Apache for some time. There’s a nice walkthrough on how to set up image link blocking in Apache on Tom Sherman’s site.


Unfortunately, IIS 6 doesn’t have native support for URL Rewriting,* but there are any number of third party ISAPI filters that can do it. The one I use is [ISAPI Rewrite](https://web.archive.org/web/20060406231523/http://www.isapirewrite.com/). It’s very similar to the Apache version, in that it is driven by the httpd.ini file in the root of each website. I struggled a bit with the rules, but thanks to a [helpful forum post](https://web.archive.org/web/20071012192714/http://www.helicontech.com/forum/forum_posts-TID-4280.asp), I realized that I needed to put all the whitelisted domains on a single line to get a boolean “or” that included the empty referrer case, like so:

kg-card-begin: html

```
[ISAPI_Rewrite]

# Block external image linking
RewriteCond Referer: (?!http://(?:www.codinghorror.com|www.bloglines.com|www.google.com)).+
RewriteRule .*.(?:gif|jpg|png) /images/block.gif [I,O]
  
```

kg-card-end: html

So, as outlined above: unless the referrer is blank, or in the whitelist, they get shunted to the blocked image.**


**Take that, 26 zillion myspace users**.


*I’m pretty sure URL Rewriting will be in IIS7, since they’re finally getting around to making a really good copy of Apache’s modular architecture in version 7.


**This is done at the ISAPI level, so unlike the cheesy ASP.NET “URL rewriting” solutions, it also works on generic URLs, not just URLs that end in .aspx or some other extension that is sent to the ASP.NET handler. This has long been a pet peeve of mine, but it’s really the fault of IIS. And it’s changing in IIS 7.

[security](https://blog.codinghorror.com/tag/security/)
[url rewriting](https://blog.codinghorror.com/tag/url-rewriting/)
[bandwidth theft](https://blog.codinghorror.com/tag/bandwidth-theft/)
[web traffic](https://blog.codinghorror.com/tag/web-traffic/)
[http](https://blog.codinghorror.com/tag/http/)
