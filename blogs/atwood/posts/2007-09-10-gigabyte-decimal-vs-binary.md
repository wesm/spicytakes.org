---
title: "Gigabyte: Decimal vs. Binary"
date: 2007-09-10
url: https://blog.codinghorror.com/gigabyte-decimal-vs-binary/
slug: gigabyte-decimal-vs-binary
word_count: 739
---

Everyone who has ever purchased a hard drive **finds out the hard way that there are two ways to define a gigabyte.**


When you buy a “500 Gigabyte” hard drive, the vendor defines it using the **decimal** **powers of ten definition** of the “Giga” prefix.

kg-card-begin: html

```
500 * 109 bytes = 500,000,000,000 = 500 Gigabytes

```


kg-card-end: html
But the operating system determines the size of the drive using the computer’s **binary powers of two definition** of the “Giga” prefix:
kg-card-begin: html

465 * 230 bytes = 499,289,948,160 = 465 Gigabytes


kg-card-end: html
If you’re wondering where 35 Gigabytes of your 500 Gigabyte drive just disappeared to, you’re not alone. It’s an old trick perpetuated by hard drive makers – they intentionally use [the official SI definitions](http://en.wikipedia.org/wiki/SI_prefix) of the Giga prefix so they can inflate the the sizes of their hard drives, at least on paper. This was always an annoyance, but now it’s much more difficult to ignore, as it results in large discrepancies with today’s enormous hard drives. When is a Terabyte hard drive not a Terabyte? When it’s 931 GB.As [Ned Batchelder notes](http://www.nedbatchelder.com/blog/index.html), the hard drive manufacturers are technically conforming to the letter of the SI prefix definitions. It’s us computer science types who are abusing the official prefix designations:
kg-card-begin: html




Year Approved
Official Definition
Informal Meaning
Difference
Prefix Derived From


[giga](http://en.wikipedia.org/wiki/Gigabyte)
GB
1960
109
230
7%
Greek root for giant


[tera](http://en.wikipedia.org/wiki/Terabyte)
TB
1960
1012
240
10%
Greek root for monster


[peta](http://en.wikipedia.org/wiki/Petabyte)
PB
1975
1015
250
13%
Greek root for five, "penta"


[exa](http://en.wikipedia.org/wiki/Exabyte)
EB
1975
1018
260
15%
Greek root for six, "hexa"


[zetta](http://en.wikipedia.org/wiki/Zettabyte)
ZB
1991
1021
270
18%
Latin root for seven, "septum", p dropped, first letter changed to S to avoid confusion with other SI symbols


[yotta](http://en.wikipedia.org/wiki/Yottabyte)
YB
1991
1024
280
21%
Greek root for eight, "octo", c dropped, y added to avoid having symbol of zero-like letter O


kg-card-end: html
As the size of the prefix grows, so does the gap between the official and informal meaning of the prefix. And yes, there are [larger official SI prefixes](http://www.lewrockwell.com/orig/kinsella6.html) beyond these, just in case someone needs [more than 1000 yottabytes](http://worsethanfailure.com/Articles/Just_In_Case_It_0x27_s_Needed.aspx). Ned noted that one of the SI proposals is for the prefix “luma,” representing 1063.Speaking of impossibly large numbers, if you’re like most people reading this article, then you probably arrived here through Google. Google is a tragically but [forever ](http://graphics.stanford.edu/~dk/google_name_origin.html)[misspelled version of Googol](http://graphics.stanford.edu/~dk/google_name_origin.html):A [googol](http://en.wikipedia.org/wiki/Googol) is 10100, i.e. a 1 followed by 100 zeros. In official SI prefix terms, a googol is approximately a yotta squared, squared. Even larger is the googolplex, which is equal to 10 to the power of a googol (10googol); this number is about the same size as the number of possible games of chess. Even larger numbers have been defined, such as [Skewes’ number](http://en.wikipedia.org/wiki/Skewes'_number), [Graham’s number](http://en.wikipedia.org/wiki/Graham's_number), and the [Moser](http://en.wikipedia.org/wiki/Steinhaus%E2%80%93Moser_notation), which I won’t even try to describe.But I digress. When we use gigabyte to mean 230, that’s an inaccurate and informal usage. Instead, we’re *supposed* to be using the more accurate and disambiguated [IEC](https://web.archive.org/web/20070917003203/http://www.iec.ch/) prefixes. They were introduced in 1998 and formalized with [IEEE 1541](http://en.wikipedia.org/wiki/IEEE_1541) in 2000.
kg-card-begin: html
[kibibyte](http://en.wikipedia.org/wiki/Kibibyte)KiB210[mebibyte](http://en.wikipedia.org/wiki/Mebibyte)MiB220[gibibyte](http://en.wikipedia.org/wiki/Gibibyte)GiB230[tebibyte](http://en.wikipedia.org/wiki/Tebibyte)TiB240[pebibyte](http://en.wikipedia.org/wiki/Pebibyte)PiB250[exbibyte](http://en.wikipedia.org/wiki/Exbibyte)EiB260[zebibyte](http://en.wikipedia.org/wiki/Zebibyte)ZiB270[yobibyte](http://en.wikipedia.org/wiki/Yobibyte)YiB280
kg-card-end: html
You occasionally see these more correct prefixes used in software, but adoption has been slow at best. There are several problems:**They sound ridiculous**. I hear the metric system used more often in the United States than I hear the words “kibibyte” or “mebibyte” uttered by anyone with a straight face. Which is to say, never.**Hard drive manufacturers won’t use them.** Drive manufacturers don’t care about being correct. What they do care about is consumers buying their drives because they have the largest possible number plastered on the front of the box. If a big lawsuit wasn’t enough to get them to mend their ways, I seriously doubt that the recommendation of an international standards body is going to sway them.**Tradition rules**. It’s hard to give up on the [rich binary history](http://en.wikipedia.org/wiki/Binary_prefix) of kilobytes, megabytes, and gigabytes, particularly when the alternatives are so questionable.It’s good to keep in mind **the discrepancy between the decimal and binary meanings of the SI prefixes**. The difference can bite you if you’re not careful. But I think we’re stuck with contextual, dual-use meanings of the SI prefixes for the foreseeable future. Or perhaps we’re all overthinking this, as Alan Green notes:Whenever I try to discuss [this] with my friends, they say, “Yotta getta life.”

[storage](https://blog.codinghorror.com/tag/storage/)
[binary](https://blog.codinghorror.com/tag/binary/)
[decimal](https://blog.codinghorror.com/tag/decimal/)
[gigabyte](https://blog.codinghorror.com/tag/gigabyte/)
[operating system](https://blog.codinghorror.com/tag/operating-system/)
