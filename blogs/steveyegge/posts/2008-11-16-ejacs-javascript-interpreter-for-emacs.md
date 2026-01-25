---
title: "Ejacs:  a JavaScript interpreter for Emacs"
date: 2008-11-16
url: https://steve-yegge.blogspot.com/2008/11/ejacs-javascript-interpreter-for-emacs.html
word_count: 3930
---

So!  I have all these cool things I want to write about, but I broke my thumbnail.  Can you tell that's a long story?
See, this summer I got excited about playing guitar again.  I usually switch between all-guitar and all-piano every other year or so.  This summer I dusted off the guitars and learned a bunch of pieces, and even composed one.  I was prepping for — among other things — a multimedia blog entry.  It was going to have a YouTube video, and a detailed discussion of a wacky yet powerful music programming language you've probably heard of but never used, and generally just be really cool.
And then it all came crashing down when I busted my thumbnail off.  And I mean
*off*
— it broke off at least a quarter inch below where the nail and skin meet.  Ick.  I just accidentally jabbed my steering wheel, and that was that.
I remember reading an interview with some dude who said he had punched a shark in the nose.  He said it was like punching a steering wheel.  So now I know more or less what it's like to punch a shark in the nose, I guess.  There's always an upside!
Anyway, that was going to be my magnum opus (literally: Op. 1) for the year, but it fell through for now.  I'll have to revisit the idea next year.  My thumbnail's back, but it's been at least 2 months since I touched my guitar, so I'll have to start over again.
Work has been extraordinarily busy, what with having to collect all these Nuka-Cola Quantum bottles and so on.  I'm sure you can imagine.  So I haven't had much time to blog lately.
But I do like to publish at least once a month, whether or not anyone actually cares.  It's been about a month, or it feels that way anyway, and all I have to show for it is this box of Blamco Mac and Cheese.
So I'm cheating this month.
You know how on Halloween how you walk around in your costume holding your little bag and you say "trick or treat", and every once in a while some asshole does a trick instead of dumping half a pound of candy into your bag?  And then he has to explain to all the dumbfounded and unhappy kids that "Trick or Treat" means that a trick is perfectly legal according to the semantics of logical-OR, and the kids remember that a-hole for the rest of their childhoods and avoid his house next year?
Yeah.
So I'm doing a trick this time.  Hee.  It's actually kind of fun when you're on the giving end.
My trick is this:  in lieu of saying anything meaningful or contemporarily relevant, I'm writing about something I did over a year ago.  And there isn't much to say, so this really will be short.
**Ejacs**
Around a year ago, I wrote a blog called
[Stevey's Boring Status Update](http://steve-yegge.blogspot.com/2007/12/boring-stevey-status-update.html)
, mostly in response to wild rumors that I'd been fired from Google.  Not so.  Not yet, anyway.
In that blog I mentioned I was working nights part-time (among other things) on a JavaScript interpreter for Emacs, written entirely in Emacs Lisp.  I also said I didn't have a name for it.  A commenter named Andrew Barry suggested that I should
**not**
call it Ejacs, and the name stuck.
Ejacs is a port of
[Narcissus](http://mxr.mozilla.org/mozilla/source/js/narcissus/)
.  Narcissus is a JavaScript interpreter written in JavaScript, by Brendan Eich, who by pure unexpected coincidence is also the inventor of JavaScript.  Narcissus is fairly small, so I thought it would be fun to port it to Emacs Lisp.
It turns out Narcissus is fundamentally incomplete.  It cheats.  It's that trick guy on Halloween.  Narcissus has a working parser and evaluator, but for its runtime it calls JavaScript.  So it's kind of like saying you're building a car by starting from scratch, using absolutely nothing except for a working car.
This meant I wound up having to write my own Ecma-262 runtime, so that the evaluator would have something to chew on.  In particular, the Ecma-262 runtime consists of all the built-in properties, functions and objects: Object, Function, Array, String, Math, Date, RegExp, Boolean, Infinity, NaN, parseInt, encodeURIComponent, etc.  A whole bunch of stuff.
I basically did this by reading the
[ECMA-262 specification](http://www.ecma-international.org/publications/standards/Ecma-262.htm)
and translating their algorithms into Emacs-Lisp.  That spec is lousy for learning JavaScript, but it's absolutely indispensable if you're trying to
*implement*
JavaScript.
I didn't know Emacs-Lisp all that well before I started, but boy howdy, I know it now.
Emacs actually has a pretty huge runtime of its own — bigger than you would ever, ever expect given its mundane title of "text editor".  Emacs has arbitrary-precision mathematics, deep Unicode support, rich Date and Calendar support, and an extensive, fairly complete operating system interface.  So a lot of the porting time was just digging through Emacs documentation (also extensive) looking for the Emacs version of whatever it was I was porting.  That was nice.
I had big plans for Ejacs.  I was going to make it a full-featured, high-performance JavaScript interpreter, with all the Emacs internals surfaced as JavaScript native host objects, so you could write Emacs customizations using object-oriented programming.  It was totally going to be the "meow" part of the cat.
And then I broke my thumbnail.
Actually, what happened was js2-mode.
**js2-mode**
After I got the interpreter working, I was at this crossroads.  There were two big use cases: a JavaScript
*editing*
mode, or a JavaScript
*Emacs development*
mode.  Both were going to be a lot of work.
It turns out you really want the editing mode first, if possible, so that when you're doing all your JavaScript programming you have a decent environment for it.  So I picked the editing mode.
Unfortunately I found the Ejacs parser wasn't full-featured enough for my editing needs, since at the time I was working on my Rhino-based Rails clone and writing tons of
[JavaScript 1.7](https://developer.mozilla.org/en/New_in_JavaScript_1.7)
code on the JVM.
I spent a little time trying to beef up the parser, then realized it would be a lot faster to just rewrite it by porting Mozilla Rhino's parser, which is (only) about 2500 lines of Java code.  Ejacs is something like 12,000 lines of Emacs-Lisp code, all told, so that didn't seem like a big deal.
So I jumped in, only to find that while the parser is 2500 lines of code, the scanner is another 2000 lines of code, and there's another 500 or so lines of support code in other files.  So I was really looking at porting 5000 lines of Java code.
Moreover, the parse tree Rhino builds is basically completely incompatible with the Ejacs parse tree.  It was richer and more complex, and needed more complicated structures to represent it.
So after I'd ported the Rhino parse tree, what I really had was a different code base.  I went ahead and finished up the editing mode, or at least enough to make it barely workable (another 5000 lines of code), and launched it.  It was a surprisingly big effort.
And it left poor Ejacs lying unused in the basement.
So today, faced with nothing to write about, I figured I'd dust off Ejacs, launch it with lots of fanfare, and then you'd hardly notice that I cheated you.  Right?
You're not coming to my house next year.  I can tell already.
Anyway, here's the code:
[http://code.google.com/p/ejacs/](http://code.google.com/p/ejacs/)
There's a README and a Wiki and installation instructions and stuff.  I can't remember how to put the code in SVN, and I'm having trouble finding it on the code.google.com site.  As soon as I figure it out I'll also make it available via SVN.
**Emacs Lisp vs. JavaScript**
In the interests of having
*something*
resembling original worthwhile content today, I'll do a little comparison of Emacs Lisp and JavaScript.  I know a lot about both languages now, and a few folks mentioned that a comparison would be potentially interesting.
Especially since I think JavaScript is a better language.
So... the best way to compare programming languages is by analogy to cars.  Lisp is a whole family of languages, and can be broken down approximately as follows:
- Scheme is an exotic sports car.  Fast.  Manual transmission.  No radio.
- Emacs Lisp is a 1984 Subaru GL 4WD:  "the car that's always in front of you."
- Common Lisp is Howl's Moving Castle.

This succinct yet completely accurate synopsis shows that all Lisps have their attractions, and yet each also has a niche.  You can choose a Lisp for the busy person, a Lisp for someone without much time, or a Lisp for the dedicated hobbyist, and you'll find that no matter which one you choose, it's missing the library you need.
Emacs Lisp can get the job done.  No question.  It's a car, and it moves.  It's better than walking.  But it pretty much combines the elegance of Common Lisp with the industrial strength of Scheme, without hitting either of them, if you catch my drift.
Anyway, here's the comparison.  Here's why I think JavaScript is a better language than Emacs Lisp.
**Problem #1:  Momentum**
A recurring theme is that Elisp and JavaScript both will both exhibit a particular problem, and there are specific near-term plans to fix it in JavaScript, but no long-term plans to fix it in Elisp.
It's easier to resign yourself to a workaround when you know it's temporary.  If you know the language is going to be enhanced, you can even design your code to accommodate the enhancements more easily when they appear.
People are working on improving JavaScript.  It's not happening quite as fast as I'd hoped earlier this year, but it's still happening.  As far as I know, Emacs Lisp is "finished" in the sense that no further evolution to the language is deemed necessary by the Emacs development team.
**Problem #2:  No encapsulation**
Every symbol in Emacs-Lisp is in the global namespace.  There is rudimentary support for hand-rolled namespaces using obarrays, but there's no equivalent to Common Lisp's
, making obarrays effectively useless as a tool for code isolation.
The only effective workaround for this problem is to prefix every symbol with the package name.  This practice has become so entrenched in Emacs-Lisp programming that many packages (e.g.
and the
elisp profiler) rely on the convention for proper operation.
The main adverse consequence of this problem in practice is program verbosity; it makes Emacs-Lisp more difficult to read and write than Common Lisp or Scheme.  It can also have a non-negligible impact on performance, especially of interpreted code, as the prefix characters can approach 5% to 10% of total program size in some cases.
The problems run slightly deeper than simple verbosity.  Without namespaces you have no real encapsulation facility: there is no convenient way to make a "package-private" variable or function.  In practice there's little problem with program integrity; it's hard for an external package to change a "private" variable inadvertently in the presence of symbol prefixes.  However, it makes it annoyingly difficult for users of the package to discern the "important" top-level configuration variables and program entry points from the unimportant ones.  Elisp attempts a few conventions here, but it's a far cry from real encapsulation support.
JavaScript also lacks namespaces.  They're being added in ES/Harmony, but in the meantime, browser JavaScript code typically uses the same name-prefixing practice as Emacs-Lisp.
However, JavaScript has lexical closures, which provide a mechanism for creating private names.  One common encapsulation idiom in browser JavaScript is to wrap a code unit in an anonymous lambda, so that all the functions in the code unit become nested functions that close lexically over the top-level names in the anonymous lambda.  This trick is nowhere near as effective in Emacs-Lisp, for several reasons:
- elisp is not lexically scoped and has no closures
- elisp nested defuns are still entered into the global namespace
- CL's ``flet'` and `labels' are only weakly supported, via macros, and they frequently confuse the debugger, indenter, and other tools.

Some elisp code (e.g. much of the code in cc-engine) prefers to work around the namespace problem by using enormous functions that can be thousands of lines long, since let-bound variables are slightly better encapsulated.  Even this is broken by elisp's dynamic scope:

```
(defun foo ()  (setq x 7))(defun bar ()  (let ((x 6))    (foo)    x))  ; you would expect x to still be 6 here(bar)7  ; d'oh!
```

So let-bound variables in elisp can still be destroyed by your callee: a dangerous situation at best.
Emacs is basically one big program soup.  There's almost no encapsulation to speak of, and it hurts.
**Problem #3:  No delegation**
One of the big advantages to object-oriented programming is that there is both syntactic support and runtime support for automatic delegation to a "supertype".  You can specialize a type and delegate some of the functionality to the base type.  Call it virtual methods or prototype inheritance or whatever you like; most successful languages support some notion of automatic delegation.
Emacs Lisp is a lot like ANSI C:  it gives you arrays, structs and functions.  You don't get pointers, but you do get garbage collection and good support for linked lists, so it's roughly a wash.
For any sufficiently large program, you need delegation.  In Ejacs I wound up having to implement my own virtual method tables, because JavaScript objects inherit from
(and in some cases,
, which inherits from
).
Writing your own virtual method dispatch is just not something you should have to do in 2008.
**Problem #4:  Properties**
I wrote about this at length in a recent blog post,
[The Universal Design Pattern](http://steve-yegge.blogspot.com/2008/10/universal-design-pattern.html)
.  JavaScript is fundamentally a properties-based language, and it's really nice to be able to just slap named properties on things when you need a place to store data.
Emacs Lisp only offers properties in the form of simple plists – linked lists where the odd entries are names and the even entries are values.  Symbols have plists, and symbols operate a little bit like very lightweight Java classes (in that they're in the global namespace), but that only gets you so far.  If you want the full JavaScript implementation of the Properties Pattern, you'll have to write a lot of code.
And so I did.  Your implementation choice for object property lists has a huge impact on runtime performance.  Emacs has hashtables, but they're heavyweight:  if you try to instantiate thousands of them it slows Emacs to a crawl.  So they're no good for the default
property list.  Emacs also has associative arrays (alists), but their performance is O(n), making them no good for objects with more than maybe 30 or 40 properties.
I wound up writing a hybrid model, where the storage starts with lightweight alists, and as you add properties to an object instance, it crosses a threshold (I set it to 50, which seemed to be about right from profiling), it copies the properties into a hashtable.  This had a dramatic increase in performance, but it was a lot of work.
I experimented with using a splay tree.  I implemented Sleater and Tarjan's splay tree algorithm in elisp; Ejacs comes with a standalone
that you can use in your programs if you like.  I was hoping that its LRU cache-like properties would help, but I never found a use case where it was faster than my alist/hashtable hybrid, so it's not currently used for anything.
And then in the end, after I was done with my implementation, it was a
*library*
(at least from the Emacs-Lisp side of the house).  It wasn't an object system for Lisp.  It's only really usable inside the JavaScript interpreter, where it has syntactic support.
You really want syntactic support.  Sure, people have ported subsets of CLOS to Emacs Lisp, but I've always found them a bit clunky.  And even in CLOS it's hard to implement the Properties Pattern.  You don't get it by default.  CLOS has lots of support for compile-time slots and virtual dispatch, but very little support for dynamic properties.  It's not terribly hard to build in, but that's my point:  for something that fundamental, you don't want to have to build it.
**Problem #5:  No polymorphic `toString`**
One of the great strengths of JavaScript is the
extension.  I don't know if they support it over in IE-land; I haven't been a tourist there in a very long time.  But in real versions of JavaScript, every object can serialize itself to source, which can then be eval'ed back to construct the original object.
This is even true for functions!  A function in JavaScript can print its own source code.  This is an amazingly powerful feature.
In Emacs Lisp, some objects have first-class print representations.  Lists and vectors do, for instance:

```
(let ((my-list '()))  (push 1 my-list)  (push 2 my-list)  (push 3 my-list)  my-list)(3 2 1)(let ((v (make-vector 3 nil)))  (aset v 0 1)  (aset v 1 2)  (aset v 2 "three")  v)[1 2 "three"]
```

But in Emacs Lisp, many built-in types (notably hashtables and functions) do NOT have a way to serialize back as source code.  This is a serious omission.
Also, trying to print a sufficiently large tree made entirely of
s will crash Emacs, which caused me a lot of grief until I migrated my parse tree to use a mixture of defstructs and lists.  Note that simply typing the name of a defstruct, or passing over it ephemerally in the debugger, will cause Emacs to try to print it, and crash.  Fun.
The problem of polymorphic debug-printing (or text-serialization) is, I think, a byproduct of Emacs not being object-oriented.  If you want a debug dump of a data structure, you write a function to do it.  But Emacs provides a half-assed solution:  it debug-prints lists very nicely, even detecting cycles and using the #-syntax for representing graph structures (as does SpiderMonkey/JavaScript).  But it has no useful debugging representation for hashtables, functions, buffers or other built-in structures, and there's no way to install your own custom printer so that the debugger and other subsystems will use it.
So it sucks.  Printing data structures in Emacs just sucks.
The situation in Ecma-262-compliant JavaScript really isn't that much better, although you can at least install your own
on the built-ins.  But any competent "server-side" JavaScript implementation (i.e. one designed for writing real apps, rather than securely scripting browser pages) has a way to define your own non-enumerable properties, so you can usually override the default behavior for things like
and
.
And all else being equal, at least JavaScript functions print themselves.
**Emacs advantages:  Macros and S-expressions**
Pound for pound, Emacs Lisp seems roughly as expressive as JavaScript or Java for writing everyday code.  It shouldn't be that way.  Emacs Lisp ought to be more succinct because it's Lisp, but it's incredibly verbose because of the namespace problem, and it's also verbose to the extent that you want to use the properties pattern without worrying about alist or hashtable performance.
Elisp does have a few places where it shines, though.  One of them is the
(Common Lisp emulation) package, which provides a whole bunch of goodies that make Elisp actually usable for real work.  Defstruct and the loop macro are especially noteworthy standouts.
Some programmers are still operating under the (ancient? legacy?) assumption that the
package is somehow deprecated or distasteful or something.  They're just being silly; don't listen to them.  Practicality should be the ONLY consideration.
The
package wouldn't have been possible without macros.  JavaScript has no macros, so even though it has better support for lambdas, closures, and even (in some versions) continuations, there are still copy/paste compression problems you can't solve in JavaScript.
Emacs Lisp has
, which makes up for a LOT of its deficiencies.  However, it really only has one flavor.  Ideally, at the
*very*
least, it should support reader macros.  The Emacs documentation says they were left out because they felt it wasn't worth it.  Who are they to make the call?  It's the users who need them.  Implementer convenience is a pretty lame metric for deciding whether to support a feature, especially after 20 years of people asking for it.
Elisp is s-expression based, which is a mixed bag.  It has some advantages, no question.  However, it fares poorly in two very common domains:  object property access, and algebraic expressions.
JavaScript is NOT s-expression based (or it wouldn't be a successful language, many would argue), but it does offer some of the benefits of s-expressions.  JSON is one such benefit.  JavaScript's declarative object literals (or as a Lisp person would say, "syntax for hashes") and arrays provide a powerful mechanism for designing and walking your own declarative data structures.
JavaScript also has all the usual (which is to say, expected) support for algebraic operators.  And unlike Java, JavaScript even got the precedence right, so it's not full of redundant parentheses.
**Overall Comparison**
In the end, it comes down to personal choice.  I've now written at least 30,000 lines of serious code in both Emacs Lisp and JavaScript, which pales next to the 750,000 or so lines of Java I've crapped out, and doesn't even compare to the amount of C, Python, assembly language or other stuff I've written.
But 30,000 lines is a pretty good hunk of code for getting to know a language.  Especially if you're writing an interpreter for one language in another language:  you wind up knowing both better than you ever wanted to know them.
And I prefer JavaScript over Emacs Lisp.
That said, I suspect I would
*probably*
prefer
[Clojure](http://clojure.org)
over Rhino, if I ever get a chance to sit down with the durn thing and use it, so it's not so much "JavaScript vs.
*Lisp*
" as it is vs. Emacs Lisp.
I would love to see Emacs Lisp get reader macros, closures, some namespace support, and the ability to install your own print functions.  This reasonably small set of features would be a huge step in usability.
However, for the nonce I'm focusing on JavaScript.  I've found that JavaScript is a language that smart people like.  It's weird, but I keep meeting really really smart people, folks who (unlike me) are actually intelligent, and they like JavaScript.  They're always a little defensive about it, and almost a little embarrassed to admit it.  But they think of it as an elegant, powerful, slightly flawed but quite enjoyable little language.
I tell ya:  if you're a programming language, it's a very good thing to have smart people liking you.
It doesn't make me smart, but I kinda like it too.  Even though there's (still) a lot of hype these days about Java, and people tootling on about how Java's going to be the next big Web language... I just don't see it happening.  There are too many smart people out there who like JavaScript.
So enjoy the interpreter.  Ejacs is just a toy, but I think it also shows a kind of promise.  Scripting Emacs using JavaScript (if anyone ever actually implements it) could be really interesting.  It could open up the world's most powerful, advanced editing environment to millions of people.  Neat.
In the meantime, it doesn't actually do squat except interpret EcmaScript in a little isolated console, so don't get your hopes up.
Reminder — here's the Ejacs URL:
[http://code.google.com/p/ejacs](http://code.google.com/p/ejacs)
- enjoy!
And with that, I'm off to find some Nuka-Cola Quantum.  I just wish those bastards hadn't capped me at level 20.