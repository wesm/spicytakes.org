---
title: "js2-mode:  a new JavaScript mode for Emacs"
date: 2008-03-30
url: https://steve-yegge.blogspot.com/2008/03/js2-mode-new-javascript-mode-for-emacs.html
word_count: 4299
---

I've written a new JavaScript editing mode for GNU Emacs, and released it on
[code.google.com](http://code.google.com/p/js2-mode/)
.
This is part of a larger project, in progress, to permit writing Emacs extensions in JavaScript instead of Emacs-Lisp.  Lest ye judge:  hey, some people swing that way.  The larger project is well underway, but probably won't be out until late summer or early fall.
My new editing mode is called
[js2-mode](http://code.google.com/p/js2-mode/wiki/InstallationInstructions)
, because eventually I plan to support JavaScript 2, also known as
[ECMAScript Edition 4](http://www.ecmascript.org)
.  Currently, however, it only supports up through
[JavaScript 1.7](http://developer.mozilla.org/en/docs/New_in_JavaScript_1.7)
, so the name is something of a misnomer for now.
It's almost ten thousand lines of elisp (just for the editing mode), which is more than I'd expected.  So I figured I'd tell you a little about what it does, why I made certain choices, and what's coming up next.  Even if you're not a JavaScript user, you might find the technical discussion mildly interesting.

## Features

In no particular order, here's what
currently supports.

## M-x customize

All the user-configurable variables are defined as Custom variables for use with
.  This means you can type

```
M-x customize-group RET js2-mode RET
```

to see a list of all the configuration options.
All the colors used for syntax highlighting are defined in the same
customization group, for convenience.
Many people complain that Emacs's Customize feature is lame.  I thought so too, for a long time, and I'm certainly not claiming it's as good as a "real" UI.  But I now appreciate that it gets the job done admirably for a text editor:  there are no dependencies on GUI widgets, and you can use the Customize package over an ssh or telnet session.  That's at least
*kind*
of cool.

## Accurate syntax highlighting

This mode includes a recursive-descent parser that I ported from
[Mozilla Rhino](http://www.mozilla.org/rhino)
.  That means it's always right.  It doesn't use heuristics or guesswork; it's exactly the same parser used by JavaScript engines.  If it's ever wrong, then it's a bug in my code, and it's fixable.
The amount of syntax highlighting is configured by a variable called
.  It ranges from 0 to 3, with the default set at 2.  Zero (or nil/NaN) means no highlighting.  level 1 does basic syntax highlighting:  keywords and declarations.    Level 2 adds highlighting for Ecma-262 builtins (and SpiderMonkey extensions) such as
,
and
.  Level 3 adds highlighting for all built-in functions and properties for all native JavaScript objects (
,
,
and so on.)
The highlighting faces are my own choices, because I felt it was important for me to foist my personal style choices on the general public.  Actually, that's only partly true:  it's also because I like the color schemes employed by Eclipse and IntelliJ better than the default Emacs color scheme.  So comments are green (not red!), keywords are blue, strings are soft blue, var decls are sea green, and so forth.
Fortunately for those (hopefully few) among you who love blood-red comments, you can add this to your .emacs file to make
honor your font-lock settings:

```
(setq js2-use-font-lock-faces t)
```

Or, alternately,
and set the value to
, which is Lisp for "true".  This particular variable requires an Emacs restart to take effect.
I just added a TODO item for myself:  define Eclipse and IntelliJ color schemes that you can choose from.  Should be pretty easy.

### Asynchronous highlighting

Unlike most other Emacs modes (but like
[nXML mode](http://www.thaiopensource.com/nxml-mode/)
),
does not use font-lock-mode, which is the standard Emacs infrastructure for doing syntax-coloring in buffers.
Although font-lock is quite fast and fairly flexible, it still uses heuristics to figure out what to highlight, and they can occasionally be wrong.  If you've ever opened up
in Emacs and seen the second half of the file turned string-blue on account of being confused over a regular expression literal with a quote in it, you know what I'm talking about.
James Clark's nXML-mode does its own syntax coloring without using font-lock.  It can do this because James wrote his own, fully-compliant, validating XML parser, so adding colors was a snap.  I thought this was pretty macho, and since I also happen to have a full parser, I blatantly copied his idea.
For the OOD-loving and API-minded among you, the "beautiful" way to do syntax coloring would have been to finish parsing,
*then*
walk the AST using a Visitor interface, applying the coloring in a second pass.  I tried it, and it was, as they say, "butt slow".  In fact (perhaps not surprisingly) walking the AST takes exactly as long as parsing, so it was twice as slow as doing it inline.
So I bit the bullet and moved my syntax-coloring to happen inline with parsing.  Fortunately it only introduced about 30 lines of code to the 4000-line parser/scanner, because most of the coloring happens in the scanner, at the token level.  Go figure.
Unfortunately, my parser is asynchronous.  It "sort of" happens on another thread, although what's really happening is that it waits for Emacs to become idle and parses until you hit a key or use the mouse.  I wanted it to be synchronous, boy howdy I did, but it just wasn't quite fast enough.  It can parse about 5000 lines a second, give or take, but for any file longer than 1000 lines or so, the parsing was happening
*every time you typed a key*
(that's what synchronous means, obviously), and the 0.2+ second delay became painfully noticeable.
I had two options:  incremental parsing, or asynchrous parsing.  Clearly, since I'm a badass programmer who
[can't recognize my own incompetence](http://www.sfgate.com/cgi-bin/article.cgi?file=/chronicle/archive/2000/01/18/MN73840.DTL)
, I chose to do incremental parsing.  I mentioned this plan a few months ago to
[Brendan Eich](http://en.wikipedia.org/wiki/Brendan_Eich)
, who said:  "Let me know how the incremental parsing goes."  Brendan is an amazingly polite guy, so at the time I didn't realize this was a code-phrase for:  "Let me know when you give up on it, loser."
The basic idea behind incremental parsing (at least, my version of it) was that I already have these little functions that know how to parse functions, statements, try-statements, for-statements, expressions, plus-expressions, and so on down the line.  That's how a recursive-descent parser works.  So I figured I'd use heuristics to back up to some coarse level of granularity — say, the current enclosing function – and parse exactly one function.  Then I'd splice the generated syntax tree fragment into my main AST, and go through all the function's siblings and update their start-positions.
Seems easy enough, right?  Especially since I wasn't doing full-blown incremental parsing: I was just doing it at the function level.  Well, it's not easy.  It's "nontrivial", a word they use in academia whenever they're talking about the Halting Problem or problems of equivalent decidability.  Actually it's quite doable, but it's a huge amount of work that I finally gave up on after a couple of weeks of effort.  There are just too many edge-cases to worry about.  And I had this nagging fear that even if I got it working, it would totally break down if you had a 5,000 line function, so I was kinda wasting my time anyway.
So, without telling Brendan (and don't you dare mention it to him), I switched to asynchronous parsing.  Actually, first I went around to my Eclipse- and IntelliJ-using friends, and I forced them to give me live demonstrations of Java editing on large files.  This is why I have so few friends.  It turns out that Eclipse and IntelliJ both use asynchronous parsing as well, which made me feel better about the basic approach.
Asynchronous parsing is pretty simple in principle:  when the user is typing, don't do anything.  Just let 'em type.  When they stop, start a timer for, say, a 200 to 500 millisecond delay, and when the timer expires, start parsing.  Every once in a while, see if they typed anything.  If so, stop parsing and let them type.
The main downside of this approach is that for some programmers, the 500-ms timer fires between every keystroke, so the file never actually finishes parsing.  (Yes, that was a mean joke.  I have a blog on this subject coming up; I'm declaring war on people too lazy to learn to type.)
Actually, now that I think about it, I did mention my change of heart (and asynchronous approach) to Brendan a week or two ago, and he jumped immediately to the smart-guy conclusion:  I need continuations.  Fortunately I'd thought of this, albeit not in the 200 milliseconds it took him to arrive at that conclusion (over wine, no less!), so I was able to retort:  "um, yeah... it's in my to-do list.  Right now I hack it."
And hack it I do!  I rely on the fact that my parser does 5000 lines a second, so if the parse gets interrupted, at
*some point*
even the fastest, most dedicated typist will have to pause for a second, and I'll finish the parse (which in turn finishes the highlighting and error/warning reporting – see below).
Unfortunately (as Brendan instantaneously concluded), this means that if the parse gets 99.9% complete, and you hit the up-arrow, it abandons the entire parse (and parse tree built so far), starting from scratch again when Emacs goes idle.  So if you open a big file (like
[prototype.js](http://www.prototypejs.org/assets/2008/1/25/prototype-1.6.0.2.js)
) and start navigating around it, you may not see any results until you stop typing or scrolling.
The proper fix will be to record where I'm at, and pick up where I left off when I restart the parse.  That's what nxml-mode does, but I'm forced to concede that James Clark is way cooler than I am.  If you have a multi-threaded system, then it's trivial, and if your system supports continuations, it's also trivial.  But Emacs has neither of these.
Instead, I pause every 100 statements or so (this is a lame heuristic, I agree) and check for user input.  Since I'm pausing at the top level of the parser, in the loop where it consumes whole statements, I really don't need to store that much information to fake a continuation, so this problem is eminently fixable.
But I had to release this thing eventually, which meant drawing the line somewhere.  So for now it has asynchronous full-restart parsing.  This means that as you edit the file, just like in Eclipse and IntelliJ, it can take a second or two for the parser to catch up with you after you pause.
It doesn't (or shouldn't) interfere with your editing, though, so hopefully this isn't a big issue.

### Missing highlighting

It's on my
TODO list to highlight
[E4X](http://en.wikipedia.org/wiki/E4X)
literals.  E4X is a JavaScript language extension (an official Ecma standard, in fact) that allows you to embed XML literals in your JavaScript code and provides various XML operators and functions that let you do DOM-style manipulations and XPath-style queries, but with JavaScript-style syntax and semantics.
I parse these properly, but don't highlight them yet.  The Rhino parser just parses them as strings, so to get more accuracy I'll need to make my own little XML parser.  It must (I think) be my own little parser because E4X permits embedding arbitrary JavaScript expressions in curly-braces as a form of templating.  This complicates the XML parsing because you can find one or more
expressions in the middle of any XML element name, attribute name, attribute value, text node, or just about anywhere else that doesn't cross a quote or angle-bracket boundary.
I'll get around to it eventually.

## Indentation

I would have been publishing this article at
*least*
a month ago if it weren't for indentation.  No, six weeks, mininum.
See, I thought that since I had gone to all the thousands of lines of effort to produce a strongly-typed AST (abstract syntax tree) for JavaScript, it should therefore be really easy to do indentation.  The AST tells me exactly what the syntax is at any given point in the buffer, so how hard could it be?
It turns out to be, oh, about fifty times harder than incremental parsing.  Surprise!
Just to give you a feel for the size of the problem, the package
(including its cc-* helper packages) bundled with GNU Emacs 22 is approximately 27,000 lines of lisp code, and it's
*all*
dedicated to indentation.  There's a teeny tiny smattering of maybe 500 lines dedicated to filling, and sure, it supports several C-like languages, but let's face it:  25k lines for indenting?  27k lines of
*Lisp*
code?  (Meaning it would be, like, five times that much Java?)
What the hell is so hard about indentation?
For starters, in order to provide user-configurable indentation for every possible syntactic context, you need to name all the syntactic contexts.
defines about 70 syntactic positions in a data structure called
.  This is a map of
, where
can be a number (a multiple of the variable
), or a symbol specifying some multiple of
, or even a function to call to figure out how to indent.
It's pretty darn flexible.  And people still complain about it!  Apparently 70 different syntactic contexts isn't enough to let you specify your indentation exactly the way you like it.
Anyhoo, most existing JavaScript editing modes for Emacs use
and try to coerce it into indenting JavaScript properly.  This usually meets with lackluster results, since JavaScript is gradually drifting further and further from C.  So is Java, but someone actually bothers to try to keep
up to date for Java.
Here's the deal:  the
code for interpreting that
data structure (with all the indentation configuration options) is pretty small.  Most of the code goes to parsing and trying to figure out the current syntactic context.
You can probably guess what I tried to do.  I wanted to let people customize their
indentation much the same way they can customize their
or
indentation, using
.  So I figured I'd use the exact same configuration data structure, and use my parse tree to replace
(and the 25k lines of lisp code for implementing it!)
*(time passes...)*
Approximately one month later, I threw in the towel.  I renamed my
to
, and my
unit-test file to
, and gave up on this approach for the forseeable future.  1500 lines of painfully crafted lisp code down the drain.
Ugh.  Sure, it was only a few hours a week, but it still felt like a lot of work.  And it was a lot of calendar time.
Amazingly, surprisingly, counterintuitively, the indentation problem is
*almost totally orthogonal*
to parsing and syntax validation.  I'd never have guessed it.  But for indentation you care about totally different things that don't matter at all to parsers.  Say you have a JavaScript argument list:  it's just
:  a paren-delimited, comma-separated, possibly empty list of identifiers.  Parsing that is pretty easy.  But for indentation purposes, that list is rife with possibility!  You might want to indent it like this:

```
(blah,  blah, blah)
```

or this:

```
(  blah,  blah,  blah)
```

or this:

```
(blah,      blah,      blah)
```

or this:

```
(      blah,      blah, blah)
```

Let's face it:  you could be a total lunatic, and
*Emacs has to make you happy*
.  So instead of simply parsing a plain argument list, you need to determine and capture the (a) the fact that it looks like an argument list, (b) the position and indentation of the open-paren, (c) whether the cursor is before or after the open-paren, (d) whether the arg list is nonempty, (e) whether the cursor is before the first list element, (f) whether the cursor is on the line containing the closing paren, (g) whether there are any block or single-line comments interspersed between
*any*
of the list elements or parentheses, (h) whether the AAAAUGH, I can't
*stand it*
anymore!
The problem is, this explosion of "one case to arbitrarily many cases" occurs for every single grammatical construct in your language.  So if you have 70-ish such constructs (as JavaScript does - Java has almost double that, because of the type system), and each one expands to 5 to 10 possible indentation situations, well, you've got an awful lot of edge cases to deal with.
Worse, having a rich AST doesn't help you much.  You can figure out that it's an argument list, and possibly where the cursor is in the list, but you still have to grope around in the buffer looking for other contextual cues that matter for indentation but which the parser threw away.  So each syntactic case in the 700-odd scenarios I had to handle expanded to anywhere from 2 to 10 lines of lisp code.
I was about 1500 lines into my
(plus unit tests), and maybe (optimistically) 35% finished, when it occurred to me:  "is there a better way?"
**Karl Angalsdkjfadslkfj to the rescue**
I remembered that there are several javascript editing modes out there already, and none of them does a very good job (or I wouldn't be working on
).  But one of them, "javascript.el", I remembered as being pretty good at indentation.  It wasn't perfect, and I'd had to write some custom hacks for it here and there, but it was actually pretty decent.  How did it work?
I went and looked at it.  It's written by a guy named, according to the comment header, Karl LandstrÃ¶m.  I'd always assumed that this was just some my-font-doesn't-support-Unicode gobbledygook, and that his name was actually something more reasonable like Karl Landstr\301^HB^P\302\301!\204^0^@.  But upon closer inspection, I think he may be a fan of the artist formerly known as the artist formerly known as Prince, aka "Prince", because the "Ã¶" in his name shows up pretty consistently across platforms and fonts.  So it may be intentional.  Perhaps his parents were ardent mathematicians.
In any case, Karl Landstrlaksjdflaksjd is an amazingly clever guy, because his indenter, which beats the pants off all the JavaScript modes based on
, is only about 200 lines of elisp.  200!?  How does he do it?
Well, in a nutshell, he makes the inspired assumption that indentation is almost always a function of brace/paren/curly nesting level, and he uses a little-known built-in Emacs function called
, written in C, which tells you the current nesting level of not only braces, parens and curlies, but also of c-style block comments, and whether you're inside a single- or double-quoted string.  How useful!  Good thing JavaScript uses C-like syntax, or that function would have been far less relevant.
The rest of his code handles cases where you have a JavaScript keyword such as
,
or
(a "possibly braceless keyword"), where you can optionally leave off the curly-brace, and it should still indent one basic step for the nested statement.
The results are actually pretty darn good, and assuming you're reasonably flexible about where you position your parens and curly-braces, you can exert at least some control over the indentation.  (E.g. you can move a curly down to its own line and manually indent it, and subsequent lines will indent from that curly.)
Go Karl!
Unfortunately, it's not perfect (no solution so elegant could ever be, at least for a language based on the inelegant syntax of C), so I was faced with a dilemma:  should I pile hack upon hack until it becomes the new
?  Or is there another way?
Well, I've always been vaguely admiring of
's Emacs indentation, which chooses among various likely indentation points when you press TAB repeatedly.  Why not use that approach for JavaScript?
So that's what I wound up doing.  I put a
*few*
tweaks into Karl's original indenter code to handle JavaScript 1.7 situations such as array comprehensions, and then wrote a "bounce indenter" that cycles among N precomputed indentation points.
For any given line, there are some obvious possible indentation points:
- whatever position Karl's guesser wants to use
- the beginning of the line
- after the '=' if the previous line is an assignment
- same indentation as the previous line
- first preceding line with less indentation than the preceding line
I wrote a function that computes all these positions, based on heuristic parsing (NOT on my AST, which might not even be available yet if the parse is taking a while), and the TAB key cycles among them.
This moved the accuracy, at least for my own JavaScript editing, from 90% accurate with Karl's mode up to 99.x% accurate, assuming you're willing to hit TAB multiple times for certain syntactic contexts.
There are still plenty of user-defined situations (e.g. parts of Google's internal JavaScript style guide) that my guesser doesn't compute.  You don't want to compute
*every*
possible indentation point, or the TAB key degenerates into the space key modulo the line length, so at some point I'll add a customization hook that lets you write a function to help decide the right indentation.
Anyway, where was I.  Oh yeah.  Indentation is a real pain in the b-hind.  I'm glad to be (mostly) done with it.  At least hopefully you now understand why my mode isn't configurable the way other C-like modes are, and you sympathize with me.  Next time I have time to write ten thousand lines of indentation-related guessing, I'll fix it.
Meanwhile, if you find points where it doesn't do what you want, let me know (or post them on the
[Wiki](http://code.google.com/p/js2-mode/w/list)
), and I'll either hack them in or write that customization hook.

## Other Stuff

I didn't expect to spend so long on just syntax highlighting and indentation.  It's just the beginning!  Unfortunately I'm out of patience, and I'm guessing you are too.  So here's a short list of other features.

### Code folding

I support hiding function bodies and /*...*/ block comments as {...}.  It's in the menu.  Turn on
, or right-click in the buffer, to invoke these functions.
At some point I'll generalize it to hiding any curly-brace construct, the way Eclipse does.  This was just an experiment to see how easy it would be.  (Answer:  pretty easy!  Emacs has good built-in support for this kind of thing.)

### Comment and string filling

One neat trick I stole from Eclipse:  if you hit <Enter> inside a string literal, it will autoamtically turn it into a multi-line string concatenation.
You can also hit Alt-q (fill-paragraph) inside a comment or a string to see hopefully useful things happen.  Let me know if it doesn't do what you expect.

### Syntax errors

The mode highlights syntax errors in red.  This can be annoying as you type, but I'm told (by Eclipse/IntelliJ users) that you get used to it.
You can control this behavior via a customization variable.

### Strict warnings

JavaScript defines a whole bunch of strict-mode warnings:  things like "don't have a trailing comma in an Array or Object literal", or "your variable name conflicts with one of the function parameters".  I've implemented some of them, with more to come.  They get underlined in orange.
I actually found some bugs in live code I'd written with this feature.  Pretty cool!

### jsdoc highlighting

There's a program similar to javadoc called "jsdoc" that lets you do documentation comments for your JavaScript functions and other declarations.  It defines a similar set of
tags.  We use it at Google, albeit with limited success because it's a Perl program that core-dumps on most of our JavaScript code base.  My mode highlights the various tags in jsdoc comments, if you happen to use them.
It's possible that you'll notice it highlighting curly-brace constructs inside jsdoc comments, such as:

```
@return {SomeType} my return value
```

Googler Bob Jervis has written a type-inferencing engine for our JSCompiler, in his 20% time, that uses the type-tags we've defined in an enhanced version of jsdoc comments.  It's still pretty new, and we're planning to open-source it and integrate it with Mozilla Rhino at some point, but since it's 20% time, there's no telling when it'll be released.  But hopefully that'll explain the bizarre highlighting you might sometimes see.

## If this isn't good enough for you...

Well, you have three options.
First, you can whine about it.  If you whine in the appropriate places, such as the Wiki, then I'll eventually notice and try to fix whatever it is that's bothering you.
Next, you can offer to help.  I haven't uploaded the original source code, but I can certainly start doing so.  (The file
is generated from a little build script I wrote, to make installation easier.)  If you're a good Emacs-Lisp programmer, and you want to help make this mode better, let me know and we can get you hooked up!
Finally, if you can afford it (or if your company can afford it), consider using
[IntellIJ IDEA](http://www.jetbrains.com/idea/features/javascript_editor.html)
.  Yes, it's commercial, but if you spend even 30 seconds on their site it becomes apparent that "commercial" means "better".  Their JavaScript support is way better than mine, and is as far as I can tell the gold standard for JavaScript editing today.
Eventually I hope to be able to reach feature parity with IntelliJ, and it's certainly possible, but it'll be some work.  In the meantime, if you can't wait, give them a try!

## Wrap-Up

At this point I have to go to the bathroom so bad that I don't care what other features I've added.  You can look at the Wiki!
If you habitually (or even occasionally) use GNU Emacs to edit JavaScript, please give this mode a try!  It's probably got a fair number of bugs and usability issues, since it's brand-new, but it'll improve more quickly if you play guinea pig for a while.
Feel free to email me directly with comments, suggestions, or bug reports, or you can go to the Wiki and add your comments there.
Enjoy!