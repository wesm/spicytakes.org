---
title: "A Spec-tacular Failure"
date: 2006-08-04
url: https://blog.codinghorror.com/a-spec-tacular-failure/
slug: a-spec-tacular-failure
word_count: 931
---

I’ve written before about the dubious value of [functional specifications](https://blog.codinghorror.com/dysfunctional-specifications/). If you want to experience the dubious value of specifications first hand, try writing a tool to read and write [ID3 tags](https://web.archive.org/web/20061115013701/http://www.id3.org/).


ID3 tags describe the metadata for an MP3 file, such as Artist, Album, Track, and so forth. ID3 tags certainly don’t *look* all that complicated. Newer versions appear at the beginning of the MP3 file, and are nearly human readable even in a hex editor:


![](https://blog.codinghorror.com/content/images/2025/04/image-740.png)


There’s a set of [comprehensive ID3 specifications](https://web.archive.org/web/20061115014018/http://www.id3.org/develop.html) to help us out. **Unfortunately the ID3 specs are, in a word, *bad***.


Even with a bad spec, you can write code to parse ID3 tags. There are a number of CodeProject articles that [read and write ID3 tags](https://web.archive.org/web/20070321141942/http://www.codeproject.com/info/search.asp?searchkw=id3) with varying levels of success. There’s also a mature .NET ID3 library available, UltraID3Lib, but unfortunately it’s closed source. It also suffers a little from [explosion at the pattern factory](https://blog.codinghorror.com/head-first-design-patterns/) design.


One of the first big warning signs is [this list of ID3 “offenders](https://web.archive.org/web/20061206112028/http://home.fuse.net/honnert/hundred/?UltraID3Lib)” on the UltraID3Lib site. It reads like a who’s who of music applications: iTunes, WinAmp, Windows Media Player. **If the applications that ship with the operating system can’t get ID3 tags right, clearly something is wrong.**


And that something is the ID3 spec. How does it suck? Let me count the ways:

- **The spec shows how but rarely explains why.** For example, frame sizes are stored as 4-byte “syncsafe integers” where the 8th bit of every byte is zeroed. Why would you store size in such an annoying, unintuitive format? Who knows; the spec doesn’t explain. You just grit your teeth and do it.
- **The vast majority of the things described in the spec do not appear in any MP3 files that I can find or create.** There are 70+ possible frame types, but I’ve only seen a dozen or so in practice. And what about encryption? Compression? CRC checks? Footers? Extended headers? Never seen ’em. And I probably never will. But I still have to parse through pages and pages of detailed text about these extremely rare features.
- **The spec has ridiculous enumerations.** Check out the 147 possible values of [the music genre byte](https://web.archive.org/web/20060717221144/http://lame.sourceforge.net/doc/html/id3.html). The existing 147 categories seem to be chosen completely at random. For example, “Negerpunk” (133), “Christian Rap” (61), and “Native US” (64). And evidently “Primus” (108) isn’t just a band, they’re a valid music genre, too. iTunes thankfully puts a stop to this madness by only displaying a fraction of these genres in its genre drop-down. And it isn’t just the genre tag; one of the possible picture types for the attached picture tag “APIC” is – and I swear I’m not making this up – “A bright coloured fish” ($11). At some point you feel like you’re wasting your time by enumerating insanity.
- **No examples are provided**. Consider the comment frame. This is a relatively complex frame; it supports multiple languages and different encodings. It also supports multiple comments per frame with descriptive labels for each one. And yet it only merits a paragraph in the [frames specification](https://web.archive.org/web/20061112214843/http://www.id3.org/id3v2.4.0-frames.txt), with no examples of usage whatsoever. Would it kill them to provide a couple examples of how a comment should actually look?
- **Related items are not together.** The comment frame has two lookups in its header: language and text encoding. There is absolutely no reference at all to these lookup tables in the comment frame description. You have to “just know” that the main ID3 spec defines all languages with three character ISO-639-2 language codes, and that there are four possible text encodings from 00 to 03, with different rules for null termination. It’d be awfully difficult to write a comment tag reader without this information, yet it’s nowhere to be found in the description of the comment tag.


The ID3 spec is doubly frustrating because it makes a simple topic difficult. **ID3 tags are just not that complicated**. The spec makes me feel like an idiot for not being able to get this stuff right. *What’s the matter? Can’t you read the spec?*


No. I can’t. And evidently, neither could the developers of WinAmp, iTunes, or Windows Media Player.


Since the ID3 spec is so deficient, **I’ve been using the behavior of popular applications as a de-facto spec**. In other words, I test to see how WinAmp behaves when editing ID3 tags:


![](https://blog.codinghorror.com/content/images/2025/04/image-741.png)


WinAmp isn’t a model ID3 tag citizen. It ignores all comments except for the first one, and it adds garbage text as the language string for comments.


I also test to see how iTunes behaves when editing ID3 tags:


![](https://blog.codinghorror.com/content/images/2025/04/image-742.png)


Although iTunes reads all versions of ID3 tags, it still writes ancient v2.2 ID3 tags to MP3 files, even in the latest version. So it’s an especially poor role model for tagging.


Warts and all, **the practical implementations of ID3 tags in popular applications like WinAmp and iTunes trump anything that’s written in the formal ID3 spec.** I finally understand what [Linus Torvalds was complaining about](https://web.archive.org/web/20071211010115/http://kerneltrap.org/node/5725):


> A “spec” is close to useless. I have never seen a spec that was both big enough to be useful and accurate. And I have seen lots of total crap work that was based on specs. It’s the single worst way to write software, because it by definition means that the software was written to match theory, not reality.


Specs, if they’re well-written, can be useful. But they probably won’t be. **The best functional spec you’ll ever have is the behavior of real applications.**

[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[metadata](https://blog.codinghorror.com/tag/metadata/)
[id3 tags](https://blog.codinghorror.com/tag/id3-tags/)
[specifications](https://blog.codinghorror.com/tag/specifications/)
