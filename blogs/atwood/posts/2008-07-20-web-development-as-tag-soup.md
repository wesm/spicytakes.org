---
title: "Web Development as Tag Soup"
date: 2008-07-20
url: https://blog.codinghorror.com/web-development-as-tag-soup/
slug: web-development-as-tag-soup
word_count: 437
---

As we work with [ASP.NET MVC](http://www.asp.net/mvc/) on Stack Overflow, I find myself violently thrust back into the bad old days of tag soup that I remember from my tenure as a classic ASP developer in the late 90s. If you’re not careful bordering on manically fastidious in constructing your Views, you’ll end up with **a giant mish-mash of HTML, Javascript, and server-side code**. Classic tag soup; difficult to read, difficult to maintain.


I don’t mean tag soup in the sense of [badly formed HTML](http://en.wikipedia.org/wiki/Tag_soup), or the [malformed world](https://blog.codinghorror.com/its-a-malformed-world/) we live in. I mean tag soup in the sense of **mixing HTML markup and server-side code**. Now you can double your pleasure: badly formed HTML, meet badly written code.


The tag soup problem seems to be **endemic to all modern web development stacks**. I see that Ruby on Rails apps have the same problem; here’s a slice of representative [RHTML](https://web.archive.org/web/20080908080454/http://wiki.rubyonrails.org/rails/pages/UnderstandingViews) from Typo, a Ruby blogging engine.


![](https://blog.codinghorror.com/content/images/2025/04/image-183.png)


Do you find this readable? Can you see where the code begins and the markup ends? Are you confident you could change the code structure without breaking the HTML, or change the HTML structure without breaking the code?


Sometimes editing this stuff makes me feel like I’m playing [Operation](http://en.wikipedia.org/wiki/Operation_(game)). I have to ever so carefully maneuver my metal tweezers into one tiny slice of code or HTML and make my changes without touching the edges and setting off that blasted electrical buzzer.


![](https://blog.codinghorror.com/content/images/2025/04/image-182.png)


I’m not trying to single out Rails or Typo here; I could easily show you a ASP.NET MVC view that’s just as confusing (or as “clear,” if you think that’s perfectly readable, I guess). Tag soup is everywhere; take a look at the Python [Django framework templates](https://web.archive.org/web/20080829190229/http://www.djangoproject.com/documentation/templates/):

kg-card-begin: html

```

<h1>Archive for {{ year }}</h1>
{% for date in days %}
{% ifchanged %}<h3>{{ date|date:“F” }}</h3>{% endifchanged %}
<a href=“{{ date|date:“M/d”|lower }}/”>{{ date|date:“j” }}</a>
{% endfor %}

```

kg-card-end: html

Perhaps when it comes to mixing HTML and server-side code, some form of soup is unavoidable, a necessary evil. The soup can be quite palatable; maybe even delicious. It’s certainly possible to write *good* tag soup and *bad* tag soup.


But I have to wonder: **is there a better way?** Is there something beyond RHTML, Views, and Templates? What examples would you point to of web development stacks that *avoided* degenerating into yet more hazardous, difficult to maintain tag soup? Is there anything truly better on the horizon?


Or is this year’s newer, fancier, even-more-delicious iteration of tag soup as good as it ever gets for web development?

[asp.net mvc](https://blog.codinghorror.com/tag/asp-net-mvc/)
[tag soup](https://blog.codinghorror.com/tag/tag-soup/)
[html](https://blog.codinghorror.com/tag/html/)
[javascript](https://blog.codinghorror.com/tag/javascript/)
[server-side code](https://blog.codinghorror.com/tag/server-side-code/)
[web development](https://blog.codinghorror.com/tag/web-development/)
