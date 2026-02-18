---
title: "Day 30: Making music in Clojure with Overtone. Clojure bugs with laziness! Fun!"
date: 2013-11-19
url: https://jvns.ca/blog/2013/11/19/day-30-making-music-in-clojure-with-overtone/
slug: day-30-making-music-in-clojure-with-overtone
word_count: 308
---


Today I started using a lovely Clojure library called
[Overtone](http://overtone.github.io/), for generating music. It is
pretty easy to use and a fun time. On the box it says that you need to
be “comfortable with” Clojure, the basics of music theory, and the
Supercollider audio synthesis environment. I do not know any of these
things and I successfully made sounds by copying and changing
examples.


I wrote a tiny bit of code to play rhythms. And I ran into my first
clojure bug! I defined a function `side-effecty-thing`, and ran


```
(map side-effecty thing sequence)

```


And that ran fine. It made sounds!


But then I tried something like


```
(def new-function [time]
    (map side-effecty thing sequence)
    (apply-at (+ time 4) '#new-function (+ time 4)))

```


which basically does the `(map side-effecty-thing)` and then calls
itself recursively, later. And this did not make sounds. And I was
TOTALLY CONFUSED, because, it says `(map side-effecty-thing)` in it!
It should make sounds!


But then Travis explained that `map` is lazy and not actually
appropriate if you want the function you are running to *happen* right
away.


So what I actually wanted to use was `doseq`, which will let you
actually make the side-effecty things happen when you ask for them.
And it throws away the result, which is good because I didn’t actually
want the result. Yay!


ALSO EMACS IS ENJOYABLE. Paredit is nice. I am in fact not using Evil
mode. I am using Normal Emacs, with a few packages:

- [Graphene](https://github.com/rdallasgray/graphene), to make
everything a bit prettier
- clojure mode, clojure test mode, and cider, for Clojure fun.
Apparently cider is the thing that people use now and it is the same
as nRepl.


This is a strange and confusing world, humans! I no longer know how to
write if statements without looking it up! Very Exciting Times!
