---
title: "Story Test"
description: "Story tests areBusinessFacingTestsused to describe and verify   the software delivered as part of aUserStory. When a story is   elaborated the team creates several story tests that act as   acceptance"
date: 2013-04-24T00:00:00
tags: ["test categories", "bad things"]
url: https://martinfowler.com/bliki/StoryTest.html
slug: StoryTest
word_count: 176
---


Story tests are [BusinessFacingTests](https://martinfowler.com/bliki/BusinessFacingTest.html) used to describe and verify
  the software delivered as part of a [UserStory](https://martinfowler.com/bliki/UserStory.html). When a story is
  elaborated the team creates several story tests that act as
  acceptance criteria for the story. The story tests can be combined
  into a regression suite for the software and provide traceability
  from the requirements (user stories) to tests and (through execution)
  to the behavior of the system. Story tests are usually [BroadStackTests](https://martinfowler.com/bliki/BroadStackTest.html).


User stories are popular because they offer a simple
  workflow, each story adds new tests to the story test suite.
  However story tests often lead to problems. Regularly adding story
  tests leads to a large body of tests, often with significant
  duplication between them. When behavior needs to change in later
  iterations of the project, duplication in tests can take a painful amount
  of time to update. Furthermore broad-stack story tests take a long
  time to execute, which is why having a lot of them violates the
  [TestPyramid](https://martinfowler.com/bliki/TestPyramid.html). As a result many people recommend using just
  a few [UserJourneyTests](https://martinfowler.com/bliki/UserJourneyTest.html) together with business-facing
  [ComponentTests](https://martinfowler.com/bliki/ComponentTest.html).
