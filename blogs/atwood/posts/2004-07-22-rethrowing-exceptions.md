---
title: "Rethrowing Exceptions"
date: 2004-07-22
url: https://blog.codinghorror.com/rethrowing-exceptions/
slug: rethrowing-exceptions
word_count: 470
---

There’s a bit more subtlety to rethrowing exceptions than most developers realize. Although this topic is covered very nicely at [The .NET Guy blog](https://web.archive.org/web/20040810135248/http://dotnetguy.techieswithcats.com/archives/004118.shtml), here’s another example:

kg-card-begin: html

```
Try
session = smgr.getSession(_strDocbaseName)
Catch ex As Exception
If ex.Message.IndexOf("authentication failed") > 0 Then
Throw New Exception("more info about the exception", ex)
Else
Throw
End If
End Try

```

kg-card-end: html

The important thing here is to preserve the call stack, and that means:

1. When throwing your more-informative exception, include the original exception as the InnerException (second parameter) for reference.
2. When you decide you can’t handle the exception, re-throw the original exception as is.


Even the documentation for Throw does not document the fact that **you can call Throw without any params to re-throw the current exception**. Not a big deal, since...

kg-card-begin: html

```
Throw ex
```

kg-card-end: html

...would do the same thing, but less code is almost always better, IMO.


So then the next natural question that most developers ask is, “When should I catch exceptions?” And it’s a very good question. Here are some guidelines that I have found useful.

1. **Unless you have a very good reason to catch an exception, DON’T. **Exceptions are supposed to be exceptional, just like the dictionary meaning: *uncommon*, *unusual*. When in doubt, let the calling routine, or the global exception handler, deal with it. This is the golden rule. The hardest kinds of exceptions to troubleshoot are the ones that don’t even exist, because a developer upstream of you decided to consume it.
2. **If you can correct the problem implied by the exception.** For example, if you try to write to a file and it is read-only, try removing the read-only flag from the file. In this case you handled the exception and fixed the problem, so you should eat the exception. It doesn’t exist, because you fixed it.
3. **If you can provide additional information about the exception.** For example, if you fail to connect via HTTP to a remote website, you can provide details about *why* the connection failed: was the DNS invalid? Did it time out? Was the connection closed? Did the site return 401 unauthorized, which implies that credentials are needed? In this case you want to catch the exception, and re-throw it as an inner exception with more information. This is a very good reason to catch an exception, but note that we are still re-throwing it!
4. **Always try to catch specific exceptions.** Avoid catching `System.Exception` whenever possible; try to catch just the specific errors that are specific to that block of code. Catch `System.IO.FileNotFound` instead.


There are, of course, times when you’ll want to violate these rules for completely legitimate reasons – but at least consider them before you do.

[exception handling](https://blog.codinghorror.com/tag/exception-handling/)
[rethrowing exceptions](https://blog.codinghorror.com/tag/rethrowing-exceptions/)
[call stack](https://blog.codinghorror.com/tag/call-stack/)
[.net](https://blog.codinghorror.com/tag/net/)
[software development](https://blog.codinghorror.com/tag/software-development/)
