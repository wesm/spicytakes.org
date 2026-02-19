---
title: "A Valid Point"
date: 2002-11-15
url: https://daringfireball.net/2002/11/a_valid_point
slug: a_valid_point
word_count: 1662
---


[BBEdit 7 is out](http://www.barebones.com/products/bbedit.html).
BBEdit releases are official holidays at Daring Fireball headquarters.


Dori Smith [marked the occasion by complaining](http://www.backupbrain.com/2002_11_10_archive.html#a003110) that because BBEdit 7 now includes language support for ASP and VBScript, but does not have a built-in CSS validator, that Bare Bones is ignoring the needs of web developers.


Only in the mind of Dori Smith could new support for two additional web programming languages serve as evidence that Bare Bones is *not* listening to web developers. Despite the fact that ASP is a Windows technology, I assure you there are *many* BBEdit users developing web sites with it.


Smith followed that post with another, [griping about BBEdit’s HTML syntax checker](http://www.backupbrain.com/2002_11_10_archive.html#a003112), which reports errors against her weblog’s front page, even though the same page passes the W3C’s online HTML validator:


> So, my conclusion stands: if I can’t use BBEdit to check HTML standards compliancy (because it gives erroneous results) and I can’t use it to check CSS standards compliancy (because it doesn’t support this), then, it’s not a useful tool for standards validation. And that is something that I do a lot of.


Actually, her conclusion does not stand at all. BBEdit is not reporting erroneous results. Her blog’s markup *does* contain errors, and BBEdit is reporting them correctly. She may do a lot of HTML validation, but she doesn’t do it well. (Which is a tad embarrassing, considering that she [claims to sit on the steering committe](http://dori.com/) of the [Web Standards Project](http://www.webstandards.org/).)


This is a fairly common source of confusion. BBEdit’s syntax checker and the W3C’s validator frequently produce different results. Which is not to say they *disagree*, however — it’s just that they work very differently, and therefore find (and miss) different classes of markup errors.


It so happens that the most common discrepancies are situations where BBEdit reports errors that the W3C validator doesn’t. The correct action to take is to fix the errors BBEdit reports. The incorrect action is to blame BBEdit; it is almost certain that BBEdit is right, and your markup is wrong.


## About Validation


Just what does it mean when your web pages pass through an HTML validator without error? Only that they’ve passed through a validator. That’s a good thing, but it most definitely does *not* mean that your markup is error-free. It might be, but each HTML checker I’m aware of misses certain classes of errors.


That’s why I use both BBEdit and the W3C’s validator to check my markup. It’s also why, when your page passes through BBEdit’s syntax checker without error, BBEdit displays a dialog that says “No errors were found,” instead of “This document has no errors.” There might well be errors, but which BBEdit’s syntax checker couldn’t find.


Most people expect these tools to flag and catch any and all errors, without mistake. But while they’re both very good tools, neither is perfect. Confusion arises when they disagree, and a web page passes through one of them without complaint, but the other tool flags an error.


For example, take a look at these two HTML documents:


### reference_count.html


```

   <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
           "http://www.w3.org/TR/html4/loose.dtd">
   <html lang="en">
   <head>
      <title>Reference Count</title>
   </head>
   
   <body>
      <p>First body.</p>
   </body>
   
   <body>
      <p>Second body.</p>
   </body>
   
   </html>

```


([Source](http://daringfireball.net/misc/2002/11/reference_count.html); [W3C results](http://validator.w3.org/check?uri=http:%2F%2Fdaringfireball.net%2Fmisc%2F2002%2F11%2Freference_count.html))


### attribute_values.html


```

   <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
           "http://www.w3.org/TR/html4/loose.dtd">
   <html lang="en">
   <head>
      <title>Attribute Values</title>
   </head>
   <body>
   
   <table>
       <tr>
           <td width="foobar">A Table</td>
       </tr>
   </table>
   
   </body>
   </html>

```


([Source](http://daringfireball.net/misc/2002/11/attribute_values.html); [W3C results](http://validator.w3.org/check?uri=http:%2F%2Fdaringfireball.net%2Fmisc%2F2002%2F11%2Fattribute_values.html))


Each file contains a relatively glaring error that doesn’t get flagged by one of the checkers. The first file has two `<body>` tags, but BBEdit’s syntax checker doesn’t catch it. The second file has a bogus value for the `<td>` tag’s `width` attribute, but the W3C’s validator doesn’t catch it.


The first example is a demonstration of reference counting, which BBEdit’s syntax checker does not perform. Basically, what it boils down to is that certain markup constructs are only allowed to appear a limited number of times. `<body>` tags, for example, are only allowed to appear once. BBEdit knows *where* a `<body>` can appear, but it doesn’t keep track of how many you’ve used.


The second example is a demonstration of attribute value parsing, which the W3C’s validator does not perform. You can put just about *anything* in an attribute value, and the W3C validator won’t catch it. A table cell width set to “foobar” is obviously an absurd example, but it illustrates the point. In practice, invalid attribute values usually contain subtle errors which look OK to the naked eye. But BBEdit catches them.


Here’s a real-world example. The original HTML 4.0 specification did not allow for percentage-based widths for table cells. (This omission was rectified in HTML 4.01.) If you try to use something like the following in an HTML 4.0 document, BBEdit rightly reports an error:


```
<td width="50%">

```


This particular issue caused an enormous amount of consternation, followed by enlightenment, typically along these lines:


**User:** BBEdit has a bug. It tells me that I can’t use percentage widths in table cells in HTML 4.0 documents.


**Bare Bones:** That’s because you’re not allowed to. The attribute value for “width” must be a number.


**User:** But percentages work in all the browsers.


**Bare Bones:** That doesn’t mean it’s valid. Browsers support all sorts of crappy markup.


**User:** But my page passes through the W3C validator! If the W3C validator says it’s OK, BBEdit must be wrong.


**Bare Bones:** The W3C validator doesn’t parse attribute values. Try changing the width to “fred flintstone”. It will still pass the W3C validator.


**User:** OK, hold on… Oh. Wow. You’re right. But I need percentage widths for my layout! What should I do?


**Bare Bones:** Complain to the authors of the 4.0 spec.


## The Fix Is In


Now that we have the background, we can easily see why BBEdit catches the errors at backupbrain.com, but the W3C validator doesn’t. All three errors are similar. For example, for this anchor tag:


`<a href="http://purl.org/net/syndication/subscribe/?rss=http://www.backupbrain.com/index.xml" title="Subscribe via SSS">
`


BBEdit reports the following error:


`File "index.html"; Line 173:  Value of attribute "href" for element "<a>" is invalid; URL path needs encoding
("/net/syndication/subscribe/?rss=http:%2F%2Fwww.backupbrain.com%2Findex.xml").
`


As you can see, it doesn’t just report the error — the slashes after the question mark in the URL need to be encoded — it generates the correctly encoded URL in the error message. (If you use BBEdit’s Anchor dialog to enter URLs, BBEdit will encode them for you.)


The W3C validator doesn’t catch the error because this is another example of attribute value parsing.


In the grand scheme of things, hers is not a grave error. It’s certainly quite common, and most user agents are smart enough to deal correctly with the unescaped slashes in the search part of her URI. But that doesn’t mean the slashes shouldn’t be escaped: “/” is a reserved character in URIs, used as a directory separator. In her href attribute above, the slashes after the “?” are not being used as directory separators, and thus should be escaped.


As Jim Correia (the Bare Bones engineer largely responsible for the syntax checker) [wrote a while back](http://search.barebones.com/action.lasso?list=web-authoring&originator=correia&subject=w3c+validator+or+bbedit+validator&contents=&-op=gte&date.sent=&-op=lte&date.sent=&-logicalop=and&-maxRecords=10&-database=lists.fp3&-layout=import&-response=%2Fhitlist.html&-noResults=noresults.html&-search=MSExplorerHack&-search=Search) on the BBEdit web authoring mailing list:


> ? starts your search part, and / is no longer being used as a
> 	hierarchy delimiter afterwards, so you should encode it. A well behaved
> 	CGI will url decode the search part before doing work and all shall be
> 	well. … 
>  (If you don’t encode the / after the ? search part delimiter, a
> 	particular implementation is left to guess. It may guess that ? was
> 	part of a resource name, and that you forgot to encode it. In this
> 	case, you won’t get the behavior that you desire. It may guess that the
> 	/ after the ? was the thing you forgot to encode, and treat the ? as
> 	the delimiter between the path and the search part, in which case you
> 	will get the behavior you desire. But why leave it to chance when
> 	encoding the / in the search part will remove the ambiguity?)


The authoritative reference is [RFC 2396](http://www.ietf.org/rfc/rfc2396.txt), co-authored by one Mr. Tim Berners-Lee.


BBEdit’s syntax checker and the W3C HTML validator are both terrific tools. (And yes, a “syntax checker” is not the same thing as a “validator”, although that’s not to say that one or the other couldn’t be improved in the future to handle all of the above examples.) Rather than competing, they complement each other rather nicely, which is why I use both.


If I had to choose just one, however, I’d go with BBEdit’s syntax checker. For one thing, it’s much more convenient to use — it’s faster to invoke, and it displays its results in a well-designed error browser that lets you jump right to the errors in your document. Furthermore, it catches more of the errors that I’m likely to make, especially stupid typos in attribute values. It’s not likely at all that I’ll include two `<body>` tags in a document.


But there’s no reason to choose. Use both. And when one reports an error that the other doesn’t, the correct action is almost always to fix it. The shortcomings in both tools are that they both miss certain kinds of errors, not that they report bogus errors.


## Pixel Pushing


Smith also complains about BBEdit’s syntax checker issuing warnings against [her cat’s homepage](http://pixel.mu). The page has 25 implicitly-closed `<li>` tags, and, not surprisingly, BBEdit issues 25 warnings about implicitly-closed `<li>` tags. I don’t understand why she’s complaining about this — especially since this warning can be turned off in BBEdit’s preferences — but then again, I don’t understand why she’s written two consecutive reviews of Script Debugger for Macworld in which she blames Late Night Software for bugs in Microsoft Word and Excel ([2.0, Jan 2001](http://www.cnn.com/2001/TECH/computing/01/23/new.applescript.features.idg/); [3.0 Feb 2002](http://www.macworld.com/2002/02/reviews/scriptdebugger.html)).



| **Previous:** | [SmartyPants 1.0](https://daringfireball.net/2002/11/smartypants_10) |
| **Next:** | [Do You Smell Something?](https://daringfireball.net/2002/11/do_you_smell_something) |


PreviousNext