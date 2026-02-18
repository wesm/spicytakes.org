---
title: "Status update, December 2019"
date: 2019-12-15
url: https://drewdevault.com/2019/12/15/Status-update-December-2019.html
slug: Status-update-December-2019
word_count: 807
---

It’s December 15th and it still hasn’t snowed here. Why did I move to this
godforsaken den of unholy heat and rain? I think I have chosen a latitude  *just* 
southerly enough to deprive me of the climate I yearn for. I take some comfort
in the knowledge that I’m travelling home to see the family in a couple of
weeks, and sure enough Colorado has been covered in snow for some time now.
Anyway, none of this is relevant to my work, which is what you came here for.
Let’s take a look at this past month.

I’ve started a couple of new projects this month, the first of which I call
“ [himitsu](https://git.sr.ht/~sircmpwn/himitsu) ”. The goal is to build a
key-value store for secure information like passwords, keys, and so on. The
design is inspired by Plan 9’s factotum, redesigned for Unix systems and
somewhat broader in scope. One interesting goal of himitsu is the ability for
programs to establish authenticated connections without ever handling your
secret information - for example, your email client could ask himitsu to connect
to an IMAP server, log in with your authentication details, then hand the
authenticated file descriptor to the mail reader. The key-value store can also
store things like the IMAP server address & port, your username, and so on,
meaning your mail reader could work out of the box with zero configuration. Work
on this project will be slow going, as I have to use extra care to make sure
that it’s secure and correct.

In SourceHut news, I focused mainly on two workstreams: single-sign-on and
names.sr.ht, the upcoming DNS and domain registration service. The first finally
fixes the problems with login across *.sr.ht, and now logging in once will log
you in everywhere. Other issues with internal OAuth keys expiring have been
fixed alongside these changes, and I’ve implemented a lot of improvements to
the billing system as well. All of these should address some inconveniences
which have been frustrating users for a while now. As for names.sr.ht, let’s
just share another teaser screenshot:

I also received my  [PinePhone](https://www.pine64.org/pinephone/)  this week, and
I’ve been terribly excited to work on it. I’ve already sent a few patches to
postmarketOS upstream, and intend to write more, to get sway working well as a
daily driver phone interface. “Sway Mobile” is now starting to take shape. The
first of the projects for this is the development of a touch-friendly
application launcher, which I’ve dubbed
“ [casa](https://git.sr.ht/~sircmpwn/casa) ”. Other projects I intend to work on
for Sway Mobile include a new, touch-friendly bar and lock screen, a new
on-screen keyboard program, and hopefully the development of touch bindings for
the compositor itself. I’ll be writing up my plans in more detail, along with a
review of the PinePhone itself, in a blog post next week.

In the course of this work, I also made a small library that readers may find
useful for their own projects:
 [libfdicons](https://gitlab.freedesktop.org/ddevault/fdicons) . It implements the
FreeDesktop icon specification in a single small C library, which I need for
Casa. In other Wayland news, I’ve made some modest progress on the book, and I
plan on writing more for it soon. I apologise for letting it get somewhat
sidelined while I focused on other projects. I ended up overhauling the XDG
chapter somewhat, as I found it pretty weak on a later reading. I intend to
write about seats (input) next, and will likely move the XDG chapter after the
seat chapter so things flow better. I’ve also started a new Wayland compositor,
 [sedna](https://git.sr.ht/~sircmpwn/sedna) , which aims to reach a broader
audience than Sway can, and I’ll be working on this as time permits.

Speaking of Sway, the next release (1.3) has been coming along, slowly but
surely. We’re only blocked by one change now, and with the original author busy
I’ve stepped up to offer what time I can implementing the last few changes. Once
we get that merged, I’ll start working on the release process for Sway 1.3.
Thank you for your patience

[aerc 0.3.0](https://git.sr.ht/~sircmpwn/aerc/refs/0.3.0)  was released this
month, and progress on the next version has been going strong. Improvements to
aerc have been almost entirely community driven, and I’ve only stepped in to
write a few small patches here and there. Thanks to all of the contributors for
their help! There are already quite a few changes in for 0.4.0, and more are in
review now, including many bug fixes, more sophisticated email templates,
contacts autocompletion, bulk email management, and more. All of this is thanks
to the great community which has grown around it!

That’s all the updates I have for you today. I’m still touched by the support
the community has given me to work on these projects. I could never be this
productive without your help. Thank you.
