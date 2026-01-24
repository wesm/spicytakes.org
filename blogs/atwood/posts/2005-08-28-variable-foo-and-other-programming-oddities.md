---
title: "Variable “foo” and Other Programming Oddities"
date: 2005-08-28
url: https://blog.codinghorror.com/variable-foo-and-other-programming-oddities/
slug: variable-foo-and-other-programming-oddities
word_count: 722
---

If you’ve ever viewed UNIX documentation, you’ve probably encountered variables foo and bar at some point. Here’s a Ruby example I found in the newsgroups:

kg-card-begin: html

```

foo = 0
bar = 0

1.times do
  foo = 1
  foo := 2
  bar = foo+1
end

puts foo, bar

```

kg-card-end: html

[O’Reilly’s FooCamp](https://en.wikipedia.org/wiki/Foo_Camp) ostensibly means “Friends of O’Reilly” but is probably a pun on this same meaningless variable. So why “foo”? I always thought foo and bar were corruptions of the phrase [FUBAR](https://en.wikipedia.org/wiki/List_of_military_slang_terms#FUBAR), but according to the jargon file, [that’s not correct](http://www.catb.org/~esr/jargon/html/F/foo.html):


> When ‘foo’ is used in connection with ‘bar’ it has generally traced to the WWII-era Army slang acronym FUBAR (‘F*cked Up Beyond All Repair’ or ‘F*cked Up Beyond All Recognition’), later modified to foobar. Early versions of the Jargon File interpreted this change as a post-war bowdlerization, but it it now seems more likely that FUBAR was itself a derivative of ‘foo’ perhaps influenced by German furchtbar (terrible) – ‘foobar’ may actually have been the original form.
> For, it seems, **the word ‘foo’ itself had an immediate prewar history in comic strips and cartoons**. The earliest documented uses were in the Smokey Stover comic strip published from about 1930 to about 1952. Bill Holman, the author of the strip, filled it with odd jokes and personal contrivances, including other nonsense phrases such as “Notary Sojac” and “1506 nix nix.” The word “foo” frequently appeared on license plates of cars, in nonsense sayings in the background of some frames (such as “He who foos last foos best” or “Many smoke but foo men chew”), and Holman had Smokey say “Where there’s foo, there’s fire.”


Then there are [GUI widgets](https://en.wikipedia.org/wiki/Widget_(GUI)). I know the word predates computers as a generalized business school expression of “some unit of produced goods,” e.g., from [ACME Corporation](https://en.wikipedia.org/wiki/Acme_Corporation). But where did the word “widget” [come from](http://alt-usage-english.org/excerpts/fxwidget.html)?

kg-card-begin: html

> “Widget” is a deliberately invented word meant (probably) to suggest “gadget.” Most dictionaries fail to trace it to its origin. **It comes from the 1924 play “Beggar on Horseback,” by George Kaufman and Marc Connelly.** In the play, a young composer gets engaged to the daughter of a rich businessman, and the next part of the play acts out his nightmare of what his life will be like, doing pointless work in a bureaucratic big business. At one point he encounters his father-in-law at work, and we get the following dialogue:
> (Father-in-law): Yes, sir!  Big business!
> Yes. Big business. What business are we in?
> Widgets.  We're in the widget business.
> The widget business?
> Yes, sir!  I suppose I'm the biggest manufacturer in the world of overhead and underground aerial widgets.
> Part of the point, of course, is that no one ever tells him what "widgets" are.

kg-card-end: html

A play, of all things. It certainly must have been popular in the 1920s for this weird little word to catch on; a google search reveals a bunch of hits for recent productions of Beggar on Horseback.


The [Beagle Brothers](http://en.wikipedia.org/wiki/Beagle_Bros) were one of my [favorite](https://blog.codinghorror.com/our-programs-are-fun-to-use/) Apple // software vendors. They had disks chock full of crazy little programs and demos, all written in Applesoft BASIC. In many of these apps the sentence “Pack my box with five dozen liquor jugs” appears. Just more Beagle Brothers zaniness, I thought. Years later, I realized what this phrase actually is. It’s a [pangram](https://en.wikipedia.org/wiki/Pangram): it uses **all 26 letters of the alphabet in a single sentence**.


The Wikipedia entry notes that pangrams are typically used in font sample apps. That’s what launches in Windows when you double-click on a font in the c:windowsfonts folder. Here are a few examples:

kg-card-begin: html


| How razorback-jumping frogs can level six piqued gymnasts! | Mac, System 7 era |
| Cozy lummox gives smart squid who asks for job pen | Mac, post-System 7 era |
| The quick brown fox jumps over the lazy dog | Windows, truetype fonts |
| Pack my box with five dozen liquor jugs | Beagle Bros fonts |
| Jackdaws love my big sphinx of quartz | Windows, bitmap fonts |


kg-card-end: html

![](https://blog.codinghorror.com/content/images/2025/05/image-131.png)


The pangram Beagle Bros chose is a great expression of their homebrew spirit: it’s rather clever *and* it involves alcohol.

[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[ruby](https://blog.codinghorror.com/tag/ruby/)
[unix](https://blog.codinghorror.com/tag/unix/)
[variable naming](https://blog.codinghorror.com/tag/variable-naming/)
[jargon file](https://blog.codinghorror.com/tag/jargon-file/)
