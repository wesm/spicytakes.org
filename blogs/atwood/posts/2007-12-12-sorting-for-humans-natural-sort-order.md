---
title: "Sorting for Humans : Natural Sort Order"
date: 2007-12-12
url: https://blog.codinghorror.com/sorting-for-humans-natural-sort-order/
slug: sorting-for-humans-natural-sort-order
word_count: 748
---

The default sort functions in almost every programming language are **poorly suited for human consumption**. What do I mean by that? Well, consider the difference between sorting filenames in Windows explorer, and sorting those very same filenames via `Array.Sort()` code:

kg-card-begin: html


| Explorer shell sort | `Array.Sort()` |
|  |  |


kg-card-end: html

Quite a difference.


I can say without the slightest hint of exaggeration that **this exact sorting problem has been a sore point on every single project I’ve ever worked on**. Users will inevitably complain that their items aren’t sorting properly, and file bugs on these “errors.” Being card-carrying members of [the homo logicus club](https://blog.codinghorror.com/the-rise-and-fall-of-homo-logicus/), we programmers produce a weary sigh, and try to keep any obvious eye-rolling in check as we patiently inform our users that this *isn’t* an error. Items *are* sorting in proper order. Proper *ASCII* order, that is. As we’re walking away, hopefully you won’t hear us mutter under our breath what we’re actually thinking – “Stupid users! They don’t even understand how sorting works!”


I always felt a pang of regret when rejecting these requests. Honestly, look at those two lists – **what sane person would want ASCII order?** It’s a completely nonsensical ordering to anyone who doesn’t have [the ASCII chart](https://web.archive.org/web/20071224045314/http://www.cdrummond.qc.ca/cegep/informat/Professeurs/Alain/files/ascii.htm) committed to memory (and by the way, uppercase A is decimal 65). I never really understood that there was another way to sort, even though natural sort has been right in front of us all along in the form of Mac Finder and Windows Explorer file listings. I had language-induced blinders on. If our built-in `sort` returns in ASCII order, then that must be correct. It was bequeathed upon us by the Language Gods. Can there *be* any other way?


Kate Rhodes is a bit up in arms about our collective ignorance of [ASCIIbetical vs. Alphabetical](http://weblog.masukomi.org/2007/12/10/alphabetical-asciibetical). Can’t say I blame her. I’m as guilty as anyone. Turns out the users weren’t the stupid ones after all – *I was*.


> Silly me, I just figured that alphabetical sorting was such a common need (judging by the number of people asking how to do it I’m not wrong either) that I wouldn’t have to write the damn thing. But I didn’t count on the stupid factor. Jesus Christ people. You’re programmers. You’re almost all college graduates and none of you know what the f**k “Alphabetical” means. You should all be ashamed. If any of you are using your language’s default sort algorithm, which is almost guaranteed to be ASCIIbetical (for good reason) to get alphabetical sorting you proceed to the nearest mirror and slap yourself repeatedly before returning to your desks and fixing your unit tests that didn’t catch this problem.


It isn’t called “Alphabetical sort”; it’s collectively known as **natural sort**. But she’s right about one thing: it’s hard to find information on natural sorting, and many programmers are completely ignorant of it. None of the common computer languages (that I know of) implement anything other than ASCIIbetical sorts. There are a few places you can find natural sort algorithms, however:

- Dave Koelle’s [The Alphanum Algorithm](https://web.archive.org/web/20080116232902/http://www.davekoelle.com/alphanum.html)
- Martin Pool’s [Natural Order String Comparison](http://sourcefrog.net/projects/natsort/)
- Ian Griffiths’ [Natural Sorting in C#](http://www.interact-sw.co.uk/iangblog/2007/12/13/natural-sorting)
- Ned Batchelder’s [Compact Python Human Sort](https://web.archive.org/web/20071217042318/http://nedbatchelder.com/blog/200712.html#e20071211T054956), along with Jussi Salmela’s [internationalized version](https://web.archive.org/web/20071217033719/http://personal.inet.fi/cool/operator/Human%20Sort.py) of same.


Don’t let Ned’s clever Python ten-liner fool you. Implementing a natural sort is more complex than it seems, and not just for [the gnarly i18n](https://blog.codinghorror.com/software-internationalization-sims-style/) issues I’ve hinted at, above. But the Python implementations are impressively succinct. One of Ned’s commenters posted this version, which is even shorter:

kg-card-begin: html

```

import re
def sort_nicely( l ):
""" Sort the given list in the way that humans expect.
"""
convert = lambda text: int(text) if text.isdigit() else text
alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
l.sort( key=alphanum_key )

```

kg-card-end: html

I tried to come up with a clever, similarly succinct C# 3.0 natural sort implementation, but I failed. I’m not interested in a one-liner contest, necessarily, but it does seem to me that a basic natural sort shouldn’t require the 40+ lines of code it takes in most languages.


As programmers, we’d do well to keep Kate’s lesson in mind: **ASCIIbetical does not equal alphabetical**. ASCII sorting serves the needs of the computer and the compiler, but what about us human beings? **Perhaps a more human-friendly natural sort option should be built into mainstream programming languages**, too.

[sorting algorithms](https://blog.codinghorror.com/tag/sorting-algorithms/)
[natural sort order](https://blog.codinghorror.com/tag/natural-sort-order/)
[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[user experience](https://blog.codinghorror.com/tag/user-experience/)
