---
title: "How Fast Can Java Parse 1 Billion Rows of Temperature Data"
subtitle: "Gunnar Morling nerd snipes the internet into building Arrow in Java."
date: 2024-01-03T20:17:22+00:00
url: https://materializedview.io/p/how-fast-can-java-parse-1-billion-rows-1brc
slug: how-fast-can-java-parse-1-billion-rows-1brc
word_count: 337
---


Gunnar Morlinglaunched1brconhis blogthis week. 1brc, or “one billion row challenge”, is a seemingly simple task: use Java to parse 1 billion rows of temperature data and calculate the min, max, and mean for each city. The format is:


```
[city];[temperature]\n
```


Frederic Branczyk, founder ofPolar Signals, pointed out that 1brc isre-implementing part of Arrow. But Gunnar’s goal is to get us using new Java features likeSIMD,virtual threads, andZGC. He previously shared aJava Updatefor Java modernization efforts (most of this is available inJava 21):


![](https://substackcdn.com/image/fetch/$s_!VBqQ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa970f3df-480f-47cf-9afe-c36e89dbd59b_1700x900.png)


NVMe’s are insanely fast—it takes only a couple of seconds to read the 12 gigs of data on my M2. Most of the focus has been on speeding up the text parsing.


Developers are havinga lot of funtrying different strategies:

- Processing the file in parallel (one chunk per-core) (code)
- Memory mapping the temperature file (code)
- Implementing custom Hashtables/data structures (code)
- Using SIMD instead of .split() for text parsing (code)
- Using virtual threads (code)
- Lots of GC tuning (comment)
- GraalVM instead of the standard JVM


I was initially drawn to the project because of the opportunity to try out SIMD, somethingI’ve written about before.My own implementationclocks in at a measly 53 seconds. I never got around to adding SIMD.


Sam Pullarais the current leader at 14 seconds. Sam gets a lot of gains from custom text parsing and custom in-memory storage structure. He’sadding SIMDnow. Follow along or submit your own.


If you attempt this project, beware that hardware is quite variable. Sam’s implementation runs on his M3 in only2 seconds. On my M2it takes 12 seconds.


Gunnar opened up aShow and tellsection for those wishing to participate in other languages.


---


Share


---


You can support me by purchasingThe Missing README: A Guide for the New Software Engineerfor yourself or gifting it to new software engineers that you know.


Buy Now


---


I occasionally invest in infrastructure startups. Companies that I’ve invested in are marked with a [$] in this newsletter. See myLinkedIn profilefor a complete list.
