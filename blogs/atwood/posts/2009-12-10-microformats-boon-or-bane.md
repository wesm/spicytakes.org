---
title: "Microformats: Boon or Bane?"
date: 2009-12-10
url: https://blog.codinghorror.com/microformats-boon-or-bane/
slug: microformats-boon-or-bane
word_count: 1064
---

I recently added [microformat](http://en.wikipedia.org/wiki/Microformat) support to the free public CVs at careers.stackoverflow.com by popular demand.


> Designed for humans first and machines second, **microformats are a set of simple, open data formats built upon existing and widely adopted standards**.


The [official](http://microformats.org/) microformat “[elevator pitch](https://blog.codinghorror.com/can-your-team-pass-the-elevator-test/)” tells us nothing useful. That’s not a good sign. It doesn’t get much better on the [learn more](http://microformats.org/about) link, either.


I’m left scratching my head, wondering **why I should care**. What problem, exactly, do microformats solve for me as a user? As a software developer? There’s lots of hand-wavy talk about *data*, but precious little in the way of concrete stories or real world examples.


But I have a real world example: a CV. To some human resource departments the standard web interchange format for a CV or Resume is already established – it’s called “Microsoft Word.” I have no beef with Word, but certainly we’d like to pick a more **simple, open data format** for our personal data than Microsoft Word – and the [hResume](https://web.archive.org/web/20100628052852/http://en.wikipedia.org/wiki/HResume) microformat seems to fit the bill. And if your CV is published on the web in a standard(ish) format, it’s easier to take it with you wherever you need to go.


I had already implemented the [tag](http://microformats.org/wiki/rel-tag) and [identity](http://microformats.org/wiki/rel-me) microformats on Stack Overflow many months ago. I wasn’t convinced of the benefits, but the implementation was so easy that it seemed like more work to argue the point than to actually *get it done*. Judge for yourself:

kg-card-begin: html

```

<a href=“http://www.codinghorror.com/” rel=“me”>codinghorror.com</a>
<a href=“/questions/tagged/captcha” rel=“tag”>captcha</a>

```

kg-card-end: html

Fairly clean and simple, right? That was the extent of my experience with microformats. Limited, but positive. Then I read through the [hResume microformat spec](http://microformats.org/wiki/hresume). You should read it too. Go ahead. I’ll wait here.


My first impression was not positive, to put it mildly. So you want me to **take the ambiguous, crappy “HTML” markup we already have and layer some ambiguous, crappy “microformat” markup on *top* of it?** And that’s... a solution? If that’s what microformats are going to be about, I think I might want off the microbus.


Let’s take a look at a representative slice of hResume markup:

kg-card-begin: html

```

<div class=“vcard”>
<a class=“fn org url” href=“http://example.com/”>Example</a>
<div class=“adr”>
<span class=“type”>Work</span>:
<div class=“street-address”>169 Maple Ave</div>
<span class=“locality”>Anytown</span>,
<abbr class=“region” title=“Iowa”>IA</abbr>
<span class=“postal-code”>50981</span>
<div class=“country-name”>USA</div>
</div>
</div>

```

kg-card-end: html

As you can see, **the crux of microformats is overloading CSS classes**. When you give something the “adr” class within the “vcard” class, that means it’s the address data field within the hCard, within the hResume.


While I can see the attraction, this approach makes me uneasy:

1. **We’re overloading the class attribute with two meanings.** Is “adr” the name of a class that contains styling information, or the name of a data field? Or both? It’s impossible to tell. The minute you introduce a microformat into your HTML, the semantics of the class attribute have been permanently altered.
2. **The microformat css class names may overlap with existing css classes**. Woe betide the poor developer who has to retrofit a microformat on an established site where “locality” or “region” have already been defined in the CSS and are associated with elements all over the site. And let me tell you, many of the microformat css field names are, uh, *conveniently* named what you’ve probably already used in your HTML somewhere. In the wrong way, inevitably.
3. **There’s no visual indication whatsoever that any given css class is a microformat**. If you hire a new developer, how can they possibly be expected to know that “postal-code” isn’t just an arbitrarily chosen CSS class name, it’s a gosh darned officially blessed *microformat*? What if they decide they don’t like dashes in CSS class names and rename the style “postalcode”? Wave bye bye to your valid microformat. If it seems fragile and obtuse, that’s because it is.
4. **The spec is *incredibly* ambiguous**. I read through the hResume, hCard, and hCalendar spec multiple times, checked all the samples, viewed source on existing sites, used all the [validators](http://ufxtract.com/) I could find, and I *still* got huge swaths of the format wrong! For a “simple” and “easy” format, it’s... anything but, in my experience. The specification is full of ambiguities and requires a lot of interpretation to even get close. I’m not the [world’s best developer](https://blog.codinghorror.com/why-im-the-best-programmer-in-the-world/), but I’m theoretically competent, and if I can’t implement hResume without wanting to cut myself and/or writing snarky blog posts like this, how can we expect everyone else to?
5. **It doesn’t handle unstructured data well**. On Stack Overflow, we have a single “location” field. No city, state, zip, lat, long, and all that jazz: just an unstructured, freeform, enter-whatever-pleases-you “location” field. This was awkward to map in hCard, which practically *demands* that addresses be chopped up into meticulous little sub-fields. This is a bit ironic for a format supposedly designed to work with the loose, unstructured world wide web. Oh, and this goes double for dates. If you don’t have an ISO datetime value, good luck.


Maybe I have a particular aversion to getting my chocolate data structure mixed up with my peanut butter layout structure, but it totally skeeves me out that the microformat folks actually *want* us to design our CSS and HTML around these specific, ambiguous and non-namespaced microformat CSS class names. It feels like a hacky overload. While you could argue this is no different than the web and HTML in general – a giant wobbly teetering tower of nasty, patched-together hacks – something about it fundamentally bothers me.


Now, all that said, **I still think microformats are useful and worth implementing**, if for no other reason than it’s *too easy not to*. If you have semi-structured data, and it maps well to an existing microformat, why not? Yes, it is kind of a hack, but it might even be a useful hack if [Google starts indexing your microformats](http://microformats.org/wiki/google-search) and presenting them in search results. While I’m unclear on the general benefits of microformats for end users or developers, seeing stuff like this in search results...


![google-microformat-results-forum.png](http://www.codinghorror.com/blog/images/google-microformat-results-forum.png)


![google-microformat-results-review.png](http://www.codinghorror.com/blog/images/google-microformat-results-review.png)


... is enough to convince me that microformats are a step in the right direction. Warts and all. While we’re waiting for HTML5 and [its mythical data attributes](http://ejohn.org/blog/html-5-data-attributes/) to ship sometime this century, it’s better than nothing.

[microformats](https://blog.codinghorror.com/tag/microformats/)
[data formats](https://blog.codinghorror.com/tag/data-formats/)
[software development](https://blog.codinghorror.com/tag/software-development/)
[web development](https://blog.codinghorror.com/tag/web-development/)
[user experience](https://blog.codinghorror.com/tag/user-experience/)
