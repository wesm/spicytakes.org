---
title: "The best software engineering paper you haven't read"
date: 2018-01-12
url: https://www.hillelwayne.com/post/the-best-se-paper/
slug: the-best-se-paper
word_count: 675
---

I want to call attention to one of the best papers I’ve ever read on software engineering, ever. Ready to be dazzled? Here goes:


[Fixing Faults in C and Java Source Code: Abbreviated vs. Full-Word Identifier Names](http://www2.unibas.it/gscanniello/Giuseppe_Scanniello%40unibas/Home_files/TOSEM.pdf) (preprint)


I know, right? *Sheer brilliance*.


Okay, maybe it doesn’t have the most exciting subject matter, but I think everybody should read it. Here’s why:


**Manageable scope.** “Is clean code good?” Too broad, what is ‘clean code’ and what is ‘good’? “Are complete variable names better than abbreviations?” Still too broad, how do we mean ‘better’? “Do complete variable names lead to faster finding of defects?” That’s something we can focus on.


**They did their homework.** They start with an entire literature review! Literature reviews are really hard to do and they aced it. Every possibly relevant paper is brought up, discussed, and clarified how much it differs from what they are trying to do. It might seem like table stakes but it’s far more comprehensive than any other paper I’ve read in SE. Heck, they might have been able to stretch that intro into a full paper, and they didn’t.


**They mix qualitive and quantitative methods.** We tend to overvalue quantitative methods (controlled experiments, data mining) and undervalue qualitative methods (interviews, ethnographies, tailing people). We need hard numbers to answer research questions, sure, but we need quals to know what questions we should even be asking. They do an experiment and then follow it up with an ethnography where they study how programmers debug abbreviated codebases. And they find some pretty interesting things.


**Objective measure of Defects.** In *Leprechauns of Software Engineering* Laurent Bossavit talks about how most people use words like “errors” and “quality” without rigorously defining it, so we have no way of knowing what we’re actually seriously measuring. They don’t fall into this trap. How? They took existing codebases and deliberately added specific faults. Not only do we have an objective measure of ‘defects’ now, we know exactly where they are.


**Really, *really* good experimental setup**. Every paper needs to have something called “Threats to validity”, which is a section where they talk about potential objections to the claims. This does not mean that these threats make the data wrong- they’re just reasons not to fully trust the results. At the most extreme, it’s something like [not actually running any of the code people wrote](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.368.1058&rep=rep1&type=pdf). More commonly, it’s stuff like “not accounting for variances in programmers” or “time of day” or whatnot. Most engineering papers are rife with threats to validity. These people, though, go to incredible lengths to rule them all out.

- “Your sample size is too small!” They have 100, which is still on the smaller side but way bigger than most studies.
- “You only tested this with newbies! It’s different for professionals!” They tested with both CS undergrads, CS grads, and professionals.
- “The codebase is a toy problem, not Real Code!” They used several complete public codebases.
- “The abbreviated codebases are different from the full-name ones!” They manually abbreviated every single codebase, so there were two copies of each: one with zero abbreviations, one with only abbreviations.


**Their experiment design is fantastic, too.** Everybody’s tested twice, once with abbreviations, once without. They’re tested on different codebases so there’s no familiarity and different times of day to account for energy levels. People are tested in four subgroups, so the researchers could study individual differences, intra-group differences, and inter-group differences. Then they analyze the results with high-powered statistics. The upshot is they can pretty much control for every possible factor, including language, experience level, fatigue, experimenter biases…


**And then an ethnography.** They watched programmers tackle each codebase and noted the differences between the abbreviated and unabbreviated source codes. I’m not going to try to summarize it. Seriously, it’s a great paper and you should read it.


Ultimately, they found no significant difference between abbreviated and full names. Unexpected, but the care they put into this reason makes me completely willing to trust them. I can’t recommend this paper enough.
