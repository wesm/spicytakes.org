---
title: "In praise of Alpine Linux"
date: 2021-05-06
url: https://drewdevault.com/2021/05/06/Praise-for-Alpine-Linux.html
slug: Praise-for-Alpine-Linux
word_count: 767
---

*Note: this blog post was originally only available via Gemini, but has been
re-formatted for the web.*

The traits I prize most in an operating system are the following:

* Simplicity
* Stability
* Reliability
* Robustness

As a bonus, I’d also like to have:

* Documentation
* Professionalism
* Performance
* Access to up-to-date software

Alpine meets all of the essential criteria and most of the optional criteria
(documentation is the weakest link), and far better than any other Linux
distribution.

In terms of simplicity, Alpine Linux is unpeered. Alpine is the only Linux
distribution that fits in my head. The pieces from which it is built from are
simple, easily understood, and few in number, and I can usually predict how it
will behave in production. The software choices, such as musl libc, are highly
appreciated in this respect as well, lending a greater degree of simplicity to
the system as a whole.

Alpine also meets expectations in terms of stability, though it is not alone in
this respect. Active development is done in an “edge” branch, which is what I
run on my main workstation and laptops. Every six months, a stable release is
cut from this branch and supported for two years, so four releases are supported
at any given moment. This strikes an excellent balance: two years is long enough
that the system is stable and predictable for a long time, but short enough to
discourage you from letting the system atrophy. An outdated system is not a
robust system.

In terms of reliability, I can be confident that an Alpine system will work
properly for an extended period of time, without frequent hands-on maintenance
or problem solving. Upgrading between releases almost always goes off without a
hitch (and usually the hitch was documented in the release notes, if you cared
to read them), and I’ve never had an issue with patch releases. Edge is less
reliable, but only marginally: it’s much more stable than, say, Arch Linux.

The last of my prized traits is robustness, and Alpine meets this as well. The
package manager, apk, is seriously robust. It expresses your constraints, and
the constraints of your desired software, and solves for a system state which is
always correct and consistent. Alpine’s behavior under pathological conditions
is generally predictable and easily understood. OpenRC is not as good, but
thankfully it’s slated to be replaced in the foreseeable future.

In these respects, Alpine is unmatched, and I would never dream of using any
other Linux distribution in production.

Documentation is one of Alpine’s weak points. This is generally offset by
Alpine’s simplicity — it can usually be understood reasonably quickly and easily
even in the absence of documentation — but it remains an issue. That being said,
Alpine has shown consistent progress in this respect in the past few releases,
shipping more manual pages, improving the wiki, and standardizing processes for
matters like release notes.

I also mostly appreciate Alpine’s professionalism. It is a serious project and
almost everyone works with the level of professionalism I would expect from a
production operating system. However, Alpine lacks strong leadership, some
trolling and uncooperative participants go unchecked, and political infighting
has occurred on a few occasions. This is usually not an impedance to getting
work done, but it is frustrating nevertheless. I always aim to work closely with
upstream on any of the projects that I use, and a professional upstream team is
a luxury that I very much appreciate when I can find it.

Alpine excels in my last two criteria: performance and access to up-to-date
software. apk is simply the fastest package manager available. It leaves apt and
dnf in the dust, and is significantly faster than pacman. Edge updates pretty
fast, and as a package maintainer it’s usually quite easy to get new versions of
upstream software in place quickly even for someone else’s package. I can expect
upstream releases to be available on edge within a few days, if not a few hours.
Access to new software in stable releases is reasonably fast, too, with less
than a six month wait for systems which are tracking the latest stable Alpine
release.

In summary, I use Alpine Linux for all of my use-cases: dedicated servers and
virtual machines in production, on my desktop workstation, on all of my laptops,
and on my PinePhone (via postmarketOS). It is the best Linux distribution I have
used to date. I maintain just under a hundred Alpine packages upstream, three
third-party package repositories, and several dozens of Alpine systems in
production. I highly recommend it.
