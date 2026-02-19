---
title: "Short and Curlies"
date: 2003-02-22
url: https://daringfireball.net/2003/02/short_and_curlies
slug: short_and_curlies
word_count: 1614
---


[Cory Doctorow says he hates curly quotes](http://www.boingboing.net/2003/02/20/why-i-hate-curlyquot.html) in web content. While I agree with him that there’s a problem, I completely disagree about the solution.


Let’s be clear: I’m the author of [SmartyPants](http://daringfireball.net/projects/smartypants/), a plug-in for Movable Type (and soon, Blosxom) weblogs which automatically generates the typographically-correct punctuation Mr. Doctorow is complaining about, so I’m not exactly an unbiased observer — I’m partially responsible for the growing movement toward using proper punctuation on weblogs.


And I couldn’t be prouder.


Doctorow’s solution is for everyone to just stick with 7-bit ASCII characters. *My* solution is to fix or discard any retarded software that still insists on such restrictions. It’s 2003, right?


## She’s Got Your Name, She’s Got Your Number


Doctorow starts:


> Curly-quotes are the bane of my blogging existence, like a never-ending
> 	supply of pubes caught between my blog-teeth. Why? Because if I blog
> 	your story and paste in an excerpt with a curly-quote, or an em-dash, or
> 	an accent character, or any other non-ASCII characters, the RSS feed for
> 	Boing Boing breaks, and then I get tons of cranky email from people who
> 	want it fixed. Then I have to haul out the XML validator and slowly
> 	open, edit and save the offending post(s), until all the non-ASCII
> 	characters are g0nezored.


This seems to hint that one needs to translate smart punctuation characters to plain ASCII characters to generate valid RSS output. Not true. It *is* true that the “raw” smart punctuation characters aren’t valid; they simply need to be replaced by the corresponding HTML entity. For example, the entity for a trademark symbol (™) is “`&trade;`”; the entity for an opening double quote is “`&ldquo;`”. Alternatively, you can use a numeric syntax, which is harder to remember, but compatible with more web browsers. The numeric entity for a left double quote is “`&8220;`”.


HTML entities aren’t hard to deal with by hand, but they can be difficult to remember, and they’re definitely ugly to look at while you’re writing. But unless you’re a professional web developer, there’s no reason to deal with them by hand — if you just want to write, your software ought to take care of them for you.


> I blame Robin Williams, the designer whose “Non-Designer’s Design
> 	Handbook” convinced a generation of geeks that their type would look
> 	suave if it came with em-dashes and curly-quotes, and caused us all to
> 	suffer through email, Usenet posts, and blog-entries where strange
> 	dipthongs are inserted in place of honest inch- and foot-marks,
> 	rendering the text unreadable except in whatever proprietary tool it
> 	was created in.


This is just so wrong. [Robin Williams is a saint.](http://www.ratz.com/robin/toc.html) A *saint*, I tell you. Her seminal [*The Mac Is Not a Typewriter*](http://beta.peachpit.com/books/catalog/48430.html) is a terrific layman’s guide to proper typography and design. Williams writes clearly and well, explaining ostensibly technical topics using non-technical words. Her design books are geared toward print design, not web design, but the basic principles are the same.


> It’s bad enough that we have three mutually exclusive
> 	line-break conventions, do we really need to migrate a bunch of
> 	centuries-old typesetters’ conventions into our ASCII paradise?


That print typesetting is a 400-year-old art form doesn’t make it obsolete. Quite the opposite, it means we’re fortunate enough to have a tremendous body of knowledge to learn from. Digital technology has dramatically changed the media and tools, but the fundamental issues of typesetting remain the same: style, tone, texture, weight, and, above all else, readability. The idea that web designers ought to ignore the lessons of traditional typesetting is as silly as recommending photographers ignore the lessons of composition, framing, and color from the art of painting.


And exactly whose paradise is ASCII? The ASCII character set is comprised of a measly 128 characters, many of which are non-printing control characters. It’s the crummiest character set imaginable, the lowest of lowest common denominators. Compatible? Yes. Cripplingly deficient? Yes, that too.


> Sure, there are some good reasons to go non-ASCII (for example, if
> 	you’re writing in Hebrew, or even French), but the tools just aren’t
> 	there yet, especially as applied to curly-quotes and em-dashes and all
> 	of Ms. Williams’s precious non-ASCII punctuation.


*Even French?* How generous! Finally, the millions of people whose names contain characters such as “é” can spell their names correctly without fear of offending Cory Doctorow’s sensibilities.


And exactly which tools “aren’t there yet”? Macintosh users have long enjoyed automatic smart quotes in their word processors, along with simple, logical keystrokes for en- and em-dashes (Option-Dash and Shift-Option-Dash, respectively). The Internet’s reliance on the decrepit ASCII character set isn’t just a huge step backwards for Mac users today; it would be a huge step backwards for Mac users circa 1987.


Email and Usenet are one thing. Those protocols were designed with nothing more than plain text in mind, and smart punctuation doesn’t belong in either medium. In email and Usenet, there is no distinction between the original source and what gets displayed on the other end of the transmission (ignoring bastardizations like HTML and “rich text” email). What I type, you see.


But the web is different: a web server sends HTML markup, but the browser displays rendered output, not the source code. So despite the fact that an HTML source file ought to be written using plain ASCII, you can use HTML entities to display non-ASCII characters in the rendered output. *This is exactly why HTML entities exist.*


Doctorow is right that there exists a lot of dumb software that makes it hard to use non-ASCII text copied and pasted from a web browser. For example, if you copy and paste a paragraph containing a quotation mark from my site, the text will contain the actual curly quote character. If you want to use that text in a `<blockquote>` section on your web site, you will need to either:

- translate the smart punctuation characters into HTML entities;
- translate them into corresponding ASCII characters; e.g. changing “`©`” to “`(c)`”, and turning curly quotes into straight ones.


That’s not a hard problem for software to solve. Any decent text editor or email client should be able to stupefy smart quote characters into their 7-bit ASCII equivalents, and I don’t consider it my problem if you’re using an indecent text editor.


I especially have no sympathy for you if your text editor is a lame textarea field in a web browser form provided by your weblogging software. This shouldn’t apply to Cory Doctorow, however, since I happen to know that [he’s a longstanding BBEdit](http://saladwithsteve.com/osx/2002_12_01_archive.html#90042204) user — he even used BBEdit to write *[Down and Out in the Magic Kingdom](http://craphound.com/down)*).


## Screaming Blue Murder


Here then is an AppleScript for BBEdit which will turn text containing smart punctuation into plain ASCII. It’ll turn curly quotes into straight quotes, en-dashes into normal hyphens, em-dashes into two dashes, and ellipses into three dots.


[Update: This script is actually sort of dumb. Instead, use BBEdit’s scriptable Convert to ASCII plug-in. I wrote an [example script and explanation](http://daringfireball.net/2003/02/larry_moe_curly.html), along with info on how to script BBEdit’s Translate Text to HTML command.]


```

tell application "BBEdit"
    set my_opts to {search mode:grep, starting at top:true}
    set w to window 1
    if (selection of w as text) is "" then
        set target to w
    else
        set target to selection of w
    end if
    replace "[\\xD2\\xD3]" using "\"" searching in target options my_opts
    replace "[\\xD4\\xD5]" using "'" searching in target options my_opts
    replace "\\xD1" using "--" searching in target options my_opts
    replace "\\xD0" using "-" searching in target options my_opts
    replace "\\xC9" using "..." searching in target options my_opts
end tell

```


If there’s a selection in the front BBEdit text window, the script will only affect the selected text; if there’s no selection, it will process the entire window. Save it in your BBEdit “Scripts” folder, set a keyboard shortcut for it using the Script palette, and you have a one-keystroke solution.


If you use [Mailsmith](http://www.barebones.com/products/mailsmith/), you can use this script simply by changing the `tell` target from “BBEdit” to “Mailsmith”. If you’re using some less scriptable email client, you’re on your own.


## It’s Too Bad, She’s Got You by the Balls


Dealing with HTML entities is a trivial software problem. Trivial. You shouldn’t have to deal with HTML entities by hand. You should not be expected to remember them, or to be forced to look at the raw entities while editing. You should be able to copy text from a web browser and have the right thing happen where ever you paste. For example, Dean Allen’s remarkable [Textile](http://textism.com/tools/textile/) web application not only translates straight quotes into curly quotes, but it also allows you to simply paste raw curly quotes (and other smart punctuation) and it will automatically generate proper HTML entities, ready for publishing anywhere on the web. This is how all web writing software should work. Textile is part of Dean’s now-in-beta-testing web publishing system [Textpattern](http://textpattern.com/); once Textpattern-powered sites start popping up, we’ll be one step closer toward making proper punctuation the norm, not the exception.


Proper typographic punctuation is 400-year-old news. That it’s considered exotic, or even non-standard, on today’s web is embarrassing. The solution isn’t for everyone to limit themselves to the same character set used on 1970’s-era VT-100 terminals. The solution is for software developers to write smarter software. Every day more web sites are starting to use smart punctuation, making sites that don’t — and the software behind them — look bad.


Did someone say *Blogger*?



| **Previous:** | [Popularity Contest](https://daringfireball.net/2003/02/popularity_contest) |
| **Next:** | [Larry, Moe, Curly](https://daringfireball.net/2003/02/larry_moe_curly) |


PreviousNext