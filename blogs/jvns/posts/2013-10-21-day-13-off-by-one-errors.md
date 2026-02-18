---
title: "Day 13: Off by one errors"
date: 2013-10-21
url: https://jvns.ca/blog/2013/10/21/day-13-off-by-one-errors/
slug: day-13-off-by-one-errors
word_count: 68
---


Today I spent most of the day figuring out that


```
n_to_read = head.hlit + head.hdist + 257

```


should be


```
n_to_read = head.hlit + head.hdist + 258

```


And I still don’t know why, exactly. In related news, I can now *almost*
decompress gzipped files.


I think the life lesson here is “sometimes it takes forever to figure
things out and it is no fun” :)
