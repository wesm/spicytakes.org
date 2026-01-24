---
title: "Unbreakable Links Revisited"
date: 2004-08-31
url: https://blog.codinghorror.com/unbreakable-links-revisited/
slug: unbreakable-links-revisited
word_count: 551
---

[Philipp Lenssen](http://blog.outer-court.com/) pointed out that my concept of [Unbreakable Links](https://blog.codinghorror.com/building-unbreakable-links/) is, unsurprisingly, not a new one. It’s also known as

- [Memomark](http://blog.outer-court.com/memomarker/)
- [Google URL](https://web.archive.org/web/20040918060313/http://www.hyperorg.com/blogger/mtarchive/000072.html)
- [Googlenym](http://irish.typepad.com/glossary/2004/08/googlenym.html)
- [Robust Hyperlinks](http://www.dlib.org/dlib/july00/wilensky/07wilensky.html)


All of these terms really refer to the same thing: **using a search engine to build an unique URL**. However, there are some not-so-obvious problems you’ll encounter when building links this way. To work around the problems, the **Robust Hyperlinks** paper proposes using a combination of techniques:

kg-card-begin: html

> *
> A Unique Identifier (UID) is a name unique within the document, as per ID attributes in SGML/XML. These survive the most violent document changes, except its own deletion.
> A Tree Walk describes the path from the root of the document, through internal structural nodes, to a point within media content at a leaf.In practice, tree walks are the central component of robust locations. Since tree walks incrementally refine the structural position in the document as the walk proceeds from root to leaf, they are robust to deletions of content that defeat unique ID and context locations. Thus, tree walks are especially helpful for documents such as those that transclude dynamic content, as with stock quotes, where the content itself changes while the structural position remains constant.We describe tree walks with a sequence of node child numbers and associated node tags (generic identifiers), terminating with an offset into a media element. This is both a simpler, less expressive, and more redundant, representation than is allowed by XPointer. For example, consider the following tree walk into a particular HTML document:21/Professor/8 0/ 0/ADDRESS 1/H3 0/BODY 0/HTML
> Context is a small amount of previous and following information from the document tree. We propose a context record containing a sequence of document content prior to the location, and a sequence of document content following the location. For example, for the location described by the tree walk above, let us suppose the word “Professor” is found in a sentence fragment that reads “congratulations on her promotion to Professor in the Computer Science Division”. The context descriptor could be:her+promotion+to+Professo r+in+the+Computer+Science
>  *

kg-card-end: html

They also propose appending this information to the URL in a querystring – so you have both an absolute link and a relative fallback:


> *Given that lexical signatures are a good way to augment URLs, we are left with the issue of how to associate these with hyperlinks. Our primary requirement is that the solution fit into the existing Web infrastructure moderately well. Our proposal is to append a signature to a URL as if it were a query term. 
> That is, if the URL is: http://www.something.com/a/b/c, and the designated resource has the signature w1,...,w5, 
> Then the robust URL is: http://www.something.com/a/b/c?lexical-signature=“w1+w2+w3+w4+w5”*


I do think, at some point in the future, **all links will be constructed this way**. The existing absolute link system breaks down over time, and I think it’s fairly obvious by now that absolute keyword search is the most effective navigation metaphor for the web. My apologies to [Yet Another Hierarchically Organized Oracle](https://web.archive.org/web/20040929080205/http://docs.yahoo.com/info/misc/history.html), but that style of tree-based directory navigation was always driven by the lack of a competent search engine, not actual choice.


Try building your own unbreakable link with [The Incredible LinkTron 5000(tm)](https://web.archive.org/web/20041016051003/http://www.codinghorror.com/linktron5k/Default.aspx)!

[seo](https://blog.codinghorror.com/tag/seo/)
[search engine optimization](https://blog.codinghorror.com/tag/search-engine-optimization/)
[unique identifier](https://blog.codinghorror.com/tag/unique-identifier/)
[tree walk](https://blog.codinghorror.com/tag/tree-walk/)
[robust hyperlinks](https://blog.codinghorror.com/tag/robust-hyperlinks/)
