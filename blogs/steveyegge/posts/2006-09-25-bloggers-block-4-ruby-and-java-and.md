---
title: "Blogger's Block #4:  Ruby and Java and Stuff"
date: 2006-09-25
url: https://steve-yegge.blogspot.com/2006/09/bloggers-block-4-ruby-and-java-and.html
word_count: 4360
---

*Part 4 of a 4-part series of short posts intended to clear out my bloggestive tract. Hold your nose!*
Well, I held out for a week.  Then I read the comments.  Argh!  Actually they were fine.  Nice comments, all around.  Whew.
I don't have any big themes to talk about today, but I've got a couple of little ones, let's call 'em bloguettes, that I'll lump together into a medley for today's entree.

## **Bloguette #1: Ruby Sneaks up on Python**

I was in Barnes today, doing my usual weekend stroll through the tech section.  Helps me keep up on the latest trends.  And wouldn't you know it, I skipped a few weeks there, and suddenly Ruby and Rails have almost as many books out as Python.  I counted eleven Ruby/RoR titles tonight, and thirteen for Python (including one Zope book).  And Ruby had a big display section at the end of one of the shelves.
Not all the publishers were O'Reilly and Pragmatic Press.  I'm pretty sure there were two or three others there, so it's not just a plot by Tim O'Reilly to sell more books.  Well, actually that's exactly what it is, but it's based on actual market research that led him to the conclusion that Rails and Ruby are both gathering steam like nobody's business.
I like a lot of languages.  Really, I do.  But I use Ruby.  I'm not even sure if I
*like*
Ruby.  The issue might just be irrelevant to whether I use it.  I like OCaml, for instance, but I don't use it.  I don't like Java, but I do use it.
*Liking*
and
*using*
are mostly orthogonal dimensions, and if you like the language you're using even a little bit, you're lucky.  That, or you just haven't gotten broad enough exposure to know how miserable you ought to be.
I use Ruby because it's been the path of least resistance for most of my programming tasks since about 3 days after I started messing with it, maybe 4 years ago.
I don't even really know Ruby all that well.  I never bothered to learn it.  I did read "Ruby in a Nutshell" cover-to-cover, but it's a short read (and it's a bit out of date now.)  Then I read bits of "Programming Ruby", but not all of it.  And now I use Ruby for everything I can, any time I have any choice in the matter.  I don't even mind that I don't know the language all that well.  It has a tiny core that serves me admirably well, and it's easy to look things up when you need to.
I do a lot more programming in Python than in Ruby -- Jython in my game server, and Python at work, since that's what everyone there uses for scripting.  I have maybe 3x more experience with Python than with Ruby (and 10x more experience with Perl).  But Perl and Python both have more unnecessary conceptual overhead, so I find I have to consult the docs more often with both of them.  And when all's said and done, Ruby code generally winds up being the most direct and succinct, whether it's mine or someone else's.
I have a lot of trouble writing about Ruby, because I find there's nothing to say.  It's why I almost never post to the O'Reilly Ruby blog.  Ruby seems so self-explanatory to me.  It makes it almost boring; you try to focus on Ruby and you wind up talking about some problem domain instead of the language.  I think that's the goal of all programming languages, but so far Ruby's one of the few to succeed at it so well.
If only it performed better.  *Sigh*.  Well, its performance is in the same class as Perl/Python/JavaScript/Lua/Bash/etc., so there are still plenty of tasks Ruby's admirably suited for.
I think next year Ruby's going to be muscling in on Perl in terms of mindshare, or shelf-share, at B&N.

## **Bloguette #2: Java's Biggest Failing (Literally)**

I still do most of my programming in Java -- at least half of it, maybe more.  The Java platform continues to make amazing strides.  The newest incarnation (JDK 6) has lots of goodies I can't wait to play with.  Like Rhino, for instance, and although they appear to have gutted it, it's still awesome.  I think it's the best choice they possibly could have made.  Thank God they didn't bundle Groovy.  What a catastrophe that was, and still is, and would have been for Java if they'd bundled it.  Rhino rocks.
The JVM is just getting faster and more stable, and there are even some OK libraries that come with it.  I used to think the Java platform libraries were the cat's meow.  Heck, I thought they were the whole damn cat.  But working with better libraries in miscellaneous other languages has got me thinking that Java's libraries are hit-or-miss.
Example: Java's concurrency libraries (java.util.concurrent[.*]) are to die for.  I mean, if you're stuck with threads.  I think in the fullness of time, hand-managed threads will be history, but in the meantime, Java's concurrency libraries are just superb.
I recently ported a medium-sized Python program I'd written (about 1200 lines of fairly dense Python code) to Java, because the Python was taking about an hour to run, and I wanted to parallelize the work.  I spent about 3 days doing the rewrite: one day on the straight port, a day adding in the threading, and a day fine-tuning it.  The straight port wound up as 1300 lines of Java (surprising that it wasn't bigger, but maybe I code in Python with a Java accent?), and ran about 50% faster, down to about 30 minutes.  After adding in the threading and state machine, the program ran in 50 to 60 seconds.
So I got an order of magnitude improvement with only about a 50% increase overall in program size.  The vast majority of the improvement was attributable to the threading, which in turn would have taken me FAR longer if I'd been using raw synchronization primitives.  The java.util.concurrent stuff made it a snap.
On the other hand, Java's DOM implementation completely blows chunks.  It quickly became the bottleneck in my application, due to an O(n) algorithm I stumbled across with no good workaround for.  I can't remember exactly where it was (this was back in July), but I found a sheepishly apologetic comment from the author in the online docs.  It was something to do with setting attributes on nodes while you're doing a traversal of some sort: something you'd definitely want to be fast, but it had at least linear performance, maybe worse, and now accounts for 95+% of my app's processing time.
And of course Java's DOM
*interface*
blows too, because you can't create subclasses or decorators or do anything useful with the DOM other than use it as a temp container until you've transfered the data to something more flexible.
Java's collections library is decent, but not superb.  It's nice having the data structures they provide, but they're not very configurable, and the language itself makes them often cumbersome.  For instance, you can have a WeakHashMap (nice), or an IdentityHashMap (nice), or a ConcurrentHashMap (also nice), but you can't combine any two of those three properties into a single hashtable.  Lame.
And java.util is missing implementations and/or interfaces for a bunch of important data types like priority queues (you're stuck using a TreeSet, which is overkill), the disjoint set ADT, splay trees, bloom filters, multi-maps, and of course any kind of built-in graph support.  Java hyper-enthusiasts will tell you: "well, go write your own!  Or use one of the many hopefully robust implementations on the web!"  That seems lame to me.  We're talking about
*data structures*
here: they're more fundamental than, say, LDAP libraries and much of the other stuff Sun's bundling these days.  It's smartest to provide robust, tuned implementations of these things, because it empowers average Java programmers to write faster, more reliable code.
Oh, and let's not even get me started with java.nio.  What a mess!  It's pretty gross, especially if you come from the comparatively simple background of select() and poll() on Unix.  But maybe the grossness was necessary.  I'll give them the benefit of the doubt.  What bugs me isn't that the API is conceptually weird and complex (and buggy as hell last time I checked); what bugs me is that nobody at Sun bothered to put a layer
*atop*
java.nio for ordinary programmers.  Like, say, a nonblocking DataInputStream that takes a type to read, a Buffer, and a callback to call when it's finished reading.  So every frigging Java programmer on the planet has to write that exact class -- or just flail around with the raw APIs, which is what I think most of them do.
And look what they did to poor LDAP!  I mean, the LDAP bindings are dirt-simple in every language I've ever used.  It's supposed to be
*lightweight*
-- that's what the "L" stands for, fer cryin' out loud.  JNDI is this huge monster.  So is JMX.  I mean, Java libraries have this way of being
*so*
bloated and overengineered.
But whatever; I've digressed.  Java's libraries are
*not*
its biggest failing.  The libraries (as I said) are decent, and the platform (in terms of tools, speed, reliability, documentation, portability, monitoring, etc.) really raises the bar on all those other loser languages out there.  All of 'em.  It's why no better languages have managed to supplant Java yet.  Even if the language and its libraries are (on the whole) better than Java's, they also have to contend with the Java platform, and so far nobody's been able to touch it, unless maybe it's .NET, but who cares about .NET?  Certainly not Amazon.com or Yahoo! or Google or any other important companies that I'm aware of.

## Literals

Anyway, Java's biggest failing, I've decided, is its lack of syntax for literal data objects.  It's an umbrella failing that accounts for most of the issues I have with the language.
The idea behind literals is that you have some sort of serialized notation for your data type, and it's part of the language syntax, so you can embed pre-initialized objects in your code.
The most obvious ones are numbers, booleans and strings.  It's hard to imagine life without support for numeric literals, isn't it?  Well, Java's support is limited at best.  There's no syntax for entering a binary value, for instance, like "0b10010100".  And there's no BigInteger/BigDecimal syntax, so working with them is a disaster and nobody does it if they can help it.  Heck, Java doesn't even have unsigned ints and longs.  But Java does more or less the bare minimum for numbers, so people don't notice it much.
Imagine if there were no String literals, so that instead of this:

```
String s = "Hello, world!";
```

you had to do this:

```
  StringBuffer sb = new StringBuffer();  sb.append('H');  sb.append('e');  sb.append('l');  sb.append('l');  sb.append('o');  sb.append(',');  sb.append(' ');  sb.append('W').append('o').append('r').append('l').append('d').append('!');  String s = sb.toString();
```

Not only is the latter bloated and ugly and error-prone (can you spot the error in mine?), it's also butt-slow.  Literals provide the compiler with opportunities for optimization.
Well, unfortunately this OOP garbage is
*exactly*
what you have to do when you're initializing a hashtable in Java.  Nearly all other languages these days have support for hashtable/hashmap literals, something like:

```
 my_hashmap = {  "key1" : "value1",  "key2" : "value2",  "key3" : "value3",  ...}
```

That's the syntax used by Python and JavaScript, but other languages are similar.  The Java equivalent is this:

```
Map<String, String> my_hashmap = new HashMap<String, String>();my_hashmap.put("key1", "value1");my_hashmap.put("key2", "value2");my_hashmap.put("key3", "value3");...
```

It might not look that much worse from this simple example, but there are definitely problems.  One is optimization; the compiler is unlikely to be able to optimize all these method calls, whereas with a literal syntax, it could potentially save on method call overhead during construction of the table (and maybe other savings as well.)
Another is nested data structures.  In JavaScript (and Python, Ruby, etc.) you just declare them in a nested fashion, like so:

```
my_thingy = {  "key1": { "foo": "bar", "foo2": "bar2"},  "key2": ["this", "is", "a", "literal", "array"],  "key3": 37.5,  "key4": "Hello, world!",   ...}
```

It would be hard to do this particular one in Java 5 because of the mixed value types, though it's probably not an issue since using mixed-type data structures is something you rarely do in practice, even in dynamically-typed languages.  But even if all the values were hashes of string-to-string, how are you going to do it in Java without literals?  You can't.  You're stuck with:

```
Map<String, Map<String, String>> my_hashmap = \   new HashMap<String, HashMap<String, String>>();Map<String, String> value = new HashMap<String, String>();value.put("foo", "bar");value.put("foo2", "bar2");my_hashmap.put("key1, value);value.clear();value.put("foo3", "bar3");value.put("foo4", "bar4");my_hashmap.put("key2, value);... 
```

And then you find out later that your clever
optimization (instead of creating a new HashMap object for each value) busted it completely.  Whee.
Java programmers wind up dealing with this kind of thing by writing generic helper functions, and it winds up layering even more OOP overhead onto something that ought to be a simple declaration.  It also tends to be brutally slow; e.g. you could write a function called buildHashMap that took an array of {key, value, key, value, ...}, but it adds a huge constant-factor overhead.
This is why Java programmers rely on XML so heavily, and it imposes both an impedance mismatch (XML is not Java, so you have to translate back and forth) and a performance penalty.
But the story doesn't end there.  What about Vector/ArrayList literals?  Java has primitive array literals, which is nice as far as it goes:

```
String[] s = new String[]{"fee", "fi", "fo", "fum"};
```

Unfortunately, Java's primitive arrays are a huge wart; they don't have methods, can't be subclassed, and basically fall entirely outside the supposedly beautiful OOP-land that Java has created.  It was for performance, to help capture skeptical C++ programmers, and they have their place.  But I don't see why they should have all the syntactic support.  I mean, the [] array-indexing operator is ONLY available for Java arrays.  Sure would be nice to have it for ArrayLists, wouldn't it?  And Strings?  And FileInputStreams?
But for some reason, Java gave arrays not one, but TWO syntactic sugarings, and then didn't give that sugar to anything else array-like in the language.
So for building ArrayLists, LinkedLists, TreeMaps and the like, you're stuck with Swing-style code assemblages.
I think of them as Swing-style because I used to do a lot of AWT and Swing programming, back when I was a Thick Client kind of guy, and they have a distinct(ly unpleasant) footprint.  It looks vaguely like this, in pseudo-Swing:

```
Panel p = new Panel(new FlowLayout());JButton b = new JButton("Press me!");b.setEventListener(somethingOrOther);p.add(b);JSomething foo = new JSomething(blah, blah);foo.setAttribute();foo.setOtherAttribute();foo.soGladIDontDoThisKindOfThingAnymore();p.add(foo);...
```

Building UIs in Swing is this huge, festering gob of object instantiations and method calls.  It's OOP at its absolute worst.  So people have come up with minilanguages (like the TableLayout), and declarative XML replacements like Apache Jelly, and other ways to try to ease the pain.
I was on a team at Amazon many years ago that was planning to port a big internal Swing application to the web, and we were looking at the various ways to do web programming, which at the time (for Java) were pretty much limited to JSP, WebMacro, and rolling your own Swing-like HTML component library.
We experimented with the OOP approach to HTML generation and quickly discarded it as unmaintainable.  (Tell that to any OOP fanatic and watch their face contort as they try to reconcile their conflicting ideas about what constitutes good programming practice.)
The right solution in this case is, of course, a Lisp dialect; Lisp really shines at this sort of thing.  But Lisp isn't so hot at algebraic expressions, and the best Lisp machines no longer look so cutting-edge compared to the JVM, and blah blah blah, so people don't use Lisp.  So it goes.
The next-best solutions are all about equally bad.  You have your XML-language approaches (like Jelly, but for the web), but they don't give you sufficient expressiveness for control flow -- presentation logic really does require code, and it gets ugly in XML in a real hurry.  You have your JSP-style templating approaches, and they aren't bad, but they can have as many as 4 or 5 different languages mixed in the same source file, which presents various problems for your tools (both the IDEs and the batch tools).
And then you have a long tail of other approaches, none of which manage to be very satisfying, but that's not really the fault of the languages.  It's the browsers' fault: they START with three languages (HTML, CSS, and JavaScript), rather than having just one language to control the entire presentation, and it only goes downhill from there.
But NONE of the approaches to web templating is as bad as Swing-style programming, with a huge thicket of calls to new(), addChild(), setAttribute(), addListener(), and the like.  The only approach that's worse (and even it might just be tied) is raw HTML printing:

```
print("<html><body>...</body></html>");
```

So we're all in agreement.  OOP-style assembly of parents and children is the worst way to generate HTML.  You want to use declarations; you want a
*template*
, something that visually looks like the end result you're trying to create.
Well, it's the exact same situation for data structures, isn't it?  You'd rather draw a picture of it (in a sense, that's exactly what you're doing with syntax for literals) than write a bunch of code to assemble it.  This is all assuming that you're working with a small data set, of course.  But that happens all the time in real-world programs; it's ubiquitous.  So you kinda want your language to support it syntactically.
And so far we've only covered literal syntax for HashMaps and ArrayLists (which you can combine to produce various kinds of custom Trees.)  Already Java's way behind other languages, and we haven't discussed any richer data types.
Like, say, objects.
JavaScript does it the best here, IMO, in the parity between hashes and objects.  It's not really possible in Ruby or Python to declare a class, then create instances of the class using literal notation the way you can in JavaScript, where the keys are the names of instance variables.  Fortunately you can accomplish this in either Ruby or Python with just a smidge of metaprogramming, so it's spilt milk at worst.
In Java, you only have one big hammer (instantiation), and one big wrench (the method call), so that's what you use.  All you can really do to help is create a constructor that takes arguments that populate the instance variables.  But if any of your instance variables are collections (other than arrays), then you're back to the old create-setprops-addchild, create-setprops-addchild pattern again.
And what about functions?  Ruby and JavaScript and Lisp and Scheme and Lua and Haskell and OCaml and most other self-respecting languages have function literals.  That is, they have a syntax for declaring an instance of a function as a data object in your code that you can assign to a variable, or pass as a parameter.
(Python has them too, but unfortunately they can only be one line, so Python folks prefer to pretend anonymous functions aren't very important.  This is one of the 10 or so big problems caused by Python's whitespace policy.  Don't ever let 'em tell you it doesn't cause problems.  It does.  Maybe it's worth the trade-off; that's a personal style preference, but they should at least admit the tradeoff exists.)
Well, Java sort of has them, but Java's static type system doesn't have a literal syntax for a method signature.  It's pretty easy to imagine one, e.g. something like:

```
(int, int) -> String x;
```

This imaginary syntax declares a variable
that takes 2 ints as parameters and returns a string.  Lots of languages have signature-syntax of some sort, and Java's syntax space is definitely sparse enough that they could pick a good syntax for it without fear of collisions, even conceptual collisions.  But no such luck.  Instead, when you want to do this sort of thing you have to declare a
*named*
interface, and then inside of it declare at least one
*named*
method (which is where the params and return type show up), and then you're still not done, because when you create the function you have to create an anonymous (or named)
*class*
that contains the definition of the function that matches the interface.
Yuck.  But at least they let you do it; the alternative of not having it at all is definitely worse.
Still... isn't syntactic sugar nice?  I mean, they added the "smart" for-loop, which Java programmers just rave about.  So someone, somewhere in the Java community thinks syntax is good.  I'm not sure many of them really understand the difference between syntactic
*sugar*
(into which category the "smart" for-loop falls) and
*orthogonal*
syntax, in which the basic operators apply to all data types for which those operators make sense, and there are literal declarations possible for
*every*
data type.
Let alone the next step, which is
*extensible*
syntax -- but that idea strikes fear into the hearts of many otherwise brave Java programmers, and Rubyists and Pythonistas as well, so let's back it up a notch to "orthogonal", and keep everyone calm.
So there you have it: Java's biggest failing.  It's the literals.  No literal syntax for array-lists (or linked lists or tree sets), nothing for hashtables, nothing for objects of classes you've personally defined, none for functions or function signatures.  Java programmers all around the world spend a
**lot**
of their time working around the problem, using XML and YAML and JSON and other non-Java data-declaration languages, and writing tons of code (whole frameworks, even) for serializing and deserializing these declarations to and from Java.  For the smaller stuff, they just write helper functions, which wind up being bloated, inefficient, error-prone, and extremely unsatisfying.
Java's next-biggest failing may well be the lack of orthogonality in its set of operators.  We can live without operator overloading, I suppose (the simplest form of extensible syntax), but only if Sun makes operators like [] and + actually work for objects other than arrays and Strings, respectively.  Jeez.

## Epiblogue

You can draw your own conclusions about why suddenly there are all these books on Ruby appearing on the bookshelves.  It's a mix of truths, no doubt.  And you can draw your own conclusions about why Sun's adding support for scripting languages to the JVM, rather than simply fixing Java so that people don't want (need, really) to use those other languages.
But when you dig down into a programming language, and you get past all the hype and the hooplah, what you find is a set of policies and decisions that affect your everyday life as a programmer in ways you can't ignore, and that no amount of hype will smooth over.
If your language is sitting on you like an invisible elephant, and everyone using the language is struggling to work around the same problems, then it's
*inevitable*
that other languages will come into play.  Libraries can make you more productive, but they have almost no effect on the
*scalability*
of the language.
Every language has a complexity ceiling, and it's determined by a whole slew of policy and design decisions within the language,
*not*
the libraries.  The slew includes the type system (with its attendant hundreds of mini-policies), and the syntax, and it also includes the language's consistency: the ratio of rules to exceptions.
Java's demonstrating quite clearly that at a certain level of complexity, the libraries and frameworks start to collapse under their own weight.  People are always writing "lightweight" replacements for existing fat Java libraries and frameworks, and then the replacements get replaced, ad infinitum.  But have you ever seen anyone write a replacement for XPath?  Nope.  It's not like everyone is rushing out to write the next big XML-querying framework.  This is because XPath is a
*language*
, not a library, and it's orders of magnitude more conceptually scalable than the equivalent DOM manipulations.
Object-Oriented Programming.  Touted even by skeptics as a radical leap forward in productivity, and all OOP really is boils down to a set of organizational techniques.  Organization is nice, sure.
But it's pretty clear that OOP alone doesn't cut it; it has to be supplemented with Language-Oriented Programming and DSLs.  And
*all*
languages, DSLs and general-purpose languages alike, have to be designed to maximize consistency; each inconsistency and special-case in the language adds to its conceptual overhead and lowers the complexity ceiling.
So you can look at the shelves filling up with Ruby books and chalk it up to marketing hype, but I have a different theory.  I think it's entirely due to complexity management: Ruby does a better job of helping managing complexity than its competitors.  It doesn't do a perfect job, mind you -- far from it.  But it's enough of a step forward in productivity (even over Perl and Python) that it's managing to shoulder its way in to a pretty crowded language space.
With that in mind, despite my griping about Java's failings, I think Sun might actually be doing the right thing by introducing scripting languages (and improving support for them in the JVM.)  Maybe.  Their investment isn't really so much in Java as it is in the JVM; the JVM is their .NET.  Java's not really about productivity, not really -- it's got a lot of strengths (performance, deployment, reliability, static checkability, and so on), but productivity isn't high on the list.  So maybe the best way to address the productivity issue, for folks who really need it more than raw performance, is to introduce new JVM languages rather than try to pull Java in two directions.
We'll see.  And with that, I think I've officially un-blocked myself; I seem to be able to blog again.  So I'm declaring the Blogger's Block series finished!

```
BloggersBlock block = new BloggersBlock();block.setFinished(true);block.tieOffAndStuff();blog.addChild(block);...
```
