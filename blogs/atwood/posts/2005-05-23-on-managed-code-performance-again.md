---
title: "On Managed Code Performance, Again"
date: 2005-05-23
url: https://blog.codinghorror.com/on-managed-code-performance-again/
slug: on-managed-code-performance-again
word_count: 277
---

[Managed code](https://blog.codinghorror.com/on-managed-code-performance/) may be [fat and slow](https://blog.codinghorror.com/the-bloated-world-of-managed-code/), but it fares surprisingly well in Rico’s C# port of Raymond Chen’s C++ [Chinese/English dictionary reader](https://web.archive.org/web/20051227141036/http://blogs.msdn.com/ricom/archive/2005/05/10/416151.aspx):


![](https://blog.codinghorror.com/content/images/2025/05/image-96.png)


Sure, the C++ version *eventually* outperforms the managed code by a factor of 2x, but what’s interesting to me – and what this graph makes very clear – is that the point of diminishing returns has set in well before that happens. As Rico notes:

kg-card-begin: html

> *
> So am I ashamed by my crushing defeat? Hardly. **The managed code achieved a very good result for hardly any effort.** To defeat the managed version, Raymond had to:
> *
> Write his own file/io stuff
> Write his own string class
> Write his own allocator
> Write his own international mapping
> Of course he used available lower level libraries to do this, but that’s still a lot of work. Can you call what’s left an STL program? I don’t think so, I think he kept the std::vector class which ultimately was never a problem and he kept the find function. Pretty much everything else is gone.
> So, yup, you can definitely beat the CLR. I think Raymond can make his program go even faster.

kg-card-end: html

It’s a pyrrhic victory once you divide the execution time by the development time of a top Microsoft C++ coder.* Now, for certain applications at the very tip of [the development pyramid](https://blog.codinghorror.com/the-one-trillion-dollar-development-pyramid/), this tradeoff may still make sense. But that list of apps gets shorter and shorter with every passing day.


*Raymond Chen, who has “fixed more Windows bugs than you’ve had hot dinners.”

[performance](https://blog.codinghorror.com/tag/performance/)
[managed code](https://blog.codinghorror.com/tag/managed-code/)
[c#](https://blog.codinghorror.com/tag/c-2/)
[c++](https://blog.codinghorror.com/tag/c/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
