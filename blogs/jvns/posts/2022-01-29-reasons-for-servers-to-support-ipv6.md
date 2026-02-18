---
title: "Reasons for servers to support IPv6"
date: 2022-01-29
url: https://jvns.ca/blog/2022/01/29/reasons-for-servers-to-support-ipv6/
slug: reasons-for-servers-to-support-ipv6
word_count: 1789
---


I’ve been having a hard time understanding IPv6. On one hand, the basics initially seem pretty
straightforward (there aren’t enough IPv4 addresses for all the devices on the
internet, so people invented IPv6! There are enough IPv6 addresses for
everyone!)


But when I try to actually understand it, I run into a lot of questions. One
question is: `twitter.com` does not support IPv6. Presumably it can’t be causing
them THAT many issues to not support it. So why *do* websites support IPv6?


I asked people on Twitter [why their servers support IPv6](https://twitter.com/b0rk/status/1487156306884636672)
and I got a lot of great answers, which I’ll summarize here. These all come
with the disclaimer that I have basically 0 experience with IPv6 so I can’t evaluate these reasons very well.


First though, I want to explain why it’s possible for `twitter.com` to not
support IPv6 because I didn’t understand that initially.


### how can you tell `twitter.com` doesn’t support IPv6?


You can tell they don’t support IPv6 is because if you look up their AAAA
record (which contains their IPv6 address), there isn’t one. Some other big
sites like `github.com` and `stripe.com` also don’t support IPv6.


```
$ dig AAAA twitter.com
(empty response)
$ dig AAAA github.com
(empty response)
$ dig AAAA stripe.com
(empty response)

```


### why does `twitter.com` still work for IPv6 users?


I found this really confusing, because I’ve always heard that lots of internet
users are forced to use IPv6 because we’ve run out of IPv4 addresses. But if
that’s true, how could twitter.com continue to work for those people without
IPv6 support? Here’s what I learned from the Twitter thread yesterday.


There are two kinds of internet service providers (ISPs):

1. ISPs who own enough IPv4 address for all of their customers
2. ISPs who don’t


My ISP is in category 1 – my computer gets its own IPv4 address, and actually
my ISP doesn’t even support IPv6 at all.


But lots of ISPs (especially outside of North America) are in category 2: they
don’t have enough IPv4 addresses for all their customers. Those ISPs handle the problem by:

- giving all of their customers a unique IPv6 address, so they can access IPv6 sites directly
- making large groups of their customers *share* IPv4 addresses. This can either be with CGNAT ("[carrier-grade NAT](https://en.wikipedia.org/wiki/Carrier-grade_NAT)") or “464XLAT” or maybe something else.


All ISPs need *some* IPv4 addresses, otherwise it would be impossible for their
customers to access IPv4-only sites like twitter.com.


### what are the reasons to support IPv6?


Now we’ve explained why it’s possible to *not* support IPv6. So why support it?
There were a lot of reasons.


### reason: CGNAT is a bottleneck


The argument that was most compelling to me was: CGNAT (carrier-grade NAT) is a
bottleneck and it causes performance issues, and it’s going to continue to get
worse over time as access to IPv4 addresses becomes more and more restricted.


Someone also mentioned that because CGNAT is a bottleneck, it’s an attractive
DDoS target because you can ruin lots of people’s internet experience just by
attacking 1 server.


Servers supporting IPv6 reduces the need for CGNAT (IPv6 users can just connect
directly!) which makes the internet work better for everyone.


I thought this argument was interesting because it’s a “public commons” /
community argument – it’s less that supporting IPv6 will make your site
specifically work better, and more that if *almost everyone* supports IPv6 then
it’ll make the experience of the internet better for everyone, especially in
countries where people don’t have easy access to IPv4 addresses.


I don’t actually know how much of an issue this is in practice.


There were lots of more selfish arguments to use IPv6 too though, so let’s get
into those.


### reason: so IPv6-only servers can access your site


I said before that most IPv6 users still have access to IPv4 through some kind
of NAT. But apparently that’s not true for everyone – some people mentioned
that they run some servers which only have IPv6 addresses and which aren’t
behind any kind of NAT. So those servers are actually totally unable to access
IPv4-only sites.


I imagine that those servers aren’t connecting to arbitrary machines that much
– maybe they only need to connect to a few hosts with IPv6 support.


But it makes sense to me that a machine should be able to access my site even
if it doesn’t have an IPv4 address.


### reason: better performance


For users who are using both IPv4 and IPv6 (with a dedicated IPv6 address and a
shared IPv4 address), apparently IPv6 is often faster because it doesn’t need
to go through an extra translation layer.


So supporting IPv6 can make the site faster for users sometimes.


In practice clients use an algorithm called “Happy Eyeballs” which tries to
figure out whether IPv4 or IPv6 will be faster and then uses whichever seems
faster.


Some other performance benefits people mentioned:

- maybe sometimes using IPv6 can get you a SEO boost because of the better performance.
- maybe using IPv6 causes you to go through better (faster) network hardware because it’s a newer protocol


### reason: resilience against IPv4 internet outages


One person said that they’ve run into issues where there was an internet outage
that only affected IPv4 traffic, because of accidental BGP poisoning.


So supporting IPv6 means that their site can still stay partially online during
those outages.


### reason: to avoid NAT issues with home servers


A few people mentioned that it’s much easier to use IPv6 with home servers –
instead of having to do port forwarding through your router, you can just give
every server a unique IPv6 address and then access it directly.


Of course, for this to work the client needs to have IPv6 support, but more and
more clients these days have IPv6 support too.


### reason: to learn about IPv6


One person said they work in security and in security it’s very important to
understand how internet protocols work (attackers are using internet
protocols!). So running an IPv6 server helps them learn how it works.


### reason: to push IPv6 forward / IPv4 is “legacy”


A couple of people said that they support IPv6 because it’s the current
standard, and so they want to contribute to the success of IPv6 by supporting
it.


A lot of people also said that they support IPv6 because they think sites that only
support IPv4 are “behind” or “legacy”.


### reason: it’s easy


I got a bunch of answers along the lines of “it’s easy, why not”. Obviously
adding IPv6 support is not easy in all situations, but a couple of reasons it
might be easy in some cases:

- you automatically got an IPv6 address from your hosting company, so all you need to do is add an `AAAA` record pointing to that address
- your site is behind a CDN that supports IPv6, so you don’t need to do anything extra


### reason: safer networking experimentation


Because the address space is so big, if you want to try something out you can
just grab an IPv6 subnet, try out some things in it, and then literally never
use that subnet again.


### reason: to run your own autonomous system (AS)


A few people said they were running their own autonomous system (I talked about what an AS is a bit in this [BGP post](https://jvns.ca/blog/2021/10/05/tools-to-look-at-bgp-routes/)). IPv4 addresses are too expensive so they bought IPv6 addresses for their AS instead.


### reason: security by obscurity


If your server *only* has a public IPv6 address, attackers can’t easily find it
by scanning the whole internet. The IPv6 address space is too big to scan!


Obviously this shouldn’t be your only security measure, but it seems like a
nice bonus – any time I run an IPv4 public server I’m always a tiny bit
surprised by how it’s constantly being scanned for vulnerabilities (like old versions of WordPress, etc).


### very silly reason: you can put easter eggs in your IPv6 address


IPv6 addresses have a lot of extra bits in them that you can do frivolous
things with. For example one of Facebook’s IPv6 addresses is
“2a03:2880:f10e:83:face:b00c:0:25de” (it has `face:b00c` in it).


### there are more reasons than I thought


That’s all I’ve learned about the “why support IPv6?” question so far.


I came away from this conversation more motivated to support IPv6 on my
(very small) servers than I had been before. But that’s because I think
supporting IPv6 will require very little effort for me. (right now I’m using a
CDN that supports IPv6 so it comes basically for free)


I know very little about IPv6 still but my impression is that IPv6 support
often isn’t zero-effort and actually can be a lot of work. For example, I have
no idea how much work it would actually be for Twitter to add IPv6 support on
their edge servers.


### supporting IPv6 can also cause problems


A friend who runs a large service told me that their service has tried to add
IPv6 support multiple times over the last 7 years, but each time it’s caused
them problems. What happened to them was:

- they advertised an AAAA record
- users would get the AAAA record and try to connect to them over IPv6
- some network equipment in the user’s ISP/internal network somewhere was broken, so the IPv6 connection failed
- as a result those users were unable to use their service


I thought it was interesting and surprising that supporting IPv6 can actually
in some cases make things *worse* for people on dual stack (IPv4 + IPv6)
networks.


### some more IPv6 questions


Here are some more IPv6 questions I have that maybe I’ll explore later:

- what are the *disadvantages* to supporting IPv6? What goes somehow wrong? (here’s one [example of an IPv6 problem](https://support.fastly.com/hc/en-us/community/posts/360040169531-I-often-can-t-access-Fastly-servers-using-HTTPS-IPv6-RST-packets-received) someone linked me to, for example)
- what are the incentives for ISPs that own enough IPv4 addresses for their customers to support IPv6? (another way of asking: is it likely that my ISP will move to supporting IPv6 in the next few years? or are they just not incentivized to do it so it’s unlikely?)
- [digital ocean](https://docs.digitalocean.com/products/networking/floating-ips/) seems to only support IPv4 floating IPs, not IPv6 floating IPs. Why not? Shouldn’t it be
*easier* to give out IPv6 floating IPs since there are more of them?
- when I try to ping an IPv6 address (like example.com’s IP `2606:2800:220:1:248:1893:25c8:1946` for example) I get the error `ping: connect: Network is unreachable`. Why? (answer: it’s because my ISP doesn’t support IPv6 so my computer doesn’t have a public IPv6 address)


This [IPv4 vs IPv6 article from Tailscale](https://tailscale.com/kb/1134/ipv6-faq/) looks interesting and answers some of these questions.
