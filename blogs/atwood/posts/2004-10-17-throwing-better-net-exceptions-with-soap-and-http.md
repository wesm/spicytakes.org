---
title: "Throwing Better .NET Exceptions with SOAP and HTTP"
date: 2004-10-17
url: https://blog.codinghorror.com/throwing-better-net-exceptions-with-soap-and-http/
slug: throwing-better-net-exceptions-with-soap-and-http
word_count: 893
---

In a recent entry,  I bemoaned the lack of good [global error handling options](https://blog.codinghorror.com/throwing-better-soap-exceptions/) for .NET Web Services. By “good” I mean “easy,” like the **Application_Error event** in Global.asax for ASP.NET websites.


I have a pretty solid web-oriented generic unhandled exception class, which is documented in my CodeProject article, [User Friendly ASP.NET Exception Handling](https://web.archive.org/web/20041027050746/http://www.codeproject.com/aspnet/ASPNETExceptionHandling.asp). This class is instantiated via Application_Error. Based on some developer feedback to that article, and a [recent MSDN article](http://msdn.microsoft.com/library/default.asp?url=%2Flibrary%2Fen-us%2Fdnaspp%2Fhtml%2Felmah.asp), I decided to experiment with hooking my class via **HttpModule**. This turned out way better than I expected – **catching unhandled exceptions via HttpModule is a far better solution than using Application_Error in global.asax**. And look how simple the HttpModule code is:

kg-card-begin: html

```
Public Class UehHttpModule
Implements IHttpModule
Public Sub Init(ByVal Application As System.Web.HttpApplication) Implements System.Web.IHttpModule.Init
AddHandler Application.Error, AddressOf OnError
End Sub
Public Sub Dispose() Implements System.Web.IHttpModule.Dispose
End Sub
Protected Overridable Sub OnError(ByVal sender As Object, ByVal args As EventArgs)
Dim app As HttpApplication = CType(sender, HttpApplication)
Dim ueh As New Handler
ueh.HandleException(app.Server.GetLastError)
End Sub
End Class
```

kg-card-end: html

Functionally, it works the same as before, but with one key benefit: **you can implement global unhandled exception handling on any ASP.NET website without recompiling.** Just drop a .dll in the bin folder, and modify web.config slightly, like so:

kg-card-begin: html

```
<system.web>
<!-- Adds our error handler to the HTTP pipeline -->
<httpModules>
<add name="UehHttpModule"
type="ASPUnhandledException.UehHttpModule, ASPUnhandledException" />
</httpModules>
</system.web>
```

kg-card-end: html

This is much simpler than recompiling, and also offers a higher level of abstraction.


Unfortunately, there’s also one minor side effect: at this stage in the HTTP pipeline, there’s no way to know what the “main” website code assembly is. The EntryAssembly, CallingAssembly, and ExecutingAssembly properties are useless: they are either null, or referencing the UEH assembly itself. This also exposes a deeper problem I had avoided in the past. How do you know what assembly a given exception occurred in? I cheated in the past by assuming the calling or entry assembly was responsible, but that was never a truly valid assumption. The exception could originate from some other random assembly. Fixing this was a pain! According to the MSDN docs, the .Source property of the exception *usually* contains the name of the assembly that generated the exception, so I leverage that to match an assembly in the AppDomain (the only assembly you typically care about is the one with the problem); if no match is found, I blindly dump summary info for all the assemblies.


This is all well and good, but it still doesn’t fix the web service problem. I figured if I was going to implement a HttpModule, I might as well bite the bullet and implement a **SoapExtension**, too. That was a bit more complicated:

kg-card-begin: html

```
Public Class UehSoapExtension
Inherits SoapExtension
Private _OldStream As Stream
Private _NewStream As Stream
Public Overloads Overrides Function GetInitializer(ByVal serviceType As System.Type) As Object
Return Nothing
End Function
Public Overloads Overrides Function GetInitializer(ByVal methodInfo As System.Web.Services.Protocols.LogicalMethodInfo, ByVal attribute As System.Web.Services.Protocols.SoapExtensionAttribute) As Object
Return Nothing
End Function
Public Overrides Sub Initialize(ByVal initializer As Object)
End Sub
Public Overrides Function ChainStream(ByVal stream As Stream) As Stream
_OldStream = stream
_NewStream = New MemoryStream
Return _NewStream
End Function
Private Sub Copy(ByVal fromStream As Stream, ByVal toStream As Stream)
Dim sr As New StreamReader(fromStream)
Dim sw As New StreamWriter(toStream)
sw.Write(sr.ReadToEnd())
sw.Flush()
End Sub
Public Overrides Sub ProcessMessage(ByVal message As System.Web.Services.Protocols.SoapMessage)
Select Case message.Stage
Case SoapMessageStage.BeforeDeserialize
Copy(_OldStream, _NewStream)
_NewStream.Position = 0
Case SoapMessageStage.AfterSerialize
If Not message.Exception Is Nothing Then
Dim ueh As New Handler
Dim strDetailNode As String
'-- handle our exception, and get the SOAP  string
strDetailNode = ueh.HandleWebServiceException(message)
'-- read the entire SOAP message stream into a string
_NewStream.Position = 0
Dim tr As TextReader = New StreamReader(_NewStream)
'-- insert our exception details into the string
Dim s As String = tr.ReadToEnd
s = s.Replace("", strDetailNode)
'-- overwrite the stream with our modified string
_NewStream = New MemoryStream
Dim tw As TextWriter = New StreamWriter(_NewStream)
tw.Write(s)
tw.Flush()
End If
_NewStream.Position = 0
Copy(_NewStream, _OldStream)
End Select
End Sub
End Class
```

kg-card-end: html

As you can see, I have to modify the SOAP message “in flight” to communicate the detailed server exception information back to the client in the <detail> node of the SOAP message. This is critical for a web service, because unlike a website, there’s no visible UI to present a helpful error page – and thus no way to diagnose the error without rooting through server files. The other behaviors (file logging, email, event log, etc.) are all the same.


So, problem solved... with one caveat. We are hooking the SOAP message pipeline, so **only “real” SOAP clients will trigger the SoapExtension**. The web browser isn’t a real SOAP client. If you trigger an exception from the web browser, you’ll just get the standard crappy exceptions, with no events generated on the server at all. Be warned; you’d expect it to work the same in the browser, but it doesn’t. It does work perfectly for SOAP clients though!


I submitted a giant update to the CodeProject article with this information, and a new demo solution. I’m not sure when they’ll get around to posting my update though. Until they do, you can download the all new VS.NET 2003 demo solution from my blog. It’s good stuff!

[.net](https://blog.codinghorror.com/tag/net/)
[soap](https://blog.codinghorror.com/tag/soap/)
[http](https://blog.codinghorror.com/tag/http/)
[exception handling](https://blog.codinghorror.com/tag/exception-handling/)
[httpmodule](https://blog.codinghorror.com/tag/httpmodule/)
