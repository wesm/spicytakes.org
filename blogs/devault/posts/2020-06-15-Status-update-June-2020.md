---
title: "Status update, June 2020"
date: 2020-06-15
url: https://drewdevault.com/2020/06/15/Status-update-June-2020.html
slug: Status-update-June-2020
word_count: 336
---

Like last month, I am writing to you from the past, preparing this status update
a day earlier than usual. This time it’s because I expect to be busy with
planned sr.ht maintenance tomorrow, so I’m getting the status updates written
ahead of time.

aerc has seen lots of patches merged recently thanks to the hard work of
co-maintainer Reto Brunner and the many contributors who sent patches, ranging
from a scrollable folder list to improvements and bugfixes for PGP support. We
wrapped all of this up in the aerc 0.4.0 release in late May. Thanks to Reto and
all of the other contributors for their hard work on aerc!

Wayland improvements have also continued at a good pace. I’ve mentioned before
that wlroots is a crucial core component tying together a lot of different parts
of the ecosystem — DRM/KMS, GBM, OpenGL, libinput, udev, and more —
bringing together integrations for many disparate systems and providing a single
unified multiplexer for them over the Wayland protocol. Taking full advantage of
all of these systems and becoming a more perfect integration of them is a
long-term goal, and we’ve been continuing to make headway on these goals over
the past few weeks. We are working hard to squeeze every drop of performance out
of your system.

In the SourceHut world, I’ve been working mainly on GraphQL support, as well as
Alpine 3.12 upgrades (the latter being the source of the planned outage). I
wrote in some detail  [on the sourcehut.org blog](https://sourcehut.org/blog/2020-06-10-how-graphql-will-shape-the-alpha/)  about why and how
the GraphQL backends are being implemented, if you’re curious. The main
development improvements in this respect which have occured since the last
status updates are the introduction of a JavaScript-free GraphQL playground, and
a GraphQL API for meta.sr.ht. Coming improvements will include an overhaul to
authentication and OAuth2 support, and a dramatically improved approach to
webhooks. Stay tuned!

That’s all for the time being. Thank you for your support and attention, and
stay safe out there. I’ll see you next month!
