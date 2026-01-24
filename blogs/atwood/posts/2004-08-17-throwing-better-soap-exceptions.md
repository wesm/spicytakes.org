---
title: "Throwing better SOAP exceptions"
date: 2004-08-17
url: https://blog.codinghorror.com/throwing-better-soap-exceptions/
slug: throwing-better-soap-exceptions
word_count: 559
---

I’m fairly happy with my [global unhandled exception handler](https://web.archive.org/web/20040701020901/http://www.codeproject.com/dotnet/ExceptionHandling.asp) for WinForms and console apps. I also successfully adapted a [version of it for use in ASP.NET apps](https://web.archive.org/web/20040826084311/http://www.codeproject.com/aspnet/ASPNETExceptionHandling.asp), where it interfaces with the **Application_Error** event in global.asax:

kg-card-begin: html

```
Sub Application_Error(ByVal sender As Object, ByVal e As EventArgs)
' Fires when an error occurs
Dim ueh As New AspUnhandledExceptionHandler(True)
ueh.HandleException(Server.GetLastError.GetBaseException())
End Sub
```

kg-card-end: html

What I haven’t been able to do, however, is get it to work with NET web services. Application_Error never fires for a web service. According to my research, **there really is no good way to generically handle unhandled exception in .NET web services.** All the alternatives are... well, bad. Here’s what you can do:

- Put a try...catch around every WebService method. These methods tend to be wrappers around other classes, so this isn’t quite as bad as it sounds, but it’s still not good.
- Use a Facade design pattern to derive all objects from parent objects that... basically do a try...catch on the .Execute method. Uh, thanks but no thanks.
- Write a custom SOAP Extension or HttpModule. This sounds reasonable but... hard. If it’s such a cool, important extension or HttpModule, wouldn’t someone have written it already?


Are there any good answers here? I would definitely like feedback if anyone has any suggestions. After some further poking around, I located the Microsoft documentation on Handling and Throwing Exceptions in XML Web Services. While it doesn’t offer any advice on the above, it did illuminate one problem: by default, **.NET doesn’t throw very good SOAP Exceptions! **You need to re-throw exceptions with some additional data to get the “optional,” but quite helpful, SOAP <detail> error element populated – like so:

kg-card-begin: html

```
Private Sub WebServiceExceptionHandler(ByVal ex As Exception)
Dim ueh As New AspUnhandledExceptionHandler
ueh.HandleException(ex)
'-- Build the detail element of the SOAP fault.
Dim doc As New System.Xml.XmlDocument
Dim node As System.Xml.XmlNode = doc.CreateNode(XmlNodeType.Element, _
SoapException.DetailElementName.Name, _
SoapException.DetailElementName.Namespace)
'-- append our error detail string to the SOAP detail element
Dim details As System.Xml.XmlNode = doc.CreateNode(XmlNodeType.Element, _
"ExceptionInfo", _
SoapException.DetailElementName.Namespace)
details.InnerText = ueh.ExceptionToString(ex)
node.AppendChild(details)
'-- re-throw the exception so we can package additional info
Throw New SoapException("Unhandled Exception: " & ex.Message, _
SoapException.ClientFaultCode, _
Context.Request.Url.ToString, node)
End Sub
```

kg-card-end: html

And it really does work. This is a capture of a generic exception using [a network sniffer](http://www.etherdetect.com/), so we’re looking at raw HTTP traffic here.


Before:

kg-card-begin: html

```

HTTP/1.1 500 Internal Server Error.
Date: Wed, 26 May 2004 05:12:08 GMT
Server: Microsoft-IIS/6.0
X-Powered-By: ASP.NET
X-AspNet-Version: 1.1.4322
Cache-Control: private
Content-Type: text/xml; charset=utf-8
Content-Length: 488
<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
<soap:Body>

<soap:Fault>
<faultcode>soap:Server</faultcode>
<faultstring>Server was unable to process request. --> Object reference not set to an instance of an object.</faultstring>
<detail />
</soap:Fault>

</soap:Body>
</soap:Envelope>

```

kg-card-end: html

After:

kg-card-begin: html

```

HTTP/1.1 500 Internal Server Error.
Date: Wed, 26 May 2004 05:09:20 GMT
Server: Microsoft-IIS/6.0
X-Powered-By: ASP.NET
X-AspNet-Version: 1.1.4322
Cache-Control: private
Content-Type: text/xml; charset=utf-8
Content-Length: 782
<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
<soap:Body>

<soap:Fault>
<faultcode>soap:Server</faultcode>
<faultstring>SoapException</faultstring>
<faultactor>http://192.168.168.10/WebService1/Service1.asmx</faultactor>
<detail>
<ExceptionType>System.NullReferenceException</ExceptionType>
<ExceptionMessage>Object reference not set to an instance of an object.</ExceptionMessage>
<ExceptionTrace>at WebService1.Service1.HelloException2() in HOMESERVERwwwroot$WebService1Service1.asmx.vb:line 70</ExceptionTrace>
</detail>
</soap:Fault>

</soap:Body>
</soap:Envelope>

```

kg-card-end: html

Notice the <detail> element is fully populated, and the entire <soap:Fault> element is much more informative – cool!

[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[error handling](https://blog.codinghorror.com/tag/error-handling/)
[web services](https://blog.codinghorror.com/tag/web-services/)
