---
title: "Etymology Of Refactoring"
description: "Where did the wordrefactoringcome   from?"
date: 2003-09-10T00:00:00
tags: ["refactoring"]
url: https://martinfowler.com/bliki/EtymologyOfRefactoring.html
slug: EtymologyOfRefactoring
word_count: 331
---


**Where did the word *refactoring* come
  from?**


This question struck my mind a few times when writing the
refactoring book. I knew the term was used within a fairly small
community, so in order to discover the etymology of refactoring I
talked to the people in that group (Ward Cunningham, Kent Beck, Bill
Opdyke, John Brant, Don Roberts, Ralph Johnson...) to find what had
led them to come up with the term.


The obvious answer comes from the notion of factoring in
  mathematics. You can take an expressions such as `x^2 + 5x +
  6` and factor it into `(x+2)(x+3)`. By factoring it
  you can make a number of mathematical operations much
  easier. Obviously this is much the same as representing 18 as
  2*3^2. I've certainly often heard of people talking about a program
  as well factored once it's broken out into similarly logical
  chunks.


When I asked around the creators of refactoring, the common
  answer was that they had no idea. The term had been around for a
  while and they don't know where it came from.


The one definite answer I got was from [Bill Opdyke](http://csc.noctrl.edu/f/opdyke/), who did the
  [first thesis](ftp://st.cs.uiuc.edu/pub/papers/refactoring/opdyke-thesis.ps.Z) on refactoring. He remembered a conversation during a
  walk with Ralph Johnson. They were discussing the notion of Software
  Factory, which was then in vogue. They surmised that since software
  development was more [like design than like manufacturing](http://patricklogan.blogspot.com/2003_08_31_patricklogan_archive.html), it would
  be better to call it a Software *Re*factory. Refactory has gone
  on to be the name for the [consulting organization](http://www.refactory.com/) that Ralph and his
  colleagues use.


The foundations of what we refer to these days as refactoring
  comes from the Smalltalk communities. However the metaphor of
  factoring a program was also part of the Forth community. [Bill Wake dug out](http://laputan.org/catfish/2011/03/post.html)
  the first known printed mention of the word ârefactoringâ in a
  Thinking Forth, a 1984 book by Leo Brodie. We're pretty sure that
  this usage didn't pass from the Forth community to the Smalltalk
  community, but developed independently.
