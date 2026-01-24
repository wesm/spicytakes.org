---
title: "The Girl Who Proved P = NP"
date: 2009-06-01
url: https://blog.codinghorror.com/the-girl-who-proved-p-np/
slug: the-girl-who-proved-p-np
word_count: 647
---

One of my all time favorite blog entries is a truly epic tale of dating gone wrong that culminates in [the strangest reference to P=NP](http://www.joeydevilla.com/2003/04/07/what-happened-to-me-and-the-new-girl-or-the-girl-who-cried-webmaster/) you’ll probably ever encounter.

kg-card-begin: html

> **Joey**: So you really did graduate from computer engineering?
> **New Girl**: Yes I did, from UBC!
> **Joey**: And you took the “Algorithms” course?
> **New Girl**: Of course!
> **Joey**: And you have all the papers you wrote?
> **New Girl**: *Yes!* I kept them all, and I’ll show them to you tomorrow!
> **Joey**: I want to see the one we always called the “Hell Paper” at Queen’s – the mandatory fourth-year paper. You know the one, where we prove P = NP?
> **New Girl**: I did that! I proved P = NP! I placed near the top of the class, and the professor used my paper as an example!
> **Joey**: You proved P = NP?
> **New Girl**: Yes!
> **Joey**: Gotcha.

kg-card-end: html

Poor Joey. Dating crazy people is one thing, but dating crazy people who *claim to have proved P=NP* is another matter entirely. I know, I know, [my track record with P=NP](https://blog.codinghorror.com/your-favorite-np-complete-cheat/) is hardly any better. But at least you’re not dating me, right?


NP completeness is one of the great [unsolved mysteries in computer science](https://web.archive.org/web/20100704092145/http://www.claymath.org/millennium/P_vs_NP/); perhaps the best way to illustrate is through [this xkcd cartoon](http://xkcd.com/287/):


![](https://blog.codinghorror.com/content/images/2025/04/image-380.png)


The defining characteristic of an NP-complete problem is that optimal solutions, using math and logic as we currently understand them, are effectively impossible. Sure, you can approximate a solution, but an *optimal* solution requires so many calculations as to be infeasible, even with computers that operated at, say... the speed of light.


> In fact, one of the outstanding problems in computer science is determining whether questions exist whose answer can be quickly checked, but which require an impossibly long time to solve by any direct procedure. Problems like the one listed above certainly seem to be of this kind, but so far no one has managed to prove that any of them really are so hard as they appear, **i.e., that there really is no feasible way to generate an answer with the help of a computer.**


It’s doubtful whether anyone will [ever prove that P=NP](http://www.cs.umd.edu/~gasarch/papers/poll.pdf) (pdf), but in the meantime it’s useful to recognize [problems that are NP complete](https://web.archive.org/web/20100327144833/http://max.cs.kzoo.edu/~kschultz/CS510/ClassPresentations/NPCartoons.html):

kg-card-begin: html

> Unfortunately, proving inherent intractability can be just as hard as finding efficient algorithms.
>     The theory of NP-completeness provides many straightforward techniques for proving that a given problem is “just as hard” as a large number of other problems that are widely recognized as being difficult and that have been confounding the experts for years. Armed with these techniques, you might be able to prove that the bandersnatch problem is NP-complete and march into your boss’s office and announce:
> *I can’t find an efficient algorithm, but neither can all these famous people.*
>     At the very least, this would inform your boss that it would do no good to fire you and hire another expert on algorithms.
>     Now you can spend your time looking for efficient algorithms that solve various special cases of the general problem. You might look for algorithms that, though not guaranteed to run quickly, seem likely to do so most of the time. Or you might even relax the problem somewhat, looking for a fast algorithm that merely finds designs that meet most of the component specifications. Thus, the primary application of the theory of NP-completeness is to assist algorithm designers in directing their problem-solving efforts toward those approaches that have the greatest likelihood of leading to useful algorithms.

kg-card-end: html

As with so many things in programming, **the first step is learning enough to know when you’re *really* screwed**.


Unfortunately for poor Joey, this sad corollary to NP-completeness apparently applies to dating, too.

[algorithms](https://blog.codinghorror.com/tag/algorithms/)
[computer engineering](https://blog.codinghorror.com/tag/computer-engineering/)
[p=np](https://blog.codinghorror.com/tag/p-np/)
