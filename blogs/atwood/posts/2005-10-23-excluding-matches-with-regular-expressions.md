---
title: "Excluding Matches With Regular Expressions"
date: 2005-10-23
url: https://blog.codinghorror.com/excluding-matches-with-regular-expressions/
slug: excluding-matches-with-regular-expressions
word_count: 292
---

Here’s [an interesting regex problem](https://web.archive.org/web/20060106112920/http://techreport.com/forums/viewtopic.php?t=34782):


> I seem to have stumbled upon a puzzle that evidently is not new, but for which no (simple) solution has yet been found. I am trying to find a way to exclude an entire word from a regular expression search. The regular expression should find and return everything EXCEPT the text string in the search expression.
> For example, if the word fox was what I wanted to exclude, and the searched text was:
> The quick brown fox jumped over the lazy dog.
> ... and I used a regular expression of [^“fox”] (which I know is incorrect) (why this doesn’t work I don’t understand; it would make life SO much easier), then the returned search results would be:
> The quick brown jumped over the lazy dog.


Regular expressions are great at matching. It’s easy to formulate a regex using what you want to match. **Stating a regex in terms of what you *don’t* want to match is a bit harder.**


One easy way to exclude text from a match is [negative lookbehind](http://www.regular-expressions.info/lookaround.html):

kg-card-begin: html

```

w+b(?<!bfox)

```

kg-card-end: html

But not all regex flavors support negative lookbehind. And those that do typically have severe restrictions on the lookbehind, eg, it must be a simple fixed-length expression. To avoid incompatibility, we can restate our solution using negative lookahead:

kg-card-begin: html

```

(?!foxb)bw+

```

kg-card-end: html

You can test this regex in the cool [online JavaScript Regex evaluator](https://web.archive.org/web/20131209121230/http://www.cuneytyilmaz.com/prog/jrx/). Unfortunately, JavaScript doesn’t support negative lookbehind, so if you want to test that one, I recommend [RegexBuddy](http://www.regexbuddy.com). It’s not free, but it’s the best regex tool out there by far– and it keeps getting better with every incremental release.

[regex](https://blog.codinghorror.com/tag/regex/)
[regular expressions](https://blog.codinghorror.com/tag/regular-expressions/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[text processing](https://blog.codinghorror.com/tag/text-processing/)
