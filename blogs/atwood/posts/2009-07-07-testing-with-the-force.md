---
title: "Testing With “The Force”"
date: 2009-07-07
url: https://blog.codinghorror.com/testing-with-the-force/
slug: testing-with-the-force
word_count: 808
---

Markdown was one of the [humane markup languages](https://blog.codinghorror.com/is-html-a-humane-markup-language/) that we evaluated and adopted for Stack Overflow. I’ve been pretty happy with it, overall. So much so that I wanted to implement a tiny, lightweight subset of Markdown for comments as well.


I settled on these three commonly used elements:

kg-card-begin: html

```

*italic* or _italic_
**bold** or __bold__
`code`

```

kg-card-end: html

I [loves me some regular expressions](https://blog.codinghorror.com/regular-expressions-now-you-have-two-problems/) and this is exactly the stuff regex was born to do! It doesn’t *look* very tough. So I dusted off [my copy of RegexBuddy](http://www.regexbuddy.com) and began.


I typed some test data in the test window, and whipped up a little regex in no time at all. This isn’t my first time at the disco.


![](https://blog.codinghorror.com/content/images/2025/04/image-399.png)


Bam! Yes! Done and *done!* By gum, I must [be a genius programmer!](https://web.archive.org/web/20090803043406/http://code.google.com/events/io/sessions/MythGeniusProgrammer.html)


Despite my obvious genius, I began to have some small, nagging doubts. Is the test phrase...

kg-card-begin: html

```

I would like this to be *italic* please.

```

kg-card-end: html

... *really* enough testing?


Sure it is! I can feel in my bones that this thing freakin’ works! It’s almost like I’m being pulled toward shipping this code by some inexorable, dark, testing... force. It’s so *seductively easy!*


![](https://blog.codinghorror.com/content/images/2025/04/image-398.png)


But wait. **I have this whole database of real world comments** that people have entered on Stack Overflow. shouldn’t I perhaps try my awesome regular expression on that corpus of data to see what happens? Oh, fine. If we must. Just to humor you, nagging doubt. Let’s run a query and see.

kg-card-begin: html

```

select Text from PostComments
where dbo.RegexIsMatch(Text, '*(.*?)*') = 1

```

kg-card-end: html

Which produced this list of matches, among others:

kg-card-begin: html

> Interesting fact about math: x * 7 == x + (x * 2) + (x * 4), or x + x >> 1 + x >> 2.  Integer addition is usually pretty cheap.
> Thanks.  What I needed was to turn on Singleline mode too, and use .*? instead of .*.
> yeah, see my edit - change select * to select RESULT.*  one row - are sure you have more than one row item with the same InstanceGUID?
> Not your main problem, but you are mix and matching wchar_t and TCHAR.  mbstowcs() converts from char * to wchar_t *.
> aawwwww... Brainf**k is not valid. :/

kg-card-end: html

Thank goodness I listened to my midi-chlorians and let **the light side of the testing force** prevail here!


![](https://blog.codinghorror.com/content/images/2025/04/image-397.png)


So how do we fix this regex? We use the light side of the force – brute force, that is, against a ton of test cases! My job here is relatively easy because I have over 20,000 test cases sitting in a database. You may not have that luxury. Maybe you’ll need to go out and find a bunch of test data on the internet somewhere. Or write a function that generates random strings to feed to the routine, also known as [fuzz testing](http://en.wikipedia.org/wiki/Fuzz_testing).


I wanted to leave the rest of this regular expression as an exercise for the reader, as I’m a sick guy who finds that sort of thing entertaining. If you don’t – well, what the heck is wrong with *you*, man? But I digress. I’ve been criticized for not providing, you know, “the answer” in my blog posts. Let’s walk through some improvements to our italic regex pattern.


First, let’s make sure we have **at least one non-whitespace character inside the asterisks**. And more than one character in total so we don’t match the ** case. We’ll use [positive lookahead and lookbehind](http://www.regular-expressions.info/lookaround.html) to do that.

kg-card-begin: html

```

*(?=S)(.+?)(?<=S)*

```

kg-card-end: html

That helps a lot, but we can test against our data to discover some other problems. We get into trouble when there are unexpected characters in front of or behind the asterisks, like, say, `p*q*r`. So let’s specify that **we only want certain characters outside the asterisks**.

kg-card-begin: html

```

(?<=[s^,(])*(?=S)(.+?)(?<=S)*(?=[s$,.?!])

```

kg-card-end: html

Run this third version against the data corpus, and wow, that’s starting to look pretty darn good! There are undoubtedly some edge conditions, particularly since we’re unlucky enough to be talking about code in a lot of our comments, which has wacky asterisk use.


This regex doesn’t have to be (and probably *cannot* be, given the huge possible number of human inputs) perfect, but running it against a large set of input test data gives me reasonable confidence that I’m not totally screwing up.


So by all means, test your code with the force – brute force! It’s good stuff! Just **be careful not to get sloppy, and let the dark side of the testing force prevail**. If you think one or two simple test cases covers it, that’s taking the easy (and most likely, buggy and incorrect) way out.

[regular expressions](https://blog.codinghorror.com/tag/regular-expressions/)
[markdown](https://blog.codinghorror.com/tag/markdown/)
[testing](https://blog.codinghorror.com/tag/testing/)
[software development](https://blog.codinghorror.com/tag/software-development/)
