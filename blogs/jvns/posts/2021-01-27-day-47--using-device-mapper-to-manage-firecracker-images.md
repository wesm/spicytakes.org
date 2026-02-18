---
title: "Day 47: Using device mapper to manage Firecracker images"
date: 2021-01-27
url: https://jvns.ca/blog/2021/01/27/day-47--using-device-mapper-to-manage-firecracker-images/
slug: day-47--using-device-mapper-to-manage-firecracker-images
word_count: 447
---


On Tuesday I didn’t get too much done, but I did learn how to use device mapper!


I mostly followed these directions:
[Fun with devicemapper snapshots](https://blog.oddbit.com/post/2018-01-25-fun-with-devicemapper-snapshots/)
but with a few changes. I basically tried to do exactly what ignite does [here in snapshot.go](https://github.com/weaveworks/ignite/blob/master/pkg/dmlegacy/snapshot.go#L61-L118), except in a bash script instead of a Go program.


This post isn’t going to be terribly clear because I’m tired right now, these
are mostly notes for myself so I can remember how to do it later.


### the problem: I don’t want to copy images every time I launch a VM


I can’t use the filesystem image directly I launch a VM because if I do, the user will
accidentally end up changing the base image themself if they write files.


I was dealing with this by making a copy every time, but that’s kind of slow
and it felt really inefficient. But there’s an alternative!


### the solution: copy on write with device mapper!


The solution is to use copy on write! So instead of making a copy, instead we
overlay another image on top. Reads come through the bottom, but any writes
only go to the top level.


The weird thing I had to wrap my head around was that unlike with overlayfs,
this copy-on-write thing is implemented at the disk image level – the overlay on
top doesn’t contain files, it just contains sort of random blocks of data that
would be totally impossible for any program to interpret by themselves.


### a commented bash script


Here’s a commented bash script with how I implemented this. It was way simpler
than I expected – it’s just runs both `losetup` and `dmsetup` twice.


```
BASEIMAGE=/path/to/base/image.ext4
OVERLAY=/path/to/overlay.ext4

# Step 1: Create an empty image
# I also tried to create the image with fallocate but it didn't work as well
for some reason I don't understand yet
qemu-img create -f raw $OVERLAY 1200M
OVERLAY_SZ=`blockdev --getsz $OVERLAY`

# Step 2: Create a loop device for the BASEIMAGE file (like /dev/loop16)
LOOP=$(losetup --find --show --read-only $BASEIMAGE)
SZ=`blockdev --getsz $BASEIMAGE`

# Step 3: Create /dev/mapper/mybase
printf "0 $SZ linear $LOOP 0\n$SZ $OVERLAY_SZ zero"  | dmsetup create mybase

# Step 4: Create another loop device for the OVERLAY file
LOOP2=$(losetup /dev/loop23 --show $OVERLAY)

# Step 5: Create the final device mapper
echo "0 $OVERLAY_SZ snapshot /dev/mapper/mybase $LOOP2 P 8" | dmsetup create myoverlay

```


### another problem: `losetup` ends up in an infinite loop sometimes


I noticed that sometimes `losetup`, instead of finding and creating a loop
device, sometimes just ends up in an infinite loop where it tries and fails to
create the same loop device forever. I don’t know why that is yet.
