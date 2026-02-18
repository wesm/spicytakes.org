---
title: "The future of Wayland, and sway's role in it"
date: 2017-10-09
url: https://drewdevault.com/2017/10/09/Future-of-sway.html
slug: Future-of-sway
word_count: 723
---

Today I’ve released sway
 [0.15-rc1](https://github.com/swaywm/sway/releases/tag/0.15-rc1) , the first
release candidate for the final 0.x release of sway. That’s right - after sway
0.15 will be sway 1.0. After today, no new features are being added to sway
until we complete the migration to our new plumbing library,
 [wlroots](https://github.com/swaywm/wlroots) . This has been a long time
coming, and I would love to introduce you to wlroots and tell you what to expect
from sway 1.0.

[Sway](https://github.com/swaywm/sway) is
a tiling Wayland compositor, if you didn’t know.

Before you can understand what wlroots is, you have to understand its
predecessor:  [wlc](https://github.com/Cloudef/wlc) . The role of wlc is to manage
a number of low-level plumbing components of a Wayland compositor. It
essentially abstracts most of the hard work of Wayland compositing away from the
compositor itself. It manages:

* The EGL (OpenGL) context
* DRM (display) resources
* libinput resources
* Rendering windows to the display
* Communicating with Wayland clients
* Xwayland (X11) support

It does a few other things, but these are the most important. When sway wants to
render a window, it will be told about its existence through a hook from wlc.
We’ll tell wlc where to put it and it will be rendered there. Most of the heavy
lifting has been handled by wlc, and this has allowed us to develop sway into a
powerful Wayland compositor very quickly.

However, wlc has some limitations, ones that sway has been hitting more and more
often in the past several months. To address these limitations, we’ve been
working very hard on a replacement for wlc called wlroots. The relationship
between wlc and wlroots is similar to the relationship between Pango and
Harfbuzz - wlroots is much more powerful, but at the cost of putting a lot more
work on the shoulders of sway. By replacing wlc, we can customize the behavior
of the low level components of our system.

I’m happy to announce that development on wlroots has been spectacular. Like
libweston has Weston itself, wlroots has a reference compositor called Rootston -
a simple floating compositor that lets us test and demonstrate the features of
wlroots. It is from this compositor that I write this blog post today. The most
difficult of our goals are behind us with wlroots, and we’re now beginning to
plan the integration of wlroots and sway.

All of this work has been possible thanks to a contingent of highly motivated
contributors who have done huge amounts of work for wlroots, writing and
maintaining entire subsystems far faster than I could have done it alone. I
really cannot overstate the importance of these contributors. Thanks to their
contributions, most of my work is in organizing development and merging pull
requests. From the bottom of my heart,  [thank
you](https://github.com/swaywm/wlroots/graphs/contributors) .

And for all of this hard work, what are we going to get? Well, for some time
now, there have been many features requests in sway that we could not address,
and many long-standing bugs we could not fix. Thanks to wlroots, we can see many
of these addressed within the next few months. Here are some of the things you
can expect from the union of wlroots and sway:

* Rotated displays
* Touchscreen bindings
* Drawing tablet support
* Mouse capture for games
* Fractional display scaling
* Display port daisy chaining
* Multi-GPU support

Some of these features are unique to sway even among Wayland  *and*  Xorg
desktops combined! Others, like output rotation, have been requested by our
users for a long time. I’m looking forward to the several dozen long-open GitHub
issues that will be closed in the next couple of months. This is just the
beginning, too - wlroots is such a radical change that I can’t even begin to
imagine all of the features we’re going to be able to build.

We’re sharing these improvements with the greater Wayland community, too.
wlroots is a platform upon which we intend to develop and promote open standards
that will unify the extensibility of all Wayland desktops. We’ve also been
working with other Wayland compositors, notably
 [way-cooler](https://github.com/way-cooler/way-cooler) , which are preparing to
move their own codebases to a wlroots-based solution.

My goal is to ship sway 1.0 before the end of the year. These are exciting times
for Wayland, and I hope you’re looking forward to it.
