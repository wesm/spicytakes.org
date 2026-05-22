---
title: "Agentic Programming"
description: "Increasingly software developers are not typing code into their IDEs.   Instead they prompt an LLM to do so, then review the results. This is a   profound change to the nature of programming, where hu"
date: 2026-05-21T00:00:00
tags: ["generative ai"]
url: https://martinfowler.com/bliki/AgenticProgramming.html
slug: AgenticProgramming
word_count: 304
---


Increasingly software developers are not typing code into their IDEs.
  Instead they prompt an LLM to do so, then review the results. This is a
  profound change to the nature of programming, where humans oversee LLM agents
  who generate the code. Humans are still responsible for what the software does
  and how it works, but use different skills to create their products.


I like to distinguish agentic programming from [Vibe Coding](https://martinfowler.com/bliki/VibeCoding.html). With vibe coding humans don't look at the code,
  indeed they forget that it even exists, while with agentic programming they are
  concerned with the code, often giving it detailed review. Agentic programming
  is also distinct from using LLMs as a sophisticated code completion mechanism,
  where LLMs participate in writing code inside an IDE environment.


This way of working hasn't got a widely established name, but the âagenticâ
  adjective is common, used as âagentic programmingâ, âagentic (software)
  engineering, âagentic codingâ, etc. (Currently I'm inclined to go with
  âagentic programmingâ.)


At the time of writing, agentic tools work in a terminal environment, the
  programmer issues prompts, which often incorporate saved documents explaining
  guidelines that the LLM should follow. The LLM then manipulates the source
  tree directly, creating and modifying files, running the code, evaluating the
  results of tests, and continuing development work, often for extended periods.
  Once done humans evaluate the agents work, doing code review, examining test
  results, and reviewing outputs from other sensors.


This shift in the nature of programming raises extensive questions about
  what kinds of activities programmers need in the future and what skills we
  require. At this point [harness engineering](https://martinfowler.com/articles/harness-engineering.html), focusing on working on the
  guides and sensors around the LLM seem central. Additionally this raises the
  importance of programmers understanding the domain they are working with,
  collaborating with users and customers to iteratively define and build their
  product.
