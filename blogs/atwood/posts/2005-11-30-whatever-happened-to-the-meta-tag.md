---
title: "Whatever Happened to the META Tag?"
date: 2005-11-30
url: https://blog.codinghorror.com/whatever-happened-to-the-meta-tag/
slug: whatever-happened-to-the-meta-tag
word_count: 631
---

When was the last time you saw a HTML header like this?

kg-card-begin: html

```

<head>
<title>GUID World</title>
<meta name=“description”
content=“Everything you wanted to know about GUIDs but were afraid to ask”>
<meta name=“keywords”
content=“GUID, UUID, globally unique identifiers, 128-bit”>
</head>

```

kg-card-end: html

The web is a **metadata-free zone**. It’s widely known that Google completely ignores metadata in its indexes. The <meta> tag has fallen so far out of favor that it drags the whole concept of metadata down with it. And perhaps rightfully so. Cory Doctorow viciously deconstructs metadata in [Metacrap](http://www.well.com/~doctorow/metacrap.htm): Putting the torch to seven straw-men of the meta-utopia:

kg-card-begin: html

> There are at least seven insurmountable obstacles between the world as we know it and meta-utopia. I’ll enumerate them below:.
> 1. People lie
> Metadata exists in a competitive world. Suppliers compete to sell their goods, cranks compete to convey their crackpot theories (mea culpa), artists compete for audience. Attention-spans and wallets may not be zero-sum, but they’re damned close. That’s why:
> A search for any commonly referenced term at a search-engine like Altavista will often turn up at least one porn link in the first ten results.
> Your mailbox is full of spam with subject lines like “Re: The information you requested.”
> Publisher’s Clearing House sends out advertisements that holler “You may already be a winner!”
> Press-releases have gargantuan lists of empty buzzwords attached to them.
> Meta-utopia is a world of reliable metadata. When poisoning the well confers benefits to the poisoners, the meta-waters get awfully toxic in short order.

kg-card-end: html

The other six reasons are equally caustic, and all have a common theme: **relying on users to create accurate metadata means you’re betting on an optimistic view of human behavior.** And we all know how well *that* works out.


Which brings me to the complete abandonment of the <meta> tag. Isn’t it ironic that groups still advocate manually adding metadata to web pages? Who, exactly, is adding The [Dublin Core Metadata Element Set](http://dublincore.org/documents/dces/) to the <head> section of their web pages? Nobody, that’s who.


Manual metadata may be suspect, but **automated generation of metadata is practically the holy grail.** Google’s entire 450 zillion dollar market cap is predicated on one tiny, automatically generated piece of metadata on every web page they index: PageRank. Popularity rules the web. It’s high school all over again: either you’re popular and people link to you, or... well, good luck on that whole prom thing.


But popularity has some limitations. For one thing, **PageRank doesn’t work on an intranet**. Office documents are rarely HTML, rarely linked to each other, and you probably don’t have a large enough sample set to do any fancy statistical analysis, either. That’s why the Google Search Appliance not only actively indexes metadata in the <meta> tag, it *requires* metadata to return relevant results. It’s [right in the manual](https://web.archive.org/web/20051130024746/http://code.google.com/gsa_apis/xml_reference.html#request_meta_filter). Just try doing that with the capital-g Google.


Perhaps that’s why Tim Bray steadfastly maintains that some form of [metadata is necessary](http://www.tbray.org/ongoing/When/200x/2003/07/29/SearchMeta) to improve search results.


> One of the Web’s distinguishing features is that there’s **a big gaping hole where the metadata ought to be**. The Web has resources, identified by URI, and you can ask for “representations,” which come with some metadata, but the metadata is about the representation, not the resource. Given a URI, the Web has no built-in way to ask questions about it, for example “What is this about?” or “When does it expire?” or “Is this suitable for children?” or “Is this good?”


I’m not an advocate of the [utopian semantic web](http://en.wikipedia.org/wiki/Semantic_Web), mind you, but I sure would like something that can tell the difference between [a Jaguar and a Jaguar](https://blog.codinghorror.com/disambiguating-search-with-quasi-evil-hierarchies/) instead of telling me which one is more popular.

[html](https://blog.codinghorror.com/tag/html/)
[metadata](https://blog.codinghorror.com/tag/metadata/)
[tags](https://blog.codinghorror.com/tag/tags/)
