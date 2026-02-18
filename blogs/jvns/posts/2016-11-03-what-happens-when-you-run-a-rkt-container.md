---
title: "What happens when you run a rkt container?"
date: 2016-11-03
url: https://jvns.ca/blog/2016/11/03/what-happens-when-you-run-a-rkt-container/
slug: what-happens-when-you-run-a-rkt-container
word_count: 2214
---


I’ve been learning a lot about [rkt](https://coreos.com/rkt) recently. rkt (“rocket”) is a program that lets you run containers. In [what even is a container?](https://jvns.ca/blog/2016/10/10/what-even-is-a-container/), we talked about how running a container can be “basically” just the same as running a process. You just run that process with a different view of the filesystem (using “namespaces”).


I’ve claimed previously on this blog that rkt “just runs programs, it’s not
that complicated, that’s why it’s cool”. But if you look at the source for rkt,
excluding tests, there are about 34,000 lines of Go code today. That’s not a
huge huge project, but it’s not trivial! What are all those 34,000 lines doing?


Since I’m trying to use rkt pretty seriously right now, I’d like to understand
its architecture. Let’s find out what rkt does when it runs a container!


I claimed somewhat boldly on twitter that this would “explain every system call
that happens in rkt”. That was somewhat of an overstatement – I picked command
line options to rkt so that it runs as few system calls as possible, and then
even so there are too many to understand in 2 days :) But that’s the spirit of
what I’m trying to do here – really understand exactly what rkt is doing.


There’s some pretty good [architecture documentation](https://github.com/coreos/rkt/blob/master/Documentation/devel/architecture.md) that I referred to a bunch and explains a bunch of things that I do not explain here.


As usual there are probably things in here that are wrong.


**What running a container looks like in rkt**


When you run a rkt container, it looks like this:


```
sudo rkt run julia.com/some_image

```


That looks pretty simple! But a lot of things need to happen for this to work.


# Part 1: FETCH


To get a container, first you need to put the files on disk somewhere! This is
actually pretty involved.


### Step 1.1: Look up julia.com/some_image


rkt uses a container format called “ACI” today.


The first thing is to download the image. You find it on the internet, download
a file, okay.  This is not trivial but it’s not what I’m interested in
right now. Next comes the interesting (to me) part.


### Step 1.2: Put the image in rkt’s local container store


You could imagine rkt could make your user keep those images on disk somewhere and tell you the
path to the image to run. (`rkt run /home/julia/my-cool-image.aci`). This is not what rkt does.


rkt instead maintains a store of all the images it knows about. Your image
needs to get into this store before it can be run.


Here’s all the images I have right now on my laptop. There are 2 of them.


```
$ sudo rkt image list
ID			NAME					SIZE	IMPORT TIME	LAST USED
sha512-6c0b85484a1c	coreos.com/rkt/stage1-coreos:1.18.0	179MiB	1 day ago	1 day ago
sha512-7b1e1a77f0b6	coreos.com/rkt/builder:1.1.0		1.6GiB	1 day ago	1 day ago

```


Where do these images actually live on disk? In `/var/lib/rkt/cas/blob/sha512`!


```
 ls /var/lib/rkt/cas/blob/sha512/*
/var/lib/rkt/cas/blob/sha512/6c:
sha512-6c0b85484a1ca60df409e7944938fc6a44ccf4a2ce373d0557ea06ec56da73c9
/var/lib/rkt/cas/blob/sha512/7b:
sha512-7b1e1a77f0b693b83d87026a44d1f57b089ef392820d8b3835df292d929e8842

```


The file `/var/lib/rkt/cas/blob/sha512/6c/sha512-6c0b85484a1ca60df409e7944938fc6a44ccf4a2ce373d0557ea06ec56da73c9`
is actually a tar archive. It just contains every file that belongs in that
image! If you list the tar archive, you see a bunch of files like this. Neat!


```
rootfs/usr/lib64/libc.so.6 -> libc-2.21.so
rootfs/usr/lib64/libcap.so
rootfs/usr/lib64/libcap.so.2 -> libcap.so.2.24
rootfs/usr/lib64/libcap.so.2.2

```


But here’s something weird: let’s compare the sizes of the images on disk, and
how much space rkt says our images take up. The /sha512-6c0b854 image is 843M,
but rkt says it’s 1.6GB! That’s almost exactly twice as much. Why? We’re going
to find out in a second.


Here’s me finding out that there’s a space mismatch:


```
root@kiwi:/var/lib/rkt/cas/tree# du -sh /var/lib/rkt/cas/blob/sha512/*/*
90M	/var/lib/rkt/cas/blob/sha512/6c/sha512-6c0b85484a1ca60df409e7944938fc6a44ccf4a2ce373d0557ea06ec56da73c9
843M	/var/lib/rkt/cas/blob/sha512/7b/sha512-7b1e1a77f0b693b83d87026a44d1f57b089ef392820d8b3835df292d929e8842
root@kiwi:/var/lib/rkt/cas/tree# sudo rkt image list
ID			NAME					SIZE	IMPORT TIME	LAST USED
sha512-6c0b85484a1c	coreos.com/rkt/stage1-coreos:1.18.0	179MiB	1 day ago	1 day ago
sha512-7b1e1a77f0b6	coreos.com/rkt/builder:1.1.0		1.6GiB	1 day ago	1 day ag

```


### Step 1.3: Find the image in the local store


Okay, awesome! Let’s suppose the image is already in the local store. We need
to look it up.


So if I’m doing `rkt run core.com/rkt/builder` I’ll find that image at
`/var/lib/rkt/cas/blob/sha512/7b/sha512-7b1e1a77f0b693b83d87026a44d1f57b089ef392820d8b3835df292d929e8842`.
But how does rkt know that that image name matches that tar file?


If I strace rkt, I see it reading a file called `/var/lib/rkt/cas/db/ql.db`.
What’s that? It turns out “ql” is an embedded SQL database written in Go. Let’s
see what’s in it! There are 3 tables (‘remote’, ‘aciinfo’, and ‘version’).
aciinfo seems to be the only really interesting one.


```
$ ql  -db /var/lib/rkt/cas/db/ql.db 'select * from aciinfo'
"sha512-7b1e1a77f0b693b83d87026a44d1f57b089ef392820d8b3835df292d929e8842", "coreos.com/rkt/builder", 2016-10-28 23:59:50.357354868 -0400 EDT, 2016-10-28 23:59:54.158511535 -0400 EDT, false, 883696128, 864451348
"sha512-6c0b85484a1ca60df409e7944938fc6a44ccf4a2ce373d0557ea06ec56da73c9", "coreos.com/rkt/stage1-coreos", 2016-10-28 23:56:30.485120722 -0400 EDT, 2016-10-28 23:56:30.950583566 -0400 EDT, false, 93723136, 93603074

```


Okay, so we can look up the image by name in the SQL database and find out where it’s supposed to be on disk. Great! What now?


### Step 1.4: copy everything from the “image store” to the “tree store”


So, you might think that we use the image store to run containers (from /var/lib/rkt/cas/blob). This is how Docker works – it just stores a bunch of images on disk and uses them directly to run containers. rkt has an EXTRA STEP, though. So before you can run your container, it

1. finds all your container’s dependencies
2. unzips every dependency into a single directory all on top of each other
3. calls that the “tree store”


If you think this takes extra disk space, you are right! When you use rkt to run a container you get 2 copies of every file in that container. I was confused about this so I asked on the mailing list why it is (which delayed me making progress on this post for several). [Here is the question I asked](https://groups.google.com/forum/?pli=1#!topic/rkt-dev/bhGeR3pUfPY)


I’m going to copy the relevant part of the reply here because it was VERY HELPFUL.


> One of the key differences between the ACI and Docker formats is that while Docker’s layers are essentially a linked list, ACI dependencies instead form a directed acyclic graph, with a separate whitelist system. This means that to create a root filesystem from a Docker image and its parent layers, you can simply layer them on top of each other while respecting the AUFS-style whiteout files; whereas the process of rendering an ACI as a root filesystem is rather more complicated [1], as you need to traverse a full graph [2], and can have cases like the same image appearing multiple times in the graph but with a different whitelist affecting which parts of it should be used [3]. To compensate for this additional complexity, we “pre-render” the root filesystem that an ACI represents into the treestore [4], and then use overlayfs on top of this at runtime.


So basically this is because of a fundamental difference between the ACI format and the Docker image format. But the new OCI format is more like the Docker format! And they’re rearchitecting how they do all their container storage on disk. So this might all be completely different in the future. Let’s move along.


# Part 2: PREPARE TO RUNNNN


Before we run, we have to PREPARE to run.


### Step 2.1: Create a pod


So when you run a rkt container, you’re actually running a thing called a “pod”. I am still somewhat confused about what running a pod entails exactly but I know that

1. you get a pod ID like 9ec8ec92-f04d-4194-956f-2aa1fe94389c
2. pods do not get automatically deleted when your program exits (they need to be garbage collected)
3. you can run “rkt prepare” to prepare a pod to run and then `rkt run-prepared` to run an already set-up pod


### Step 2.2: mount the pod’s filesystems


To run a program, the pod needs files! The files that the pod is going to run are in the “tree store”. Here’s a system call from rkt setting up the pod’s filesystems:


```
32034 mount("overlay",
"/var/lib/rkt/pods/run/9ec8ec92-f04d-4194-956f-2aa1fe94389c/stage1/rootfs",
"overlay", 0,
"lowerdir=/var/lib/rkt/cas/tree/deps-sha512-7d429fe0c72eb12b91726bde7ff2b730b4b72c1c380a4ea5d09ff162b086cb49/rootfs,upperdir=/var/lib/rkt/pods/run/9ec8ec92-f04d-4194-956f-2aa1fe94389c/overlay/deps-sha512-7d429fe0c72eb12b91726bde7ff2b730b4b72c1c380a4ea5d09ff162b086cb49/upper,workdir=/var/lib/rkt/pods/run/9ec8ec92-f04d-4194-956f-2aa1fe94389c/overlay/deps-sha512-7d429fe0c72eb12b91726bde7ff2b730b4b72c1c380a4ea5d09ff162b086cb49/work")
= 0b12b91726bde7ff2b730b4b72c1c380a4ea5d09ff162b086cb49

```


Goodness. This basically says “take `/var/lib/rkt/cas/tree/deps-sha512-7d429fe0c72e...` and `/var/lib/rkt/pods/run/9ec8ec92-f04d-4194-956f-2aa1fe94389c/overlay/deps-sha512-7d429fe0c72eb12b91726bde7ff2b730b4b72c1c380a4ea5d09ff162b086cb49/upper` and put them together to make `/var/lib/rkt/pods/run/9ec8ec9.../stage1/rootfs`”.


This is called an “overlay filesystem” and it is a big part of how containers work. Basically if you want to run 3 programs on the same computer with the same base container, you can! And they can share files on disk! But that doesn’t mean they share files with each other – if one program edits a file from the base container, the other programs won’t see the changes. Instead they all get their own filesystems, which use copy-on-write.


# Part 3: RUN!!!!!!!!!!


The last thing we get to do is RUN THE CONTAINER. We’re going to go through a
bunch of system calls now! Here’s how I ran `rkt run`, with some commentary
about why I picked that option. Basically I picked options that would run my
container in the simplest way possible. Simplest does not mean best – the simplest way
includes turning off all security features :)


```
rkt run 
   coreos.com/rkt/builder
  # security features are complicated! turn them all off
  --insecure-options=all
  # no network namespaces, just do the most boring possible networking
  --net=host
  # use the "fly" stage1 -- this will just run my container using a chroot
  # (network namespaces don't even work with this anyway, the --net=host is kinda redundant)
  --stage1-name=coreos.com/rkt/stage1-fly:1
  # set up a couple of volumes that this particular container wants
  --volume src-dir,kind=host,source=(pwd)
  --volume build-dir,kind=host,source=(pwd)/build

```


Okay, what happens when we do this? We’ve already set up our pod (in the PREPARE step). Here’s the first interesting thing I saw.


```
/var/lib/rkt/pods/run/10a558fc-f917-443a-ad23-b54a7c5ce95d/stage1/rootfs/run

```


It is running our program! It then goes and does a bunch of boring stuff where
it sets up /proc or whatever. This is pretty annoying to read because this
program is a Go program so there are a lot of weird Go runtime system calls
because it runs one thread per core or something.


Also it reads the pod manifest and figures out what its job is (what program is
it supposed to run).


This container’s job is to run a file called `/scripts/build.sh`. It finally does
it! Here’s what that looks like:


```
30297 chroot("stage1/rootfs/opt/stage2/builder/rootfs") = 0
30297 chdir("/opt/rkt")                 = 0
30297 setresgid(0, 0, 0)                = 0
30297 setresuid(0, 0, 0)                = 0
30297 fcntl(4, F_SETFD, 0)              = 0
30297 execve("/bin/bash", ["/bin/bash", "/scripts/build.sh"], [/* 5 vars */] <unfinished ...>

```


We did it! We ran a container!


### what is this “stage1” business, julia?


Yeah, sorry, this is a weird rkt thing. BASICALLY there is a set of programs
called “stage1” which get included in your filesystem. Their job is to take
your “container manifest”  (which says what program to run) and the rkt command
line arguments (like which ports to map to which other ports) and make it all
happen for you. So they’re basically responsible for setting up the actual
container.


As far as I understand there are basically only 2 interesting ones: the regular
one (which uses systemd) and the lightweight one (“fly”). I picked the
lightweight one here because the other one has way more system calls and it’s
more complicated to understand.


### Step ???: A lot of security checks


One thing I’ve intentionally left out here is – rkt does a ton of security checks when you run a container. They’re called “image”, “tls”, “ondisk”, “http”, “pubkey”, “capabilities”, “paths”, and “seccomp”. You might have noticed that I ran with `--insecure-options=all`. This is not what I do in real life, but it is a lot to talk about and this is already getting to be 2000 words.


Some of them are during fetch (which you can separate out and do before running the container) and some of them are during run. So it might be reasonable to ignore all the `fetch` security checks if you already did them all when fetching. Who knows. I’m not going to give you security recommendations, you should not listen to me.


### Understanding the systems you are using is cool


Someone on twitter asked me “julia, why are you asking all these questions,
this is not the level of abstraction you should work at, you need to ship
code!”


And this is sort of true! Everyone should not need to know all the details of
how everything they use works. That would take too much time. Imagine if every
Linux user needed to read Linux kernel code to do their job! Eep.


HOWEVER. Right now it is my job to work on making sure containers will work, so
that other people do not have to worry about it! This means that I have to (get
to?) worry about some of the weird stuff my container software is doing.


If I know rkt’s storage model, then I can make guesses at exactly how much disk
space rkt is going to use in production, then I can plan to give my machines an
appropriate amount of storage, and then nobody will run out of disk space!
Running out of disk space is THE WORST.


This is why I appreciate documents like Kelsey Hightower’s [Kubernetes the Hard Way](https://github.com/kelseyhightower/kubernetes-the-hard-way) – when you
work with complex systems, a lot of the time **someone** needs to understand
how they work, so they can plan to operate the system correctly.


Right now I get to be that someone, for some things. Yay!
