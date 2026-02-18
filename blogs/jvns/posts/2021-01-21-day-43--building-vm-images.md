---
title: "Day 43: Building VM images"
date: 2021-01-21
url: https://jvns.ca/blog/2021/01/21/day-43--building-vm-images/
slug: day-43--building-vm-images
word_count: 381
---


I spent all day yesterday trying to build Ubuntu VM images that work with
Firecracker without too much success.


### some miscellaneous things I learned about manipulating images


At some point I was trying to extract the filesystem from the Ubuntu cloud
image to use with Firecracker. This did not work

- I can use `sfdisk` to view the partition table of a disk image
- I can use `dd` to extract `dd if=focal-server-cloudimg-amd64.img.orig.raw of=focal-image.ext4 skip=227328 count=4384735`
- Some Linux files are “sparse” which means that regions which are filled with 0s are collapsed. Very useful for disk images.
- I can use `fallocate -d` to turn a non-sparse file into a sparse file


### compiling the linux kernel isn’t that slow


The Firecracker instructions suggest building your own Linux kernel from
source. This seemed intimidating to me because I hadn’t done it before but it
was actually totally fine!


It only took me like 5 minutes to compile a Linux kernel from scratch (with
`make -j12` on an AMD Ryzen 5). I was really surprised by this, I thought it
would take like 2 hours.


I found out that the Linux kernel I compiled didn’t have the ISO filesystem
support, so I needed to reconfigure it to include ISO filesystem support. This
was very easy.


### the Ubuntu docker image doesn’t seem like the best base for a VM image


I’m still not sure what Ubuntu image I should use as a base for my VMs. I’ve
been trying both the Ubuntu cloud image ([https://cloud-images.ubuntu.com/focal/current/focal-server-cloudimg-amd64.img](https://cloud-images.ubuntu.com/focal/current/focal-server-cloudimg-amd64.img))
and the Docker Ubuntu:20.04 image


Problems with the Ubuntu cloud image: I haven’t been able to get it to boot yet
for some reason I haven’t worked out. It gets stuck on this `A start job is running for /dev/disk/by-label/UEFI` step that  Idon’t understand.


Problems with the Docker image: it does boot, but I haven’t managed to convince
`cloud-init` to successfully run in it yet. I also need to install a some basic
things in it (like `init` and `udev` for some reason), and it’s not really
designed to be a system to log into so I feel like it’s missing a lot of things


Maybe today I’ll go back to the cloud image and see what problems there are with getting it to boot.
