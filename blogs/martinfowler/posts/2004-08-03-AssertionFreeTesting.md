---
title: "Assertion Free Testing"
description: "Here's a story from a friend of a friend. I'm sure it must be 	true, at least somewhere."
date: 2004-08-03T00:00:00
tags: ["testing", "bad things"]
url: https://martinfowler.com/bliki/AssertionFreeTesting.html
slug: AssertionFreeTesting
word_count: 215
---


Here's a story from a friend of a friend. I'm sure it must be
	true, at least somewhere.


A project got started to do a big system. It was outsourced to a
	big software/consultancy house - one I know you've heard of. They
	put in an impressive team for the bid, and naturally swapped them
	all out for a lot of junior people for the actual work. All standard
	procedure.


The twist is that the company made a big point of using heavy
	testing with JUnit. Every public method had to have JUnit
	tests. They proudly showed the client all the tests and the green bar.


However there weren't any assertions in the JUnit tests.


I don't know if they did code coverage analysis on this project,
	but of course you can do this and have 100% code coverage - which is
	one reason why you have to be careful on interpreting code coverage
  data.1


1: 
      Although assertion-free testing is mostly a joke, it isn't
      entirely useless. As Carlos Villela reminded me, some faults do
      show up through code execution, eg null pointer exceptions.


## Notes


1: 
      Although assertion-free testing is mostly a joke, it isn't
      entirely useless. As Carlos Villela reminded me, some faults do
      show up through code execution, eg null pointer exceptions.
