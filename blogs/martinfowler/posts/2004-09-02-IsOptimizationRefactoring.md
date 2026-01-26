---
title: "Is Optimization Refactoring"
description: "If you make a change to improve the performance of a 	program, is this a refactoring?"
date: 2004-09-02T00:00:00
tags: ["refactoring boundary"]
url: https://martinfowler.com/bliki/IsOptimizationRefactoring.html
slug: IsOptimizationRefactoring
word_count: 215
---


**If you make a change to improve the performance of a
	program, is this a refactoring?**


I see optimization and refactoring as two separate things, even
	though they often use the same transformations, and a particular
	transformation you do to your program may be both.


The reason I see them as different is because they have a
	different purpose. You do refactoring to make the code easier to
	understand, you do optimization to make it go faster. Introducing a
	variable (for example) could be done for either purpose, but
	depending on how you do it you are primarily doing one or the
	other. When you are refactoring you are thinking about making the
	code clearer. Your judgement on whether it's successful is based on
	your (subjective) assessment of whether the change makes the program
	easier to understand. When you are optimizing you are thinking about
	performance. You should be using a profiler, before and after the
	change to ensure that your optimization really did help
	performance. If the situation is performance critical you should
	keep a log of your change so you can retest its effectiveness when
	your environment (compiler, VM etc) changes later on.


So although the two are similar, and share many transformations,
	I see them as different because their purpose is different.
