---
title: "Announcing first-class Mercurial support on Sourcehut"
date: 2019-04-15
url: https://drewdevault.com/2019/04/15/Announcing-first-class-hg-support-on-sourcehut.html
slug: Announcing-first-class-hg-support-on-sourcehut
word_count: 289
---

I’m pleased to announce that the final pieces have fallen into place for
 [Mercurial](https://www.mercurial-scm.org/)  support on
 [SourceHut](https://sourcehut.org) , which is now on-par with our git offering.
Special thanks are owed to SourceHut contributor Ludovic Chabant, who has been
instrumental in adding Mercurial support to SourceHut. You may have heard about
it while this was still experimental - but I’m happy to tell you that we have
now completely integrated Mercurial support into SourceHut! Want to try it out?
Check out  [the tutorial](https://man.sr.ht/tutorials/set-up-account-and-hg.md) .

Mercurial support on SourceHut includes all of the trimmings, including CI
support via  [builds.sr.ht](https://builds.sr.ht)  and email-driven collaboration
on  [lists.sr.ht](https://lists.sr.ht) . Of course, it’s also 100%
free-as-in-freedom, open source software ( [hosted on
itself](https://hg.sr.ht/~sircmpwn/hg.sr.ht) ) that you can  [deploy on your own
servers](https://man.sr.ht/hg.sr.ht/installation.md) . We’ve tested hg.sr.ht
on some of the largest Mercurial repositories out there, including
mozilla-central and NetBSD src. The NetBSD project in particular has been very
helpful, walking us through their CVS to Hg conversion and stress-testing
hg.sr.ht with the resulting giant repositories. I’m looking forward to working
more with them in the future!

The Mercurial community is actively innovating their software, and we’ll be
right behind them. I’m excited to provide a platform for elevating the Mercurial
community. There weren’t a lot of good options for Mercurial fans before
SourceHut. Let’s fix that together! SourceHut will be taking a more active role
in the Hg community, just like we have for git, and together we’ll build a great
platform for software development.

I’ll see you in Paris in May, at the  [inaugural Mercurial
conference](https://www.mercurial-scm.org/pipermail/mercurial/2019-April/051196.html) !

Hg support on SourceHut was largely written by members of the Mercurial
community. If there are other version control communities interested in
SourceHut support, please  [reach out](mailto:~sircmpwn/sr.ht-dev@lists.sr.ht) !
