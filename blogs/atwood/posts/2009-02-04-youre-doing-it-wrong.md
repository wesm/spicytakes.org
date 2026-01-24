---
title: "You’re Doing It Wrong"
date: 2009-02-04
url: https://blog.codinghorror.com/youre-doing-it-wrong/
slug: youre-doing-it-wrong
word_count: 695
---

In [The Sad Tragedy of Micro-Optimization Theater](https://blog.codinghorror.com/the-sad-tragedy-of-micro-optimization-theater/) we discussed the performance considerations of building a fragment of HTML.

kg-card-begin: html

```

string s =
@"<div class=""action-time"">{0}{1}</div>
<div class=""gravatar32"">{2}</div>
<div class=""details"">{3}<br/>{4}</div>";
return String.Format(s, st(), st(), st(), st());

```

kg-card-end: html

The second act of this particular theater was foreshadowed by [Stephen Touset’s](https://web.archive.org/web/20090208074114/http://www.workingwithrails.com/person/14560-stephen-touset) comment:


> The correct answer is that **if you’re concatenating HTML, you’re doing it wrong in the first place. Use an HTML templating language.** The people maintaining your code after you will thank you (currently, you risk anything from open mockery to significant property damage).


The performance characteristics of building small string fragments isn’t just a red herring – no, it’s far, far worse. The *entire question is wrong*. This is one of my favorite [lessons from The Pragmatic Programmer](https://blog.codinghorror.com/a-pragmatic-quick-reference/).


> When faced with an impossible problem, identify the real constraints. Ask yourself: “Does it have to be done this way? Does it have to be done at all?”


If our ultimate conclusion was that performance is secondary to readability of code, that’s exactly what we should have asked, before doing anything else.


Let’s express the same code sample using the standard [ASP.NET MVC](http://www.asp.net/mvc/) templating engine. And yes, we render stuff like this all over the place in Stack Overflow. It’s the default method of rendering for a reason.

kg-card-begin: html

```

<div class=“action-time”><%= User.ActionTime %></div>
<div class=“gravatar32”><%= User.Gravatar %></div>
<div class=“details”><%= User.Details %><br/><%= User.Stuff %></div>

```

kg-card-end: html

We have a HTML file, through which we poke some holes and insert the data. Simple enough, and conceptually similar to the `String.Replace` version. Templating works reasonably well in the trivial cases when you have an object with obvious, basic data types in fields that you spit out.


But beyond those simple cases, it’s shocking how hairy HTML templating gets. What if you need do to a bit of formatting or processing to get that data into shape before displaying it? What if you need to make decisions and display things differently depending on the contents of those fields? Your once-simple page templates get progressively more and more complex.

kg-card-begin: html

```

<%foreach (var User in Users) { %>
<div class=“action-time”><%= ActionSpan(User)%></div>
<% if (User.IsAnonymous) { %>
<div class=“gravatar32”><%= RenderGravatar(User)%></div>
<div class=“details”><%= RepSpan(User)%><br/><%= Flair(User)%></div>
<% } else { %>
<div class=“anon”>anonymous</div>
<% } %>
<% } %>

```

kg-card-end: html

This is a fairly mild case, but you can see where templating naturally tends toward a frantic, unreadable mish-mash of code and template – [Web Development as Tag Soup](https://blog.codinghorror.com/web-development-as-tag-soup/). If your HTML templates can’t be kept simple, they’re not a heck of a lot better than the procedural string building code they’re replacing. And this is not an easy thing to stay on top of, in my experience. The daily grind of struggling to keep the templates from devolving into tag soup starts to feel every bit as grotty as all that nasty string work we were theoretically replacing.


Now it’s my turn to ask – *why?*


I think existing templating solutions are going about this completely backwards. **Rather than poking holes in HTML to insert code, we should simply treat HTML *as* code.**


Like so:

kg-card-begin: html

```

foreach (var User in Users)
{
<div class=“action-time”>[ActionSpan(User)]</div>
if (User.IsAnonymous)
{
<div class=“gravatar32”>[RenderGravatar(User)]</div>
<div class=“details”>[UserRepSpan(User)]<br/>[UserFlairSpan(User)]</div>
}
else
{
<div class=“anon”>anonymous</div>
}
}
```

kg-card-end: html

Seamlessly mixing code and HTML, using a minimum of those headache-inducing escape characters. Is this a programming language for [a race of futuristic supermen?](https://blog.codinghorror.com/a-race-of-futuristic-supermen/) No. There are languages that can do this right now, today – where you can **stick HTML in the middle of your code**. It’s already possible [using Visual Basic XML Literals](https://web.archive.org/web/20090205151813/http://blogs.msdn.com/dmitryr/archive/2008/12/29/asp-net-mvc-view-engine-using-vb-net-xml-literals.aspx), for example.


![](https://blog.codinghorror.com/content/images/2025/04/image-298.png)


Even the [hilariously maligned X#](http://www.reddit.com/r/programming/comments/7rc5v/x_xml_oriented_programming_language_i_cant/c076grx) has the right core idea. Templating tends to break down because **it forces you to treat code and markup as two different and fundamentally incompatible things.** We spend all our time awkwardly switching between markup-land and code-land using escape sequences. They’re always fighting each other – and us.


Seeing HTML and code get equal treatment in my IDE makes me realize one thing:


We’ve *all* been doing it wrong.

[html](https://blog.codinghorror.com/tag/html/)
[performance optimization](https://blog.codinghorror.com/tag/performance-optimization/)
[templating languages](https://blog.codinghorror.com/tag/templating-languages/)
[string formatting](https://blog.codinghorror.com/tag/string-formatting/)
[software maintenance](https://blog.codinghorror.com/tag/software-maintenance/)
