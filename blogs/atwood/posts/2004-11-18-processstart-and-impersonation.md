---
title: "Process.Start and Impersonation"
date: 2004-11-18
url: https://blog.codinghorror.com/processstart-and-impersonation/
slug: processstart-and-impersonation
word_count: 544
---

Did you know that **Process.Start always uses the security context of the parent ASP.NET process?** I just found this out the hard way; Using Process.Start on “whoami.exe” always returns the ASPNET worker process no matter what I do. Some searching turned up this [entry in Scott’s blog](http://odetocode.com/Blogs/scott/archive/2004/10/28/602.aspx):


> *I wanted to run these processes with the identity of the client, but this poses a problem. The Process class in System.Diagnostics can start a new process, but the process always inherits the security context of the parent process. Even if the ASP.NET thread invoking the Start method is impersonating a client, the Process still starts with the ASP.NET worker process credentials.
> Enter .NET 2.0, which includes the User, Domain, and Password properties on the ProcessStartInfo type. In .NET 2.0 you can start a process under a different set of credentials.*


Way to rub salt in my wounds, Whidbey. This is a very unfortunate limitation of .NET 1.1, as it severely limits what I can do with Process.Start in a web app. Scott helpfully provides a bit of sample C# code that calls the Win32 APIs to simulate a stripped down version of the Whidbey behavior today.


If you *aren’t* calling Process.Start, you may be able to impersonate to get the behavior you want. The MSKB article, [How to implement impersonation in an ASP.NET application](https://web.archive.org/web/20041205004554/http://support.microsoft.com/?id=306158), provides some nice, relatively painless workarounds:

kg-card-begin: html

> *If you want to impersonate a user on a thread in ASP.NET, you can use one of the following methods, based on your requirements:*
>  [Impersonate the IIS authenticated account or user](https://web.archive.org/web/20041205004554/http://support.microsoft.com/?id=306158#1)
>  [Impersonate a specific user for all the requests of an ASP.NET application](https://web.archive.org/web/20041205004554/http://support.microsoft.com/?id=306158#2)
>  [Impersonate the authenticating user in code](https://web.archive.org/web/20041205004554/http://support.microsoft.com/?id=306158#3)
>  [Impersonate a specific user in code](https://web.archive.org/web/20041205004554/http://support.microsoft.com/?id=306158#4)
> Note: You can use the following code to determine what user the thread is executing as:
> `System.Security.Principal.WindowsIdentity.GetCurrent().Name `

kg-card-end: html

The last method is the most interesting to me – it lets you impersonate an arbitrary user on the fly, execute a specific set of code as that user, then revert back to the ASP.NET credentials. Bear in mind that **impersonation is a very expensive operation; it’s not something you want to do often**.


Scott’s code assumes we want to impersonate the current user and that we don’t have the password. I want to Process.Start as an arbitrary function account using plaintext account and password information. That requires a more masochistic workaround – calling the newer Win32 API method **CreateProcessWithLogonW()** directly. The only good sample code I could find was for VB6: [How To Start a Process as Another User from Visual Basic](https://web.archive.org/web/20050223051605/http://support.microsoft.com/default.aspx?scid=kb%3Ben-us%3B285879). However, I couldn’t get this to work in VB.NET.


Even if I could get that API call to work, I still wouldn’t have the amenities of the Process class that I need. I want to redirect the standard output and standard error output, then capture them into strings, so I can echo the result of my command line operation to the web page.


There’s a good example of [command line capture behavior](https://web.archive.org/web/20041206183128/http://www.codeproject.com/csharp/LaunchProcess.asp) on CodeProject. That’s for WinForms, but the process is similar for ASP.NET. Well, except for that pesky Process.Start credentials problem... another reason to look forward to .NET 2.0, I guess.

[.net](https://blog.codinghorror.com/tag/net/)
[c#](https://blog.codinghorror.com/tag/c-2/)
[asp.net](https://blog.codinghorror.com/tag/asp-net/)
[process.start](https://blog.codinghorror.com/tag/process-start/)
[impersonation](https://blog.codinghorror.com/tag/impersonation/)
