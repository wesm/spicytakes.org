---
title: "Title Case"
date: 2008-05-20
url: https://daringfireball.net/2008/05/title_case
slug: title_case
word_count: 490
---


Here’s one of the little tools I’ve written to help publish DF which I’ve never gotten around to sharing: an ostensibly clever script for converting text to title case. I use it to standardize the capitalization of Linked List headlines, for example.


[Here’s the source code.](http://daringfireball.net/projects/titlecase/TitleCase.pl)


[**Update, 13 August 2008:** Thanks to Aristotle Pagaltzis, the script has now been improved in several ways. See [here](http://daringfireball.net/2008/08/title_case_update) for details.]


It’s a Perl script, so save it as a text file and you can use it anywhere where Perl works. I use it as a system-wide service (with the shortcut Command-Shift-T) via [Jesper’s excellent (and free) ThisService utility](http://wafflesoftware.net/thisservice/).


It’s pretty easy to write a non-clever title-casing function. The simplest way is to just capitalize the first letter of every word. That’s not right, though, because it’ll leave you with capitalized small words like *if*, *in*, *of*, *on*, etc. What you want is something that not only knows not to capitalize such words, but will *un*-capitalize them if they’re erroneously capitalized in the input.


So, some of the cleverness in this script:

- It knows about small words that should not be capitalized. Not all style guides use the same list of words — for example, many lowercase *with*, but I do not. The list of words is easily modified to suit your own taste/rules:
`my @small_words = qw(a an and as at but by en for if in of
                    on or the to v[.]? via vs[.]?);
`
(The only trickery here is that “v” and “vs” include optional dots, expressed in regex syntax.)
- The script assumes that words with capitalized letters other than the first character are already correctly capitalized. This means it will leave a word like “iTunes” alone, rather than mangling it into “ITunes” or, worse, “Itunes”.
- It also skips over any words with line dots; “example.com” and “del.icio.us” will remain lowercase.
- It has hard-coded hacks specifically to deal with odd cases I’ve run into, like “AT&T” and “Q&A”, both of which contain small words (*at* and *a*) which normally should be lowercase.
- The first and last word of the title are always capitalized, so input such as “Nothing to be afraid of” will be turned into “Nothing to Be Afraid Of”.
- A small word after a colon will be capitalized.


[Here’s a small list of edge cases](http://daringfireball.net/projects/titlecase/examples-edge-cases) that the script handles.


The source code itself is, uh, rather convoluted, to say the least. It’s one of those pieces of code that started small and simple, and grew ugly over time as edge cases were worked around one at a time. I’ve been using this script for *years*, but have put off publishing it on the grounds that it looks like the sort of punctuation-riddled code that gives Perl phobics the heebie-jeebies.


But it works, so screw it, here it is.



| **Previous:** | [Why Apple Won’t Buy Adobe](https://daringfireball.net/2008/05/why_apple_wont_buy_adobe) |
| **Next:** | [Sixty-Six](https://daringfireball.net/2008/05/sixtysix) |


PreviousNext