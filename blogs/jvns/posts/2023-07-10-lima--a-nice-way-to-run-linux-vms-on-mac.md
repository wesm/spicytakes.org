---
title: "Lima: a nice way to run Linux VMs on Mac"
date: 2023-07-10
url: https://jvns.ca/blog/2023/07/10/lima--a-nice-way-to-run-linux-vms-on-mac/
slug: lima--a-nice-way-to-run-linux-vms-on-mac
word_count: 1169
---


Hello! Here’s a new entry in the “cool software julia likes” section.


A little while ago I started using a Mac, and one of my biggest
frustrations with it is that often I need to run Linux-specific software. For
example, the [nginx playground](https://jvns.ca/blog/2021/09/24/new-tool--an-nginx-playground/) I
posted about the other day only works on Linux because it uses Linux namespaces (via `bubblewrap`)
to sandbox nginx. And I’m working on another playground right now that uses bubblewrap too.


This post is very short, it’s just to say that Lima seems nice and much simpler
to get started with than Vagrant.


### enter Lima!


I was complaining about this to a friend, and they mentioned
[Lima](https://lima-vm.io/), which stands for **Li**nux on **Ma**c. I’d heard
of [colima](https://github.com/abiosoft/colima) (another way to run Linux
containers on Mac), but I hadn’t realized that Lima also just lets you run VMs.


It was surprisingly simple to set up. I just had to:

1. Install Lima (I did `nix-env -iA nixpkgs.lima` but you can also install it with `brew install lima`)
2. Run `limactl start default` to start the VM
3. Run `lima` to get a shell


That’s it! By default it mounts your home directory as read-only inside the VM


There’s a config file in `~/.lima/default/lima.yaml`, but I haven’t needed to change it yet.


### some nice things about Lima


Some things I appreciate about Lima (as opposed to Vagrant which I’ve used in the past and found kind of frustrating) are:

1. it provides a default config
2. it automatically downloads a Ubuntu 22.04 image to use in the VM (which is what I would have probably picked anyway)
3. it mounts my entire home directory inside the VM, which I really like as a default choice (it feels very seamless)


I think the paradigm of “I have a single chaotic global Linux VM which I use
for all my projects” might work better for me than super carefully configured
per-project VMs. Though I’m sure that you can have carefully configured
per-project VMs with Lima too if you want, I’m just only using the `default` VM.


### problem 1: I don’t know how to mount directories read-write


I wanted to have my entire home directory mounted read-only, but have some
subdirectories (like `~/work/nginx-playground`) mounted read-write. I did some
research and here’s what I found:

- a comment on [this github issue](https://github.com/lima-vm/lima/issues/873) says that you can use [mountType: “virtiofs” and vmType: “vz”](https://github.com/lima-vm/lima/blob/master/docs/vmtype.md#vz) to mount subdirectories of your home directory read-write
- the Lima version packaged in nix 23.05 doesn’t seem to support `vmType: vz` (though I could be wrong about this)


Maybe I’ll figure out how to mount directories read-write later, I’m not too
bothered by working around it for now.


### problem 2: networking


I’m trying to set up some weird networking stuff ([this tun/tap setup](https://jvns.ca/blog/2022/09/06/send-network-packets-python-tun-tap/))
in Lima and while it appeared to work at first, actually the `tun` network
device seems to be unreliable in a weird way for reasons I don’t understand.


Another weird Lima networking thing: here’s what gets printed out when I ping a machine:


```
$ ping 8.8.8.8
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
ping: Warning: time of day goes back (-7148662230695168869us), taking countermeasures
ping: Warning: time of day goes back (-7148662230695168680us), taking countermeasures
64 bytes from 8.8.8.8: icmp_seq=0 ttl=255 time=0.000 ms
wrong data byte #16 should be 0x10 but was 0x0
#16	0 6 0 1 6c 55 ad 64 0 0 0 0 72 95 9 0 0 0 0 0 10 11 12 13 14 15 16 17 18 19 1a 1b
#48	1c 1d 1e 1f 20 21 22 23
ping: Warning: time of day goes back (-6518721232815721329us), taking countermeasures
64 bytes from 8.8.8.8: icmp_seq=0 ttl=255 time=0.000 ms (DUP!)
wrong data byte #16 should be 0x10 but was 0x0
#16	0 6 0 2 6d 55 ad 64 0 0 0 0 2f 9d 9 0 0 0 0 0 10 11 12 13 14 15 16 17 18 19 1a 1b
#48	1c 1d 1e 1f 20 21 22 23
ping: Warning: time of day goes back (-4844789546316441458us), taking countermeasures
64 bytes from 8.8.8.8: icmp_seq=0 ttl=255 time=0.000 ms (DUP!)
wrong data byte #16 should be 0x10 but was 0x0
#16	0 6 0 3 6e 55 ad 64 0 0 0 0 69 b3 9 0 0 0 0 0 10 11 12 13 14 15 16 17 18 19 1a 1b
#48	1c 1d 1e 1f 20 21 22 23
ping: Warning: time of day goes back (-3834857329877608539us), taking countermeasures
64 bytes from 8.8.8.8: icmp_seq=0 ttl=255 time=0.000 ms (DUP!)
wrong data byte #16 should be 0x10 but was 0x0
#16	0 6 0 4 6f 55 ad 64 0 0 0 0 6c c0 9 0 0 0 0 0 10 11 12 13 14 15 16 17 18 19 1a 1b
#48	1c 1d 1e 1f 20 21 22 23
ping: Warning: time of day goes back (-2395394298978302982us), taking countermeasures
64 bytes from 8.8.8.8: icmp_seq=0 ttl=255 time=0.000 ms (DUP!)
wrong data byte #16 should be 0x10 but was 0x0
#16	0 6 0 5 70 55 ad 64 0 0 0 0 65 d3 9 0 0 0 0 0 10 11 12 13 14 15 16 17 18 19 1a 1b
#48	1c 1d 1e 1f 20 21 22 23

```


This seems to be a [known issue with ICMP](https://github.com/lima-vm/lima/issues/193).


### why not use containers?


I wanted a VM and not a Linux container because:

1. the playground runs on a VM in production, not in a container, and generally
it’s easier to develop in a similar environment to production
2. all of my playgrounds use Linux namespaces, and I don’t know how to create a
namespace inside a container. Probably you can but I don’t feel like
figuring it out and it seems like an unnecessary distraction.
3. on Mac you need to run containers inside a Linux VM anyway, so I’d rather
use a VM directly and not introduce another unnecessary layer


### OrbStack seems nice too


After I wrote this, a bunch of people commented to say that
[OrbStack](https://orbstack.dev/) is great. I was struggling with the
networking in Lima (like I mentioned above) so I tried out OrbStack and the network does seem to be better.


`ping` acts normally, unlike in Lima:


```
$ ping 8.8.8.8
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=113 time=19.8 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=113 time=15.9 ms
64 bytes from 8.8.8.8: icmp_seq=3 ttl=113 time=23.1 ms
64 bytes from 8.8.8.8: icmp_seq=4 ttl=113 time=22.7 ms

```


The setup steps for OrbStack are:

1. Download OrbStack from the website
2. In the GUI, create a VM
3. Run `orb`
4. That’s it


So it seems equally simple to set up.


### that’s all!


Some other notes:

- It looks like Lima works on Linux too
- a bunch of people on Mastodon also said [colima](https://github.com/abiosoft/colima) (built on top of Lima) is a nice Docker alternative on Mac for running Linux containers
