---
title: "Business Facing Test"
description: "User-journey tests are a form ofBusinessFacingTest, designed   to simulate a typical user's âjourneyâ through the system. Such a   test will typically cover a user's entire interaction with the sy"
date: 2013-04-24T00:00:00
tags: ["test categories"]
url: https://martinfowler.com/bliki/BusinessFacingTest.html
slug: BusinessFacingTest
word_count: 232
---


A business-facing test is a test that's intended to be used as an
  aid to communicating with the non-programming members of a
  development team such as customers, users, business analysts and the
  like. When automated, they describe the system in domain-oriented terms,
  ignoring the component architecture of the system itself.
  Business-facing tests are often used as acceptance criteria, having
  such tests pass indicates the system provides the functionality that
  the customer expects.


Automated business-facing tests are often represented in some form of
  [DomainSpecificLanguage](https://martinfowler.com/bliki/DomainSpecificLanguage.html), since this helps communication with
  non-programmers and also helps give programmers a mechanism that helps them
  step back from the details of the code. Tools like [Cucumber](http://cukes.info) and Twist help design such DSLs and provide
  mechanisms to bind them to the system under test.


Business-facing tests are commonly implemented as
  [BroadStackTests](https://martinfowler.com/bliki/BroadStackTest.html) since their user-oriented expression
  suggests treating the system under test as a black box. However
  there are significant advantages to implementing business-facing
  tests as [ComponentTests](https://martinfowler.com/bliki/ComponentTest.html) since this often results in
  easier maintenance and faster execution.


I'm a big fan of automated testing, but it's important to recognize
  that manual tests play a significant role in business-facing
  testing. Techniques such as exploratory testing and usability
  testing are inherently manual activities and are essential parts of
  a well-balanced test portfolio.


[StoryTests](https://martinfowler.com/bliki/StoryTest.html) and [UserJourneyTests](https://martinfowler.com/bliki/UserJourneyTest.html) are two
  common forms of business-facing test. The term business-facing test
  comes from [Brian
  Marick's test quadrant](http://www.exampler.com/old-blog/2003/08/21/#agile-testing-project-1).
