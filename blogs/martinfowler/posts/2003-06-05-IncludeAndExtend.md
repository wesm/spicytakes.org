---
title: "Include And Extend"
description: "UML use case diagrams define a bunch of relationships between use 	cases. The two best known are include and extend. There seem to be 	more questions on these two relationships than on any other part "
date: 2003-06-05T00:00:00
tags: ["uml"]
url: https://martinfowler.com/bliki/IncludeAndExtend.html
slug: IncludeAndExtend
word_count: 210
---


UML use case diagrams define a bunch of relationships between use
	cases. The two best known are include and extend. There seem to be
	more questions on these two relationships than on any other part of
	use cases, perhaps even anything in the UML.


You won't find an explanation here, rather my advice is to ignore
	extend. Just pretend it doesn't exist. Using extend properly isn't
	going to make any significant difference to your project - you
	almost certainly have much more important issues to worry about.


Include, on the other hand, is useful. You use it when you have a
	bunch of steps in a use case that's either duplicated between use
	cases, or makes sense as its own chunk. However don't take include
	too far - one level of included use cases will probably suffice for
	most cases.


In any case remember that use case diagrams are very close to
	useless. The real value of use cases lies in the content - the text
	that describes them. The diagram makes a visual table of contents,
	but nothing more.


If you want to learn about use cases, you should get hold of
	[Cockburn](https://www.amazon.com/gp/product/0201702258/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=0201702258&linkCode=as2&tag=martinfowlerc-20). It is by far the best book
	on the subject, and is preferable to my advice.
