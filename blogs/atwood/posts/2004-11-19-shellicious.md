---
title: "Shellicious"
date: 2004-11-19
url: https://blog.codinghorror.com/shellicious/
slug: shellicious
word_count: 1284
---

I mentioned in a previous post that I was **launching command line utilities **[**from an ASP.NET web app**](https://blog.codinghorror.com/processstart-and-impersonation/)** and capturing the output**. I wrote a little multithreaded .Process wrapper class to encapsulate this behavior. It's nothing magical, but it is handy for these scenarios:

kg-card-begin: html

```
Dim cmd As String
cmd = "whoami.exe"
Dim s As New Shell
Console.WriteLine("executing " & cmd)
s.Execute(cmd)
Console.WriteLine("output:")
Console.Write(s.Output)
Console.WriteLine("error:")
Console.Write(s.Error)
Console.WriteLine("execution took " & _
s.ExecutionTime.ToString " milliseconds")
Console.WriteLine("exit code was " & _
s.ExitCode.ToString)
Console.ReadLine()
```

kg-card-end: html

Don't forget to set the .WorkingDirectory if your executables aren't in the default path.


The Shell class is currently synchronous– code execution halts until the command returns or times out. If you have long running console processes, you might want to make this class asynchronous (e.g., non-blocking) and raise events for things like console lines being written, command terminating, etcetera. [These features](https://blog.codinghorror.com/full-threaded-shellicious/) were added.


Code follows...

kg-card-begin: html

```
Imports System.Text
Imports System.IO
Imports System.Diagnostics
Imports System.Threading
''' <summary>
''' Execute a command line string and return the output and/or error.
''' </summary>
Public Class Shell
Implements IDisposable
Private _p As Process
Private _intMaxWaitMs As Integer = 120000
Private _blnDisposed As Boolean = False
Private _OutputBuilder As StringBuilder
Private _ErrorBuilder As StringBuilder
Private _blnGetOutput As Boolean = True
Private _blnGetError As Boolean = True
Private _blnLaunchInThread As Boolean = False
Private _strWorkingDirectory As String
Private _StartTime As DateTime
Private _blnCancelRequested As Boolean = False
Private Const _intSleepMs As Integer = 200
Private _OutputThread As Thread
Private _ErrorThread As Thread
Private _blnProcessLaunched As Boolean = False
Public Event OutputLine(ByVal LineText As String)
Public Event ExecutionComplete(ByVal TimedOut As Boolean)
''' <summary>
''' The working directory to be used by the process that is launched.
''' If left blank, will default to the whatever the current path is.
''' </summary>
Public Property WorkingDirectory() As String
Get
Return _strWorkingDirectory
End Get
Set(ByVal Value As String)
_strWorkingDirectory = Value
End Set
End Property
''' <summary>
''' capture any returned output from the command into the .Output string
''' </summary>
Public Property CaptureOutput() As Boolean
Get
Return _blnGetOutput
End Get
Set(ByVal Value As Boolean)
_blnGetOutput = Value
End Set
End Property
''' <summary>
''' capture any returned errors from the command into the .Error string
''' </summary>
Public Property CaptureError() As Boolean
Get
Return _blnGetError
End Get
Set(ByVal Value As Boolean)
_blnGetError = Value
End Set
End Property
''' <summary>
''' Maximum number of seconds to wait for the process to finish running.
''' Use Integer.MaxValue to specify infinite wait.
''' If the process is not finished in this time, it will be automatically killed.
''' </summary>
Public Property MaximumWaitSeconds() As Integer
Get
Return Convert.ToInt32(_intMaxWaitMs / 1000)
End Get
Set(ByVal Value As Integer)
_intMaxWaitMs = Value * 1000
End Set
End Property
''' <summary>
''' execute the command in a seperate thread, synchronously; if not set, execution is asynchronous (blocking)
''' </summary>
Public Property UseNewThread() As Boolean
Get
Return _blnLaunchInThread
End Get
Set(ByVal Value As Boolean)
_blnLaunchInThread = Value
End Set
End Property
''' <summary>
''' any returned output from the command. Only provided if .CaptureOutput is True.
''' </summary>
Public ReadOnly Property Output() As String
Get
If _OutputBuilder Is Nothing Then
Return ""
Else
Return _OutputBuilder.ToString
End If
End Get
End Property
''' <summary>
''' any returned errors from the command. Only provided if .CaptureError is True.
''' </summary>
Public ReadOnly Property [Error]() As String
Get
If _ErrorBuilder Is Nothing Then
Return ""
Else
Return _ErrorBuilder.ToString
End If
End Get
End Property
''' <summary>
''' command execution time in milliseconds. Returns zero until execution is complete.
''' </summary>
Public ReadOnly Property ExecutionTime() As Integer
Get
If _p Is Nothing Then Return 0
If Not ProcessHasExited() Then Return 0
Return Convert.ToInt32(New TimeSpan(_p.ExitTime.Ticks - _StartTime.Ticks).TotalMilliseconds)
End Get
End Property
''' <summary>
''' exit code for the command. Returns -1 until execution is complete.
''' </summary>
''' <remarks>
''' Developers usually indicate a successful exit by an ExitCode value of zero, and designate errors by nonzero
''' values that the calling method can use to identify the cause of an abnormal process termination.
''' It is not necessary to follow these guidelines, but they are the convention.
''' </remarks>
Public ReadOnly Property ExitCode() As Integer
Get
If _p Is Nothing Then Return -1
If Not ProcessHasExited() Then Return -1
Return _p.ExitCode
End Get
End Property
''' <summary>
''' Executes a command line and waits for it to finish. Check .Error and .Output for results.
''' Set .WorkingDirectory if your command is not fully pathed, or not in the path on this machine.
''' </summary>
''' <param name="Command">valid command line string to execute</param>
Public Sub Execute(ByVal Command As String)
StartProcess("cmd.exe", "/c " & Command "")
End Sub
''' <summary>
''' Cancels execution of the command if it is still running
''' </summary>
Public Sub CancelExecution()
_blnCancelRequested = True
End Sub
Private Function ProcessHasExited() As Boolean
If _p Is Nothing Then
Return True
End If
Return _p.HasExited
End Function
Private Sub LaunchThreadHandler()
'-- launch process
_p.Start()
_blnProcessLaunched = True
WaitForExit()
End Sub
Private Sub OutputThreadHandler()
Dim strLine As String
'-- this will run forever until the thread is aborted or suspended; this is by design
Do While True
If _blnProcessLaunched Then
If _p Is Nothing Then Exit Do
If _blnCancelRequested Then Exit Do
strLine = _p.StandardOutput.ReadLine
If Not strLine Is Nothing Then
_OutputBuilder.Append(strLine)
_OutputBuilder.Append(Environment.NewLine)
RaiseEvent OutputLine(strLine)
Else
'-- suspend
Thread.Sleep(0)
End If
Else
Thread.Sleep(20)
End If
Loop
End Sub
Private Sub ErrorThreadHandler()
Dim strLine As String
'-- this will run forever until the thread is aborted or suspended; this is by design
Do While True
If _blnProcessLaunched Then
If _p Is Nothing Then Exit Do
If _blnCancelRequested Then Exit Do
strLine = _p.StandardError.ReadLine
If Not strLine Is Nothing Then
_ErrorBuilder.Append(strLine)
_ErrorBuilder.Append(Environment.NewLine)
Else
'-- suspend
Thread.Sleep(0)
End If
Else
Thread.Sleep(20)
End If
Loop
End Sub
Private Sub StartProcess(ByVal strFileName As String, Optional ByVal strArguments As String = "")
Dim LaunchThread As Thread
_p = New Process
With _p.StartInfo
If Not _strWorkingDirectory Is Nothing Then
.WorkingDirectory = _strWorkingDirectory
End If
.FileName = strFileName
.Arguments = strArguments
.UseShellExecute = False
.CreateNoWindow = True
.RedirectStandardOutput = _blnGetOutput
.RedirectStandardError = _blnGetError
End With
_StartTime = DateTime.Now
If _blnLaunchInThread Then
LaunchThread = New Thread(New ThreadStart(AddressOf LaunchThreadHandler))
LaunchThread.Name = "ShellLaunchThread"
LaunchThread.Start()
Else
_p.Start()
_blnProcessLaunched = True
End If
'-- spawn threads to read in output and error as they are created
If _blnGetOutput Then
_OutputBuilder = New StringBuilder
_OutputThread = New Thread(New ThreadStart(AddressOf OutputThreadHandler))
_OutputThread.Name = "ShellOutputThread"
_OutputThread.Start()
End If
If _blnGetError Then
_ErrorBuilder = New StringBuilder
_ErrorThread = New Thread(New ThreadStart(AddressOf ErrorThreadHandler))
_ErrorThread.Name = "ShellErrorThread"
_ErrorThread.Start()
End If
If LaunchThread Is Nothing Then
WaitForExit()
End If
End Sub
Private Sub WaitForExit()
'-- wait for process to exit, or else we time out
_blnCancelRequested = False
Dim intWaitedMs As Integer = 0
Do While (Not ProcessHasExited()) And (intWaitedMs < _intMaxWaitMs) And (Not _blnCancelRequested)
Thread.Sleep(_intSleepMs)
intWaitedMs += _intSleepMs
Loop
CloseThreads()
'-- if we timed out, kill the process
If (intWaitedMs >= _intMaxWaitMs) Or _blnCancelRequested Then
_p.Kill()
RaiseEvent ExecutionComplete(True)
Else
RaiseEvent ExecutionComplete(False)
End If
End Sub
Private Sub CloseThreads()
If Not _OutputThread Is Nothing Then
If _OutputThread.IsAlive() Then
_OutputThread.Abort()
End If
_OutputThread = Nothing
End If
If Not _ErrorThread Is Nothing Then
If _ErrorThread.IsAlive() Then
_ErrorThread.Abort()
End If
_ErrorThread = Nothing
End If
End Sub
#Region "  Destructor"
Public Overloads Sub Dispose() Implements System.IDisposable.Dispose
Dispose(False)
GC.SuppressFinalize(Me)
End Sub
Protected Overridable Overloads Sub Dispose(ByVal IsFinalizer As Boolean)
If Not _blnDisposed Then
If IsFinalizer Then
End If
If Not _p Is Nothing Then
_p.Close()
_p = Nothing
End If
CloseThreads()
End If
_blnDisposed = True
End Sub
Protected Overrides Sub Finalize()
Dispose(True)
End Sub
#End Region
End Class
```

kg-card-end: html
[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[user experience](https://blog.codinghorror.com/tag/user-experience/)
