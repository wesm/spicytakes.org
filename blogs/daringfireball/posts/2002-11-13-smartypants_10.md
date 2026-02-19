---
title: "SmartyPants 1.0"
date: 2002-11-13
url: https://daringfireball.net/2002/11/smartypants_10
slug: smartypants_10
word_count: 160
---


Remember my [instructions](http://daringfireball.net/2002/08/movable_type_smart_quote_devilry.html) for generating smart quotes in Movable Type using Brad Choate’s MTPerlScript plug-in? Forget about that. I’ve got something better now.


Introducing [SmartyPants](http://daringfireball.net/projects/smartypants/), a free plug-in for Movable Type (version 2.5 or later).


SmartyPants is much improved over my previous MTPerlScript-based
solution. New features:

- Much easier to use and install. It’s just a simple plug-in, and
	it can be invoked from templates like so:
	

	<$MTEntryBody smarty_pants="1"$>
- Smarter algorithm, fixing several cases where quotes were
curled in the wrong direction.
- Now supports ``backticks'' -style quotes and smart ellipses.
- Ignores content inside <pre> and <code> tags.


Details, download, and documentation are all available on the [SmartyPants project page](http://daringfireball.net/projects/smartypants/).


If you’re currently using my previous smart quotes solution, I highly recommend you switch to SmartyPants. It’s easier, more accurate, faster, and offers you more control over which transformations occur when you publish articles.



| **Previous:** | [Journaling Details](https://daringfireball.net/2002/11/journaling_details) |
| **Next:** | [A Valid Point](https://daringfireball.net/2002/11/a_valid_point) |


PreviousNext