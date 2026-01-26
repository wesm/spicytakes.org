---
title: "Broad Stack Test"
description: "Story tests areBusinessFacingTestsused to describe and verify   the software delivered as part of aUserStory. When a story is   elaborated the team creates several story tests that act as   acceptance"
date: 2013-04-24T00:00:00
tags: ["test categories"]
url: https://martinfowler.com/bliki/BroadStackTest.html
slug: BroadStackTest
word_count: 261
---


A broad-stack test is a test that exercises most of the parts of a
  large application. It's often referred to as an **end-to-end test** or
  **full-stack test**. It
  lies in contrast to a [ComponentTest](https://martinfowler.com/bliki/ComponentTest.html), which only exercises
  a well-defined part of a system.


The difference between a broad-stack test and a component test is
  a continuum rather than a clear line. One area where bits can be missing from the
  fullness of the stack is how the test manipulates the application.
  Broad-stack tests often manipulate the application through a UI, such
  as testing web applications with tools like Selenium and Sahi.
  However a [SubcutaneousTest](https://martinfowler.com/bliki/SubcutaneousTest.html) can also be a broad-stack test
  if it continues to exercise most of the rest of the software. To
  further limit the scope, a test that exercises an application
  through a service interface can also be considered to be broad-stack
  test of the the server.


The other area where these tests don't cover the full breadth of
  the stack lies in connection to remote systems. Many people,
  including myself, think that tests that call remote systems are
  unnecessarily slow and brittle. It is usually better to use
  [TestDoubles](https://martinfowler.com/bliki/TestDouble.html) for these remote systems and check the
  doubles with [ContractTests](https://martinfowler.com/bliki/ContractTest.html)


Broad-stack tests have the advantage of exercising the application
  with all its parts connected together and thus can find bugs in the
  interaction between components in the way that component tests
  cannot. However broad-stack tests also tend to be harder to maintain and
  slower to run than component tests. As a result the [TestPyramid](https://martinfowler.com/bliki/TestPyramid.html)
  suggests using fewer broad-stack tests.
