---
title: "Testing Language"
description: "I'm currently sitting in a session atXP daywhere Owen Rogers and Rob Styles are talking about the differences between XP's unit and acceptance tests. This triggered a thought in my mind - what should "
date: 2003-12-02T00:00:00
tags: ["testing"]
url: https://martinfowler.com/bliki/TestingLanguage.html
slug: TestingLanguage
word_count: 137
---


I'm currently sitting in a session at [XP day](http://www.xpday.org/) where Owen Rogers and Rob
Styles are talking about the differences between XP's unit and
acceptance tests. This triggered a thought in my mind - what should a
language for writing acceptance tests be?


Commercial tools for UI testing tend to have their own
proprietary language. [Brett

Pettichord](http://www.stickyminds.com/sitewide.asp?ObjectId=2326&ObjectType=COL&Function=edetail), amongst others, question this; preferring a common
scripting language such as Ruby or Python.


But I wonder if a language designed for programming is really the
right language for writing tests. The point about tests is that they
operate by example. They don't try to cover how to handle any value,
instead they describe specific scenarios and responses. I wonder if
this implies a different kind of programming language is required.
Perhaps this is the truly startling innovation in [FIT](http://fit.c2.com/).
