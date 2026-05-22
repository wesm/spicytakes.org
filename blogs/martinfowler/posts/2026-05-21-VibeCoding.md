---
title: "Vibe Coding"
description: "Vibe coding is building a software application by prompting an LLM, telling it   what to build, trying it out, prompting for changes - but without looking at   any of the code that the LLM generates. "
date: 2026-05-21T00:00:00
tags: ["generative ai"]
url: https://martinfowler.com/bliki/VibeCoding.html
slug: VibeCoding
word_count: 790
---


Vibe coding is building a software application by prompting an LLM, telling it
  what to build, trying it out, prompting for changes - but without looking at
  any of the code that the LLM generates. This technique can be used by people
  without any knowledge of programming. However the resulting software often
  shows problems with maintainability, correctness, and security - so is best
  used for disposable software written for a limited audience.


The term was coined in February 2025 by Andrej Karpathy, an experienced
  programmer, in a post on X:


> There's a new kind of coding I call âvibe codingâ, where you fully give
>     in to the vibes, embrace exponentials, and forget that the code even exists.
>     It's possible because the LLMs (e.g. Cursor Composer w Sonnet) are getting
>     too good. Also I just talk to Composer with SuperWhisper so I barely even
>     touch the keyboard. I ask for the dumbest things like âdecrease the padding
>     on the sidebar by halfâ because I'm too lazy to find it. I âAccept Allâ
>     always, I don't read the diffs anymore. When I get error messages I just
>     copy paste them in with no comment, usually that fixes it. The code grows
>     beyond my usual comprehension, I'd have to really read through it for a
>     while. Sometimes the LLMs can't fix a bug so I just work around it or ask
>     for random changes until it goes away. It's not too bad for throwaway
>     weekend projects, but still quite amusing. I'm building a project or webapp,
>     but it's not really coding - I just see stuff, say stuff, run stuff, and
>     copy paste stuff, and it mostly works.
> -- [Andrej Karpathy](https://x.com/karpathy/status/1886192184808149383)


The key point about vibe coding is **âforget that the code even existsâ**.
  This is what gives it much of its usefulness, but also its limitations.


Since the [November Inflection](https://martinfowler.com/bliki/NovemberInflection.html) many programmers are
  getting LLMs to write all their code, commenting that they may never write a
  line of code directly again. However they do care about this code, reviewing
  it, paying attention to its internal structure. In that case, they aren't
  forgetting the code exists, so it's really a different thing that I call
  [Agentic Programming](https://martinfowler.com/bliki/AgenticProgramming.html). Sadly the term âvibe codingâ really
  caught on, so many people use it to mean agentic programming. However I feel
  that despite this rapid [Semantic Diffusion](https://martinfowler.com/bliki/SemanticDiffusion.html), it's worth
  trying to keep the concepts of vibe coding and agentic programming separate,
  as they are both different to use and different in their consequences.


Because a vibe coder doesn't look at the code, they don't need programming
  skills, so it's perfect for someone with no programming knowledge to build
  applications for their own use. Experienced programmers may also find it handy
  for rapid development of disposable software or prototypes.


Vibe coding
  is still new, so we are exploring its limitations, and those limitations
  change as the sophistication of models and their [harnesses](https://martinfowler.com/articles/harness-engineering.html) change. These
  limitations do introduce considerable risks, particularly if the vibed
  software is used widely or has access to sensitive information.


Perhaps the most serious risk is that of security. LLMs are inherently
  vulnerable as they provide a large attack surface for predators. Vibe coded
  applications can often expose sensitive information or worse, credentials to
  attack deeper into an organization's systems. Even non-programmers need to be
  aware of the [Lethal
  Trifecta](https://martinfowler.com/articles/agentic-ai-security.html#lethal-trifecta).


With little attention to the code, vibed software can rapidly produce
  many lines of code of a very low quality. Such code makes it difficult, even for an LLM,
  to modify and enhance the software in the future. While it's possible that
  growing LLM capabilities will allow it to work with even the largest bowls of
  spaghetti software, thus far it seems clear that well-structured software
  makes life easier for LLMs too.


LLMs are famous for habit of hallucinating incorrect facts and presenting
  these with great confidence. This habit also leads them to create software
  that behaves incorrectly - and those errors may not be manifest to the user.
  Furthermore the non-determinism of LLMs means that it's likely that asking an
  LLM to enhance some software could easily lead it to introduce errors, even in
  parts of the code that shouldn't change due to the new request. We should thus
  treat LLM-generated software with skepticism, it can still be useful, but we
  need to be aware of the risks.


On the whole vibe coding software is best used for disposable software
  that's only used by its author or a close group of collaborators who
  understand and accept the risks involved. Code that is more complex, more
  widely-used, and with more consequences to its risks should not be forgotten about.
