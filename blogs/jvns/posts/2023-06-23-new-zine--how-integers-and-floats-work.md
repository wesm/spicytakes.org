---
title: "New zine: How Integers and Floats Work"
date: 2023-06-23
url: https://jvns.ca/blog/2023/06/23/new-zine--how-integers-and-floats-work/
slug: new-zine--how-integers-and-floats-work
word_count: 796
---


Hello! On Wednesday, we released a new zine: **How Integers and Floats Work**!


You can get it for $12 here:
[https://wizardzines.com/zines/integers-floats](https://wizardzines.com/zines/integers-floats), or get
an [13-pack of all my zines here](https://wizardzines.com/zines/all-the-zines/).


Here’s the cover:


### the table of contents


Here’s the table of contents!


Now let’s talk about some of the motivations for writing this zine!


### motivation 1: demystify binary


I wrote this zine because I used to find binary data really impenetrable. There
are all these 0s and 1s! What does it mean?


But if you look at any binary file format, most of it is integers! For example,
if you look at the DNS parsing in [Implement DNS in a Weekend](https://implement-dns.wizardzines.com/), it’s all about encoding and
decoding a bunch of integers (plus some ASCII strings, which arguably are also arrays of integers).


So I think that learning how integers work in depth is a really nice way to get
started with understanding binary file formats. The zine also talks about some
other tricks for encoding binary data into integers with binary operations and
bit flags.


### motivation 2: explain floating point


The second motivation was to explain floating point. Floating point is pretty
weird! (see [examples of floating point problems](https://jvns.ca/blog/2023/01/13/examples-of-floating-point-problems/)
for a very long list)


And almost all explanations of floating point I’ve read have been really math
and notation heavy in a way that I find pretty unpleasant and confusing, even
though I love math more than most people (I did a pure math degree) and am
pretty good at it.


We spent weeks working on a clearer explanation of floating point with minimal
math jargon and lots of pictures and I think we got there. Here’s one example page, on
the floating point number line:


![](https://wizardzines.com/zines/integers-floats/samples/2-floating-point.png)


### it comes with a playground: memory spy!


One of my favourite ways to learn about how my computer represents things in
memory has been to use a debugger to look at the memory of a real program.


But C debuggers like gdb are pretty hard to use at first! So
[Marie](https://marieflanagan.com/) and I made a playground called [Memory Spy](https://memory-spy.wizardzines.com/). It runs a C debugger behind the
scenes, but it provides a much simpler interface – there are a bunch of
very simple example C programs, and you can just click on each line to view how
the variable on that line is represented in memory.


Here’s a screenshot:


![](https://jvns.ca/images/memory-spy.png)


Memory Spy is inspired by Philip Guo’s great [Python Tutor](https://pythontutor.com/).


### float.exposed is great


When doing demos and research for this zine, I found myself reaching for
[float.exposed](https://float.exposed/) a lot to show how numbers are encoded
in floating point. It’s by [Bartosz Ciechanowski](https://ciechanow.ski/), who has tons of other great visualizations on his site.


I loved it so much that I made a clone called [integer.exposed](https://integer.exposed) for
integers (with permission), so that people could look at integers in a similar way.


### some blog posts I wrote along the way


Here are a few blog posts I wrote while thinking about how to write this zine:

- [examples of floating point problems](https://jvns.ca/blog/2023/01/13/examples-of-floating-point-problems/)
- [examples of problems with integers](https://jvns.ca/blog/2023/01/18/examples-of-problems-with-integers/)
- [some possible reasons for 8-bit bytes](https://jvns.ca/blog/2023/03/06/possible-reasons-8-bit-bytes/)


### you can get a print copy shipped to you!


There’s always been the option to print the zines yourself on your home
printer.


But this time there’s a new option too: you can get a print copy shipped to
you! (just click on the “print version” link on [this page](https://wizardzines.com/zines/integers-floats/))


The only caveat is print orders will ship in **August** – I
need to wait for orders to come in to get an idea of how many I should print
before sending it to the printer.


### people who helped with this zine


I don’t make these zines by myself!


I worked with [Marie LeBlanc Flanagan](https://marieflanagan.com/) every
morning for 5 months to clarify explanations and build [memory spy](https://memory-spy.wizardzines.com).


The cover is by Vladimir Kašiković, Gersande La Flèche did copy editing, Dolly
Lanuza did editing, another friend did technical review.


[Stefan Karpinski](https://karpinski.org/) gave a talk 10 years ago at the Recurse Center (I even [blogged about it at the time](https://jvns.ca/blog/2013/11/13/day-27-magic-testing-functions/))
which was the first explanation of floating point that ever made any sense to
me. He also explained how signed integers work to me in a Mastodon post a few
months ago, when I was in the middle of writing the zine.


And finally, I want to thank all the beta readers – 60 of you read the zine and left
comments about what was confusing, what was working, and ideas for how to make
it better. It made the end product so much better.


### thank you


As always: if you’ve bought zines in the past, thank you for all your support
over the years. I couldn’t do this without you.
