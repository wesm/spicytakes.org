---
title: "LLMs bring new nature of abstraction"
description: "Like most loudmouths in this field, I've been paying a lot of attention     to the role that generative AI systems may play in software development. I     think the appearance of LLMs will change soft"
date: 2025-06-24T00:00:00
tags: ["generative ai"]
url: https://martinfowler.com/articles/2025-nature-abstraction.html
slug: 2025-nature-abstraction
word_count: 548
---


Like most loudmouths in this field, I've been paying a lot of attention
    to the role that generative AI systems may play in software development. I
    think the appearance of LLMs will change software development to a similar
    degree as the change from assembler to the first high-level programming
    languages. The further development of languages and frameworks increased our
    abstraction level and productivity, but didn't have that kind of impact on
    the *nature* of programming. LLMs are making that degree of impact, but with
    the distinction that it isn't just raising the level of abstraction, but
    also forcing us to consider what it means to program with non-deterministic
    tools.


High-Level Languages (HLLs) introduced a radically new level of abstraction. With assembler I'm
    thinking about the instruction set of a particular machine. I have to figure
    out how to do even simple actions by moving data into the right registers to
    invoke those specific actions. HLLs meant I could now think in terms of
    sequences of statements, conditionals to choose between alternatives, and
    iteration to repeatedly apply statements to collections of data values. I
    can introduce names into many aspects of my code, making it clear what
    values are supposed to represent. Early languages certainly had their
    limitations. My first professional programming was in Fortran IV, where âIFâ
    statements didn't have an âELSEâ clause, and I had to remember to name my
    integer variables so they started with the letters âIâ through âNâ.


Relaxing such restrictions and gaining block structure (âI can have more
    than one statement after my IFâ) made my programming easier (and more fun)
    but are the same kind of thing. Now I hardly ever write loops, I
    instinctively pass functions as data - but I'm still talking to the machine
    in a similar way than I did all those days ago on the Dorset moors with
    Fortran. Ruby is a far more sophisticated language than Fortran, but it has
    the same ambiance, in a way that Fortran and PDP-11 machine instructions do
    not.


Thus far I've not had the opportunity to do more than dabble with the
    best Gen-AI tools, but I'm fascinated as I listen to [friends and
    colleagues](https://martinfowler.com/articles/exploring-gen-ai.html) share their experiences. I'm convinced that this is another
    fundamental change: talking to the machine in prompts is as different to
    Ruby as Fortran to assembler. But this is more than a huge jump in
    abstraction. When I wrote a Fortran function, I could compile it a hundred
    times, and the result still manifested the exact same bugs. Large Language Models introduce a
    non-deterministic abstraction, so I can't just store my prompts in git and
    know that I'll get the same behavior each time. As my [colleague
    Birgitta put it](https://martinfowler.com/articles/exploring-gen-ai/07-how-is-this-different.html), we're not just moving *up* the abstraction levels,
    we're moving *sideways* into non-determinism at the same time.


![Previous improvements raise the level of abstraction, but LLMs go sideways](https://martinfowler.com/articles/exploring-gen-ai/abstraction-levels-with-genai.png)


illustration: Birgitta BÃ¶ckeler


As we learn to use LLMs in our work, we have to figure out how to
    live with this non-determinism. This change is dramatic, and rather excites
    me. I'm sure I'll be sad at some things we'll lose, but there will also
    things we'll gain that few of us understand yet. This evolution in
    non-determinism is unprecedented in the history of our profession.


---
