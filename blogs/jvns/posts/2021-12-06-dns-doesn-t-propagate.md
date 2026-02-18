---
title: "DNS 'propagation' is actually caches expiring"
date: 2021-12-06
url: https://jvns.ca/blog/2021/12/06/dns-doesn-t-propagate/
slug: dns-doesn-t-propagate
word_count: 2161
---


Hello! Yesterday I [tweeted this](https://twitter.com/b0rk/status/1467585993138229248):


> I feel like the term "DNS propagation" is misleading, like you're not actually waiting for DNS records to "propagate", you're waiting for cached records to expire— 🔎Julia Evans🔍 (@b0rk) [December 5, 2021](https://twitter.com/b0rk/status/1467585993138229248?ref_src=twsrc%5Etfw)


and I want to talk about it a little more. This came up because I was showing a
friend a demo of how DNS caching works last week, and he realized that what was
happening in the demo didn’t line up with his mental model of how DNS worked.
He immediately brought this up and adjusted his mental model (“oh, DNS records are
**pulled**, not **pushed**!”). But this it got me thinking – why did my very
smart and experienced friend have an inaccurate mental model for how DNS works
in the first place?


First – I’m very tired of posts that complain about how people are “wrong” about how a
given piece of technology works without explaining why it’s helpful to be
“right”. So here’s why I like knowing how DNS works.


### having a correct mental model for DNS helps me make updates faster


A common piece of advice I see for handling DNS updates is “wait 24-48 hours”.
But I am very impatient, and I do NOT want to wait 48 hours! But if I want to
confidently ignore this advice (and I really do!!!), then I have to actually
understand how DNS works.


And it is possible to ignore this “24-48 hours” advice sometimes! It even turns
out that in some cases (like when creating a record for a new name that didn’t
have any records before), you don’t need to wait for DNS updates at all! It’s the best.


And of course, knowing how DNS works makes me much more confident debugging
DNS problems when things go wrong, which always feels good.


Now that I’ve hopefully made a case for why this is interesting to understand, let’s talk about how DNS updates work!


### DNS is pull, not push


When you make a DNS request (for example when you type `google.com` in your
browser), you make a request to a **DNS resolver**, like `8.8.8.8`.


When you create a DNS record for a domain, you set the DNS record on an **authoritative nameserver**.


There are 2 ways you could imagine this working:

1. When an authoritative nameserver gets an update for a DNS record, it immediately starts pushing updates to every resolver it knows about **(false)**
2. The authoritative nameserver never pushes updates, it just replies with the current record when it receives a query **(true)**


In fact, if you create a DNS record, it’s possible that no DNS resolver will
ever know about it! For example, I just created a record for a subdomain of
jvns.ca that I will not tell you. Nobody will ever make a DNS query for that
subdomain (I’m not going to make one, and you can’t because I didn’t tell you
what it is!), so no resolver knows about it.


### new DNS records are actually available instantly


I just created a TXT record at `newrecord.jvns.ca` with the content “i’m a new
record”. Then a few seconds later, I ran `dig txt newrecord.jvns.ca`. And it
worked right away, even though only 10 seconds had passed. I didn’t have to
wait at all!


This is how CDNs work too – if you request a new resource that hasn’t be
requested before, you’ll get it right away.


### why DNS updates take time: caching


But when you update a DNS record, it *is* slow! So why is that, if records
don’t need time to get pushed out? Well, DNS resolvers like `8.8.8.8` cache DNS
records.


And if those cached records are still valid, they’ll never request a new
record! So a DNS update doesn’t fully take effect until **all cached versions
of that record have expired**. When people say “we’re waiting for DNS to propagate”, what they
actually mean is “we’re waiting for cached records to expire”.


You might think that if you have a record where the TTL is 60, resolvers will
cache it for 60 seconds, so you just need to wait 60 seconds for the change to
be applied. But that would be too easy! So let’s talk about a few reasons that
caches could take a longer time to expire (like an hour or a day).


**slow update reason 1: some resolvers ignore TTLs**


We said before that for a DNS update to fully take effect, all cached versions
of that record need to expire. In theory, the TTL (“time to live”) on the
record determines how long resolvers cache your record before. But that would
be too easy :(


Instead, very rudely, some resolvers will ignore your TTL and just cache your
record for as long as you feel like! Like 24 hours!


So your DNS records updates might take more time to take effect than you’d
expect from the TTL.


**slow update reason 2: negative DNS caching**


If you query for a DNS record that **doesn’t exist**, your resolver might cache the **absence** of that record.
This has happened to me a lot of times and it’s always super frustrating – here’s how it goes:

1. I visit `something.mydomain.com` before creating the DNS record
2. I create the record
3. Then I visit it again. But it doesn’t work for a long time!!! Except after some mysterious amount of time it suddenly starts working?? Why???


One day recently I decided to actually find out why this was happening, found a
Stack Overflow answer talking about it, and of course the answer is in a DNS
RFC! The [RFC for negative caching](https://www.rfc-editor.org/rfc/rfc2308)
says that the TTL for negative caching is “the minimum of the MINIMUM field of
the SOA record and the TTL of the SOA itself”.


Let’s see what that is for subdomains of `jvns.ca`:


```
$ dig soa jvns.ca 
jvns.ca.		3600	IN	SOA	art.ns.cloudflare.com. dns.cloudflare.com. 2264245811 10000 2400 604800 3600

```


It’s the minimum of the SOA TTL (3600) and the
last number in the SOA record’s value (3600). So negative caching will happen
for an hour. And sure enough, the last time I caused this problem for myself, I
waited an hour and everything worked! Hooray!


While testing this, I noticed that Cloudflare’s resolver (1.1.1.1) doesn’t seem
to do negative DNS caching, but my ISP’s resolver does. Weird!


**slow update reason 3: browser and OS caching**


DNS resolvers aren’t the only place DNS records are cached – your browser and
OS might also be caching DNS records!


For example, in Firefox I sometimes need to press Ctrl+Shift+R to force reload
a page after a DNS change, even if the TTL has expired and there’s a new record
available. So Firefox seems to cache a little more aggressively than my DNS
resolver does.


**slow update reason 4: nameserver records are cached for a long time**


Just making changes to DNS records is normally relatively fast, as long as you
have a short TTL. But changing your domain’s nameservers can take more time. This is because to change your nameservers, 2 things have to happen:

1. Your registrar has to tell your TLD’s nameservers about the new nameservers for your domain (I don’t know exactly how long this takes or why it takes time, but it’s not instant!)
2. Resolvers have cached records for your nameserver, and those records need to expire. The TTL on those records is usually something like 1 day, so this can easily take a day.


For example, I just changed the nameservers for a domain I don’t use 5 minutes
ago, and step 1 isn’t even done yet!


### DNS resolvers are a bit like CDNs


If you already know how content delivery networks work, here’s an analogy! The
way DNS resolver caching works is similar to how CDN caching work in a couple of ways:

1. they both have an origin server (for DNS, the authoritative name server, for CDNs, the HTTP origin)
2. they both expire their caches at some point (for DNS, when the TTL expires or maybe later if that’s the resolver’s policy, and for CDNs based on the HTTP `Cache-Control` header, or whatever the CDN’s policy is)


There are differences too – for example, CDNs usually have a way to purge
records (which is VERY useful), and DNS often don’t. Though
8.8.8.8 seems to have a [“flush cache” feature](https://developers.google.com/speed/public-dns/cache). And CDNs are
much more centralized. DNS resolvers are much more difficult to work with
because there are thousands of different DNS resolvers run by different
organizations and running different software and there’s no way to control what
they do directly.


### the term “DNS propagation” feels misleading to me


I feel like the widespread use of the term “DNS propagation” is a little…
misleading? I’m not going to pretend to have a better term, but the reason that
so many people have an incorrect mental model of how DNS works isn’t because
they’re dumb – the “propagation” terminology we use to talk about why DNS
updates are slow implies an incorrect mental model!  No wonder people are
confused!


For most programmers, “there are a bunch of cached records you have
no control over and you need to wait for them to expire” is a pretty normal and
approachable concept! We deal with caching all the time, and we all
know why it’s frustrating to deal with. So it seems to me like if we used a
term that’s more accurate, people would default to a more correct model of how
DNS works.


Of course, I’m not sure that the term “DNS propagation” is *why* people like my
friend end up with an incorrect mental model for how DNS works. That’s a strong
statement and I don’t have a lot of evidence for it! But I did get quite a few
of responses to my original tweet saying that just that 1 sentence (“you’re not
actually waiting for DNS records to “propagate”, you’re waiting for cached
records to expire”) cleared up some confusion for them.


And I’m definitely not the first person to think that the term “propagation” is
misleading. A couple of examples:

- [DNS propagation does not exist](https://www.nslookup.io/blog/dns-propagation-does-not-exist/)
- this [DNS propagation checker](https://www.whatsmydns.net/#) says on its
homepage “While technically DNS **does not propagate**, this is the term that
people have become familiar with…”


### okay, DNS records actually do “propagate”.


Okay, so if DNS record don’t “propagate”, why do we use the term “DNS
propagation?”. There must be a reason, right? Well, I [posted on twitter about
this actually](https://twitter.com/b0rk/status/1467585993138229248), and a few
people mentioned that DNS records actually *do* get “pushed out”. But pushing
out these changes is pretty fast and it’s not why DNS updates are slow.


My understanding of this is that:

1. If you run a big authoritative DNS server, you want to run it globally so
that people can get DNS responses quickly no matter where they are in the
world
2. When there’s an update, it needs to get synced to all the other
authoritative servers globally, and that syncing takes time


But this delay isn’t what people are referring to when they talk about “DNS
propagation”. My guess is that in the vast majority of cases, this propagation
delay is at most a couple of minutes.  I’ve never actually seen this delay
happening in practice when I’ve set a DNS record.


And when people talk about “DNS propagation”, they’re basically always talking
about waiting for cached records to expire, which can easily take hours or
days.


### maybe we use the term “propagation” for historical reasons?


In the 90s, maybe DNS records really did take multiple hours to get
“propagated” and pushed out, and so it was more accurate to use the term
“propagation” to describe why you needed to wait? And maybe that’s why we still
use the term “propagation” to talk about the reason for DNS delays? I have no
idea how DNS worked in the 90s though.


### this terminology is probably here to stay


I’m not trying to say here that people should stop using the term “DNS
propagation” to talk about waiting for cached records to expire. I’m probably
going to keep using it sometimes – it’s a very widely used term that a lot of
people recognize! And if everyone in the conversation already has an accurate
understanding of how DNS works, using the term “DNS propagation” of course
isn’t going to suddenly make people forget how DNS actually works :)


But I do think it’s important to recognize when terms we use are potentially
misleading. I think I’m going to be more careful about using it in the
future, especially when explaining DNS to people who don’t have a good
understanding of it yet.


### that’s all!


I hope that this helps make DNS less mysterious to some of you!


Thanks to Aditya, Taylor, and Hazem for their comments on a draft of this post
