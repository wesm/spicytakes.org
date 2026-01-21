---
title: "Brain FLOPS"
date: 2022-02-17
url: https://geohot.github.io/blog/jekyll/update/2022/02/17/brain-flops.html
slug: brain-flops
word_count: 106
---

# Brain FLOPS

Feb 17, 2022

Google “energy for neuron firing” and you get:

> In final, the energy supply to a neuron by ATP during one action potential is 2.468 × 10^−7 J

This means that assuming the brain is drawing 20W, that’s 81M firing events per second.

Assuming each neuron has a fan-out of 1000, aka 1000 MACs, that’s 2000 FLOPS per neuron. That’s only 162 GFLOPS…to be fair, they are sparse. But a far cry from 20 PFLOPS, the classic estimate of brain compute. Even assuming they use 1% 1’s, that’s still only 16 TFLOPS.

Maybe a 3090 is already a human brain.
