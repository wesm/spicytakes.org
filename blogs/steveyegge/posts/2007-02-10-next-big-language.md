---
title: "The Next Big Language"
date: 2007-02-10
url: https://steve-yegge.blogspot.com/2007/02/next-big-language.html
word_count: 3446
---



|  | *There seems to be a long period of initial obscurity for any new language.  Then after that comes a long period of semi-obscurity, followed by total obscurity.
—Paul Bissex* |


*Note:  after I wrote this entry, one or two commenters speculated that I might be talking about something Google is doing.  They're barking up the wrong tree:  I may not be the smartest feller ever to fall off the cabbage truck, but I'm not -that- stupid.  The speculation in this blog is all based on stuff I've read on the net.  It's purely my own ideas and opinions, and I don't speak for Google (nor in today's entry, even -about- Google).  You'll have to look beyond Google for clues about NBL.  Enjoy!*
People are always asking me to comment on their new programming language they're designing.  I don't know about you, but I find that pretty funny, given the general trend of my comments on existing languages.  I mean, if you saw someone walking around kicking people directly in the metaphorical groin, would you go up and beg them to do it to you too?
And I feel bad about giving them my feedback, because I don't want to discourage them.  It's just that nobody will ever,
*ever*
use their language.  The odds are impossibly stacked against it.  Not to be discouraging, of course.
But people are still always trying to make new languages, because we have yet to see a language that is (a) popular and (b) doesn't suck.  Do you disagree?  If so, I don't mind.  It just means your standards aren't as high as mine.  Nothing wrong with that.
Back when I was in the Navy, just out of boot camp, an otherwise entirely forgettable petty officer first class instructor of ours offered us, unasked and free of charge, his sage advice on how to pick up women at a bar: "Go ugly early."  With this declaration, he had made it clear that he and I thought rather differently about certain things in life.  But I had to hand it to him: here was a man of conviction. He didn't care what other people thought of him, or for that matter, what he thought of himself.  He had defined his philosophy and he was sticking with it.
And in a sense, he taught me a valuable lesson, although it's not the one he probably thought he was teaching me.  I'll pass it on to you, unasked and free of charge.  If you want to spare yourself a lot of angst in deciding which programming language to use, then I recommend this simple rule:
**Go ugly early.**
C++ will go out with you in a heartbeat.
For my part, I want to encourage people to make their own languages, because doing it makes you a world-class programmer.  Seriously.  Not just a better programmer, but a best programmer.  I've said it before, and I'm sticking with it: having a deep understanding of compilers is what separates the wheat from the chaff.  I say that without having the slightest frigging clue what "chaff" is, but let's assume it's some sort of inferior wheat substitute, possibly made from tofu.
But I really need to stop spending time telling people individually why their languages are doomed to fail.  Instead, I'll summarize it in today's blog entry.
**Summary**
: your language is doomed to fail, with probability 1 minus epsilon.  If you fell off a thirty-story building, you
*might*
survive (anyone else watch the last episode of Heroes?  wasn't that an awesome scene?) but for all practical purposes the odds are nil.
Before I go into slightly more detail, I'll let you in on a secret.  Just between you and me.  Nobody else will know but us.  The secret is that last week I got an insider's tip: I know what the Next Big Language is going to be.
You probably imagine some sort of Old Boys Network that's responsible for deciding what we unwashed masses are going to use next.  You know, a bunch of corporate executive cigar-chomping porcine thugs sitting on each others' boards, conspiring and maneuvering to wheel and deal with mergers and consolidations, and suddenly language XYZ is endorsed by all the big companies at once, so you have to learn it or you'll get fired and deported and have to go live on the streets in some fly-specked third world country where, ironically, you don't speak the language there either.  Well, that's
*exactly*
how it works; how the hell do you think we all wound up programming in Java?
Seriously, though.  I know I have a very slight tendency to exaggerate a wee bit now and again, for dramatic effect.  And I don't always stop at stretching my metaphors; sometimes I drag them out to the back alley and beat the living crap out of them.  But it should be clear that there's a grain of truth to my cigar-chomping executives: most successful languages have had some pretty serious corporate backing.  C++ had AT&T and Microsoft.  Java had Sun and IBM.  C# and Visual Basic had Microsoft.  Perl basically had O'Reilly.  JavaScript had Netscape, Sun,
*and*
Microsoft (among others).  And so on.
And I found a tip — a rather detail-packed one at that — as to which way the wind is blowing.  Let's face it: I've been digging into this story for
*years*
, so it should be no surprise that I got the scoop.
*(Hint:  the "tip" was synthesized from reading a bunch of public web pages, so you've got all the clues you need.)*
Unfortunately I can't tell you what language it is.  For one thing, you probably wouldn't believe me.  For another, it wouldn't be fair; there are plenty of contenders out there, and it seems like they should all have a fighting chance.  Instead, I'm going to outline the characteristics that a language needs in order to be a megahit.  You won't like some of them, and I sure as hell don't like some of them, but we're talking stark reality here.  It's not a matter of opinion.
I'm really killing two birds here: by telling you where languages are headed, I'm giving you enough hints to figure out what the Next Big Language is without committing to anything, thereby evading the inevitable jihad against me if I were to say its name.  Second, I'm giving language designers valuable information that should help them get their language adopted, if that's their goal.
But first, some preliminaries and caveats are in order.
*You won't be deported to Columbia*
Just because the Next Big Language (NBL from now on) is going to arrive very soon (timeline: 18-24 months, as far as I can tell, which in language terms means "imminent") doesn't mean
*your*
language is going away.  You won't lose your job, so don't freak out on me.
What it does mean is that there's going to be a massive momentum shift, so if you start preparing now, it's not going to hit you as hard when it happens.  You'll be ready.
Heck, if you're lucky, you already know the language — at least the subset of it that exists today.  If so, you've got a big head start.
*NBL does not replace C++*
NBL is garbage collected.  There will always be a bunch of engineers who think that's evil, and they'll continue to use C++.
C++ does need to get replaced someday.  It's just horrid, and everyone knows it.  However, there aren't very many people trying to replace it, either.  The only contenders I'm aware of are Objective C and the
[D Programming Language](http://www.digitalmars.com/d)
.
D's a really beautiful language.  By rights it should be the next C++.  However, C++ programmers won't have it because it's garbage collected (even though it can be disabled, and even though
*Stroustroup himself*
is now advocating adding garbage collection to C++).  Walter Bright is one hell of a lot smarter than the C++ programmers who won't look at his language, and he has demonstrated that D is as fast as or faster than C++ and nearly as expressive as Ruby or Python.  It's a secret weapon just waiting to be seized by some smart company or open-source project.
But nobody ever accuses programmers of being
*wise*
.
I don't know much about Objective C, to be honest; I've read one or two books about it, and it looks decent-ish, but not inspiring in the way that D is (for instance.)  So I can't say much about it.  Seems kinda ho-hum to me.
Anyway, most of the language research and effort and creativity out there, both in academia and industry, is focused on higher-level languages, so it looks like C++ will continue to struggle happily in its tar pit for some years to come.
*NBL isn't about winning beauty contests*
When I refer to NBL, the Next Big Language, I specifically mean the next
*popular*
language.  I.e., a language that you yourself will wind up learning and actually using.  You can point to all sorts of languages, both existing and in the works, that are prettier than NBL.  Doesn't matter, though.  Heck, as you'll see (Rule #1), beauty is one of the obstacles to adoption.
If your goal as a language designer is to design a language that meets your own personal sense of aesthetics, then you're an artist, and I salute you.  For my part, I'm looking for the middle ground between hard-nosed I-don't-care pragmatism (in which case you go ugly early, use Java or C++, and be done with it) and idealistic better-world optimism.  And I think a lot of other people are too.
In any case, I'm not claiming that NBL is a
*great*
language; I'm just saying it doesn't suck.  In practice it's actually quite good, and it will be very, very popular.  NBL isn't the 100-year language, but it will definitely be the 10- to 20-year language.
And now, on to the features.  Get ready to get mad.
**The Language Arena**
Here's how you compete in the programming language arena today.  Follow these rules and you stand a chance.  Ignore them and your language will be Lion Chow.
*Rule #1: C-like syntax*
C(++)-like syntax is the standard.  Your language's popularity will fall off as a direct function of how far you deviate from it.
There's plenty of wiggle room in the way you define classes and other OOP constructs, but you'll need to stick fairly closely to the basic control-flow constructs, arithmetic expressions and operators, and the use of curly-braces for delimiting blocks and function bodies.
This is because programmers are lame, but hey, it's your target audience.  Give the people what they want.
People sometimes ask me why I think C's syntax is bad.  The reason is pretty simple: it's too complicated.  Well, C's wasn't so bad, but when you throw OOP into the mix (whether it's Java's, or C++'s, or D's, or anyone's), the grammar becomes enormously complex, with hundreds of productions.
It might feel, as a programmer using a C-like syntax, that the syntax is helping you out.  Unfortunately, as soon as you try to write code that deals with the language itself, you hit a wall.
Case in point:  Java folks always wish they had a better Java code formatter.  The best one ever written was Jalopy, but it never took off, in part because it wasn't open source, but also in part because its manual was
*astoundingly*
long and complicated.  Why?  Because it provided rules for customizing every last one of the hundreds of edge cases in Java's syntax.  And this was before Java 5 came along and made it even more complicated with generics and so on.
So people settle for the one built into Eclipse, but nobody ever goes in and messes with its actual internal mechanisms themselves, because even if they're unhappy with the way it handles certain syntactic cases, it's  too damned complicated to bother with.
Most programmers don't realize how often they need to deal with code that processes code.  It's an important case that comes up in many, many everyday situations, but we don't have particularly good tools for dealing with it, because the syntax itself prevents it from being easy.
That's why it's bad.
Unfortunately, even Ruby and Python (which "feel" simpler, syntactically) both also have very complicated grammars, making it nontrivial to write code that processes them, even with parsers that hand you the AST directly.
Whatever.  Now you know why I think C's syntax is bad.  It's because it
*is*
bad.
But bad or not, NBL will have approximately C-like syntax because if it doesn't, most programmers won't give it a second glance.
Sigh.
*Rule #2: Dynamic typing with optional static types.*
There are two ways to make a language.  The old way is to make it super static, to protect programmers from hurting themselves.  The classic example is SML, which is so fanatically typed that you're guaranteed
*never*
to get a runtime exception, because you will
*never*
get your goddamn program to compile.  There's nothing more fun than having your compiler tell you: "Error: expected type (int, int, int) but got type (int, int, int)".  Sheesh.
When you make a static language, you will be forced to add dynamism to it, because otherwise it's like programming in a straitjacket.  If you don't add dynamic features to your static language, then assuming everyone hasn't ditched it entirely, they will start building in the dynamic features themselves, no matter how hard it is, and how awkward they are to use.
The other way to design a language is to make it dynamic, and then you'll be forced to add static checks in later.  If you don't, then programmers will start simulating static checks using assertions and preprocessors and all manner of other hacks, in an effort to help lock things down once they've stabilized past the prototyping phase.
Adding in optional static types is the ideal solution.  It helps with performance, it helps with code reliability and (possibly) readability, it helps IDEs navigate your code, and most importantly, it helps combat the incredible FUD that dynamic languages inspire in people who come from static backgrounds.
It should be pretty obvious that dynamic + optional static types is a better approach than static + optional dynamic features.  The latter is premature optimization, plain and simple:  the root of all evil.
So NBL will be a dynamic language with optional static types.
As a special sneak preview, its static type system will include a "standard" class system (i.e. the kind you're used to if you do any conventional OOP using C++ or Java or Python or whatever, as opposed to Common Lisp's object system or some other unconventional one.)  Not that the standard system is any better, but it's what people want.
*Rule #3: Performance*
NBL will perform about as well as Java.  That means if it's one of the big existing dynamic languages out there, something major is going to have to happen with performance.
It turns out that
*eval()*
is one of the key things that gets in the way of performance optimizations.  It can easily invalidate all sorts of otherwise reasonable assumptions about variable bindings, stack addresses and so on.  It's also pretty important, so you can't just get rid of it.
So NBL will have to do something clever about eval.
Generally speaking, NBL will have to have a much greater focus on performance than so-called "scripting languages" have had in the past.  I mean, if it's really the Next Big Thing, it'll have to run on mobile devices, game platforms, and all sorts of other hardware-constrained devices.
It sounds impossible, I know.  But it's not.  Those compiler writers are a tricky bunch, and they have decades of experience.  A bunch of them got together and did a lot of head-scratching over NBL, and the result is going to perform quite nicely.
*Rule #4: Tools*
Let's face it: one of the biggest reasons people haven't adopted Ruby or Python is the lack of IDE support.  IDEs like Visual Studio and Eclipse have set the bar and the expectations for most programmers out there.
I can't tell you how many times I've heard people say they wouldn't use Ruby because it lacks automated refactoring tools.  Ruby doesn't actually need them in the way Java does; it's like refusing to switch to an electric car because there's no place to put the gasoline.  But programmers are a stubborn bunch, and to win them over you have to give them what they think they want.
So NBL will have great tools.  They might not be Java-great on Day One of NBL's reign, but they'll be a lot better than the options available for Perl/Python/Ruby/Tcl and the rest of the popular dynamic languages out there today.
*Rule #5: Kitchen Sink*
Word on the street is that all languages are evolving towards each other.  It's another way of saying they all have feature envy.  So NBL is going to have to play along.
Here's a short list of programming-language features that have become ad-hoc standards that everyone expects:
1. Object-literal syntax for arrays and hashes
2. Array slicing and other intelligent collection operators
3. Perl 5 compatible regular expression literals
4. Destructuring bind (e.g. x, y = returnTwoValues())
5. Function literals and first-class, non-broken closures
6. Standard OOP with classes, instances, interfaces, polymorphism, etc.
7. Visibility quantifiers (public/private/protected)
8. Iterators and generators
9. List comprehensions
10. Namespaces and packages
11. Cross-platform GUI
12. Operator overloading
13. Keyword and rest parameters
14. First-class parser and AST support
15. Static typing *and* duck typing
16. Type expressions and statically checkable semantics
17. Solid string and collection libraries
18. Strings and streams act like collections

Additionally, NBL will have first-class continuations and call/cc.  I hear it may even (eventually) have a hygienic macro system, although not in any near-term release.
Not sure about threads.  I tend to think you need them, although of course they can be simulated with call/cc.  I've also noticed that languages with poor threading support tend to use multiprocessing, which makes them
*more*
scalable across machines, since by the time you've set up IPC, distributing across machines isn't much of an architectural change.  But I think threads (or equivalent) are still useful.  Hopefully NBL has a story here.
*Rule 6:  Multi-Platform*
NBL will run, at a minimum, both standalone and on the JVM.  I'm not sure about plans for .NET, but it seems like that will have to happen as well.
And there are two other platforms that NBL will run on which, more than anything else, are responsible for its upcoming dominance, but I'd be giving away too much if I told you what they were.
**It's all about not sucking**
The features I've outlined don't make NBL a great language.  I think a truly great language would support Erlang-style concurrency, would have a simpler syntax and a powerful macro system, and would probably have much better support for high-level declarative constructs, e.g. path expressions, structural dispatch (e.g. OCaml's match ... with statement) and query minilanguages.  Among other things.
The features I've outlined are basically the minimal set of requirements for
*not sucking*
.  At least off the top of my head; I've probably overlooked a few.
Well... OK, I think C-style syntax kinda sucks, for reasons I've outlined, but it's a price I'm willing to pay, because I think there's no choice.  Rule #1 is in there strictly to support popularity.
Looking at the list, it's amazing that you have to work so hard just to meet the minimum standard for not sucking.  The bar has really gone up for programming languages.
Not to discourage you or anything.
Is NBL (the one whose name I won't tell you)
*guaranteed*
to be the Next Big Language?  I think it's got about a 90+% chance, but there's still hope for the other runner-ups.
For instance, it
*might*
be possible to get away with non-C syntax, provided you offer everything else I've listed here, but you'll have to bear in mind that you're competing against NBL, which has all the features of your language
*plus*
C-like syntax.  So your language would have to offer something not in this list that gives it a huge leg up on NBL.  (And I'm afraid simpler syntax alone won't do it; you're going to have to offer something that compensates for your lack of C syntax, because that's just how programmers are.)
So it's possible. But my bet is on NBL.
And now, if you'd like to see some excellent variations on the old game of Shoot The Messenger, enjoy the comments!