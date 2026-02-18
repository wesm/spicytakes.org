---
title: "Portability matters"
date: 2017-11-13
url: https://drewdevault.com/2017/11/13/Portability-matters.html
slug: Portability-matters
word_count: 547
---

There are many kinds of “portability” in software. Portability refers to the
relative ease of “porting” a piece of software to another system. That
platform might be another operating system, another CPU architecture, another
web browser, another filesystem… and so on. More portable software uses the
limited subset of interfaces that are common between systems, and less portable
software leverages interfaces specific to a particular system.

Some people think that portability isn’t very important, or don’t understand the
degree to which it’s important. Some people might call their software portable
if it works on Windows and macOS - they’re wrong. They might call their software
portable if it works on Windows, macOS, and Linux - but they’re wrong, too.
Supporting multiple systems does not necessarily make your software portable.
What makes your software portable is  *standards* .

The most important standard for software portability is POSIX, or the  **Portable
Operating System Interface** . Significant subsets of this standard are supported
by many, many operating systems, including:

* Linux
* *BSD
* macOS
* Minix
* Solaris
* BeOS
* Haiku
* AIX

I  [could go
on](https://en.wikipedia.org/wiki/POSIX#POSIX-oriented_operating_systems) .
Through these operating systems, you’re able to run POSIX compatible code on a
large number of CPU architectures as well, such as:

* i386
* amd64
* ARM
* MIPS
* PowerPC
* sparc
* ia64
* VAX

Again, I could go on. Here’s the point: by supporting POSIX, your software runs
on basically every system.  *That’s*  what it means to be portable - standards.
So why is it important to support POSIX?

First of all, if you use POSIX then your software runs on just about anything,
so lots of users will be available to you and it will work in a variety of
situations. You get lots of platforms for free (or at least cheap). But more
importantly,  *new platforms*  get your software for free, too.

The current market leaders are not the end-all-be-all of operating system
design - far from it. What they have in their advantage is working well enough
and being incubent. Windows, Linux, and macOS are still popular for the same
reason that legislator you don’t like keeps getting elected! However, new
operating systems have a fighting chance thanks to POSIX. All you have to do to
make your OS viable is implement POSIX and you will immediately open up
hundreds, if not thousands, of potential applications. Portability is important
for innovation.

The same applies to other kinds of portability. Limiting yourself to standard
browser features gives new browsers a chance. Implementing standard networking
protocols allows you to interop with other platforms. I’d argue that failing to
do this is  *unethical*  - it’s just another form of vendor lock-in. This is why
Windows does not support POSIX.

This is also why I question niche programming languages like Rust when they
claim to be suited to systems programming or even kernel development. That’s
simply not true when they only run on a small handful of operating systems and
CPU architectures. C runs on  *literally*  everything.

In conclusion: use standard interfaces for your software. That guy who wants to
bring new life to that old VAX will thank you. The authors of
 [servo](https://servo.org/)  thank you.  *You*  will thank you when your
circumstances change in 5 years.
