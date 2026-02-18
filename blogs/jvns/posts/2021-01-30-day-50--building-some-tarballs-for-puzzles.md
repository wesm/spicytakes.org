---
title: "Day 50: Building some tarballs for puzzles, and trying to make a kernel boot faster"
date: 2021-01-30
url: https://jvns.ca/blog/2021/01/30/day-50--building-some-tarballs-for-puzzles/
slug: day-50--building-some-tarballs-for-puzzles
word_count: 681
---


On Friday I made progress on 3 things:

1. getting my 5.8 kernel to boot faster in Firecracker
2. built some puzzle tarballs (which I’ll explain in a bit)
3. loaded the puzzle tarballs into my Firecracker VMs


### the mystery of the slow kernel boot


I noticed that I had 2 pauses when I started my kernel with Firecracker (here’s the [complete log](https://gist.github.com/jvns/198a1e851fde1cbe4df3c21d6d2cf9dd)).


one for 0.3 seconds:


```
[    0.142205] i8042: If AUX port is really absent please use the 'i8042.noaux' option
2021-01-29T09:14:10.315589518 [anonymous-instance:WARN:src/devices/src/legacy/i8042.rs:126] Failed to trigger i8042 kbd interrupt (disabled by guest OS)
[    0.424261] serio: i8042 KBD port at 0x60,0x64 irq 1

```


and one for 0.5 seconds:


```
[    0.442595] Key type encrypted registered
[    0.936675] input: AT Raw Set 2 keyboard as /devices/platform/i8042/serio0/input/input0

```


I asked about this in the Firecracker Slack and got a reply suggesting to use
the `i8042.noaux` option for the first delay. (which I hadn’t noticed, even
though it says it right there :)).  That fixed it!


I still don’t understand why the second delay is happening or how to fix it.
Someone suggested it might be related to secure boot, but I spent a while
poking at my kernel config and tried compiling with 6 different configurations
and didn’t get anywhere, so I gave up for the day and moved onto something
else.


### building tarballs of each puzzle


I wrote a little Python script to do this. It basically runs a `build.sh`
script that I write to build the puzzle inside a Docker container, and then
makes a tarball of the Docker container’s current working directory.


Basically I took advantage of the fact that I know how Docker uses overlayfs
internally and just took a tarball of the upper part of the overlay directly.


I did this because I couldn’t find a good way to do it using the normal Docker
interfaces – I tried some things using a Docker experimental feature called
`docker build --squash` but didn’t really get anywhere.


```
import os
import subprocess
import json
import time


pwd = os.getcwd()

container_id = subprocess.check_output(["docker", "run", "-v", f"{pwd}:/puzzle", "-td",  "my-base-image", "/bin/bash"])
container_id = container_id.decode("utf-8").strip()
container_json = subprocess.check_output(["docker", "inspect", container_id])
properties = json.loads(container_json)

upperdir = properties[0]['GraphDriver']['Data']['UpperDir']

subprocess.check_call(["docker", "exec", container_id, "bash", "/puzzle/build.sh"])
subprocess.check_call(["sudo", "tar", "-C", upperdir, "--exclude=puzzle", "--xattrs", "-cf", "puzzle.tar", '.'])

subprocess.check_call(["docker", "kill", container_id])

```


### loading the puzzle tarball when I start a puzzle


I then wrote a little Go function to load in these tarballs when I start a VM.
It’s really dumb, it just mounts the image, extracts the tarball into the
mounted directory, and unmounts.


```
func (opts *options) copyPuzzleFiles(imagePath string) error {
	if opts.Request.Tarball == "" {
		return nil
	}
	mountDir := filepath.Join(ImageDir, pseudo_uuid())
	err := os.Mkdir(mountDir, 0755)
	defer os.Remove(mountDir)
	if err != nil {
		return fmt.Errorf("Failed creating dir: %s", mountDir, err)
	}

	if err := exec.Command("mount", imagePath, mountDir).Run(); err != nil {
		return fmt.Errorf("Failed mounting path %s: %s", imagePath, err)
	}

	if err := exec.Command("tar", "-C", mountDir, "-xf", opts.Request.Tarball).Run(); err != nil {
		return fmt.Errorf("Failed to extract tarball %s: %s", opts.Request.Tarball, err)
	}

	if err := exec.Command("umount", mountDir).Run(); err != nil {
		return fmt.Errorf("Failed umounting path %s: %s", imagePath, err)
	}
	return nil
}

```


One thing I’ve been thinking about with code like this is whether it makes
sense to shell out to tools or whether it would be better to – for example, Go
has a tarball. Right now I don’t really see any benefit to using Go’s tar code
because I feel like these command line tools (mount/umount/tar) are really a
known quantity and if I tried to reimplement them in Go I would just write a
buggy version that I’d then have to maintain.


### filesystems!


I also had a really delightful conversation with my friend Dave about
filesystems where we talked about my problems with using device mapper and how
Firecracker doesn’t support qcow2 and ideas for different ways to get
Firecracker to support overlay images.


There’s an interesting discussion on the Firecracker GitHub about
[implementing a virtio backend ](https://github.com/firecracker-microvm/firecracker/pull/1351) to let the VM share a directory from the host.
