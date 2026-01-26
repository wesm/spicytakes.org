---
title: "Test Driven Development"
description: "Test-Driven Development (TDD) is a technique for building   software that guides software development by writing tests. It was   developed byKent   Beckin the late 1990's as part of   Extreme Programm"
date: 2023-12-11T00:00:00
tags: ["testing", "programming style"]
url: https://martinfowler.com/bliki/TestDrivenDevelopment.html
slug: TestDrivenDevelopment
word_count: 393
---


Test-Driven Development (TDD) is a technique for building
  software that guides software development by writing tests. It was
  developed by [Kent
  Beck](https://substack.com/@kentbeck) in the late 1990's as part of
  Extreme Programming. In essence we follow three simple
  steps repeatedly:

- Write a test for the next bit of functionality you want to add.
- Write the functional code until the test passes.
- Refactor both new and old code to make it well structured.


![](images/test-driven-development/card.png)


Although these three steps, often summarized as *Red - Green -
  Refactor*, are the heart of the process, there's also a vital initial
  step where we write out a list of test cases first. We then pick one of these
  tests, apply red-green-refactor to it, and once we're done pick the next.
  Sequencing the tests properly is a skill, we want to pick tests that drive us
  quickly to the salient points in the design. During the process we should add
  more tests to our lists as they occur to us.


Writing the test first, what [XPE2](https://www.amazon.com/gp/product/0321278658/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=0321278658&linkCode=as2&tag=martinfowlerc-20) calls
  Test-First Programming, provides two main benefits. Most obviously it's a way
  to get [SelfTestingCode](https://martinfowler.com/bliki/SelfTestingCode.html), since we can only write some functional
  code in response to making a test pass. The second benefit is that thinking
  about the test first forces us to think about the interface to the code first.
  This focus on interface and how you use a class helps us separate interface
  from implementation, a key element of good design that many programmers
  struggle with.


The most common way that I hear to screw up TDD is neglecting
  the third step. Refactoring the code to keep it clean is a key part
  of the process, otherwise we just end up with a messy aggregation of
  code fragments. (At least these will have tests, so it's a less
  painful result than most failures of design.)


## Further Reading


Kent's summary of the [canonical way to do TDD](https://tidyfirst.substack.com/p/canon-tdd)
    is the key online summary.


For more depth, head to Kent Beck's book
    [Test-Driven Development](https://www.amazon.com/gp/product/0321146530/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=0321146530&linkCode=as2&tag=martinfowlerc-20).


The relevant chapter of James Shore's [The
    Art of Agile Development](https://www.amazon.com/gp/product/1492080691/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=1492080691&linkCode=as2&tag=martinfowlerc-20) is another sound description that also
    connects it to the rest of effective agile development. James also wrote a
    series of screencasts called [Let's Play TDD](http://www.jamesshore.com/Blog/Lets-Play).


## Revisions


My original post of this page was 2005-03-05. Inspired by Kent's
    canonical post, I updated it on 2023-12-11
