---
title: "Full Threaded Shellicious"
date: 2004-11-22
url: https://blog.codinghorror.com/full-threaded-shellicious/
slug: full-threaded-shellicious
word_count: 208
---

I couldn’t resist adding some features to [my Shellicious code](https://blog.codinghorror.com/shellicious/). You can now run shell commands either asynchronously (as before) or synchronously, like so:

kg-card-begin: html

```
Private WithEvents _s As New Shell
Private _IsExecutionComplete As Boolean = False
Public Sub Main()
 _s.UseNewThread = True
_s.Execute("C:LongRunningConsoleApp.exe")
Do While Not _IsExecutionComplete
'-- do other work here..
Thread.Sleep(20)
Loop
Console.WriteLine("Exiting Sub Main()..")
Console.ReadLine()
End Sub
Private Sub OutputLine(ByVal LineText As String) Handles _s.OutputLine
Console.WriteLine(LineText)
End Sub
Private Sub ExecutionComplete(ByVal TimedOut As Boolean) _
Handles _s.ExecutionComplete
_IsExecutionComplete = True
Console.WriteLine("execution complete; did we time out? " & TimedOut)
If _s.ExitCode <> 0 Then
Console.WriteLine(_s.Error)
End If
Console.WriteLine(_s.ExecutionTime)
Console.WriteLine(_s.ExitCode)
End Sub
```

kg-card-end: html

I updated the code in the original post. And this time I remembered to give the threads names, which always helps in debugging:

kg-card-begin: html

```
The thread 'ShellErrorThread' (0xca4) has exited with code 0 (0x0).
The thread 'ShellOutputThread' (0x934) has exited with code 0 (0x0).
The thread 'ShellLaunchThread' (0x5c0) has exited with code 0 (0x0).
```

kg-card-end: html

So far so good. The synchronous behavior respects the same .MaximumWaitSeconds property as before, and there’s a new .CancelExecution method if you want to bail out on demand.

[shell scripting](https://blog.codinghorror.com/tag/shell-scripting/)
[shell commands](https://blog.codinghorror.com/tag/shell-commands/)
[asynchronous programming](https://blog.codinghorror.com/tag/asynchronous-programming/)
[synchronous programming](https://blog.codinghorror.com/tag/synchronous-programming/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
