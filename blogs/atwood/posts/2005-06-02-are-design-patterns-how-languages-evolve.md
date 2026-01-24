---
title: "Are Design Patterns How Languages Evolve?"
date: 2005-06-02
url: https://blog.codinghorror.com/are-design-patterns-how-languages-evolve/
slug: are-design-patterns-how-languages-evolve
word_count: 586
---

Paul Graham’s essay, Revenge of the Nerds, is a nearly pornographic [love letter to Lisp](http://www.paulgraham.com/icad.html). If you can manage to read all the way to the end, there’s an interesting footnote buried at the bottom:


> [Peter Norvig](http://norvig.com/design-patterns/) found that 16 of the 23 patterns in Design Patterns were “invisible or simpler” in Lisp.


He should have opened the essay with that evidence, because it strengthens his conclusion considerably:


> In the OO world you hear a good deal about “patterns.” **When I see patterns in my programs, I consider it a sign of trouble.** The shape of a program should reflect only the problem it needs to solve. Any other regularity in the code is a sign, to me at least, that I’m using abstractions that aren’t powerful enough – often that I’m generating by hand the expansions of some macro that I need to write.


There’s a Wiki entry called [Are Design Patterns Missing Language Features?](http://c2.com/cgi/wiki?AreDesignPatternsMissingLanguageFeatures) which expands and elaborates on Paul Graham’s hypothesis. It even has a handy chart of the [classic Gang of Four patterns](http://www.amazon.com/exec/obidos/ASIN/0201633612/) and the corresponding language features that implement each one. It then degrades into a weird little Wiki-fight, but the saner comments look like this:


> Has anyone ever considered that **design patterns are the way that programming languages evolve?** In the same way as communicative language, commonly used abbreviations ( or patterns ) may become standard. In English words like “won’t” and “isn’t” are abbreviations, but are more or less considered standard words today. In the same way, ‘if-then-else’ or ‘do-while’ could be considered design patterns that have now become standard features in many languages. Perhaps later languages will include many design patterns as standard features.


According to Graham, Lisp is so malleable that design patterns immediately become part of the base language; they are indistinguishable from the original core language constructs. Lisp doesn’t need to evolve – it just instantly *becomes*. One wonders, then, why Lisp hasn’t become sentient and taken over the world by now. As Paul helpfully points out, it could be because [we’re so stupid](http://www.paulgraham.com/icadmore.html):


> I also disagree that it is not believable that the vast majority of programmers have been boneheads for 40 years. It seems to me entirely possible.


All kidding aside, I tend to agree on two points:

1. **Excessive reliance on design patterns is indicative of failings in the language**. As many commenters in the wiki point out, you’d see dozens of “design patterns” in assembly or C code; these are language features that we take for granted today. We’ve certainly seen evolution along those lines even in the modest lifetime of .NET so far. There are plenty of “syntactical sugar” constructs such as `Using` which encapsulate common patterns, and even more (such as `Nullable` and Generics) on the way.
2. **Languages evolve – slowly.** It takes time to figure out the failings, shortcomings, and weaknesses of any language. Even Lisp. That’s why the [the language family tree](http://www.levenez.com/lang/) has roots going all the way back to 1954. New languages are created; old ones fall out of favor. And there’s a lot of cross-pollination between family trees. Almost all modern languages have a very complete implementation of regular expressions, which is one of the central features of the PERL language.


If anything, Lisp is strong evidence that computer language evolution is quite slow; it’s one of the oldest languages on the chart, and we’re still adapting features from it.

[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[design patterns](https://blog.codinghorror.com/tag/design-patterns/)
[lisp](https://blog.codinghorror.com/tag/lisp/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[technical practices](https://blog.codinghorror.com/tag/technical-practices/)
