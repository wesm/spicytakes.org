---
title: "Day 52: testing how many Firecracker VMs I can run"
date: 2021-02-04
url: https://jvns.ca/blog/2021/02/04/day-52--out-of-memory-errors/
slug: day-52--out-of-memory-errors
word_count: 331
---


On Tuesday I finally got around to do something I’d been meaning to do for a
while: test how many Firecracker VMs I can actually run on my little
DigitalOcean droplet with 1GB of RAM.


This turned out to be less complicated to test than I thought, so let’s get to
it.


### each VM uses 100MB of memory


I hadn’t really thought to look at this number before, but each VM as
configured right now seems to use about 100% of memory.


I’m not sure if I can reduce this yet, but 100MB doesn’t really seem like an
unreasonable amount of memory for a whole VM because:

- My kernel is about 30MB and my understanding is that the whole kernel has to
be loaded into memory.
- VMs can’t share memory with each other


So we’re already at 30MB/VM at a minimum.


### I can run about 4 VMs at a time


In my testing so far, I can start about 4 VMs at a time before they start
getting OOM killed by the kernel for using too much memory.


I think I could probably get away with a few more but this isn’t great – I
think I’d definitely need a bigger machine to use this approach.


### why can the Firecracker demo run 4000 VMs?


I still felt a bit confused, because I remembered this [firecracker
demo](https://github.com/firecracker-microvm/firecracker-demo) that said they
could run 4000 VMs at a time. Why did that work?


Then I did the arithmetic and it seems pretty straightforward – they were
running the demo on an `i3.metal` which has 512GB of RAM. So those instances
have 500x more memory than my little DigitalOcean droplet so it makes sense
that they can run about 500x more VMs.


512GB divided 4000 gives each VM about 125MB of memory, which is what I’m
using.


### maybe I’ll use fly.io instead for now


Now I’m looking into using fly.io (which runs Firecracker VMs). We’ll see how that goes!
