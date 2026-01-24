---
title: "When Object-Oriented Rendering is Too Much Code"
date: 2006-06-21
url: https://blog.codinghorror.com/when-object-oriented-rendering-is-too-much-code/
slug: when-object-oriented-rendering-is-too-much-code
word_count: 357
---

Let’s say you wanted to generate and render this XML fragment:

kg-card-begin: html

<status code="1" />
<data>
<usergroup id="usr" />
</data>


kg-card-end: html
Here’s a fully object-oriented way of building it:
kg-card-begin: html


System.Text.StringBuilder sb = new System.Text.StringBuilder();
XmlWriterSettings xs = new XmlWriterSettings();
xs.ConformanceLevel = ConformanceLevel.Fragment;
xs.Indent = true;
XmlWriter xw = XmlWriter.Create(sb, xs);
xw.WriteStartElement("status");
xw.WriteAttributeString("code", "1");
xw.WriteEndElement();
xw.WriteStartElement("data");
xw.WriteStartElement("usergroup");
xw.WriteAttributeString("id", "usr");
xw.WriteEndElement();
xw.WriteEndElement();
xw.Flush();
return sb.ToString();


kg-card-end: html
That seems like a *tremendous* amount of code to do something relatively simple. I could abandon the pure object approach and do it in two lines of code:
kg-card-begin: html


string s =
@"<status code=""{0}"" />
<data>
<usergroup id=""{1}"" />
</data>";
return String.Format(s, "1", "usr");


kg-card-end: html
It’s far less code. And it's much easier to read!I’ve worked with developers who insisted that **everything had to be generated through an object model**, even if the object-oriented way required many times the amount of code. Although I haven’t worked with Daniel Cazzulino, he [typifies this attitude](http://weblogs.asp.net/cazzu/archive/2004/07/15/AwfulResponseWrite.aspx):If you’re using Response.Write, you’re a dreadful citizen of the ASP.NET world.

As my friend Victor said, “Response.Write is there just for compatibility reasons and for old script programmers to not feel lonely.”

An app written in such a way will not only be difficult to maintain and evolve, it will be almost impossible to customize (specially its layout), will never catch up with the upcoming mobile features and just hurts the eye. Every time I see a Response.Write, and specially if it’s not even kind enough to use HtmlTextWriterTag, HtmlTextWriterAttribute and HtmlTextWriterStyle, the developer who wrote it is instantly removed from my in-memory list of good ASP.NET programmers.[Like Rick Strahl](http://west-wind.com/weblog/posts/5906.aspx), I’m not convinced the verbosity of objects like HtmlTextWriter and XmlTextWriter are warranted.The idea of “write once, run anywhere” via a complex set of objects and adapters is a pleasant one, but it also adds a heavy burden of verbosity and complexity to your project. And you [probably aren’t gonna need it](http://xp.c2.com/YouArentGonnaNeedIt.html) anyway. **Sometimes it’s simpler and clearer to render the HTML or XML directly to the page without all that OO cruft gunking up the works.**

[xml](https://blog.codinghorror.com/tag/xml/)
[object-oriented programming](https://blog.codinghorror.com/tag/object-oriented-programming/)
[rendering](https://blog.codinghorror.com/tag/rendering/)
[code optimization](https://blog.codinghorror.com/tag/code-optimization/)
