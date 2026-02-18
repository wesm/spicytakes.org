---
title: "New playground: integer.exposed"
date: 2023-04-19
url: https://jvns.ca/blog/2023/04/19/new-playground-integer-exposed/
slug: new-playground-integer-exposed
word_count: 659
---


Hello! For the last few months we’ve been working on a zine about how integers
and floating point numbers work. Whenever I make a zine I like to release a
playground to go with it, like [mess with dns](https://messwithdns.net/) for the DNS zine or the [sql playground](https://sql-playground.wizardzines.com/).


For this one, I made a simple playground called [integer.exposed](https://integer.exposed), inspired by
Bartosz Ciechanowski’s [float.exposed](https://float.exposed).


It’s a lot less elaborate than Mess With DNS, so I’ll keep this blog post short.


### the inspiration: float.exposed


I did a couple of talks about how integers and floating point work last month,
and in the talk about floating point I found myself CONSTANTLY referring to
this site called [Float Exposed](https://float.exposed/) by Bartosz Ciechanowski to demonstrate various things. (Aside: If you haven’t seen
Ciechanowski’s incredible [interactive explainers](https://ciechanow.ski/archives/) on bicycles, mechanical watches,
lenses, the internal combustion engine, and more, you should check them out!)


Here’s what it it looks like:


![](https://jvns.ca/images/float-exposed.png)


Things I’ve done with it:

- Increment the significand of a float (to show people how close together successive floats are)
- Show special values like [NaN](https://float.exposed/0x7ff8000000000000) and [infinity](https://float.exposed/0x7ff0000000000000), and show how if you change the bits in NaN, it’s still NaN
- Go to a [large integer value](https://float.exposed/0x43abc16d674ec801) and show how the distance between floats is very large
- Show how you get drastically different precision for [one million as a 32-bit float](https://float.exposed/0x4b189680) and as a [64-bit float](https://float.exposed/0x416312d000000000) (try incrementing the significand for each one!)


and lots more! It’s an incredible way to get hands on with floats and improve your intuition around how they work.


### float.exposed, but for integers


Integers aren’t as complicated as floats, but there are some nonobvious things
about them: you have signed integers and unsigned integers, you have
endianness, and there are some weird operations like right/left shift. So when
I was talking about integers, I found myself wanting a similar website to
[float.exposed](https://float.exposed) to demonstrate things.


So with permission, I put one together at [integer.exposed](https://integer.exposed). Here’s a screenshot:


![](https://jvns.ca/images/int-exposed.png)


The UI is a little different: integers don’t have many different parts the way
floating point numbers do, so there’s a single row of buttons that you can use
to do various operations on the integer.


A note on byte order: Like float.exposed, it uses a big endian byte order,
because I think it’s more intuitive to read. But you do have to keep in mind
that on most computers the bytes will actually be in the reverse order.


### some interesting things to try


Here are some things I think are fun to try:

1. **signed integers**: Look at how [-1](https://integer.exposed/#0xff) is
represented. Increment and decrement it a few times and see how the signed
and unsigned values change. Do the same with
[-128](https://integer.exposed/#0x80). Also look at how -1 is represented as
a 16/32/64-bit integer.
2. **signed/unsigned right shift**: Similarly with [-1](https://integer.exposed/#0xffff): try out signed right shift (also known as “arithmetic right shift”) and see how the result is different from unsigned right shift (aka “logical right shift”).
3. **counting in binary**: Start at [0](https://integer.exposed/#0x00) and increment a bunch of times and watch the binary value count up.
4. **not**: Take any number (like [123](https://integer.exposed/#0x7b)) and NOT it. See how `NOT` is almost exactly the same as negation, but not quite.
5. **swap the byte order**. Take a number like [12345678](https://integer.exposed/#0x4e61bc00) and see how if you swap the byte order, the result is an unrecognizably different number.
6. look at how [powers of 2 are represented](https://integer.exposed/#0x00000800)


### the tech stack


As usual for me it uses Vue.js. If you want to see how it works you can just
view source – it’s only two files, `index.html` and `script.js`.


I took a bunch of the CSS from [float.exposed](https://float.exposed).


### that’s all!


Let me know if you notice any bugs! I might add more features, but I want to keep it pretty simple.


I’ve also built another more involved playground that I’m hoping to release and
write up soon.
