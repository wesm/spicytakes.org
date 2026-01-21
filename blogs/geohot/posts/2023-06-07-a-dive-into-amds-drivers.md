---
title: "A dive into the AMD driver workflow"
date: 2023-06-07
url: https://geohot.github.io/blog/jekyll/update/2023/06/07/a-dive-into-amds-drivers.html
slug: a-dive-into-amds-drivers
word_count: 516
---

# A dive into the AMD driver workflow

Jun 7, 2023

I ended up getting a response from high level people at AMD. It was still very light on any real technical information, but it did include some great phrases like “I am able to replicate the issues you are facing” and some mockable phrases like “We are hoping that this will improve your perception of AMD products and this will be reflected in your public messaging.”

Though they did end up sending me a ROCm 5.6 driver tarball that seems to be able to run rocm_bandwidth_test and gpu-burn in loops on 2x 7900XTX. So it fixed the main reported issue! Sadly, they asked me not to distribute it, and gave no more details on what the issue is.

A note culturally, I do sadly feel like what they responded to was george is upset and saying bad things about us which is bad for our brand and not holy shit we have a broken driver released panicing thousands of people’s kernels and crashing their GPUs . But it’s a start.

Let’s say, tentatively, that the AMD on MLPerf plan is back on, as I trust they will release this fixed driver.

AMD has two drivers, “amdgpu” and “AMDGPU-Pro”, henceforth “Pro”

Oddly, they appear to both be open source, at least in kernel land, but only amdgpu is in the Linux kernel in drivers/gpu/drm/amd . Pro is packaged as part of ROCm in dkms debs . These are the subfolders

* acp
* amdgpu
* amdkcl (Pro only)
* amdkfd
* backport (Pro only)
* display
* dkms (Pro only)
* include
* pm
So amdgpu appears to be a subset of Pro.

They also release a git repo for the Pro driver, called ROCK-Kernel-Driver .

* 6.0.5.50500-1581431
* 6.0.5.50501-1593694
* 6.1.5.50600-1602498 (the beta version they gave me)
Sadly, the public repo is not kept up to date, the last commit was on Apr 19.

I also know there’s more after Apr 19, because there’s an amd-gfx mailing list! These amdgpu commits are merged into amd-staging-drm-next. Arch even has an AUR for it.

* amdgpu in trunk
* amdgpu in amd-staging-drm-next
I got the amd-staging-drm-next kernel built on Ubuntu, but example ROCm apps refused to run at all. It’s worth investigating exactly what the differences between the ROCK-Kernel-Driver (Pro) and mainline linux trees (amdgpu) are. I’ll add links if anyone has them.

My ask to AMD, why keep the real driver development workflow closed source?

Before my big AMD driver rant , I built master from ROCK-Kernel-Driver (because it’s rude to complain before you try master). I didn’t understand it was actually just the same as amdgpu-dkms from 5.5. Had the 5.6 stuff from the private tarball been pushed, the building of master would have fixed my issues.

Let’s make the driver developed in the open! Cathedral style is no better than NVIDIA . And in order to beat them, you must be playing to win, not just playing not to lose. Combine the driver openness with public hardware docs and you have a competitive advantage.
