---
title: "Marcia, Marcia, Markdown"
date: 2004-03-25
url: https://daringfireball.net/2004/03/marcia_marcia_markdown
slug: marcia_marcia_markdown
word_count: 268
---


## Markdown 1.0b4


[Version 1.0b4 is out](https://daringfireball.net/projects/markdown/). No new features, just bug fixes and
improved integration with Blosxom. Thanks to everyone who submitted
bug reports. I strongly recommend this version to anyone using earlier
betas.


## Aaron Swartz’s html2text


A handful of people have asked if there’s a way to translate Markdown
in reverse — to turn HTML back into Markdown-formatted plain text.
The short answer is yes, by using Aaron Swartz’s new version of
[html2text](http://www.aaronsw.com/2002/html2text/):


> html2text is a Python script that convers a page of HTML into clean,
> easy-to-read plain ASCII. Better yet, that ASCII also happens to be
> valid Markdown (a text-to-HTML format).


html2text works so well that I’m planning to use it to convert most of
my old Daring Fireball articles (the ones I wrote in raw HTML). It’s
worth noting that if you start with a Markdown document, translate it
to HTML, then use html2text to go back to Markdown, it won’t give you
the exact same document you started with. That sort of complete
round-trip fidelity simply is not possible, but html2text comes pretty
close.


Also, much like Markdown and SmartyPants, html2text works as a BBEdit
text filter. Simply save a copy in the Unix Filters folder in your
BBEdit Support folder.


## Gust’s HumaneText


Markdown and html2text are now available from the Mac OS X Services
menu, thanks to [Gust’s HumaneText](http://gu.st/proj/HumaneText.service/), a free utility for Mac OS X
10.3 or later. This means you can use Markdown from Services-aware
apps, including [SubEthaEdit](http://www.codingmonkeys.de/subethaedit/) and TextEdit.



| **Previous:** | [Dive Into Markdown](https://daringfireball.net/2004/03/dive_into_markdown) |
| **Next:** | [Ronco Spray-On Usability](https://daringfireball.net/2004/04/spray_on_usability) |


PreviousNext