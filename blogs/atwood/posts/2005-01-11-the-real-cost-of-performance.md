---
title: "The real cost of performance"
date: 2005-01-11
url: https://blog.codinghorror.com/the-real-cost-of-performance/
slug: the-real-cost-of-performance
word_count: 722
---

I don’t usually get territorial about modifications to “my” code. First of all, it’s *our* code. And if you want to change something, be my guest; that’s why God invented source control. But, for the love of all that’s holy, **don’t take working code and break it in the name of highly questionable “performance” gains**. I was forced to have a sit-down discussion yesterday with another programmer about some of my NameValueCode code he, uh, *refactored:*

kg-card-begin: html

```
If Value <> "" Then
If nvc.Item(name) = "" Then
nvc.Add(name, Value)
End If
End If
```

kg-card-end: html

Isn’t it absolutely fabulous? This is the kind of master coding wizardry that Donald Knuth can only dream about, friends. But it’s not good enough for some programmers, who just can’t help themselves:

kg-card-begin: html

```
If Value <> String.Empty Then
If nvc.Item(name).Equals(String.Empty) Then
nvc.Add(name, Value)
End If
End If
```

kg-card-end: html

Do you see the bug?* Imagine my surprise when I got an exception in a previously working section of very straightforward code. I approached the developer and quizzed him about this change. Here’s what I got:

1. *Calling the .Equals method performs better than straight equality*


I researched this, and [he’s right](https://web.archive.org/web/20060130214700/http://dotnetjunkies.com/WebLog/chris.taylor/archive/2004/05/18/13927.aspx):


> *When the C# compiler encounters a == operator on strings it generates a call to the op_Equality method of the string class. When the VB.NET compiler encounters the seemingly corresponding = operator it rather generates a call to **Microsoft.VisualBasic.CompilerServices.StringType.StrCmp**, this is to maintain a functional compatibility with VB6 code.*


However, the performance gain is marginal at best. And if we wanted the most performant string comparison, oddly enough, it *wouldn’t* be StringVariable.Equals – it would be the shared/static String.Equals method:


> *I want to point out that the results contained in here are relative and would hardly alter the overall performance of your application except is some very rare and extreme cases... I would definitely bear these results in mind when performing an operation which has high volumes and is string comparison intensive in which case I would consider using the String.Equals as an alternative.*

1. *We can convert between C# and VB.NET more easily if we use .Equals*


Since when did converting our code between .NET languages become a decision point in writing our code? That’s news to me. And I never see C# coders using the .Equals operator for trivial equality tests anyway. They probably think it’s even dumber than I do.

1. *It’s more object oriented this way*


And that’s adequate justification for throwing out one of the most basic operators in any language with a harder-to-read and more obscure variant?


I do try to be tolerant of other people’s crazy practices. I really do. But this is insane. **Can you imagine reading code littered with tons of .Equals calls instead of the simple, straightforward = operator?** I tried my best to gently convince this guy that perhaps, just perhaps, the readability of using simple s = “string” tests might outweigh any of the incredible speed benefits he’s adding to our database driven ASP.NET web application. When it isn’t... querying the database.


I’ve linked to this [Eric Lippert post](https://web.archive.org/web/20051222102846/http://blogs.msdn.com/ericlippert/archive/2003/10/17/53237.aspx) before, but it’s so apropos that it deserves a second link:


> *Write the code to be extremely straightforward. **Code that makes sense is code which can be analyzed and maintained, and that makes it performant.** Consider our “unused Dim” example – the fact that an unused Dim has a 50 ns cost is irrelevant. It’s an unused variable. It’s worthless code. It’s a distraction to maintenance programmers. That’s the real performance cost.*


Always, *always* write for simplicity and readability first. That should be your main goal when writing code: to express yourself as simply and clearly as you possibly can. If you must optimize, use real optimizations based on actual metrics in a functional application. Not hypothetical theory based on some article you read on some website.


*Nothing = “” evaluates to True. If the item isn’t found in the NameValueCollection, the object will be Nothing. Good luck calling the .Equals method on Nothing. I have no real opinion on the merits of String.Empty versus “” other than noting that “” is shorter and can be used as an assignment in constant and optional declarations.

[code refactoring](https://blog.codinghorror.com/tag/code-refactoring/)
[performance optimization](https://blog.codinghorror.com/tag/performance-optimization/)
[programming best practices](https://blog.codinghorror.com/tag/programming-best-practices/)
[debugging](https://blog.codinghorror.com/tag/debugging/)
[software quality](https://blog.codinghorror.com/tag/software-quality/)
