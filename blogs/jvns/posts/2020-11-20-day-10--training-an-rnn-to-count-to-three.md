---
title: "Day 10: Training an RNN to count to three"
date: 2020-11-20
url: https://jvns.ca/blog/2020/11/20/day-10--training-an-rnn-to-count-to-three/
slug: day-10--training-an-rnn-to-count-to-three
word_count: 265
---


Yesterday I was trying to train an RNN to generate English that sounds kind of
like Shakespeare. That was not working, so today I instead tried to do
something MUCH simpler: train an RNN to generate sequences like


```
0 1 2 0 1 2 0 1 2 0 1 2

```


and slightly more complicated sequences like


```
0 1 2 1 0 1 2 1 0 1 2 1 0 1 2 1 0

```


I used (I think) the exact same RNN that I couldn’t get to work yesterday to
generate English by training it on Shakespeare, so it was cool to see that I could at least use it for
this much simpler task (memorize short sequences of numbers).


### the jupyter notebook


It’s late so I won’t explain all the code in this blog
post, but here’s the PyTorch code I wrote to train the RNN to count to three.

- Here it is as a [github gist](https://gist.github.com/jvns/b8804fb9d0672ce147a28d22648b4bd7)
- and [here it is on Colab](https://colab.research.google.com/gist/jvns/b8804fb9d0672ce147a28d22648b4bd7/rnn-123.ipynb) if you want to run it yourself


In the gist there are a few experiments with different sequence lengths, like
(unsurprisingly) it takes longer to train it to memorize a sequence of length
20 than a sequence of length 5.


### simplifying is nice


I’m super happy that I got an RNN to do something that I actually understand! I
feel pretty hopeful that on Monday I’ll be able to go back to the character RNN
problem of trying to get the RNN to generate English words now that I have this simpler thing working.
