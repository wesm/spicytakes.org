---
title: "Developers: Let distros do their job"
date: 2021-09-27
url: https://drewdevault.com/2021/09/27/Let-distros-do-their-job.html
slug: Let-distros-do-their-job
word_count: 923
---

I wrote a post some time ago titled  [Developers shouldn’t distribute their own
software](https://drewdevault.com/2019/12/09/Developers-shouldnt-distribute.html) , and after a discussion on the sr.ht IRC channel today, the topic
seems worthy of renewed mention. Let’s start with this: what exactly is a
software distribution, anyway?

I use “software distribution” here, rather than “Linux distribution”, because it
generalizes better. For example, all of the major BSD systems, plus Illumos and
others besides, are software distributions, but don’t involve Linux. Some differ
further still, sitting on top of another operating system, such as Nix or
pkgsrc. What these systems all have in common is that they concern themselves
with the  *distribution*  of  *software* , and thus are a  *software distribution* .

An important trait of these systems is that they function independently of the
development of the software they distribute, and are overseen by a third party.
For the purpose of this discussion, I will rule out package repositories which
are not curated by the third-party in question, such as npm or PyPI. It is no
coincidence that such repositories often end up  [distributing](https://www.zdnet.com/article/two-malicious-python-libraries-removed-from-pypi/)   [malware](https://www.trendmicro.com/vinfo/dk/security/news/cybercrime-and-digital-threats/hacker-infects-node-js-package-to-steal-from-bitcoin-wallets) .

Software distributions are often volunteer-run and represent the interests
of the users; in a sense they are a kind of  [union](https://en.wikipedia.org/wiki/Trade_union)  of users. They handle
building your software for their system, and come to the table with
domain-specific knowledge about the concerns of the platform that they’re
working with. There are hundreds of Linux distros and each does things
differently — the package maintainers are the experts who save you the
burden of learning how all of them work. Instead of cramming all of your files
into /opt, they will carefully sort it into the right place, make sure all of
your dependencies are sorted upon installation, and make the installation of
your software a single command (or click) away.

They also serve an important role as the user’s advocate. If an update ships
which breaks a bunch of other packages, they’ll be in the trenches dealing with
it so that the users don’t face the breakage themselves. They are also the first
line of defense preventing the installation of malware on the user’s system.
Many sideloaded packages for Linux include  telemetry  spyware or adware from
the upstream distributor, which is usually patched out by the distribution.

Distributions are also working on innovative projects at the scale of the entire
software ecosystem, and are dealing with bigger picture things than you need to
concern yourself with. Here are some things which they have already solved:

* Automatic updates and dependency management
* Universal cryptographic signatures for all packages
* Worldwide distribution and bandwidth sharing via mirrors
* System-wide audits of software installed on your machine
* CVE management and patch distribution
* Long-term support

There are several areas of open research, too, such as reproducible builds or
deterministic whole-system configuration like Nix and Guix are working on. You
can take advantage of all of this innovation and research for the low price of
zero dollars by standing back and letting distros handle the distribution of
your software. It’s what they’re good at.

There are a few things you  *can*  do to make this work better.

* Ship your software as a simple tarball. Don’t ship pre-built binaries and
definitely don’t ship a “curl | bash” command. Naive users will mess up their
systems when they use them.
* Use widely adopted, standard build systems and methodologies. Use the standard
approach for your programming language. They have already been through the
gamut of distros and their operating modes are well-understood by packagers.
* [Ship good release notes](https://drewdevault.com/2021/05/19/How-to-write-release-notes.html) . Distro packagers read them! Give them a head’s
up about any important changes which might affect their distro.
* Be picky with your dependencies and try to avoid making huge dependency trees.
Bonus: this leads to better security and maintainability!
* Maintain a friendly dialogue with distro maintainers if and when they come
asking questions. They’re the expert on their distro, but you’re the expert on
your software, and sometimes you will meet to compare notes.

*See also: [FOSDEM 2018 - How To Make Package Managers Cry](https://archive.fosdem.org/2018/schedule/event/how_to_make_package_managers_cry/)*

One thing you shouldn’t do is go around asking distros to add your program to
their repos. Once you ship your tarballs, your job is done. It’s the  *users*  who
will go to their distro and ask for a new package. And users — do this! If
you find yourself wanting to use some cool software which isn’t in your distro,
go ask for it, or better yet, package it up yourself. For many packages, this is
as simple as copying and pasting a similar package (let’s hope they followed my
advice about using an industry-standard build system), making some tweaks, and
building it.

Distros are quite accessible projects, packaging is usually not that difficult.
Distributions always need more volunteers, and there are plenty of friendly
experts at your local distro who would be pleased to help you figure out the
finer details, assuming you’re prepared to stand up and do the work yourself.
Once you get used to it, making and submitting a new package can take as little
as 10 or 15 minutes for a simple one.

Oh, and if you are in the developer role — you are presumably also a user
of both your own software and some kind of software distribution. This puts you
in a really good position to champion it for inclusion in your own distro :)

P.S. Systems which invert this model, e.g. Flatpak, are completely missing the
point.
