---
title: "KISS and YAGNI"
date: 2004-10-21
url: https://blog.codinghorror.com/kiss-and-yagni/
slug: kiss-and-yagni
word_count: 383
---

Microsoft performance guy, Rico, touches on a topic near and [dear to my heart](https://web.archive.org/web/20051205091425/http://blogs.msdn.com/ricom/archive/2004/10/19/244735.aspx):


> *I hardly think that one can make any conclusions about which vendor has the edge in performance from my article on Performance Tidbits. If I was to summarize my advice in that blog in a few words it would be “don’t use OOP features that you don’t need.”
> This is not to say that you should shun virtual functions, inheritance, or other features of modern programming languages. Far from it, often they not only add clarity and maintainability they also improve performance. **But, as often, I find that people have written their code in some elaborate way when a much simpler model would have been equally serviceable and more performant.** Whatever programming religion you may have I think you’ll agree that more complex language abstractions do not inherently help your design – rather each more sophisticated feature starts at a net negative and must somehow earn its way to positiveness with benefits such as clarity, ease of maintenance, performance, and so forth.*


So when I say things like, “don’t use a delegates if regular polymorphism would do,” I don’t mean that you should avoid delegates. I mean that you should not use them if they are overkill.


Don’t use fancy OOP features *just because you can*. Use fancy OOP features because they have specific, demonstrable benefit to the problem you’re trying to solve. You laugh, but like Rico, **I see this all the time**. Most programmers  have never met [an object they didn’t like](https://blog.codinghorror.com/inherits-nothing/). I think it should be the other way around: these techniques are guilty until proven innocent in the court of KISS ([Keep It Simple, Stupid](http://en.wikipedia.org/wiki/KISS_Principle)).


As developers, I think we also tend to be far too optimistic in assessing the generality of our own solutions, and thus we end up building elaborate OOP frameworks around things that may not justify that level of complexity. To combat this urge, I suggest following the YAGNI ([You Aren’t Gonna Need It](http://c2.com/cgi/wiki?YouArentGonnaNeedIt=)) doctrine. Build what you need as you need it, aggressively refactoring as you go along; don’t spend a lot of time planning for grandiose, unknown future scenarios. Good software can evolve into what it will ultimately become.

[oop](https://blog.codinghorror.com/tag/oop/)
[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[kiss](https://blog.codinghorror.com/tag/kiss/)
[yagni](https://blog.codinghorror.com/tag/yagni/)
