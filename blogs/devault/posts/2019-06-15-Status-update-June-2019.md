---
title: "Status update, June 2019"
date: 2019-06-15
url: https://drewdevault.com/2019/06/15/Status-update-June-2019.html
slug: Status-update-June-2019
word_count: 950
---

Summer is in full swing here in Philadelphia. Last night I got great views of
Jupiter and a nearly-full Moon, and my first Saturn observation of the year.  I
love astronomy on clear Friday nights, there’s always plenty of people coming
through the city. And today, on a relaxing lazy Saturday, waiting for friends
for dinner later, I have the privilege of sharing another status report with
you.

First, I want to talk about some work I’ve done with blogs lately. On the bottom
of this article you’ll find a few blog posts from around the net. This is
populated with  [openring](https://git.sr.ht/~sircmpwn/openring) , a small Go tool
I made to fetch a few articles from a list of RSS feeds. A couple of other
people have added this to their own sites as well, and I hope to use this to
encourage the growth of a network of bloggers supporting each other without any
nonfree or centralized software. I’ll write about this in its own article in
time. I’ve also made an  [open offer](/make-a-blog)  to give $20 to anyone who
wants to make their own blog, and so far 5 new blogs have taken me up on the
offer. Maybe you’ll be the next?

Other side projects have seen some nice progress this month, too.
 [Wio](https://git.sr.ht/~sircmpwn/wio)  has received a few patches from Leon
Plickat improving the UX, and I understand more are on the way. I’m also happy
to tell you that the RISC-V musl libc port I was working on is heading upstream
and slated for inclusion in the next release! Big thanks to everyone who helped
with that, and to Rich Felker for reviewing it and assembling the final patches.
I was also able to find some time this month to contribute to
 [mrsh](https://git.sr.ht/~emersion/mrsh) , adding support for job IDs, the
 `wait` ,  `break` , and  `continue`  builtins, and a handful of other improvements.
I’m really excited about mrsh, it’s getting close to completion. My friend
Luminarys also finally released  [synapse 1.0](https://synapse-bt.org/) , a
bittorrent client that I had a  [hand in
designing](https://github.com/Luminarys/synapse/commit/ac92bb424c3d7d99905f4c0988c924001b688080#diff-d981183863e690e9f0f2bd20145a7a16) ,
and  [building](https://github.com/ddevault/receptor) 
 [frontends](https://broca.synapse-bt.org/)  for. Congrats, Lumi! This one has
been a long time coming.

Alright, now for some updates on the larger, long-term projects. The initial
pre-release of aerc  [shipped](/2019/06/03/Announcing-aerc-0.1.0.html)  two weeks
ago! Even since then it’s already attracted a flurry of patches from the
community. I’m tremendously excited about this project, I think it has heaps of
potential and a community is quickly forming to help us live up to it. Since
0.1.0 it’s already grown support for formatting the index list, swapped the
Python dependency for POSIX awk, grown temporary accounts and the ability to
view headers, and more. I’ve already started planning 0.2.0 - check out  [the
list of
blockers](https://todo.sr.ht/~sircmpwn/aerc2?search=label:%22blocker%22%20status%3Aopen) 
for a sneak peek.

The Godot+Wayland workstream has picked up again, and I’ve secured some VR
hardware (an HTC Vive) and started working on  [planning the changes
necessary](https://github.com/swaywm/wlroots/issues/1723)  for first-class VR
support on wlroots. In the future I also would like to contribute with the
OpenXR and OpenHMD efforts for bringing a full-stack free software solution for
VR. I also did a proof-of-concept 3D Wayland compositor that I intend to
translate to VR once I have the system up and running on Wayland:

In other respects, sway & wlroots have been somewhat quiet. We’ve been focusing
on small bug fixes and quality-of-life improvements, while some beefier changes
are stewing on the horizon. wlroots has seen some slow and steady progress on
refining its DRM implementation, improvements to which are going to lead to even
further improved performance and capability of the downstream compositors -
notably, direct scan-out has just been merged with the help of Scott Anderson
and Simon Ser.

In SourceHut news, the most exciting is perhaps that todo.sr.ht has grown an API
and webhooks! That makes it the last major sr.ht service to gain these features,
which unblocks a lot of other stuff in the pipeline. The biggest workstream
unblocked by this is dispatch.sr.ht, which has an design proposal for an
overhaul under discussion on the development list. This’ll open the door for
features like building patches sent to mailing lists, linking tickets to
commits, and much more. I’ve also deployed another compute server to pick up the
load as git.sr.ht grows to demand more resources, which frees up the box it used
to be on with more space for smaller services to get comfortable. I was also
happy to bring Ludovic Chabant, the driving force behind hg.sr.ht, with me to
attend a Mercurial conference in Paris, where I learned heaps about the
internals (and externals, to be honest) of Mercurial. Cool things are in store
here, too! Big thanks to the Mercurial maintainers for being so accommodating of
my ignorance, and for putting on a friendly and productive conference.

In the next month, I’m moving aerc to the backburner and turning my focus back
to SourceHut & wlroots VR. I’m getting a consistent stream of great patches for
aerc to review, so I’m happy to leave it in the community’s hands for a while.
For SourceHut, the upcoming dispatch workstream is going to be a huge boon to
the community there. On its coattails will come more powerful data import &
export tools, giving the users more ownership and autonomy over their data, and
perhaps following this will be some nice improvements to git.sr.ht. I’m also
going to try and find time to invest more in Alpine Linux on RISC-V this month.

From the bottom of my heart, thank you again for lending your support. I’ve
never been busier, happier, and more productive than I have been since working
on FOSS full-time. Let’s keep building awesome software together.
