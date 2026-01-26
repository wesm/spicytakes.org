---
title: "Test Coverage"
description: "From time to time I hear people asking what value of test coverage (also   called code coverage) they should aim for, or stating their coverage   levels with pride. Such statements miss the point. Tes"
date: 2012-04-17T00:00:00
tags: ["testing", "metrics"]
url: https://martinfowler.com/bliki/TestCoverage.html
slug: TestCoverage
word_count: 712
---


From time to time I hear people asking what value of test coverage (also
  called code coverage) they should aim for, or stating their coverage
  levels with pride. Such statements miss the point. Test coverage is
  a useful tool for finding untested parts of a codebase. Test
  coverage is of little use as a numeric statement of how good your
  tests are.


![](images/testCoverage/sketch.png)


Let's look at the second statement first. I've heard of places
  that may say things like âyou can't go into production with less
  than 87% coverageâ. I've heard some people say that you should use
  things like TDD and must get 100% coverage. A wise man once
  said:


> I expect a high level of coverage. Sometimes managers require
>     one. There's a subtle difference.
> -- [Brian Marick](http://www.exampler.com/testing-com/writings/coverage.pdf)


If you make a certain level of coverage a target, people will try
  to attain it. The trouble is that high coverage numbers are too easy
  to reach with low quality testing. At the most absurd level you have
  [AssertionFreeTesting](https://martinfowler.com/bliki/AssertionFreeTesting.html). But even without that you get lots
  of tests looking for things that rarely go wrong distracting you
  from testing the things that really matter.


Like most aspects of programming, testing requires
  thoughtfulness. TDD is a very useful, but certainly not sufficient,
  tool to help you get good tests. If you are testing thoughtfully and
  well, I would expect a coverage percentage in the upper 80s or 90s.
  I would be suspicious of anything like 100% - it would smell of
  someone writing tests to make the coverage numbers happy, but not
  thinking about what they are doing.


The reason, of course, why people focus on coverage numbers is
  because they want to know if they are testing enough. Certainly low
  coverage numbers, say below half, are a sign of trouble. But high
  numbers don't necessarily mean much, and lead to [ignorance-promoting
  dashboards](https://sriramnarayan.blogspot.com/2011/04/dashboards-promote-ignorance.html?m=0). Sufficiency of testing is much more complicated
  attribute than coverage can answer. I would say you are doing enough
  testing if the following is true:

- You rarely get bugs that escape into production, **and**
- You are rarely hesitant to change some code for fear it will
  cause production bugs.


Can you test too much? Sure you can. You are testing too much if
you can remove tests while still having enough. But this is a
difficult thing to sense. One sign you are testing too much is if
your tests are slowing you down. If it seems like a simple change to
code causes excessively long changes to tests, that's a sign that
there's a problem with the tests. This may not be so much that you are
testing too many things, but that you have duplication in your tests.


Some people think that you have too many tests if they take too
long to run. I'm  less convinced by this argument. You can always move
slow tests to a later stage in your deployment pipeline, or even pull
them out of the pipeline and run them periodically. Doing these things
will slow down the feedback from those tests, but that's part of the
trade-off of build times versus test confidence.


So what is the value of coverage analysis again? Well it helps you
find which bits of your code aren't being tested. 1 It's worth running
coverage tools every so often and looking at these bits of untested
code. Do they worry you that they aren't being tested?


1: 
    By âyouâ here I mean the people writing the tests. Coverage is of
    little value to management since you need a technical background
    to understand whether the tests are good or whether the uncovered
    code is a problem.


> If a part of your test suite is weak in a way that coverage can
>   detect, it's likely also weak in a way coverage can't detect.
> -- [Brian Marick](http://www.exampler.com/testing-com/writings/coverage.pdf)


## Further Reading


Brian Marick has an excellent article on the [misuse
  of code coverage](http://www.exampler.com/testing-com/writings/coverage.pdf). And it's worth reading the [pithy commentary of Testivus](http://www.developertesting.com/archives/month200705/20070504-000425.html).


## Notes


1: 
    By âyouâ here I mean the people writing the tests. Coverage is of
    little value to management since you need a technical background
    to understand whether the tests are good or whether the uncovered
    code is a problem.
