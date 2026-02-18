---
title: "Bring more Tor into your life"
date: 2015-11-11
url: https://drewdevault.com/2015/11/11/Bring-more-tor-into-your-life.html
slug: Bring-more-tor-into-your-life
word_count: 441
---

[Tor](https://www.torproject.org/)  is a project that improves your privacy
online by encrypting and bouncing your connection through several nodes before
leaving for the outside world. It makes it much more difficult for someone
spying on you to know who you’re talking to online and what you’re saying to
them. Many people use it with the Tor Browser (a fork of Firefox) and only use
it with HTTP.

What some people do not know is that Tor works at the TCP level, and can be used
for any kind of traffic. There is a glaring issue with using Tor for your daily
browsing - it’s significantly slower. That being said, there are several things
you run on your computer where speed is not quite as important. I am personally
using Tor for several things (this list is incomplete):

* IRC (chat)
* Email client
* DNS lookups (systemwide)
* Downloading system updates

Anything that supports downloading through a SOCKS proxy can be used through
Tor. You can also use programs like
 [torify](https://trac.torproject.org/projects/tor/wiki/doc/TorifyHOWTO)  to
transparently wrap syscalls in Tor for any program (this is how I got my email
to use Tor).

Of course, Tor can’t help you if you compromise yourself. You should not use
bittorrent over Tor, and you should check your other applications. You should
also be using SSL/TLS/etc on top of Tor, so that exit nodes can’t be evil with
your traffic.

## Orbot

I also use Tor on my phone. I run all of my phone’s traffic through Tor, since I
don’t use the internet on my phone much. I have whitelisted apps that need to
stream video or audio, though, for the sake of speed. You can do this, too - set
up a black or whitelist of apps on your phone whose networking will be done
through Tor. The app for this is
 [here](https://guardianproject.info/apps/orbot/) .

## Why bother?

The easy answer is “secure everything”. If you don’t have a good reason to
remain insecure, you should default to secure. That argument doesn’t work on
everyone, though, so here are some others.

* Securing trivial traffic makes more noise to hide the things you care about
* You can have more peace of mind about using public WiFi networks if you’re
using Tor.
* ISPs can’t inject extra ads and tracking into things you’re using over Tor.
* The NSA targets people who use Tor. If you “have nothing to hide”, then you
can help defend those who do by adding more noise and giving agencies that
engage in illegal spying a bigger haystack. Bonus: Tor helps make sure that
even though you’re being looked at, you’re secure.
