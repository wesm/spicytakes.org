---
title: "Movable Type Smart Quote Devilry"
date: 2002-08-16
url: https://daringfireball.net/2002/08/movable_type_smart_quote_devilry
slug: movable_type_smart_quote_devilry
word_count: 1590
---


Over at [DiveIntoMark](http://diveintomark.org), Mark Pilgrim has some excellent tips with regard to hacking Movable Type [to generate smart quotes](http://web.archive.org/web/20021205190859/http://diveintomark.org/archives/2002/08/15.html#better_living_through_regular_expressions) (a.k.a. curly quotes, a.k.a. typographer’s quotes). This got the gears turning here at Daring Fireball — surely, this could and should be even easier.


[***13 Nov 2002:** If you’re using Movable Type 2.5 or later, these instructions are now obsoleted by my new [SmartyPants plug-in](http://daringfireball.net/projects/smartypants/).*]


[***5 Oct 2002:** This article was edited on October 5 to (1) fix a few bugs; (2) take advantage of improvements in the latest versions of Brad Choate’s plug-ins; and (3) improve the smart-quotes algorithm. See [this article](http://daringfireball.net/2002/10/movable_type_smart_quotes_now_with_retsin.html) for details about the changes.*]


For, what, at least the last 15 years or so, Mac users have come to expect proper quotes to happen automatically simply by typing regular apostrophes and quotation marks. In their word processors, that is. In HTML markup, however, smart quotes have been a royal pain in the ass.


The problem with getting smart quotes in HTML is that the curly quote characters aren’t part of the standard cross-platform ASCII character set, which means that if you want them to appear properly on all platforms, you need to use entities. But raw entities are ugly and distracting — it’s hard to write and edit when your text looks like this:


```
&#8220;Who&#8217;re you?&#8221;, she said.

```


So, most people ignore the issue, and simply use good old-fashioned dumb quotes in their HTML. Typography nerds who persevere and insist upon doing the right thing, like [Textism’s](http://textism.com) Dean Allen, typically resort to [preflighting scripts](http://web.archive.org/web/20040603082220/http://www.textism.com/resources/index.html?id=9) to generate smart quote entities. In other words, a three-step process:

1. Write, edit, and fuss over a blog article, using plain text.
2. Run preflight script(s) to generate the desired entities.
3. Post the article to the web.


But the whole point of modern blogging tools is that they make posting articles easy. Normal, non-obsessive people will only tolerate steps 1 and 3: write, then post. And they’re right — educating quotes is not a difficult problem to solve, and your software should be able to do it for you.


Our own preflight scripts here at Daring Fireball are BBEdit text filters, written in Perl. But why invoke them manually, when Movable Type itself is extensible with Perl? Why indeed.


The way it ought to work is to write using plain old easy-to-type dumb quotes, store the article in Movable Type’s database with the dumb quotes, and have the quote education take place at the template level, when the article gets published.


Here’s our solution:

1. Install two of Brad Choate’s free Movable Type plug-ins: [MTPerlScript](http://www.bradchoate.com/past/mtperlscript.php) (version 1.3 or later) and [MTMacro](http://www.bradchoate.com/past/mtmacros.php) (version 1.5 or later). They’re a cinch to install — instructions are included in the readme files. Be sure to install the latest versions of both plug-ins — older versions won’t work with the macros defined below. Mr. Pilgrim is using one of Mr. Choate’s other plug-ins, MTRegex, but the smart quotes algorithm we’re using can’t be expressed as a single regular expression. We need multiple patterns and few `while()` loops. The amazing MTPerlScript plug-in allows us to do that.
2. Add a template module containing the following text. I named my module “Educate Quotes”. This module contains two things: (1) a macro that defines a new `<educate_quotes>` tag for MT templates; and (2) the Perl script that does all our quote education, including both single and double quotes. The Perl script also creates em dashes — like the ones bracketing this very clause — by turning each occurrence of “ -- ” (space dash dash space) into a genuine em dash HTML entity.


<MTMacroDefine ctag="educate_quotes" script="PerlScript">
print educate_quotes::educate($MTMacroContent);
</MTMacroDefine>


<MTPerlScript package="educate_quotes" cache="1" once="1">

sub educate {
    $_ = shift;

    # First, check to see if the text we're educating contains
    # markup. If it does, we need to take extra steps to avoid
    # smartening any quotes within HTML tags.

    if (m/<.+>/s) {

        # Find single quotes that need to be turned into closing
        # curly quotes. The pattern looks for text between tags.
        1 while s{
            (?<=>)          # Positive lookbehind for a ">"
            ([^<]+)?        # One or more of anything but "<", optionally.
            (?<!\s)         # Negative lookbehind for a whitespace char
            '               # A quote
            (?(1)|(?=\s))   # If $1 captured, then do nothing;
                            # if not, then make sure the next char is whitespace  
        }{$1&#8217;}xgs;
        
        # Any remaining single quotes should be turned into
        # opening curly quotes.
        1 while s/(>[^<]*)'/$1&#8216;/xgs;
        
        # Closing double-quotes (same pattern as above)
        1 while s{
            (?<=>)          # Positive lookbehind for a ">"
            ([^<]+)?        # One or more of anything but "<", optionally.
            (?<!\s)         # Negative lookbehind for a whitespace char
            "               # A quote
            (?(1)|(?=\s))   # If $1 captured, then do nothing;
                            # if not, then make sure the next char is whitespace  
        }{$1&#8221;}xgs;
        
        # Opening double-quotes
        1 while s/(>[^<]*)"/$1&#8220;/xgs;
        
        # Let's make real em-dashes while we're here.
        1 while s/(>[^<]*)(\ --\ )/$1\ &#8212;\ /gs;
    }
    else {
        # The text we're educating doesn't contain markup,
        # so we don't need anything fancy.
        
        s/(\S)'/$1&#8217;/g;    # closing single quotes
        s/'/&#8216;/g;          # opening single quotes
        
        s/(\S)"/$1&#8221;/g;    # closing double quotes
        s/"/&#8220;/g;          # opening double quotes
        
        s/ -&#45 /&#8212;/g;       # em dashes
    }

    return $_;
}

</MTPerlScript>
3. In each of your blog templates in which you want smart quotes, include the Educate Quotes module by inserting the following code. (It doesn’t matter where you put this in the template; somewhere near the top is as good a place as any.)

<$MTInclude module="Educate Quotes"$>
4. Finally, wrap the MT tags whose quotes you want to educate in `MT` tags that call our script. For example, the only tags we want to educate here at Daring Fireball are each entry’s title and body. Here’s the template code we previously used:

<h1><$MTEntryTitle$></h1>


And here’s what we use now to generate the same output, but with educated quotes:

<MTMacroApply>
<h1><educate_quotes><MTEntryTitle></educate_quotes></h1>
	
<educate_quotes><MTEntryBody></educate_quotes>
</MTMacroApply>


## Notes and Warnings


We’re eating our own dog food here at Daring Fireball, so we’re using this very script ourselves (at least at the time of this writing) with no ill effects whatsoever. But bugs happen; if you find one, please do let us know.


The whole thing gives off a tad whiff of being a hack. It’d be slicker, safer, and easier to use in templates if this were its own plug-in, rather than a script that runs inside the MTPerlScript plug-in.


## Nerdy Overview of the Smart Quotes Algorithm and Regex Patterns


The curious reader might question why the `educate()` routine is as complicated as it is. At first thought, you might be tempted to simply use the technique used in the `else` block — four simple calls to the substitution operator. The problem is that when you’re educating quotes in HTML markup, you can’t mess with the quotes inside tags. You don’t want to change


```
    <a href="foo">
```


into


```
    <a href=&#8220;foo&#8221;>
```


So, the first step in the script is to see if the text we’re working with contains HTML markup:


```
    if (m/<.+>/s) {

```


If it doesn’t, then it’s a piece of cake to smarten up the quotes. Jump to the `else` block and run a few simple substitutions.


If the text *does* contain markup, then we need to use loops to search for every straight quote (and apostrophe) that *isn’t* inside a tag:


```
    1 while s{
            (?<=>)          # Positive lookbehind for a ">"
            ([^<]+)?        # One or more of anything but "<", optionally.
            (?<!\s)         # Negative lookbehind for a whitespace char
            '               # A quote
            (?(1)|(?=\s))   # If $1 captured, then do nothing;
                            # if not, then make sure the next char is whitespace  
        }{$1&#8217;}xgs;

```


We need a loop because a single regex substitution pattern can’t find multiple quotes in a single stretch of text between tags. In English, the pattern for closing single quotes is looking for “>” followed by one or more characters that are not “<”, followed by a non-whitespace character, followed by an apostrophe.


But if there are two or more closing single quote characters in a run of text, the pattern is only going to match the first, because the subsequent quotes won’t have the “>” to match, because the regex engine moved past that text in the first match. Thus, we loop. The `while` loop keeps running as long as the pattern matches. Once we’ve smartened up all the quotes, it stops and moves on to the next one.


The logic for determining whether a quote is opening or closing is fairly simple: if the character immediately preceding is non-whitespace, then it’s a closing quote. It’s also a closing quote if the quote is the first character after the tag, and the next character after the quote is a space (for example: `if you have "<i>italics</i>" inside quotes`). Once you’ve changed those, any remainders are opening quotes.


One last note. If you ever actually want to use literal straight quote characters — like we did here in our code sections — you’ll need to explicitly ask for them by using HTML entities. “&quot;” will give you a straight double quote character, and “&#39;” will give you a straight apostrophe.


## Credits


Special thanks to [Brad Choate](http://www.bradchoate.com), who not only wrote the amazing plug-ins upon which this article depends, but also wrote in with a fix to a glaring bug in my original implementation. Brad is the man.



| **Previous:** | [Jack Valenti Does Not Smell Like Teen Spirit](https://daringfireball.net/2002/08/jack_valenti_does_not_smell_like_teen_spirit) |
| **Next:** | [Why HyperCard Failed](https://daringfireball.net/2002/08/why_hypercard_failed) |


PreviousNext