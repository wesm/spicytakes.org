---
title: "Taking a sabbatical to work on Ruby profiling tools"
date: 2017-12-02
url: https://jvns.ca/blog/2017/12/02/taking-a-sabbatical-to-work-on-ruby-profiling-tools/
slug: taking-a-sabbatical-to-work-on-ruby-profiling-tools
word_count: 769
---


Hello! I have an exciting announcement! I’ve announced this before on Twitter, but not here.


From January 1 to April 1, I’ll be on sabbatical from my job and delightful team (thanks Stripe! ❤)
and working on building better profiling tools for Ruby (and maybe Python??). I’ll be doing the Segment Open Source Fellowship (thanks Segment!)– you can read a nice description of [the fellowship and of all of the fellows’ projects](https://segment.com/blog/segment-open-fellows-2017/).


The plan is to expand the prototype in [this blog post](https://jvns.ca/blog/2016/06/12/a-weird-system-call-process-vm-readv/) and [this github repo](https://github.com/jvns/ruby-stacktrace) into a real project that actually works.


### why does Ruby need better profiling tools?


GREAT QUESTION!!!


I’ve been frustrated for a long time by Ruby and Python’s available profiling tools. In C and Java,
I can just attach to any program (`strace -p $PID`, `sudo perf record -g -p $PID`, attach with
YourKit/VisualVM) and immediately start getting information about what the program is doing.


With Ruby, I need to do a bunch of steps before I start getting profiling information:

- choose a profiling library
- include the gem/module in my program
- write code (!?!) to specify which parts of the code I want to profile


This makes me grumpy. So my plan is to work on something that’s easier to use!  This is the
interface for the tools I’m excited about building:

1. Find your process’s PID
2. `run_profiler -p $PID`
3. Look at useful graphs
4. Use the information to make your program faster!!


The main exciting thing this means is – you don’t have to turn on profiling in advance! You don’t
need to use any special gems! It Just Works!


That is the dream. Probably the thing I actually build will not quite reach that dream, like it will
only work on Linux to start and require your Ruby runtime to have debugging symbols.


### why I’m excited about this


I think profiling tools are important, and I think **usability** of profiling tools is really
important. I’ve often had a performance problem, thought “oh, let me just get a memory profile of
this node.js program, that will help”, and 3 hours of frustration later been unable to get the
information I wanted and given up.


Profiling tools are not useful if they are so confusing to use that people give up!


So if we make profiling tools easier to use, people who get frustrated with their slow programs can
**fix** those programs a lot more easily! There’s so much low-hanging fruit in performance – maybe
you [accidentally wrote a quadratic function](https://accidentallyquadratic.tumblr.com/), maybe you
wrote a small hacky thing and someone just needs to spend 30 minutes optimizing it, maybe you
[accidentally used java.lang.Math.pow](https://jvns.ca/blog/2015/09/10/a-millisecond-isnt-fast-and-how-we-fixed-it/).
Without a profiler, it’s basically impossible to diagnose these performance problems!


### debugging / programming capabilities everyone should have access to


There are 3 main things I would like to be easy to get from any program:

- the current stack trace of the program (from every thread, say)
- a memory profile of the program (how many of every object is being used?)
- a sampled CPU profile / flamegraph of the program (what functions are being called the most?)


I’m only planning to work on CPU profiling (and probably “get the current stack trace”, because
that’s such a simple thing).


### also a little nervous!


I have **used** a lot of profilers/debuggers (and written who knows how many blog posts about
debugging tools), but I’ve never tried to **make** a profiler before. I’ve never
tried to make an open source project that other people actually use! (strictly speaking, [https://github.com/jvns/pandas-cookbook](https://github.com/jvns/pandas-cookbook) has thousands of github forks/stars/users, but it’s a tutorial which is a little different)


I expect to run into all kinds of problems! Maybe the approach I take won’t work out! We’ll see what
happens.


Anyway, how am I going to learn & get better if I don’t do things that are a bit scary?  I’m excited to work on this problem!


### open source sabbaticals are cool!


I think taking a 3-month sabbatical from work to work on an open source thing full time is a really
cool thing – I get to go back to my awesome job after, and I get to work on something I’m excited
about! I am happy that I work at a place that has a sabbatical program.


### get in touch if you have ideas


If you have ideas / are interested in this field too, send me an email! I’m [julia@jvns.ca](mailto:julia@jvns.ca).
Throughout this project I would be totally delighted to get contributions, and I’ll post about the
progress I make along the way.
