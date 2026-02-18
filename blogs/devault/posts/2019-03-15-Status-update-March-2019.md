---
title: "Status update, March 2019"
date: 2019-03-15
url: https://drewdevault.com/2019/03/15/Status-update-March-2019.html
slug: Status-update-March-2019
word_count: 1037
---

My todo list is getting completed at a pace it’s never seen before, and growing
at a new pace, too. This full-time FOSS gig is really killing it! As the good
weather finally starts to roll in, it’s time for March’s status update. Note: I
posted updates  [on Patreon](https://www.patreon.com/sircmpwn/posts)  before, but will start posting here
instead. This medium doesn’t depend on a proprietary service, allows for richer
content, and is useful for my supporters who support my work via other donation
platforms.

Sway 1.0 has been released!    I wrote a  [detailed
write-up](/2019/03/11/Sway-1.0-released.html)  on the release and our future
plans separately, which I encourage you to read if you haven’t already. However,
I do have some additional progress to share outside of the big sway 1.0 news.
In the last update, I mentioned that I got a Librem 5 devkit from Guido
Günther 1  at FOSDEM. My plans were to get this up and running with sway and
start improving touch support, and I’ve accomplished both:

As you can see, I also got  [postmarketOS](https://postmarketos.org/)  running,
and I love it - I hope to work with them a lot in the future. The  [first
patch](https://github.com/swaywm/sway/pull/3711)  for improving touch support in
sway has landed and I’ll be writing more in the future. I also sent some patches
to Purism’s  [virtboard](https://source.puri.sm/Librem5/virtboard)  project, an
on-screen keyboard, making it more useful for Sway users. I hope to make an OSK
of my own at some point, with multiple layouts, CJK support, and client-aware
autocompletion, in the future. Until then, an improved virtboard is a nice
stop-gap :) I’ve also been working on wlroots a bit, including  [a patch adding
remote desktop support](https://github.com/swaywm/wlroots/pull/1578) .

In other Wayland news, I’ve also taken a part time contract to build a module
integrating wlroots with the  [Godot game engine](https://godotengine.org/) :
 [gdwlroots](https://git.sr.ht/~sircmpwn/gdwlroots) . The long-term goal is to
build a VR compositor based on Godot and develop standards for Wayland
applications to have 3D content. 100% of this work is free software (MIT
licensed) and will bring improvements to both the wlroots and Godot ecosystems.
Next week I’ll be starting work on adding a Wayland backend to Godot so that
Godot-based games can run on Wayland compositors directly. Here’s an example
compositor running on Godot:

<video
src="/l.sr.ht/9bV-.webm"
autoplay muted loop controls
style=“max-width: 100%;”

I’ve also made some significant progress on
 [aerc2](https://git.sr.ht/~sircmpwn/aerc2) . I have fleshed out the command
subsystem, rigged up keybindings, and implemented the message list, and along
with it all of the asynchronous communication between the UI thread, network
thread, and mail server. I think at this point most of the unknowns are solved
with aerc2, and the rest just remains to be implemented. I’m glad I chose to
rewrite it from C, though my love for C still runs deep. The Go ecosystem is
much better suited to the complex problems and dependency tree of software like
aerc, plus has a nice concurrency model for aerc’s async design. 2  The next
major problem to address is the embedded terminal emulator, which I hope to
start working on soon.

aerc2’s progress is a great example of my marginalized projects
becoming my side projects, as my side projects become my full-time job, and thus
all of them are developing at a substantially improved pace. The productivity
increase is pretty crazy. I’m really thankful to everyone who’s supporting my
work, and excited to keep building crazy cool software thanks to you.

I was meaning to work on RISC-V this month, but I’ve been a little bit
distracted by everything else. However, there has been some discussion about how
to approach upstreaming and I’m planning on tackling this next week. I also
spent some time putting together a custom 1U I can install in my datacenter for
a more permanent RISC-V setup. Some of this is working towards getting RISC-V
ready for builds.sr.ht users to take advantage of - that relay is for cutting
power to the board to force a reboot when it misbehaves - but a lot of this is
also useful for my own purposes in porting musl & Alpine Linux.

One problem I’m still trying to solve is the microSD card. I don’t want to run
untrusted builds.sr.ht code when that microSD card is plugged in. I’ve been
working on some prototyping (breaking out the old soldering iron) to make a
microSD… thing, which I can plug into this and physically cut VCC to the
microSD card with that relay I have rigged up. This is pretty hard, and my
initial attempts were unsuccessful. If anyone knowledgable about this has ideas,
please get in touch.

Outside of RISC-V, I have been contributing to Alpine Linux a lot more lately in
general. I adopted the sway & wlroots packages, have been working on improved
PyQt support, cleaning up Python packages, clearing out the nonfree MongoDB
packages, and more. I also added a bunch of new packages for miscellaneous
stuff, including alacritty, font-noto-cjk, nethack, and Simon Ser’s
 [go-dkim](https://github.com/emersion/go-dkim)  milter. Most importantly,
however, I’ve started
 [planning](https://wiki.alpinelinux.org/wiki/Python_package_policies)  and
 [discussing](https://lists.alpinelinux.org/alpine-devel/6465.html)  a Python
overhaul project in aports with the Alpine team, which will including cleaning
up all of the Python patches and starting on Python 2 removal. I depend a lot on
Alpine and its Python support, so I’m excited to be working on these
improvements!

I have some Sourcehut news as well. Like usual, there’ll be a detailed
Sourcehut-specific update posted to the
 [sr.ht-announce](https://lists.sr.ht/~sircmpwn/sr.ht-announce)  mailing list
later on. With Ludovic Chabant’s help, there have been continued improvements to
Mercurial support, notably adding builds.sr.ht integration as of yesterday.
Thanks Ludovic! We’ve also been talking to some NetBSD folks who may be
interested in using Sourcehut to host the NetBSD code once they finish their
CVS->Hg migration, and we’ve been improving the performance for large
repositories during their experiments on sr.ht.

There’s a bunch more going on with Sourcehut - paste.sr.ht, APIs, a command line
interface for those APIs, webhooks, and more still - check out the email on
sr.ht-announce later. That’s all I have for you today. Thank you for your
support, and until next time!

1. A Purism employee that works closely with wlroots on the Librem 5 ↩︎
2. “aerc” stands for “asynchronous email reading client”, after all. ↩︎
