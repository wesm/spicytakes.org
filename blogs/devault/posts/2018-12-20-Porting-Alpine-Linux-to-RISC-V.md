---
title: "Porting Alpine Linux to RISC-V"
date: 2018-12-20
url: https://drewdevault.com/2018/12/20/Porting-Alpine-Linux-to-RISC-V.html
slug: Porting-Alpine-Linux-to-RISC-V
word_count: 903
---

I recently received my  [HiFive Unleashed](https://www.sifive.com/boards/hifive-unleashed) , after several excruciating
months of waiting, and it’s incredibly cool. For those unaware, the HiFive
Unleashed is the first consumer-facing Linux-capable  [RISC-V](https://en.wikipedia.org/wiki/RISC-V)  hardware.
For anyone who’s still lost, RISC-V is an  [open](https://github.com/riscv) ,
royalty-free  [instruction set
architecture](https://en.wikipedia.org/wiki/Instruction_set_architecture) , and
the HiFive is an  [open](https://github.com/sifive)  CPU implementing it. And here
it is on my dining room table:

This board is  *cool* . I’m working on making this hardware available to
 [builds.sr.ht](https://meta.sr.ht)  users in the next few months, where I intend to use it to
automate the remainder of the Alpine Linux port and make it available to any
other operating systems (including non-Linux) and userspace software which are
interested in working on a RISC-V port. I’m fairly certain that this will be the
first time hardware-backed RISC-V cycles are being made available to the public.

There are two phases to porting an operating system to a new architecture:
bootstrapping and, uh, porting. For lack of a better term. As part of
bootstrapping, you need to obtain a cross-compiler, port libc, and cross-compile
the basics. Bootstrapping ends once the system is  *self-hosting* : able to
compile itself. The “porting” process involves compiling all of the packages
available for your operating system, which can take a long time and is generally
automated.

The first order of business is the cross-compiler. RISC-V support landed in
binutils 2.28 and gcc 7.1 several releases ago, so no need to worry about adding
a RISC-V target to our compiler. Building both with
 `--target=riscv64-linux-musl`  is sufficient to complete this step. The other
major piece is the C standard library, or libc. Unlike the C compiler, this step
required some extra effort on my part - the RISC-V port of musl libc, which
Alpine Linux is based on, is a work-in-progress and has not yet been upstreamed.

There does exist  [a patch](https://github.com/riscv/riscv-musl)  for RISC-V support, though it had never
been tested at a scale like this. Accordingly, I ran into several bugs, for
which I wrote several patches ( [1](https://github.com/riscv/riscv-musl/pull/2)   [2](https://github.com/riscv/riscv-musl/pull/3)   [3](https://github.com/riscv/riscv-musl/pull/4) ). Having a working distro
based on the RISC-V port makes a much more compelling argument for the maturity
of the port, and for its inclusion upstream, so I’m happy to have caught these
issues. Until then, I added the port and my patches to the Alpine Linux musl
package manually.

A C compiler and libc implementation open the floodgates to porting a huge
volume of software to your platform. The next step is to identify and port the
essential packages for a self-hosting system.  For this, Alpine has a great
 [bootstrapping script](https://git.alpinelinux.org/cgit/aports/tree/scripts/bootstrap.sh)  which handles preparing the cross-compiler
and building the base system. Many (if not most) of these packages required
patching, tweaks, and manual intervention - this isn’t a turnkey solution - but
it is an incredibly useful tool. The most important packages at this step are
the native toolchain 1 , the package manager itself, and various other useful
things like tar, patch, openssl, and so on.

Once the essential packages are built and the system can compile itself, the
long porting process begins. It’s generally wise to drop the cross-compiler here
and start doing native builds, if your hardware is fast enough. This is a
tradeoff, because the RISC-V system is somewhat slower than my x86_64 bootstrap
machine - but many packages require lots of manual tweaks and patching to get
cross-compiling working. The time saved by not worrying about this makes up for
the slower build times 2 .

There are thousands of packages, so the next step for me (and anyone else
working on a port) is to automate the remainder of the process. For me, an
intermediate step is integrating this with builds.sr.ht to organize my own work
and to make cycles available to other people interested in RISC-V. Not all
packages are going to be ported for free - but many will! Once you unlock the
programming languages - C, Python, Perl, Ruby 3 , etc - most open source
software is pretty portable across architectures. One of my core goals with
sr.ht is to encourage portable software to proliferate!

If any readers have their own RISC-V hardware, or want to try it with qemu, I
have a RISC-V Alpine Linux repository here 4 . Something like this will install
it to /mnt:

```
apk add \
    -X https://mirror.sr.ht/alpine/main/ \
    --allow-untrusted \
    --arch=riscv64 \
    --root=/mnt \
    alpine-base alpine-sdk vim chrony
```

Run  `/bin/busybox --install`  and  `apk fix`  on first boot. This is still a work
in progress, so configuring the rest is an exercise left to the reader until I
can clean up the process and make a nice install script. Good luck!

Closing note: big thanks to the help from the community in #riscv on Freenode,
and to the hard work of the Debian and Fedora teams paving a lot of the way and
getting patches out there for lots of software! I still got to have all the fun
working on musl so I wasn’t entirely on the beaten path :)

1. Meaning a compiler which both *targets* RISC-V and *runs* on RISC-V. ↩︎
2. I was actually really impressed with the speed of the HiFive Unleashed. The main bottleneck is the mmcblk driver - once you get files in the kernel cache things are quite pleasant and snappy. ↩︎
3. I have all four of these now! ↩︎
4. [main](https://mirror.sr.ht/alpine/main/), [community](https://mirror.sr.ht/alpine/community/), [testing](https://mirror.sr.ht/alpine/testing/) ↩︎
