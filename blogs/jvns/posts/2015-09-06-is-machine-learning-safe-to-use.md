---
title: "Is machine learning safe to use?"
date: 2015-09-06
url: https://jvns.ca/blog/2015/09/06/is-machine-learning-safe-to-use/
slug: is-machine-learning-safe-to-use
word_count: 189
---


I’ve been thinking about this a lot because I do ML at work. here are a few of my
current thoughts. I’d like to hear what you think
[on twitter](https://twitter.com/b0rk/status/640536115091521536) – I think  being responsible for the accuracy of a system that you don’t fully understand is scary/ very interesting.


![](https://jvns.ca/images/ml_safe.jpg)


transcript:


**FIRST**: Can you understand your model? A regression with 10 variables is easy; a big random forest isn’t.


A model you don’t understand is

- **awesome**. It can perform really well, and you can save time at first by ignoring the details.
- **scary**. It will make unpredictable and sometimes embarrassing mistakes. You’re responsible for them.
- **only as good as your data**. Often when I train a new model I think at some point “NO PLZ DON’T USE THAT DATA TO MAKE DECISION OH NOOOOO”


Some way to make it less scary:

- have a human **double check** the scariest choices
- use complicated models when it’s okay to make unpredictable mistakes, simple models when it’s less okay
- use ML for research, learn why it’s doing better, incorporate your findings into a less complex system
