---
title: "Tradable Quality Hypothesis"
description: "I commonly come across developers who are frustrated because   âmanagement want more features, they don't care about qualityâ. I'm   always sad when I hear this, because when I hear this I know th"
date: 2011-02-21T00:00:00
tags: ["productivity"]
url: https://martinfowler.com/bliki/TradableQualityHypothesis.html
slug: TradableQualityHypothesis
word_count: 650
---


I commonly come across developers who are frustrated because
  âmanagement want more features, they don't care about qualityâ. I'm
  always sad when I hear this, because when I hear this I know that
  the developers, management and their customers have already
  lost. Their defeat has been caused by
  framing the situation in terms of the *tradable quality
  hypothesis*.


In many aspects of life, quality is something we trade-off for
  cost. A nicer car will cost more, so we might forego that Ferrari we
  fancy for something cheaper. Shall I spend the extra for really
  fresh fish at Turners, or go to the supermarket? As a result we are
  used to the idea that quality costs more. Sometimes we're prepared
  to pay, sometimes we'll go for the cheaper option.


From time to time you'll hear this notion applied to software,
  particularly software design. Refactoring some crufty code will take
  time, we'd rather add more features instead. The underlying
  assumption here is that quality is tradable, by enforcing less
  quality we gain in the other dimensions of cost, scope, or speed.


When we examine this hypothesis we have to first think about what
  we mean by quality. Quality means different things to different
  people. In a software context we might define quality as how
  pleasing the user-interface is, or how many defects show up, or how
  well-factored the software is.


I follow Kent Beck in making a distinction between internal and
  external quality. The pleasantness and effectiveness of a
  user-interface is external quality as it's something that can be
  perceived by the users of a system. That is something that can be
  sensibly involved in a trade off - do I want extra work on making
  feature A easier to use or should I add feature B?


The internal structure of the software, however, is not something
  that's directly perceivable by the user. I can't tell from using a
  program whether its internals are constructed well or not. Internal
  quality is thus a more hidden attribute. When someone says we should
  do things that reduce the design quality of a system to build more
  features, that person is applying the tradable quality hypothesis to
  internal quality.


The trouble with doing this, is that if internal quality is
  tradable, then it makes no sense to put any effort into internal
  quality at all. If a good design stops us from adding features and
  provides no benefit to the user then why do it?


The reason that people care about internal quality is because
  they think another hypothesis applies - the
  [DesignStaminaHypothesis](https://martinfowler.com/bliki/DesignStaminaHypothesis.html). In this hypothesis internal
  quality isn't tradable because **reducing internal quality slows us
  down.** It's true that not attending to design can supply a short term speed up, but this
  is only over a quite short time horizon - far shorter than most
  people think.


But the tragedy is that as soon as you frame internal quality
  as tradable, you've lost. People are so used to quality being
  tradable that even in the best circumstances you're going to have
  difficulty overcoming it. Saying that we need to spend less time
  adding new features to improve quality is just nailing down the lid.


Instead it's vital to focus on the true value of
  internal quality - that it's the enabler to speed. The purpose of
  internal quality is to go faster. This cuts both ways, of course, it
  also means you should understand how putting some time into a refactoring is
  going to help you go faster, otherwise you shouldn't be doing it.


This, by the way, is another source of disquiet I have with the
  software craftsmanship metaphor. When you say 'craft' to people, they
  imagine fine workmanship, leather panelling, smooth joints - and
  consequently higher costs. The word 'craft' reinforces the tradable
  quality hypothesis - and that's a crippling disadvantage to those of
  us who know that speed requires good design.
