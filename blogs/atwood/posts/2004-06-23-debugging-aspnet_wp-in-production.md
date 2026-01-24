---
title: "Debugging ASPNET_WP in Production"
date: 2004-06-23
url: https://blog.codinghorror.com/debugging-aspnet_wp-in-production/
slug: debugging-aspnet_wp-in-production
word_count: 1075
---

One of our production web servers keeps deadlocking the ASPNET_WP process, like so:


> aspnet_wp.exe (PID: 3588) was recycled because it was suspected to be in a deadlocked state. It did not send any responses for pending requests in the last 180 seconds.


This is painful. It means the server becomes unavailable for over three minutes, and any pending requests return errors after ASPNET_WP is cycled. The best part is, this happens completely randomly. We can’t force it to happen or duplicate it, we just have to wait for it to happen. And it inevitably does, several times per day. We went through all the normal troubleshooting procedures and exhausted them all, which left... the tough stuff.


Luckily for us, Microsoft has an excellent article, Production Debugging for .NET Framework Applications, which goes into excruciating detail on how to deal with this situation. In other words, you bring out the big guns:

- [Debugging Tools for Windows 32-bit Version](https://web.archive.org/web/20040803114557/http://www.microsoft.com/whdc/devtools/debugging/installx86.mspx) (windbg.exe and related tools)
- [.NET-specific Debugging Tools Download](https://web.archive.org/web/20051222030418/http://www.microsoft.com/downloads/details.aspx?displaylang=en&FamilyID=7C6EC49C-A8F7-4323-B583-6A7A6AEB5E66) (dbgnetfx.exe)


The article contains an excellent walkthrough, but here’s the reader’s digest version of what you need to do:

1. Install the above tools on the web server with the problem. Unzip the dbgnetfx.exe contents to the debugging tools folder.
2. use the command line tool **adplus.vbs -hang -p ASPNET_WP** to generate a memory dump of the ASPNET_WP process. This will create a folder containing a fairly large file (mine was ~90mb) inside the debugging tools folder. This can be kind of a pain, because you have to trigger this after the crash or during the hang (as in my case). The **adplus_aspnet.vbs** file has some special functionality to “kick in” automatically during crash or hang scenarios.
3. Fire up the windbg.exe application, and open the crash dump file via the drop-down menus. You will need to set the symbol paths (most importantly, including Microsoft’s public http:// symbol server URL) as listed in the document; scroll down to the section titled “To enter the symbol paths, do one of the following.” The windbg app has a command line entry area at the bottom, near the status bar, so that’s where you want to enter those symbol path commands.
4. At this point skip directly to the .NET specific debugging information, which relies on the windbg add in “sos.dll.” That’s contained in the dbgnetfx.exe archive. Scroll down to **.load SOSsos.dll** (er, “son of strike?” I want some of what they’re smoking at MS!) and proceed from there.


Once you’ve gone through all that rigamarole, you actually get some useful, .NET specific information, such as all the thread info:

kg-card-begin: html

```
0:000> !threads
ThreadCount: 23
UnstartedThread: 0
BackgroundThread: 23
PendingThread: 0
DeadThread: 0
PreEmptive   GC Alloc               Lock
ID ThreadOBJ    State     GC       Context       Domain   Count APT Exception
1  1050 0013cc48   200a220 Enabled  05544368:05545054 0020fe78     1 MTA
8  1090 0014ca30      b220 Enabled  00000000:00000000 001400f0     0 MTA (Finalizer)
10   b54 00158f60   1800220 Enabled  00000000:00000000 001400f0     0 MTA (Threadpool Worker)
4   770 0019d8a8   2000220 Enabled  0553c374:0553d054 0020fe78     1 MTA
9  10a0 001c1308   2000220 Enabled  016118ac:01612568 0020fe78     1 MTA
11   d30 001c1800   2000220 Enabled  0554238c:05543054 0020fe78     1 MTA
12  104c 001c1d70   2000220 Enabled  0160f8ac:01610568 0020fe78     1 MTA
14  102c 001ffe50   1800220 Enabled  00000000:00000000 001400f0     0 MTA (Threadpool Worker)
15   3c8 0ebf4488   1800220 Enabled  00000000:00000000 001400f0     0 MTA (Threadpool Worker)
16   aa0 0ec39468   1800220 Enabled  00000000:00000000 001400f0     0 MTA (Threadpool Worker)
18   fd8 001c1b80   1800220 Enabled  00000000:00000000 001400f0     0 MTA (Threadpool Worker)
19  1040 001c1640   1800220 Enabled  00000000:00000000 001400f0     0 MTA (Threadpool Worker)
20  101c 001c19c0   2000220 Enabled  05546398:05547054 0020fe78     1 MTA
21  1044 107e4a08   2000220 Enabled  0554a380:0554b054 0020fe78     1 MTA
22   ea8 107d8b80   2000220 Enabled  01613864:01614568 0020fe78     1 MTA
23   d28 0ec8bef0   2000220 Enabled  05540380:05541054 0020fe78     1 MTA
24   7c8 0ec8cbe0   2000220 Enabled  05548374:05549054 0020fe78     1 MTA
25  1084 1085ebb8   2000220 Enabled  0160b8b8:0160c568 0020fe78     1 MTA
26  1034 0ec8d7d8   2000220 Enabled  0160d8ac:0160e568 0020fe78     1 MTA
27   804 107ae008   2000220 Enabled  016098b8:0160a568 0020fe78     1 MTA
28   c20 107aecf8   2000220 Enabled  01607894:01608568 0020fe78     1 MTA
29   ea4 1089f3d0   2000220 Enabled  0553e3a4:0553f054 0020fe78     1 MTA
30   d88 108a0340       220 Enabled  00000000:00000000 001400f0     0 MTA
```

kg-card-end: html

Of the 32 threads, 14 are associated with the AppDomain for W3SVC5, which I know because I compared the **!dumpdomain (domainid)** output for the value 0020fe78.


OK, so we know we have a lot of blocked threads associated with our website, which we... already sort of knew. Wouldn’t it be helpful if we knew... exactly what .NET commands these threads were issuing?

kg-card-begin: html

```
0:000> ~*e !clrstack
Thread 4
ESP       EIP
00fbf394  77f8287e [FRAME: ECallMethodFrame] [DEFAULT] I4 System.Threading.WaitHandle.WaitMultiple(SZArray Class System.Threading.WaitHandle,I4,Boolean,Boolean)
00fbf3ac  799f1171 [DEFAULT] I4 System.Threading.WaitHandle.WaitAny(SZArray Class System.Threading.WaitHandle,I4,Boolean)
00fbf3c0  0ebe6410 [DEFAULT] [hasThis] Class System.Data.OracleClient.IDBPooledObject System.Data.OracleClient.DBObjectPool.GetObject(ByRef Boolean)
00fbf3f0  0ebe5486 [DEFAULT] Class System.Data.OracleClient.OracleInternalConnection System.Data.OracleClient.OracleConnectionPoolManager.GetPooledConnection(String,Class System.Data.OracleClient.OracleConnectionString,ByRef Boolean)
00fbf40c  0ebe50fa [DEFAULT] [hasThis] Void System.Data.OracleClient.OracleConnection.OpenInternal(Class System.Data.OracleClient.OracleConnectionString,Object)
00fbf448  0ebe5011 [DEFAULT] [hasThis] Void System.Data.OracleClient.OracleConnection.Open()
00fbf454  0fa31977 [DEFAULT] [hasThis] Void SharedUtils.DB.DBDataset.Fill(ByRef Class System.Data.OracleClient.OracleCommand,String)
at [+0x6f] [+0x26]
00fbf48c  0fa330e3 [DEFAULT] [hasThis] Void SharedUtils.DB.DBDataset.Fill(ByRef Class System.Data.OracleClient.OracleCommand,String,String)
at [+0x23] [+0x10]
00fbf4a0  0fa32a2f [DEFAULT] [hasThis] Void CrazyApp.API.Library.GetTreeForContainer(I4,ByRef Class System.Data.DataSet,String,String)
at [+0x12f] [+0xa3]
Thread 9
ESP       EIP
0dddf3f4  77f8287e [FRAME: ECallMethodFrame] [DEFAULT] I4 System.Threading.WaitHandle.WaitMultiple(SZArray Class System.Threading.WaitHandle,I4,Boolean,Boolean)
0dddf40c  799f1171 [DEFAULT] I4 System.Threading.WaitHandle.WaitAny(SZArray Class System.Threading.WaitHandle,I4,Boolean)
0dddf420  0ebe6410 [DEFAULT] [hasThis] Class System.Data.OracleClient.IDBPooledObject System.Data.OracleClient.DBObjectPool.GetObject(ByRef Boolean)
0dddf450  0ebe5486 [DEFAULT] Class System.Data.OracleClient.OracleInternalConnection System.Data.OracleClient.OracleConnectionPoolManager.GetPooledConnection(String,Class System.Data.OracleClient.OracleConnectionString,ByRef Boolean)
0dddf46c  0ebe50fa [DEFAULT] [hasThis] Void System.Data.OracleClient.OracleConnection.OpenInternal(Class System.Data.OracleClient.OracleConnectionString,Object)
0dddf4a8  0ebe5011 [DEFAULT] [hasThis] Void System.Data.OracleClient.OracleConnection.Open()
0dddf4b4  0fa31977 [DEFAULT] [hasThis] Void SharedUtils.DB.DBDataset.Fill(ByRef Class System.Data.OracleClient.OracleCommand,String)
at [+0x6f] [+0x26]
0dddf4ec  0fa330e3 [DEFAULT] [hasThis] Void SharedUtils.DB.DBDataset.Fill(ByRef Class System.Data.OracleClient.OracleCommand,String,String)
at [+0x23] [+0x10]
0dddf500  0fa36a3c [DEFAULT] [hasThis] Class CrazyApp.API.Node.Document CrazyApp.API.Library.GetDocument(I4)
at [+0x7c] [+0x32]
```

kg-card-end: html

I have changed the name of our application to “CrazyApp” to protect the guilty, and I have simplified the dump to only two of the 14 threads. Based on these thread command lists, it now very clear what is going on here: we’re blocking while waiting for database resources via the System.Data.OracleClient.DBObjectPool.GetObject command, on every single thread!


Armed with this information, rather than “gee, ASPNET_WP is deadlocking a lot,” we were able to determine that the *real* problem is a [pooled connection is not disposed](https://web.archive.org/web/20051222204549/https://support.microsoft.com/default.aspx?scid=kb%3Ben-us%3B830173) by Microsoft .NET Managed Provider for Oracle when an exception occurs. There are a lot of people on the newsgroups [complaining about the same thing](http://groups.google.com/groups?hl=en&lr=&ie=UTF-8&q=System.NullReferenceException+System.Data.OracleClient&btnG=Search&ref=blog.codinghorror.com), namely, that the Microsoft System.Data.OracleClient is blindly re-using connections **that it knows to be bad**, which of generates a NullObjectException, and sooner or later – basically at random – causes ASPNET_WP to fall over and cycle.


Good times... good times...

[c#](https://blog.codinghorror.com/tag/c-2/)
[asp.net](https://blog.codinghorror.com/tag/asp-net/)
[debugging](https://blog.codinghorror.com/tag/debugging/)
[production](https://blog.codinghorror.com/tag/production/)
[server](https://blog.codinghorror.com/tag/server/)
