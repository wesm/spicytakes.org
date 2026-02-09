---
title: "Theory of Relative Dependency and TDD"
date: 2010-08-15
url: https://blog.mempko.com/theory-of-relative-dependency-and-tdd/
slug: theory-of-relative-dependency-and-tdd
word_count: 747
tags: ['#wordpress', '#Import 2024-11-03 23:36']
---



Refactoring is great right? I mean, it is something we do all the time. If you do TDD, you do it all the time, its part of the process. But is it such a good thing? What do we tend to do when we refactor and why in the world does code have “smells”?


I always felt that the idea refactoring is good was a sham. Our second bedroom for the longest time was my wife’s craft room. There was a big desk, and several other pieces of furniture. We installed shelves in various places, and generally the room had a certain amount of clutter to it. If I continued my dream of learning wood working, I might have wired the room for some wood working equipment.


Then my wife got pregnant, so we “refactored” the room. We had always expected to have a child, but never knew when that would happen. It became a real pain to change the room into a baby room. Clutter had to be removed, walls pained, furniture given away. Had we given the room more thought about its purpose and layout, the work to change it to a baby room would have been significantly less.


In other words, refactoring is the result of poor planning and poor design. How can poor planning be a good thing? I suppose in the modern world of “Agile” development using XP practices, down is up, and up is down.


After reading a paper by Koru and Emam about the “Theory of Relative Dependency” (IEEE Issue 99), got me thinking about refactoring and TDD in particular.


The paper was a study on many open source projects showing that for large scale systems, higher coupling was concentrated on smaller modules, and that smaller modules had a proportionally higher concentration of defects than larger ones. They also showed that refactoring exacerbates this coupling.


The TDD culture celebrates refactoring. The Test-Code-Refactor cycle is supposed to be lighting short. Empirical studies such as those by Janzen and Saledian do show that TDD does result is smaller modules with higher parameter “fan in”. Do you see where I am going? If you do, keep reading!


Koru and Eman recommended that agile software shops concentrate their QA and testing on these smaller components instead of the large ones because, duh, they have higher defect rates.


What is interesting with TDD is you get into this catch-22. You produce smaller modules and constantly refactor. These smaller modules will typically have higher coupling and defect rates according to Koru and Eman. Therefore you should focus your testing on these smaller modules!


You NEED the tests to sustain such rapid refactoring that TDD embraces. If you took some software designed by TDD and removed the tests, you would be left with many small modules that are highly dependent. This  is a difficult design to reason about and change. The software design of these systems will eventually collapse under their own weight.


The unit tests themselves are highly coupled pieces of code! And with a typical one-to-one ratio between unit tests and code, this means half your code is tightly coupled code! Despite what others tell you, unit tests ARE code and they need to be maintained.


This frightens me. This means that any real meaningful refactoring , the cross functional, cross object kind would be almost impossible in a large project employing this approach.


I am trying to keep TDD out of my workplace for this reason. I feel that TDD is used by people as a crutch, as a replacement for thinking. Its friendly to that because you know what you are doing at any moment. “I am writing test now, ok it failed, not I write code, ok it passed, now I refactor, ok now I write more tests”.


Not thinking is built into the process.


For people who need this kind of structure, by all means do TDD. But for those adventurous enough to swim in the mental ether, to think, to feel, to care, avoid it.


A lot of this is speculative on my part and a lot of it is from my own experience with TDD. There are not many studies on TDD and many of those like Janzen and Saledian “Does Test-Driven Development Really Improve Software Design?” have mixed results. James Coplien wrote a great article called [“Religion’s Newfound Restraint on Progress” ](http://www.artima.com/weblogs/viewpost.jsp?thread=216434&ref=blog.mempko.com)that talks more about TDD and the dogmatic approach people take with it. I highly recommend it.

