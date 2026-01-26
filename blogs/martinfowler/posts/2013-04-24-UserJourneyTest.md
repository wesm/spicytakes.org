---
title: "User Journey Test"
description: "User-journey tests are a form ofBusinessFacingTest, designed   to simulate a typical user's âjourneyâ through the system. Such a   test will typically cover a user's entire interaction with the sy"
date: 2013-04-24T00:00:00
tags: ["test categories"]
url: https://martinfowler.com/bliki/UserJourneyTest.html
slug: UserJourneyTest
word_count: 186
---


User-journey tests are a form of [BusinessFacingTest](https://martinfowler.com/bliki/BusinessFacingTest.html), designed
  to simulate a typical user's âjourneyâ through the system. Such a
  test will typically cover a user's entire interaction with the system in
  order to achieve some goal. They act as one path in a use case.


They are usually [BroadStackTests](https://martinfowler.com/bliki/BroadStackTest.html) and as such, are
  usually slow to execute and prone to being brittle. Consequently
  suites of user journey tests usually aren't built to be
  comprehensive tests of a system's behavior. Usually you will have
  only a few user journey tests to exercise the integration of the
  system as a whole - probably only one path for each use case
  (usually the happy path). Verification of all the variations in
  behavior is left to tests done in different styles, usually with
  more focused coverage.


In contrast to [StoryTests](https://martinfowler.com/bliki/StoryTest.html), user journey tests are not tied to
  user stories. When you play a story you look at the existing user
  journey tests and modify them to support any change in behavior
  implied by the user story, only rarely does a user story lead to an
  entirely new user journey test.
