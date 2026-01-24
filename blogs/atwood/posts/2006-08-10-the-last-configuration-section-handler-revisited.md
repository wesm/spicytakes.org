---
title: "The Last Configuration Section Handler... Revisited"
date: 2006-08-10
url: https://blog.codinghorror.com/the-last-configuration-section-handler-revisited/
slug: the-last-configuration-section-handler-revisited
word_count: 411
---

If you need to store a little bit of state – in your configuration file, or on disk – nothing is faster than some quick and dirty [serialization](http://en.wikipedia.org/wiki/Serialization). Or as I like to call it, stringization.


In late 2004, I wrote about [The Last Configuration Section Handler](https://blog.codinghorror.com/the-last-configuration-section-handler/), which does exactly this for .config files. It’s based on earlier work by [Craig Andera of Pluralsight](https://web.archive.org/web/20061209233026/http://www.pluralsight.com/wiki/default.aspx/Craig/XmlSerializerSectionHandler.html). Let’s bring that code up to date for Visual Studio 2005, and furthermore, we’ll do it in C# and *The Language of the Gods*, VB.NET.


The first thing to do is **set up a little class that represents the data you want to serialize. **Include whatever types you need, but make everything public so it’ll be visible to the serializer.

kg-card-begin: html

namespace SomeNamespace
 {
     public class MyStuff
     {
         public int i;
         public string s;
     } 
 }

kg-card-end: html

Now use this routine to serialize it:

kg-card-begin: html

static string SerializeObject(object o)
 {
     StringBuilder sb = new StringBuilder();
     StringWriter sw = new StringWriter(sb);
     XmlTextWriter xtw = new XmlTextWriter(sw);
     xtw.Formatting = Formatting.Indented;
     xtw.WriteRaw(null);
 
     XmlSerializerNamespaces xsn = new XmlSerializerNamespaces();
     xsn.Add("", "");
 
     XmlSerializer xs = new XmlSerializer(o.GetType());
     xs.Serialize(xtw, o, xsn);
     string s = sb.ToString();
 
     // <Foo> becomes <Foo type="MyClass.Foo">
     s = Regex.Replace(s, "(<" + o.GetType().Name + ")(>)", "$1 type="" + o.GetType().FullName + ""$2");
     return s;
 }

kg-card-end: html

The output is your class, serialized as a nice human-readable string.

kg-card-begin: html

<MyStuff type="SomeNamespace.MyStuff">
   <i>1234</i>
   <s>A bunch of information</s>
 </MyStuff>

kg-card-end: html

It’s just so darn... straightforward. As if I needed another reason to [love strings](https://blog.codinghorror.com/i-heart-strings/). Anyway, take that string and paste it into your web.config file.


To read it in, you’ll need a custom config section. Paste this into your config file to define one:

kg-card-begin: html

<configSections>
   <section name="MyStuff" type="XmlSerializerSectionHandler, CSSerializerSection" />
 </configSections>

kg-card-end: html

The actual XmlSerializerSectionHandler is a bit too much code to paste into a blog post, but it’s still relatively simple:

1. Extract the type from the XML Type attribute
2. Make sure the type is valid
3. Deserialize the XML into a new object of that type


The XmlSerializerSectionHandler is too verbose to reprint here mainly because I added a bunch of error trapping. If something goes wrong, you get a nice explanatory exception instead of a cryptic error. It’s good stuff.


(There’s almost no difference at all between the two languages, except that VB for some reason requires an additional namespace; instead of “SomeNamespace.MyStuff,” it’s “VBSerializerSection.SomeNamespace.MyStuff.”)

[c#](https://blog.codinghorror.com/tag/c-2/)
[.config files](https://blog.codinghorror.com/tag/config-files/)
[serialization](https://blog.codinghorror.com/tag/serialization/)
[vb.net](https://blog.codinghorror.com/tag/vb-net/)
[configuration	handler](https://blog.codinghorror.com/tag/configurationhandler/)
