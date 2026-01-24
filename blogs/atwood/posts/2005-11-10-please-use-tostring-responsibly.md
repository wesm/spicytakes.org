---
title: "Please use .ToString() responsibly"
date: 2005-11-10
url: https://blog.codinghorror.com/please-use-tostring-responsibly/
slug: please-use-tostring-responsibly
word_count: 288
---

I’ve seen this kind of code a lot recently:

kg-card-begin: html

```

try
{
int i = 0;
int x = 0;
Console.WriteLine(i / x);
}
catch (Exception ex)
{
Console.WriteLine(ex.Message);
}
```

kg-card-end: html

This results in the following output:

kg-card-begin: html

```

Attempted to divide by zero.

```

kg-card-end: html

Unless there’s some compelling reason you need an ultra-terse version of the error, **it’s almost always better to use the provided Exception.ToString() method.** Compare the difference:

kg-card-begin: html

```

System.DivideByZeroException: Attempted to divide by zero.
at ConsoleApplication1.Program.Main(String[] args)
in C:Program.cs:line 15

```

kg-card-end: html

This also brings up an interesting corollary: **any object you build should have a meaningful .ToString() method.** I expect a proper string representation of *what you are*, not a meaningless echo of your class name!


One object that violates this horribly is DataSet. Let’s say we have a DataSet containing a single DataTable. When you type DataSet.ToString(), what do you think should happen? Wait, wait, don’t tell me. I’ll tell you. This happens:

kg-card-begin: html

```

System.Data.DataSet

```

kg-card-end: html

Useless. How about something that actually shows the object in string form?

kg-card-begin: html

```

+----------------------------------------------------------------+
| DataSet1                                                       |
+----------------------------------------------------------------+
| Table1                                                         |
+---------+-----------+------------------+------------+----------+
| field01 | field02   | field03          | field04    | field05  |
+---------+-----------+------------------+------------+----------+
|       1 | first     | NULL             | NULL       | NULL     |
|       2 | second    | another          | 1999-10-23 | 10:30:00 |
|       3 | a third   | more foo for you | 1999-10-24 | 10:30:01 |
+---------+-----------+------------------+------------+----------+

```

kg-card-end: html

Seems perfectly logical to me, but you’ll have to write your own custom ToString() implementation to get the behavior that should have been there in the first place.

[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[exception handling](https://blog.codinghorror.com/tag/exception-handling/)
[.tostring()](https://blog.codinghorror.com/tag/tostring/)
[c#](https://blog.codinghorror.com/tag/c-2/)
[debugging](https://blog.codinghorror.com/tag/debugging/)
