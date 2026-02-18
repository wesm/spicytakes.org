---
title: "Sway & wlroots at XDC 2018"
date: 2018-09-30
url: https://drewdevault.com/2018/09/30/Sway-wlroots-at-XDC-2018.html
slug: Sway-wlroots-at-XDC-2018
word_count: 736
---

Just got my first full night of sleep after the return flight from Spain after
attending  [XDC 2018](https://xdc2018.x.org/) . It was a lot of fun! I attended
along with four other major wlroots contributors. Joining me were  [Simon Ser
(emersion)](https://github.com/emersion)  (a volunteer) and  [Scott Anderson
(ascent12)](https://github.com/ascent12)  of
 [Collabora](https://www.collabora.com/) , who work on both
 [wlroots](https://github.com/swaywm/wlroots)  and
 [sway](https://github.com/swaywm/sway) .  [ongy](https://github.com/ongy)  works on
wlroots,  [hsroots](https://github.com/swaywm/hsroots) , and
 [waymonad](https://github.com/waymonad/waymonad) , and joined us on behalf
of  [IGEL](https://www.igel.com/) . Finally, we were joined by  [Guido Günther
(agx)](https://github.com/agx)  of  [Purism](https://puri.sm/) , who works with us
on wlroots and on the Librem 5. This was my first time meeting most of them
face-to-face!

wlroots was among the highest-level software represented at XDC. Most of the
attendees are hacking on the kernel or mesa drivers, and we had a lot to learn
from each other. The most directly applicable talk was probably VKMS (virtual
kernel mode setting), a work-in-process kernel subsystem which will be useful
for testing the complex wlroots DRM code. We had many chances to catch up with
the presenters after their talk to learn more and establish a good
relationship. We discovered from these chats that some parts of our DRM code
was buggy, and have even started onboarding some of them as contributors to sway
and wlroots.

We also learned a lot from the other talks, in ways that will pay off over time.
One of my favorites was an introduction to the design of Intel GPUs, which went
into a great amount of detail into how the machine code for these GPUs worked,
why these design decisions make them efficient, and their limitations and
inherent challenges. Combined with other talks, we got a lot of insight into the
design and function of mesa, graphics drivers, and GPUs. These folks were very
available to us for further discussion and clarification after their talks, a
recurring theme at XDC and one of the best parts of the conference.

Another recurring theme at XDC was talks about how mesa is tested, with the most
in-depth coverage being on Intel’s new CI platform. They provide access to Mesa
developers to test their code on  *every*  generation of Intel GPU in the course
of about 30 minutes, and brought some concrete data to the table to show that it
really works to make their drivers more stable. I took notes that you can expect
to turn into builds.sr.ht features! And since these folks were often available
for chats afterwards, I think they were taking notes, too.

I also met many of the driver developers from AMD, Intel, and Nvidia; all of
whom had interesting insights and were a pleasure to hang out with. In fact,
Nvidia’s representatives were the first people I met! On the night of the
kick-off party, I led the wlroots clan to the bar for beers and introduced
myself to the people who were standing there - who already knew me from my
writings critical of Nvidia. Awkward! A productive conversation ensued
regardless, where I was sad to conclude that we still aren’t going to see any
meaningful involvement in open source from Nvidia. Many of their engineers are
open to it, but I think that the engineering culture at Nvidia is unhealthy and
that the engineers have very little influence. We made our case and brought up
points they weren’t thinking about, and I can only hope they’ll take them home
and work on gradually improving the culture.

Unfortunately, Wayland itself was somewhat poorly represented. Daniel Stone (a
Wayland & Weston maintainer) was there, and Roman Glig (of KDE), but some KDE
folks had to cancel and many people I had hoped to meet were not present. Some
of the discussions I wanted to have about protocol standardization and
cooperation throughout Wayland didn’t happen. Regardless, the outcome of XDC was
very positive - we learned a lot and taught a lot. We found new contributors to
our projects, and have been made into new contributors for everyone else’s
projects.

Big shoutout to the X Foundation for organizing the event, and to the beautiful
city of A Coruña for hosting us, and to University of A Coruña for sharing their
university - which consequently led to meeting some students there that used
Sway and wanted to contribute! Thanks as well to the generous sponsors, both for
sponsoring the event and for sending representatives to give talks and meet the
community.
