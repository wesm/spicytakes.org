---
title: "The One Trillion Dollar Development Pyramid"
date: 2005-02-28
url: https://blog.codinghorror.com/the-one-trillion-dollar-development-pyramid/
slug: the-one-trillion-dollar-development-pyramid
word_count: 922
---

Kit George is the program manager for the [.NET Base Class Library team](https://web.archive.org/web/20051016033235/http://msdn.microsoft.com/netframework/programming/bcl/BCLTeam.aspx). Kit recently posted an entry on the BCL blog describing a [solution to a customer problem](https://web.archive.org/web/20060502142357/http://blogs.msdn.com/bclteam/archive/2005/02/21/377575.aspx):


> *We recently got asked this question by a customer: “In C#, how do I ensure that a string entered into a text box is of the format: letter,number,letter,number,letter,number?”
> The first answer seems to be pretty straightforward: use RegEx! Regular Expressions are a pretty powerful mechanism for matching strings, and seem the obvious choice. However, you’ve always got to remember that RegEx, while powerful, is also a pretty hefty mechanism for String matching. When you’re looking for complex strings it’s often a good choice (since writing the code yourself can be unbelievably tricky), but when what you’re looking for is pretty simple (as in this case), then doing your own matching shouldn’t be too tough, and is going to perform a lot more solidly.*


Kit goes on to illustrate that, indeed, writing a simple per-character string check is faster than a regular expression. There are some caveats with his example, but ultimately it works out to be at least 3 times faster. And performance is incredibly important... **when you’re writing base class libraries designed to be used by millions of developers.** Therein lies the problem.


The techniques that make sense for the relative handful of developers writing the .NET framework rarely make sense for the vast legions of developers who are building on top of the framework. The guys at the top of the kernel-OS-framework pyramid don’t have much in common with the lower (and order-of-magnitude larger!) levels of the coding pyramid. I occasionally run into developers who point to the Linux source code as a model for development, and my question to them is always the same: **since when are we writing an operating system?** Everyone likes to think that they’re working on [something fantastically complicated](https://blog.codinghorror.com/were-building-the-space-shuttle/) that will be used by millions of developers, but reality is... somewhat less exciting.


![](https://blog.codinghorror.com/content/images/2025/05/image-55.png)


We’re all participants, willing or not, in **the One Trillion Dollar Development Pyramid**.

1. **Dozens**. The developers working on your kernel should be [Dave Cutler-esque geniuses](https://blog.codinghorror.com/showstopper/). There aren’t many guys playing the game at this level. Copying UNIX over and over is laudable enough, but developing an entire OS architecture from scratch is the ultimate in hardcore development.
2. **Hundreds**. Those kernel developers support several hundred OS developers, who should be the best of the best, your [Raymond Chens](https://web.archive.org/web/20050228223007/http://weblogs.asp.net/oldnewthing/), if you will. They create the OS infrastructure that makes everything else possible.
3. **Thousands**. Those OS developers support a thousand framework developers. Highly talented, handpicked developers building abstract APIs that enable huge productivity gains.
4. **Millions.** The framework supports millions of developers of wildly disparate skill levels: everything from rank beginner to near-genius. And they’re pounding out trillions of lines of code on every imaginable kind of application.


The development techniques used on each level of the pyramid may not have a whole lot in common. Can you imagine IIS 7.0 written in managed C#? The [personalities and skills](https://blog.codinghorror.com/commandos-infantry-and-police/) required at each level are quite different as well. Can you imagine working on GenericBusinessApp 3.7 with Dave Cutler? “I’ve got [chunks of guys like you](http://snltranscripts.jt.org/90/90ksinatra.phtml) in my stool!”


The real risk here is **delusions of grandeur**: thinking that you’re working at a higher level of the pyramid than you actually are, and choosing techniques that don’t make sense for your project. Jon Galloway has an [insightful rebuttal](https://web.archive.org/web/20060623174853/http://weblogs.asp.net/jgalloway/archive/2005/02/16/374212.aspx) of Joel Spolsky’s recommendation that every college graduate [learn low-level C programming](http://www.joelonsoftware.com/items/2005/01/02.html) which illustrates this conceit:


> *Modern programming languages run on top of frameworks. .NET apps use the .NET framework, Java uses J2EE (et. al.), and arguably web apps run on top of a browser / communication communication that constitutes an application framework. The list could go on (GTK, XUL, web service, Flash). Most good frameworks are standards based, and all of them host your solutions so you only solve new problems.
> C code, by and large, is not about frameworks. At its best, it uses some libraries and links to some API’s. C gives you a toolset that can solve just about any problem, but requires that you solve each and every problem every time. Frameworks were created to obviate solving the same problems in each program you write. Software development has made a steady progression from code to libraries to components to frameworks. Thankfully, you don’t need to retrace this path just as you don’t need to experience the dark ages to live in the post-renaissance world.
> To be productive as a programmer these days, you either need to be learning to get the most out of existing frameworks or helping to build tomorrow’s frameworks. To learn to be a productive programmer, you need to learn how to work with frameworks.*


Kit George has the privilege of working on a team producing code that will be used by millions of developers. It’s his job to make the base classes as performant as possible, even at the cost of readability. We’re writing GenericBusinessApp 3.7, which will have a few hundred users at most. Users who are far more concerned with leaving at 5pm every day than they are with the incomparable thrill of using yet another version of GenericBusinessApp.


A Regex that uses one line of code to validate “letter,number,letter,number,letter,number” may not be faster in processor time, but it’s certainly faster in development time – and for us, that wins every time.

[.net](https://blog.codinghorror.com/tag/net/)
[c#](https://blog.codinghorror.com/tag/c-2/)
[regular expressions](https://blog.codinghorror.com/tag/regular-expressions/)
[software development](https://blog.codinghorror.com/tag/software-development/)
[programming](https://blog.codinghorror.com/tag/programming/)
