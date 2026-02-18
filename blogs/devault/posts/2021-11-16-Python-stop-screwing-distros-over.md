---
title: "Python: Please stop screwing over Linux distros"
date: 2021-11-16
url: https://drewdevault.com/2021/11/16/Python-stop-screwing-distros-over.html
slug: Python-stop-screwing-distros-over
word_count: 658
---

> Linux distributions? Oh, those things we use to bootstrap our Docker
> containers? Yeah, those are annoying. What were you complaining about again?

The Python community is obsessed with reinventing the wheel, over and over and
over and over and over and over again. distutils, setuptools, pip, pipenv, tox,
flit, conda, poetry, virtualenv, requirements.txt, setup.py, setup.cfg,
pyproject.toml… I honestly can’t even list all of the things you have to deal
with. It’s a disaster.

This comic is almost 4 years old and it has become much worse since. Python is a
mess. I really want to like Python. I have used it for many years and in many
projects, including SourceHut, which was predominantly developed in Python. But
I simply can’t handle it anymore, and I have been hard at work removing Python
from my stack.

This has always been a problem with Python, but in the past few years everyone
and their cousin decided to “solve” it by building another mess which is totally
incompatible with all of the others, all of the “solutions” enjoying varying
levels of success in the community and none of them blessed as the official
answer.

I manage my Python packages in the only way which I think is sane: installing
them from my Linux distribution’s package manager. I maintain a few dozen Python
packages for Alpine Linux myself. It’s from this perspective that, throughout
all of this turmoil in Python’s packaging world, I have found myself feeling
especially put out.

Every one of these package managers is designed for a reckless world in which
programmers chuck packages wholesale into ~/.pip, set up virtualenvs and pin
their dependencies to 10 versions and 6 vulnerabilities ago, and ship their
computers directly into production in Docker containers which aim to do the
minimum amount necessary to make their user’s private data as insecure as
possible.

None of these newfangled solutions addresses the needs of any of the distros,
despite our repeated pleas. They all break backwards compatibility with our
use-case and send our complaints to /dev/null. I have seen representatives from
every Linux distro making repeated, desperate pleas to Python to address their
concerns, from Debian to Arch to Alpine to NixOS, plus non-Linux distros like
FreeBSD and Illumos. Everyone is frustrated. We are all struggling to deal with
Python right now, and Python is not listening to us.

What is it about Linux distros that makes our use-case unimportant? Have we
offered no value to Python over the past 30 years? Do you just feel that it’s
time to shrug off the “legacy” systems we represent and embrace the brave new
world of serverless cloud-scale regulation-arbitrage move-fast-and-break-things
culture of the techbro startup?

Distros are feeling especially frustrated right now, but I don’t think we’re
alone. Everyone is frustrated with Python packaging. I call on the PSF to sit
down for some serious, sober engineering work to fix this problem. Draw up a
list of the use-cases you need to support, pick the most promising initiative,
and put in the hours to make it work properly, today and tomorrow. Design
something you can stick with and make stable for the next 30 years. If you have
to break some hearts, fine. Not all of these solutions can win. Right now,
upstream neglect is destroying the Python ecosystem. The situation is grave, and
we need strong upstream leadership right now.

P.S. PEP-517 and 518 are a start, but are very disappointing in how little they
address distro problems. These PEPs are designed to tolerate the proliferation
of build systems, which is exactly what needs to stop. Python ought to stop
trying to avoid hurting anyone’s feelings and pick one. Maybe their
decision-making framework prevents this, if so, the framework needs to be
changed.

P.P.S. There are a lot of relevant xkcds that I wanted to add. Here’s the ones I
left out:

* [https://xkcd.com/1988/](https://xkcd.com/1988/)
* [https://xkcd.com/927/](https://xkcd.com/927/)

Further reading:  [Developers: Let distros do their job](https://drewdevault.com/2021/09/27/Let-distros-do-their-job.html)
