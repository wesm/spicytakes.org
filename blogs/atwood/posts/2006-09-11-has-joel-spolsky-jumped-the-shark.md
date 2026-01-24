---
title: "Has Joel Spolsky Jumped the Shark?"
date: 2006-09-11
url: https://blog.codinghorror.com/has-joel-spolsky-jumped-the-shark/
slug: has-joel-spolsky-jumped-the-shark
word_count: 819
---

When you’re starting out as a technical blogger, you’ll inevitably stumble across [Joel on Software](http://www.joelonsoftware.com/). He’s been blogging since the year 2000, when computers were hand-carved of wood and the internet transmitted data via carrier pigeon. He has his own [software development company](https://glitch.com/), a few [books](http://www.amazon.com/exec/obidos/ASIN/1893115941) under his belt, and he’s an outstanding and entertaining writer by any measure. In many ways, Joel is a legend.


Although Joel’s blog entries are generally pure gold, he has generated his fair share of controversy in the last six years. For example, he [doesn’t like programming using exceptions](http://www.joelonsoftware.com/items/2003/10/13.html), despite the fact that they are [the bread and butter](http://www.nedbatchelder.com/text/exceptions-vs-status.html) of modern programming languages. He also said that [teaching new programmers only Java](http://www.joelonsoftware.com/articles/ThePerilsofJavaSchools.html) is liable to poison their minds, although I think Java is [the least](http://www.nedbatchelder.com/blog/20060101T073856.html) of any budding new programmer’s problems. But a few of Joel’s recent posts go far, far beyond these minor gaffes.


For instance, two weeks ago we found out that Joel’s company wrote their flagship product, FogBugz, in a [proprietary language they created themselves](http://www.joelonsoftware.com/items/2006/09/01.html).


> FogBugz is written in Wasabi, a very advanced, functional-programming dialect of Basic with closures and lambdas and Rails-like active records that can be compiled down to VBScript, JavaScript, PHP4 or PHP5. **Wasabi is a private, in-house language written by one of our best developers that is optimized specifically for developing FogBugz**; the Wasabi compiler itself is written in C#.


You couldn’t possibly have heard it, but that was the sound of fifty thousand programmers’ heads simultaneously exploding.


Writing your own language is absolutely beyond the pale. It’s a toxic decision that is so completely at odds with Joel’s previous excellent and sane advice on software development that people *literally thought he was joking*. He had to write [an entire follow-up post](http://www.joelonsoftware.com/items/2006/09/01b.html) to explain that, no, he *wasn’t* kidding.


Read his defense of Wasabi. If anything, it *amplifies* the insanity. Because, you know, installing a PHP/NET/Java runtime at a customer site is totally unsupportable, even though it’s the business model of 99.9% of the rest of the world. And with Wasabi, they can add any language features they want! Just like Lisp, right? And eventually they’ll plug in a .NET CLR back-end to Wasabi and generate bytecode! Never mind the fact that your company’s flagship application is still written in a freaky custom language based on *VBScript* that only three people in the world know how to program.


But wait! It gets worse!


![](https://blog.codinghorror.com/content/images/2025/05/image-354.png)


Now Joel says that a dynamically typed language like Ruby can’t possibly be [fast enough to run FogBugz](http://www.joelonsoftware.com/items/2006/09/12.html):


> I understand the philosophy that developer cycles are more important than cpu cycles, but frankly that’s just a bumper-sticker slogan and not fair to the people who are complaining about performance. Even though our product, FogBugz, seems like something that should be perfect for Ruby on Rails, we have several parts of code where performance is extremely important. In FogBugz 6 there’s one place where we need to do literally millions of calculations to display a single chart on a single web page. We have gotten it down to 3 seconds or so in our current development environment with a lot of optimization, but frankly with a duck-typed function call I really don’t think we could do it before the web browser gave up and timed out and the sun cooled down a couple of degrees.


Let me get this straight. Let me make sure I’m understanding this. Because I think I’ve gone crosseyed.

1. I don’t see how Wasabi – a language that, per Joel, *compiles down to VBScript on Windows – *could actually be faster than Ruby. VBScript certainly isn’t compiled, and it isn’t exactly known for its blazing speed. Speed improvement is one of the many bullet points used to justify the switch from ASP to ASP.NET.
2. If performance is so critically important in this section of the code, why wouldn’t Joel simply build that section of the code in a compiled language and *call it* from the other language? Am I missing something here? Is there some law that states all code for a web application must be in the same exact language?
3. Justifying any language choice based on one tiny section of the code makes no sense whatsoever. It’s a complete reversal of the well-known 90/10 rule. If we followed Joel’s logic, we should reject all dynamically typed languages. Even in a world filled with 3 gigahertz $200 dual-core CPUs that get cheaper every nanosecond. Because, y’know, there’s this one part here that’s kinda slow.


All of this makes me wonder: **has Joel Spolsky jumped the shark?**


I reject this new, highly illogical Joel Spolsky. I demand the immediate return of the sage, sane, wise Joel Spolsky of years past. But maybe it’s like wishing for a long-running television show to return to its previous glories.

[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[technology trends](https://blog.codinghorror.com/tag/technology-trends/)
[technical practices](https://blog.codinghorror.com/tag/technical-practices/)
