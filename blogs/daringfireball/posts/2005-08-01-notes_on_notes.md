---
title: "Notes on Notes"
date: 2005-08-01
url: https://daringfireball.net/2005/08/notes_on_notes
slug: notes_on_notes
word_count: 654
---


## Sidenotes


In addition to bottom-of-the-article footnotes, *sidenotes* (a.k.a.
*margin notes*) can also work well on the web. Two recent
implementations struck me as well-done.

- [Brand Spanking New’s sidenotes](http://www.brandspankingnew.net/archive/2005/07/css_footnotes_r.html) implementation uses CSS
and JavaScript to present notes in the sidebar, in a fixed
position on the page, when you click on the note reference in the
main text. (See the demo [here](http://www.brandspankingnew.net/specials/footnote_3.html).)
- [Beau Hartshorne’s sidenotes](http://www.hartshorne.ca/2005/07/27/footnotes_v_sidenotes/) are simpler, requiring only CSS,
with no scripting or hacks to workaround deficiencies in Internet
Explorer. In Hartshorne’s implementation, each note is displayed
in the sidebar next to the text it references.


I chose a footnote-style design here for Daring Fireball, but I like 
sidenotes, too. In particular, I prefer both footnotes and sidenotes
over pop-up and tooltip-style inline notes. No, the web is not print,
but that doesn’t mean web designers can’t build upon and learn from
traditional typography and print design. Both footnotes and sidenotes
are well-represented in good design from the past few hundred years.


The primary advantage to sidenotes vs. footnotes is that their
placement — next to the text they’re referencing — obviates the
entire problem I addressed when I [wrote about my own footnotes](http://daringfireball.net/2005/07/footnotes)
last week. There is no need to design anything to help the reader
figure out what part of the main text each note applies to.


But this spatial relationship also leads to the primary disadvantage
to sidenotes: a long passage of text in a sidenote prevents you from
placing a second note in close proximity to the first. So sidenotes
work best if your notes are short, whereas footnotes work equally well
for long and short notes.


## Other Comments


[Joe Clark wrote about my footnotes](http://blog.fawny.org/2005/07/24/footnote/) to (a) bemoan the fact that
HTML has no tags to truly mark up notes (footnotes, sidenotes,
whatever) as notes; (b) argue that my footnotes aren’t innovative,
“but merely a ‘Back to Top of Page’ link in sequined cocktail dress
and rouge”; and (c) argue that I chose the wrong arrow glyphs to use
as the “back” markers.


I agree with Clark on (a) — that there exists no HTML tag syntax
specifically appropriate for notes is a glaring omission, and but one
that standards wonks don’t seem to care about.


As for (b), I never claimed my design was innovative. In fact, the
reason I like it is that it seems rather obvious and quite
traditional. The only aspect that might have even a whiff of
innovation is the use of ‘↩’ (the Unicode left arrow with hook) as a
dingbat representing the back-to-where-the note-was-referenced link. I
love using Unicode characters for purposes such as this (e.g. my use
of ‘★’ as the permalink marker for [Linked List](http://daringfireball.net/linked/) entries) — it
feels like a cross between punctuation and iconography.


But I can’t say this is innovative, either. The only reason these
characters exist in Unicode is that they’re supposed to be, well,
used. But they’re not commonly used on the web because most existing
installations of Microsoft Windows can’t display them properly. I just
don’t care, at least here on Daring Fireball, but most designers
working on most web sites don’t have that luxury.


Regarding point (c), that I chose the wrong arrow, Clark writes:


> we are not hooking and moving leftwards; we’re going *straight up* ↑


Only here must I disagree completely with Clark. I chose ‘↩’ not
because it implies moving *left*, but because it implies moving
*back*. And a left-pointing arrow has meant “back” ever since
[Mosaic](http://archive.ncsa.uiuc.edu/SDG/Software/MacMosaic/Documentation/Quickstart.html). I chose the hooked arrow, instead of, say,’←’ or ‘⇠’, simply
because it felt right. But even here with this choice, it’d take a
bigger ego than mine to lay claim to any innovation, when Apple has
been using this hooked arrow:


for Safari’s SnapBack feature ever since the Safari public beta.



| **Previous:** | [Location Validation in the Dashboard Weather Widget](https://daringfireball.net/2005/07/weather_widget_location) |
| **Next:** | [Trusted](https://daringfireball.net/2005/08/trusted) |


PreviousNext