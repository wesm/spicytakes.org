---
title: "Status update, July 2019"
date: 2019-07-15
url: https://drewdevault.com/2019/07/15/Status-update-July-2019.html
slug: Status-update-July-2019
word_count: 765
---

Today I received the keys to my new apartment, which by way of not being
directly in the middle of the city 1  saves me a decent chunk of money - and
allows me to proudly announce that I have officially broken even on doing free
software full time! I owe a great deal of thanks to all of you who have  [donated
to support my work](https://drewdevault.com/donate)  or purchased a paid
 [SourceHut](https://sourcehut.org)  account. I’ve dreamed of sustainably working
on free software for a long, long time, and I’m very grateful for all of your
support in helping realize that dream. Now let me share with you what your money
has bought over the past month!

First, my  [make a blog](https://drewdevault.com/make-a-blog)  offer has closed
for the time being, and the world is now 13 blogs richer for it. Be sure to
check them out! I have also started a mailing list for tech writers: the  [free
writers club](https://lists.sr.ht/~sircmpwn/free-writers-club) , which I
encourage anyone using free software to blog about technology to join for
editorial advice, software recommendations, and periodic reminders to keep
writing. The offer to get paid for your own new blog will reopen in the future,
keep an eye out!

As far as projects are concerned, lots of good stuff this month. aerc has been
making excellent progress. We just pulled in the first batch of patches adding
maildir support, and will soon have sendmail and mbox support as well. We’ve
also begun on mouse support, and you can now click to switch between tabs. The
initial patches for tab completion have also been added. Additional changes
include an :unsubscribe command to unsubscribe from marketing emails and mailing
lists, basic search functionality, OAuth IMAP authentication, changing config
options at runtime, and DNS lookups to complete your settings in the new account
wizard more quickly. Building more upon these features, and a handler for mailto
links, are the main blockers for aerc 0.2.0.

In Wayland news, VR work continues. I’ve taken on the goal of implementing DRM
leasing for Wayland, which will allow VR applications to take exclusive control
over the headset’s graphical resources from Wayland compositor. A similar
technology exists for X11, and I’ve written a Wayland protocol for the same
purpose on Wayland. I’ve also written a Vulkan extension to utilize this
protocol in Vulkan’s WSI layer. I’ve written implementations of these for
wlroots, sway, mesa, and the radv (AMD) Vulkan driver. The result: a working VR
demo on Sway (audio warning):

There’s still some details to sort out on the standardization of these
extensions, which are under discussion now. In the coming weeks I hope to have
an implementation for Xwayland (which will get working games based on Steam’s
OpenVR runtime), and get a proof-of-concept of a VR-driven Wayland compositor
based on the demo shown in the previous status update. Exciting stuff!

I’ve also had time to write a few more chapters for my Wayland book, which I’ll
be speeding up my work on. I’ll soon be leaving for an extended trip to Japan,
and on these grueling flights I’ll have plenty of time to work on it. In
additional Wayland news, we’ve been chugging along with small bugfixes and
improvements to wlroots and sway, and implementing more plumbing work to round
out our implementation of everything. Our work continues to evolve into the most
robust Wayland implementation available today, and I can only see it getting
stronger.

On SourceHut, I have plenty of developments to share, but will leave the details
for the  [sr.ht-announce mailing
list](https://lists.sr.ht/~sircmpwn/sr.ht-announce) . The most exciting news is
that  [Alpine Linux](https://alpinelinux.org) , my favorite Linux distribution,
has completed their mailing list infrastructure migration to  [their own
lists.sr.ht instance](https://lists.alpinelinux.org) ! I’ve also been hard at
work expanding lists.sr.ht’s capabilities to this end. The other big piece of
news was announced on my blog last week:  [code
annotations](https://drewdevault.com/2019/07/08/Announcing-annotations-for-sourcehut.html) .
All of our services have also been upgraded to Alpine 3.10, and the Alpine
mirror reorganized a bit to make future upgrades smooth.  There’s all sorts of
other goodies to share, but I’ll leave the rest for the sr.ht-announce post
later today.

All sorts of other little things have gotten done, like sending patches upstream
for kmscube fixes, minor improvements to scdoc, writing a new build system for
mrsh, improvements to openring… but I’m running out of patience and I imagine
you are, too. Again I’m eternally grateful for your support: thank you. I’ll see
you again for the next status update, same time next month!

1. I can see city hall out the window of my old apartment ↩︎
