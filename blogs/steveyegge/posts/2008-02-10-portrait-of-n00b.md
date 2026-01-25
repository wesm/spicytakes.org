---
title: "Portrait of a N00b"
date: 2008-02-10
url: https://steve-yegge.blogspot.com/2008/02/portrait-of-n00b.html
word_count: 4786
---



|  | *The older I grow, the less important the comma becomes. Let the reader catch his own breath.
 — Elizabeth Clarkson Zwart* |


This is how I used to comment my code, twenty years ago (
*Note: dramatization*
):

```
  /**   * By the time we get to this point in the function,   * our structure is set up properly and we've created   * a buffer large enough to handle the input plus some   * overflow space.  I'm not sure if the overflow space   * is strictly necessary, but it can't hurt.  Next we   * have to update the counter to account for the fact   * that the caller has read a value without consuming   * it.  I considered putting the counter-increment on   * the shoulders of the caller, but since it meant every   * caller had to do it, I figured it made more sense to   * just move it here.  We can revisit the decision down   * the road if we find some callers that need the option   * of incrementing it themselves.   */   counter++;  // increment the consumed-value counter   /**    * Now we've got to start traversing the buffer, but we    * need an extra index to do it; otherwise we'll wind up    * at the end of the function without having any idea    * what the initial value was.  I considered calling this    * variable 'ref', since in some sense we're going to be    * treating it as a reference, but eventually I decided    * it makes more sense to use 'pos'; I'm definitely open    * to discussion on it, though.    */   char* pos = buffer;  // start our traversal   /**    * NEXT, we...    */
```

Does this style look at all familiar?  It should!  This is, to put it as impolitely as possible, n00b-style.  (Incidentally, if u dont no wat a n00b iz, u r 1.)
This is how junior programmers write code.  If you've read Malcom Gladwell's remarkable and eye-opening book
, you'll notice a striking similarity to the real-life 2-year-old Emily he describes in Chapter Three, who tells herself stories after her parents leave her room.  Here's a short excerpt from one of her stories:

> Tomorrow when we wake up from bed, first me and Daddy and Mommy, you, eat breakfast eat breakfast like we usually do, and then we're going to play and then soon as Daddy comes, Carl's going to come over, and then we're going to play a little while.  And then Carl and Emily are both going down to the car with somebody, and we're going to ride to nursery school [whispered], and then when we get there, we're all going to get out of the car...

Gladwell's account of Emily is fascinating, as she's allegedly a completely normal 2-year-old; they all do this when Mommy and Daddy aren't around.
Gladwell explains:

> Sometimes these stories were what linguists call temporal narratives.  She would create a story to try to integrate events, actions, and feelings into one structure — a process that is a critical part of a child's mental development.

If you look back at the comments in my hypothetical code from 20 years ago, you'll see that I was doing exactly what Emily does: making up a temporal narrative in an attempt to carve out a mental picture of the computation for myself.  These stories I told myself were a critical part of my mental development as a programmer.  I was a child trying to make sense of a big, scary new world.
Most programmers go through this phase.  It's perfectly normal.
In contrast, here's what my code tends to look like today:
***Update, Nov 14 2011:**  I did a terrible job of making my point with this code.  I deliberately chose some of the most freakish code I've ever written, because I wanted it to look ugly and scary.  I'm trying to show here what "typical" veteran code looks like to a junior programmer.  This code serves as a *caricature* for illustration purposes.  You're supposed to be put off by it.  If I had been trying to show you what modern art looks like to the uninitiated, I would have showed you a graffitied subway station wall that someone had just vomited on.  This is the coding equivalent.

If you *insist* on missing my point entirely and arguing about whether this function is "good code" or not, then I assure you:  **this code is horrific**.  It's a Lisp port of a Java port of some old C code.  *Both* ports intentionally stay as faithful to the original as possible, line-by-line in the most un-idiomatic code imaginable.  Why?  To make it easy to propagate bug fixes in the original to both ports.  So it's ugly for a legitimate reason.  But it's still frigging ugly.*

```
(defun js2-parse-variables (in-for decl-type)  "Parse a 'var', 'const' or 'let' statement or for-loop initializer.IN-FOR is true if we are currently in the midst of the init clause of a for.DECL-TYPE is a token value: either VAR, CONST, or LET depending on context.Returns the parsed statement node."  (let ((result (make-js2-var-decl-node))        destructuring-init        destructuring        s start tt init name node        (continue t))    ;; Examples:    ;; var foo = {a: 1, b: 2}, bar = [3, 4];    ;; var {b: s2, a: s1} = foo, x = 6, y, [s3, s4] = bar;    (while continue      (setq destructuring nil            s nil            tt (js2-peek-token)            start js2-token-start            init nil)      (if (or (= tt js2-LB) (= tt js2-LC))          ;; Destructuring assignment, e.g., var [a, b] = ...          (setq destructuring (js2-parse-primary-expr))        ;; Simple variable name        (js2-must-match js2-NAME "msg.bad.var")        (setq name (make-js2-name-node))        (js2-define-symbol decl-type js2-ts-string))      (when (js2-match-token js2-ASSIGN)        (setq init (js2-parse-assign-expr in-for)))      (if destructuring          (progn            (if (null init)                ;; for (var [k, v] in foo) is initialized differently                (unless in-for                  (js2-report-error "msg.destruct.assign.no.init")))            (setq node (make-js2-destructuring-init-node :start start                                                         :end js2-ts-cursor                                                         :lhs destructuring                                                         :initializer init))            (js2-node-add-children node destructuring init))        ;; simple variable, possibly with initializer        (setq node (make-js2-var-init-node :start start                                           :end js2-ts-cursor                                           :name name                                           :initializer init))        (js2-node-add-children node name init))      (js2-block-node-push result node)      (js2-node-add-children result node)      (unless (js2-match-token js2-COMMA)        (setq continue nil)))    result))
```

If I'd seen this code 20 years ago I'd have been appalled.  The lines of code are all crammed together!  Some of them
*aren't even commented!*
If I'd been given the task of maintaining this code, I'd have been screaming "rewrite!"
I probably write more Java and JavaScript these days, but I picked an Emacs-Lisp function I wrote recently to highlight how alien my code today would have looked to me twenty years ago.
To be fair, this function is actually a port of some Java code from Mozilla Rhino's JavaScript parser, which in turn is a port of some C code from SpiderMonkey's parser, which in turn was probably borrowed and modified from some other compiler.  Compiler code tends to have some of the purest lineage around, tracing back to the assembly-language code they wrote for the first compilers 40 or 50 years ago.  Which means it's going to be a bit on the ugly side compared to "ordinary" code.
But when I write code in other languages these days, even in Java, it looks a lot more like this Emacs Lisp fragment than like the n00b code I was writing 20 years ago.  It's
*denser*
:  there's less whitespace and far less commenting.  Most of the commenting is in the form of doc-comments for automated API-doc extraction.  On the whole, my code today is much more compressed.
In the old days, seeing too much code at once quite frankly exceeded my complexity threshold, and when I had to work with it I'd typically try to rewrite it or at least comment it heavily.  Today, however, I just slog through it without complaining (much).  When I have a specific goal in mind and a complicated piece of code to write, I spend my time making it happen rather than telling myself stories about it.
**A decade of experience makes you a teenager**
After going through their 2-year-old phase, programmers eventually have to go through a stupid-teenager phase.  All this month I've been hearing sad but unsurprising news stories about teenagers getting stuck on big rocks, being killed falling off cliffs, or dying of exposure.  I'm actually lucky the same didn't happen to me when I was a teenager.  It's just a bad time for us.  Even though teenagers are old enough to understand the warnings, they have this feeling of invincibility that gets them into trouble and often mortal peril.
The programming equivalent happens around us all the time too.  Junior programmers with five to ten years of experience under their belts (still n00bs in their own way) attempt to build giant systems and eventually find themselves stuck on the cliff waiting for a helicopter bailout, telling themselves "my next system rewrite will be better!"  Or they fall off the cliff – i.e., the project gets canceled, people get laid off, maybe the company goes under.
Yes, I've gone through that phase too.  And let's face it:  even seasoned programmers need a little optimism and a little bravery in order tackle real challenges.  Even as an experienced programmer, you should expect to fail at projects occasionally or you're probably not trying hard enough.  Once again, this is all perfectly normal.
That being said, as a hiring manager or company owner you should keep in mind that "5 to 10 years of experience" on a resume does
*not*
translate to "experienced"; it means "crazy invincible-feeling teenager with a 50/50 shot at writing a pile of crap that he or she and his or her team can't handle, and they'll eventually, possibly repeatedly, try to rewrite it all."  It's just how things are:  programmers can't escape being teenagers at some point.
**Building compression tolerance**
Hopefully the scene I've painted so far helps you understand why sometimes you look at code and you just hate it immediately.  If you're a n00b, you'll look at experienced code and say it's impenetrable, undisciplined crap written by someone who never learned the essentials of modern software engineering.  If you're a veteran, you'll look at n00b code and say it's over-commented, ornamental fluff that an intern could have written in a single night of heavy drinking.
The sticking point is compression-tolerance.  As you write code through your career, especially if it's code spanning very different languages and problem domains, your tolerance for code compression increases.  It's no different from the progression from reading children's books with giant text to increasingly complex novels with smaller text and bigger words.  (This progression eventually leads to
, if you're curious.)
The question is, what do you do when the two groups (vets and n00bs) need to share code?
I've heard (and even made) the argument that you should write for the lowest common denominator of programmers.  If you write code that newer programmers can't understand, then you're hurting everyone's productivity and chances for success, or so the argument goes.
However, I can now finally also see things from the veteran point of view.  A programmer with a high tolerance for compression is actually hindered by a screenful of storytelling.  Why?  Because in order to understand a code base you need to be able to pack as much of it as possible into your head.  If it's a complicated algorithm, a veteran programmer wants to see the whole thing on the screen, which means reducing the number of blank lines and inline comments –
*especially*
comments that simply reiterate what the code is doing.  This is exactly the opposite of what a n00b programmer wants.  n00bs want to focus on one statement or expression at a time, moving all the code around it out of view so they can concentrate, fer cryin' out loud.
So it's a problem.
Should a team write for the least common denominator?  And if so, exactly how compressed should they make the code?  I think the question may be unanswerable.  It's like asking for a single format for all books, from children's books to epic novels.  Each team is going to have its own average preference.  I suspect it's a good idea to encourage people to move their stories into design documents and leave them out of the code, since a junior programmer forced to work in a compressed code base may well grow up faster.
As for me, at this point in my career I would rather puzzle through a small, dense, complex piece of code than a massive system with thousands of files containing mostly comments and whitespace.  To some people this trait undoubtedly flags me as a cranky old dinosaur.  Since this is likely the majority of programmers out there, maybe I
*am*
a cranky old dinosaur.  Rawr.
**Metadata Madness**
Everyone knows that comments are
[metadata](http://en.wikipedia.org/wiki/Metadata)
:  information
*about*
the data (in this case, the data being your source code.)  But people often forget that comments aren't just a
*kind*
of metadata.  Comments and metadata are the same thing!
Metadata is any kind of description or model of something else.  The comments in your code are just a a natural-language description of the computation.  What makes metadata
*meta*
-data is that it's not strictly necessary.  If I have a dog with some pedigree paperwork, and I lose the paperwork, I still have a perfectly valid dog.
You already know the comments you write have no bearing on the runtime operation of your code.  The compiler just throws them away. And we've established that one hallmark of a n00b programmer is commenting to excess:  in a sense, modeling every single step of the computation in painstaking detail, just like Emily modeled her ideal Friday by walking through every step and reassuring her 2-year-old self that she really did understand how it was going to work.
Well, we also know that static types are just metadata.  They're a specialized kind of comment targeted at two kinds of readers:  programmers and compilers.  Static types tell a story about the computation, presumably to help both reader groups understand the intent of the program.  But the static types can be thrown away at runtime, because in the end they're just stylized comments.  They're like pedigree paperwork:  it might make a certain insecure personality type happier about their dog, but the dog certainly doesn't care.
If static types are comments, then I think we can conclude that people who rely too much on static types, people who really
*love*
the static modeling process, are n00bs.
Hee hee.
Seriously, though:  I'm not actually bashing on static-typing here; I'm bashing on the over-application of it.  Junior programmers overuse static typing in the exact same way, and for the same reasons, as they overuse comments.
I'll elaborate by first drawing a parallel to data modeling, which is another kind of "static typing".  If you've been working in a field that uses relational databases heavily, you'll probably have noticed that there's a certain personality type that's drawn to relational data modeling as a career unto itself.  They're usually the logical modelers, not the physical modelers.  They may have begun their careers as programmers, but they find they really love data modeling; it's like a calling for them.
If you know the kind of person I'm talking about, you'll doubtless also have noticed they're always getting in your way.  They band together and form Database Cabals and Schema Councils and other obstructive bureacracies in the name of safety.  And they spend a lot of time fighting with the engineers trying to get stuff done, especially at the fringes:  teams that are
*not*
working directly with the schema associated with the main revenue stream for the company, but are out trying to solve tangential problems and just happen, by misfortune, to be homed in the same databases.
I've been in surprisingly many situations at different companies where I had a fringe team that was being held up by data modelers who were overly-concerned about data integrity when the real business need was
*flexibility*
, which is sort of the opposite of strong data modeling.  When you need flexible storage, name/value pairs can get you a long, long, LONG way.  (I have a whole blog planned on this topic, in fact.  It's one of my favorite vapor-blogs at the moment.)
It's obviously important to do some amount of data modeling.  What's not so obvious is when to stop.  It's like commenting your code:  newer programmers just don't know when to quit.  When you're a little insecure, adding comments and metadata are a great security-blanket that make you feel busy when you've in fact stopped making forward progress and are just reiterating (or perhaps teaching yourself) what's already been accomplished.
Hardcore logical data modelers often suffer from an affliction called
*metadata addiction*
.  Metadata modeling is seductive.  It lets you take things at a leisurely pace.  You don't have to be faced with too much complexity at once, because everything has to go in a new box before you'll look at it.  To be sure, having
*some*
metadata (be it a data model, or static types, or comments) is important for human communication and to some extent for performance tuning.  But a surprising percentage of people in our industry take it too far, and make
*describing*
an activity more important than the activity itself.
The metadata-addiction phenomenon applies equally to coders.  Code
*is*
data, and data
*is*
code.  The two are inextricably linked.  The data in your genes is code.  The floor plans for your house are code.  The two concepts are actually indistinguishable, linked at a fundamental level by the idea of an Interpreter, which sits at the very heart of Computer Science.  Metadata, on the other hand, is more like the kidney of Computer Science.  In practice you can lose half of it and hardly notice.
**Creeping bureacracy**
I think that by far the biggest reason that C++ and Java are the predominant industry languages today, as opposed to dynamic languages like Perl/Python/Ruby or academic languages like Modula-3/SML/Haskell, is that C++ and Java cater to both secure and insecure programmers.
You can write C++ like straight C code if you like, using buffers and pointers and nary a user-defined type to be found.  Or you can spend weeks agonizing over template metaprogramming with your peers, trying to force the type system to do something it's just not powerful enough to express.  Guess which group gets more actual work done?  My bet would be the C coders.  C++ helps them iron things out in sticky situations (e.g. data structures) where you need a little more structure around the public API, but for the most part they're just moving data around and running algorithms, rather than trying to coerce their error-handling system to catch programmatic errors.  It's fun to try to make a bulletproof model, but their peers are making them look bad by actually deploying systems.  In practice, trying to make an error-proof system is way more work than it's worth.
Similarly, you can write Java code more or less like straight C, and a lot of seasoned programmers do.  It's a little nicer than C because it has object-orientation built in, but that's fairly orthogonal to the static type system.  You don't need static types for OOP:  in fact OOP was born and proven in dynamic languages like Smalltalk and Lisp long before it was picked up by the static-type camps.  The important elements of OOP are
*syntax*
(and even that's optional) and an object model implemented in the runtime.
So you can write Java code that's object-oriented but C-like using arrays, vectors, linked lists, hashtables, and a minimal sprinkling of classes.  Or you can spend years creating mountains of class hierarchies and volumes of UML in a heroic effort to tell people stories about all the great code you're going to write someday.
Perl, Python and Ruby fail to attract many Java and C++ programmers because, well, they force you to get stuff done.  It's not very easy to drag your heels and dicker with class modeling in dynamic languages, although I suppose some people still manage.  By and large these languages (like C) force you to face the computation head-on.  That makes them really unpopular with metadata-addicted n00bs.  It's funny, but I used to get really pissed off at Larry Wall for calling Java programmers "babies".  It turns out the situation is a little more complicated than that... but only a little.
And Haskell, OCaml and their ilk are part of a 45-year-old static-typing movement within academia to try to force people to model everything.  Programmers hate that.  These languages will never,
*ever*
enjoy any substantial commercial success, for the exact same reason the Semantic Web is a failure.  You can't force people to provide metadata for everything they do.  They'll hate you.
One very real technical problem with the forced-modeling approaches that static type systems are often "wrong".  It may be hard to imagine, because by a certain definition they can't be "wrong": the code (or data) is programmatically checked to conform to whatever constraints are imposed by the type system.  So the code or data always matches the type model.  But the type system is "wrong" whenever it
*cannot*
match the intended computational model.  Every time want to use multiple inheritance or mixins in Java's type system, Java is "wrong", because it can't do what you want.  You have to take the most natural design and corrupt it to fit Java's view of the world.
An important theoretical idea behind type systems is "soundness".  Researchers love to go on about whether a type system is "sound" or not, and "unsound" type systems are considered bad.  C++ and Java have "unsound" type systems.  What researchers fail to realize is that until they can come up with a type system that is never "wrong" in the sense I described earlier, they will continue to frustrate their users, and their languages will be abandoned for more flexible ones.  (And, Scala folks, it can't just be
*possible*
to express things like property lists – it has to be
*trivial*
.)
To date, the more "sound" a type system is, the more often it's wrong when you try to use it.  This is half the reason that C++ and Java are so successful:  they let you stop using the type system whenever it gets in your way.
The other half of their success stems from the ability to create user-defined static types.  Not, mind you, because they're helpful in creating solidly-engineered systems.  They are, sure.  But the reason C++ and Java (particularly Java) have been so successful is that their type systems form a "let's not get any work done" playground for n00bs to spend time modeling things and telling themselves stories.
Java has been
*overrun*
by metadata-addicted n00bs.  You can't go to a bookstore or visit a forum or (at some companies) even go to the bathroom without hearing from them.  You can't actually model everything; it's formally impossible and pragmatically a dead-end.  But they try.  And they tell their peers (just like our metadata-addicted logical data modelers) that you have to model
*everything*
or you're a Bad Citizen.
This gets them stuck on cliffs again and again, and because they're teenagers they don't understand what they did wrong.  Static type models have weight and inertia.  They take time to create, time to maintain, time to change, and time to work around when they're wrong.  They're
*just*
comments, nothing more.  All metadata is equivalent in the sense of being tangential documentation.  And static type models get directly in the way of flexibility, rapid development, and system-extensibility.
I've deleted several thousand words about the evolution of Apache Struts and WebWork, an example framework I chose to illustrate my point.  Rather than waste a bunch of time with it, I'll just give you a quote from one of the Struts developers in "The Evolution of Struts 2":

> ...the Struts 1 code base didn’t lend itself to drastic improvements, and its feature set was rather limited, particularly lacking in features such as Ajax, rapid development, and extensibility."

Struts 2 was thrown away for WebWork, which was in the process of throwing away version 1 (for similar reasons) in favor of version 2 (which has all the same problems).
Some of those several thousand words were devoted to JUnit 4, which has comically (almost tragically) locked on, n00b-style, to the idea that Java 5 annotations, being another form of metadata, are the answer to mankind's centuries of struggle.  They've moved all their code out of the method bodies and into the annotations sections.  It's truly the most absurd overuse of metadata I've ever seen.  But there isn't space to cover it here; I encourage you to go goggle at it.
There are die-hard Java folks out there who are practically gasping to inject the opinion, right here, that "rapid development" is a byproduct of static typing, via IDEs that can traverse the model.
Why, then, was Struts considered by its own developers to be a failure of rapid development?  The answer, my dear die-hard Java fans, is that a sufficiently large model can outweigh its own benefits.  Even an IDE can't make things go faster when you have ten thousand classes in your system.  Development slows because you're being buried in metadata!  Sure, the IDE can help you navigate around it, but once you've created an ocean, even the best boats in the world take a long time to move around it.
There are hundreds of open-source and proprietary Java frameworks out there that were designed by code-teenagers and are in perpetual trouble.  I've often complained that the problem is Java, and while I think the Java language (which I've come to realize is disturbingly Pascal-like) is partly to blame, I think the bigger problem is cultural:  it's hard to restrain metadata addiction once it begins creeping into a project, a team, or an organization.
Java programmers, and logical data modelers, and other metadata-addicted developers, are burying us with their "comments" in the form of models within their static type system.  Just like I did when I was a n00b.  But they're doing it with the best of intentions, and they're young and eager and energetic, and they stand on street corners and hand you leaflets about how great it is to model everything.
Seasoned programmers ignore them and just get it done.
**Solutions and takeaways**
Software engineering is hard to get right.  One person's pretty data model looks like metadata-addiction to another person.
I think we can learn some lessons from code-commenting:  don't try to model everything!  You need to step back and let the code speak for itself.
For instance, as just one random illustrative example, you might need to return 2 values from a function in Java (a language with no direct support for multiple return values).  Should you model it as a
class with named
and
fields (presumably with actual names appropriate to the problem at hand)?  Or should you just return a 2-element array (possibly of mixed types) and have the caller unpack it?
I think the general answer to this is:
**when in doubt, don't model it**
.  Just get the code written, make forward progress.  Don't let yourself get bogged down with the details of modeling a
*helper*
class that you're creating for documentation purposes.
If it's a public-facing API, take a lesson from doc-comments (which should be present even in seasoned code), and
*do*
model it.  Just don't go overboard with it.  Your users don't want to see page after page of diagrams just to make a call to your service.
Lastly, if you're revisiting your code down the road and you find a spot that's always confusing you, or isn't performing well, consider adding some extra static types to clarify it (for you and for your compiler).  Just keep in mind that it's a trade-off:  you're introducing clarifying metadata at the cost of maintenance, upkeep, flexibility, testability and extensibility.  Don't go too wild with it.
That way the cliff you build will stay small enough for you to climb down without a helicopter rescue.
**Postscript**
I'm leaving comments on, at least until "click-my-link" spam starts to surface.  I'm curious to know how this entry goes over.  This was an especially difficult entry to write.  I did a lot of editing on it, and left out a lot as a result.  I feel like I may not have made my points as clearly as I'd like.  And I'm sure I haven't convinced the metadata-addicted that they have a problem, although at least now they know someone out there thinks they have a problem, which is a start.
Let me know what you think!