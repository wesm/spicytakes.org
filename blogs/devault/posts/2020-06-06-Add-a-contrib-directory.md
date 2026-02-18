---
title: "Add a \"contrib\" directory to your projects"
date: 2020-06-06
url: https://drewdevault.com/2020/06/06/Add-a-contrib-directory.html
slug: Add-a-contrib-directory
word_count: 564
---

There’s a common pattern among free- and open-source software projects to
include a “contrib” directory at the top of their source code tree. I’ve seen
this in many projects for many years, but I’ve seen it discussed only rarely
— so here we are!

The contrib directory is used as an unorganized (or, at best, lightly organized)
bin of various useful things  **contrib** uted by the community around the
software, but which is not necessarily a good candidate for being a proper part
of the software. Things in contrib should not be wired into your build system,
shouldn’t be part of your automated testing, shouldn’t be included in your
documentation, and should not be installed with your packages. contrib entries
are not supported by the maintainers, and are given only a light code review at
the most. There is no guarantee whatsoever of workitude or maintenance for
anything found in contrib.

Nevertheless, it is often useful to have such a place to put various little
scripts, config files, and so on, which provide a helpful leg-up for users
hoping to integrate the software with some third-party product, configure it to
fit nicely into an unusual environment, coax it into some unusual behavior, or
whatever else the case may be. The idea is to provide a place to drop a couple
of files which might save a future someone facing similar problems from doing
all of the work themselves. Such people can contribute back small fixes or
improvements, and the maintenance burden of such contributions lies entirely
with the users.

If the contributor wants to take on a greater maintenance burden, this kind of
stuff is better suited to a standalone project, with its own issue tracking,
releases, and so on. If you just wrote a little script and want somewhere to
drop it so that others may find it useful, then contrib is the place for you.

For a quick example, let’s consult Sway’s  [contrib
folder](https://github.com/swaywm/sway/tree/master/contrib) :

```
_incr_version
autoname-workspaces.py
grimshot
grimshot.1
grimshot.1.scd
inactive-windows-transparency.py
```

The  `_incr_version`  script is something that I use myself to help with preparing
new releases. It is a tool useful only to maintainers, and therefore is not
distributed with the project.

Looking at  `autoname-workspaces.py`  next, from which we can see that the quality
criteria is reduced for members of contrib — none of Sway’s upstream code
is written in Python, and the introduction of such a dependency would be
controversial. This script automatically changes your workspace name based on
what applications you’re running in it — an interesting workflow, but
quite different from the  OOTB  experience.

`grimshot`  is a shell script which ties together many third-party programs
(grim, slurp, wl-copy, jq, and notify-send) to make a convenient way of taking
screenshots. Adding this upstream would introduce  *a lot*  of third-party
dependencies for a minor convenience. This tool has had a bit more effort put
into it: notice that a man page is provided as well. Because the contrib
directory does not participate in the upstream build system, the contributor has
also added a pre-compiled man page so that you can skip this step when
installing it on your system.

Last, we have  `inactive-windows-transparency.py` , which is a script for making
all windows other than your focused one semi-transparent. Some people may want
this, but again, it’s not really something we’d consider appropriate for the
OOTB experience. Perfect for contrib!
