---
title: "Status update, January 2022"
date: 2022-01-17
url: https://drewdevault.com/2022/01/17/Status-update-January-2022.html
slug: Status-update-January-2022
word_count: 432
---

Happy New Year! I had a lovely time in Amsterdam. No one had prepared me for the
(apparently infamous) fireworks culture of the Netherlands. I thought it was
really cool.

Our programming language continues to improve apace. Our cryptography suite now
includes Argon2, Salsa20/XSalsa20, ChaCha20/XChaCha20, and Poly1305, and based
on these functions we have added libsodium-style high-level cryptographic
utilities for AEAD and key derivation, with stream encryption, message signing
and verification, and key exchange coming soon. We have also laid out the
priorities for future crypto work towards supporting TLS, and on the way we
expect to have ed25519/x25519 and Diffie-Hellman added soon. Perhaps enough to
implement an SSH client?

I also implemented an efficient path manipulation module for the standard
library (something I would really have liked to have in C!), and progress
continues on date/time support. We also have a new MIME module (just for Media
Types, not all of MIME) and I expect a patch implementing net::uri to arrive in
my inbox soon. I also finished up cmsg support (for sendmsg and recvmsg), which
is necessary for the Wayland implementation I’m working on (and was a major pain
in the ass). I spent some time working with another collaborator, who is
developing a RISC-V kernel in our language, implementing a serial driver for the
SiFive UART, plus improving the device tree loader and UEFI support.

One of the standard library contributors also wrote a side-project to implement
 [Ray Tracing in One Weekend](https://raytracing.github.io/)  in our language:

In other words, language development has been very busy in the past few weeks.
Another note: I have prepared  [a lightning talk](https://fosdem.org/2022/schedule/event/lg_qbe/)  for FOSDEM which talks about
the backend that we’re using:  [qbe](https://c9x.me/compile) . Check it out!

In SourceHut news, we have brought on a new full-time contributor, Adnan
Maolood, thanks to  [a generous grant from NLNet](https://sourcehut.org/blog/2022-01-10-nlnet-graphql-funding/) . We also have another
full-time software engineer starting on February 1st (on our own dime), so I’m
very much looking forward to that. Adnan will be helping us with the GraphQL
work, and the new engineer will be working similarly to Simon and I on FOSS
projects generally (and, hopefully, with GraphQL et al as well). Speaking of
GraphQL, I’m putting the finishing touches on the todo.sr.ht writable API this
week: legacy webhooks. These are nearly done, and following this we need to do
the security review and acceptance testing, then we can ship. Adnan has been
hard at work on adding GraphQL-native webhooks to git.sr.ht, which should also
ship pretty soon.

That’s all for today. Thanks for reading! I’ll see you again in another month.
