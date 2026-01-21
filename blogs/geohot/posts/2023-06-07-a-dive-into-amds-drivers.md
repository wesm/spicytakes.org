---
title: "A dive into the AMD driver workflow"
date: 2023-06-07
url: https://geohot.github.io/blog/jekyll/update/2023/06/07/a-dive-into-amds-drivers.html
slug: a-dive-into-amds-drivers
word_count: 505
---

I ended up getting a response from high level people at AMD. It was still very light on any real technical information, but it did include some great phrases like “I am able to replicate the issues you are facing” and some mockable phrases like “We are hoping that this will improve your perception of AMD products and this will be reflected in your public messaging.”

Though they did end up sending me a ROCm 5.6 driver tarball that seems to be able to run  [rocm_bandwidth_test](https://github.com/RadeonOpenCompute/rocm_bandwidth_test)  and  [gpu-burn](https://github.com/ROCm-Developer-Tools/HIP-Examples/tree/master/gpu-burn)  in loops on 2x 7900XTX. So it fixed the main reported issue! Sadly, they asked me not to distribute it, and gave no more details on what the issue is.

A note culturally, I do sadly feel like what they responded to was  *george is upset and saying bad things about us which is bad for our brand*  and not  *holy shit we have a broken driver released panicing thousands of people’s kernels and crashing their GPUs* . But it’s a start.

Let’s say, tentatively, that the AMD on MLPerf plan is back on, as I trust they will release this fixed driver.

AMD has two drivers, “amdgpu” and “AMDGPU-Pro”, henceforth “Pro”

Oddly, they appear to both be open source, at least in kernel land, but only amdgpu is in the Linux kernel in  `drivers/gpu/drm/amd` . Pro is packaged as part of ROCm in  [dkms debs](https://repo.radeon.com/amdgpu/5.5.1/ubuntu/pool/main/a/amdgpu-dkms/) . These are the subfolders

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

They also release a git repo for the Pro driver, called  [ROCK-Kernel-Driver](https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver) .

* [6.0.5.50500-1581431](https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/tree/rocm-5.5.0/drivers/gpu/drm/amd)
* [6.0.5.50501-1593694](https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/tree/rocm-5.5.1/drivers/gpu/drm/amd)
* 6.1.5.50600-1602498 (the beta version they gave me)

Sadly, the public repo is not kept up to date, the last commit was on Apr 19.

I also know there’s more after Apr 19, because there’s an  [amd-gfx](https://lists.freedesktop.org/mailman/listinfo/amd-gfx)  mailing list! These amdgpu commits are merged into amd-staging-drm-next. Arch even has an  [AUR](https://aur.archlinux.org/packages/linux-amd-staging-drm-next-git)  for it.

* [amdgpu in trunk](https://github.com/torvalds/linux/tree/master/drivers/gpu/drm/amd)
* [amdgpu in amd-staging-drm-next](https://gitlab.freedesktop.org/agd5f/linux/-/tree/amd-staging-drm-next/drivers/gpu/drm/amd)

I got the amd-staging-drm-next kernel built on Ubuntu, but example ROCm apps refused to run at all. It’s worth investigating exactly what the differences between the ROCK-Kernel-Driver (Pro) and mainline linux trees (amdgpu) are. I’ll add links if anyone has them.

My ask to AMD, why keep the real driver development workflow closed source?

Before my  [big AMD driver rant](https://www.youtube.com/watch?v=Mr0rWJhv9jU) , I built master from  [ROCK-Kernel-Driver](https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver)  (because it’s rude to complain before you try master). I didn’t understand it was actually just the same as amdgpu-dkms from 5.5. Had the 5.6 stuff from the private tarball been pushed, the building of master would have fixed my issues.

Let’s make the driver developed in the open! Cathedral style is no better than  [NVIDIA](https://github.com/NVIDIA/open-gpu-kernel-modules) . And in order to beat them, you must be playing to win, not just playing not to lose. Combine the driver openness with public  [hardware docs](https://www.intel.com/content/www/us/en/docs/graphics-for-linux/developer-reference/1-0/alchemist-arctic-sound-m.html)  and you have a competitive advantage.
