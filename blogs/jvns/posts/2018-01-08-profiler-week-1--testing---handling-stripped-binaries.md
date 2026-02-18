---
title: "Profiler week 1: testing & profiling stripped binaries"
date: 2018-01-08
url: https://jvns.ca/blog/2018/01/08/profiler-week-1--testing---handling-stripped-binaries/
slug: profiler-week-1--testing---handling-stripped-binaries
word_count: 852
---


Hello! of working on my Ruby profiler, and so here’s the first weekly update! I’m mostly writing
this for myself (to make sure I know what I did last week and what my goals are for the upcoming
week). But maybe you will find it interesting too!


Last week I had 2 goals:

- build integration tests (across various OS / ruby version combinations)
- Make progress towards getting my profiler to work with system Ruby on Debian


### integration testing the profiler


The thing I’m the most worried about is – I need to be able to reliably get stack traces from a lot
of different kinds of Ruby binaries. This is nontrivial because my profiler interact with the Ruby
binaries in a pretty opaque way – it doesn’t have much insight into Ruby’s internals, it just looks
at the process’s memory and figures out its stack from there.


To make sure it works on Ruby 3.5.2 without debug symbols installed on Ubuntu 14.04, it’s useful to
have integration tests!


There are at least 3 axes I need to test:

- which Ruby version is running?
- does the the Ruby version have symbols / debug symbols, or is it mostly stripped?
- which OS is it running on?


So I started making a few Dockerfiles last week.  ([here’s one of them](https://github.com/jvns/ruby-stacktrace/blob/9b1b583d7a53572248c1c35f39ad406ac5086470/docker/Dockerfile.ubuntu1604))


Right now I’m only testing on Linux (Ubuntu 14.04, 16.04, and Fedora 27). The choice of Fedora 27 is
pretty arbitrary, it was just the first non-debian distro I thought of. Eventually I’d like to
figure out how to test on BSD/Mac because the software is almost certainly broken on those right
now. Maybe I can use Travis to do that?


[This is my script to run the tests right now](https://github.com/jvns/ruby-stacktrace/blob/9b1b583d7a53572248c1c35f39ad406ac5086470/build.sh). It basically just runs the profiler on one Ruby program and makes sure it succeeds. Right now all the rbenv-installed Ruby tests pass and all the system Ruby tests fail.


I’ll add more Ruby versions later (there are many more versions than 2.3.5! =) ) but that should be
easy.


### is it enough to test just rbenv and debian’s Ruby package?


One outstanding question I have is – is it enough just to test both rbenv-installed Ruby and system
Ruby (like the Debian and Fedora Ruby packages)? I suppose I’ll find out! I can always add more
integration tests laster.


### getting system Ruby to work (partial success!)


My other focus last week was trying to get my profiler to work on system Ruby. Specifically – the
Ruby installed in the `ruby2.3` package on Ubuntu 16.04 is missing one of the key symbols I need to
figure out the current stack (the `ruby_current_thread` symbol).


I could deal with this by just asking people to install the `libruby2.3-dbg` package (which contains
debug symbols). But it seemed more fun to just try to get it to work without debug symbols.


And I did!!! I managed to find the address of the `ruby_current_thread` symbol through some educated
guessing!! And once I’d found that address, the profiler actually worked! It got stack traces out of
the process!


This is a “partial success” instead of a “total success” because it worked great on my laptop, but
then when I tried it in the Docker container it didn’t work. Don’t know why yet but that’s next!


### policy for accepting contributions (maybe I’ll use C4)


I was at StarCon this weekend (which I’ll write about later). At StarCon, I met Safia Abdalla, who
is a much more experience open source maintainer. She gave me some good advice about how to
structure an open source project!


In particular: she told me that for
her main project ([nteract](https://github.com/nteract/nteract)) they use the “Collective Code
Construction Contract” (“C4”) development model from ZeroMQ (see [the spec](https://rfc.zeromq.org/spec:42/C4/) and [pieter hintjens’ book chapter describing the philosophy](https://hintjens.gitbooks.io/social-architecture/content/chapter4.html)). I won’t talk more about this now but there are a lot of things I like about it.


### code from last week


I merged 3 PRs last week:

- [Reimplement using bindgen-generated Ruby bindings instead of DWARF](https://github.com/jvns/ruby-stacktrace/pull/25) – a huge refactor of all of the core functionality that I’m pretty hopeful about. In particular it makes it possible for the profiler to work even if DWARF debugging symbols aren’t available.
- [make it possible to profile a subprocess](https://github.com/jvns/ruby-stacktrace/pull/26) –
lets you do `./profile ruby my-process.rb`, which will spawn a subprocess and then profile it.
- [set up integration tests](https://github.com/jvns/ruby-stacktrace/pull/27)


and worked on 1 branch. [Here’s the current commit](https://github.com/jvns/ruby-stacktrace/commit/7b5c42b35bbe855639f100bf7f7fd104c8ff5618).
It’s a mess but the meat is in `get_thread_address_alt` and `is_maybe_thread` (which check if a
given address looks like it **could** be the current thread address).


### goals this week

- Add support for Ruby 1.8/1.9/2.5
- Get my branch supporting system Ruby working more reliably
- Write more integration tests and publish Docker images to a Docker registry for them (so that
other people can easily run the integration tests if they want)
- Give the project an official name and create a github organization for it


If I could do all that by the end of the week I would be very happy!
