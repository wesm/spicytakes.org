---
title: "Status update, May 2022"
date: 2022-05-16
url: https://drewdevault.com/2022/05/16/Status-update-May-2022.html
slug: Status-update-May-2022
word_count: 981
---

This was an exciting month:  [the Hare programming language](https://harelang.org)  is a secret no more!
You can now  [try out](https://harelang.org/tutorials/introduction/)  the programming language I first teased  [over a year ago](/2021/03/19/A-new-systems-language.html) 
and  [tell me what you think](mailto:sir@cmpwn.com) . I hope you like it! I’m
quite pleased with it so far.

One thing Hare has done is allow me to unshelve several projects which were
blocked pending the availability of a suitable language to write them in. I have
actually been working on several of these for a while now — and several
more are to come later — but I couldn’t share them thanks to Hare’s policy
of secrecy early in its development. Allow me to introduce you to a few
projects!

**[Helios](https://sr.ht/~sircmpwn/helios)**  is a micro-kernel for x86_64, and ideally later for aarch64 and
riscv64 as well (and possibly other targets as Hare grows additional ports). We
have a few things working, such as paging and interrupts, and as of this morning
we have entered userspace. Next up is rigging up syscalls and scheduling, then
we’re going to start fleshing out an L4-inspired API and writing some drivers in
userspace.

**[Himitsu](https://sr.ht/~sircmpwn/himitsu)**  is a secret storage system. It can act as a password manager, but
it also stores other arbitrary secret data, such as private keys. Each key is a
set of key/value pairs, some of which can be secret. This allows you to store
additional data alongside your password (such as your username or email for
login), and also supports secret data other than passwords — like SSH
keys. An extensible consent and agent protocols allow you to expand it to
support a wide variety of use-cases for secure use of secrets.

**[btqd](https://sr.ht/~sircmpwn/btqd)** , or “bittorrent queue daemon”, is (going to be) a bittorrent daemon,
but it is still very early in development. The design is essentially that of a
process supervisor which manages a queue of torrents and fires up subprocesses
to seed or leech for a set of active torrents. Each subprocess, such as btlc
(bittorrent leech client), or btsc (bittorrent seed client), can also be used
separately from the queue daemon. Further development is blocked on net::http,
which is blocked on TLS support, for tracker announce requests. I may
temporarily unblock this by shelling out to curl instead.

**[scheduled](https://sr.ht/~sircmpwn/scheduled)**  is also early in development. It is a replacement for crond (and
also  [at(1)](https://linux.die.net/man/1/at) ) which is redesigned from the ground up. I have never been thrilled
with cron’s design — it’s very un-Unix like. scheduled will have better
error handling and logging, a much more flexible and understandable approach to
configuration, and a better approach to security, plus the ability to do ad-hoc
scheduling from the command line. This was designed prior to date/time support
landing in Hare, and was blocked for a while, but is now unblocked. However, it
is not my highest priority.

Each of these projects will spawn more blog posts (or talks) going into greater
depth on their design goals and rationale later on. For now, with the
introductions out of the way, allow me to fill you in on the things which got
done in this past month in particular.

I’ll keep the SourceHut news short, and expand upon it in the “what’s cooking”
post later today. For my own part, I spent some time working on  [hut](https://sr.ht/~emersion/hut)  to add
support for comprehensive account data import/export. This will allow you to
easily take all of your data out of sourcehut and import it into another
instance, or any compatible software — your git repos are just git repos
and your mailing lists are just mbox files, so you could push them to GitHub or
import them into GNU Mailman, for example. This work is also a step towards
self-service account deletion and renaming, both prioritized for the beta.

Regarding Hare itself, there are many important recent developments. Over 300
commits landed this month, so I’ll have to leave some details out. An OpenBSD
port is underway by Brian Callahan, and the initial patches have landed for the
Hare compiler. The crypto module grew  [blowfish](https://docs.harelang.org/crypto/blowfish)  and  [bcrypt](https://docs.harelang.org/crypto/bcrypt)  support, both
useful mainly for legacy compatibility, as well as the more immediately useful
 [x25519](https://docs.harelang.org/crypto/x25519)  and  [pem](https://docs.harelang.org/encoding/pem)  implementations. There is also a new  [encoding::json](https://docs.harelang.org/encoding/json) 
module, 1  and a number of fixes and improvements have been steadily
flowing in for  [regex](https://docs.harelang.org/regex) ,  [bufio](https://docs.harelang.org/bufio) ,  [net](https://docs.harelang.org/net) ,  [net::uri](https://docs.harelang.org/net/uri) , and  [datetime](https://docs.harelang.org/datetime) , along with
dozens of others.

For Himitsu, I developed  [hare-ssh](https://sr.ht/~sircmpwn/hare-ssh)  this month to facilitate the addition of
 [himitsu-ssh](https://git.sr.ht/~sircmpwn/himitsu-ssh) , which provides SSH tooling that integrates with Himitsu (check
out the video above for a demo). The “hissh-import” command decodes OpenSSH
private keys and loads them into the Himitsu keystore, and the “hissh-agent”
command runs an SSH agent that performs authentication with the private keys
stored in Himitsu. Future additions will include “hissh-export”, for getting
your private keys back out in a useful format, and “hissh-keygen”, for skipping
the import/export step entirely. Presently only ed25519 keys are supported; more
will be added as the necessary primitives are added to Hare upstream.

I did some work on Helios this weekend, following a brief hiatus. I wrote a more
generalized page table implementation which can manage multiple page tables
(necessary to have separate address spaces for each process), and started
rigging up the kernel to userspace transition, which I briefly covered earlier
in the post. As of this morning, I have some code running in userspace —
one variant attempts to  `cli` , causing a general protection fault (as expected),
and another just runs a busy loop, which works without any faults. Next steps
are syscalls and scheduling.

That’s all the news for today. Hare! Woo! Thanks for reading, and be sure to
check out — and maybe contribute to? — some of these projects. Take
care!

1. Which is likely to be moved to the extended library in the future. ↩︎
