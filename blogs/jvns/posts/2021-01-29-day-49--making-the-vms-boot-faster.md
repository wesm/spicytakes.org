---
title: "Day 49: making the VMs boot faster"
date: 2021-01-29
url: https://jvns.ca/blog/2021/01/29/day-49--making-the-vms-boot-faster/
slug: day-49--making-the-vms-boot-faster
word_count: 890
---


Yesterday I integrated my new device mapper code and spent a bunch of time
trying to make my VMs boot faster and I learned a bunch of things.


My plan for making them boot faster was:

1. replace systemd with a lighter weight init system
2. that’s it


I think I actually discovered that the problem wasn’t systemd and that I can
keep systemd! I’ll talk about that in a second, but first I’m going to try to
write down some of my problems with loop devices.


### weird bug: sometimes I can’t allocate a loop device


Sometimes, after I create a bunch of /dev/loop devices, I get an error like
`"/dev/loop26 already mounted or mount point busy."` when trying to create and
use another one.


I think what’s happening under the hood here is that my program does an ioctl
to `/dev/loop-control` to get the ID of a free loop device, like this:


```
stat("/dev/loop-control", {st_mode=S_IFCHR|0660, st_rdev=makedev(0xa, 0xed), ...}) = 0
openat(AT_FDCWD, "/dev/loop-control", O_RDWR|O_CLOEXEC) = 3</dev/loop-control<char 10:237>>
ioctl(3</dev/loop-control<char 10:237>>, LOOP_CTL_GET_FREE) = 24
close(3</dev/loop-control<char 10:237>>) = 0

```


So the kernel here is saying “Ok, /dev/loop24 free”.


But then when I actually try to *use* /dev/loop24, I get an error.


I still don’t understand why this is (am I just misunderstanding something
about how the loop device interface works? is it a kernel bug?). I found a
workaround, which is if I free all of my loop devices then I can allocate them again.


I think this might be because I’m using different loop devices to refer to the
same file, but I’m not sure yet.


### adventures in replacing init: can’t allocate a pseudoterminal


Okay, back to my adventures with init systems. I tried replacing systemd in my VMs with `tini`,
a little init system meant for use with containers.


Basically I set `/sbin/init` to this little shell script


```
#!/bin/bash

mkdir -p /run/sshd

tini -- /usr/sbin/sshd -D

```


I ran into 2 problems with this (which is not very many considering how little it’s doing!!)


**problem 1**: `ps aux` didn’t work.


This was because I hadn’t mounted procfs. I added `mount -t proc proc /proc` to
the beginning of the script and that fixed it. Easy.


**problem 2**: I couldn’t get a prompt from SSH


When I sshed to my VM, I got this error:


```
PTY allocation request failed on channel 0

```


I had no idea what this meant. I asked on Zulip and Ori linked me to this great
article [The TTY Demystified](https://www.linusakesson.net/programming/tty/). I
didn’t read the whole thing, but it mentioned `/dev/pts` and so I tried to `ls /dev/pts` inside my VM.


And behold – I didn’t have a `/dev/pts`! I Googled how to get one, and found that I could run


```
mount -t devpts devpts /dev/pts

```


and fix the problem! I didn’t know that Linux had was a `devpts` filesystem for
managing pseudoterminals, that feels like a major missing piece in my “how do
terminals even work” model.


I added  `mount -t devpts devpts /dev/pts` to my little init bash script and that fixed the problem.


### adventures in replacing init: make systemd start faster


Once I got this to work I was talking about it to Kamal, and he said something
to the effect of “well, if you need to do so little to have an init system, maybe you can
just disable most of systemd and then keep using systemd!” I thought that was a
fair point (and I do want to be using systemd, to make it feel like a real
computer)


I wrote a hacky Python script called `systemd-surgery.py` and ran it inside my
VM. I don’t know that this is the best way to do it, but VMs are disposable and
it seemed to work fine.


Here’s the script with some comments.


```
import glob
import os
keep = [
        'ssh.service', # because we want sshd
        'systemd-user-sessions.service', # because otherwise systemd complains it's not done booting when you login
        'systemd-remount-fs.service', # because I think this might be what mounts procfs and devpts
        'systemd-journald.service', # because otherwise systemd complains that it can't log its progress on boot
        'sys-kernel-debug.mount', # because we love debugging
        'sys-kernel-tracing.mount', # because we love tracing
        'sys-kernel-config.mount', # not sure what this is, might remove it
#        'dbus.service', # need this for systemd analyze to work, but not otherwise I think
]
targets = ['getty', 'multi-user', 'sockets', 'timers', 'sysinit', 'default']

for t in targets:
    for filename in glob.glob(f"/etc/systemd/system/{t}.target.wants/*"):
        if os.path.basename(filename) in keep:
            continue
        print(filename)
        os.remove(filename)
    for filename in glob.glob(f"/usr/lib/systemd/system/{t}.target.wants/*"):
        if os.path.basename(filename) in keep:
            continue
        print(filename)
        os.remove(filename)

```


I got systemd’s start time to about 0.3s on my fast computer, which felt pretty
good.


### the real problem: my kernel was starting slowly!!!


Once I got systemd to be fast, I noticed something new I hadn’t noticed before:
my kernel was taking 1 second to boot and get into userspace!


I thought this was weird because Firecracker’s whole deal is that you can get
into userspace in 150ms. I tested with their example kernel, and that one in
fact took 144ms to get into userspace!


I don’t know why my kernel is 7x slower, but that’s what I’m going to look into
next. Probably I compiled it wrong or something. I didn’t see a lot of clues in
the logs but we’ll figure it out!
