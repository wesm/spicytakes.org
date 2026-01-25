---
title: "Shiny and New:  Emacs 22"
date: 2006-06-10
url: https://steve-yegge.blogspot.com/2006/06/shiny-and-new-emacs-22.html
word_count: 5695
---

I finally upgraded to Emacs 22 a few weeks ago, and now I'm wishing I'd braved it sooner.  Technically it's not released yet; I'm working from a build of a cvs snapshot from a month or so ago.  But the Emacs dev team works pretty hard to make sure it has problem-free builds on a whole slew of platforms, so just following their instructions has a pretty good chance of working for you.
It's worth the effort.  Truly.  Reading through its NEWS file, there's just tons and tons of new functionality.  It's going to take me some time, maybe a few weekends, just to absorb it all.
Personally, though, I think there are two features that by themselves justify the entire effort of upgrading:  the Unicode and UTF-8 support, and the enhanced
command.

### International At Last

It's been a
*very*
long wait for Unicode and UTF-8 support, and now that I have it, I could never go back.  There isn't much to say about it, except that it works.  Seamlessly.  It used to be hard to get international characters into and out of Emacs, because it had its own custom way of dealing with them.  Now it's a snap.
In fact — here, I'll show ya.  If you type
, it brings up the HELLO file, which contains greetings in a variety of languages.  Here's some Chinese:  中文,普通话,汉语.  Here's some Korean:  안녕하세요, 안녕하십니까.  Here's some Russian:  Здравствуйте!
I'm not doing anything special; I'm just copying the strings out of the HELLO buffer and into my html buffer, and saving the file.   I added the content-type header line in this HTML file, and all the characters just show up effortlessly in Firefox.
If you can't see them in your browser, well... Firefox is
[free](http://www.mozilla.com/firefox)
.  Or it might be a font problem on your system.  As far as I'm concerned, any problems you may have in viewing them is no longer the fault of my Emacs session, which makes me Happy.  Speaking as a developer who needs to internationalize every program I write, I can't begin to tell you how useful it's been to have seamless editing of utf-8 encoded files for the past month.
Right there, that feature alone is worth the upgrade.
But wait, there's more... Even though Emacs 22 has a
*bunch*
of noteworthy and exciting new features, blah blah blah, I'm going to blithely ignore them all today and focus with single-minded zeal on just one feature.  It has a teeny tiny entry in the NEWS file; it's barely mentioned, really.  I'm sure it was a thousand times less work than the UTF-8 support, but even so, it might well be strong enough on its own to justify the (moderate) pain of upgrading from Emacs 21.
Take a look at my examples and see if you agree!

### Replacement Super-Powers

Emacs 22 sports an amazing new editing feature that's had me drooling in anticipation since I first heard about it, maybe six or eight months ago.  As you can well imagine, that's a lot of drool.
And what might the feature be, you ask?  Well, they've enhanced
to accept lisp expressions to be evaluated in the replacement string.
That might not seem like a big deal, so let's run through some examples, from simple to very fancy.

#### Example:  Changing Case in Replacement Strings

Have you ever wanted to change the case of certain letters in the replacement string for
?  It used to be a real pain; you either had to write a Lisp function or fix them all by hand.  Now it's trivial.
As a simple demonstration, let's say you have a list of names that you need capitalized, like so:

```
bobsueralphalicejimmyprestonbilly joe jim bob
```

It's a contrived example, since Emacs already has
.  Or you could use
.  But let's try it with the new
evaluation feature to see how it works.
It's just like a normal
, but you'll prefix any lisp expressions in the replacement string with the sequence `
' (i.e., a backslash and a comma).  In this case, we match the whole word, and invoke the Emacs-Lisp function `
' to capitalize the word we just matched:

```
M-x replace-regexp  Replace regexp:  \(\w+\)  Replace regexp with:  \,(capitalize \1)
```

and we wind up with each word capitalized, just like we wanted:

```
BobSueRalphAliceJimmyPrestonBilly Joe Jim Bob
```

Unlike the
commands, which have hardwired behavior, the
commands give us tremendous flexibility.  For instance, we could have capitalized the last letters of the names instead, by splitting each word into two regexps, with the second regexp matching just the last character.  Then it's a simple matter to reconstruct the word with the last letter capitalized:

```
M-x replace-regexp  Replace regexp:  \(\w+\)\(\w\)  Replace regexp with:  \1\,(capitalize \2)
```

..to get the reverse capitalization we wanted:

```
boBsuEralpHalicEjimmYprestoNbillY joE jiM boB
```

For a somewhat more realistic example, let's say you've defined some "getter" functions in a Java class, like so:

```
  public Relative father() { return this.father; }  public Relative mother() { return this.mother; }  public Relative sister() { return this.sister; }  public Relative brother() { return this.brother; }  public Relative auntie() { return this.auntie; }  public Relative uncle() { return this.uncle; }  ...
```

and your code reviewer wants you prepend the word "get" to each of them.
Well, this is a classic refactoring situation ("rename method"), but you're going to have to invoke the refactoring manually for each method, and you may have hundreds of them.
If these methods have been around a while, and they're being referenced by many external callers, then you're safest using a refactoring tool.  You may even consider writing a one-off refactoring script, perhaps in
[Jython](http://www.jython.org)
or
[Mozilla Rhino](http://www.mozilla.org/rhino)
, that makes programmatic use of either your IDE's refactoring APIs or a lower-level tool such as
[ANTLR](http://www.antlr.org)
or
[JavaCC](http://javacc.dev.java.net)
.
Whew!  That's going to be a lot of work, no matter how you slice it.  And if you've published your APIs externally, then you're screwed; all you can do is
the old names and hope people stop using them someday.
But that's why you get your code reviews done early, right?  In many real-world situations, you're performing a rename-method on a new class that has no external callers yet.  And in those situations, Emacs 22 will get the job done far faster than a refactoring IDE can.
In this case, we'd just do a straightforward replacement with capitalization, similar to the one in our last example, like so:

```
M-x replace-regexp  Replace regexp: \(public Relative \)\(\w\)\(\w+\)  Replace regexp with: \1get\,(capitalize \2)\3
```



| Et voilà: | <-- (p.s.: C-x 8 ` a gives you that neat 'à' character.) |



```
  public Relative getFather() { return this.father; }  public Relative getMother() { return this.mother; }  public Relative getSister() { return this.sister; }  public Relative getBrother() { return this.brother; }  public Relative getAuntie() { return this.auntie; }  public Relative getUncle() { return this.uncle; }  ...
```

Even if you do most of your coding in the comfy confines of a visual IDE, it can be awfully handy to keep Emacs around for your fine-grained text surgery.
Now we can move on to some more interesting examples, so you can feel you got your money's worth out of today's blog entry.  But first...

#### A Note About Emacs Regexps

Emacs regular expression syntax is very old, predating Perl 5's fancier regex syntax by almost a decade.  Perl's regexp enhancements are the defacto standard, supported in virtually all major programming languages.  Unfortunately, nobody has ever seen fit to retrofit poor Emacs with an alternate Perl-compatible regexp syntax, so Emacs regexps are now nonstandard and a bit awkward.  Here are a few of the noteworthy differences:
- You have to escape the **(**, **)**, **{**, **}**, and **|** metacharacters.  That is, they're not metacharacters by default — without the backslash, they match themselves.
- There's no '\d' shortcut for the [0-9] character class.
- There are no lookahead or lookbehind assertions.
- There are no direct equivalents for Perl's {n}?, {n,}?, {n,m}?, /i, /m, /s, /x, \G, or (?# ...) constructs.

But Emacs still supports some of the constructs you've come to expect:
- You can specify exactly N repetitions with `\{N\}', and between N and M repetitions (inclusive) with `\{N,M\}'.  E.g. [0-9]\{3\}-[0-9]\{4\} matches a 7-digit phone-number in the format xxx-xxxx.
- You can have backreferences to previously matched groups in the regular expression.  E.g. \(re\).*\1 matches words with "re" appearing at least twice, like ca**re**f**re**e and p**re**miè**re**.
- You can specify "shy" groups that don't record the match with \(?: ... \).

There are also some Emacs-specific enhancements, such as matchers for entries in the mode-specific syntax tables.  The Info pages have more details on Emacs regular expressions.
If you plan to be more than a casual Emacs user, you should study the regexp syntax carefully, because there are many useful commands in Emacs that operate on regular expression matches.  The better you know the Emacs-specific syntax, the more productive you'll be.
I suppose before we move on to the next example, I should preemptively answer one of the most frequently asked questions about Emacs regexps.
**Q:**
How do I embed a newline in a regexp I'm typing into the minibuffer?
**A:**
You use the key sequence
.  The C-q invokes the Emacs `
' command, which basically says "insert the next character literally, without invoking any commands with it."  C-j (i.e., control-j) is how a newline character is represented in Emacs.
is a useful general-purpose Emacs command.  Whenever you want to insert a character (in the minibuffer or a regular buffer), and it's just refusing to go in,
will almost always do the trick.

#### Example:  Numbering Lists

With our new replacement-with-evaluation feature, it becomes straightforward to create numbered lists.  Emacs 22 has introduced a new backreferencing metacharacter, `
**\#**
', which counts the number of replacements we've done so far in the current command.  So even without using any Lisp, we already have one way to make numbered lists.
Let's see... we'll need a short list of words as an example.  How about all the words in
that
*don't*
end in [a-z]?  Easy enough to find out.  We
(only if you're on a Unix system, of course, and the location varies), and then
.  Ah, perfect — our
buffer shows 32 matches:

```
   1987:Bogotá   5243:Fabergé   9772:Mallarmé  12044:Paraná  12499:Poincaré  16956:abbé  19923:appliqué  20932:attaché  23704:blasé  26223:café  26511:canapé  29314:cliché  31431:consommé  38981:décolleté  42995:fiancé  43623:flambé  44996:frappé  48317:habitué  58328:macramé  58898:manqué  62514:naiveté  65243:outré  66710:passé  71609:protégé  73675:recherché  76387:risqué  76847:roué  77811:sauté  82455:soufflé  89055:touché  96268:émigré  96274:études
```

They're prefixed by their line number, but we can make that disappear during the replacement.  Let's turn them into a numbered list.  First copy the matches into a new, writable buffer, then
to go to the top of the list, and then:

```
M-x replace-regexp  Replace regexp: \(.+:\)  Replace regexp with \#. 
```

Boom!

```
0. Bogotá1. Fabergé2. Mallarmé3. Paraná4. Poincaré5. abbé6. appliqué7. attaché8. blasé9. café10. canapé11. cliché12. consommé13. décolleté14. fiancé15. flambé16. frappé17. habitué18. macramé19. manqué20. naiveté21. outré22. passé23. protégé24. recherché25. risqué26. roué27. sauté28. soufflé29. touché30. émigré31. études
```

Oooh, but only Computer Science students like lists numbered from zero. So let's
(using
**C-/**
of course — everyone uses
**C-x C-u**
, but that's way too many keystrokes for something as common as Undo!) and use a tiny bit of Lisp to start the numbering at 1.
It so happens that Emacs-Lisp defines a function called
, which increments a number.  So we can just wrap the
in our replacement string with that function, like so:


| \,(1+ \#). | <-- (There's a trailing space after the ".") |


The result is just what we wanted:

```
1. Bogotá2. Fabergé3. Mallarmé4. Paraná5. Poincaré6. abbé7. appliqué8. attaché9. blasé...
```

The lisp
function operates on numbers, not strings, so you might have expected it to barf with a
error.  Our example works because the
**\#**
metacharacter returns a
*count*
of matches so far, which is a number, not a string value.  In our next example, we'll have to do the conversion ourselves.

#### Example:  Re-numbering Lists

We can use Lisp-code snippet similar to our previous one to renumber an existing list.  Let's say we want to insert a word in a numbered list, like so:

```
1. Bogotá2. Fabergé3. Flambé     <-- (We inserted this one.  Nice word, eh?)3. Mallarmé4. Paraná5. Poincaré6. abbé7. appliqué8. attaché9. blasé...
```

Easy to fix in Emacs22:  place the cursor just after the word we inserted, and
`
' with `
'.  The result:

```
1. Bogotá2. Fabergé3. Flambé4. Mallarmé5. Paraná6. Poincaré7. abbé8. appliqué9. attaché10. blasé...
```

This time we used a numbered backreference (
**\1**
), which always returns a string.  Don't be fooled by the fact that we appear to be matching a number:  the regexp `
' matches a string containing numeric digits, and we have to do a type conversion (using the Emacs-Lisp builtin function
) if we want to increment it.
I hope by now you're beginning to suspect that knowing a little Emacs-Lisp can help you
*immensely*
with your editing tasks.  Believe it!  (Not surprisingly, knowing a lot of Emacs-Lisp helps even more.)

#### Example:  Alphabetically Numbered Lists

Let's say we have a list of 26 or fewer items, and we want to "number" it with A, B, and C rather than 1, 2, and 3.
Well, shoot.  The list we've been using has 32 items.  I'd prefer a list of 26 (or so) for this example.
Let's see... we can write a wee Lisp function to group the words in
by their ending letters a-z:

```
(cl-prettyprint (save-excursion   (set-buffer "words")   (loop for c from ?a to ?z         collect (let ((i 0)                       (tail (string c)))                   (beginning-of-buffer)                   (while (re-search-forward (concat tail "$") nil t)                     (incf i))                   (cons tail i)))))
```

We just evaluate this snippet in our
buffer (by typing
after the last paren).  It crunches the
buffer and produces:

```
(("a" . 1625) ("b" . 167) ("c" . 772) ("d" . 8331) ("e" . 7190) ("f" . 191) ("g" . 7401) ("h" . 991) ("i" . 457) ("j" . 4) ("k" . 784) ("l" . 2041) ("m" . 920) ("n" . 4347) ("o" . 718) ("p" . 450) ("q" . 5) ("r" . 4279) ("s" . 44857) ("t" . 4454) ("u" . 140) ("v" . 46) ("w" . 247) ("x" . 182) ("y" . 5519) ("z" . 124))
```

Hmmm... nothing really promising.  We only get 9 words if we combine the ones ending in "q" and "j".  A minor tweak to our search function will show us words ending with a doubled letter:

```
(cl-prettyprint (save-excursion   (set-buffer "words")   (loop for c from ?a to ?z         collect (let ((i 0)                       (tail (concat (string c) (string c))))                   (beginning-of-buffer)                   (while (re-search-forward (concat tail "$") nil t)                     (incf i))                   (cons tail i)))))
```

Evaluating it gives us:

```
(("aa" . 2) ("bb" . 3) ("cc" . 1) ("dd" . 5) ("ee" . 136) ("ff" . 75) ("gg" . 4) ("hh" . 0) ("ii" . 4) ("jj" . 0) ("kk" . 0) ("ll" . 291) ("mm" . 2) ("nn" . 38) ("oo" . 30) ("pp" . 4) ("qq" . 0) ("rr" . 13) ("ss" . 1276) ("tt" . 58) ("uu" . 1) ("vv" . 0) ("ww" . 0) ("xx" . 0) ("yy" . 0) ("zz" . 9))
```

Looks like we have more options with this list.  Maybe if we just take the ones with a count of 5 or less... looks like 26 of them.  Perfect!
We could write a little more code to extract the words matching our criteria, but it's clearly going to be fastest to eyeball it.  So we call
with the regexp
, and we get our list of 26 words:

```
   2145:Bragg   3436:Cobb   5662:Fromm   6284:Gregg   6317:Grimm   6675:Hawaii   8025:Judd   8290:Kellogg   8411:Kidd   8509:Knapp   8645:Krupp   8689:Kwanzaa   8804:Lapp  12549:Pompeii  15425:Todd  16257:Webb  16641:Yacc  17702:add  21427:baa  39145:ebb  39372:egg  46305:genii  62411:muumuu  64283:odd  72801:radii  78139:schlepp
```

And what a fine bunch of words they are.  Just
*try*
doing that exercise in Java or C++ sometime.
In any case, now we have a list for our example, and we want to number it alphabetically.  So we need to replace all the cruft up through each ':' with a counter converted to an alphabet character.
As we saw in our little function that produced this word list, Emacs uses `?c' syntax to represent characters, and internally they're just ints.  So we just add the character `?a' to our `\#' counter this time, to loop through the characters 'a' to 'z':

```
M-x replace-regexp  Replace regexp:  ^\(.+:\)  Replace regexp with:  \,(+ ?a \#)) 
```

And, ladies and gentlemen... behold!

```
97) Bragg98) Cobb99) Fromm100) Gregg101) Grimm102) Hawaii103) Judd104) Kellogg105) Kidd106) Knapp107) Krupp108) Kwanzaa109) Lapp110) Pompeii111) Todd112) Webb113) Yacc114) add115) baa116) ebb117) egg118) genii119) muumuu120) odd121) radii122) schlepp
```

D'oh!!!!  I forgot to convert the counter back to a character.  Haha.  Oops.
After a quick C-/ to undo the operation, we can just change the replacement regexp to `
', and we finally have our alphabetically-enumerated word list:

```
a) Braggb) Cobbc) Frommd) Gregge) Grimmf) Hawaiig) Juddh) Kelloggi) Kiddj) Knappk) Kruppl) Kwanzaam) Lappn) Pompeiio) Toddp) Webbq) Yaccr) adds) baat) ebbu) eggv) geniiw) muumuux) oddy) radiiz) schlepp
```

Or we could get capital letters by using
instead.
Note that
has its own command history list, so you can just use up-arrow to fetch old regexps you've entered, and tweak them in place.  Easier than re-entering them from scratch every time.

#### Some Even Snazzier Examples

So far we've used this amazing little new feature to generate (and renumber) various lists, and to change the capitalization of the replacement text on the fly (in two different ways).  Both very practical and useful transformations.
In our next example, we'll assume you're working on a Java-based Web application, because your company is too lame to let you use
[Ruby on Rails](http://www.rubyonrails.org)
.  Hypothetically speaking, of course.
Suppose you have some JSP files containing references to various static images, e.g. <img src=
"images/foo_bar.gif"
>, and you decide you want to change them to calls into Java code to fetch the image URLs as the page is composed.  So
"images/foo_bar.gif"
needs to change to (say)
.
Well, clearly no fancy-pants refactoring IDE on the planet is going to be able to help you with this.  If you're an Eclipse or IntelliJ or Visual Studio user, get ready for some carpal tunnel while you manually change every instance.
However, if you've followed the examples so far, you know it's trivial in Emacs 22:

```
M-x replace-regexp  Replace regexp:  "images/\([a-z_]+\)\.\(gif\|jpg\)"  Replace regexp with: <%= StaticImageManager.\,(upcase (concat \1 "_" \2)).getUrl() %>
```

and they're all fixed in the blink of an eye.
But you knew that by now.  This example wasn't more complex than the others, just a little longer.
It starts to get even more interesting if you permit side effects in your lisp expressions.  That is to say, persistent changes to the world, whether it's Emacs variables, your buffer configuration, or even your filesystem.  You have to be a bit more careful, but you can use the new
eval feature as a powerful interactive scripting engine.
Our last example will be opening files.  Often you'll find yourself looking for files using the Unix `find' command in a shell.  But what if you want to open the files it turned up?
Again, it's a slightly contrived example, because it's already possible to use Unix shell commands and the "emacsclient" program to instruct Emacs to open the files you find.  But it should suffice to show you what we mean by "side-effecting replacements".
A simple example should work.  Let's go to our installed emacs lisp directory.  Mine's
, which I found by looking at my
variable in my
buffer.  There are various subdirectories, including
,
, and others.
To have Emacs open (say) all the elisp files beginning with the letter `x', we
, cd to
, and use the `find' command:

```
/usr/share/emacs/22.0.50/lisp>find . -name "x*.el"./progmodes/xscheme.el./term/x-win.el./term/xterm.el./obsolete/x-apollo.el./obsolete/x-menu.el./x-dnd.el./xml.el./xt-mouse.el
```

If you select the lines naming the 8 files above, then
will operate just in the selected region.  Opening the selected files is then one easy command:

```
M-x replace-regexp  Replace regexp:  .+  Replace regexp with:  \,(find-file-noselect \&)
```

The files are silently opened in the background when you execute this "replacement" command.  We could alternately have used
to watch them opened noisily in the foreground, but when opening lots of files I personally prefer to open them in the background.  (This also makes them appear at the bottom of your buffer-list.)
Note that we used a new metacharacter here, `
**\&**
', which grabs the entire string that matched.  That means we were able to omit the grouping parens.  We also relied on the fact that Emacs regexps are, by default, anchored to the beginning and end of the line, so `
' matches exactly one line, not counting the newline character.  Pretty convenient!
After the replacement, the lines in your
buffer are replaced with the return values of the calls to
, which in this case is just the name of the file.  But we don't really care, since it's a shell buffer; we were doing it purely for the side effect and not for the replacement.
Armed with your new-found knowledge,
and
should become some of the most powerful tools in your editing toolchest.  The more experience you have with Emacs regular expressions, and with Emacs Lisp, the more bang for your buck you'll get out of this enhancement.

#### Example:  Heading-Tag Promotion/Demotion

Oh, OK, fine.  One
*laaaaaast*
example, because I just ran into it as I was putting in my final edits.  You know how most browsers like to render <h1> tags in 10-foot tall letters?  So we all start with <h2> or even <h3> tags and work down from there?  (Those of us too lazy to muck with CSS overly much, that is.  Which is most of us.)
Well, I started my blog entry today with <h1> tags, and decided to bump them all up a number (and thus down in size.)
I used to do this operation with N successive replacements, with N ranging from 2 to 5.  You replace the <h5>'s with <h6>, then the <h4>'s with <h5>, and so on.  No more of that hooey for me!  I can renumber them all with a single replacement.  You guessed it:

```
M-x replace-regexp  Replace regexp:  <\(/?\)h\([0-9]\)>  Replace regexp with:  <\1h\,(1+ (string-to-int \2))>
```

Zoom, zoom, zoom!  All fixed in one swell foop.  That's just awesome.
There's also a new
function, but it's not all that different from what we've talked about here, so you can read about it when you upgrade.
You
*are*
going to upgrade now, right?  Well, it's your choice, it's your time.  Gotta spend time to save time, as the old saying (almost) goes.
But I think it was worth it.

### How do I learn this Emacs-Lisp doohickey, anyway?

It's really not too hard.  Honest.  Especially since I'm going to tell you some things that will make it much easier on you, because Emacs Lisp is pretty different from other languages you're used to.  If you keep these points firmly in mind, learning it will be a snap, really.  They're all things I wish someone had told me when I started learning elisp.

#### It'll Always be Useful

First, recognize that Emacs Lisp isn't going anywhere.  Emacs is not going to magically become programmable in Python or Ruby or JavaScript or Perl overnight.  (Or, God save us, Java or C++ or C# — all fine languages, to be sure, but they all suck at scripting.)
And judging from the last decade's pace of innovation in editing and coding environments, it will be many years before any editor begins to approach Emacs in the things Emacs does well.  [The one noteworthy exception is
[VIM](http://www.vim.org)
, which is also very powerful by all accounts, though I have no experience with it. If you have already developed a preference for vi over emacs, then you may experience greater happiness pursuing expertise with VIM.  Psh.]
There do, in fact, exist packages that make it possible to write Emacs extensions in Python (
[PyMacs](http://www.emacswiki.org/cgi-bin/wiki?PyMacs)
), Ruby (
[El4r](http://www.rubyist.net/~rubikitch/computer/el4r/index.en.html)
), and Perl (
[EPL](http://search.cpan.org/~jtobey/Emacs-EPL-0.7/lib/Emacs/Lisp.pm)
).  But they're far from seamless:  they're hard to install and they're hard to learn.  They will only appeal to you (maybe) if you're a truly die-hard programmer in one of those languages,
*and*
you already know a fair amount of emacs-lisp, because they're closely tied to the elisp programming model.  You will still need to know about buffers, overlays, markers, plists, symbols, and all the other Emacs-Lisp abstractions.  And you'll have to deal with the sometimes complex mapping between language X and Emacs-Lisp.
Plus, if you want to share your extensions with your friends, they'll have to go through the install process as well.  I just wouldn't go there, not if you're trying to learn how to get better with Emacs.  If you're an expert in both languages, then sure.  The package authors could use your help.
In the meantime, Emacs isn't going anywhere, and Emacs-Lisp isn't going anywhere, not for several decades at least, so it
*will*
benefit you to learn them deeply.  It will never be obsolete knowledge.  You might as well start learning it now, and reap the benefits now.

#### It's Kinda Like XML

You can think of Emacs Lisp as being very much like XML.  There are some differences that will become apparent as you use it, but thinking of it as XML will help a
*lot*
.
In most programming languages, it's good style to avoid deeply indented code.  With XML, indentation depth is entirely a function of your data domain; you don't generally think about restructuring it to avoid indentation.  (Think of XHTML, for instance, in which the nesting can become arbitrarily deep.)  With XML, you're building a tree structure, and it's easy to see it that way.  Your XML processing tools help you manage navigating your way around complex documents.
With Lisp, you're also building an explicit tree structure.  That means it's going to be indented very differently from your C/Java/Perl/Python code.  The indentation is less something you decide, and more something that's decided for you based on the approach you take to the problem.
The perpetual indentation used to drive me nuts, but I've come to appreciate its advantages.  I won't go into them here, but given what you know about XML, I'm sure you can imagine a few benefits without too much effort.

#### It Gets Better With Practice

If you do it enough, eventually you'll enjoy programming in Emacs-Lisp, no matter how much you hate it initially.  You'll probably never love it, and you'll pine for a more powerful Lisp dialect, and for features from other languages you know.  But like any other programming language, it becomes way more fun as you go from beginner to expert.
Programmers really hate new syntax.  Most people find it harder to learn new syntax than to learn new Design Patterns or APIs or frameworks.  So you'll initially dislike Emacs-Lisp's syntax; it's virtually guaranteed.  Fortunately, it doesn't really have much in the way of syntax; almost everything follows the exact same s-expression form.  So you should get past the syntax pretty quickly, and in a few weeks you'll start liking it just fine.

#### It's Oddly "Zippy"

Emacs-Lisp uses a radically different programming model from other languages.  There's a strong (nearly 1:1) correspondence between what you can do in the editor and what you can do in the language.  Writing elisp code is very much like scripting your actions in the editor.
For instance, to get the length of the current line (assuming the function doesn't exist), your code will
*remember*
where you are, then
*move*
the cursor to the beginning of the line, get the buffer position,
*jump*
the cursor to the end of the line, get the buffer position there, subtract the two buffer positions,
*return*
the cursor to where you were, and then finally return the value.  That's a lot of moving around!  [You can also use
and
, but in general, you still zip around a lot.]
As another example, if you wanted to determine whether any lines in the buffer started with a particular regexp, then you'd go look at them!  You don't call a function that returns a list of lines in the buffer (though you could write one).  You just save your position, go to the beginning of the buffer, and call
and
to check each line against the regexp.  It's like you've got a little worker-bee version of yourself, doing automatically what you could have done by hand (albeit much more slowly) using editor commands.
Over the years, they've piled up thousands of shortcut functions, and much of the time you wind up programming "normally" by invoking functions on data structures, like in other languages.  But it really helps to remember that little worker bee that zips around like Feynman's lonely electron.  Your coding will go more smoothly if you keep it in mind.

#### You can Learn From its Peers

Lastly, it's useful to know that Emacs-Lisp has a lot in common with two other famous Lisp dialects:
[Common Lisp](http://www.cliki.net/index)
and
[Scheme](http://www.schemers.org)
.  It's arguably closer to Common Lisp, and in many ways it's inferior to both of them, but learning a little about Common Lisp or Scheme will improve your Emacs-Lisp coding dramatically.  And, as it happens, there are far more books published about Common Lisp and Scheme than there are about Emacs Lisp.  I'll list a few of my favorites here.

#### Emacs-Lisp Books

You should start with Richard M. Stallman's book.  He wrote Emacs, and he wrote the
[Gnu Emacs Manual](http://www.amazon.com/o/asin/188211485X)
.  It's a classic, and probably remains the best book on Emacs to date.  It's a good idea to read it just to get an overview of all the things Emacs can do out of the box.  Otherwise it'll be hard to know what kinds of Emacs-Lisp programs you can write.
Next, you'll want the all-time classic,
[Mastering Regular Expressions](http://www.amazon.com/o/asin/0596002890)
, by Jeffrey Friedl.  Don't leave home without it.
Starting with Emacs 22, the Emacs-Lisp Reference Manual comes bundled with the distribution.  I don't know if it's sold in hardcopy anymore, but it's chock-full of critically important information, so you'd do well to read it.  (And re-read it periodically.  It's a lot of information.)
I do have a couple of books on Emacs Lisp:
[An Introduction to Programming in Emacs Lisp](http://www.amazon.com/o/asin/1882114566)
(Robert Chassell)
[Writing GNU Emacs Extensions](http://www.amazon.com/o/asin/1565922611)
(Bob Glickstein)
They're not bad, but I honestly never got much from them.  However, your mileage may vary.  Go to Amazon, peek through them a bit, and decide for yourself whether they'll be helpful.

#### Common Lisp Books

There are lots — lots and lots — but these are the ones I personally found most directly relevant to helping me learn Emacs-Lisp:
[ANSI Common Lisp](http://www.amazon.com/o/asin/0133708756)
(Paul Graham)
[On Lisp](http://www.paulgraham.com/onlisp.html)
(Paul Graham) — out of print, but available as a PDF.  I printed it out and bound it at FedEx/Kinko's.
I own (and have read) essentially all of the other books on Common Lisp in print today, and the two above got me the furthest towards Emacs-Lisp proficiency.  I'm not counting Peter Norvig's
[AI](http://www.amazon.com/o/asin/1558601910)
[books](http://www.amazon.com/o/asin/0137903952)
, since their focus is AI, not Lisp.  They're awesome books, though; I recommend them both highly.
And if you're actually trying to learn Common Lisp to
*use*
it (as opposed to applying what you can of it to Emacs), then you'd better get a copy of
[Peter Siebel's Book](http://www.amazon.com/o/asin/1590592395)
.  It's essential.

#### Scheme Books

Again, lots to choose from, and Scheme books tend to be more didactic, so I found they had a bigger impact in terms of ingraining the core ideas of Lisp.  Listed in decreasing order of mind-opening wow-ness:
[Structure and Interpretation of Computer Programs](http://www.amazon.com/o/asin/0262011530)
— a good candidate for the "Best Computer Science Book Ever" award.
[The Little Schemer](http://www.amazon.com/o/asin/0262560992)
— I worked through every single exercise twice:  once in Scheme, once in Emacs-Lisp.  Ditto for the sequel,
[The Seasoned Schemer](http://www.amazon.com/o/asin/026256100X)
, and I just started on the brand-new third volume,
[The Reasoned Schemer](http://www.amazon.com/o/asin/0262562146)
.
[The Scheme Programming Language](http://www.amazon.com/o/asin/0262541483)
— good book, though a bit heavy going, as it's long on concepts and short on explanations.  I found it well worth wrestling through, though.
Scheme is a wonderful language, and worth learning in its own right.

#### Caveats

If Emacs 22 goes on a horrible disk-eating rampage, don't blame me.
As one might expect of alpha software, it's got some bugs and glitches.  I've never had anything really scary happen.  It hasn't corrupted my data so far, and it has only crashed once or twice (i.e., far less often than the supposedly "stable" releases of XEmacs).  But it occasionally does surprising things, like minimizing the entire frame if I try to 'q' (quit) certain read-only windows, or suddenly bringing up a completions buffer when I'm typing along in fundamental mode.  They're rare enough not to have bothered me much.
They've also broken backwards-compatibility with several in-house functions and modes, so I've had to do some work to rewrite them.  If you rely on proprietary Emacs-Lisp software as part of your job, and you're not proficient with elisp yourself, then you should make sure you have a local guru available before you upgrade to Emacs 22, or some stuff may stop working for you.
This blog entry consists, as usual, of only my very own whimsical opinions.  I don't speak for my employer, nor for anyone else's employer, nor for any of the authors cited here, nor for the most excellent development teams working on Emacs, XEmacs, VIM, Eclipse, IntelliJ, Visual Studio, Firefox, and Ruby on Rails.  I just speak for me.
If you didn't like this article, please be sure to run over to Reddit and call me stupid there.  I'm sure people would hate to miss an opportunity to hear how you've taken such a boldly prominent and decisive stand on some random guy's personal blog.
And if you did like the article — well, go play with
[Emacs 22](http://savannah.gnu.org/projects/emacs/)
!