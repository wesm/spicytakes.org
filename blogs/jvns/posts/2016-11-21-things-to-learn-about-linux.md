---
title: "Things to learn about Linux"
date: 2016-11-21
url: https://jvns.ca/blog/2016/11/21/things-to-learn-about-linux/
slug: things-to-learn-about-linux
word_count: 485
---


I asked on Twitter today what Linux things they would like to know more
about. I thought the replies were really cool so here’s a list (many of
them could be discussed on any Unixy OS, some of them are Linux-specific)

- tcp/ip & networking stuff
- what is a port/socket?
- seccomp
- systemd
- IPC (interprocess communication, pipes)
- permissions, setuid, sticky bits, how does chown work
- how the shell uses fork & exec
- how can I make my computer a router?
- process groups, session leaders, shell job control
- memory allocation, how do heaps work, what does malloc do?
- ttys, how do terminals work
- process scheduling
- drivers
- what’s the difference between Linux and Unix
- the kernel
- modern X servers
- how does X11 work?
- Linux’s zero-copy API (sendfile, splice, tee)
- what is dmesg even doing
- how kernel modules work
- embedded stuff: realtime, GPIO, etc
- btrfs
- QEMU/KVM
- shell redirection
- HAL
- chroot
- filesystems & inodes
- what is RSS, how do I know how much memory my process is using
- iptables
- what is a network interface exactly?
- what is syslog and how does it work?
- how are logs usually organized?
- virtual memory
- BPF
- bootloader, initrd, kernel parameters
- the `ip` command
- what are all the files that are not file files (/dev, stdin, /proc,
/sys)
- dbus
- sed and awk
- namespaces, cgroups, docker, SELinux, AppArmor
- debuggers
- what’s the difference between threads and processes?
- if unix is text-based, how do desktop environments like GNOME fit in?
- how does the “man” system work.
- kpatch, kgraph, kexec
- more about the stack. Are C vars really stack slots? How tf do setjmp
and longjmp work?
- package management
- mounts and vfs


this is great for so many reasons!

1. I need to draw 11 more drawings about Linux this month and these are
such great ideas
2. there are many things I don’t know on this list and it’s a cool
reminder of how much interesting stuff there still is to learn! A few
of these I barely even know what they are (dbus, SELinux) or only have a
pretty sketchy notion (seccomp, how X11 works, many more)
3. it’s also a cool reminder of how far I’ve come – I at least know
where to *start* with most of the things on this list, even if I
definitely could not explain a lot of them in detail without looking
some stuff up.


Also I sometimes want to remind people that you too could write
interesting
blog posts / drawings on the internet – for instance “what is dmesg even doing” is
an interesting topic, and totally possible to learn about! (I just
read [dmesg](https://en.wikipedia.org/wiki/Dmesg) on Wikipedia and now I
know more!)
