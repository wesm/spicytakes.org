---
title: "Given When Then"
description: "Given-When-Then is a style of representing tests - or as its   advocates would say - specifying a system's behavior usingSpecificationByExample. It's an   approach developed byDaniel Terhorst-Northand"
date: 2013-08-21T00:00:00
tags: ["testing", "domain specific language"]
url: https://martinfowler.com/bliki/GivenWhenThen.html
slug: GivenWhenThen
word_count: 629
---


Given-When-Then is a style of representing tests - or as its
  advocates would say - specifying a system's behavior using [SpecificationByExample](https://martinfowler.com/bliki/SpecificationByExample.html). It's an
  approach developed by [Daniel Terhorst-North](http://dannorth.net/about/) and Chris Matts as part of
  [Behavior-Driven
  Development](http://dannorth.net/introducing-bdd/) (BDD).  1 It appears as a structuring approach
  for many testing frameworks such as Cucumber. You can also look at
  it as a reformulation of the [Four-Phase
  Test](http://xunitpatterns.com/Four%20Phase%20Test.html) pattern.


1: 
      In review comments on this, Dan credits Ivan Moore for a
      significant amount of inspiration in coming up with this.


The essential idea is to break down writing a scenario (or test) into three
  sections:

- The **given** part describes the state of the world before
    you begin the behavior you're specifying in this scenario. You can
    think of it as the pre-conditions to the test.
- The **when** section is that behavior that you're
    specifying.
- Finally the **then** section describes the changes you
    expect due to the specified behavior.


Since we're talking about using examples as specifications, it
  makes sense to show this with an
  example 2


2: 
       from [Pete Hodgson](http://blog.thepete.net/)


```

Feature: User trades stocks
  Scenario: User requests a sell before close of trading
    Given I have 100 shares of MSFT stock
       And I have 150 shares of APPL stock
       And the time is before close of trading

    When I ask to sell 20 shares of MSFT stock
     
     Then I should have 80 shares of MSFT stock
      And I should have 150 shares of APPL stock
      And a sell order for 20 shares of MSFT stock should have been executed
  
```


The above example uses Cucumber 3, which a popular way of writing
  [BusinessFacingTests](https://martinfowler.com/bliki/BusinessFacingTest.html) but you can use the Given-When-Then
  style with any kind of tests. Some people like to put
  Given-When-Then as comments to mark informal blocks inside unit
  tests 4. I've also seen this convention
  to structure informal prose.


3: 
      Or to be strict it uses Gherkin, which is the name of Cucumber's
      DSL.


4: 
      Test frameworks tend to follow either
  naming style of xunit or BDD, the latter tend to name methods in the
  Given-When-Then style.


It's usual with this approach to see âandsâ used to combine
  multiple expressions within each clause.


I've characterized the given as a description of the
  pre-condition state because that's the way I prefer to think of it.
  A testing framework, however, interprets the givens as a set of
  commands to bring the system-under-test into the correct state before
  executing the when command. (Which is why other naming conventions
  often call this âsetupâ.) Testing frameworks provide various query
  methods for the then commands - these should
  be free of side-effects.


Although Given-When-Then style is symptomatic to BDD, the basic
  idea is pretty common when writing tests or specification by
  example. [Meszaros](https://martinfowler.com/books/xunit) describes the pattern as [Four-Phase
  Test](http://xunitpatterns.com/Four%20Phase%20Test.html). His four phases are Setup (Given), Exercise (When), Verify
  (Then) and Teardown 5. Bill Wake came up
  with the formulation as [Arrange, Act, Assert](http://xp123.com/articles/3a-arrange-act-assert/).


5: 
      Teardown isn't always needed when implementing
  tests (particularly if you are using [Automated
  Teardown](http://xunitpatterns.com/Automated%20Teardown.html)) and doesn't add much to the communication aspect of
  specification by example. So it's reasonable to see it missing from
  the BDD style.


## Notes


1: 
      In review comments on this, Dan credits Ivan Moore for a
      significant amount of inspiration in coming up with this.


2: 
       from [Pete Hodgson](http://blog.thepete.net/)


3: 
      Or to be strict it uses Gherkin, which is the name of Cucumber's
      DSL.


4: 
      Test frameworks tend to follow either
  naming style of xunit or BDD, the latter tend to name methods in the
  Given-When-Then style.


5: 
      Teardown isn't always needed when implementing
  tests (particularly if you are using [Automated
  Teardown](http://xunitpatterns.com/Automated%20Teardown.html)) and doesn't add much to the communication aspect of
  specification by example. So it's reasonable to see it missing from
  the BDD style.
