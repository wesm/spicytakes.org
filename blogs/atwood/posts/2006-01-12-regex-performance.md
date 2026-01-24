---
title: "Regex Performance"
date: 2006-01-12
url: https://blog.codinghorror.com/regex-performance/
slug: regex-performance
word_count: 819
---

I was intrigued by a recent comment from a Microsoft Hotmail developer on the pitfalls they’ve run into while upgrading Hotmail to .NET 2.0:


> Regular Expressions can be very expensive. Certain (unintended and intended) strings may cause RegExes to exhibit exponential behavior. We’ve taken several hotfixes for this. RegExes are so handy, but devs really need to understand how they work; we’ve gotten bitten by them.


I’m definitely guilty of this. When I throw a regex together, I never worry about performance; I know the target strings will generally be far too small to ever cause a problem. But you may not need a large string to cause a major performance bottleneck – it’s entirely possible to formulate regular expression patterns that consume **exponentially more CPU time for each additional input character**, as noted in [this python mailing list posting](http://mail.python.org/pipermail/python-dev/2003-May/035916.html):


> I’m acutely aware of that one because it burns people regularly. These aren’t cases of hostile input, they’re cases of innocently “erroneous” input. After maybe a year of experience, people using a backtracking regexp engine usually figure out how to write a regexp that doesn’t go resource-crazy when parsing strings that *do* match. Those are the inputs the program expects. But all inputs can suffers errors, and a Regexe that works well when the input matches can still go nuts trying to match a non-matching string, consuming an exponential amount of time trying an exponential number of futile backtracking possibilities.


The example provided in that email is a pattern of

kg-card-begin: html

```
(x+x+)+y
```

kg-card-end: html

Which means, in regex-ese:

- One or more of the character X
- One or more of the character X
- One or more of the previous two matches combined
- Followed by a single character Y


I tried this pattern in [RegexBuddy](http://www.regexbuddy.com)’s debugger first, with a simple 20 character test string:

kg-card-begin: html

```
xxxxxxxxxxxxxxxxxxxx
```

kg-card-end: html

![](https://blog.codinghorror.com/content/images/2025/05/image-156.png)


This is no problem in RegexBuddy, because it has an advanced regular expression engine that throttles regex expressions before they hang your machine. Now let’s try it in .NET and see what happens:

kg-card-begin: html

```
Dim pattern As String = "(x+x+)+y"
Dim sw As New Stopwatch
sw.Start()
Regex.Match("xxxxxxxxxxxxxy", pattern)
sw.Stop()
Console.Write("Valid match took ")
Console.Write(sw.ElapsedMilliseconds)
Console.WriteLine(" ms")
Dim s As String = "xx"
For n As Integer = 1 To 24
sw.Start()
Regex.Match(s, pattern)
sw.Stop()
Console.Write("Invalid match of ")
Console.Write(s.Length)
Console.Write(" chars took ")
Console.Write(sw.ElapsedMilliseconds)
Console.WriteLine(" ms")
s = s + "x"
Next
```

kg-card-end: html

Here’s the output from this console app:

kg-card-begin: html

```
Valid match took 0 ms
Invalid match of 2 chars took 0 ms
Invalid match of 3 chars took 0 ms
Invalid match of 4 chars took 0 ms
Invalid match of 5 chars took 0 ms
Invalid match of 6 chars took 0 ms
Invalid match of 7 chars took 0 ms
Invalid match of 8 chars took 0 ms
Invalid match of 9 chars took 0 ms
Invalid match of 10 chars took 1 ms
Invalid match of 11 chars took 2 ms
Invalid match of 12 chars took 3 ms
Invalid match of 13 chars took 6 ms
Invalid match of 14 chars took 13 ms
Invalid match of 15 chars took 25 ms
Invalid match of 16 chars took 50 ms
Invalid match of 17 chars took 100 ms
Invalid match of 18 chars took 202 ms
Invalid match of 19 chars took 403 ms
Invalid match of 20 chars took 808 ms
Invalid match of 21 chars took 1624 ms
Invalid match of 22 chars took 3257 ms
Invalid match of 23 chars took 6432 ms
Invalid match of 24 chars took 12857 ms
Invalid match of 25 chars took 25657 ms
```

kg-card-end: html

Looks like [n-squared behavior](https://blog.codinghorror.com/everything-is-fast-for-small-n/) to me.


I can see where the Hotmail devs would be freaking out about this, considering matching against only 20 characters eats almost a full second of server CPU time! It’s too bad the .NET regex engine doesn’t implement some kind of throttling or exception behavior when the cost of the regex grows too large.


The author of RegexBuddy calls this **catastrophic backtracking**, and he has a page describing [how to avoid catastrophic backtracking](http://www.regular-expressions.info/catastrophic.html) in your regular expressions:


> The solution is simple. When nesting repetition operators, **make absolutely sure that there is only one way to match the same match**. If repeating the inner loop 4 times and the outer loop 7 times results in the same overall match as repeating the inner loop 6 times and the outer loop 2 times, you can be sure that the regex engine will try all those combinations.


The essential part of the customer example he gives is converting a dot (any character) match to a [^,rn] (not comma, not carriage return, not newline) match. In other words – be as specific as possible!

[regex](https://blog.codinghorror.com/tag/regex/)
[performance](https://blog.codinghorror.com/tag/performance/)
[software development](https://blog.codinghorror.com/tag/software-development/)
[programming concepts](https://blog.codinghorror.com/tag/programming-concepts/)
[security](https://blog.codinghorror.com/tag/security/)
