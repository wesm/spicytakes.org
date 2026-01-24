---
title: "Improved Unhandled Exception behavior in .NET 2.0"
date: 2005-02-18
url: https://blog.codinghorror.com/improved-unhandled-exception-behavior-in-net-20/
slug: improved-unhandled-exception-behavior-in-net-20
word_count: 564
---

I recently posted a question about [console apps and AppDomain.CurrentDomain.UnhandledException](https://blog.codinghorror.com/console-apps-and-appdomain-currentdomain-unhandledexception/) – specifically, why doesn’t it work as described in the MSDN documentation?


I even filed an [official bug report](https://web.archive.org/web/20050220115744/http://lab.msdn.microsoft.com/ProductFeedback/viewFeedback.aspx?feedbackId=FDBK21092) on this. I guess it worked, because Microsoft’s Jonathan Keljo was kind enough to explain this behavior in the comments:


> *Sorry for the confusion. This behavior is actually the design, though the design can be a little convoluted at times.
> The first thing to understand is that the UnhandledException event is not an unhandled exception “handler.” Registering for the event, contrary to what the documentation says :-(, does not cause unhandled exceptions to be handled. (Since then they wouldn’t be unhandled, but I’ll stop with the circular reasoning already... ) The UnhandledException event simply notifies you that an exception has gone unhandled, in case you want to try to save state before your thread or application dies. FWIW, I have filed a bug to get the docs fixed.
> Just to complicate things, in v1.0 and 1.1, an unhandled exception did not always mean that your application would die. If the unhandled exception occurred on anything other than the main thread or a thread that began its life in unmanaged code, the CLR ate the exception and allowed your app to keep going. This was generally evil, because what would often happen was, for example, that ThreadPool threads would silently die off, one by one, until your application wasn’t actually doing any work. Figuring out the cause of this kind of failure was nearly impossible. This may be why Jeff thought it worked before...he just always saw crashes on non-main threads.
> **In v2.0, an unhandled exception on any thread will take down the application. We’ve found that it’s tremendously easier to debug crashes than it is to debug hangs or the silent-stoppage-of-work problem described above.**
> BTW, on my 1.1 machine the example from MSDN does have the expected output; it’s just that the second line doesn’t show up until after you’ve attached a debugger (or not). In v2 we’ve flipped things around so that the UnhandledException event fires before the debugger attaches, which seems to be what most people expect.
> Jonathan Keljo
> CLR Exceptions PM*


It’s good to hear that unhandled exception behavior will be more coherent in .NET 2.0. I can’t think of any reason I would want the debugger to attach (or, if no debugger is registered, the .NET crash dialog to appear) before our global unhandled exception event fires!


I knew that exceptions were only handled on the main thread in .NET 1.1; you have to add the handler to any new managed thread you spawn. However, I’ve also seen the behavior Jonathan describes here:


> *if the unhandled exception [ occurs in ] a thread that began its life in unmanaged code, **the CLR eats the exception and allows your app to keep going***


I remember spending an entire day working on winforms drag and drop problems that were a side effect of this unwanted exception behavior – in retrospect, I guess it’s because drag and drop occurs on an unmanaged COM thread. Anyway, through a painful process of elimination, we finally decided that our code was encountering some kind of error and silently returning from functions. I’m looking forward to *not* going through that in .NET 2.0!

[.net](https://blog.codinghorror.com/tag/net/)
[exception handling](https://blog.codinghorror.com/tag/exception-handling/)
[appdomain](https://blog.codinghorror.com/tag/appdomain/)
[unhandledexception](https://blog.codinghorror.com/tag/unhandledexception/)
[bug report](https://blog.codinghorror.com/tag/bug-report/)
