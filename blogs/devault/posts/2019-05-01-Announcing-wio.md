---
title: "Announcing Wio: A clone of Plan 9's Rio for Wayland"
date: 2019-05-01
url: https://drewdevault.com/2019/05/01/Announcing-wio.html
slug: Announcing-wio
word_count: 372
---

For a few hours here and there over the past few months, I’ve been working on a
side project:  [Wio](https://wio-project.org) . I’ll just let the (3 minute)
screencast do the talking first:

**Note** : this video begins with several seconds of grey video. This is normal.

In short, Wio is a Wayland compositor based on wlroots which has a similar look
and feel to Plan 9’s Rio desktop. It works by running each application in its
own nested Wayland compositor, based on  [Cage](https://www.hjdskes.nl/projects/cage/)  - yet another wlroots-based
Wayland compositor. I used Cage in  [last week’s RDP article](https://drewdevault.com/2019/04/23/Using-cage-for-a-seamless-RDP-Wayland-desktop.html) , but
here’s another cool use-case for it.

The behavior this allows for (each window taking over its parent’s window,
rather than spawning a new window) has been something I wanted to demonstrate on
Wayland for a very long time. This is a good demonstration of how Wayland’s
fundamentally different and conservative design allows for some interesting
use-cases which aren’t possible at all on X11.

I’ve also given Wio some nice features which are easy thanks to wlroots, but
difficult on Plan 9 without kernel hacking. Namely, these are multihead support,
HiDPI support, and support for the wlroots layer shell protocol. Several other
wlroots protocols were invited to the party, useful for taking screenshots,
redshift, and so on. Layer shell support is particularly cool, since programs
like swaybg and waybar work on Wio.

In terms of Rio compatability, Wio has a ways to go. I would seriously
appreciate help from users who are interested in improving Wio. Some notably
missing features include:

* Any kind of filesystem resembling Rio’s window management filesystem. In
theory this ought to be do-able with FUSE, at least in part (/dev/text might
be tough).
* Running every application in its own namespace, for double the Plan 9
* Hiding/showing windows (that menu entry is dead)
* Joint improvements with Cage to bring greater support for Wayland features,
like client-side window resize/move, fullscreen windows, etc
* Damage tracking to avoid re-rendering everything on every frame, saving
battery life and GPU time

If you’re interested in helping, please join the IRC channel and say hello:
 [#wio on irc.freenode.net](http://webchat.freenode.net/?channels=%23wio&uio=MTA9dHJ1ZSYxMT0xNzQmMTM9ZmFsc2U4c) . For Wio’s source code and other
information, visit the website at  [wio-project.org](https://wio-project.org) .
