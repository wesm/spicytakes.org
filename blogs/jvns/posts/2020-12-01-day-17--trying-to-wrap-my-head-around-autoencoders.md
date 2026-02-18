---
title: "Day 17: trying to wrap my head around autoencoders"
date: 2020-12-01
url: https://jvns.ca/blog/2020/12/01/day-17--trying-to-wrap-my-head-around-autoencoders/
slug: day-17--trying-to-wrap-my-head-around-autoencoders
word_count: 472
---


Hello! Right now I’m back to working on neural networks with sketches of
[faces](https://quickdraw.withgoogle.com/data/face).


### current goal: cluster the faces somehow


As a starting point, I thought it’d be fun to, instead of generating faces, get
the neural network to do some unsupervised clustering of the faces! The idea is:

1. Get the Machine Learning to cluster the faces into groups
2. See if I like the faces in some groups more than others
3. If I do, then maybe just train a model on the cluster of faces that I like


### how do you actually do clustering of a sequence of vectors though?


The usual way to do clustering is with k-means or something, but these drawings
of faces aren’t a single vector, they’re a sequence of vectors! So k-means
wouldn’t make any sense.


I Googled “rnn unsupervised clustering” a little bit and learned about a way to
do this: autoencoders!


It seems like the way an autoencoder works at a high level is:

1. Create “encoder” RNN that translates the input into a lower-dimensional vector (like 4 dimensions or something)
2. Create a “decoder” RNN that translates the 4-dimensional


Train both of them together, with the objective function being something like:


```
loss = F.cross_entropy(decoder(encoder(input)), input)

```


where we try to get `decoder(encoder(x))` as close to `x` as possible.


I found a [tutorial on the PyTorch wiki talking about how to use this encoder /
decoder pattern to do
translation](https://pytorch.org/tutorials/intermediate/seq2seq_translation_tutorial.html)
from French to English.


### questions I still have about autoencoders


I’m still pretty confused about how this encoder / decoder pattern actually
works, and I didn’t get very far on this today. So here are some
questions in the hopes that I can answer them tomorrow!

1. when training, do I need to embed my original input vector into a higher
dimensional space (with a `nn.Embedding`)?  (I don’t think so, because they’re vectors and not
integer labels, but I’m not sure)
2. The `Encoder` class in the translation tutorial outputs 2 vectors, an output
and a hidden vector. Which one is the encoding, the output or the hidden
vector? (or both???)
3. Should my hidden vector have a lot of dimensions (like 50), or should it
have the same number of dimensions as I want classes to categorize my faces
into (like 5?)
4. Both of the examples I’m looking at use a `relu` function as part of their
neural networks. What does `relu` mean?


### tomorrow: maybe write a toy autoencoder!


Maybe tomorrow I’ll try to do a simpler autoencoder example with some toy data,
I think that might clarify things for me! As always trying to use a technique
I don’t understand at all with a complicated dataset is really confusing and
demoralizing, I think if I simplify the dataset a LOT it should go better.
