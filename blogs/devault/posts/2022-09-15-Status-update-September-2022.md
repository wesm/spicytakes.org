---
title: "Status update, September 2022"
date: 2022-09-15
url: https://drewdevault.com/2022/09/15/Status-update-September-2022.html
slug: Status-update-September-2022
word_count: 227
---

I have COVID-19 and I am halfway through my stockpile of tissues, so I’m gonna
keep this status update brief.

In Hare news, I finally put the last pieces into place to make  [cross
compiling](https://harelang.org/blog/2022-09-06-cross-builds-with-hare/)  as easy as possible. Nothing else particularly world-shattering
going on here. I have a bunch of new stuff in my patch queue to review once I’m
feeling better, however, including bigint stuff — a big step towards
TLS support. Unrelatedly, TLS support seems to be progressing upstream in qbe.
(See what I did there?)

[powerctl](https://git.sr.ht/~sircmpwn/powerctl)  is a small new project I wrote
to configure power management states on Linux. I’m pretty pleased with how it
turned out. It makes for a good  [case study](https://drewdevault.com/2022/08/28/powerctl-a-hare-case-study.html)  on Hare for systems programming.

In Helios, I have been refactoring the hell out of everything, rewriting or
redesigning large parts of it from scratch. Presently this means that a lot of
the functionality which was previously present was removed, and is being slowly
re-introduced with substantial changes. The key is reworking these features to
take better consideration of the full object lifecycle — creating,
copying, and destroying capabilities. An improvement which ended up being useful
in the course of this work is adding address space IDs (PCIDs on x86_64), which
is going to offer a substantial performance boost down the line.

Alright, time for a nap. Bye!
