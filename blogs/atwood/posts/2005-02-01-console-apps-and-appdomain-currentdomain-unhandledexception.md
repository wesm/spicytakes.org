---
title: "Console apps and AppDomain.CurrentDomain.UnhandledException"
date: 2005-02-01
url: https://blog.codinghorror.com/console-apps-and-appdomain-currentdomain-unhandledexception/
slug: console-apps-and-appdomain-currentdomain-unhandledexception
word_count: 358
---

This one has me stumped. I’d swear this behaved differently prior to .NET 1.1 service pack 1 (and/or XP SP2), but I can’t prove it. As reported by a CodeProject reader, **you’ll get the standard .NET crash dialog in a console app, even if you’ve registered an unhandled exception handler for your AppDomain**. What gives? Why doesn’t AppDomain.CurrentDomain.UnhandledException capture exceptions on the main thread of a .NET console application?


But don’t take my word for it – try it yourself. Use [this sample](https://web.archive.org/web/20061008124659/http://www.developer.com/net/cplus/article.php/10919_2108931_1) ([source code zip file](https://web.archive.org/web/20061006184515/http://www.developer.com/img/articles/2003/03/12/NET/DeadDotNet.zip)) from John Robbins, co-founder of Wintellect. Or, paste the code from this MSDN article into a new console app and run it:

kg-card-begin: html

```
Sub Main()
Dim cd As AppDomain = AppDomain.CurrentDomain
AddHandler cd.UnhandledException, AddressOf MyHandler
Try
Throw New Exception("1")
Catch e As Exception
Console.WriteLine("Catch clause caught : " + e.Message)
End Try
Throw New Exception("2")
' Expected output:
'   Catch clause caught : 1
'   MyHandler caught : 2
End Sub
Sub MyHandler(sender As Object, args As UnhandledExceptionEventArgs)
Dim e As Exception = DirectCast(args.ExceptionObject, Exception)
Console.WriteLine("MyHandler caught : " + e.Message)
End Sub
```

kg-card-end: html

At first I was concerned that installing VS.NET had somehow forced me into some kind of bizarre first-chance exception mode exclusive to console applications, but not so. **The compiled .exe behaves in the same way on every machine I tried it on**: I get the standard .NET crash dialog, then *after* I dismiss that, I get the unhandled exception handler I wanted in the first place. That’s... not exactly the order I had in mind.


There’s a way to disable the [.NET JIT debugging dialog](http://www.hanselman.com/blog/PermaLink,guid,d5ce2207-514d-4370-8650-9fe81478b54f.aspx), as described by Scott Hanselman. But that’s an extreme “solution” – it disables the crash dialog for all .NET apps. It’s also treating the symptoms rather than the disease: **why can’t we catch unhandled exceptions in console apps any more?** I’d swear this worked the last time I looked at it. And the MSDN sample code certainly implies that it’s possible – but good luck getting that sample to print the expected output.


So what am I missing here?

[.net framework](https://blog.codinghorror.com/tag/net-framework/)
[console applications](https://blog.codinghorror.com/tag/console-applications/)
[appdomain](https://blog.codinghorror.com/tag/appdomain/)
[unhandled exception](https://blog.codinghorror.com/tag/unhandled-exception/)
[exception handling](https://blog.codinghorror.com/tag/exception-handling/)
