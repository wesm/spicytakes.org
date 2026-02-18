---
title: "Killing ants with nuclear weapons"
date: 2017-09-08
url: https://drewdevault.com/2017/09/08/Complicated.html
slug: Complicated
word_count: 571
---

Complexity is quickly becoming an epidemic. In this developer’s opinion,
complexity is the ultimate enemy - the final boss - of good software design.
Complicated software generally has complicated bugs. Simple software generally
has simple bugs. It’s as easy as that.

It’s for this reason that I strongly dislike many of the tools and architectures
that have been proliferating over the past few years, particularly in web
development. When I look at a tool like Gulp, I wonder if its success is largely
attributable to people not bothering to learn how Makefiles work. Tools like
Docker make me wonder if they’re an excuse to avoid learning how to do ops or
how to use your distribution’s package manager. Chef makes me wonder if its
users forgot that shell scripts can use SSH, too.

These tools offer a value add. But how does it compare to the cost of the
additional complexity? In my opinion, in  *every case* 1  the value add is far
outweighed by the massive complexity cost. This complexity cost shows itself
when the system breaks (and it will - all systems break) and you have to dive
into these overengineered tools. Don’t forget that dependencies are fallible,
and never add a dependency you wouldn’t feel comfortable debugging. The time
spent learning these complicated systems to fix the inevitable bugs is surely
much less than the time spent learning the venerable tools that fill the same
niche (or, in many cases, accepting that you don’t even need this particular
shiny thing).

Reinventing the wheel is a favorite pastime of mine. There are many such wheels
that I have reinvented or am currently reinventing. The problem isn’t in
reinventing the wheel - it’s in doing so before you actually understand the
wheel 2 . I wonder if many of these complicated tools are written by people who
set out before they fully understood what they were replacing, and I’m  *certain* 
that they’re mostly used by such people. I understand it may seem intimidating
to learn venerable tools like make(1) or chroot(1), but they’re just a short man
page away 3 .

It’s not just tools, though. I couldn’t explain the features of C++ in fewer than
several thousand words (same goes for Rust). GNU continues to add proprietary
extensions and unnecessary features to everything they work on. Every update
shipped to your phone is making it slower to ensure you’ll buy the new one.
Desktop applications are shipping entire web browsers into your disk and your
RAM; server applications ship entire operating systems in glorified chroots; and
hundreds of megabytes of JavaScript, ads, and spyware are shoved down the pipe
on every web page you visit.

This is an epidemic. It’s time we cut this shit out. Please, design your systems
with simplicity in mind. Moore’s law is running out 4 , the free lunch is
coming to an end. We have heaps and heaps of complicated, fragile abstractions
to dismantle.

1. That I’ve seen (or heard of) ↩︎
2. “Those who don’t understand UNIX are doomed to reinvent it, poorly.” ↩︎
3. Of course, [*"…full documentation for make is maintained as a GNU info page…"*](https://xkcd.com/912/) ↩︎
4. Transistors are approaching a scale where quantum problems come into play, and we are limited by the speed of light without getting any smaller. The RAM bottleneck is another serious issue, for which innovation has been stagnant for some time now. ↩︎
