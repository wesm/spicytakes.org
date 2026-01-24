---
title: "For Best Results, Don’t Initialize Variables"
date: 2005-07-18
url: https://blog.codinghorror.com/for-best-results-dont-initialize-variables/
slug: for-best-results-dont-initialize-variables
word_count: 428
---

I noticed on a few projects I’m currently working on that the developers are maniacal about initializing variables. That is, either they initialize them when they’re declared:

kg-card-begin: html

```

private string s = null;
private int n = 0;
private DataSet ds = null;

```

kg-card-end: html

Or they initialize them in the constructor:

kg-card-begin: html

```

class MyClass
{
private string s;
private int n;
private DataSet ds;
public MyClass()
{
s = null;
n = 0;
ds = null;
}
}

```

kg-card-end: html

Well, this all struck me as unnecessary work in the .NET world. Sure, maybe that’s the convention in the wild and wooly world of buffer overrunsC++, but this is **managed code**. Do we really want to play the [I’m smarter than the runtime](https://blog.codinghorror.com/im-smarter-than-the-runtime/) game again?


Ok, so maybe you’re a masochist and you like extra typing. What about the performance argument? According to this [well-researched CodeProject article](https://web.archive.org/web/20050727083228/http://www.codeproject.com/dotnet/DontInitializeVariables.asp), initializing variables actually hurts performance. The author provides some benchmark test code along with his results:

kg-card-begin: html


| Creating an object and initializing on definition | 11% slower |
| Creating an object and initializing in the constructor | 16% slower |
| Calling a method and initializing variables | 25% slower |


kg-card-end: html

That’s on the author’s Pentium-M 1.6ghz. I tested the same code (optimizations enabled, release mode) on my Athlon 64 2.1ghz and a Prescott P4 2.8ghz:

kg-card-begin: html


|  | Athlon 64 | P4 |
| Creating an object and initializing on definition | 30% slower | 35% slower |
| Creating an object and initializing in the constructor | 30% slower | 36% slower |
| Calling a method and initializing variables | 14% slower | 8% slower |


kg-card-end: html

I recompiled under VS.NET 2005 beta 2 using the Athlon 64 to see how .NET 2.0 handles this:

kg-card-begin: html


| Creating an object and initializing on definition | 0% slower |
| Creating an object and initializing in the constructor | 20 % slower |
| Calling a method and initializing variables | 20% slower |


kg-card-end: html

Clearly there’s a substantial performance penalty for initializing variables in both .NET 1.1 and even .NET 2.0 (although the newer compiler appears to optimize away initialization on definition). I recommend **avoiding initialization as a general rule**, unless you have a compelling reason to do so. If you’re only initializing variables to avoid the uninitialized variable compiler warning, check out the [new #pragma warning feature](https://web.archive.org/web/20060101064529/http://blogs.msdn.com/gusperez/articles/85722.aspx) to programmatically disable specific warnings in .NET 2.0.

[performance](https://blog.codinghorror.com/tag/performance/)
[initialization](https://blog.codinghorror.com/tag/initialization/)
[variables](https://blog.codinghorror.com/tag/variables/)
[.net](https://blog.codinghorror.com/tag/net/)
[coding practices](https://blog.codinghorror.com/tag/coding-practices/)
