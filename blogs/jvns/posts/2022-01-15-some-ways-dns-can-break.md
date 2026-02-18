---
title: "Some ways DNS can break"
date: 2022-01-15
url: https://jvns.ca/blog/2022/01/15/some-ways-dns-can-break/
slug: some-ways-dns-can-break
word_count: 1615
---


When I first learned about it, DNS didn’t seem like it should be THAT
complicated. Like, there are DNS records, they’re stored on a server, what’s
the big deal?


But with DNS, reading about how it works in a textbook doesn’t prepare you for
the sheer volume of different ways DNS can break your system in practice. It’s
not just caching problems!


So I [asked people on Twitter](https://twitter.com/b0rk/status/1481265429897261058) for
example of DNS problems they’ve run into, especially DNS problems that **didn’t
initially appear to be DNS problems**. (the popular “it’s always DNS” meme)


I’m not going to discuss how to solve or avoid any of these problems in this
post, but I’ve linked to webpages discussing the problem where I could find
them.


### problem: slow network requests


Your network requests are a little bit slower than expected, and it’s actually
because your DNS resolver is slow for some reason. This might be because the
resolver is under a lot of load, or it has a memory leak, or something else.


I’ve run into this before with my router’s DNS forwarder – all of my DNS
requests were slow, and I restarted my router and that fixed the problem.


### problem: DNS timeouts


A couple of people mentioned network requests that were taking 2+ seconds or 30
seconds because of DNS queries that were timing out. This is sort of the same
as “slow requests”, but it’s worse because queries can take several seconds to
time out.


Sophie Haskins has a great blog post [Misadventures with Kube DNS](https://blog.sophaskins.net/blog/misadventures-with-kube-dns/) about DNS
timeouts with Kubernetes.


### problem: ndots


A few people mentioned a specific issue where Kubernetes sets `ndots:5` in its `/etc/resolv.conf`


Here’s an example /etc/resolv.conf from [Kubernetes pods /etc/resolv.conf ndots:5 option and why it may negatively affect your application performances](https://pracucci.com/kubernetes-dns-resolution-ndots-options-and-why-it-may-affect-application-performances.html).


```
nameserver 100.64.0.10
search namespace.svc.cluster.local svc.cluster.local cluster.local eu-west-1.compute.internal
options ndots:5

```


My understanding is that if this is your `/etc/resolv.conf` and you look up
`google.com`, your application will call the C `getaddrinfo` function, and
`getaddrinfo` will:

1. look up `google.com.namespace.svc.cluster.local.`
2. look up `google.com.svc.cluster.local.`
3. look up `google.com.cluster.local.`
4. look up `google.com.eu-west-1.compute.internal.`
5. look up `google.com.`


Basically it checks if `google.com` is actually a subdomain of everything on the `search` line.


So every time you make a DNS query, you need to wait for 4 DNS queries to fail
before you can get to the actual real DNS query that succeeds.


### problem: it’s hard to tell what DNS resolver(s) your system is using


This isn’t a bug by itself, but when you run into a problem with DNS, often
it’s related in some way to your DNS resolver. I don’t know of any foolproof
way to tell what DNS resolver is being used.


A few things I know:

- on Linux, I think that most things use /etc/resolv.conf to choose a DNS
resolver. There are definitely exceptions though, for example your browser
might ignore /etc/resolv.conf and use a different DNS-over-HTTPS service
instead.
- if you’re using UDP DNS, you can use `sudo tcpdump port 53`  to see where DNS
requests are being sent. This doesn’t work if you’re using DNS over HTTPS or
DNS over TLS though.


I also vaguely remember it being even more confusing on MacOS than on Linux,
though I don’t know why.


### problem: DNS servers that return NXDOMAIN instead of NOERROR


Here’s a problem that I ran into once, where nginx couldn’t resolve a domain.

- I set up nginx to use a specific DNS server to resolve DNS queries
- when visiting the domain, nginx made 2 queries, one for an `A` record, and one for an `AAAA` record
- the DNS server returned a `NXDOMAIN` reply for the `A` query
- nginx decided “ok, that domain doesn’t exist”, and gave up
- the DNS server returned a successful reply for the `AAAA` query
- nginx ignored the `AAAA` record because it had already given up


The problem was that the DNS server should have returned `NOERROR` – that
domain *did* exist, it was just that there weren’t any `A` records for it. I
reported the bug, they fixed it, and that fixed the problem.


I’ve implemented this bug myself too, so I understand why it happens – it’s
easy to think “there aren’t any records for this query, I should return an
`NXDOMAIN` error”.


### problem: negative DNS caching


If you visit a domain before creating a DNS record for it, the **absence** of
the record will be cached. This is very surprising the first time your run into
it – I only learned about this last year!


The TTL for cache entry is the TTL of the domain’s SOA record – for example
for `jvns.ca`, it’s an hour.


### problem: nginx caching DNS records forever


If you put this in your nginx config:


```
location / {
    proxy_pass https://some.domain.com;
}

```


then nginx will resolve `some.domain.com` once on startup and never again. This
is especially dangerous if the IP address for `some.domain.com`  changes
infrequently, because it might keep happily working for months and then
suddenly break at 2am one day.


There are pretty well-known ways to fix this and this post isn’t about nginx so
I won’t get into it, but it’s surprising the first time you run into it.


Here’s a [blog post](https://medium.com/driven-by-code/dynamic-dns-resolution-in-nginx-22133c22e3ab) with a story of how this happened to someone with an AWS load balancer.


### problem: Java caching DNS records forever


Same thing, but for Java: [Apparently](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/java-dg-jvm-ttl.html)
depending on how you configure Java, “the JVM default TTL [might be] set so
that it will never refresh DNS entries until the JVM is restarted.”


I haven’t run into this myself but I asked a friend about it who writes more
Java than me and they told me that it’s happened to them.


Of course, literally any software could have this problem of caching DNS
records forever, but the main cases I’ve heard of in practice are nginx and
Java.


### problem: that entry in /etc/hosts you forgot about


Another variant on caching issues: entries in `/etc/hosts` that override your
usual DNS settings!


This is extra confusing because `dig` ignores `/etc/hosts`, so everything SEEMS
like it should be fine ("`dig whatever.com` is working!").


### problem: your email isn’t being sent / is going to spam


The way email is sent and validated is through DNS (MX records, SPF records,
DKIM records), so a lot of email problems are DNS problems.


### problem: internationalized domain names don’t work


You can register domain names with non-ASCII characters or emoji like [https://💩.la](https://%F0%9F%92%A9.la/).


The way this works with DNS is that `💩.la` gets translated into `xn--ls8h.la` with an encoding called “punycode”.


But even though there’s a clear standard for how they should work with DNS, a lot of software doesn’t handle internationalized domain names well!
There’s a fun story about this in Julian Squires’ great talk [The emoji that Killed Chrome!!](https://www.youtube.com/watch?v=UE-fJjMasec).


### problem: TCP DNS is blocked by a firewall


A couple of people mentioned that some firewalls allow UDP port 53 but not TCP
port 53. But large DNS queries need to use TCP port 53, so this can cause weird
intermittent problems that are hard to debug.


### problem: musl doesn’t support TCP DNS


A lot of applications use libc’s `getaddrinfo` to make DNS queries. musl is an
alternative to `glibc` that’s used in Alpine Docker container which doesn’t
support TCP DNS. This can cause problems if you make DNS queries where the
response would be too big to fit inside a regular DNS UDP packet (512 bytes).


I’m still a bit fuzzy on this so I might have it wrong, but my understanding of how this can break is:

1. musl’s getaddrinfo makes a DNS query
2. the DNS server notices that the response is too big to fit in a single DNS response packet
3. the DNS server returns an **empty** truncated response, expecting that the client will retry by making a TCP DNS query
4. `musl` does not support TCP so it does not retry


A blog post about this: [DNS resolution issue in Alpine Linux](https://christoph.luppri.ch/fixing-dns-resolution-for-ruby-on-alpine-linux)


### problem: round robin DNS doesn’t work with `getaddrinfo`


One way you could approach load balancing is to use “round robin DNS”. The idea
is that every time you make a DNS query, you get a different IP address.
Apparently this works if you use `gethostbyname` to make DNS queries, but it
does not work if you use `getaddrinfo` because `getaddrinfo` sorts the IP
responses it receives.


So you could run into an upsetting problem if you switch from `gethostbyname` to `getaddrinfo` behind the scenes without realising that this will break your DNS load balancing.


This is especially insidious because you might not realize that you’re
switching to `gethostbyname` to `getaddrinfo` at all – if you’re not writing a
C program, those functions calls are hidden inside some library. So it could be
part of a seemingly innocuous upgrade.


Here are a couple of pages discussing this:

- [getaddrinfo breaks round robin DNS](https://groups.google.com/g/consul-tool/c/AGgPjrrkw3g)
- [getaddrinfo with round robin DNS and happy eyeballs](https://daniel.haxx.se/blog/2012/01/03/getaddrinfo-with-round-robin-dns-and-happy-eyeballs/)


### problem: a race condition when starting a service


A problem someone [mentioned](https://mobile.twitter.com/omatskiv/status/1481305175440646148)
with Kubernetes DNS: they had 2 containers which started simultaneously and
immediately tried to resolve each other. But the DNS lookup failed because the
Kubernetes DNS change hadn’t happened yet, and then the failure was cached so
it kept failing.


### that’s all!


I’ve definitely missed some important DNS problems here, so I’d love to hear
what I’ve missed. I’d also love links to blog posts that write up examples of
these problems – I think it’s really useful to see how the problem
specifically manifests in practice and how people debugged it.
