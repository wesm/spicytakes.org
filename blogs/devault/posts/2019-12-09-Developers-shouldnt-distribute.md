---
title: "Developers shouldn't distribute their own software"
date: 2019-12-09
url: https://drewdevault.com/2019/12/09/Developers-shouldnt-distribute.html
slug: Developers-shouldnt-distribute
word_count: 664
---

An oft-heard complaint about Linux is that software distribution often takes
several forms: a Windows version, a macOS version, and… a Debian version, an
Ubuntu version, a Fedora version, a CentOS version, an openSUSE version… but
these complaints miss the point. The true distributable form for Linux software,
and rather for Unix software in general, is a .tar.gz file containing the source
code.

**Note** : This article presumes that proprietary/nonfree software is irrelevant,
and so should you.

That’s not to imply that end-users should take this tarball and run  `./configure && make && sudo make install`  themselves. Rather, the responsibility for
end-user software distribution is on the distribution itself. That’s why we call
it a  *distribution* . This relationship may feel like an unnecessary middleman to
the software developer who just wants to get their code into their user’s hands,
but on the whole this relationship has far more benefits than drawbacks.

As the old complaint would suggest, there are hundreds of variants of Linux
alone, not to mention the BSD flavors and any novel new OS that comes out next
week. Each of these environments has its own take on how the system as a whole
should be organized and operate, and it’s a fools’ errand for a single team to
try and make sense of it all. More often than not, software which tries to field
this responsibility itself sticks out like a sore thumb on the user’s operating
system, totally flying in the face the conventions set out by the distribution.

Thankfully, each distro includes its own set of volunteers dedicated to this
specific job: packaging software for the distribution and making sure it
conforms to the norms of the target environment. This model also adds a set of
checks and balances to the system, in which the distro maintainers can audit
each other’s work for bugs and examine the software being packaged for
anti-features like telemetry or advertisements, patching it out as necessary.
These systems keep malware out of the repositories, handle distribution of
updates, cryptographically verifying signatures, scaling the distribution out
across many mirrors - it’s a robust system with decades of refinement.

The difference in trust between managed software repositories like Debian,
Alpine Linux, Fedora, and so on; and unmanaged software repositories like PyPI,
npm, Chrome extensions, the Google Play store, Flatpak, etc — is starkly
obvious. Debian and its peers are full of quality software which integrates well
into the host system and is free of malware. Unmanaged repositories, however,
are  [constant sources](https://www.zdnet.com/article/two-malicious-python-libraries-removed-from-pypi/)  for crapware and malware. I don’t trust
developers to publish software with my best interests in mind, and developers
shouldn’t ask for that level of trust. It’s only through a partnership with
distributions that we can build a mutually trustworthy system for software
distribution.

Some developers may complain that distros ship their software too slowly, but
you shouldn’t sweat it. End-user distros ship updates reasonably quickly, and
server distros ship updates at a schedule which meets the user’s needs. This
inconsistent pace in release schedules among free software distributions is a
feature, not a bug, and allows the system to work to the needs of its specific
audience. You should use a distro that ships updates to  *you*  at the pace you
wish, and let your users do the same.

So, to developers: just don’t worry about distribution! Stick a tarball on your
release page and leave the rest up to distros. And to users: install packages
from your distro’s repositories, and learn how its packaging process works so
you can get involved when you find a package missing. It’s not as hard as it
looks, and they could use your help. For my part, I work both as a developer,
packager, and end-user, publishing my software as tarballs, packaging some of it
up for my  [distro of choice](https://pkgs.alpinelinux.org/packages?name=&branch=edge&arch=x86_64&maintainer=Drew+DeVault) , report bugs to other maintainers, and field
requests from maintainers of other distros as necessary. Software distribution
is a social system and it works.
