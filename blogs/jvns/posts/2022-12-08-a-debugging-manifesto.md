---
title: "A debugging manifesto"
date: 2022-12-08
url: https://jvns.ca/blog/2022/12/08/a-debugging-manifesto/
slug: a-debugging-manifesto
word_count: 731
---


Hello! I’ve been working on a zine about debugging for the last 6 months with
my friend [Marie](https://marieflanagan.com/), and one of the problems we ran
into was figuring out how to explain the right *attitude* to take when debugging.


We ended up writing a short debugging manifesto to start the zine with, and I’m
pretty happy with how it came out. Here it is as an image, and as text (with
some extra explanations)


![](https://jvns.ca/images/manifesto.png)


### 1. Inspect, don’t squash


When you run into a bug, the natural instinct is to try to *fix it* as fast as
possible. And of course, sometimes that’s what you have to do – if the bug is
causing a huge production incident, you have to mitigate it quickly before
diving into figuring out the root cause.


But in my day to day debugging, I find that it’s generally more effective (and
faster!) to **leave the bug in place**, figure out exactly what’s gone wrong,
and then fix it after I’ve understood what happened.


Trying to fix it or add workarounds without fully understanding what happened
usually ends up just leaving me *more* confused.


### 2. Being stuck is temporary


Sometimes I get really demoralized when debugging and it feels like I’ll NEVER
make progress.


I have to remind myself that I’ve fixed a lot of bugs before, and I’ll probably
fix this one too :)


### 3. Trust nobody and nothing


Sometimes bugs come from surprising sources! For example, in [I think I found a Mac kernel bug?](https://jvns.ca/blog/2018/01/28/mac-freeze/) I describe how,
the first time I tried to write a program for Mac OS, I had a bug in my program
that was caused by a Mac OS kernel bug.


This was really surprising (usually the operating system is not at fault!!),
but sometimes even normally-trustworthy sources are wrong. Even it’s a popular
library, your operating system, the official documentation, or an extremely
smart and competent coworker!


### 4. It’s probably your code


That said, **almost all of the time** the problem is not “there’s a bug in Mac
OS”. I can only speak for myself, but 95% of the time something is going wrong
with my program, it’s because I did something silly.


So it’s important to look for the problem in your own code first before trying
to blame some external source.


### 5. Don’t go it alone


I’ve learned SO much by asking coworkers or friends for help with debugging. I
think it’s one of the most fun ways to collaborate because you have a specific
goal, and there are tons of opportunities to share information like:

- how to use a specific debugging tool (“here’s how to use GDB to inspect the memory here….”)
- how a computer thing works (“hey, can you explain CORS?”)
- similar past bugs (“I’ve seen this break in X way in the past, maybe it’s that?”)


### 6. There’s always a reason


This one kind of speaks for itself: sometimes it *feels* like things are just
randomly breaking for no reason, but that’s never true.


Even if something truly weird is happening (like a hardware problem), that’s
still a reason.


### 7. Build your toolkit


I’ve written a LOT about my love for debugging tools like tcpdump, strace, and
more on this blog.


To fix bugs you need information about what your program is doing, and to get
that information sometimes you need to learn a new tool.


Also, sometimes you need to build your own better tools, like by improving your
test suite, pretty printing, etc.


### 8. It can be an adventure


As you probably know if you’re a regular reader of this blog, I love debugging
and I’ve learned a lot from doing it. You get to learn something new! Sometimes
you get a great war story to tell! What could be more fun?


I really think of debugging as an investment in my future knowledge – if
something is breaking, it’s often because there’s something wrong in my mental
model, and that’s an opportunity to learn and make sure that I know it for next
time.


Of course, not *all* bugs are adventures (that off-by-one error I was debugging
today certainly did not feel like a fun adventure). But I think it’s important
to (as much as you can) reflect on your bugs and see what you can learn from
them.
