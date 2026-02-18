---
title: "Status update, October 2019"
date: 2019-10-15
url: https://drewdevault.com/2019/10/15/Status-update-October-2019.html
slug: Status-update-October-2019
word_count: 831
---

Last month, I gave you an update at the conclusion of a long series of travels.
But, I wasn’t done yet - this month, I spent a week in Montreal for  [XDC](https://xdc2019.x.org/) .
Simon Ser put up  [a great write-up](https://emersion.fr/blog/2019/xdc2019-wrap-up/)  which goes over a lot of the
important things we discussed there. It was a wonderful conference and well
worth the trip - but I truly am sick of travelling. Now, I can enjoy some time
at home, working on free and open source software.

I have a video to share today, of a workflow on git.sr.ht that I’m very excited
about: sending patchsets as emails from the web.

Sourcehut’s development plans can be described in three broad strokes: (1) make
a bunch of services (or: primitives for a development hub); (2) rig them all up
with APIs and webhooks; and (3) teach them how to talk to each other. Over the
past year, (1) and (2) are mostly complete, and (3) is now underway. Teaching
git.sr.ht and lists.sr.ht to talk to each other is an important step, because it
will give us a web-based code review flow which is backed by emails. This meets
an original design goal of Sourcehut: to build user-friendly tools on top of
existing systems.

The other end of this work is on lists.sr.ht, but for now it’s indirect: I’ve
also been working on  [pygit2](https://github.com/libgit2/pygit2/pulls?q=is%3Apr+author%3Addevault+is%3Aclosed)  fleshing out the Odb backend API, so
that I can make a pygit2 repo which is backed by the git.sr.ht API. From there,
it’ll be easy to teach lists.sr.ht about git.sr.ht - and perhaps other git
services as well.

There’s also a fourth stage of Sourcehut: giving back to the free software
community. To this end, I intend to spend Sourcehut’s profits on sponsoring
motivated and talented free software developers to work on self-directed
projects. I’m very excited to announce that there’s progress here as well:
 [Simon Ser](https://emersion.fr)  is now joining Sourcehut and will be doing just
that: self-directed free software projects. He’s written more about this on  [his
blog](https://emersion.fr/blog/2019/working-full-time-on-open-source/)  and I’ll
be writing more on  [sourcehut.org](https://sourcehut.org)  later.

Wrapping up Sourcehut news, I’ll leave you with an out-of-context screenshot of
a mockup I made this month:

Let’s move on to Wayland news. We’ve started the planning for the next sway
release, and it’s shaping up to be really cool. We expect to ship patches which
can reduce input latency to as low as 1ms, introduce the foreign toplevel
management protocol for better mate-panel support, and introduce damage tracking
to our screencopy protocol - which is being used to make a VNC server for
sway and other wlroots-based compositors; and proper drawing tablet support.
We’re also making strong headway on a long-term project to overhaul rendering
and DRM in wlroots, with the long term goal of achieving the holy grail levels
of performance on any device.

[The Wayland book](https://wayland-book.com)  is also in good shape. A lot of
people have purchased the drafts - over a hundred! Thank you for picking it up,
and please send your feedback along. I completed chapter 8 this month. I also
expect to receive the last few parts for my second POWER9 machine today, and I
plan on using this to test Wayland, Mesa, etc - on ppc64le. The  [first POWER9
machine](https://drewdevault.com/2019/10/10/RaptorCS-redemption.html)  is now provisioned and humming along in the Sourcehut
datacenter, by the way.

VR work has also been chugging along again this month. I’ve started contributing
to  [Monado](https://gitlab.freedesktop.org/monado/monado/merge_requests?scope=all&utf8=%E2%9C%93&state=merged&author_username=ddevault) , which is basically to OpenXR as Mesa is to OpenGL. I’ve
seen merged an overhaul to their build system, an overhaul for their dated
Wayland backend, and even some deeper work ensuring conformance with the OpenXR
specification. A lot of this work has also been in getting to know everyone and
planning the future of the project, as it’s still in early stages.

To quickly summarize my other various projects:

* **ctools**  has seen many small improvements and bug fixes, and has grown the
dirname, rmdir, env, and sleep utilities.
* **aerc**  has also seen small improvements and bug fixes, but has also learned
about sorting and will soon grow a threaded message list
* **chopsui**  is stirring in its sleep, and I’ve been giving some new attention
to its design problems in the hopes that the next iteration will be the
correct design for a new GUI toolkit.
* [**wshowkeys**](https://git.sr.ht/~sircmpwn/wshowkeys)  is a new little tool I
built to display your keypresses on-screen during a Wayland session, useful
for live streaming or video recording
* **9front**  has been eating some of my evenings lately, and I’ve been making
small improvements to various tools and improving Plan 9 support among some
packages in the Go ecosystem. I have more plans for this… stay tuned.

That’s all I’ve got for today. Thank you for your support! Oh, and one last
note: I’ve been invited to the  [Github sponsors
program](https://github.com/users/ddevault/sponsorship) , so if you want to
donate through it Github will match your donation for a little while. Cheers!
