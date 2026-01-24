---
title: "Hungarian Wars"
date: 2004-06-28
url: https://blog.codinghorror.com/hungarian-wars/
slug: hungarian-wars
word_count: 732
---

I’ve found a number of blog posts about [the pros and cons](https://web.archive.org/web/20040703032637/http://weblogs.asp.net/ericlippert/archive/2003/09/12/52989.aspx) of Simonyi’s **Hungarian Notation**, most notably, [this blog post](http://www.secretgeek.net/charles_hungar.asp) commenting on the extreme polarity of the reprinted MSDN article rating:


![](https://blog.codinghorror.com/content/images/2025/06/image-52.png)


This single image really cuts to the heart of the debate, pointedly illustrating what a [religious war](http://www.lyricsfreak.com/b/blue-oyster-cult/20521.html) this topic is.


Coming from a traditional VB background, with our txts, our frms, and strs and ints, I was befuddled when presented with .NET – what naming scheme do you use for a fully OO language where... *everything is an object*? **objEverything** isn’t very satisfying. So, you start to question whether the naming scheme [ever made any sense](https://web.archive.org/web/20040610195002/http://neopoleon.com/blog/posts/6630.aspx) at all.


After a lot of thought, and a lot of hand-wringing, here are the conventions I ultimately settled on for my .NET development. I’m not proposing these as a standard, merely documenting the thought process that goes into coherent variable naming:

1. Most functions should be short enough that you won’t have a zillion variables. If you have that many variables to tell apart, you have bigger fish to fry.
2. I want to be able to tell “simple” intrinsic types from full blown objects at a glance.* This distinction is important to me. Yeah, they’re all still objects, but there are the common simple variables types we use 99% of the time (e.g., String and Integer), and then there’s everything else.
3. I want to be able to tell class level variables from local variables at a glance.* How far up do I need to scroll?
4. The variable names should be descriptive, readable and succinct.
5. I do not believe every single object needs a unique prefix. This is insane, and as the [VB6 document](https://web.archive.org/web/20060909070533/https://support.microsoft.com/default.aspx?scid=http%3A%2F%2Fsupport.microsoft.com%3A80%2Fsupport%2Fkb%2Farticles%2FQ173%2F7%2F38.ASP&NoWebContent=1) illustrates, this way leads madness...


*At a glance means without having to mouse or cursor over the variable name, e.g., it should work even in the high tech Notepad IDE.


If there is a theme here, it is simplicity and readability. The other theme is that Hungarian Notation seems to have somehow evolved into a catch-all term for “Here’s the [variable naming convention we use](https://web.archive.org/web/20040710121011/http://weblogs.asp.net/larryosterman/archive/2004/06/22/162629.aspx) on our team.” It’s like Linux: there are umpteen zillion “distros” out there, all slightly different flavors of the same basic theme. Here’s what my flavor looks like:

kg-card-begin: html

```
Public Class Class1
Public _strCustomerName as String
Public Function GetCustomerFields(ByVal intCustomerID As Integer) As Specialized.NameValueCollection
Dim nvc As New Specialized.NameValueCollection
Dim ds As New Data.DataSet
Dim dr As Data.DataRow
For Each dr In ds.Tables(0).Rows
nvc.Add(dr.Item("name"), dr.Item("value"))
Next
Return nvc
End Function
End Class
```

kg-card-end: html

The numbered list above documents the rationale (or lack thereof) behind this. You can see where I totally punted on the concept of object prefixes in a fully object oriented language. So many of objects I create are “one off,” with such a limited lifetime and such an obvious, scoped usage that I don’t feel the need to give them unique names. Does it really help to call the dataset dsCustomers in this case? I don’t think so. Keep it short and sweet.


Ultimately, as in the MSDN rating, naming conventions are kind of personal. Pointing out how stupid someone’s variable names are is like telling them how stupid they are for naming their first born child “Melvin.”


On the other hand, I do think it is rude to enter a development team and arbitrarily decide to settle on “the best” conventions; deciding what conventions to adopt is certainly a topic worth broaching in a team developer meeting, but it’s also just plain good manners: when in Rome, do as the Romans do. In the end, **it’s more important to be internally consistent with a naming standard** than it is to spend a lot of time sussing out some kind of perfect, interplanetary naming standard that will never be definitively decided to anyone’s satisfaction anyway.


Pick a reasonable, basic set of standards that most can agree on, but **leave room for personal interpretations**, too. There’s nothing quite as soul crushing as over-standardizing in a religious area where there really isn’t a “right” answer.


> In closing, it is evident that the conventions participated in making the code more correct, easier to write, and easier to read. Naming conventions cannot guarantee good code, however; only the skill of the programmer can.
> – Charles Simonyi

[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[naming conventions](https://blog.codinghorror.com/tag/naming-conventions/)
[object-oriented programming](https://blog.codinghorror.com/tag/object-oriented-programming/)
