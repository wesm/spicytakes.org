---
title: "Recursive Page.FindControl"
date: 2005-06-01
url: https://blog.codinghorror.com/recursive-pagefindcontrol/
slug: recursive-pagefindcontrol
word_count: 183
---

I’m currently writing my first ASP.NET 2.0 website. VS.NET 2005 is worlds better than VS.NET 2003, but I was mildly surprised to find that Microsoft still hasn’t added a recursive overload for `Page.FindControl`. So, courtesy of Oddur Magnusson, here it is:

kg-card-begin: html

```
private Control FindControlRecursive(Control root, string id)
{
if (root.ID == id)
{
return root;
}
foreach (Control c in root.Controls)
{
Control t = FindControlRecursive(c, id);
if (t != null)
{
return t;
}
}
return null;
}
```

kg-card-end: html

This makes life much easier when you’re trying to get to controls that are themselves contained within other containers, eg, a `TextBox` inside a `DataView` or `DataList`. Would it have killed Microsoft to add an overloaded, recursive version of this?


One interesting semi-undocumented feature of `Page.FindControl`: you can specify a full “path” to a control using colons as separators, like so:

kg-card-begin: html

```
Page.FindControl(“DataList1:_ctl0:TextBox3”)

```

kg-card-end: html

That’s assuming all the containers in the hierarchy have explicit names. You can view source to determine what the dynamically generated ‘null’ IDs are.

[asp.net](https://blog.codinghorror.com/tag/asp-net/)
[c sharp](https://blog.codinghorror.com/tag/c-sharp/)
[recursion](https://blog.codinghorror.com/tag/recursion/)
[web development](https://blog.codinghorror.com/tag/web-development/)
