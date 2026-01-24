---
title: "Performance Considered Harmful"
date: 2004-09-14
url: https://blog.codinghorror.com/performance-considered-harmful/
slug: performance-considered-harmful
word_count: 361
---

Scott Hanselman continues to impress with his consistently useful blog entries, this time an [observation about performance](http://www.hanselman.com/blog/PermaLink.aspx?guid=9a741bf3-f99f-4737-9a2e-000328d54e37). I found an even more interesting link buried in the comments, though: the Eric Lippert post, [How Bad is Good Enough?](https://web.archive.org/web/20051222102846/http://blogs.msdn.com/ericlippert/archive/2003/10/17/53237.aspx)


> *I’ve read articles about the script engines that say things like “you should use And 1 to determine whether a number is even rather than Mod 2 because the chip executes the And instruction faster”, as though VBScript compiled down to tightly optimized machine code. People who base their choice of operator on utterly nonsensical rationales are not going to write code that is maintainable or robust. **Those programs end up broken, and ****“broken****” is the ultimate in bad performance, no matter how fast the incorrect program is.**
> If you want to write fast code – in script or not – then ignore every article you ever see on “tips and tricks” that tell you which operators are faster and what the cost of dimensioning a variable is. Writing fast code does not require a collection of cheap tricks, it requires analysis of user scenarios to set goals, followed by a rigorous program of careful measurements and small changes until the goals are reached.
> And don’t forget also that RIGHT is better than FAST. Write the code to be extremely straightforward. Code that makes sense is code which can be analyzed and maintained, and that makes it performant. Consider our “unused Dim” example – the fact that an unused Dim has a 50 ns cost is irrelevant. It’s an unused variable. It’s worthless code. It’s a distraction to maintenance programmers. That’s the real performance cost – it makes it harder for the devs doing the perf analysis to do their jobs well!*


It’s a fascinating corollary to my previous post on this topic, [Why Aren’t My Optimizations Optimizing?](https://blog.codinghorror.com/why-arent-my-optimizations-optimizing/) This is what I refer to as the **“we have met the enemy, and he is us”** phenomenon. That’s one key difference I’ve observed between a good developer and a great developer – great developers realize that they are their own worst enemies.

[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[performance tuning](https://blog.codinghorror.com/tag/performance-tuning/)
[optimization](https://blog.codinghorror.com/tag/optimization/)
[maintainability](https://blog.codinghorror.com/tag/maintainability/)
