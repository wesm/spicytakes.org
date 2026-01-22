---
title: "We should not describe LRM’s as “thinking”"
date: 2025-06-17
url: https://mathbabe.org/2025/06/17/we-should-not-describe-lrms-as-thinking/
word_count: 773
---


Yesterday I read a paper that’s seemingly being taken very seriously by some folks in the LLM/LRM developer community (maybe because it was put out by Apple). It’s called


[The Illusion of Thinking:
Understanding the Strengths and Limitations of Reasoning Models
via the Lens of Problem Complexity](https://ml-site.cdn-apple.com/papers/the-illusion-of-thinking.pdf)


In it, the authors pit Large Language Models (LLMs) against Large Reasoning Models (LRMs) (these are essentially LLMs that have been fine-tuned to provide reasoning in steps) and notice that, for dumb things, the LLM’s are better at stuff, then for moderately complex things, the LRMs are better, then when you get sufficiently complex, they both fail.


This seems pretty obvious, from a pure thought experiment perspective: why would we think that LRMs are better no matter what complexity? It stands to reason that, at some point, the questions get too hard and they cannot answer them, especially if the solutions are not somewhere on the internet.


But the example they used – or at least one of them – made me consider the possibility that their experiments were showing something even more interesting, and disappointing, than they realized.


Basically, they asked lots of versions of LLMs and LRMs to solve the Tower of Hanoi puzzle for n discs, where n got bigger. They noticed that all of them failed when n got to be 10 or larger.


They also did other experiments with other games, but I’m going to focus on the Tower of Hanoi.


Why? Because it happens to be the first puzzle I ever “got” as a young mathematician. I must have been given one of these puzzles as a present or something when I was like 8 years old, and I remember figuring out how to solve it and I remember proving that it took 2^n-1 moves to do it in general, for n discs.


It’s not just me! This is one of the most famous and easiest math puzzles of all time! There must be thousands of math nerds who have blogged at one time or another about this very topic. Moreover, the way to solve it for n+1 discs is insanely easy if you know how to solve it for n discs, which is to say it’s iterative.


Another way of saying this is that, it’s actually not harder, or more complex, to solve this for 10 discs than it is for 9 discs.


Which is another way of saying, the LRMs really do not understand all of those blogposts they’ve been trained on explicitly, and thus have not successfully been shown to “think” at all.


And yet, this paper, even though it’s a critique of the status quo thinking around LRMs and LLMs and the way they get trained and the way they get tested, still falls prey to the most embarrassing mistake, namely of assuming the pseudo-scientific marketing language of Silicon Valley, wherein the models are considered to be “thinking”.


There’s no real mathematical thinking going on here, because there’s no “aha” moment when the model actually understands the thousands of explanations of proofs of how to solve the Tower of Hanoi that it’s been trained on. To test that I talked to my 16-year-old son this morning before school. It took him about a minute to get the lay of the land and another two minutes to figure out the iterative solution. After that he knew exactly how to solve the puzzle for any n. That’s what an “aha” moment looks like.


And by the way, the paper also describes the fact that one reason LRMs are not as good at simple problems as LLMs is that they tend to locate the correct answer, and then keep working and finally output a more complicated, wrong answer. That’s another indication that they do not actually understand anything.


In conclusion, let’s not call these things thinking. They are not. They are, as always, predicting the next word in someone’s blog post who is writing about the Towers of Hanoi.


One last point, which is more of a political positioning issue. Sam Altman has been known to say he doesn’t worry about global climate change because, once the AI becomes super humanly intelligent, *we will just ask it how to solve climate change*. I hope this kind of rhetoric is exposed once and for all, as a money and power grab and nothing else. If AI cannot understand the simplest and most mathematical and sanitary issue such as the Tower of Hanoi for n discs, it definitely cannot help us out of an enormously messy human quagmire that will pit different stakeholder groups against each other and cause unavoidable harm.
