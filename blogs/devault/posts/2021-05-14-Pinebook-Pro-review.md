---
title: "Pinebook Pro review"
date: 2021-05-14
url: https://drewdevault.com/2021/05/14/Pinebook-Pro-review.html
slug: Pinebook-Pro-review
word_count: 737
---

I received the original Pinebook for free from the good folks at Pine64 a few
years ago, when I visited Berlin to work with the KDE developers. Honestly, I
was underwhelmed. The performance was abysmal and ARM is a nightmare to work
with. For these reasons, I was skeptical when I bought the Pinebook Pro. I have
also  [spoken of my disdain for modern laptops in general before](https://drewdevault.com/2020/02/18/Fucking-laptops.html) : the state
of laptops in $CURRENTYEAR is abysmal. As such, I have been using a ThinkPad
X200, an 11 year old laptop, as my sole laptop for several years now.

I am pleased to share that the Pinebook Pro is a pleasure to use, and is likely
to finally replace the old ThinkPad for most of my needs.

Let me get the bad parts out of the way upfront: ARM is still a nightmare to
work with. I really hate this architecture. Alpine Linux’s upstream aarch64
doesn’t work with this laptop, so I have to use  [postmarketOS](http://postmarketos.org) , an Alpine
derivative, instead. I do  *like*  pmOS — on phones — but I would
definitely prefer to use Alpine upstream for a laptop use-case.  That being
said, the Pine community has been doing a very good job of working on getting
support for their devices upstream, and the situation has been steadily
improving. I expect that one of the next batches of PBPs will include an updated
u-Boot payload which will make UEFI booting possible, and Linux distros with the
necessary kernel patches upstreamed will be shipping in the foreseeable future.
This will alleviate most
of my ARM-based grievances.

The built-in speakers are also pretty tinny and weak. It has a headphone port
which works fine, though. Configuring ALSA is a chore; these SoCs tend to have
rather complicated audio setups. I have not been able to get the webcam working
(some kernel option is missing, my contact at pmOS is working on it), but I
understand that the quality is pretty poor. It can supposedly be configured to
work with a USB-C dock for an external display, but I have never got it working
and I understand that there are some kernel bits missing for this as well. The
touchpad is also pretty bad, but thankfully I use mainly keyboard-driven
software. The built-in eMMC storage is pretty small, though it can be upgraded
and I understand that there is an option to install an NVMe — at the
expense of your battery life.

Cons aside, what do I like about it? Well, many things. It’s lightweight and
thin (1.3kg), but has a nice 14" screen that feels like the right size for me.
The screen looks really nice, too. The colors look good, it works well at any
brightness level, and in most lighting situations. It’s definitely better than
the old X200 display. The keyboard is not as nice as the ThinkPad (a high bar to
meet), but it’s pretty comfortable for extended use. The two USB-3 ports and the
sole USB-C port are also nice to have. It can charge via USB-C, or via an
included DC wall wart and barrel plug. The battery lasts for 6-8 hours: way
better than my old ThinkPad.

It is an ARM machine, so the performance is not competitive with modern x86_64
platforms. It is somewhat faster than my 11-year-old previous machine, though.
It has six cores and any parallelizable job (like building code) works
acceptably fast, at least for the languages I primarily use (i.e. not Rust or
C++). It can also play back 1080p video with a  *little bit*  of stuttering, and
720p video flawlessly. Browsing the web is a bit of a chore, but it always was.
 [Sourcehut works fine](https://sourcehut.org/blog/2021-05-08-sourcehut-is-the-fastest-who-cares) .

The device is user-servicable, which I appreciate very much. It’s very easy to
take apart (a small Phillips head screwdriver is sufficient) and you can buy
individual parts from the Pine64 store to do replacements yourself.

In short, it checks most of my boxes, which is something no other laptop has
even come remotely close to in the past  **ten years** . It is the only laptop I
have ever used which makes a substantial improvement on the circa-2010 state of
the art. Because ARM is a nightmare, I’m still likely to use the old ThinkPads
for some use-cases, namely for hobby OS development and running niche operating
systems. But my Pinebook Pro is here to stay.
