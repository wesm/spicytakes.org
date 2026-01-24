---
title: "Creating Even More Exceptional Exceptions"
date: 2004-10-26
url: https://blog.codinghorror.com/creating-even-more-exceptional-exceptions/
slug: creating-even-more-exceptional-exceptions
word_count: 468
---

In response to my previous post decrying the lack of a master list of [Exception classes for .NET](https://blog.codinghorror.com/creating-more-exceptional-exceptions/), a helpful reader pointed out a clever little utility buried in the .NET SDK:

kg-card-begin: html

```
Program FilesMicrosoft Visual Studio .NET 2003SDKv1.1Binwincv.exe
```

kg-card-end: html

Wincv works well, but it doesn’t allow me to sort or even copy out the class names. After [reflecting on this](http://www.aisto.com/roeder/dotnet/) a bit, I generated the following console app:

kg-card-begin: html

```
Sub Main()
ReflectionSearch(".*exception$")
Console.ReadLine()
End Sub
Sub ReflectionSearch(ByVal strPattern As String)
Dim a As Reflection.Assembly
Dim m As Reflection.Module
Dim t As Type
Dim al As New ArrayList
Dim sl As New SortedList
Dim strAssemblyName As String
For Each strAssemblyName In DefaultAssemblyList()
a = Reflection.Assembly.Load(strAssemblyName)
For Each m In a.GetModules
For Each t In m.GetTypes
al.Add(t)
Dim strFullName As String = t.FullName
If Regex.IsMatch(strFullName, strPattern, RegexOptions.IgnoreCase) Then
sl.Add(strFullName, Nothing)
End If
Next
Next
Next
Dim de As DictionaryEntry
For Each de In sl
Console.WriteLine(de.Key)
Next
Console.WriteLine(sl.Count.ToString & " matches for " & strPattern)
End Sub
Function DefaultAssemblyList() as ArrayList
Dim al As New ArrayList
With al
.Add("mscorlib, Version=1.0.5000.0, Culture=neutral, PublicKeyToken=b77a5c561934e089")
.Add("System.Data, Version=1.0.5000.0, Culture=neutral, PublicKeyToken=b77a5c561934e089")
.Add("System, Version=1.0.5000.0, Culture=neutral, PublicKeyToken=b77a5c561934e089")
.Add("System.Runtime.Remoting, Version=1.0.5000.0, Culture=neutral, PublicKeyToken=b77a5c561934e089")
.Add("System.Windows.Forms, Version=1.0.5000.0, Culture=neutral, PublicKeyToken=b77a5c561934e089")
.Add("System.Xml, Version=1.0.5000.0, Culture=neutral, PublicKeyToken=b77a5c561934e089")
.Add("System.Design, Version=1.0.5000.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a")
.Add("System.DirectoryServices, Version=1.0.5000.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a")
.Add("System.Drawing.Design, Version=1.0.5000.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a")
.Add("System.Drawing, Version=1.0.5000.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a")
.Add("System.Messaging, Version=1.0.5000.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a")
.Add("System.Runtime.Serialization.Formatters.Soap, Version=1.0.5000.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a")
.Add("System.Security, Version=1.0.5000.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a")
.Add("System.ServiceProcess, Version=1.0.5000.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a")
.Add("System.Web, Version=1.0.5000.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a")
.Add("System.Web.Services, Version=1.0.5000.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a")
.Add("System.Management, Version=1.0.5000.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a")
End With
Return al
End Function
```

kg-card-end: html

This console app produces the following (mostly) sorted list of **141 classes in the framework that end in Exception.** Now there’s *really* no reason to throw generic System.Exception, because one of these likely to be a better match – or, failing that, a custom Exception. Thanks for the tips, guys.


p.s. I really am lazy.

kg-card-begin: html

```
System.AppDomainUnloadedException
System.ApplicationException
System.ArgumentException
System.ArgumentNullException
System.ArgumentOutOfRangeException
System.ArithmeticException
System.ArrayTypeMismatchException
System.BadImageFormatException
System.CannotUnloadAppDomainException
System.ComponentModel.Design.CheckoutException
System.ComponentModel.Design.Serialization.CodeDomSerializerException
System.ComponentModel.InvalidEnumArgumentException
System.ComponentModel.LicenseException
System.ComponentModel.WarningException
System.ComponentModel.Win32Exception
System.Configuration.ConfigurationException
System.ContextMarshalException
System.Data.ConstraintException
System.Data.DataException
System.Data.DBConcurrencyException
System.Data.DeletedRowInaccessibleException
System.Data.DuplicateNameException
System.Data.EvaluateException
System.Data.ExprException
System.Data.InRowChangingEventException
System.Data.InvalidConstraintException
System.Data.InvalidExpressionException
System.Data.MissingPrimaryKeyException
System.Data.NoNullAllowedException
System.Data.Odbc.OdbcException
System.Data.OleDb.OleDbException
System.Data.ReadOnlyException
System.Data.RowNotInTableException
System.Data.SqlClient._ValueException
System.Data.SqlClient.SqlException
System.Data.SqlTypes.SqlNullValueException
System.Data.SqlTypes.SqlTruncateException
System.Data.SqlTypes.SqlTypeException
System.Data.StrongTypingException
System.Data.SyntaxErrorException
System.Data.TypedDataSetGeneratorException
System.Data.VersionNotFoundException
System.DivideByZeroException
System.DllNotFoundException
System.Drawing.Printing.InvalidPrinterException
System.DuplicateWaitObjectException
System.EntryPointNotFoundException
System.Exception
System.ExecutionEngineException
System.FieldAccessException
System.FormatException
System.IndexOutOfRangeException
System.InvalidCastException
System.InvalidOperationException
System.InvalidProgramException
System.IO.DirectoryNotFoundException
System.IO.EndOfStreamException
System.IO.FileLoadException
System.IO.FileNotFoundException
System.IO.InternalBufferOverflowException
System.IO.IOException
System.IO.IsolatedStorage.IsolatedStorageException
System.IO.PathTooLongException
System.Management.ManagementException
System.MemberAccessException
System.Messaging.MessageQueueException
System.MethodAccessException
System.MissingFieldException
System.MissingMemberException
System.MissingMethodException
System.MulticastNotSupportedException
System.Net.CookieException
System.Net.ProtocolViolationException
System.Net.Sockets.SocketException
System.Net.WebException
System.NotFiniteNumberException
System.NotImplementedException
System.NotSupportedException
System.NullReferenceException
System.ObjectDisposedException
System.OutOfMemoryException
System.OverflowException
System.PlatformNotSupportedException
System.RankException
System.Reflection.AmbiguousMatchException
System.Reflection.CustomAttributeFormatException
System.Reflection.InvalidFilterCriteriaException
System.Reflection.ReflectionTypeLoadException
System.Reflection.TargetException
System.Reflection.TargetInvocationException
System.Reflection.TargetParameterCountException
System.Resources.MissingManifestResourceException
System.Runtime.InteropServices.COMException
System.Runtime.InteropServices.ExternalException
System.Runtime.InteropServices.InvalidComObjectException
System.Runtime.InteropServices.InvalidOleVariantTypeException
System.Runtime.InteropServices.MarshalDirectiveException
System.Runtime.InteropServices.SafeArrayRankMismatchException
System.Runtime.InteropServices.SafeArrayTypeMismatchException
System.Runtime.InteropServices.SEHException
System.Runtime.Remoting.MetadataServices.SUDSGeneratorException
System.Runtime.Remoting.MetadataServices.SUDSParserException
System.Runtime.Remoting.RemotingException
System.Runtime.Remoting.RemotingTimeoutException
System.Runtime.Remoting.ServerException
System.Runtime.Serialization.SerializationException
System.Security.Cryptography.CryptographicException
System.Security.Cryptography.CryptographicUnexpectedOperationException
System.Security.Policy.PolicyException
System.Security.SecurityException
System.Security.VerificationException
System.Security.XmlSyntaxException
System.ServiceProcess.TimeoutException
System.StackOverflowException
System.SystemException
System.Threading.SynchronizationLockException
System.Threading.ThreadAbortException
System.Threading.ThreadInterruptedException
System.Threading.ThreadStateException
System.Threading.ThreadStopException
System.TypeInitializationException
System.TypeLoadException
System.TypeUnloadedException
System.UnauthorizedAccessException
System.UriFormatException
System.Web.HttpApplication+CancelModuleException
System.Web.HttpCompileException
System.Web.HttpException
System.Web.HttpParseException
System.Web.HttpRequestValidationException
System.Web.HttpUnhandledException
System.Web.Services.Discovery.InvalidContentTypeException
System.Web.Services.Discovery.InvalidDocumentContentsException
System.Web.Services.Protocols.SoapException
System.Web.Services.Protocols.SoapHeaderException
System.Windows.Forms.AxHost+InvalidActiveXStateException
System.Xml.Schema.XmlSchemaException
System.Xml.XmlException
System.Xml.XPath.XPathException
System.Xml.Xsl.XsltCompileException
System.Xml.Xsl.XsltException
```

kg-card-end: html
[.net framework](https://blog.codinghorror.com/tag/net-framework/)
[exception handling](https://blog.codinghorror.com/tag/exception-handling/)
[reflection](https://blog.codinghorror.com/tag/reflection/)
[.net sdk](https://blog.codinghorror.com/tag/net-sdk/)
