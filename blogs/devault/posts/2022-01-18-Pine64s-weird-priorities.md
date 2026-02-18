---
title: "Pine64 should re-evaluate their community priorities"
date: 2022-01-18
url: https://drewdevault.com/2022/01/18/Pine64s-weird-priorities.html
slug: Pine64s-weird-priorities
word_count: 830
---

Pine64 has a really interesting idea: make cheap hardware with low margins, get
it into the hands of the FOSS community, and let them come up with the software.
No one has ever done this before, at least not on this scale, and it’s a really
neat idea! Pine64 is doing a lot to support the FOSS community bringing up its
hardware, but I’m afraid that I have to ask them to do a bit more.

There’s a handful of different roles that need to be filled in on the software
side of things to get this ecosystem going. Ordered from most to least
important, these are (broadly speaking) as follows:

1. Implementing and upstreaming kernel drivers, u-Boot support, etc
2. Building out a robust telephony stack for Linux
3. Building a mobile user interface for Linux
4. Maintaining distros that tie it all together

Again, this is ordered from most to least important, but in practice, the
ecosystem prioritizes them in reverse. Pine64 themselves contribute no labor to
any of these focus areas, and though they provide some funding, they provide it
from the bottom of this list up, putting most of it into distros and very little
into the kernel, bootloaders, or telephony. This is nice, but… why fund the
distros at all? Distros are not the ones getting results in these focus areas.
Their job is to  *distribute*  the results of community efforts.

Don’t get me wrong, the distros do an important job and they ought to get the
funding they need, but this is just creating fragmentation in the ecosystem. As
one example, we could be installing the Linux distribution of our choice on the
Pinebook Pro using a standard aarch64 UEFI ISO installer, just like we do for
any other laptop, if someone spent a couple of weeks upstreaming the last 6
patches to mainline Linux and put together a suitable u-Boot payload to flash on
the SPI flash chip. But, instead of one working solution for everyone, we have
20+ Linux distros publishing Pine64-specific images to flash to microSD cards.

The favorites, which is apparently Manjaro, 1  compete for funding and then
spend it each according to their own discretion working on the same problems. If
we instead spent it on the focus areas directly, then Manjaro and all of the
other distros would benefit from this work for free. The telephony stack is
equally important, and equally sharable between distros, but isn’t really
getting any dedicated funding. You can’t have a phone without telephony. The
mobile UI is also important, but it’s the easiest part to build, and a working
phone with a shitty UI is better than a phone with a pretty UI that doesn’t
work.

The work is getting done, to be fair, but it’s getting done very slowly. Many of
the distros targetting Linux for mobile devices have people working on the
important focus areas, but as a matter of necessity: to accomplish their goals
when no one else is working on these problems, they had to become experts and
divide their limited volunteer time between distro maintenance and software
development. As a result, they’ve become experts with specific allegiances and
incentives, and though there’s some patch sharing and collaboration between
distros, it’s done informally across a dozen independent organizational
structures with varying degrees of collaboration based on a model which was
stapled onto an inherently backwards system of priorities. In a system with
limited resources (funding, developer time, etc), these inefficiencies can be
very wasteful.

After I got my hands on the PineNote hardware, I quickly understood that it was
likely going to suffer even moreso from this problem. A course change is called
for if Pine64 wants to maximize their odds of success with their current and
future product lines. I think that the best strategic decision would be to hire
just one full-time software developer to specifically focus on development and
upstreaming in Linux mainline, u-Boot mainline, ModemManager, etc, and on
writing docs, collaborating with other projects, and so on. This person should
be figuring out how to get generalized software solutions to unlock the
potential of the hardware, focusing on getting it to the right upstreams, and
distributing these solutions to the whole ecosystem.

It’s  *awesome*  that Pine64 is willing to financially support the FOSS community
around their devices, and as the ones actually selling the devices, they’re the
only entity in this equation with the budget to actually do so. Pine64 is doing
some really amazing work! However, a better financial strategy is called for
here. Give it some thought, guys.

1. I will go on the record as saying that Manjaro Linux is a bad Linux
distribution and a bad place to send this money. They have a history of
internal corruption, a record of questionable spending, and a plethora of
technical issues and problematic behavior in the FOSS ecosystem. What limited
budget there is to go around was wasted in their hands. ↩︎
