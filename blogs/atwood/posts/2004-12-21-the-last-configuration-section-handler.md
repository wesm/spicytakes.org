---
title: "The Last Configuration Section Handler..."
date: 2004-12-21
url: https://blog.codinghorror.com/the-last-configuration-section-handler/
slug: the-last-configuration-section-handler
word_count: 732
---

I stumbled across the Craig Andera post, [The Last Configuration Section Handler I’ll Ever Need](https://web.archive.org/web/20040806015414/http://www.pluralsight.com/craig/articleview.aspx/CLR%20Workings/The%20Last%20Configuration%20Section%20Handler%20I.xml) a few months ago, but I didn’t really understand the implications until I started writing a bunch of configuration section handlers. His approach is very clever; **instead of writing a bunch of tedious code to read settings from a .config file, you deserialize an instance of the class using the .config file XML as the input!**


Here’s the VB.NET version of the necessary ConfigurationSectionHandler:

kg-card-begin: html

```
Imports System.Xml
Imports System.Xml.Xpath
Imports System.Xml.Serialization
Imports System.Configuration
Public Class XmlSerializerSectionHandler
Implements IConfigurationSectionHandler
Public Function Create(ByVal parent As Object, ByVal configContext As Object, _
ByVal section As System.Xml.XmlNode) As Object _
Implements System.Configuration.IConfigurationSectionHandler.Create
Dim xpn As XPathNavigator = section.CreateNavigator
Dim TypeName As String = xpn.Evaluate("string(@type)").ToString
Dim t as Type = Type.GetType(TypeName)
Dim xs as XmlSerializer = New XmlSerializer(t)
Return xs.Deserialize(New XmlNodeReader(section))
End Function
End Class
```

kg-card-end: html

And here’s an example of what your **.config* file would look like:

kg-card-begin: html

```
<configuration>
<configSections>
<section name="MyStuff"
type="MyClass.XmlSerializerSectionHandler, MyClass" />
</configSections>
<MyStuff type="MyClass.MyStuff">
<Foo>234</Foo>
<Bar>A bunch of information</Bar>
</MyStuff>
</configuration>
```

kg-card-end: html

Note the **type=** attrib on the MyStuff element. With the type information in that attribute, the <MyStuff> config section can be deserialized to an instance of the MyStuff object:

kg-card-begin: html

```
Class MyStuff
Public foo As Integer
Public bar As String
End Class
```

kg-card-end: html

... in a single call!

kg-card-begin: html

```
Dim ms As MyStuff
ms = CType(ConfigurationSettings.GetConfig("MyStuff"), MyClass.MyStuff)
```

kg-card-end: html

Before going this route, **make sure your class serializes to the same XML format exactly **–** **otherwise you’ll get a bunch of non-intuitive deserialization error messages. Here’s a quick way to serialize a class to the console and view the correct XML that is expected for deserialization:

kg-card-begin: html

```
Dim o as New MyStuff
o.foo = 3
o.bar = "stuff"
Dim sb As New Text.StringBuilder
Dim sw As New IO.StringWriter(sb)
Dim xs As XmlSerializer = New XmlSerializer(o.GetType)
Dim xsn As New XmlSerializerNamespaces
xsn.Add("", "")
Dim xtw As New Xml.XmlTextWriter(sw)
xtw.Formatting = Xml.Formatting.Indented
xtw.WriteRaw("")
xs.Serialize(xtw, o, xsn)
Dim s As String = sb.ToString
s = Regex.Replace(s, "(<" & o.GetType.Name & ")(>)", "$1 type=""" & o.GetType.FullName & """$2")
Console.WriteLine(s)
```

kg-card-end: html

Note that some of the contortions in the above code are necessary to get a “clean” set of XML output, free of namespaces, encoding, and the like. This code was borrowed from [Mark Allanson’s blog](https://web.archive.org/web/20050228005146/http://www.markallanson.net/archives/000179.html).


It really could be The Last Configuration Section You’ll Ever Need.


However, troubleshooting XML that won’t deserialize can be... difficult. Here’s an improved, more robust XmlSerializerSectionHandler that provides much better feedback when things go wrong.

kg-card-begin: html

```
<summary>
Configuration section handler that deserializes configuration settings to an object.
</summary>
<remarks>The root node must have a type attribute defining the type to deserialize to.</remarks>
Public Class XmlSerializerSectionHandler
Implements IConfigurationSectionHandler
Public Function Create(ByVal parent As Object, ByVal configContext As Object, ByVal section As System.Xml.XmlNode) As Object _
Implements System.Configuration.IConfigurationSectionHandler.Create
'-- get the name of the type from the type= attribute on the root node
Dim xpn As XPathNavigator = section.CreateNavigator
Dim TypeName As String = xpn.Evaluate("string(@type)").ToString
If TypeName = "" Then
Throw New ConfigurationException( _
"The type attribute is not present on the root node of " & _
"the <" & section.Name & "> configuration section ", _
section)
End If
'-- make sure this string evaluates to a valid type
Dim t As Type = Type.GetType(TypeName)
If t Is Nothing Then
Throw New ConfigurationException( _
"The type attribute '" & TypeName & "' specified in the root node of the " & _
"the <" & section.Name & "> configuration section " & _
"is not a valid type.", section)
End If
Dim xs As XmlSerializer = New XmlSerializer(t)
'-- attempt to deserialize an object of this type from the provided XML section
Dim xnr As New XmlNodeReader(section)
Try
Return xs.Deserialize(xnr)
Catch ex As Exception
Dim s As String = ex.Message
Dim innerException As Exception = ex.InnerException
Do While Not innerException Is Nothing
s &= " " & innerException.Message
innerException = innerException.InnerException
Loop
Throw New ConfigurationException( _
"Unable to deserialize an object of type '" & TypeName & "' from " & _
"the <" & section.Name & "> configuration section: " & s, _
ex, section)
End Try
End Function
End Class
```

kg-card-end: html
[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[configurationsectionhandler](https://blog.codinghorror.com/tag/configurationsectionhandler/)
[.net](https://blog.codinghorror.com/tag/net/)
[xmlserialization](https://blog.codinghorror.com/tag/xmlserialization/)
