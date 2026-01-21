---
title: "A Correction on my AI chip thoughts"
date: 2021-12-12
url: https://geohot.github.io/blog/jekyll/update/2021/12/12/a-correction-on-ai-chips.html
slug: a-correction-on-ai-chips
word_count: 409
---

This is a correction to my  [previous post](https://geohot.github.io/blog/jekyll/update/2021/06/13/a-breakdown-of-ai-chip-companies.html)

While my mockery of the startups that have raised 100s of millions of dollars without shipping a product stays, my thoughts on VLIW and big chips were wrong.

I’ve been working more on  [tinygrad](https://github.com/geohot/tinygrad) , and it does seem that the fundamental operation is not like the computation in software 1.0. From  [Jim Keller on Lex](https://www.youtube.com/watch?v=Nb2tebYAaOA) , there’s three fundamental types of compute

**CPU** : add, multiply, load, store, compare, branch (nothing can be known about anything)

**GPU** : add, multiply, load, store (when things happen is known, but the addresses aren’t)

**DSP** : add, multiply (everything is known except the data)

Neural networks are DSPs. All the loads and stores can be statically computed, which isn’t even possible for GPU workloads, never mind CPU ones.

TBH, I didn’t think the problem through well. I assumed that the startups didn’t ship because of bad technical tradeoffs; I was primed to believe this from my experience with self driving. I don’t think that’s the case, and I think they just don’t ship because of the general dysfunction in the economy. They don’t make chips, they make shares.

For deep learning, VLIW is a good idea. Fancy compilers are a good idea. Because it’s not like general purpose compute.  [Rice’s theorem](https://en.wikipedia.org/wiki/Rice%27s_theorem)  doesn’t apply here. In both training and inference, the exact exact same operations are run every time. It’s only the data that changes.

I’m kicking myself for getting this wrong. I wrote  [an accelerator](https://github.com/commaai/openpilot/tree/master/selfdrive/modeld/thneed)  in openpilot based around the idea of the exact same compute every time, and torch 1.10 is adding  [CUDA caching](https://pytorch.org/docs/master/notes/cuda.html#cuda-graphs)  for this. This same idea applies all the way down the stack.

I also didn’t understand the physics of chips and where the power costs are. The key is data locality. Having to move data costs power.

Google got most of these tradeoffs correct with the TPU. I took a look at  [their instruction set](https://github.com/geohot/tinygrad/tree/master/accel/tpu)  and compiler, and while it’s complex, that complexity is only up front to compile the model. After that, it’s way simpler (aka, less power and less issues) at runtime than CUDA and PyTorch.

The only questionable choice is why not take this further? The interconnects between the chips cost power.

As much as I hate to admit it,  [Cerebras](https://cerebras.net)  seems good. The big chip with the local memory is the right tradeoff. You can control 400,000 cores. Too bad you can’t buy one.
