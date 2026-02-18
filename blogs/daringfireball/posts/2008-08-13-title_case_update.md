---
title: "Title Case Update"
date: 2008-08-13
url: https://daringfireball.net/2008/08/title_case_update
slug: title_case_update
word_count: 334
---


[**Update 9 August 2015:** The current version of my personal title casing script is available [here on Gist](https://gist.github.com/gruber/9f9e8650d68b13ce4d78).]


Back in May, [I published a Perl script](http://daringfireball.net/2008/05/title_case) I wrote for properly title-casing text. Its main trick was in being smart about “small words” that should not be capitalized even in title case.


I wrote:


> The source code itself is, uh, rather convoluted, to say the
> least. It’s one of those pieces of code that started small and
> simple, and grew ugly over time as edge cases were worked around
> one at a time. I’ve been using this script for *years*, but have
> put off publishing it on the grounds that it looks like the sort
> of punctuation-riddled code that gives Perl phobics the
> heebie-jeebies.


A slew of clever people took my script and ported it to other languages — [JavaScript](http://ejohn.org/blog/title-capitalization-in-javascript/), [Python](http://muffinresearch.co.uk/archives/2008/05/27/titlecasepy-titlecase-in-python/), [Ruby](http://samsouder.com/articles/2008/05/27/daring-fireballs-titlecase-ruby-conversion), [PHP](http://nanovivid.com/stuff/wordpress/title-case/), [Objective-C](http://www.vengefulcow.com/titlecase/), even [Nu](http://github.com/Grayson/nutitlecase/tree/master). Crackerjack work, one and all. But two stand out, at least for my own needs.


[David Gouch wrote his own version in JavaScript](http://individed.com/code/to-title-case/); his script handles all the edge conditions my script did, and also some others. He also published a [list of test cases and the results](http://individed.com/code/to-title-case/tests.html) of my original script, John Resig’s bug-for-bug port to JavaScript of my script, and Gouch’s superior solution. This is the best JavaScript solution I’ve seen; I’m using it in the bookmarklets I use for posting Linked List items.


Aristotle Pagaltzis was kind enough to take my Perl script and [refactored it in a straightforward and logical way](http://plasmasturm.org/code/titlecase/), fixing some of the edge conditions along the way. He took Gouch’s test cases and turned them into a proper [testing suite](http://github.com/ap/titlecase/tree/master%2Ftest.pl?raw=true). The result is better than my original script in every way, and his test suite can be used to improve any implementation.


My thanks to everyone who pitched in on these scripts, and to David Gouch and Aristotle Pagaltzis especially.



| **Previous:** | [Memoranda](https://daringfireball.net/2008/08/memoranda) |
| **Next:** | [Raining on the OpenClip Parade](https://daringfireball.net/2008/08/raining_on_the_openclip_parade) |


PreviousNext