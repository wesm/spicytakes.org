---
title: "Status update, November 2019"
date: 2019-11-15
url: https://drewdevault.com/2019/11/15/Status-update-November-2019.html
slug: Status-update-November-2019
word_count: 434
---

Today’s update is especially exciting, because today marks the 1 year
anniversary of Sourcehut  [opening it’s alpha](https://drewdevault.com/2018/11/15/sr.ht-general-availability.html)  to public
registration. I wrote a  [nice long article](https://sourcehut.org/blog/2019-11-15-sourcehut-1-year-alpha/)  which goes into
detail about what Sourcehut accomplished in 2019, what’s to come for 2020, and
it lays out the entire master plan for your consideration. Be sure to give that
a look if you have the time. I haven’t slowed down on my other projects, though,
so here’re some more updates!

I’ve been pushing hard on the VR work this month, with lots of help from Simon
Ser. We’ve put together  [wxrc](https://git.sr.ht/~sircmpwn/wxrc)  - Wayland XR
Compositor - which does what it says on the tin. It’s similar to what you’ve
seen in my earlier updates, but it’s a bespoke C project instead of a
Godot-based compositor, resulting in something much lighter weight and more
efficient. The other advantage is that it’s based on OpenXR, thanks to  [our
many](https://gitlab.freedesktop.org/monado/monado/merge_requests?scope=all&utf8=%E2%9C%93&state=all&author_username=ddevault)   [contributions](https://gitlab.freedesktop.org/monado/monado/merge_requests?scope=all&utf8=%E2%9C%93&state=all&author_username=emersion)  to Monado, an open-source
OpenXR runtime - the previous incarnations were based on SteamVR, which is
a proprietary runtime and proprietary API. We’ve also got 3D Wayland clients
working as of this week, check out our video:

This work has generated more patches for a large variety of projects - Mesa,
Wayland, Xorg, wlroots, sway, new Vulkan and OpenXR standards, and more. This
is really cross-cutting work and we’re making improvements across the whole
graphics ecosystem to support it.

Speaking of Wayland, the upcoming Sway release is looking like it’s going to be
really good. I mentioned this last month, but we’re still on track for getting
lots of great features in - VNC support, foreign toplevel management (taskbars),
input latency reductions, drawing tablet support, and more. I’m pretty excited.
I wrote chapters 9 and 9.1 for the Wayland book this month as well.

In aerc news, thanks entirely to its contributors and not to me, lots of new
features have been making their way in. Message templates are one of them, which
you can take advantage of to customize the reply and forwarded message
templates, or make new templates of your own. aerc has learned AUTH LOGIN
support as well, and received a number of bugfixes. ctools has also seen a
number of patches coming in, including support for echo, tee, and nohup, along
with several bug fixes.

In totally off-the-wall news, I’ve  [started a page](/japanese.html)  cataloguing my
tools and recommendations for Japanese language learners.

That’s all I’ve got for you today, I hope it’s enough! Thank you for your
continued love and support, I’m really proud to be able to work on these
projects for you.
