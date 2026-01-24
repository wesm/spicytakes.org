---
title: "Is HTML a Humane Markup Language?"
date: 2008-05-13
url: https://blog.codinghorror.com/is-html-a-humane-markup-language/
slug: is-html-a-humane-markup-language
word_count: 1175
---

One of the things we’re thinking about while building [stackoverflow.com](http://stackoverflow.com/) is **how to let users style the questions and answers they’re entering on the site**. Nothing’s decided at this point, but we definitely *won’t* be giving users one of those friendly-but-irritating HTML GUI browser layout controls.


![](https://blog.codinghorror.com/content/images/2025/04/image-112.png)


I have one iron-clad design guide: **this is a site for programmers, so they should be comfortable with basic markup**. None of that nancy-boy GUI toolbar handholding nonsense for us, thank you very much. If you can sling code, a little bit of presentation markup is child’s play.


We will support some sort of markup language to style the questions and answers. But *what* markup language?


I mentioned in [podcast #4](http://blog.stackoverflow.com/index.php/2008/05/podcast-4/) that we consider Wikipedia a defining influence. Let’s see how Wikipedia handles markup syntax. This is what the [edit page](http://en.wikipedia.org/w/index.php?title=Joel_Spolsky&action=edit) for Joel Spolsky’s Wikipedia entry looks like:


![](https://blog.codinghorror.com/content/images/2025/04/image-111.png)


It’s an effective markup language, but I think you’ll agree that it’s more intimidating than *humane*. Wikipedia’s [How to Edit a Page](http://en.wikipedia.org/wiki/Wikipedia:How_to_edit_a_page) and the accompanying [Wikipedia syntax cheatsheet](http://en.wikipedia.org/wiki/Wikipedia:Cheatsheet) helps. Some. I’d argue that writing a Wikipedia entry is a step beyond mere presentational markup; it’s almost like *coding*, as you weave the article into the Wikipedia gestalt. (Incidentally, if you haven’t ever edited a Wikipedia article, you should. I consider it a rite of passage, a sort of internet merit badge for anyone who is serious about their online presence.)


Let’s consider a simpler example. What we’re looking for is some kind of middle ground, a [humane text format](http://bluebones.net/2005/02/humane-text-formats/). Let’s start with some basic HTML.

kg-card-begin: html


| Lightweight Markup Languages
According to **Wikipedia**:

          A [lightweight markup language](http://en.wikipedia.org/wiki/List_of_lightweight_markup_languages) is a markup language with a simple syntax, designed to be easy for a human to enter with a simple text editor, and easy to read in its raw form.
        
Some examples are:

Markdown
Textile
BBCode
Wikipedia

Markup should also extend to *code*:

10 PRINT "I ROCK AT BASIC!"
20 GOTO 10 |


kg-card-end: html

Here’s what that looks like expressed in a variety of lightweight markup languages. Bear in mind that **each of these will produce HTML equivalent to the above**.

kg-card-begin: html

[Textile](https://web.archive.org/web/20081026175423/http://textile.thresholdstate.com/)


[Markdown](http://daringfireball.net/projects/markdown/dingus)





h1. Lightweight Markup Languages
According to *Wikipedia*:
bq. A “lightweight markup language”:http://is.gd/gns
is a markup language with a simple syntax, designed
to be easy for a human to enter with a simple text
editor, and easy to read in its raw form.
Some examples are:
* Markdown
* Textile
* BBCode
* Wikipedia
Markup should also extend to _code_:
pre. 10 PRINT “I ROCK AT BASIC!”
20 GOTO 10
      



Lightweight Markup Languages
============================
According to **Wikipedia**:
> A [lightweight markup language](http://is.gd/gns)
is a markup language with a simple syntax, designed
to be easy for a human to enter with a simple text
editor, and easy to read in its raw form.
Some examples are:
* Markdown
* Textile
* BBCode
* Wikipedia
Markup should also extend to _code_:
10 PRINT “I ROCK AT BASIC!”
20 GOTO 10

kg-card-end: html
kg-card-begin: html


| [Wikipedia](http://en.wikipedia.org/wiki/Wikipedia:How_to_edit_a_page) | [BBCode](http://www.phpbb.com/community/faq.php?mode=bbcode) |
| ==Lightweight Markup Languages==
According to '''Wikipedia''':
:A [[lightweight markup language]]
is a markup language with a simple syntax, designed
to be easy for a human to enter with a simple text
editor, and easy to read in its raw form.
Some examples are:
* Markdown
* Textile
* BBCode
* Wikipedia
Markup should also extend to ''code'':
<source lang=qbasic>
10 PRINT “I ROCK AT BASIC!”
20 GOTO 10
</source> | [size=150]Lightweight Markup Languages[/size]
According to [b]Wikipedia[/b]:
[quote]
A [url=http://is.gd/gns]lightweight markup language[/url]
is a markup language with a simple syntax, designed
to be easy for a human to enter with a simple text
editor, and easy to read in its raw form.
[/quote]
Some examples are:
[list]
[*]Markdown
[*]Textile
[*]BBCode
[*]Wikipedia
[/list]
Markup should also extend to [i]code[/i]:
[code]
10 PRINT “I ROCK AT BASIC!”
20 GOTO 10
[/code] |



kg-card-end: html
None of these lightweight markup languages are particularly difficult to understand – and they’re easy on the eyes, as promised. But I still had to look up the reference syntax for each one and map it to the HTML that I already know by heart. I also found them disturbingly close to “magic” for some of the formatting rules, to the point that I wished I could just write literal HTML and get exactly what I want without guessing how the parser is going to interpret my fake-plain-text.Which leads directly to this question: **why not just stick with what we already know and use HTML?** This c2 wiki page titled Why Doesn’t Wiki Do HTML? makes the case that – at least for Wiki content – you’re better off leaving HTML behind:In a Wiki, the emphasis is on content, not presentation. Simple Wiki markup rules let people focus on expressing their ideas.Why not use a domain-specific markup language designed to do “the simplest thing that could possibly work?”Some HTML tags are difficult to work with and can break the flow of your thoughts. The table tag, for example.Does the average user really need total HTML and CSS layout power?Allowing the full range of HTML tags can lead to major security vulnerabilities.Many people don’t know HTML. A simple Wiki markup language is easier to learn.I’m not sure I agree with all of this, but it can make sense in the context of a full-blown Wiki. It’s worth considering.After all this research on humane markup languages, much to my chagrin, I’ve come full circle. **I now no longer think humane markup languages make sense for most uses**. I agree with the guy at fileformat.info – HTML is generally [the better choice](http://www.fileformat.info/news/2005/03/04/humane_text_formats.htm):**Simplicity**
If the source and destination are the web, why not use the native markup language of the web?**Readability**
HTML is a bit less readable than the lightweight markup languages, it’s true. But basic HTML is not onerous to read, particularly if we hide the repetitive paragraph tags.**Security**
With a bit of careful coding, it is possible to whitelist specific HTML tags that you will allow. This way you avoid exposing yourself to risky/vulnerable tags.**Conversion**
It’s not at all clear that *any* existing lightweight markup language has critical mass, with the possible exception of Wikipedia’s flavor. On the other hand, text parsers and tools will always understand HTML.**What people know**
A lot more people know HTML than any given flavor of humane text. If you’re a programmer, you damn well *better* know HTML. For the handful of wiki-like functions we may need, it’s possible to add some optional attributes to the HTML tags. And wouldn’t that be easier to learn than some weird, pseudo-ASCII derivation of HTML?I do think we’ll adopt some of the cleverer functions of Textile and Markdown, insofar as they remove mundane HTML markup scutwork. But in general, **I’d much rather rely on a subset of trusty old HTML** than expend brain cells trying to [remember the fake-HTML way](http://hobix.com/textile/quick.html) to make something bold, or create a hyperlink. HTML isn’t perfect, but it’s an eminently reasonable humane markup language.

[html](https://blog.codinghorror.com/tag/html/)
[markup language](https://blog.codinghorror.com/tag/markup-language/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[user experience](https://blog.codinghorror.com/tag/user-experience/)
