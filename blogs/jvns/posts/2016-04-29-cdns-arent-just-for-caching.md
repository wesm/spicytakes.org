---
title: "CDNs aren't just for caching"
date: 2016-04-29
url: https://jvns.ca/blog/2016/04/29/cdns-arent-just-for-caching/
slug: cdns-arent-just-for-caching
word_count: 1476
---


I joined the infrastructure team at work this week! So I’ve been learning a bunch of new things. Today I learned a ton about what CDNs are for.


A CDN is a “content delivery network” – the idea is that you’re a website and you have some Fancy Javascript File that you want people everywhere in the world to download. No problem. That is what the internet is for.


But you are in New York, and the speed of light is slow (really!), and you are trying to send the javascript file to Sydney – that’s 16,000 km away, which is 50ms at the speed of light, or a 100ms round trip. With a bad mobile connection that’s dropping packets, it can get even worse! So now everyone can probably still get your file, mostly, but it might take them a long time to get it.


A common solution is to put the file on a server physically in Sydney, so that Sydneysiders (!!) can get it faster. This is what a CDN does. And I thought that was all that it did! But today I asked [many questions on Twitter](https://twitter.com/b0rk/status/726062053920747520) and it turns out that I was very wrong – CDNs are not only good for caching content! People also use them for other reasons! So in this post we’re only going to discuss non-caching uses of CDNs.


The core questions we’re going to try to answer are:

- does putting your site (without caching) behind a CDN get you better performance?
- how about better reliability?
- are there other advantages?


Spoiler: the answers to all these questions seem to be yes, sometimes.


### make your site faster: speed up the dreaded TLS handshake


This was the first (and most compelling) reason that people repeatedly brought up.


Suppose that you’re serving content securely, as we like to do these days. If you Google “TLS handshake”, you’ll see a diagram like [this one](http://chimera.labs.oreilly.com/books/1230000000545/ch04.html#TLS_HANDSHAKE). The important thing about this diagram is that it has 7 packets. If a cell phone in Sydney needs to set up a TLS connection with your website in New York that will take at **least** 350ms (because of the speed of light), and more if any packets get dropped. This is not good!


But how will a proxy server in Sydney fix this?! WELL. Suppose you give the server in Sydney your SSL certificate. Then it can set up a TLS connection with the flaky cell phone and, separately, use a TLS connection it already has set up to send you the data and get the cell phone the response. Lots of people told me that they do this and that it can be way faster. Cool.


You are perceptive and will notice that you have to give the CDN your SSL certificate to do this. More about that later.


### make your site faster: smart routing


Forgetting about TLS for a moment now: how else could having a server in Sydney help the flaky cell phone get its data faster? Well, this is the normal way you’ll get the data from the phone to your server


```
phone -> public internet -> your server

```


If you have a CDN which owns / has “peering agreements” on a lot of cool network infrastructure, then you could potentially have


```
phone -> public internet -> Sydney computer -> magic CDN internet -> your server

```


no public internet for you! You can buy MAGICAL FANCY INTERNET for your users to get to your server on.


Basically CDNs have a bunch of routing tricks that they can use to make your packets go faster. One cool article about this (thanks to [Nelson Minar](https://twitter.com/nelson)) is [Fixing the internet for real time applications](http://engineering.riotgames.com/news/fixing-internet-real-time-applications-part-ii) – it’s not about CDNs but it is about a games company building a bunch of network infrastructure. Super well written. It talks a little about BGP which is a super interesting topic that I do not yet know a lot about.


Fancy routing tricks to get you your data faster is what Cloudflare is talking about with things like [Railgun](https://blog.cloudflare.com/railgun-v5-has-landed/).


### keep your site up: DDOS mitigation


I originally phrased my question as “can a CDN help with site reliability?” If it can protect you from a DDOS attack, then, yes it can!!! This also has nothing to do with caching – if the CDN can manage to pass through all the normal requests you want to see but block all the ATTACK SCARY BAD REQUESTS, then that’s awesome and will help keep your site up.


### performance is reliability


I asked “can CDNs help with reliability or just performance?” and a few people very rightly pointed out that you can’t really completely separate those two things. As an extreme example, if your site takes 3 minutes to respond, you cannot truly fairly say that it is “up”. And a lot of timeouts kick in after just a few seconds!


### better security?


A few people mentioned that using a CDN can improve your security. Specifically – suppose a new SSL vulnerability comes out. Maybe the CDN has a super kickass security team and they’ll patch the vulnerability really quickly, and also make sure that they don’t accept SSL versions that are insecure.


This one seems a little more tenuous to me – like, I also work for a company with a really good security team. It feels kind of scary to me to not have control over when you can patch your server (apparently maybe [some Amazon ELBs took a long time to get patched for Heartbleed?](https://twitter.com/jmhodges/status/726147739520618496) See also [this HN thread](https://news.ycombinator.com/item?id=7551968)).


The other thing about security here is – governments make companies hand over information, and if you give the CDN your SSL certificate and put sensitive traffic through it, then you don’t know who they are giving your users’ data to. I used to think this was weird paranoia but I’m pretty sure by now we all know it’s a real thing to worry about.


Cloudflare apparently has a thing called [Keyless SSL](https://blog.cloudflare.com/keyless-ssl-the-nitty-gritty-technical-details/) which “allows sites to use CloudFlare without requiring them to give up custody of their private keys”. Honestly I did not understand that blog post yet but it seems interesting and highly relevant so I am linking to it anyway.


I know approximately nothing about security so I’m going to stop talking about security now.


### so do you get better reliability? (some downsides)


I was asking all these questions because I was trying to figure out if putting your website behind a CDN will make it more or less reliable. Nothing with computers is all butterflies & flowers and now we get to talk about a couple more disadvantages of putting your site behind a CDN: **configuration problems** and **the CDN going down**.


First, configuration problems. I only know like 3 things about CDNs as of this week but I do know that they’re pretty tricky to configure. You need to set all these cache-control headers and make all these settings and connect them to your servers right and it’s easy to accidentally screw something up and bring down your site.


Second, if your site is up 99.9% of the time and the CDN is up 99.9% of the time, suddenly now your site + the CDN is only up 99.8% of the time. I can’t really find good stats on SLAs for fastly/cloudfront/cloudflare/akamai/whatever so it’s not clear to me how often CDNs usually have reliability problems. However, the more I learn about computers the more I learn to be skeptical of services other people are selling you. If you know where to find stats about this I would be super interested.


### this stuff is hard


It is apparently a pretty normal thing to put a site behind a CDN without caching it! Who knew? Not me, before today. There’s a good [talk from Etsy from 2013](https://youtu.be/HU_OZbxzgi0) about using multiple CDNs which I’ve read the slides for and need to watch.


I realized that I linked to Cloudflare a lot in this blog post. I think this is because they have a great technical blog that explains a lot of interesting stuff (like [the curious case of slow downloads](https://blog.cloudflare.com/the-curious-case-of-slow-downloads/)) so it’s easier to understand what’s going on with their products. I have never used Cloudflare for anything serious so I can’t speak to how well it actually works (though I do use it for this blog).


As usual I learned most of this stuff literally today so probably at least 5 things are wrong. Especially the security stuff.


I’m really impressed by companies with great technical blogs. And kind of jealous of the people who work for those companies. People from Cloudflare say the company lets people write on their blog about what they find interesting! This seems like an awesome strategy.
