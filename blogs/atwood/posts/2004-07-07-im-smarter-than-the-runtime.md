---
title: "I’m smarter than the Runtime!"
date: 2004-07-07
url: https://blog.codinghorror.com/im-smarter-than-the-runtime/
slug: im-smarter-than-the-runtime
word_count: 272
---

One of the great features of .NET is the [automatic garbage collection](https://web.archive.org/web/20040829040829/http://msdn.microsoft.com/msdnmag/issues/1100/GCI/default.aspx) that absolves the developer of worrying about C++ style memory management, where for every allocate, there must be a destroy, or you’re leaking. And yet, I frequently see overzealous developers write code like this:

kg-card-begin: html

```
Public Function CrazyFunction() As Integer
Dim ds As DataSet = Client.GetDataSet
Dim dr() As DataRow
Select Case _strType
Case "Apple", "Orange"
Return _intID
Case Else
dr = Client.GetParentRow(ds, _intID)
End Select
If Not ds Is Nothing Then ds.Dispose()
Return NVLInteger(dr(0).Item("NODE_ID"))
End Function
```

kg-card-end: html

At best, this is extra, meaningless code that someone has to debug and read.


At worst, coding like this screams “I’m smarter than the Runtime!” E.g., that the developer somehow knows more about the lifetime and scope of variables than the runtime does. Or that they don’t trust the runtime to take care of these mundane scoping disposals. These kinds of developers are, in my experience, dangerous.


The other problem here is the intentional deviation from the default behavior, which is to let the variable fall out of scope naturally. Default behaviors are there to make our lives easier, and to protect us – they should be leveraged whenever possible.


While there are certainly valid reasons to dispose / close, primarily for objects that have associated “real world” resources like files, database connections, and GDI handles – **that is the exception rather than the rule**. Why create extra work for yourself (and the people who will maintain your code) by littering your code with these unnecessary, C++ style Dispose() calls?

[.net](https://blog.codinghorror.com/tag/net/)
[garbage collection](https://blog.codinghorror.com/tag/garbage-collection/)
[memory management](https://blog.codinghorror.com/tag/memory-management/)
[software development](https://blog.codinghorror.com/tag/software-development/)
[debugging](https://blog.codinghorror.com/tag/debugging/)
