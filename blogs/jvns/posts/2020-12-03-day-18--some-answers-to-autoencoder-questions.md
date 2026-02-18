---
title: "Day 18: an answer to an autoencoder question"
date: 2020-12-03
url: https://jvns.ca/blog/2020/12/03/day-18--some-answers-to-autoencoder-questions/
slug: day-18--some-answers-to-autoencoder-questions
word_count: 205
---


I’m going to keep this one short because I want to get back to coding!


One of the questions I had in the last post was:


> The `Encoder` class in the translation tutorial outputs 2 vectors, an output and a hidden vector. Which one is the encoding, the output or the hidden vector? (or both???)


I’ve been struggling a bit to find out the answers to questions like this –
there are 10 million blogs about deep learning, but somehow I feel like they
often don’t answer my questions. My best strategy so far has to been to search
the PyTorch forums, and that’s how I found the answer to this one! I searched for something like “autoencoder” and found [this answer](https://discuss.pytorch.org/t/gru-time-series-autoencoder/77126/2)


The answer to that question is that the hidden vector is the encoding, and you
just throw out the output.


That answer helped me a LOT and I managed to get a simple autoencoder to work
once I had the answer!  It’s always surprising to me every single time how
helpful it is to focus and articulate the questions I have.


I still don’t know what the `relu` is for, but it’s nice to have the answer to
at least one question.
