---
title: "The Trouble with PDFs"
date: 2008-01-01
url: https://blog.codinghorror.com/the-trouble-with-pdfs/
slug: the-trouble-with-pdfs
word_count: 840
---

Adobe’s [Portable Document Format](http://en.wikipedia.org/wiki/Portable_Document_Format) is so advanced it makes you wonder why anyone bothers with primitive HTML. It’s a completely vector-based layout format, both display and resolution independent. With PDF, you sacrifice almost nothing compared to traditional book and magazine layouts except the [obvious limitation of resolution](https://blog.codinghorror.com/printer-and-screen-resolution/). Here’s Kevin Kelly [extolling the virtues of PDFs](http://www.kk.org/cooltools/archives/002537.php):


> A PDF is able to retain the highly evolved grammar, design and syntax that one thousand years of bookmaking has attained. Because of the idiosyncratic way web browsers work, designers do not have full control of what you as a reader see on the web. The web page, including its fonts, fonts sizes, and placement of material and size of the window, partly depends on the viewer’s preferences. In my experience as a reader, a web designer, and a book designer, the reading experience on paper – and PDFs – is much more refined and elegant. As a publisher and designer I can direct the flow of attention with better tools (font choices, rules, lines, columns) and better control. The benefit to me as a reader is that this sophisticated design translates into increased clarity, smoothness, comprehension, and enjoyment.


But **I have a problem with PDF files**.

1. Every time I link to a PDF, I have to tag the link (pdf) to indicate that the hyperlink will whisk you away, not to another web page as you might expect, but to a strange, otherworldly out-of-browser experience.
2. Links to PDF files assume the user has a PDF viewer installed. Do they? And how will the link be handled? As *in situ* navigation, presenting the user with a weird new set of PDF controls? Or as an undesirable popup window? Browser support for PDF is so weird there are [entire PDF add-ons](https://www.gonitro.com/) to deal with it.
3. The layout better be mind-blowingly good to justify the use of the PDF format. For most of the PDFs I encounter, the information could have been presented in HTML and CSS markup with almost no aesthetic loss at all. The “refined, elegant, sophisticated design” offered by PDF is often wasted.
4. You might argue that PDFs make sense as a secondary, print-optimized version of existing HTML content. But why not stick to *one* version of the content? Why repeat ourselves? Do we really want to maintain two different versions of the same content?


I’m not the first person to note [the usability problems of PDF](http://www.useit.com/alertbox/20030714.html), but I consider this a classic case of [worse is better](https://blog.codinghorror.com/worse-is-better/). The advantages of PDF rarely outweigh the many disadvantages compared to plain old HTML. I suppose relying on PDF was more defensible in 2001, when browser printing support was notoriously poor, and HTML layout was not well understood. But it’s 2008. I’m surprised how many authors *still* reach for the safety blanket of PDF when they and their audience would be much better served with modern HTML.


The other problem with PDFs is a bit more subtle. A PDF is not merely a PDF; it’s a *statement*. An implicit protest against the terrible limitations of the HTML used by the unwashed masses. PDF content yearns to be free of the constraints of common HTML – this content, you see, [signifies something](https://web.archive.org/web/20080106083400/http://www.dashes.com/anil/2003/11/tools-affect-co.html):


> It seems that the PDF format signifies something now, and it’s something more than just user inconvenience. In addition to requiring the user to shift mental modes, (“I’m seeing something designed as a PDF now, this must be *serious information*...”) the requirement that a document either be downloaded or viewed in a context that’s radically different from standard web pages seems like a subtle assertion of authority by a document’s creator. The decision to switch from standard HTML to PDF isn’t arbitrary, but it isn’t based on technical requirements either. It’s based on the value that an author wants to assign to the work, and it benefits from the still-prevalent, though rapidly fading, consensus that print work is somehow more inherently valuable and authoritative than web pages and other online content.


The **massive inconvenience of PDF for the user** rarely outweighs the minor HTML injustices righted through the power of PDF layout. Consider Kevin Kelly’s own [True Films 3.0 PDF](http://www.kk.org/cooltools/archives/002538.php):


![](https://blog.codinghorror.com/content/images/2025/03/image-404.png)


Kevin went to the trouble of packaging this content up as a PDF, even adding Adobe’s brand new support for contextual PDF advertising. All in the name of better formatting. But I don’t see any advanced formatting here! Everything in that PDF would render perfectly as HTML. And **it’d be *better* as HTML**: easier to hyperlink and search, more accessible to a wide audience, and it would *certainly* generate greater advertising revenue through the existing web ad ecosystem.


I don’t dispute Mr. Kelly’s taste in movies for a second. And I worship at the altar of his [Cool Tools](http://www.kk.org/cooltools/index.php). But I’ll never understand how [the founding editor of Wired](http://en.wikipedia.org/wiki/Kevin_Kelly_%28editor%29) could fall prey to such shallow PDF elitism – completely missing the obvious and inherent power of the world’s HTML common denominator.

[pdfs](https://blog.codinghorror.com/tag/pdfs/)
[adobe](https://blog.codinghorror.com/tag/adobe/)
[portable document format](https://blog.codinghorror.com/tag/portable-document-format/)
[layouts](https://blog.codinghorror.com/tag/layouts/)
[design](https://blog.codinghorror.com/tag/design/)
