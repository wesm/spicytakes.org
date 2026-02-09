---
title: "Deep Latent Space Maps"
date: 2019-03-06
url: https://blog.mempko.com/deep-latent-space-maps/
slug: deep-latent-space-maps
word_count: 612
tags: ['#wordpress', '#Import 2024-11-03 23:36']
---



As I watch my children grow up, I am always amazed at their pace of learning. It turns out by 18 the average person learns about 60,000 words which average about 9 words a day. Typically these new words are learned by as little as one example of the thing or concept learned. Anyone working in the AI field understands that one huge drawback of the latest NN based learning systems is that the number of examples the system needs to learn a label is enormous. Typically, in the thousands to millions of examples, which is often out of reach for most researchers in the field, which is why there are public datasets used by researchers (TIMIT, MNIST, and ImageNet, ActivityNet, etc.) for training and testing new models.


I think it’s clear to most researchers that Deep Learning has a deep problem because these systems learn in clearly inferior ways. As I watch my children learn, I am deeply unsatisfied with current techniques and know there must be a better way. I am not the only one who feels this way, and many started looking at older ideas in ML to combine them with Deep Learning (Deep Learning itself is an old idea).


There is some [exciting research](https://numenta.com/neuroscience-research/research-publications/papers/a-framework-for-intelligence-and-cortical-function-based-on-grid-cells-in-the-neocortex/?ref=blog.mempko.com) coming out suggesting that there are these grid cells which represent objects in many domains, and they take input from the senses and vote on the best model of the world they are perceiving.  This research seems to partly validate Geoffrey Hinton’s idea of capsule networks which take many models and vote on a prediction to higher level features. Typically the capsules vote for manually selected features like the position and orientation of an object in Hinton’s case. It seems we can learn the features instead because it’s possible the brain uses grid cells to map to features in an abstract latent space.


One promising approach to learning this mapping is to use deep learning to learn embeddings from some medium, to take input data and map it to some latent space. This is called Deep Feature Extraction. Such a trained network can convert an image, sound, or text into a Feature Vector. This technique is useful because this can be done unsupervised only requiring many examples of data (images, sound, text, ext) instead of labeled ground truth. These learned feature vectors are then typically used downstream by some other technique (xgboost, svm) to learn labels.


One area I want to explore is to take Peter Gärdenfors idea of a [Conceptual Space](https://en.wikipedia.org/wiki/Conceptual_space?ref=blog.mempko.com) and combine it with deep feature extraction and Geoffrey Hinton’s idea of [capsule networks](https://en.wikipedia.org/wiki/Capsule_neural_network?ref=blog.mempko.com). What I want to do is to use deep feature extraction to produce feature vectors in latent space. Then the Labeled data can be used to map out the latent space over several domains using [Voronoi space partitioning](https://en.wikipedia.org/wiki/Voronoi_diagram?ref=blog.mempko.com). You can then train many of these mappings into the domain of your choosing and use a voting mechanism to extract the probable labels. I call the latent space partitioning using labeled domains **Deep Latent Space Maps**.


The devil is in the details, but in principle, a learning system becomes creating these **Deep Latent Space Maps**. Classification is then taking the inputs through all the mappers and using the voting mechanism to extract the probable labels. In other words, you can train it using only as little as one example of an object, word or thing. As more examples are provided, the map can be re-adjusted to take in the new information. The interesting bit here is to explore using Peter Gärdenfors idea of how learning works in our brain which new research is increasingly validating. It just feels right.

