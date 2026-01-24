---
title: "Creating More Exceptional Exceptions"
date: 2004-10-24
url: https://blog.codinghorror.com/creating-more-exceptional-exceptions/
slug: creating-more-exceptional-exceptions
word_count: 628
---

I find myself throwing plain old **System.Exception** far too often. If only I had a complete reference of the many default Exception classes Microsoft provides, like the one [Chris Sully](https://web.archive.org/web/20040707080254/http://www.dotnetjohn.com/articles/articleid42.aspx) provides in his article. That’s good as a starting point, but I don’t see things like **System.Data.DataException** in there. Does anyone know of a more comprehensive list of *Exception classes for all the common .NET namespaces?


While searching for this, I also found some interesting commentary on **System.ApplicationException**. I always wondered what the heck that was for, and a linked Microsoft page confirms my suspicions:


> *Designing exception hierarchies is tricky. Well-designed exception hierarchies are wide, not very deep, and contain only those exceptions for which there is a programmatic scenario for catching. We added ApplicationException thinking it would add value by grouping exceptions declared outside of the .NET Framework, but there is no scenario for catching ApplicationException and it only adds unnecessary depth to the hierarchy. You should not define new exception classes derived from ApplicationException; use Exception instead. In addition, you should not write code that catches ApplicationException.*


Well, so much for that.


There’s also some discussion about the merits of error codes vs. exceptions. Opinions vary, but the determining factor seems to be performance. The first entry in MSDN’s Performance Tips and Tricks in .NET Applications talks about exceptions:


> *Throwing exceptions can be very expensive, so make sure that you don’t throw a lot of them. Use Perfmon to see how many exceptions your application is throwing. It may surprise you to find that certain areas of your application throw more exceptions than you expected. For better granularity, you can also check the exception number programmatically by using Performance Counters.
> Finding and designing away exception-heavy code can result in a decent perf win. **Bear in mind that this has nothing to do with try/catch blocks: you only incur the cost when the actual exception is thrown. You can use as many try/catch blocks as you want.** Using exceptions gratuitously is where you lose performance. For example, you should stay away from things like using exceptions for control flow.*


At some point in the development of your project, I suggest you turn on “Break on all exceptions” using the VS.NET Exceptions menu. This will expose any loops where you are catching thrown exceptions. That’s how I found out we are using a a third party tree control which throws an exception on every row paint!


That’s a big deal, because **throwing an exception is literally slower than making a database call**. This really surprised me, because a DB query is *incredibly* slow. But [it’s true](https://web.archive.org/web/20041024132647/http://www.howzatt.demon.co.uk/articles/12May04.html):


> *Yes, that’s right - the decimal point is in the right place for function #2! **The code path through the exception throwing route took almost 3 orders of magnitude longer than the raw code.** This is why, for this article, I’m just not interested in minor optimizations of the source code since the impact of exceptions dwarfs them.*


This sounds really bad, but in practice, it shouldn’t matter. If you are using exceptions properly, they should rarely be occurring and therefore any performance cost is moot. Eric Gunnerson puts it best:


> *So, if you are not a programming God like those OS developers, you should consider using exceptions for your application errors. They are more powerful, more expressive, and less prone to abuse than error codes. They are one of the fundamental ways that we make managed programming more productive and less error prone. In fact, the CLR internally uses exceptions even in the unmanaged portions of the engine. However, there is a serious long term performance problem with exceptions and this must be factored into your decision.*

[exception handling](https://blog.codinghorror.com/tag/exception-handling/)
[.net](https://blog.codinghorror.com/tag/net/)
[error handling](https://blog.codinghorror.com/tag/error-handling/)
[software development](https://blog.codinghorror.com/tag/software-development/)
[exception classes](https://blog.codinghorror.com/tag/exception-classes/)
