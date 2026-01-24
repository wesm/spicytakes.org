---
title: "Logging TraceListener"
date: 2005-03-06
url: https://blog.codinghorror.com/logging-tracelistener/
slug: logging-tracelistener
word_count: 679
---

I’m working on a console app that needs to provide integrated logging of its own output. Sure, you could do a standard console output redirect, but I wanted the app to be responsible for logging its own output. I decided to write my own `TraceListener` that **automatically creates IIS-style cyclic logfiles** using the `Trace` method, like so:

kg-card-begin: html

```
Sub Main()
AddListeners(False)
Trace.WriteLine("Hello World!")
Trace.WriteLine("Hello World!", "category1")
Dim h As New Hashtable
Trace.WriteLine(h)
Trace.WriteLine(h, "category2")
For i As Integer = 0 To 99
Trace.WriteLine("Line " & i)
Next
End Sub
Private Sub AddListeners(ByVal DoLog As Boolean)
'-- this causes Trace.Write to
'-- mimic Console.Write
Dim t As New TextWriterTraceListener(System.Console.Out)
Trace.Listeners.Add(t)
'-- this enables IIS-style logging
If DoLog Then
Dim ct As New CyclicLogTraceListener
ct.FolderName = "."
ct.FileCountThreshold = 3
ct.FileSizeThreshold = 3500
ct.FileSizeUnit = CyclicLogTraceListener.SizeUnit.Bytes
ct.FileNameTemplate = "{0:0000}.log"
ct.TimeStampFormat = "yyyy-dd-MM hh:mm:ss"
ct.AddMethod = True
ct.AddPidTid = True
ct.FieldSeparator = ", "
Trace.Listeners.Add(ct)
End If
End Sub
```

kg-card-end: html

You can either add the listener in code, as above, or more dynamically via the `System.Diagnostics` section of the .config file:

kg-card-begin: html

```
<system.diagnostics>  
<trace autoflush="true" indentsize="4">  
<listeners>  
<add name="CyclicLog" type="ConsoleApp.CyclicLogTraceListener,ConsoleApp"  
initializeData="fileSizeThreshold=5000, fileCountThreshold=3, addPidTid=True" />  
</listeners>  
</trace>  
</system.diagnostics>
```

kg-card-end: html

This results in a **log file named 0000.log in the application folder** that looks like so:

kg-card-begin: html

```
2005-07-03 12:25:43, 1392/1476, ConsoleApp.Module1.Main, Hello World!
2005-07-03 12:25:43, 1392/1476, ConsoleApp.Module1.Main, category1, Hello World!
2005-07-03 12:25:43, 1392/1476, ConsoleApp.Module1.Main, System.Collections.Hashtable
2005-07-03 12:25:43, 1392/1476, ConsoleApp.Module1.Main, category2, System.Collections.Hashtable
2005-07-03 12:25:43, 1392/1476, ConsoleApp.Module1.Main, Line 0
2005-07-03 12:25:43, 1392/1476, ConsoleApp.Module1.Main, Line 1
2005-07-03 12:25:43, 1392/1476, ConsoleApp.Module1.Main, Line 2
2005-07-03 12:25:43, 1392/1476, ConsoleApp.Module1.Main, Line 3
2005-07-03 12:25:43, 1392/1476, ConsoleApp.Module1.Main, Line 4
```

kg-card-end: html

The neat thing is that we get this behavior for free – as long as I use `Trace.WriteLine` instead of `Console.WriteLine`, my console app logs its own output, and I can easily modify the logging behavior post-deployment by editing the .config file.


Code follows...


Here’s the complete CyclicLogTraceListener class:

kg-card-begin: html

```
<Imports System>
<Imports System.Diagnostics>
<Imports System.IO>
<Imports System.Reflection>
<Imports System.Text>
<Imports System.Text.RegularExpressions>

<Public Class CyclicLogTraceListener>
<Inherits TraceListener>
<Private Const _StackFrameSkipCount As Integer=5>
<Private Const _IndentCharacter As Char=" "c>
<Private _FileIndex As Long=0>
<Private _FirstLogFound As Boolean=False>
<Private _FileNameTemplateHasFormatting As Boolean=False>
<Private _FileLength As Long=0>
<Private _FileCreationDate As DateTime=DateTime.MinValue>
<Private _sw As StreamWriter>

<#Region "Properties">
<Private _FolderName As String>
<Private _FieldSeparator As String>
<Private _FileSizeThreshold As Long>
<Private _FileSizeUnit As SizeUnit>
<Private _FileCountThreshold As Long>
<Private _FileName As String>
<Private _FileNameTemplate As String>
<Private _TimeStampFormat As String>
<Private _AddMethod As Boolean>
<Private _AddPidTid As Boolean>
<Private _AutoFlush As Boolean>
<Private _FileAgeThreshold As Long>
<Private _FileAgeUnit As AgeUnit>

<!-- Enums -->
<Public Enum AgeUnit>
<Minutes>
<Hours>
<Days>
<Weeks>
<Months>
<End Enum>

<Public Enum SizeUnit>
<Gigabytes>
<Megabytes>
<Kilobytes>
<Bytes>
<End Enum>

<!-- Properties -->
<Public Property AutoFlush() As Boolean>
<Get><Return _AutoFlush><End Get>
<Set(ByVal Value As Boolean)><_AutoFlush=Value><End Set>
<End Property>

<Public Property FolderName() As String>
<Set(ByVal Value As String)>
<_FolderName=Value>
<If Not _FolderName.EndsWith(Path.DirectorySeparatorChar) Then>
<_FolderName=_FolderName & Path.DirectorySeparatorChar>
<End If>
<If Not Directory.Exists(_FolderName) Then>
<Throw New DirectoryNotFoundException("Requested trace logging directory '" & _FolderName & "' does not exist")>
<End If>
<End Set>
<Get><Return _FolderName><End Get>
<End Property>

<Public Property FieldSeparator() As String>
<Set(ByVal Value As String)><_FieldSeparator=Value><End Set>
<Get><Return _FieldSeparator><End Get>
<End Property>

<#End Region>

<#Region "Public Methods">
<Public Sub New()>
<Me.FileNameTemplate="{0:0000}.log">
<_FolderName=".">
<_FileSizeThreshold=1>
<_FileSizeUnit=SizeUnit.Megabytes>
<_FileCountThreshold=10000>
<_TimeStampFormat="yyyy-dd-MM hh:mm:ss">
<_AddMethod=False>
<_AddPidTid=False>
<_FieldSeparator=", ">
<_FileAgeUnit=AgeUnit.Days>
<_FileAgeThreshold=0>
<_AutoFlush=True>
<End Sub>

<Public Sub New(ByVal initializeData As String)>
<Me.New()>
<FolderName=ParseString(initializeData, "folderName", _FolderName)>
<_FileSizeThreshold=ParseLong(initializeData, "fileSizeThreshold", _FileSizeThreshold)>
<_FileSizeUnit=DirectCast(ParseEnum(initializeData, "fileSizeUnit", _FileSizeUnit, GetType(SizeUnit)), SizeUnit)>
<_FileCountThreshold=ParseLong(initializeData, "fileCountThreshold", _FileCountThreshold)>
<_FileAgeThreshold=ParseLong(initializeData, "fileAgeThreshold", _FileAgeThreshold)>
<_FileAgeUnit=DirectCast(ParseEnum(initializeData, "fileAgeUnit", _FileAgeUnit, GetType(AgeUnit)), AgeUnit)>
<_FileNameTemplate=ParseString(initializeData, "fileNameTemplate", _FileNameTemplate)>
<_TimeStampFormat=ParseString(initializeData, "timeStampFormat", _TimeStampFormat)>
<_AddPidTid=ParseBoolean(initializeData, "addPidTid", _AddPidTid)>
<_AddMethod=ParseBoolean(initializeData, "addMethod", _AddMethod)>
<_FieldSeparator=ParseString(initializeData, "fieldSeparator", _FieldSeparator)>
<End Sub>

<Public Overloads Overrides Sub Write(ByVal message As String)>
<WriteMessage(FormatMessage(message, "", False))>
<End Sub>

<Public Overloads Overrides Sub WriteLine(ByVal message As String)>
<WriteMessage(FormatMessage(message, "", True))>
<End Sub>

<Public Overrides Sub Close()>
<SyncLock Me>
<CloseLogFile()>
<End SyncLock>
<End Sub>

<Public Overrides Sub Flush()>
<SyncLock Me>
<If Not _sw Is Nothing Then>
<_sw.Flush()>
<End If>
<End SyncLock>
<End Sub>

<#End Region>
<#End Class>
```

kg-card-end: html
[logging](https://blog.codinghorror.com/tag/logging/)
[tracelistener](https://blog.codinghorror.com/tag/tracelistener/)
[console app](https://blog.codinghorror.com/tag/console-app/)
[integrated logging](https://blog.codinghorror.com/tag/integrated-logging/)
[trace method](https://blog.codinghorror.com/tag/trace-method/)
