---
title: "Component Test"
description: "A component test is a test that limits the scope of the exercised   software to a portion of the system under test. It is in contrast to   aBroadStackTestthat's intended to exercise as much of the sys"
date: 2013-04-22T00:00:00
tags: ["test categories"]
url: https://martinfowler.com/bliki/ComponentTest.html
slug: ComponentTest
word_count: 197
---


A component test is a test that limits the scope of the exercised
  software to a portion of the system under test. It is in contrast to
  a [BroadStackTest](https://martinfowler.com/bliki/BroadStackTest.html) that's intended to exercise as much of the system
  as is reasonable.


The difference between broad-stack and component tests is one of
  degree rather than an absolute difference. Component tests can be as
  large or small as you define your components. The essence of the
  difference is that component tests deliberately neglect parts of the
  system outside the scope of the test. This is usually done by
  manipulating the system through internal code interfaces, using
  tools like [xunit](https://martinfowler.com/bliki/Xunit.html) testing tools, and by using [TestDoubles](https://martinfowler.com/bliki/TestDouble.html)
  to isolate the code under test from other components.


Component tests are usually easier to write and maintain than
  broad-stack tests. They are also faster to run, since they only hit
  part of the code base. In theory a system with excellent component
  test coverage should be free of bugs, but in practice bugs like to
  lurk in the interactions between components. Therefore it's good to
  use the [TestPyramid](https://martinfowler.com/bliki/TestPyramid.html) and combine a large quantity of
  component tests with a smaller amount of broad-stack tests.
