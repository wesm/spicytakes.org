---
title: "About the Footnotes"
date: 2005-07-20
url: https://daringfireball.net/2005/07/footnotes
slug: footnotes
word_count: 670
---


I’ve been experimenting with the use of footnotes here on Daring
Fireball over the last few months.1
In print, implementing footnotes is rather straightforward: put the
note references in the text, then place the notes themselves in
smaller type at the bottom of the pages where the references occur.


In a weblog post, the implementation is not so obvious. It’s easy to
just put the note references in the text, in superscript, and make
them clickable links that jump to the notes themselves at the bottom
of the article. And that’s more or less all I did, originally.


The problem with this is that a weblog post — especially longish ones
like those here at Daring Fireball — is very different from a printed
page in a book. When you, i.e. the reader, encounter a footnote
reference in a book, you can glance down to the bottom of the current
page to read the note, then glance back up to your original position
in the text. You can do this because you have some short-term spatial
memory of where the footnote reference was — and all you have to do
is get close, visually, and your eyes will quickly spot the
superscript footnote reference.


But with a weblog post, there are no “pages”. It’s just one long
article that scrolls down continuously. By placing the notes at the
bottom of the article, they’re in some way more like endnotes than
footnotes. Assuming there’s a hyperlink from the superscript footnote
reference to the note itself, how do you get back to where you were
when you’re done reading the note?


It ends up you *can* use the browser Back button for this, but this
isn’t obvious, and it isn’t perfect. Because what if you (again, the
reader) decide to wait and read the notes *after* you’ve finished the
article, rather than reading them on-the-fly as you encounter the
references? It’d be nice to be able to figure out from the notes
themselves where they were referenced in the text.


So, here’s what I’ve come up with.


At the end of each footnote, I’ve included a link back to the spot in
the text where the note is referenced. Rather than add needless noise
to the page, instead of using a textual link, I’m simply using a bit
of Unicode typography:


↩


A.k.a. Unicode **LEFTWARDS ARROW WITH HOOK**, decimal-encoded HTML
entity `&#x21A9;`. Clicking on the arrow at the end of each note will
jump you back to the spot in the text where the note was referenced.
This works pretty well and looks pretty good, and it solves the “how
do you get back to the text from the footnote” problem concisely and
quietly.2


There are innumerable other ways footnotes — or footnote-esque asides — can be implemented on the web. Dynamic HTML techniques allow you to
toggle element visibility on the fly. I considered ideas for
displaying footnotes to the right of the main text column, and also
making them pop into place directly underneath the paragraph in which
they’re referenced. I’ve seen some sites which implement
footnote-esque asides as mouseover tooltips.


But I like the traditional placement at the bottom. It just feels
right to me. Plus, this design has the added benefit of requiring no
CSS or JavaScript whatsoever, just relative anchors, which means that
for Daring Fireball members who read the site via the [full-content
RSS feed](https://daringfireball.net/members/), the footnotes work in their feed aggregators. (At least
they work in NetNewsWire, which covers the overwhelming majority of
members who read the full-content feed.)


---

1. E.g. “[Font Caches Gone Wild](https://daringfireball.net/2005/03/font_caches_gone_wild)”.
↩︎
2. Of course, because it’s a Unicode character, the design assumes you’ve got a Unicode-savvy web browser and Unicode-savvy fonts installed on your system. Some users of pre-XP versions of Windows may just see a box instead of a hooked arrow. My heart bleeds.
↩︎



| **Previous:** | [Is That a Podcast in Your Pocket?](https://daringfireball.net/2005/07/podcast_pocket) |
| **Next:** | [Location Validation in the Dashboard Weather Widget](https://daringfireball.net/2005/07/weather_widget_location) |


PreviousNext