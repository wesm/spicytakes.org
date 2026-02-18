---
title: "Status update, August 2022"
date: 2022-08-16
url: https://drewdevault.com/2022/08/16/Status-update-August-2022.html
slug: Status-update-August-2022
word_count: 301
---

It is a blessedly cool morning here in Amsterdam. I was busy moving house
earlier this month, so this update is a bit quieter than most.

For a fun off-beat project this month, I started working on a  [GameBoy
emulator](https://git.sr.ht/~sircmpwn/hdmg)  written in Hare. No promises on when
it will be functional or how much I plan on working on it – just doing it for
fun. In more serious Hare news, I have implemented Thread-Local Storage (TLS)
for qbe, our compiler backend. Hare’s standard library does not support
multi-threading, but I needed this for Helios, whose driver library does support
threads. It will also presumably be of use for cproc once it lands upstream.

Speaking of Helios, it received the runtime components for TLS support on
x86_64, namely the handling of %fs and its base register MSR in the context
switch, and updates to the ELF loader for handling .tdata/.tbss sections.
I have also implemented support for moving and copying capabilities, which will
be useful for creating new processes in userspace. Significant progress towards
capability destructors was also made, with some capabilities — pages and
page tables in particular — being reclaimable now. Next goal is to finish
up all of this capability work so that you can freely create, copy, move, and
destroy capabilities, then use all of these features to implement a simple
shell. There is also some refactoring due at some point soon, so we’ll see about
that.

Other Hare progress has been slow this month, as I’m currently looking at a
patch queue 123 emails backed up. When I’m able to sit down and get through
these, we can expect a bunch of updates in short order.

SourceHut news will be covered in the “what’s cooking” post later today. That’s
all for now! Thanks for tuning in.
