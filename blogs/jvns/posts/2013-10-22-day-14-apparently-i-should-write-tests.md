---
title: "Day 14: When it's hard to write tests, that's when I should be testing"
date: 2013-10-22
url: https://jvns.ca/blog/2013/10/22/day-14-apparently-i-should-write-tests/
slug: day-14-apparently-i-should-write-tests
word_count: 332
---


So yesterday I was fighting with an off-by-one error most of the day.
And while it was happening, it was pretty upsetting. There was all this
code! And I had no idea where the problem was!


And I kept talking to people about it (Alan! Stefan! Sumana!), and
kept having conversations like


**Them:** “Do you have unit tests?”.


**Me:** “Some! But it’s complicated! I don’t really know what my output is supposed to be in the middle of the calculation, just the final result!”.


**Them:** “Oh yeah that makes sense it sounds tough”.


BUT! It turns out that when you’re not sure exactly what your code is
supposed to be doing or how to verify whether it’s correct is *exactly
when* it’s the most helpful to write unit tests.


And Stefan suggested an awesome way to fix it a little bit: I took the
C implementation of gunzip I was using as an example, put some print
statements in the middle, and then I had some reference data to check one of
the intermediate objects in my program against! It is
[here](https://github.com/jvns/gzip.jl/blob/master/test/code_lengths.txt).


The gunzip is part way to working now – I can decompress small files,
but there is still some kind of bug when I try to decompress a bigger
file. BUT I WILL FIX IT. And I’m thinking, if I write more tests, maybe
I’ll have a better handle on which parts of the code I’m confident and
which parts are more likely to be broken.


There is also a whole book on how to test when testing is hard called
[Working Effectively With Legacy Code](http://www.amazon.com/Working-Effectively-Legacy-Michael-Feathers/dp/0131177052).
I’ve read a little of it and it is pretty great. The chapter titles are
like “I Don’t Have Much Time and I Have to Change It” and “I Need To
Change A Monster Method And I Can’t Write Tests For It”.


Pretty much all the situations it describes are less tractable than my
gzip situation, so I pretty much have no excuses :)
