---
title: "Machine Justification"
description: "I remember in my teens being told of the wonderful things Artificial Intelligence (AI)   would do in the next few years. Now severaldecadeslater, some of these seem to be   happening. The most recent "
date: 2017-11-14T00:00:00
tags: ["data analytics"]
url: https://martinfowler.com/bliki/MachineJustification.html
slug: MachineJustification
word_count: 599
---


I remember in my teens being told of the wonderful things Artificial Intelligence (AI)
  would do in the next few years. Now several *decades* later, some of these seem to be
  happening. The most recent triumph was of [computers teaching each other to play Go](https://www.theatlantic.com/technology/archive/2017/10/alphago-zero-the-ai-that-taught-itself-go/543450/) by
  playing against each other, rapidly becoming more proficient than any human, with
  strategies human experts could barely comprehend. It's natural to wonder what will
  happen over the next few years, will computers soon have greater intelligence than
  humanity? (Given some recent election results, that may not be too hard a bar to cross.)


But as I hear of these, I recall Pablo Picasso's [comment](https://quoteinvestigator.com/2011/11/05/computers-useless/) about computers many decades
  ago: âComputers are useless. They can only give you answersâ. The kind of reasoning that
  techniques such as Machine Learning can result in are truly impressive in their results,
  and will be useful to us as users and developers of software. But answers, while useful,
  aren't always the whole picture. I learned this in my early days of school - just
  providing the answer to a math problem would only get me a couple of marks, to get the
  full score I had to show *how* I got it. The reasoning that got to the answer was more
  valuable than the result itself. That's one of the limitations of the self-taught Go
  AIs. While they can win, they cannot explain their strategies.


Given this world, one of the big challenges I see for AI is that while we may have
  figured out Machine Learning in order to teach them to get answers, we  haven't got
  systems that can do Machine Justification for their answers. As AIs make more judgments for
  us, we'll increasingly run into situations where the answer isn't enough. An AI might be
  trained in such a way to rule on legal cases, but could we accept a judgment where the
  AI cannot explain its reasoning?


Given this it seems likely that we will need a new class of âprogrammer' in the
  future, one whose job is to figure out why AIs get the answer they do, to deduce the
  reasoning underlying the AIs skills. We could see many fields where AIs make opaque
  judgments that we can see are good, but need another approach for us to really learn
  the theory that underlies their decisions.


This problem is particularly acute since we've discovered that it's awfully easy for
  these machines to learn undesirable behaviors from their training data, such as
  [discriminating against racial minorities](https://www.theatlantic.com/technology/archive/2016/12/how-algorithms-can-bring-down-minorities-credit-scores/509333/) when judging credit ratings.


Like many, I see much of the opportunity of computers is in collaboration with
  humans. Good use of computers is understanding where the computer is strong (rapidly
  doing constrained work) and where humans are better, and using a mix. Computers are, at
  their most intellectual, a tool for the mind. In programming I'm happy to lean on the
  compiler to help me find errors or suggest alternatives, a practice which I was scolded
  for as a young programmer. That boundary between where the two are strongest is fluid,
  and one of the fascinations of the future is how we can best take advantage of its movement.


## Further Reading


[MIT Technology Review](https://www.technologyreview.com/s/604087/the-dark-secret-at-the-heart-of-ai/) looks at the broad topic of
    explainability for AI.


Some articles in the dangers of machine learning and undesirable bias from [The Atlantic](https://www.theatlantic.com/technology/archive/2016/12/how-algorithms-can-bring-down-minorities-credit-scores/509333/), [NPR](https://www.npr.org/sections/alltechconsidered/2017/03/31/521946210/will-using-artificial-intelligence-to-make-loans-trade-one-kind-of-bias-for-anot), and [Tech Republic](https://www.techrepublic.com/article/bias-in-machine-learning-and-how-to-stop-it/)


## Acknowledgements

Brandon Byars, Chris Ford, Christoph Windheuser, Danilo Sato, Dave Elliman, Ian
    Cartwright, Kent Rahman, Saleem Siddiqui, Sallie Walecka, Tito Sarrionandia, and
    Vishal Bardoloi

    discussed drafts of this post on our internal mailing lists.