---
title: "Learn to Read the Source, Luke"
date: 2012-04-16
url: https://blog.codinghorror.com/learn-to-read-the-source-luke/
slug: learn-to-read-the-source-luke
word_count: 945
---

In the calculus of communication, writing coherent paragraphs that your fellow human beings can comprehend and understand is [*far* more difficult](https://blog.codinghorror.com/is-writing-more-important-than-programming/) than tapping out a few lines of software code that the interpreter or compiler won’t barf on.


That’s why, when it comes to code, [all the documentation probably sucks](https://blog.codinghorror.com/if-it-isnt-documented-it-doesnt-exist/). And because writing for people is way harder than writing for machines, the documentation will *continue* to suck for the foreseeable future. There’s very little you can do about it.


Except for one thing.


![](https://blog.codinghorror.com/content/images/2025/04/image-611.png)


You can **learn to read the source, Luke**.


The transformative [power of “source always included”](https://blog.codinghorror.com/the-power-of-view-source/) in JavaScript is a major reason why I coined – and continue to believe in – [Atwood’s Law](https://blog.codinghorror.com/the-principle-of-least-power/). Even if “view source” isn’t built in (but it totally should be), you should demand access to the underlying source code for your stack. **No matter what the documentation says, the source code is the ultimate truth, the best and most definitive and up-to-date documentation you’re likely to find.** This will be true *forever*, so the sooner you come to terms with this, the better off you’ll be as a software developer.


I had a whole entry I was going to write about this, and then I discovered [Brandon Bloom’s](https://web.archive.org/web/20120420020815/http://blog.brandonbloom.name/) brilliant [post](http://news.ycombinator.com/item?id=3769446) on the topic at Hacker News. Read closely, because he explains the virtue of reading source, and in what context you *need* to read the source, far better than I could:

kg-card-begin: html

> I started working with Microsoft platforms professionally at age 15 or so. I worked for Microsoft as a software developer doing integration work on Visual Studio. More than ten years after I first wrote a line of Visual Basic, I wish I could never link against a closed library ever again.
> Using software is different than building software. When you’re using most software for its primary function, it’s a well worn path. Others have encountered the problems and enough people have spoken up to prompt the core contributors to correct the issue. But when you’re building software, you’re doing something new. And there are so many ways to do it, you’ll encounter unused bits, rusty corners, and unfinished experimental code paths. You’ll encounter edge cases that have been known to be broken, but were worked around.
> Sometimes, the documentation isn’t complete. Sometimes, it’s wrong. The source code never lies. For an experienced developer, reading the source can often be faster… especially if you’re already familiar with the package’s architecture. I’m in a medium-sized co-working space with several startups. A lot of the other CTOs and engineers come to our team for guidance and advice on occasion. **When people report a problem with their stack, the first question I ask them is: “Well, did you read the source code?”**
> I encourage developers to git clone anything and everything they depend on. Initially, they are all afraid. “That project is too big, I’ll never find it!” or “I’m not smart enough to understand it” or “That code is so ugly! I can’t stand to look at it.” But you don’t have to search the whole thing, you just need to follow the trail. And if you can’t understand the platform below you, how can you understand your own software? And most of the time, what inexperienced developers consider beautiful is superficial, and what they consider ugly, is battle-hardened production-ready code from master hackers.
> Now, a year or two later, I’ve had a couple of developers come up to me and thank me for forcing them to sink or swim in other people’s code bases. They are better at their craft and they wonder how they ever got anything done without the source code in the past.
> When you run a business, if your software has a bug, your customers don’t care if it is your fault or Linus’ or some random Rails developer’s. They care that your software is bugged. Everyone’s software becomes my software because all of their bugs are my bugs. When something goes wrong, you need to seek out what is broken, and you need to fix it. You fix it at the right spot in the stack to minimize risks, maintenance costs, and turnaround time. Sometimes, a quick workaround is best. Other times, you’ll need to recompile your compiler. Often, you can ask someone else to fix it upstream, but just as often, you’ll need to fix it yourself.
> Closed-software shops have two choices: beg for generosity, or work around it.
> Open source shops with weaker developers tend to act the same as closed-software shops.
> Older shops tend to slowly build the muscles required to maintain their own forks and patches and whatnot.
> True hackers have come to terms with a simple fact: If it runs on my machine, it’s my software. I’m responsible for it. I must understand it. Building from source is the rule and not an exception. I must control my environment and I must control my dependencies.

kg-card-end: html

Nobody reads other people’s code for fun. Hell, I don’t even like [reading my own code](https://blog.codinghorror.com/nobody-hates-software-more-than-software-developers/). The idea that you’d settle down in a deep leather chair with your smoking jacket and a snifter of brandy for a fine evening of reading through someone else’s code is absurd.


But we need access to the source code. We *must* read other people’s code because [we have to understand it](https://blog.codinghorror.com/when-understanding-means-rewriting/) to get things done. So don’t be afraid to **read the source, Luke** – and follow it wherever it takes you, no matter how scary looking that code is.

[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[software documentation](https://blog.codinghorror.com/tag/software-documentation/)
[javascript](https://blog.codinghorror.com/tag/javascript/)
[source code](https://blog.codinghorror.com/tag/source-code/)
[software development practices](https://blog.codinghorror.com/tag/software-development-practices/)
