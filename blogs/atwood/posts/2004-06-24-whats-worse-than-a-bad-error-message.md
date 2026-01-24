---
title: "What’s worse than a Bad Error Message?"
date: 2004-06-24
url: https://blog.codinghorror.com/whats-worse-than-a-bad-error-message/
slug: whats-worse-than-a-bad-error-message
word_count: 494
---

I’m sure I don’t have to explain what is wrong with error messages like this:


> [*Catastrophic Failure*](https://web.archive.org/web/20060203124453/https://support.microsoft.com/default.aspx?scid=http%3A%2F%2Fsupport.microsoft.com%3A80%2Fsupport%2Fkb%2Farticles%2FQ243%2F3%2F49.ASP&NoWebContent=1)
> [*General Protection Fault*](https://web.archive.org/web/20040817012746/http://www.duxcw.com/faq/win/bsod.htm)
> [*Error: The operation completed successfully*](https://web.archive.org/web/20040805090306/http://www.it-faq.pl/mskb/276/011.HTM)


Or these classic error messages from 1976:


![A set of classic error messages from 1976, such as "archive disk worn", "back at begining", "may be damaged"](https://blog.codinghorror.com/content/images/2025/12/classic-1976-error-messages.png)


But as bad as those are, they pale in comparison to what is, hands down, the worst kind of error message: a beautiful, well-formatted, informative, **incorrect **error message.


Due to the issue documented in my previous post, we’re currently replacing the database layer of our production application – switching from Microsoft’s **System.Data.OracleClient**, to Oracle’s **Oracle.DataAccess**. Just what you want to do in a production system, make sweeping changes in the back end soon after deployment. Er, right. But I digress.


The initial conversion went better than expected, and ran fine on development machines within a few hours. However, when we deployed our Smart Client app, we encountered the following exception:

kg-card-begin: html

```
(Inner Exception)
Exception Source:      Oracle.DataAccess
Exception Type:        System.DllNotFoundException
Exception Message:     Unable to load DLL (OraOps9.dll).
Exception Target Site: GetRegTraceInfo
---- Stack Trace ----
Oracle.DataAccess.Client.OpsTrace.GetRegTraceInfo(TrcLevel As UInt32&)
CrazyApp.Loader.EXE: N 00000
Oracle.DataAccess.Client.OracleConnection..ctor()
CrazyApp.Loader.EXE: N 00032
SharedUtils.DB.DBDataset..ctor(info As SerializationInfo, context As StreamingContext)
CrazyApp.Loader.EXE: N 00040
(Outer Exception)
Exception Source:      mscorlib
Exception Type:        System.Reflection.TargetInvocationException
Exception Message:     Exception has been thrown by the target of an invocation.
Exception Target Site: HandleReturnMessage
---- Stack Trace ----
System.Runtime.Remoting.Proxies.RealProxy.HandleReturnMessage(reqMsg As IMessage, retMsg As IMessage)
CrazyApp.Loader.EXE: N 00264
System.Runtime.Remoting.Proxies.RealProxy.PrivateInvoke(msgData As MessageData&, type As Int32)
CrazyApp.Loader.EXE: N 00682
CrazyApp.API.UserManager.GetUser(dsUser As DataSet&)
CrazyApp.Loader.EXE: N 00000
CrazyApp.UI.Data.ClientDatasetManager.GetCurrentUserDataset(blnForceRefresh As Boolean)
CrazyApp.Loader.EXE: N 00081
```

kg-card-end: html

Thus began an entire day of hair-pulling exercises in determining why the remoted Oracle call can’t locate OraOps9.dll. It has to be a configuration problem on the server with the Oracle driver. Just like the nicely formatted error message says, with its informative stack traces and exception details. Right?


Wrong. After exhausting every possible scenario – I wish I could say it was skill, but it’s a lot more like dogged trial and error – we determined that, **despite the fact that the exception is wrapped in a remoting call, the required file is missing from the client!**


I discovered this on my own machine. Intellectually, I knew there was no way I could be getting different results from a server call than any other client. The only possible explanation was a new client dependency introduced by referencing types in Oracle.DataAccess. But I *still refused to believe this*. In fact, I did not believe it until I duplicated it, by installing the Oracle 9 client and .NET layer on a clean build machine. Sure enough, the smart client app ran fine as soon as I did that.


I’ve probably spent more time chasing down erroneous error messages than the time I’ve spent on all other error messages combined. Evidently computers, like people, are big fat stinkin’ liars!

[error messages](https://blog.codinghorror.com/tag/error-messages/)
[software development](https://blog.codinghorror.com/tag/software-development/)
[debugging](https://blog.codinghorror.com/tag/debugging/)
[technical practices](https://blog.codinghorror.com/tag/technical-practices/)
