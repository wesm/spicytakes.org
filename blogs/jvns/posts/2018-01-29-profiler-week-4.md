---
title: "Profiler week 4: callgrind support, containers, Mac progress!"
date: 2018-01-29
url: https://jvns.ca/blog/2018/01/29/profiler-week-4/
slug: profiler-week-4
word_count: 566
---


Today is Monday and week 4 of working on my profiler is over! I’m 1/3 of the way through. Eep! My
main goal for last week was to release Mac support, which hasn’t quite happened yet – it turns out
that Mac systems programming is more complicated than I thought (getting a mac’s memory maps is [really hard!](https://jvns.ca/blog/2018/01/26/mac-memory-maps/) and I got derailed a bit by [a kernel bug](https://jvns.ca/blog/2018/01/28/mac-freeze/)).


### last week (contributions!!)


exciting things that happened last week:

- 2 new people contributed code to rbspy! ([@liaden](https://github.com/liaden) and [@vasi](https://github.com/vasi)!). liaden contributed a `--duration` flag
and a `--rate` flag, so you can change the rate rbspy is sampling at. vasi contributed a new
output format for rbspy (cachegrind format!) which I think will be useful – it lets you see.
[The cachegrind PR has some nice pictures](https://github.com/rbspy/rbspy/pull/75).
- also lots of folks made issues and suggestions and tried it out, which is awesome. All the issues
are so helpful!
- Added support for profiling processes running in containers! It seems to work well!
- Learned A LOT more about Mac systems programming than I used to know. I think I should be able to
merge a Mac support PR in the next day or two.


So far it seems like Rust is easy enough that some non-Rust-programmers can come in and start
contributing PRs to rbspy, which is really nice to see!


### next week


On the schedule for this week:

- finish up Mac support
- fix a bug with getting the stacks when the top function in the stack is a C function that I can
reproduce
- possibly put together a website?
- @liaden is working on support for profiling subprocesses (so you can point rbspy at your Unicorn
process or something, and it’ll profile all of your web workers). I think that’ll be awesome.


### a Rust flamegraph library?


Something that’s been on my mind but I haven’t really figured out is – rbspy is growing a few new
visualization formats (flamegraphs! callgrind format!). I think it could be cool to build a Rust
crate with support for different visualization formats, so that if people build other profilers then
they can kinda have access to a consistent library of visualization formats.


I don’t really know if I have time for that though! For now I’m going to stay focused on lower level
concerns.


### MEMORY PROFILERS!!!


I’m not done with CPU profiling (there are still lots of rough edges to sort out!) but once I get
things slightly more feature complete I think I kinda want to let the CPU profiler rest for a bit and work on
prototyping something else while I give people a chance to try out the project.


Today I had 2 extremely helpful conversations about memory profilers and I feel excited about trying
something out!


My thought is to maybe add a `memprofile` subcommand to rbspy, where you give it a PID and it
does… something? I have 2 ideas for what it could do right now:

- give you a memory profile of your program (a summary of objects / their types / their sizes)
- start tracking **new** allocations and tell you where they’re happening and how much memory is
being allocated right now.


I’m hoping to have time to do some work prototyping a memory profiler this week. We’ll see what
happens in real life!
