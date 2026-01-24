---
title: "Custom AssemblyInfo Attributes"
date: 2004-11-28
url: https://blog.codinghorror.com/custom-assemblyinfo-attributes/
slug: custom-assemblyinfo-attributes
word_count: 352
---

To complement my previous post bemoaning the [lack of respect for AssemblyInfo](https://blog.codinghorror.com/populate-your-assemblyinfo/), I wanted to illustrate just how easy it is to add a few custom attributes to our AssemblyInfo file:

kg-card-begin: html

```
Imports System
Imports System.Reflection
<Assembly: AssemblyTitle("ASPUnhandledException")>
<Assembly: AssemblyDescription("ASP.NET unhandled exception handling library")>
<Assembly: AssemblyCompany("Atwood Heavy Industries")>
<Assembly: AssemblyCompanyEmail("[email protected]")>
<Assembly: AssemblyCompanyUrl("http://www.atwoodheavyindustries.com")>
<Assembly: AssemblyProduct("Exception Handling Framework")>
<Assembly: AssemblyCopyright(" 2004, Atwood Heavy Industries")>
<Assembly: AssemblyTrademark("All Rights Reserved")>
<Assembly: CLSCompliant(True)>
<Assembly: AssemblyVersion("2.1.*")>
```

kg-card-end: html

To get the custom attributes **AssemblyCompanyUrl** and **AssemblyCompanyEmail **working, just add these two classes to your solution:

kg-card-begin: html

```
<AttributeUsage(AttributeTargets.Assembly)> _
Public Class AssemblyCompanyEmailAttribute
Inherits System.Attribute
Private _strCompanyEmail As String
Public Sub New(ByVal email As String)
_strCompanyEmail = email
End Sub
Public Overridable ReadOnly Property CompanyEmail() As String
Get
Return _strCompanyEmail
End Get
End Property
End Class
<AttributeUsage(AttributeTargets.Assembly)> _
Public Class AssemblyCompanyUrlAttribute
Inherits System.Attribute
Private _strCompanyUrl As String
Public Sub New(ByVal url As String)
_strCompanyUrl = url
End Sub
Public Overridable ReadOnly Property CompanyUrl() As String
Get
Return _strCompanyUrl
End Get
End Property
End Class
```

kg-card-end: html

Once you’ve compiled your assembly, the obvious question is, how do we get these attributes (custom or standard) back out? I do it with a reflection loop into a NameValueCollection:

kg-card-begin: html

```
Private Shared Function GetAssemblyAttribs(ByVal a As Reflection.Assembly) _
As Specialized.NameValueCollection
Dim attribs() As Object
Dim attrib As Object
Dim Name As String
Dim Value As String
Dim nvc As New Specialized.NameValueCollection
attribs = a.GetCustomAttributes(False)
For Each attrib In attribs
Name = attrib.GetType().ToString()
Value = ""
Select Case Name
Case "System.Reflection.AssemblyTrademarkAttribute"
Name = "Trademark"
Value = CType(attrib, AssemblyTrademarkAttribute).Trademark.ToString
Case "System.Reflection.AssemblyProductAttribute"
Name = "Product"
Value = CType(attrib, AssemblyProductAttribute).Product.ToString
Case "System.Reflection.AssemblyCopyrightAttribute"
Name = "Copyright"
Value = CType(attrib, AssemblyCopyrightAttribute).Copyright.ToString
Case "System.Reflection.AssemblyCompanyAttribute"
Name = "Company"
Value = CType(attrib, AssemblyCompanyAttribute).Company.ToString
Case "System.Reflection.AssemblyTitleAttribute"
Name = "Title"
Value = CType(attrib, AssemblyTitleAttribute).Title.ToString
Case "System.Reflection.AssemblyDescriptionAttribute"
Name = "Description"
Value = CType(attrib, AssemblyDescriptionAttribute).Description.ToString
Case Else
'Console.WriteLine(Name)
End Select
If Value <> "" Then
If nvc.Item(Name) = "" Then
nvc.Add(Name, Value)
End If
End If
Next
Return nvc
End Function
```

kg-card-end: html

But I am sure there are other ways.

[.net](https://blog.codinghorror.com/tag/net/)
[assemblyinfo](https://blog.codinghorror.com/tag/assemblyinfo/)
[attributes](https://blog.codinghorror.com/tag/attributes/)
[assembly](https://blog.codinghorror.com/tag/assembly/)
[programming](https://blog.codinghorror.com/tag/programming/)
