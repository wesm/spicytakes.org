---
title: "C# implementation of ASCII85"
date: 2005-10-07
url: https://blog.codinghorror.com/c-implementation-of-ascii85/
slug: c-implementation-of-ascii85
word_count: 181
---

As promised, here is my C# implementation of the ASCII85 algorithm. This code is a loose port of the C sample referenced from [the Wikipedia page](http://en.wikipedia.org/wiki/Ascii85). It’s too much code to paste into a single entry, so I packaged it as a VS.NET 2003 solution – using [Clean Sources Plus](https://blog.codinghorror.com/clean-sources-plus/), of course!

- [VS.NET 2003 ASCII85 console solution](https://github.com/coding-horror/ascii85) (4kb)


This includes both encoding and decoding, with reasonable data validation and a few minor options. Here’s a quick list of the public methods:

kg-card-begin: html

```
Encode(byte[] ba)
Decode(string s)

```

kg-card-end: html

And a handful of properties:

kg-card-begin: html

```

EnforceMarks (bool)
LineLength (int)
PrefixMark (string)
SuffixMark (string)

```

kg-card-end: html

The sample app includes a basic test harness which tests string and binary file encoding, as well as some bad data scenarios. Here’s the default demo running against the vaguely creepy [Wikipedia slogan](http://en.wikipedia.org/wiki/Wikipedia:Logos_and_slogans):


![](https://blog.codinghorror.com/content/images/2025/03/image-302.png)


Of course, converting printable text to, er... printable text... isn’t exactly an earth-shattering demo. Normally you’d be doing this on some kind of real binary data, as in the [GUID.ToByteArray() example](https://blog.codinghorror.com/equipping-our-ascii-armor/).

[c#](https://blog.codinghorror.com/tag/c-2/)
[encoding](https://blog.codinghorror.com/tag/encoding/)
[decoding](https://blog.codinghorror.com/tag/decoding/)
[ascii85](https://blog.codinghorror.com/tag/ascii85/)
[algorithm](https://blog.codinghorror.com/tag/algorithm/)
