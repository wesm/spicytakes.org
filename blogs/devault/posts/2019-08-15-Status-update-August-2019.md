---
title: "Status update, August 2019"
date: 2019-08-15
url: https://drewdevault.com/2019/08/15/Status-update-August-2019.html
slug: Status-update-August-2019
word_count: 651
---

Outside my window, the morning sun can be seen rising over the land of the
rising sun, as I sip from a coffee purchased at the konbini down the street. I
almost forgot to order it, as the staffer behind the counter pointed out with a
smile and a joke that, having been told in Japanese, mostly went over my head.
It’s on this quiet Osaka morning I write today’s status update - there are lots
of existing developments to share!

Let’s start with sourcehut news. I deployed a cool feature yesterday - SSH
access to builds.sr.ht. You can now SSH into a failed build to examine the
failure and investigate the root cause. You can also get a shell on-demand for
any build image, including for experimental arm64 support. I’ll be writing a
full-length blog post going into detail about this feature later in the week.
Additionally, with contributor Ryan Chan’s help, man.sr.ht received a huge
overhaul which moved wikis out of man.sr.ht’s dedicated git subsystem and into
git.sr.ht repositories, allowing you to make your wiki out of a branch of your
main project repo or browse the git data on the web. I’ll be posting more sr.ht
news to sr.ht-announce later today if you want to hear more!

[aerc 0.2.0](https://git.sr.ht/~sircmpwn/aerc/refs/0.2.0)  has been released,
which included nearly 200 changes from 34 contributors. I’m grateful to the
community for this crazy amount of support - working together we’ll make aerc
amazing in no time. Highlights include maildir and sendmail transports, search
and filtering, support for  `mailto:`  links, tab completion, and more. We haven’t
slowed down since, and the next release already has support lined up for
notmuch, more tab completion support, and more features for mail composition. In
related news, Greg Kroah-Hartman of Linux kernel fame was kind enough to  [write
up](http://www.kroah.com/log/blog/2019/08/14/patch-workflow-with-mutt-2019/) 
details about his email workflow to help guide the direction of aerc. I’ll be
writing a follow-up post next week explaining how aerc aims to solve the
problems he lays out.

Sway and wlroots continue chugging along as well, with the release of Sway
1.2-rc1 coming earlier this week. This release adds many features from the
recent i3 4.17 release, and adds a handful of small features and bug fixes. The
corresponding wlroots release will be pretty cool, too, adding support for
direct scanout and fixing dozens of bugs. I’d like to draw your attention as
well to a cool project from the Sway community: Jason Francis’s
 [wdisplays](https://github.com/cyclopsian/wdisplays) , a GUI for arranging and
configuring displays on wlroots-based desktops. The changes necessary for it to
work will land in sway 1.2, and users building from git can try it out today.

On the DRM leasing and VR for Wayland work I was discussing in the last update,
I’m happy to share that I’ve got it working with SteamVR! I’ve written a
 [detailed blog post](/2019/08/09/DRM-leasing-and-VR-for-Wayland.html)  which
explains all of the work that went into this project, if you want to learn about
it in depth and watch some cool videos summing up the work. There’s still a lot
of work to do in negotiating the standardization of new interfaces to support
this feature in several projects, but all of the unknowns have been discovered
and answered. We will have VR on Wayland soon. I plan on making my way to the
 [Monado](https://monado.dev/)  and  [OpenXR](https://www.khronos.org/openxr)  to
help realize a top-to-bottom free software VR stack designed with Wayland in
mind. I’ll also be joining many members of the wlroots gang at
 [XDC](https://xdc2019.x.org/)  in October, where I hope to meet the people
working on OpenXR.

I’ve also invested more time into my Wayland book, because I’ve realized that at
my current pace it won’t be done any time soon. It’s now about half complete and
I’ve picked up the pace considerably. If you’re interested in helping review the
drafts, please let me know!

That’s all for today. Thank you for your continued support!
