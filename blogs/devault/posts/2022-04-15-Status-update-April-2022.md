---
title: "Status update, April 2022"
date: 2022-04-15
url: https://drewdevault.com/2022/04/15/Status-update-April-2022.html
slug: Status-update-April-2022
word_count: 724
---

This month marked my first time filing taxes in two countries, and I can assure
you it is the worst. I am now a single-issue voter in the US: stop taxing
expats! You can get some insight into the financials of SourceHut in the
recently-published  [financial report](https://sourcehut.org/blog/2022-04-08-2021-financial-report/) . But let’s get right into the fun stuff:
free software development news.

There was some slowdown from me this month thanks to all of the business and
financial crap I had to put up with, but I was able to get some cool stuff done
and many other contributors have been keeping things moving. I’ll start by
introducing a new/old project: Himitsu.

Essentially, Himitsu is a secret storage system whose intended use-case is to
provide features like password storage and SSH agent functionality. It draws
much of its inspiration from Plan 9’s Factotum. You may have stumbled upon an
 [early prototype](https://git.sr.ht/~sircmpwn/himitsu.old)  on git.sr.ht which introduces the basic idea and included
the start of an implementation in C. Ultimately I shelved this project for want
of a better programming language to implement it with, and then I made a better
programming language to implement it with. Over the past two weeks, I have
implemented something similar to where the C codebase was left, in fewer than
half the lines of code and much less than half the time. Here’s a little peek at
what works now:

```
[12:18:31] taiga ~/s/himitsu $ ./himitsud 
Please enter your passphrase to unlock the keyring: 
[2022-04-15 12:18:56] himitsud running
^Z[1]+  Stopped                    ./himitsud
[12:18:57] taiga ~/s/himitsu $ bg
[1] ./himitsud
[12:18:58] taiga ~/s/himitsu $ nc -U ~/.local/state/himitsu/socket 
add proto=imap host=example.org user=sir@cmpwn.com password!="Hello world!"
^C
[12:19:12] taiga ~/s/himitsu $ ls ~/.local/share/himitsu/
2849c1d5-61b3-4803-98cf-fc57fe5f69a6  index  key
[12:19:14] taiga ~/s/himitsu $ cat ~/.local/share/himitsu/index
YNfVlkORDX1GmXIfL8vOiiTgBJKh47biFsUaKrqzfMP2xfD4B9/lqSl2Y9OtIpVcYzrNjBBZOxcO81vNQdgnvxQ+xaCKaVpQS4Dh6DyaY0/lpq6rfowTY5GwcI155KkmTI4z1ABOVkL4z4XDsQ2DEiqClcQE5/+CxsQ/U/u9DthLJRjrjw==
[12:19:19] taiga ~/s/himitsu $ fg
./himitsud
^C[2022-04-15 12:19:22] himitsud terminated
[12:19:22] taiga ~/s/himitsu $ ./himitsud 
Please enter your passphrase to unlock the keyring: 
Loaded key proto=imap host=example.org user=sir@cmpwn.com password!=2849c1d5-61b3-4803-98cf-fc57fe5f69a6
[2022-04-15 12:19:29] himitsud running
^C[2022-04-15 12:19:31] himitsud terminated
[12:19:33] taiga ~/s/himitsu $ find . -type f | xargs wc -l | tail -n1
  895 total
```

This project is progressing quite fast and I hope to have it working for some
basic use-cases soon. I’ll do a dedicated blog post explaining how it works and
why it’s important later on, though it will remain mostly under wraps until the
language is released.

Speaking of the language, there were a number of exciting developments this
month. Two major standard library initiatives were merged: regex and datetime.
The regex implementation is simple, small, and fast, targeting POSIX ERE as a
reasonably sane conservative baseline regex dialect. The datetime implementation
is quite interesting as well, and it provides a pretty comprehensive API which
should address almost all use-cases for timekeeping in our language with a
robust and easy-to-use API. As a bonus, and a little flex at how robust our
design is, we’ve included support for Martian time. I’m very pleased with how
both of these turned out.

```
use datetime;
use fmt;
use os;
use time::chrono;

export fn main() void = {
	const now = datetime::in(chrono::MTC, datetime::now());
	fmt::printf("Current Martian coordinated time: ")!;
	datetime::format(os::stdout, datetime::STAMP, &now)!;
	fmt::println()!;
};
```

Other recent improvements include support for signal handling, glob, aes-ni, and
net::uri. Work has slowed down on cryptography — please get in touch if
you’d like to help. Many readers will be happy to know that there are rumblings
about possibly going public soon; after a couple more milestones we’ll be having
a meeting to nail down the most urgent priorities before going public and then
we’ll get this language into your hands to play with.

I also started a bittorrent daemon in this language, but it’s temporarily
blocked until we sort out HTTP/TLS. So, moving right along: SourceHut news?
Naturally I will leave most of it for the “what’s cooking” post, but I’ll offer
you a little tease of what we’ve been working on: GraphQL. We landed support
this month for GraphQL-native webhooks in todo.sr.ht, as well as some new
improvements to the pages.sr.ht GQL API. hg.sr.ht is also now starting to see
some polish put on its GraphQL support, and some research is underway on GraphQL
Federation. Very soon we will be able to put a bow on this work.

That’s all for today! Thanks again for reading and for your ongoing support. I
appreciate you!
