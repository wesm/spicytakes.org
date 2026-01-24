---
title: "Determining Build Date the hard way"
date: 2005-04-14
url: https://blog.codinghorror.com/determining-build-date-the-hard-way/
slug: determining-build-date-the-hard-way
word_count: 606
---

One of the key diagnostic data points for any .NET assembly is “when was it built?” Until recently, I thought there were only two ways to suss this out:

1. Check the filesystem date and time
2. Derive the build date from the assembly version


The filesystem method has obvious limitations:

kg-card-begin: html

```
Function AssemblyLastWriteTime(ByVal a As Reflection.Assembly) As DateTime
Try
Return File.GetLastWriteTime(a.Location)
Catch ex As Exception
Return DateTime.MaxValue
End Try
End Function
```

kg-card-end: html

The version method, however, works quite well – as long as developers don’t deviate too far from the default .NET version string of `<Assembly: AssemblyVersion("1.0.*")>`


> *When specifying a version, you have to at least specify major. If you specify major and minor, you can specify an asterisk (*) for build. This will cause **build to be equal to the number of days since January 1, 2000 local time, and for revision to be equal to the number of seconds since midnight local time, divided by 2.**
> If you specify major, minor, and build, you can specify an asterisk for revision. This will cause revision to be equal to the number of seconds since midnight local time, divided by 2.*

kg-card-begin: html

```
Function AssemblyBuildDate(ByVal a As Reflection.Assembly, _
Optional ByVal forceFileDate As Boolean = False) As DateTime
Dim v As System.Version = a.GetName.Version
Dim dt As DateTime
If forceFileDate OrElse (v.Build < 730 Or v.Revision = 0) Then
dt = AssemblyLastWriteTime(a)
Else
dt = New DateTime(2000, 1, 1, 0, 0, 0). _
AddDays(v.Build). _
AddSeconds(v.Revision * 2)
If TimeZone.IsDaylightSavingTime(dt, _
TimeZone.CurrentTimeZone.GetDaylightChanges(dt.Year)) Then
dt = dt.AddHours(1)
End If
'-- sanity check
If dt > DateTime.Now Or dt < New DateTime(2000, 1, 1, 0, 0, 0) Then
dt = AssemblyLastWriteTime(a)
End If
End If
Return dt
End Function
```

kg-card-end: html

Be careful when relying on version to predict build date in Visual Studio .NET. For some reason, the IDE does not update the build number every time you build a solution. **Visual Studio only increments the build and revision number when the solution is closed and reopened.** If you build fifty times throughout the day in the same solution, every single one of your builds will have the same version. Close and reopen that solution, though, and you’ll get a new version immediately. Go figure.


Luckily, we don’t have to settle for those two options. There’s a third way to calculate build date that’s much more reliable. Dustin Aleksiuk recently posted a clever [blog entry](https://web.archive.org/web/20060615040705/http://blog.signaleleven.com/index.php?itemid=10) describing how to **retrieve the embedded linker timestamp** from the IMAGE_FILE_HEADER section of the [Portable Executable](https://web.archive.org/web/20050626081241/http://www.codeproject.com/win32/vbdebugger.asp) header:

kg-card-begin: html

```
Function RetrieveLinkerTimestamp(ByVal filePath As String) As DateTime
Const PeHeaderOffset As Integer = 60
Const LinkerTimestampOffset As Integer = 8
Dim b(2047) As Byte
Dim s As Stream
Try
s = New FileStream(filePath, FileMode.Open, FileAccess.Read)
s.Read(b, 0, 2048)
Finally
If Not s Is Nothing Then s.Close()
End Try
Dim i As Integer = BitConverter.ToInt32(b, PeHeaderOffset)
Dim SecondsSince1970 As Integer = BitConverter.ToInt32(b, i + LinkerTimestampOffset)
Dim dt As New DateTime(1970, 1, 1, 0, 0, 0)
dt = dt.AddSeconds(SecondsSince1970)
dt = dt.AddHours(TimeZone.CurrentTimeZone.GetUtcOffset(dt).Hours)
Return dt
End Function
```

kg-card-end: html

When I ran Dustin’s code for the first time, I wondered why the dates and minutes were correct, but the hours were consistently off by four. Even I can figure out GMT/UTC issues when they practically slap me in the face. I emailed Dustin to ask him what he thought, and as it turns out, **Dustin lives in GMT **–** **that’s the ultimate “it runs on my machine!” Sure does make those pesky mental IIS logfile date conversions easier, too... ;)

[.net](https://blog.codinghorror.com/tag/net/)
[assembly](https://blog.codinghorror.com/tag/assembly/)
[build date](https://blog.codinghorror.com/tag/build-date/)
[versioning](https://blog.codinghorror.com/tag/versioning/)
[filesystem](https://blog.codinghorror.com/tag/filesystem/)
