---
title: "Status update, October 2021"
date: 2021-10-15
url: https://drewdevault.com/2021/10/15/Status-update-October-2021.html
slug: Status-update-October-2021
word_count: 573
---

On this dreary morning here in Amsterdam, I’ve made my cup of coffee and
snuggled my cat, and so I’m pleased to share some FOSS news with you. Some cool
news today! We’re preparing for a new core product launch at sr.ht, cool updates
for our secret programming language, plus news for visurf.

Simon Ser has been hard at work on expanding his  [soju](https://sr.ht/~emersion/soju/)  and  [gamja](https://sr.ht/~emersion/gamja/) 
projects for the purpose of creating a new core sourcehut product: chat.sr.ht.
We’re rolling this out in a private beta at first, to seek a fuller
understanding of the system’s performance characteristics, to make sure
everything is well-tested and reliable, and to make plans for scaling,
maintenance, and general availability. In short, chat.sr.ht is a hosted IRC
bouncer which is being made available to all paid sr.ht users, and a kind of
webchat gateway which will be offered to unpaid and anonymous users. I’m pretty
excited about it, and looking forward to posting a more detailed announcement in
a couple of weeks. In other sourcehut news, work on GraphQL continues, with
paste.sr.ht landing and todo.sr.ht’s writable API in progress.

Our programming langauge project grew some interesting features this month as
well, the most notable of which is probably reflection. I wrote  [an earlier blog
post](https://drewdevault.com/2021/10/05/Reflection.html)  which goes over this in some detail. There’s also ongoing work to
develop the standard library’s time and date support, riscv64 support is
essentially done, and we’ve overhauled the grammar for switch and match
statements to reduce a level of indentation for typical code. In the coming
weeks, I hope to see date/time support and reflection fleshed out much more, and
to see some more development on the self-hosted compiler.

Work has also continued apace on  [visurf](https://sr.ht/~sircmpwn/visurf) , which is a project I would love to
have your help with — drop me a note on #netsurf on libera.chat if you’re
interested. Since we last spoke, visurf has gained support for readline-esque
keybindings on the exline, a “follow” mode for keyboard navigation, Wayland
clipboard support, and a few other features besides. Please help! This project
will need a lot of work to complete, and much of that work is very accessible to
programmers of any skill level.

Also on the subject of Netsurf and Netsurf-adjacent work, I broke ground on
 [antiweb](https://git.sr.ht/~sircmpwn/antiweb)  this month. The goal of this project is to provide a conservative
CSS toolkit which allows you to build web interfaces which are compatible with
marginalized browsers like Netsurf and Lynx. I should be able to migrate my blog
to this framework in the foreseeable future, and ultimately the sourcehut
frontend will be overhauled with this framework.

And a collection of minor updates:

* I have been working on Alpine Linux for RISC-V again, and have upstreamed the
necessary patches to get u-Boot to bootstrap UEFI into grub for a reasonably
sane boot experience. Next up will be getting this installed onto the onboard
SPI flash so that it works more like a native firmware.
* I have tagged versions 1.0 of  [gmnisrv](https://git.sr.ht/~sircmpwn/gmnisrv)  and  [gmni](https://git.sr.ht/~sircmpwn/gmni) .
* Adnan Maolood has been hard at work on  [godocs.io](https://godocs.io)  and we should soon
expect a 1.0 of our gddo fork as well, which should make it more or less
plug-and-play to get a working godocs instance on localhost from your local
Go module cache.

That’s all for today! Take care, and thank you as always for your continued
support. I’ll see you next month!
