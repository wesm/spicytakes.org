---
title: "Movable Type Smart Quotes, Now With Retsin"
date: 2002-10-05
url: https://daringfireball.net/2002/10/movable_type_smart_quotes_now_with_retsin
slug: movable_type_smart_quotes_now_with_retsin
word_count: 585
---


Back in August, I [posted an article](http://daringfireball.net/2002/08/movable_type_smart_quote_devilry.html) describing how to convert straight quotes to curly quotes in [Movable Type](http://movabletype.org) blog templates. I’ve fixed some bugs, improved the smart quotes algorithm, and taken advantage of new features in the latest version of [Brad Choate’s](http://www.bradchoate.com) MT plug-ins. If you use Movable Type, read on for details.


[***13 Nov 2002:** If you’re using Movable Type 2.5 or later, these instructions are now obsoleted by my new [SmartyPants plug-in](http://daringfireball.net/projects/smartypants/).*]


If you want to just cut to the chase, go ahead and read the [full instuctions](http://daringfireball.net/2002/08/movable_type_smart_quote_devilry.html). (That’s the URL for the original article, but it now contains the updated instructions.)


## Changes

- The original instructions contained a really stupid bug because of the way I quoted text passed to the Perl script. I was using Perl’s `q()` operator, using parentheses as delimiters. If you tried to publish a post containing unbalanced parens — most frequently because of smileys: `:-)` — MT would fail to publish the article, and you’d see cryptic errors (which probably looked like downright gibberish if you don’t speak Perl). This is now fixed.
- The regular expressions which perform the quote education failed in a few edge cases. For example, the closing quote in the following text would be erroneously turned into an opening quote:

    some "<em>italics</em>" inside quotes


This is now fixed.
- The latest versions of Brad Choate’s [MTPerlScript](http://www.bradchoate.com/past/mtperlscript.php) and [MTMacro](http://www.bradchoate.com/past/mtmacros.php) plug-ins (1.3 and 1.5, respectively) now integrate with each other, which makes it easy to create pseudo-tags for MT templates which execute Perl scripts.


In the original instructions, you needed to use something like this in your templates (ignore the stupid `q()` bug):

    <h1><MTPerlScript>
        print educate_quotes::educate( q(<$MTEntryTitle$>) );
    </MTPerlScript></h1>

    <MTPerlScript>
        print educate_quotes::educate( q(<$MTEntryBody$>) );
    </MTPerlScript>


Now, you can use this instead:

    <MTMacroApply>
    <h1><educate_quotes><MTEntryTitle></educate_quotes></h1>

    <educate_quotes><MTEntryBody></educate_quotes>
    </MTMacroApply>


## How Smart Is Smart Enough?


One case where my algorithm still fails is if you use a single apostrophe in a leading contraction, such as either of these examples:


```
    during the '80s

    'Twas the night before Christmas...

```


The algorithm will turn both apostrophes into *opening* single quotes; they should be closing quotes. This is a tough problem to solve without making special cases. In fact, the same problem happens in every word processor I tried. I figure if BBEdit, Word, and QuarkXPress aren’t smart enough to get this right, I don’t care if my script is either.


Plus, in the specific case of abbreviated decades, my style is to write them like this:


```
    during the 80's...

```


which works just fine.


## Elsewhere


Matthew Mullenweg offers his own [set of instructions](http://www.photomatt.net/scripts/mtcurly%20), using Brad Choate’s MTRegex plug-in. However, I don’t believe it’s possible to correctly educate quotes in HTML markup only using regular expressions. Mullenweg comes close, but his implementation will do bad things
with perfectly valid markup like this:


```
    <p>Link <a href = "foo" >this</a> baby.</p>

```


where by “bad things”, I mean it will curl the quotes around the href
attribute inside the tag. This won’t happen if, as is usually done, you put the attribute right next to the equals sign:


```
   href="foo"

```


but I’m uncomfortable failing against valid markup, especially in this case, when it will prevent the tag from working at all.


Mullenweg’s implementation also fails if the quotes contain only one
character:


```
    <p>What about the letter "a"?</p>

```


because his regex pattern requires at least two characters between quotes in order to match.



| **Previous:** | [Linktoberfest](https://daringfireball.net/2002/10/linktoberfest) |
| **Next:** | [Matters Unix](https://daringfireball.net/2002/10/matters_unix) |


PreviousNext