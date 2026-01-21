---
title: "Can tinygrad win?"
date: 2025-07-06
url: https://geohot.github.io/blog/jekyll/update/2025/07/06/can-tinygrad-win.html
slug: can-tinygrad-win
word_count: 711
---

This is not going to be a cakewalk like self driving cars. Most of comma’s competition is now out of business, taking billions and billions of dollars with it. Re: Tesla and FSD, we always expected Tesla to have the lead, but it’s not a winner take all market, it will look more like iOS vs Android. comma has been around for 10 years, is profitable, and is now growing rapidly. In self driving, most of the competition wasn’t even playing the right game.

This isn’t how it is for ML frameworks. tinygrad’s competition is playing the right game, open source, and run by some quite smart people. But this is my second startup, so hopefully taking a bit more risk is appropriate.

For comma to win, all it would take is people in 2016 being wrong about LIDAR, mapping, end to end, and  [hand coding](http://www.incompleteideas.net/IncIdeas/BitterLesson.html) , which hopefully we all agree now that they were. For tinygrad to win, it requires something much deeper to be wrong about  *software development in general* .

As it stands now, tinygrad is 14556 lines. Line count is not a perfect proxy for complexity, but when you have differences of multiple orders of magnitude, it might mean something. I asked ChatGPT to estimate the lines of code in PyTorch, JAX, and MLIR.

* JAX = 400k
* MLIR = 950k
* PyTorch = 3300k

They range from one to two orders of magnitude off. And this isn’t even including all the libraries and drivers the other frameworks rely on, CUDA, cuBLAS, Triton, nccl, LLVM, etc…. tinygrad includes every single piece of code needed to drive an AMD RDNA3 GPU except for LLVM, and we plan to remove LLVM in a year or two as well.

But so what? What does line count matter? One hypothesis is that tinygrad is only smaller because it’s not speed or feature competitive, and that if and when it becomes competitive, it will also be that many lines. But I just don’t think that’s true. tinygrad is already feature competitive, and for speed, I think the bitter lesson also applies to software.

When you look at the machine learning ecosystem, you realize it’s just the same problems over and over again. The problem of multi machine, multi GPU, multi SM, multi ALU, cross machine memory scheduling, DRAM scheduling, SRAM scheduling, register scheduling, it’s all the same underlying problem at different scales. And yet, in all the current ecosystems, there are completely different codebases and libraries at each scale.

I don’t think this stands. I suspect there is a simple formulation of the problem underlying all of the scheduling. Of course, this problem will be in NP and hard to optimize, but I’m betting the bitter lesson wins here. The goal of the tinygrad project is to abstract away everything except the absolute core problem in the cleanest way possible.

This is why we need to replace everything. A model for the hardware is simple compared to a model for CUDA. If we succeed, tinygrad will not only be the fastest NN framework, but it will be under 25k lines all in, GPT-5 scale training job to MMIO on the PCIe bus!

Here are the steps to get there:

1. Expose the underlying search problem spanning several orders of magnitude. Due to the execution of neural networks not being data dependent, this problem is very amenable to search.
2. Make sure your formulation is simple and complete. Fully capture all dimensions of the search space. The optimization goal is simple, run faster.
3. Apply the state of the art in search. Burn compute. Use LLMs to guide. Use SAT solvers. Reinforcement learning. It doesn’t matter, there’s no way to cheat this goal. Just see if it runs faster.

If this works, not only do we win with tinygrad, but hopefully people begin to rethink software in general. Of course, it’s a big if, this isn’t like comma where it was hard to lose. But if it wins…

The main thing to watch is development speed. Our bet has to be that tinygrad’s development speed is outpacing the others. We have the  [AMD contract](https://x.com/__tinygrad__/status/1935364905949110532)  to train LLaMA 405B as fast as NVIDIA due in a year, let’s see if we succeed.
