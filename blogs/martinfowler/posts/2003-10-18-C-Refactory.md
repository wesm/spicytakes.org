---
title: "C- Refactory"
description: "So farrefactoring toolshave appeared for a number of languages. After Smalltalk's lead, we've seen several tools for Java and a couple for C#. One language conspicuous by its absence is C++, despiteap"
date: 2003-10-18T00:00:00
tags: ["refactoring"]
url: https://martinfowler.com/bliki/C-Refactory.html
slug: C-Refactory
word_count: 325
---


So far [refactoring tools](http://www.refactoring.com/tools.html)
have appeared for a number of languages. After Smalltalk's lead, we've
seen several tools for Java and a couple for C#. One language
conspicuous by its absence is C++, despite [appeals](http://www.artima.com/weblogs/viewpost.jsp?thread=11070).

All this despite the fact that the first refactoring thesis was done
by [Bill Opdyke](http://csc.noctrl.edu/f/opdyke), who's
background is in C++.


There are several reasons for this, including the sheer
complexity of the C++ language. Such difficulties don't stop the
determined for long, however, and [Ralph Johnson](http://st-www.cs.uiuc.edu/users/johnson/) has
been determined to continue the good tradition of refactoring work at
UIUC. Since C++ is so tricky, there's a lot to be said with starting
with C. C avoids some of the complexity of C++, and there's no
shortage of refactorable C programs out there. In addition C shares
several of C++'s serious challenges, such as the pre-processor.


I caught up with Ralph at [JAOO](http://www.jaoo.dk/)
recently and he filled me in on the research of Alejandra Garrido who
has taken up the challenge of the [C
Refactory](http://jerry.cs.uiuc.edu/~garrido/CRefactory.html). His description was dominated by the difficulties of
dealing with the C pre-processor, particular conditional compilation
and macros. The essential problem is that accurate refactoring
operates on the abstract syntax tree (AST) of the program, but macros
distance the program text from the AST. As a result a C refactoring
tool needs to build a macro-aware AST which holds within it the
variants of the AST that would be compiled. It's hairy work but
Alejandra has had some success, including reading in source to the
Linux kernel as part of the testing for the research tool.


It's still too early to have programmers all over the world using
tools to refactor their C, but  those of you that are interested might
enjoy a dip into the [C Refactory
website.](http://jerry.cs.uiuc.edu/~garrido/CRefactory.html) It contains a bunch of papers by Alejandra and Ralph, and
describes how to get on a mailing list to find out more about this
this work.
