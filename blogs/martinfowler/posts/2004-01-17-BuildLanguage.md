---
title: "Build Language"
description: "Bruce Eckel'srecent poston ant and make triggered me to share some of my thoughts about build languages. Both ant and make specify how builds happen, they are a language for describing builds. Both ar"
date: 2004-01-17T00:00:00
tags: ["build scripting"]
url: https://martinfowler.com/bliki/BuildLanguage.html
slug: BuildLanguage
word_count: 323
---


Bruce Eckel's [recent post](http://mindview.net/WebLog/log-0046) on ant and
make triggered me to share some of my thoughts about build languages.
Both ant and make specify how builds happen, they are a language for
describing builds. Both are pretty widely used and have been
successful. Yet both run into limitations, with larger systems it's
quite common to find people generating their ant/make files from other
programs.


I think I'm agreeing with Bruce for the reason. Simple builds are
easy to express as a series of tasks and dependencies. For such builds
the facilities of ant/make work well. But more complex builds require
conditional logic, and that requires more general programming language
constructs - and that's where ant/make fall down.


Ant made the decision to use XML as its file format. At the time
I thought it was a good choice. In those early days I was working with
Matt Foemmel on a large project and he built a similar system to ant
(ant didn't exist at the time and we needed it). He also picked XML as
the language. It made sense to us because XML is a tolerable way of
describing hierarchical data, and a hierarchy seemed to fit a build
scripts demands. We've both concluded since that a programming
language is more the way to go and that's not a good
[UseOfXml](https://martinfowler.com/bliki/UseOfXml.html).


Since I do a fair bit of programming in Ruby, I've naturally
started to play with [Rake](http://rake.rubyforge.org/), a
ruby make. The interesting thing about the rakefiles is that they are
regular ruby programs with a few conventions and support to allow you
to declare tasks and dependencies. I only have small tasks to work
with it, and so far I find it very comfortable. Since it is a full
blown programming language I would expect it to work well for larger
builds, I already have found it handy to do things like loops,
subroutines and list collection in my build files.
