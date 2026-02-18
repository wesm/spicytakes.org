---
title: "Choosing a VPN service is a serious decision"
date: 2019-04-19
url: https://drewdevault.com/2019/04/19/Your-VPN-is-a-serious-choice.html
slug: Your-VPN-is-a-serious-choice
word_count: 1085
---

There’s a disturbing trend in the past year or so of various VPN companies
advertising to the general, non-technical public. It’s great that the general
public is starting to become more aware of their privacy online, but I’m not a
fan of these companies exploiting public paranoia to peddle their wares. Using
a VPN in the first place has potentially grave consequences for your privacy -
and can often be worse than not using one in the first place.

It’s true that, generally speaking, when you use a VPN, the websites you visit
don’t have access to your original IP address, which can be used to derive your
approximate location (often not more specific than your city or neighborhood).
But that’s not true of the VPN provider themselves - who can identify you much
more precisely because you used your VPN login to access the service.
Additionally, they can promise not to siphon off your data and write it down
somewhere - tracking you, selling it to advertisers, handing it over to law
enforcement - but they  *could*  and you’d be none the wiser. By routing all of
your traffic through a VPN,  *you route all of your traffic through a VPN* .

Another advantage offered by VPNs is that they can prevent your ISP from knowing
what you’re doing online. If you don’t trust your ISP but you do trust your VPN,
this makes a lot of sense. It also makes sense if you’re on an unfamiliar
network, like airport WiFi. However, it’s still quite important that you  *do* 
trust the VPN on the other end. You need to do research. What country are they
based in, and what’s their diplomatic relationship with your home country? What
kind of power the local authorities have to force them to record & disclose your
traffic? Are they backed by venture capitalists who expect infinite growth, and
will they eventually have to meet those demands by way of selling your
information to advertisers? What happens to you when their business is going
poorly? How much do you trust their security competency - are they likely to be
hacked? If you haven’t answered all of these questions yourself, then you should
not use a VPN.

Even more alarming than the large advertising campaigns which have been popular
in the past few months is push-button VPN services which are coming
pre-installed on consumer hardware and software. These bother me because they’re
implemented by programmers who should understand this stuff and know better than
to write the code. Opera now has a push-button VPN pre-bundled which is free and
tells you little about the service before happily sending all of your traffic
through it.  Do you trust a Chinese web browser’s free VPN to behave in your
best interests?  Purism also recently announced a collaboration with Private
Internet Access to ship a VPN in their upcoming Librem 5. I consider this highly
irresponsible of Purism, and actually discussed the matter at some length with
Todd Weaver (the CEO) over email. We need to stop making it easy for users to
siphon all of their data into the hands of someone they don’t know.

For anyone who needs a VPN but isn’t comfortable using one of these companies,
there are other choices. First, consider that any website you visit with HTTPs
support (identified by the little green lock in the address bar on your web
browser) is already encrypting all of your traffic so it cannot be read or
tampered with. This discloses your IP address to the operator of that website
and discloses that you visited that website to your ISP, but does not disclose
any data you sent to them, or any content they sent to you, to your ISP or any
eavesdroppers. If you’re careful to use HTTPS (and other forms of SSL for
things like email), that can often be enough. 1

If that’s not enough, the ironclad solution is
 [Tor](https://www.torproject.org/) . When you connect to a website on Tor, it (1)
hides your IP address from the website and any eavesdroppers, (2) hides who
you’re talking to from your ISP, and (3) hides what you’re talking about from
the ISP. In some cases (onion services), it even hides the origin of the service
you’re talking to from  *you* . Tor comes with its own set of limitations and
pitfalls for privacy & security, which you should  [read about and
understand](https://2019.www.torproject.org/download/download.html.en#Warning) 
before using it. Bad actors on the Tor network can read and tamper with your
traffic if you aren’t using SSL or Onion routing.

Finally, if you have some technical know-how, you can set up your own VPN. If
you have a server somewhere (or rent one from a VPS provider), you can install a
VPN on it. I suggest  [Wireguard](https://www.wireguard.com/)  (easiest, Linux
only) or  [OpenVPN](https://openvpn.net)  (more difficult, works on everything).
Once again, this comes with its own limitations. You’ll always be using a
consistent IP address that services you visit can remember to track you, and you
get a new ISP (whoever your VPS provider uses). This’ll generally route you
through commercial ISPs, though, who are much less likely to do obnoxious crap
like injecting ads in webpages or redirecting your failed DNS queries to “search
results” (i.e. more ads). You’ll need to vet your VPS provider and their ISP
with equal care.

Understand who handles your data - encrypted and unencrypted - before you share
it.  No matter your approach, you should also always install an adblocker (I
strongly recommend  [uBlock
Origin](https://github.com/gorhill/uBlock/#installation) ), stick to
HTTPS-enabled websites, and be suspicious of and diligent about every piece of
software, every browser extension, every app you install, and every website you
visit. Most of them are trying to spy on you.

Related articles:

* [VPN - a Very Precarious Narrative - Dennis Schubert](https://schub.io/blog/2019/04/08/very-precarious-narrative.html)
* [The trustworthy of VPN review sites and how affiliate programs affects their opinion](https://www.skadligkod.se/vpn/the-trustworthy-of-vpn-review-sites-and-how-affiliate-programs-affects-their-opinion/)

1. A reader points out that HTTPS can also be tampered with. If someone else administrates your computer (such as your employer), they can install custom certificates that allow them to tamper with your traffic. This is also sometimes done by software you install on your system, like antivirus software (which more times than not, is a virus itself). Additionally, anyone who can strongarm a certificate authority (state actors) may be able to issue an illegitimate certificate for the same purpose. The only communication method I know of which has no known flaws is onion routing on Tor. ↩︎
