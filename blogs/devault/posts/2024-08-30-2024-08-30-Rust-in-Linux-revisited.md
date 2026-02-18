---
title: "Rust for Linux revisited"
date: 2024-08-30
url: https://drewdevault.com/2024/08/30/2024-08-30-Rust-in-Linux-revisited.html
slug: 2024-08-30-Rust-in-Linux-revisited
word_count: 1260
---

> *Ugh. Drew’s blogging about Rust again.*

– You

I promise to be nice.

Two years ago, seeing the Rust-for-Linux project starting to get the ball
rolling, I wrote “ [Does Rust belong in the Linux kernel?](https://drewdevault.com/2022/10/03/Does-Rust-belong-in-Linux.html) ”, penning a
conclusion consistent with  [Betteridge’s law of headlines](https://en.wikipedia.org/wiki/Betteridge's_law_of_headlines) . Two years on we
have a lot of experience to draw on to see how Rust-for-Linux is actually playing
out, and I’d like to renew my thoughts with some hindsight – and more
compassion. If you’re one of the Rust-for-Linux participants burned out or
burning out on this project, I want to help. Burnout sucks – I’ve been there.

The people working on Rust-for-Linux are incredibly smart, talented, and
passionate developers who have their eyes set on a goal and are tirelessly
working towards it – and, as time has shown, with a great deal of patience.
Though I’ve developed a mostly-well-earned reputation for being a fierce critic
of Rust, I do believe it has its place and I have a lot of respect for the work
these folks are doing. These developers are ambitious and motivated to make an
impact, and Linux is undoubtedly the highest-impact software in the world, and
in theory Linux is enthusiastically ready to accept motivated innovators into
its fold to facilitate that impact.

At least in theory. In practice, the Linux community is the wild wild west, and
sweeping changes are infamously difficult to achieve consensus on, and this is
by far the broadest sweeping change ever proposed for the project. Every
subsystem is a private fiefdom, subject to the whims of each one of Linux’s
1,700+ maintainers, almost all of whom have a dog in this race. It’s herding
cats: introducing Rust effectively is one part coding work and ninety-nine parts
political work – and it’s a lot of coding work. Every subsystem has its own
unique culture and its own strongly held beliefs and values.

The consequences of these factors is that Rust-for-Linux has become a burnout
machine. My heart goes out to the developers who have been burned in this
project. It’s not fair. Free software is about putting in the work, it’s a
classical do-ocracy… until it isn’t, and people get hurt. In spite of my
critiques of the project, I recognize the talent and humanity of everyone
involved, and wouldn’t have wished these outcomes on them. I also have sympathy
for many of the established Linux developers who didn’t exactly want this on
their plate… but that’s neither here nor there for the purpose of this post,
and any of those developers and their fiefdoms who went out of their way to make
life  *difficult*  for the Rust developers above and beyond what was needed to
ensure technical excellence are accountable for these shitty outcomes. 1

So where do we go now?

Well, let me begin by re-iterating something from my last article on the
subject: “I wish [Rust-for-Linux] the best of luck and hope to see them
succeed”. Their path is theirs to choose, and though I might advise a moment to
rest before diving headfirst into this political maelstrom once again, I support
you in your endeavours if this is what you choose to do. Not my business. That
said, allow me to humbly propose a different path for your consideration.

Here’s the pitch: a motivated group of talented Rust OS developers could build a
Linux-compatible kernel, from scratch, very quickly, with no need to engage in
LKML politics. You would be astonished by how quickly you can make meaningful
gains in this kind of environment; I think if the amount of effort being put
into Rust-for-Linux were applied to a new Linux-compatible OS we could have
something production ready for some use-cases within a few years.

Novel OS design is hard: projects like  [Redox](https://www.redox-os.org/)  are working on this, but it
will take a long time to bear fruit and research operating systems often have to
go back to the drawing board and make major revisions over and over again before
something useful and robust emerges. This is important work – and near to my
heart – but it’s not for everyone. However, making an OS which is based on a
proven design like Linux is  *much*  easier and can be done very quickly. I worked
on my own novel OS design for a couple of years and it’s still stuck in design
hell and badly in need of being rethought; on the other hand I wrote a passable
Unix clone alone in less than 30 days.

Rust is a great fit for a large monolithic kernel design like Linux. Imagine
having the opportunity to implement something like the dcache from scratch in
Rust, without engaging with the politics – that’s something a small group of
people, perhaps as few as one, could make substantial inroads on in a short
period of time taking full advantage of what Rust has on offer. Working towards
compatibility with an existing design can leverage a much larger talent pool
than the very difficult problem of novel OS design, a lot of people can manage
with a copy of the ISA manual and a missive to implement a single syscall in a
Linux-compatible fashion over the weekend. A small and motivated group of
contributors could take on the work of, say, building out io_uring compatibility
and start finding wins fast – it’s a lot easier than designing io_uring from
scratch. I might even jump in and build out a driver or two for fun myself, that
sounds like a good opportunity for me to learn Rust properly with a fun project
with a well-defined scope.

Attracting labor shouldn’t be too difficult with this project in mind, either.
If there was  *the*  Rust OS project, with a well-defined scope and design (i.e.
aiming for Linux ABI compatibility), I’m sure there’s a lot of people who’d jump
in to stake a claim on some piece of the puzzle and put it together, and the
folks working on Rust-for-Linux have the benefit of a great deal of experience
with the Linux kernel to apply to oversight on the broader design approach.
Having a clear, well-proven goal in mind can also help to attract the same
people who want to make an impact in a way that a speculative research project
might not. Freeing yourselves of the LKML political battles would probably be a
big win for the ambitions of bringing Rust into kernel space. Such an effort
would also be a great way to mentor a new generation of kernel hackers who are
comfortable with Rust in kernel space and ready to deploy their skillset to the
research projects that will build a next-generation OS like Redox. The labor
pool of serious OS developers badly needs a project like this to make that
happen.

So my suggestion for the Rust-for-Linux project is: you’re burned out and that’s
awful, I feel for you. It might be fun and rewarding to spend your recovery
busting out a small prototype Unix kernel and start fleshing out bits and pieces
of the Linux ABI with your friends. I can tell you from my own experience doing
something very much like this that it was a very rewarding burnout recovery
project for me. And who knows where it could go?

Once again wishing you the best and hoping for your success, wherever the path
ahead leads.

1. Yes, I saw that video, and yes, I expect much better from you in the
future, Ted. That was some hostile, toxic bullshit. ↩︎
