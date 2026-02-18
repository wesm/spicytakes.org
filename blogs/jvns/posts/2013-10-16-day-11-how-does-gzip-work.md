---
title: "Day 11: How does gzip work?"
date: 2013-10-16
url: https://jvns.ca/blog/2013/10/16/day-11-how-does-gzip-work/
slug: day-11-how-does-gzip-work
word_count: 337
---


Spoiler: I don’t really know yet, but there is a lot of mucking with bits.


Yesterday I was flailing around a bit looking for projects. Today at
lunch Kat helped me figure one out: writing a parallel version of
[gzip](http://en.wikipedia.org/wiki/Gzip) in
[Julia](http://julialang.org/). Julia is a pretty good choice for this
because it lets you do low-level bit-fiddling and write efficient
algorithms, but still has lots of nice high-level features. It also looks
a lot like Python!


The document I’m using to understand how gzip works is
[this really detailed and wonderful page](http://www.infinitepartitions.com/art001.html).
So if you actually want to know you should just read that.


The basic idea behind gzip is

1. use some not-so-complicated algorithms (Huffman coding, LZ77
compression). These things *sound* like they would be the complicated
part, but so far they don’t seem to be too bad. Conceptually. I think.
2. Do all kinds of bit fiddly things to actually make it efficient.


Some choice things from the article (emphasis mine)

- “hclen is the declaration of *four less than* how many 3-bit length
codes follow” (why four?!??)
- Everything is variable-length encoded, so instead of just having
bytes, you have bit sequences of various lengths that you have to
extract. Because efficiency. Huffman coding is what makes this
variable-length encoding madness actually work.
- Every gzip file begins with the “magic bytes” `1F8B`


Here is a snippet of Julia code that I wrote to work on this! This code takes
an array of 8 bits and converts it into a byte. By default Julia does some
smart things like bounds checking, but you can make this even faster by
preventing bounds checking with `@inbounds`.


You can see that this kind of just looks like Python, except it is fast! (I
promise)


```
function make_int(bv::BitVector)
    num = 0x00
    for i=1:length(bv)
        num = (num << 1) + bv[i]
    end
    return num
end

```


That’s it! Maybe tomorrow I will actually understand how gzip uses Huffman
coding. So far I have *started* to decode the gzip header.
