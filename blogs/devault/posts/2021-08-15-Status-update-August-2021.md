---
title: "Status update, August 2021"
date: 2021-08-15
url: https://drewdevault.com/2021/08/15/Status-update-August-2021.html
slug: Status-update-August-2021
word_count: 341
---

Greetings! It’s shaping up to be a beautiful day here in Amsterdam, and I have
found the city much to my liking so far. If you’re in Amsterdam and want to grab
a beer sometime, send me an email! I’ve been making a lot of new friends here.
Meanwhile, I’ve also enjoyed a noticable increase in my productivity levels.
Let’s go over the month’s accomplishments.

First, I have spent most of my time on the programming language project. I
mentioned in the last update that we broke ground on a codegen rewrite, and
yesterday all of our tests finally passed and I merged it. The new design is
much better, and we should be able to simplify it even further still when we
write the  hosted compiler 
in the near future. This will also give us a better basis for a small number of
experiments we’d like to do before finalizing the language design. Some other
improvements include fleshing out our floating point math support library, a
base64 module, a poll module, and parallel DNS resolution.

In SourceHut news, we shipped the  [lists.sr.ht GraphQL API](https://man.sr.ht/lists.sr.ht/graphql.md) . Future work will
expand support for thread parsing and implement write operations. Presently, I
am also working on a design for GraphQL-native webhooks, targetting meta.sr.ht
for the initial release. sr.ht packages for Alpine 3.14 were now made available,
and planned maintenance two weeks ago was the first of two fleet-wide rollouts
of the upgrades to sr.ht hosted — the next is scheduled for tomorrow.

These two projects are my primary focus right now, and they’re both making good
progress. In the coming month, I hope to address a few language design questions
and build a more sophisticated I/O abstraction for the standard library. On
sr.ht, I plan on expanding the GraphQL-native webhooks prototype and hopefully
shipping it to one of the GQL APIs, along with starting on another major GQL
support movement — either write support for lists.sr.ht, or the initial
paste.sr.ht GQL API.

That’s all I have to share today! Thanks for tuning in.
