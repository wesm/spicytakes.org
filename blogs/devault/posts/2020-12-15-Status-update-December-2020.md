---
title: "Status update, December 2020"
date: 2020-12-15
url: https://drewdevault.com/2020/12/15/Status-update-December-2020.html
slug: Status-update-December-2020
word_count: 305
---

Happy holidays! I hope everyone’s having a great time staying at home and not
spending any time with your families. It’s time for another summary of the
month’s advances in FOSS development. Let’s get to it!

One of my main focuses has been on sourcehut’s API 2.0 planning. This month, the
meta.sr.ht and git.sr.ht GraphQL APIs have shipped feature parity with the REST
APIs, and the RFC 6749 compatible OAuth 2.0 implementation has shipped. I’ve
broken ground on the todo.sr.ht GraphQL API — it’ll be next. Check out the
 [GraphQL docs on man.sr.ht](https://man.sr.ht/graphql.md)  if you want to kick
the tires.

I also wrote a little tool this month called
 [mkproof](https://git.sr.ht/~sircmpwn/mkproof) , after brainstorming some ways to
allow sourcehut signups over Tor without enabling abuse. The idea is that you
can generate a challenge (mkchallenge), give it to a user who generates a proof
for that challenge (mkproof), and then verify their proof is correct. Generating
the proof is computationally expensive and resistant to highly parallel attacks
(e.g. GPUs), and takes tens of minutes of work — making it unpractical for
spammers to register accounts in bulk, while still allowing Tor users to
register with their anonymity intact.

On the Gemini front, patches from Mark Dain, William Casarin, and Eyal Sawady
have improved  [gmnisrv](https://git.sr.ht/~sircmpwn/gmnisrv)  in several respects
— mainly bugfixes — and  [gmnlm](https://git.sr.ht/~sircmpwn/gmni) 
has grown the “<n>|” command, which pipes the Nth link into a shell
command. Thanks are due to Alexey Yerin as well, who sent a little bugfix with
redirect handling.

The  [second draft of the BARE
specification](https://datatracker.ietf.org/doc/draft-devault-bare/)  was
submitted to the IETF this month. Will revisit it again in several weeks. John
Mulligan has also sent several patches improving go-bare — thanks!

scdoc 1.11.0 was released this month, with only minor bug fixes.

That’s all for now! I’ll see you in a month.
