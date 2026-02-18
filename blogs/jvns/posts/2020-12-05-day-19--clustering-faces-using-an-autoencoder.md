---
title: "Day 19: Clustering faces (poorly) using an autoencoder"
date: 2020-12-05
url: https://jvns.ca/blog/2020/12/05/day-19--clustering-faces-using-an-autoencoder/
slug: day-19--clustering-faces-using-an-autoencoder
word_count: 429
---


I’ve been working on clustering faces using an autoencoder, and I finally have
some fun screenshots to share so here they are.


### our training data: faces


Our input data looks like this: (from the [google quickdraw dataset](https://quickdraw.withgoogle.com/data/face))


![](https://jvns.ca/images/faces1.png)


Each face is represented as a sequence of vectors, one vector for every
line in the face (kind of like an SVG path). Here’s an example:


```
tensor([[-0.0956, -0.2869,  0.0000],
        [-0.3108, -0.1434,  0.0000],
        [-0.5738,  0.1673,  0.0000],
        [-0.3108,  0.2391,  0.0000],
        [-0.3586,  0.4303,  0.0000],
        ... lots more ...

```


# the idea: many vectors -> one vector -> many vectors


The way RNN autoencoders work that there’s an `Encoder` RNN that turns this
sequence of vectors into 1 vector (mine is 50 dimension), and then a `Decoder`
RNN that turns the 1 vector back into a sequence of vectors.


The idea is to train the Encoder and Decoder networks so that
`Decoder(Encoder(x))` is as close to `x` as possible for every `x` in the
training set. I used the mean squared error as a loss function to start.


The training didn’t go that well – I got the loss to go down a bit (from 0.3
to 0.25), but it definitely didn’t seem that well trained. I think it would
have maybe done better if I trained it for longer but I got bored.


### the autoencoder results


Here are 4 pairs of `x` and `Decoder(Encoder(x))` from the training set


![](https://jvns.ca/images/autoencoder-result.png)


I’m actually pretty impressed by this – it seems to have figured how to draw a
circle of about the right size for the face, and vaguely that it should draw
something inside the circle. Way better than nothing!


### doing some clustering


My original goal was to cluster the faces by taking `Encoder(x)` for the inputs
in the training set  and clustering those vectors.


I used
[DBSCAN](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html)
from scikit-learn more or less arbitrarily, basically because it seemed like it
might work better for higher dimensional vectors (I had 50 dimensions)


here’s what the clusters looked like:


![](https://jvns.ca/images/clusters.png)


It seems to have clustered them mostly by the size of the face, and not by any
of the interior features. This makes sense because the decoder seems to be able
to reproduce the size of the face pretty effectively but totally fails at
reproducing the interior features. Neat!


### next: see if I can get it to draw some eyes


My next goal I think is to see if I can improve the autoencoder network so that
it can also draw the components inside the face better. We’ll see how it goes!
