---
title: "Test Cancer"
description: "As my career has turned into full-time authorship, I often worry 	about distancing myself from the realities of day-to-day software 	development. I've seen other well-known figures lose contact with 	"
date: 2007-12-06T00:00:00
tags: ["testing", "bad things"]
url: https://martinfowler.com/bliki/TestCancer.html
slug: TestCancer
word_count: 508
---


As my career has turned into full-time authorship, I often worry
	about distancing myself from the realities of day-to-day software
	development. I've seen other well-known figures lose contact with
	reality, and I fear the same fate. My greatest source of resistance
	to this is Thoughtworks, which acts as a regular dose of reality to
	keep my feet on the ground.


Thoughtworks also acts as a source of ideas from the field, and I
enjoy writing about useful things that my colleagues have discovered
and developed. Usually these are helpful ideas, that I hope that some
of my readers will be able to use. My topic today isn't such a
pleasant topic. It's a problem and one that we don't have an answer
for.


The scenario runs like this. We carry out a project for a client
and hand over a shiny new piece of software. As is our habit these
days, we also hand over a bevy of automated tests for this software
(typically there are as many lines of code of tests as there are of
functional code). These tests are usually a mix of unit tests and
broader ranging functional and acceptance tests. Either way the tests
act as an active description of what the software does and a bug
detector to quickly find problems as we evolve the software. We
treasure these tests, they are a key to our success in building
software systems.


Some months later the happy customer calls us back to do some
	further work on the software, adding new features and
	capabilities. We come in, keen to work on a code base that may have
	faults - but at least are *our* faults. Then we make an
	unpleasant discovery.


The tests no longer run.


Sometimes the tests are excluded from the build scripts, and
	haven't been run in months. Sometimes the âtestsâ are run, but a
	good proportion of them are commented out. Either way our precious
	tests are afflicted with a nasty cancer that is time-consuming and
	frustrating to eradicate.


We ask what happened and are told things like âwe made a change
	and some tests broke, so we removed the testsâ. You can look at this
	as *our* failing - we haven't managed to fully teach the client
	teams about the value of the tests. We need to do more to pass on
	that failing tests need to be investigated, not simply ignored. But
	whatever anyone says, we've discovered that cancer of the tests is a
	 common disease.


We don't think that the fact that Test Cancer appears is a reason
  against writing tests. Even if a particularly virulant strain wipes
  them all out the day after we leave, we still got value from them
  while we were building the system. And  tests don't always get
  cancer. We recently spoke to a developer who had become a convert to
  TDD after maintaining a system we'd handed over a few years ago. The
  tests made our code much easier to work with than code that other
  firms had added later.
