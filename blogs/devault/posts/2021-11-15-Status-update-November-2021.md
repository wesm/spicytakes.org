---
title: "Status update, November 2021"
date: 2021-11-15
url: https://drewdevault.com/2021/11/15/Status-update-November-2021.html
slug: Status-update-November-2021
word_count: 301
---

Hello again! Following a spooky month, we find ourselves again considering the
progress of our eternal march towards FOSS world domination.

I’ll first address SourceHut briefly: today is the third anniversary of the
opening of the public alpha! I have written  [a longer post for sourcehut.org](https://sourcehut.org/blog/2021-11-15-sourcehuts-third-year/) 
which I encourage you to read for all of the details.

In other news, we have decided to delay the release of our new programming
language, perhaps by as much as a year. We were aiming for February ‘22, but
slow progress on some key areas such as cryptography and the self-hosting
compiler, plus the looming necessity of the full-scale acceptance testing of the
whole language and standard library, compound to make us unsure about meeting
the original release plans. However, progress is slow but moving. We have
incorporated the first parts of AES support in our cryptography library, and
ported the language to FreeBSD. A good start on date/time support has been under
development and I’m pretty optimistic about the API design we’ve come up with.
Things are looking good, but it will take longer than expected.

[visurf](https://sr.ht/~sircmpwn/visurf)  has enjoyed quite a bit of progress
this month, thanks in large part to the help of a few new contributors. Nice
work, everyone! We could still use more help, so please swing by the #netsurf
channel on Libera Chat if you’re interested in participating. Improvements which
landed this month include configuration options, url filtering via  [awk
scripts](https://git.sr.ht/~sircmpwn/dotfiles/tree/master/bin/urlfilter) , searching through pages, and copying links on the page with the
link following tool.

Projects which received minor updates this month include scdoc, gmni, kineto,
and godocs.io. That’s it for today! My focus for the next month will be much the
same as this month: SourceHut GraphQL work and programming language work. See
you in another month!
