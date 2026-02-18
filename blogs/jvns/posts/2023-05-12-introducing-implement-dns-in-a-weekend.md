---
title: "Introducing 'Implement DNS in a Weekend'"
date: 2023-05-12
url: https://jvns.ca/blog/2023/05/12/introducing-implement-dns-in-a-weekend/
slug: introducing-implement-dns-in-a-weekend
word_count: 904
---


Hello! I’m excited to announce a project I’ve been working on for a long time:
a free guide to implementing your own DNS resolver in a weekend.


The whole thing is about 200 lines of Python, including implementing all of the
binary DNS parsing from scratch. Here’s the link:

>>
[Implement DNS in a Weekend](https://implement-dns.wizardzines.com)
<<

This project is a fun way to learn:

- How to parse a binary network protocol like DNS
- How DNS works behind the scenes (what’s actually happening when you make a DNS query?)


The testers have reported that it takes around 2-4 hours to do in Python.


### what’s a DNS resolver?


A DNS resolver is a program that knows how to figure out what the IP address
for a domain is. Here’s what the command line interface of the resolver you’ll
write looks like:


```
$ python3 resolve.py example.com
93.184.216.34

```


### implementing DNS gives me an amazing sense of confidence


In [Learning DNS in 10 years](https://jvns.ca/blog/2023/05/08/new-talk-learning-dns-in-10-years/), I
talked about how having implemented a toy version of DNS myself from scratch gives
me an unparalleled sense of confidence in my understanding of DNS.


So this guide is my attempt to share that sense of confidence with you all.


Also, if you’ve bought [How DNS Works](https://wizardzines.com/zines/dns), I think
this guide is a nice companion – you can implement your own DNS
resolver to solidify your understanding of the concepts in the zine.


### it’s a Jupyter notebook


In this guide, I wanted to mix code that you could run with explanations. I
struggled to figure out the right format for months, and then I finally thought
of using a [Jupyter notebook](https://jupyter.org/)! This meant that I could easily check that all of
the code actually ran.


I used [Jupyter Book](https://jupyterbook.org) to convert the Jupyter notebooks
into a website. It reruns the notebook before converting it to HTML, so I could
easily guarantee that all of the code actually runs and outputs what it says
that it outputs. I ended up hacking the theme a lot to make it more minimal, as
well as doing some terrible things with Beautiful Soup to get a table of
contents that shows you the global TOC as well as the page’s local section
headings all in one place.


You can also download the Jupyter notebooks and run them on your own computer
if you’d like, using the “download the code” button on the [homepage](https://implement-dns.wizardzines.com/).


### why Python?


I used Python for this guide instead of a lower-level language like Go or Rust
to make it more approachable – when I started learning networking 10 years
ago, I didn’t really know any systems languages well, and I found them kind of
intimidating. Implementing [traceroute using scapy in Python](https://jvns.ca/blog/2013/10/31/day-20-scapy-and-traceroute/)  felt
much less scary.


You can very easily pack/unpack binary data in Python with `struct.pack` and
`struct.unpack`, so Python being a higher-level language doesn’t really cause
any problems.


The idea is that you can either follow the guide in Python (which is the
easiest mode), or if you want a bigger challenge, you can translate the code to
any language you’d like. (Go? Javascript? Rust? Bash? Lua? Ruby?)


### only the standard library


It was important to me to really show how to implement DNS “from scratch”, so
the guide only uses a few very basic standard library modules: `struct`,
`socket`, `io`, `random`, and `dataclasses`.


Here’s what we use each module for:

- `random` is used for generating DNS query IDs
- `socket` is used to make a UDP connection
- `struct` is used for converting to/from binary (`struct.pack` and `struct.unpack`)
- `dataclasses` are used to make serializing / deserializing records a little more ergonomic
- `io` is used for `BytesIO`, which gives us a reader interface which stores a
pointer to how much of the packet we’ve read so far. If I were implementing
DNS in a language that didn’t have this kind of reader interface, I might
implement my own.


### it includes some bonus exercises


The toy DNS resolver is obviously missing a bunch of important features, so
I’ve added some exercises at the end with examples of features you could add
(and bugs you could fix) to make it a little more like a “real” DNS resolver.


This list isn’t particularly exhaustive though, and I’d love to hear other
ideas for relatively-easy-to-implement DNS resolver features I’ve missed.


### next goal: TLS


I’ve actually written toy implementations of a bunch of other network protocols
in Python (ICMP, UDP, TCP, HTTP, and TLS), and I’m hoping to release “Implement
TLS in a weekend” at some point.


No promises though – I have another zine to finish writing first (on all the
surprising things about how integers and floats work on computers), and a toy
TLS implementation is quite a bit more involved than a toy DNS implementation.


### thanks to the beta testers


Thanks to everyone (Atticus, Miccah, Enric, Ben, Ben, Maryanne, Adam, Jordan,
and anyone else I missed) who tested this guide and reported confusing or
missing explanations, mistakes, and typos.


Also a huge thanks to my friend Allison Kaptur who designed the first “Domain
Name Saturday” workshop with me at the Recurse Center in 2020.


The name was inspired by [Ray Tracing in One Weekend](https://raytracing.github.io/).


### here’s the link again


Here’s the link to the guide again if you’d like to try it out:

>>
[Implement DNS in a Weekend](https://implement-dns.wizardzines.com)
<<