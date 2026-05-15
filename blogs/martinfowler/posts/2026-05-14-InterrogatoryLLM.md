---
title: "Interrogatory LLM"
description: "When we need an LLM to perform a complex task, we often need to feed it a   lot of context. Coming up with a design for a new feature requires   descriptions of how we want the feature to appear to th"
date: 2026-05-14T00:00:00
tags: ["generative ai"]
url: https://martinfowler.com/bliki/InterrogatoryLLM.html
slug: InterrogatoryLLM
word_count: 466
---


When we need an LLM to perform a complex task, we often need to feed it a
  lot of context. Coming up with a design for a new feature requires
  descriptions of how we want the feature to appear to the user, guidelines on
  how it should be implemented, information on external systems to consult, and
  so on. All this can be several pages of markdown. The obvious way to do
  this is for a human to write this context, but an alternative is to use an LLM to write
  this context after interviewing a human.


The way I can do this is to prompt the LLM to interrogate me. It should ask me
  all the questions it needs to create this appropriate context. I can feed much
  of the information it needs, and tell it other sources it needs to consult if
  it can't figure those out itself. Once it's done, it can then create the
  context report for another session (perhaps with another model) to carry out
  the next step.


I first saw a decent description of this approach in [Harper
  Reed's blog](https://harper.blog/2025/02/16/my-llm-codegen-workflow-atm/). A striking element of his approach is insisting that the LLM
  ask only one question at a time. (When I tried it, I found it needed to be
  frequently reminded of this.)


Another way to use an interrogatory LLM is to give it a document, such as a
  software specification, that captures knowledge about a domain - and then ask
  the LLM to interview a human expert to determine if the document is accurate.
  This is an alternative to getting the human expert to read the document to
  review it. People often find reviewing hard, so a conversation with an LLM
  might be more fruitful, particularly if the document isn't well-written.


Naturally we can use both of these, using one interrogatory LLM to build a
  document, then using other interrogatory LLMs to review it with other experts.


The above is getting an LLM to create or assess context for a particular
  use of an LLM. But the technique is more broadly applicable. I've become a
  natural writer, someone who finds the process of writing an essential part of
  thinking. To really understand something, I need to write about it. But
  different people are different. Many folks find writing hard, often
  *very* hard. This can be a real problem when we need to get information
  out of someone's head into a form that other humans can consume. Maybe such
  people would find it easier to ask an LLM to interview them than to write a
  document themselves. Certainly the result will have that tang of AI-writing
  that folks like me shudder at - but that's better than not having the
  information itself, either due to rushed writing or no writing at all.
