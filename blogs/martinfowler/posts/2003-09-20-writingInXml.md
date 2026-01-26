---
title: "Writing with XML"
description: "All of this site is written in simple XML documents and   transformed to HTML. I find this works really well, and means I   never have to worry about dealing with HTML formats. (Not that fancy   layou"
date: 2003-09-20T00:00:00
tags: ["writing"]
url: https://martinfowler.com/articles/writingInXml.html
slug: writingInXml
word_count: 2482
---


## How I got started


### First steps - the refactoring catalog


I began working with XML around 2000, when my refactoring
book came out. I'd already set up a web site, and decided to add a new
site to act as a portal of information about refactoring. On that site
I list all the refactorings in my book (together with a few others)
and decided to use XML to store the refactorings, that way I hoped
that it would be easier to edit and update them.


On the whole I found web site work a bit of a pain. Writing
in HTML is awkward, particularly if I want to make global changes or
to search the HTML files for useful information. Furthermore I
couldn't easily prepare material for both HTML and print use. My dream
was always to write where I could have a single piece of text that
could be formatted either in HTML or in a good print form. None of the
tools I had available to me at that time really did a good job of
both.


I've always been a fan of logical styles when writing. As
soon as I start doing anything non-trivial in a word processor I like
to set up logical styles that match the way the content of my writing
is structured. That way I can think about content and formatting
separately - although as you can tell my HTML format is hardly
sophisticated. So the idea of writing text marked up with XML and then
formatting separately for HTML appealed to me a lot.


Although my efforts with the refactoring catalog were
somewhat crude (or at least they seem that way to me now) I was very
pleased with how the process all worked. I wrote the book using
framemaker and the version then allowed a primitive, but effective,
way to save the frame data in XML. The resulting XML was okay, but it
wasn't exactly how I wanted it, since it tagged the elements in
Framemaker's vocabulary, rather than the tags I wanted to use for the
site. Fortunately XSLT is just perfect for fixing this problem, and
even though I was unused to XSLT, it was easy to write a stylesheet
that would transform the elements I wanted to keep, while filtering
out the ones I didn't want on the site.


Once I had the files together, I was able to write another
XSLT stylesheet to display the files as HTML. One stylesheet formatted
the lot, and should I want to change it, again I had only one place to
change. (The DRY principle is a good thing!)


Since each file was textual and well structured, I could also
write a program to create the catalog index file. This is Java program
that reads each catalog file in the directory and writes out selected
information from each refactoring in the index. That way if I ever add
or alter a refactoring, I just run the program to update the index. By
putting all this into an ant script, I can regenerate the whole site
by just running ant's build process. All in all I was very pleased
with the whole experience


### A web site and a book


Happy with my success with the refactoring catalog, I started
to use XML and XSLT on my web site. I started to write articles in XML
and transform them into HTML. I like this because I don't have to
bother with all the formatting codes of HTML, I can just write with a
simple set of tags in XML and let the stylesheet take care of the
rest. I can also use XSLT do tasks like automatically generate a table
of contents for each article.


So as 2001 went on I became steadily more skilled in this
environment, and figured out how bend XSLT to my will. It occurred to
me that this might be time to work on a book in XML. So far all my
book writing had been done in Framemaker. Framemaker has its faults,
but for me it's strengths were it solidity and its awesome
cross-referencing capabilities. However I was frustrated by its closed
file formats, that often meant I couldn't do tasks that weren't
supported by the tool. You also can't script in Frame without
expensive and awkward add on software. The real issue for me, however,
was that I wanted to put my emerging book on the web in HTML, and I
wasn't happy with Frame's conversion process, certainly not compared
with XML/XSLT.


So I embarked on my [P of EAA](https://martinfowler.com/books/eaa.html)  book in XML, and all in all I liked the
way it turned out. Suffice to say that my next book will be written in
XML too. I found it useful not just for me, but also there a few
tricks that were handy when collaborating with a co-author, particular
when Dave Rice ended up in Australia. The strength wasn't so much XML,
as the fact that XML is a plain text format, which opens up tools that
work well with plain text.


## Typing in the text


It seems the first question people ask is âwhat do you type in
the text withâ. The answer seems pretty obvious to me - a text
editor. As a programmer I'm pretty familiar with many text editors,
and one of the strengths of XML as a format is that you can use
whatever text editor you like to type things in with. This was great
for collaborators since I didn't have to worry about getting expensive
software to them to contribute their sections to the book.


While I was writing the book, my text editor of choice was
TextPad - surely the best $30 I've ever spent on a piece of
software. It's fast and full of simple but handy features. I found its
clips library was really good at tagging the text the way I wanted
it.


I considered other XML editing tools, but wasn't keen on the
various alternatives. Most of them wanted DTDs to do anything
interesting, and I only started using DTDs late in the game.


Just this last few months I've started using XEmacs. I've used
emacs off and on for many years, but mostly off as every computer I
used seemed to either not have it, or the windows ports were very
unknowing of the rest of the system (I consider cut and paste to be
basic functionality.) Xemacs 21.4 on windows is pretty windows
friendly. The SGML major mode works quite nicely for text based
documents, particularly if you have a DTD - which I now do. Of course
you have to be used to emacs key combinations, which seem very retro
these days.


I've tried XML spy a couple of times, but it doesn't really
suit my purposes. It's more focused on data oriented XML and isn't
really as nice for typing text. Once I got used to the key
combinations I missed the nice ones in XEmacs.


I'll see how things develop in the future. I could certainly
imagine a better tool that a simple text editor, but so far the text
editors have beaten some very fancy and expensive tools.


## Converting to HTML


This approach works particularly wonderfully when you are
producing HTML pages. Writing in XML and transforming with XSLT works
very well for me.


It didn't start that way. XSLT is a pain of a language - a
wonderful reason why you shouldn't use anything XML based as a
programming language. Some may find its lisp-like quality of
data/program similarity to be appealing. I just find it very hard to
write and work with. It's also pretty complex, which doesn't help at all.


Despite its faults, XSLT is powerful. But there are a few tips
to make your life saner

- remember that XSLT is like a functional programming language, it doesn't allow variables in the normal way, so you use recursion when you want to loop.
- use it to match patterns not to drive the output. So prefer
 <xsl:template match = âfooâ> to <xsl:for-each>. (You'll
be more comfortable with this if you've ever used awk.)
- Get Michael Kay's [XSLT Programmer's
reference](https://www.amazon.com/gp/product/1861005067/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=1861005067&linkCode=as2&tag=martinfowlerc-20). It's a dauntingly large book, but it is a very fine
reference. It isn't the greatest book to learn XSLT from, but I find
it great in answering detailed questions.


For producing HTML, and indeed in lots of other places, I
relied on build scripts. For the book I had ant scripts that built the
code and built the book pages automatically. Having a build script
made life much easier.


All in all, however, I really like the separation that XML/XSLT
gives me. I find it much easier to write with a simple set of logical
tags, even though my pages are very simple in their formatting. One
day I'll maybe have a fancy web site.


## Converting to print


While converting to HTML is simple and obvious, books require a
print style format. That was rather more of an issue


My first attempt was to use XSL-FO with apache's FOP. At that
time (early 2002) I found that while XSL-FO clearly had all the
capabilities I needed, FOP had limitations that defeated me -
particularly for such a large book. Another issue with the FOP route,
at least at the moment, was that the publisher wasn't really ready for
it.


I see these issues as temporary. As we get better XSL-FO tools,
then that will be an obvious way to produce print-ready output. When I
next need to produce print ready output, I'll give XSL-FO another look.


What I ended up doing was reverting to my trusty Framemaker. I
did this by generating Framemaker files automatically from the XML. I
did this in two stages. The first was an XSLT transform that converted
the tags I used for  [P of EAA](https://martinfowler.com/books/eaa.html) to tags that mirrored the subset of Frame
I was using. Then I used a Ruby script to convert from the Frame like
XML to Frame's textual MIF format file. Using XSLT for the first step
worked well in doing all the hard futzing with the transform, but XSLT
isn't good for handling the precise text format needed by Frame. The
combination of XSLT and Ruby worked perfectly.


Another option that's now available for XML to print is to use
Open Office. Open Office's file formats are zipped XML and they take
care to separate content from formatting. As such it should be
straightforward to use XSLT to transform the content and add the
formatting separately in Open Office. The future version of Microsoft
Word may well also support this kind of thing.


## Diagrams


My writing often contains diagrams, particularly UML diagrams,
and I'm often asked what I use for that. I've long avoided fancy CASE
tools in preference to Visio - and even with Visio I don't use the
standard UML templates that come with the product. The trouble with
CASE tools, and with Visio's UML templates, is that they try to be
intelligent. However their intelligence about UML is a lot less than
the average developer, so instead the tools just get in the way.


As a result I use a different set of templates developed by
Pavel Hruby (see my [links](https://martinfowler.com/links.html) page for the link).


The big frustration with Visio is that it has annoying glitches
on its output. When you output to gif, for example, the results are
not too good, frequently chopping the very top line of the figure. I'm
looking forward to more browser support for SVG and will probably
experiment with Open Office's draw capabilities in the future to see
if it produces a better result.


One big thing I didn't do right away, was to have a script to
automatically export all Visio diagrams to gif. I did this later on
(it checks to see if the Visio file was modified after the
corresponding gif was produced). Once I had the script life was much
easier - fortunately Visio is really easy to drive with pretty much
any scripting language (in my case, Ruby).


## Automatic Code Import


One of the nicest things about using this scheme was automatic
code import for my sample code. Most authors have nightmares on sample
code, almost always something goes wrong and they have sample code
that isn't consistent or doesn't compile - just due to the
difficulties of keeping copy and pasted code in sync.


I was able to do things much better. All my code examples were
kept in directories where I could use Ant to build and test the whole
directory. I could then tag the source code file with commented tags
to mark sections of code to import into the book. I then wrote some
simple Java code to whip through the source files and produce XML
files that contained the fragments from the source code. These
fragments could then be easily imported into output when I ran the
XSLT. It was a wondrous removal of what otherwise is such a messy
process, and allowed me to confidently change my code examples
whenever I needed to.


## Collaboration and Versioning


I collaborated with several people on  [P of EAA](https://martinfowler.com/books/eaa.html) - most
noticeably David Rice who wrote a large section of the book. With us
both modifying both text and code examples we needed to coordinate our
work carefully.


The answer was CVS. Since XML files are just text, CVS proved a
perfect way to handle our collaboration. Any time we modified anything
we uploaded the files to CVS. This became essential as we pushed
against the deadline with David working in Australia.


Of course CVS was useful just for me personally. It allowed me
to safely mess with the text any time I liked, knowing there was
always a solid version history of every file. We versioned everything,
including the various java libraries and .NET assemblies that our stuff
depended on. Just as programmers should always work with version
control, so should authors!


## Final Thoughts


Even in these early days of XML related technologies, I found
XML a really good way to write a major book. I now use it without
hesitation for almost all the writing I do - including this
article. (The main exception is when I'm doing my IEEE Software
column, they like to receive Word files and it's short enough that I
don't get the other usual problems.)


If you're wondering about using XML for a web site, report, or
book; I'd  warmly recommend it if you're a geek and happy to mess
around with XSLT, scripts and the like. If you're less geeky then I'd
wait for the moment - but keep a sharp eye on XML-aware word
processors. If the new Word is anything like the rumors, things will
get interesting.


---
