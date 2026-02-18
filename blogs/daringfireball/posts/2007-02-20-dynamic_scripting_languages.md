---
title: "Using Dynamic Scripting Languages for Mac OS X Application Development"
date: 2007-02-20
url: https://daringfireball.net/2007/02/dynamic_scripting_languages
slug: dynamic_scripting_languages
word_count: 316
---


There’s been a lot of interesting discussion over the last week regarding the use of dynamic scripting languages for programming desktop applications. Here’s some of what caught my eye:

- [Andrew Shebanow](http://blogs.adobe.com/shebanation/2007/02/desktop_application_programmin.html) argues that this transition isn’t in the
future; it’s happening now. Adobe Lightroom’s user interface is
mostly written in [Lua](http://www.lua.org/), for example. He also has a good point
that what makes these languages interesting isn’t that they are
interpreted, but that they’re dynamic.
- [Bill Bumgarner](http://www.friday.com/bbum/2007/02/16/c-portable-macro-assembler/) reminds us that the Python-Cocoa PyObjC
bridge isn’t new; it’s been used in production since the Next
era in the mid-90s. He also has some good insight into why Ruby
and Python are such good fits for bridging to frameworks
originally designed for use with Objective-C. He also links to
a couple of professional Mac apps that are already written using
PyObjC.
- [Michael Tsai](http://mjtsai.com/blog/2007/02/14/c-is-the-new-assembly/) is already writing commercial software
using a hybrid approach with Python and Objective-C; he writes
that the most common performance hit comes when crossing the
bridge.
- [Jesper](http://waffle.wootest.net/2007/02/16/the-planks-in-the-bridge/) has more on why the Python and Ruby Cocoa bridges
aren’t likely to suffer the same fate — irrelevance and
eventual obsolescence — that Apple’s Java Cocoa bridge did. In
a nut: Ruby and Python are both *more* dynamic than Objective-C;
Java is *less* dynamic than Objective-C.
- [Scott Stevenson](http://theocacao.com/document.page/428/) says not so fast — Objective-C 2.0
(coming in Leopard), which adds garbage collection and some
useful new syntax like properties and `foreach` loops, obviates
many of the things that might draw Cocoa developers to Ruby or
Python, and has the advantage of being the language Cocoa was
specifically written for.


(The comment threads on most of these articles are worth a read, too.)



| **Previous:** | [Translation From PR-Speak to English of Selected Portions of Macrovision CEO Fred Amoroso’s Response to Steve Jobs’s ‘Thoughts on Music’](https://daringfireball.net/2007/02/macrovision_translation) |
| **Next:** | [Fair Enough](https://daringfireball.net/2007/02/fair_enough) |


PreviousNext