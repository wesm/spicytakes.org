---
title: "My Rust OS will never be finished (and it's a success!)"
date: 2014-03-21
url: https://jvns.ca/blog/2014/03/21/my-rust-os-will-never-be-finished/
slug: my-rust-os-will-never-be-finished
word_count: 412
---


In November/December last year, I spent 3 weeks working on a toy
operating system in Rust. (for more, see
[Writing an OS in Rust in tiny steps](http://jvns.ca/blog/2014/03/12/the-rust-os-story/),
and [more](http://jvns.ca/categories/kernel/)).


I wrote a ton of blog posts about it, and I gave a talk about the
process at Mozilla last week
([the video](https://air.mozilla.org/rust-meetup-march-2014/)). At
that talk, a few people asked me if I was going to finish the project.
I said no, and here’s why.


There are lots of reasons for working on programming projects. Just a
few:

- to end up with useful code
- to learn something
- to explore a new concept (see: Bret Victor’s demos)


The reason I wrote an operating system in Rust wasn’t so that I could
have an operating system written in Rust.


I already have an kernel on
my computer (Linux), and other people have already written Rust
operating systems better than I have. Any code that I write in 3 weeks
is at best a duplication of someone else’s work, and mimicking
the state of the art 20 years ago.


I worked on that project to learn about how operating systems work,
and that was a huge success. I read a 20-part essay about linkers, and
learned about virtual memory, how executables are structured, how
program execution works, how system calls work, the x86 boot process,
interrupt handlers, keyboard drivers, and a ton of other things.


Another amazing example of a project like this is
[@kellabyte](http://twitter.com/kellabyte)’s
[Haywire](https://github.com/kellabyte/Haywire), a HTTP server in C
she wrote to learn more about writing performant code. It actually
compiles and you can benchmark it yourself, but her blog posts are
more useful to me than her code –
[Hello haywire](http://kellabyte.com/2013/08/16/hello-haywire/)
[HTTP response caching in Haywire](http://kellabyte.com/2013/08/20/http-response-caching-in-haywire/),
[Further reducing memory allocations and use of string functions in Haywire](http://kellabyte.com/2013/08/22/further-reducing-memory-allocations-and-use-of-string-functions-in-haywire/).


So when people ask me why my code doesn’t compile, it’s because the
code is basically a trivial output of the process. The
[blog posts I wrote](http://jvns.ca/categories/kernel/) are
*much* more important, because they talk about what I learned. My code
probably won’t be useful to you – it would be better to start with
[rustboot](https://github.com/charliesome/rustboot) and take your own
path.


Not finishing your project doesn’t mean it’s not a success. It depends
what your goals are the for the project! I wrote an operating system
in Rust to learn, and I learned a ton. It’s not finished, and it won’t
be. How could it ever be? I hope to not ever finish learning.
