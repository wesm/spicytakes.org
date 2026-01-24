---
title: "Micro-Optimization and Meatballs"
date: 2005-01-15
url: https://blog.codinghorror.com/micro-optimization-and-meatballs/
slug: micro-optimization-and-meatballs
word_count: 402
---

In my previous entry on [the real cost of performance](https://blog.codinghorror.com/the-real-cost-of-performance/), there were some complaints that [my code’s slow and it sucks](https://web.archive.org/web/20060104170203/http://robgarrett.com/Blogs/software/archive/2005/01/12/443.aspx#FeedBack). If I had a nickel every time someone told me that, I could have retired years ago. Let’s take a look at the specific complaint that **the s <> “” comparison is inefficient**, using low-level windows API timing in the Stopwatch class:

kg-card-begin: html

```
Const iterations As Integer = 1000000
Dim s As String = "sample string"
Dim sw As New Stopwatch
Dim n As Integer
n = 0
sw.Start()
For i As Integer = 1 To iterations
If s.Length = 0 Then
n += 1
End If
Next
sw.Stop()
Console.WriteLine(sw.ElapsedMs)
n = 0
sw.Start()
For i As Integer = 1 To iterations
If s = String.Empty Then
n += 1
End If
Next
sw.Stop()
Console.WriteLine(sw.ElapsedMs)
n = 0
sw.Start()
For i As Integer = 1 To iterations
If s = "" Then
n += 1
End If
Next
sw.Stop()
Console.WriteLine(sw.ElapsedMs)
n = 0
sw.Start()
For i As Integer = 1 To iterations
If s.Equals(String.Empty) Then
n += 1
End If
Next
sw.Stop()
Console.WriteLine(sw.ElapsedMs)
```

kg-card-end: html

Here are the results:

kg-card-begin: html


|  | Athlon FX-53
2.4 GHz | Pentium-M
1.2 GHz |
| `s.Length = 0` | 2.6 ms | 10 ms |
| `s = String.Empty` | 20 ms | 46 ms |
| `s =""` | 20 ms | 43 ms |
| `s.Equals(String.Empty)` | 13 ms | 26 ms |


kg-card-end: html

So, yes, String.Length is five (or more) times faster. And yes, using String.Equals is twice as fast. However, neither of those will work when the string is Nothing, and **we’re still talking about a difference of 30 milliseconds, on the slowest computer I own, over a MILLION string comparisons!** This brings to mind a Bill Murray quote from [Meatballs](http://www.imdb.com/title/tt0079540/): *It just doesn’t matter! It just doesn’t matter!*


![](https://blog.codinghorror.com/content/images/2025/05/image-42.png)


Arguments about which method results in code that is easier to read and easier to maintain will be gladly entertained. Arguments about speed will not. Stop micro-optimizing and start macro-optimizing: per Lippert, **code that makes sense is code which can be analyzed and maintained, and that makes it performant.**


If you’d like to time this yourself, here’s a [stopwatch class](https://blog.codinghorror.com/a-stopwatch-class-for-net-11/) which uses the high resolution API counters. Good luck – you’re gonna need it. The resolution, I mean.

[performance](https://blog.codinghorror.com/tag/performance/)
[optimization](https://blog.codinghorror.com/tag/optimization/)
[software development](https://blog.codinghorror.com/tag/software-development/)
[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[.net](https://blog.codinghorror.com/tag/net/)
