---
title: "Celebrate tiny learning milestones"
date: 2022-03-13
url: https://jvns.ca/blog/2022/03/13/celebrate-tiny-learning-milestones/
slug: celebrate-tiny-learning-milestones
word_count: 1043
---


Hello! Today I want to talk about – how do you know you’re getting better at programming?


One obvious approach is:

1. make goals
2. periodically check if you achieved those goals
3. if you did, celebrate


### I kind of hate goals


Goals can be useful, but a lot of the time I actually find them stressful and
not that helpful. For example, here are a few goals I wrote down for myself 9
years ago:

- write a nontrivial amount of C code that works and is used by actual people
- contribute to an open source project in C
- learn C++


9 years later, I have done 0 of those things. With the “goal” framing, it’s to
think of this as a bad thing! Like, I wanted to learn C++ and I didn’t! I still
can’t write C comfortably! Oh no! I guess I failed!


I find this framing depressing and unhelpful. In reality, I didn’t have any real
reason to learn C++ then and I still don’t now. So it makes sense that I
haven’t learned it.


Instead of goals, I like to think about **tiny milestones**.


### what’s a milestone?


Usually when we talk about milestones we mean something big that only happens every few years, like “I graduated from university”.


But in this post I want to talk about milestones in the sense of its etymology
– **stones** placed every **mile** on a highway, so that you can track your
progress along a path.


These happen much more often – maybe you used a new tool for the first time,
or you fixed a new type of bug that you’ve never seen before, or you learned
about a new concept!


### a few of my tiny C milestones


Here are a few examples of tiny milestones from the last 9 years that are
spiritually related to my original “learn C/C++” goals.


I’m pretty sure that each of these individually took less than a week, though
all together they took many years and a lot of them would have been impossible
for me at the beginning.

- wrote a tiny Linux kernel module that does almost nothing
- learned about `strace`
- wrote a very basic shell in C with a friend
- learned how ELF binaries are organized (symbols, sections, etc)
- learned how to use `gdb` to inspect a C program’s memory
- learned a little about how how `gdb` actually works internally (using DWARF)
- learned the difference between static and dynamic linking
- learned how to look at how a program is linked with `ldd` or `file`
- (years later) debugged a problem that was caused by dynamic linking
- implemented a buffer overflow exploit using `gdb` and `strace` (for a CTF)
- got a core dump for a crashing C++ program and managed to get a stack trace out of it
- learned about the RAII pattern (though in Rust, not C++)
- learned what a few basic x86 assembly instructions mean (`mov`, etc)
- pair programmed with a friend who already knew x86 assembly on implementing one Advent of Code problem (Day 1) in x86 assembly
- in general I’m comfortable writing very basic C programs as long as they
don’t have to do anything fancy like “memory management”


And there were even some major milestones, like I wrote a [Ruby profiler](https://github.com/rbspy/rbspy) in Rust in 2018.


When I think about it this way, I feel really good about my skills! I’ve
learned all kinds of stuff related to systems programming, it just happened in
a different way than I originally expected.


### fixing a bug can be a milestone


Every time I solve a bug that I couldn’t have solved before, I think of it as a
tiny milestone. For example, I’ve been trying to get better at CSS. One big
part of that for me is diving deeper into CSS bugs I encounter instead of
giving up.


Last year, I was having a problem with a flexbox. It was something that I
vaguely felt had happened to me before but that I’d never been able to fix, and
it made me feel like I didn’t understand how flexbox worked.


But instead of just finding a workaround, I decided to try to understand what was actually happening. And I
ended up finding a blog post that explained what was happening – [Flexbox Containers, PRE tags and managing Overflow](https://weblog.west-wind.com/posts/2016/feb/15/flexbox-containers-pre-tags-and-managing-overflow).
And that was really the cause of my bug!


### changing goals isn’t a bad thing


The reason I still haven’t learned C isn’t that I suck or that C is impossible
to learn. It’s just that learning how to write C well was never actually
something I had a real reason to do.


Instead I learned Rust and Go and `strace` and `gdb` and about C structs and
symbols and the call stack and the heap and lots of other things. (as an aside, I loved this paper [Some were meant for C](https://www.humprog.org/~stephen/research/papers/kell17some-preprint.pdf)
about how why C is still so important)


And that worked great! So I think it’s much more healthy to be flexible about
your goals and to celebrate the milestones you do end up getting to instead of
feeling bad about goals that you “failed” at.


### you can learn a lot by “accident”


Most of my tiny milestones came up naturally because I had a project I wanted
to do or a bug I needed to solve. So I didn’t need to explicitly plan for them,
they just kind of happened along the way because I kept doing projects that
challenged me.


### celebrate your tiny milestones


It’s really helpful for me to **celebrate** tiny milestones like this. I celebrate
a lot by writing blog posts – I wrote the above list mostly by looking at my
list of old blog posts for things I’d written about related to C.


If you don’t blog (it’s definitely not for everyone!), it can be helpful to write down
this kind of thing in your [brag document](https://jvns.ca/blog/brag-documents/) instead.


But I do think it’s important to celebrate these milestones *somewhere*. It
gives me a real sense that I’m making progress and it helps me stay motivated
to keep learning about the thing.
