---
title: "Day 16: gzip + poetry = awesome"
date: 2013-10-24
url: https://jvns.ca/blog/2013/10/24/day-16-gzip-plus-poetry-equals-awesome/
slug: day-16-gzip-plus-poetry-equals-awesome
word_count: 195
---


Gzip compresses by replacing text with pointers to earlier parts of the text.
Here’s a visualization of what actually happens when you decompress “The
Raven”. It highlights the bits of text that are copied from previously in the
poem.


I showed this as a Thursday talk at Hacker School today :) I really like how
you can see the rhyming inside the poem like (rapping… tapping) come out in
the compression algorithm.


No sound, just gzip.


You can try it out if you want by cloning
[https://github.com/jvns/gzip.jl](https://github.com/jvns/gzip.jl) and
checking out the ‘visualization’ branch.


*Edit:* Thanks to a suggestion in the comments, here’s [the whole poem](https://rawgithub.com/jvns/7155528/raw/ef9785f023fc68d78dc4f61e732007149eec1e69/raven.html) and [Hamlet](http://rawgithub.com/jvns/7155528/raw/8b6e49a1fb99cb919a30a73262894d041e41ce91/hamlet-gzip.html).


*Edit:* Some clarifications, for the interested:


I implemented gunzip from scratch to learn how it works. This visualization is
a small hack on top of that, just adding some print and sleep statements. You can
see [the source code](https://github.com/jvns/gzip.jl/blob/visualization/gzip.jl#L360)
that produces it.


This in fact shows how LZ77 compression works, which is the first step of gzip
(or DEFLATE) compression. The second step is Huffman coding and isn’t shown in
the video at all :). If you want to know more,
try this [excellent but very long page](http://www.infinitepartitions.com/art001.html).
