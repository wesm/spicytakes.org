---
title: "The Tyranny of ElseIf"
date: 2004-06-20
url: https://blog.codinghorror.com/the-tyranny-of-elseif/
slug: the-tyranny-of-elseif
word_count: 275
---

I don’t understand it. I’ve seen this phenomenon over and over in VB.NET, in code from experienced programmers:

kg-card-begin: html

```
If dt.DayOfWeek = DayOfWeek.Sunday Then
Return dt
ElseIf dt.DayOfWeek = DayOfWeek.Monday Then
Return dt.AddDays(6)
ElseIf dt.DayOfWeek = DayOfWeek.Tuesday Then
Return dt.AddDays(5)
ElseIf dt.DayOfWeek = DayOfWeek.Wednesday Then
Return dt.AddDays(4)
ElseIf dt.DayOfWeek = DayOfWeek.Thursday Then
Return dt.AddDays(3)
ElseIf dt.DayOfWeek = DayOfWeek.Friday Then
Return dt.AddDays(2)
ElseIf dt.DayOfWeek = DayOfWeek.Saturday Then
Return dt.AddDays(1)
End If
```

kg-card-end: html

Why in the world would you express logic this way, instead of the much simpler SELECT CASE statement?

kg-card-begin: html

```
Select Case dt.DayOfWeek
Case DayOfWeek.Sunday
Return dt
Case DayOfWeek.Monday
Return dt.AddDays(6)
Case DayOfWeek.Tuesday
Return dt.AddDays(5)
Case DayOfWeek.Wednesday
Return dt.AddDays(4)
Case DayOfWeek.Thursday
Return dt.AddDays(3)
Case DayOfWeek.Friday
Return dt.AddDays(2)
Case DayOfWeek.Saturday
Return dt.AddDays(1)
End Select
```

kg-card-end: html

I mention this because I see it constantly from many different programmers. What gives?


I think the ELSEIF keyword is destructive and, like GOTO, has no good use outside of a very specialized niche. ELSEIF, in my experience, is abused far more than it is used properly. Here’s another example from a project I work on:

kg-card-begin: html

```
If result = DialogResult.Retry Then
strProjectName = .ProjDetailsPnl.PnlGenInfo.TxtProjectName.Text
ElseIf result = DialogResult.OK Then
intNewProjectID = .ProjectID
End If
```

kg-card-end: html

I have a very hard time coming up with any valid justification for the use of ELSEIF. 98 times out of 100, SELECT CASE is easier to read and offers the CASE ELSE condition, which encourages developers to handle unknown conditions properly. In the above example, what happens when the dialog returns DialogResult.Cancel?

[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[clean code practices](https://blog.codinghorror.com/tag/clean-code-practices/)
[code refactoring](https://blog.codinghorror.com/tag/code-refactoring/)
