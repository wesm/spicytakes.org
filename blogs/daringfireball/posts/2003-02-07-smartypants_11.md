---
title: "SmartyPants 1.1"
date: 2003-02-07
url: https://daringfireball.net/2003/02/smartypants_11
slug: smartypants_11
word_count: 267
---


[SmartyPants 1.1](http://daringfireball.net/projects/smartypants/) has been released. Highly recommended for all users of SmartyPants 1.0.


What’s new:

- The `smart_dashes` template attribute now offers an option to use “--” for *en* dashes, and “---” for *em* dashes.
- Using the `smarty_pants` attribute with a value of “2” will do the same thing as `smarty_pants="1"`, with one difference: it will use the new shortcuts for en- and em-dashes.
- The default `smart_dashes` behavior now simply translates “—” (dash dash) into an em-dash. Previously, it would look for “ — ” (space dash dash space), which was dumb, since many people do not use spaces around their em dashes.
- Closing quotes (single and double) were incorrectly curled in situations like this:
- Added `<kbd>` to the list of tags in which text shouldn’t be educated. Previously, the list included only `<pre> and <code>`.


## What About Movable Type 2.6?


Glad you asked.


The [upcoming Movable Type 2.6](http://www.movabletype.org/news/2003_01.shtml#000747) is going to add a new Text Formatting feature:


> Instead of a simple Convert Line Breaks checkbox, you can now set a different formatting option for each entry. Plugins can add new options to the Text Formatting menu, which allows for greater integration with the formatting within the system (for example, Text Formatting will be applied on the preview screen).


We have top men working on integrating SmartyPants with MT 2.6’s Text Formatting system. *Who?* Top men.


In the meantime, however, Movable Type 2.6 isn’t even out yet. SmartyPants 1.1 is. Spread the word, and smarten your quotes.



| **Previous:** | [Enkode This](https://daringfireball.net/2003/02/enkode_this) |
| **Next:** | [When in Rome](https://daringfireball.net/2003/02/when_in_rome) |


PreviousNext