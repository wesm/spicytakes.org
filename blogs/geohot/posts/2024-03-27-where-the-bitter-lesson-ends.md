---
title: "Where the Bitter Lesson ends"
date: 2024-03-27
url: https://geohot.github.io/blog/jekyll/update/2024/03/27/where-the-bitter-lesson-ends.html
slug: where-the-bitter-lesson-ends
word_count: 596
---

# Where the Bitter Lesson ends

Mar 27, 2024

> Humanity only has one engineering project, building better engineers than humans. After that, the thing we built can do the engineering.

Clips have been making the rounds on Twitter from my second Lex about the “bishop guy” in a chess engine, or a “cone guy” in a self driving car. These engineering ideas look ever more ridiculous.

Since the beginning of comma, I wanted to make a machine that could drive cars like a human. Obviously there’s no reference to traffic cones inside human DNA, they learn about them from data. So there shouldn’t be any reference to traffic cones in your codebase.

Rich Sutton stated this most iconically in 2019.

> One thing that should be learned from the bitter lesson is the great power of general purpose methods, of methods that continue to scale with increased computation even as the available computation becomes very great. The two methods that seem to scale arbitrarily in this way are search and learning.

But then where does it stop? Why draw the line at DNA? Evolution is clearly a search and optimization process. Why is hard coding stuff that’s in the human DNA okay, why not evolve a driving agent? Why not evolve life?

The concept of a Seed AI is very captivating. Build a minimum viable self improving AI, and allow it to bootstrap its way to human and beyond. This is clearly possible, evolution did it (though with an ungodly amount of compute).

But remember, our goal is just to build something superhuman, not go beyond. Unlike a self driving car, if you were building a train driving agent, learning like a human is probably not the right choice. It’s simple enough to code and test. You should have a train_signal.py

Imagine you are tasked with building a radio. Which of these approaches would you take?

* Understanding where radios come from and replicating that. Setting up the same initial conditions of radio, an eccentric Italian man born in 1874, an attic in Pontecchio, an estate owned by the man’s father in Bologna to expand to, etc…
* Taking apart a radio. Reverse engineering and documenting each piece. Building things that behave like each piece. Testing them in the original radio. Building a clone.
I imagine the second path would be more fruitful and faster. We have a working example, we just need to clone it. A much easier task than creating it from scratch.

I say the bitter lesson stops at human DNA. While we have to avoid cargo culting, I think that many of the pieces of the human brain are starting to be buildable with today’s technology. The brain isn’t some hyperelegant machine that captures the essence of learning, it’s a bunch of hacks , and hacks that we can replicate.

Having a cone guy in your self driving car company is still ridiculous, because the only working implementation of a driving agent doesn’t have a cone guy, it learns cones from data. But the only working implementation of engineers do have a neocortex, a hippocampus, a basal ganglia , an amygdala, and a thalamus.

I would be fine with our human agent software having directories for each one of those pieces. Transformers as a neocortex, some way better RAG as a hippocampus, actually working TD-learning as a basal ganglia, an amygdala to prevent the robot destroying itself, and a thalamus to coordinate the system and search.

We are just trying to build knock-off humans, not solve life. They can do that.
