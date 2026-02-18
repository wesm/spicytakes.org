---
title: "Linux development is distributed - profoundly so"
date: 2020-09-02
url: https://drewdevault.com/2020/09/02/Linux-development-is-profoundly-distributed.html
slug: Linux-development-is-profoundly-distributed
word_count: 857
---

The standard introduction to git starts with an explanation of what it means to
use a “distributed” version control system. It’s pointed out that every
developer has a complete local copy of the repository and can work independently
and offline, often contrasting this design with systems like SVN and CVS.  The
explanation usually stops here. If you want to learn more, consider git’s roots:
it is the version control system purpose-built for Linux, the largest and most
active open source project in the world. To learn more about the true nature of
distributed development, we should observe Linux.

Pull up your local copy of the Linux source code (you have one of those,
right? 1 ) and open the MAINTAINERS file. Scroll down to line 150 or so and
let’s start reading some of these entries.

Each of these represents a different individual or group which has some interest
in the Linux kernel, often a particular driver. Most of them have an “F” entry,
which indicates which files they’re responsible for in the source code. Most
have an “L” entry, which has a mailing list you can post questions, bug reports,
and patches to, as well as an individual maintainer (“M”) or maintainers who are
known to have expertise and autonomy over this part of the kernel. Many of them
— but, hmm, not all — also have a tree (“T”), which is a dedicated
git repo with their copy of Linux, for staging changes to the kernel. This is
common with larger drivers or with “meta” organizations, which oversee
development of entire subsystems.

However, this presents a simplified view. Look carefully at the “DRM” drivers
( [Direct Rendering Manager](https://en.wikipedia.org/wiki/Direct_Rendering_Manager) ); a group of drivers and maintainers who are
collectively responsible for graphics on Linux. There are many drivers and many
maintainers, but a careful eye will notice that there are many similarities as
well. A lot of them use the same mailing list,  [dri-devel@lists.freedesktop.org](mailto:dri-devel@lists.freedesktop.org) ,
and many of them use the same git repository:
 `git://anongit.freedesktop.org/drm/drm-misc` . It’s not mentioned in this file,
but many of them also shared the FreeDesktop bugzilla until recently, then moved
to the FreeDesktop GitLab; and many of them share the  `#dri-devel`  IRC channel
on Freenode. And again I’m simplifying — there are also many related IRC
channels and git repos, and some larger drivers like AMDGPU have dedicated
mailing lists and trees.

There’s more complexity to this system still. For example, not all of these
subsystems are using git. The Intel TXT subsystem uses Mercurial. The Device
Mapper team (one of the largest and most important Linux subsystems) uses
 [Quilt](https://savannah.nongnu.org/projects/quilt) . And like Linux DRM is a meta-project for many DRM-related subsystems
& drivers, there are higher-level meta projects still, such as driver-core,
which manages code and subsystems common to  *all*  I/O drivers. There are also
cross-cutting concerns, such as the interaction between linux-usb and various
network driver teams.

Patches to any particular driver could first end up on a domain-specific mailing
list, with a particular maintainer being responsible for reviewing and
integrating the patch, with their own policies and workflows and tooling. Then
it might flow upwards towards another subsystem with its own similar features,
and then up again towards meta-meta trees like linux-staging, and eventually to
Linus’ tree 2 . Along the way it might receive feedback from other projects if it
has cross-cutting concerns, tracing out an ever growing and shrinking bubble of
inclusion among the trees, ultimately ending up in every tree. And that’s
 *still*  a simplification — for example, an important bug fix may sidestep
all of this entirely and get applied on top of a downstream distribution kernel,
ending up on end-user machines before it’s made much progress upstream at all.

This complex  *graph*  of Linux development has code flowing smoothly between
hundreds of repositories, emails exchanging between hundreds of mailing lists,
passing through the hands of dozens of maintainers, several bug trackers,
various CI systems, all day, every day, ten-thousand fold. This is truly
illustrative of  **distributed**  software development, well above and beyond the
typical explanation given to a new git user. The profound potential of the
distributed git system can be plainly seen in the project for which it was
principally designed. It’s also plain to see how difficult it would be to adapt
this system to something like GitHub pull requests, despite how easy many who
are perplexed by the email-driven workflow wish it to be 3 . As a matter of
fact, several Linux teams are already using GitHub and GitLab and even pull or
merge requests on their respective platforms.  However, scaling this system up
to the entire kernel would be a great challenge indeed.

By the way — that MAINTAINERS file? Scroll to the bottom. My copy is
 *19,000 lines long* .

1. Okay, just in case: `git clone https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git` ↩︎
2. That’s not the only destination; for example, some patches will end up in the LTS kernels as well. ↩︎
3. If you are among the perplexed, [my interactive git send-email tutorial](https://git-send-email.io) takes about 10 minutes and is often recommended to new developers by Greg KH himself. ↩︎
