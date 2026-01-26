---
title: "Erratic Test Failure"
description: "I was working on some of my book example code the other day. I 	made some changes, got everything working, ran tests, and committed 	it to my personal repository. I then moved over to a different area"
date: 2005-03-28T00:00:00
tags: ["testing", "bad things"]
url: https://martinfowler.com/bliki/ErraticTestFailure.html
slug: ErraticTestFailure
word_count: 570
---


I was working on some of my book example code the other day. I
	made some changes, got everything working, ran tests, and committed
	it to my personal repository. I then moved over to a different area
	and made a couple of changes - and some unexpected tests broke in
	the previous area. Now part of the point of running automated tests
	is to find unexpected breaks, but this book code has completely
	independent areas. This was odd.


Rather than try to debug the problem I used
	[DiffDebugging](https://martinfowler.com/bliki/DiffDebugging.html). I'd not done much since the commit so I
	did `svn revert`. I reran the tests - failed. But I was
	certain I ran the tests before I committed. I decided to run the
	tests via ant instead of in IntelliJ. The ant tests all
	passed. They're the same tests, running all JUnit classes in the
	directory. So why were they passing in ant and failing in IntelliJ?


At this point I'm ashamed to admit what I thought next. âMust be
	something wrong with IntelliJ - maybe it's got some form of cache
	and is confused by subversion's revertâ. Early on in my programming
	youth an older programmer taught me the first rule of debugging -
	the bug's always in your code, not the compiler. But under in the
	influence of my stupidity I restarted IntelliJ  - an lo the tests
	all passed again. Problem solved - NOT! Fortunately the second time this odd behavior happened to me I
	was pairing with [Sergey](http://www.sergeydmitriev.com/), and he approached
	the problem without my stupidity and found the bug.


To help you find the answer to these kinds of problems go out
	into the open air and build a word with letters six and half feet
	high. Build it out of cedar so you won't have to paint it - but
	don't forget to decorate it with cherries. The word is:


isolation.


If tests sometimes pass and sometimes fail on a run without any
	code changes, or tests pass when run in some suites but fail when
	run in others; nine times out of eight the reason is that there is
	some shared data between tests that isn't being properly
	reinitialized. When that happens just running a test can be the
	difference between other tests passing and failing. The result is an
	intermittent failure - always the worst because you can't reliably
	reproduce it.


I was using JUnit - which is strong on isolation (which is why it
	uses the [JunitNewInstance](https://martinfowler.com/bliki/JunitNewInstance.html) behavior). So my problem must
	have come from some static data. In this case it was calls to get
	the current day. I'd used a [ClockWrapper](https://martinfowler.com/bliki/ClockWrapper.html), but failed to initialize
	it in some of my tests. So depending on which was the last test that
	initialized it, some tests would fail.


There are two lessons here. Firstly do everything you can to keep
	your test data isolated. Try to create fresh data
	every time (although there is a trade-off here with getting fast
	test runs). The more you practice good test isolation, the less
	chance you have of running into this kind of problem.


Secondly if you do get this kind of intermittent test failures,
	suspect any data that gets shared between tests. Check that the the
	intermittently failing tests fully initialize the data in test
	runs. With anything that isn't initialized, make sure you know where
	it got created and if it's ever changed.
