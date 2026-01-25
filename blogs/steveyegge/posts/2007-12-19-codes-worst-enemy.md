---
title: "Code's Worst Enemy"
date: 2007-12-19
url: https://steve-yegge.blogspot.com/2007/12/codes-worst-enemy.html
word_count: 5252
---

I'm a programmer, and I'm on vacation today.  Guess what I'm doing?  As much as I'd love to tell you I'm sipping Mai Tais in the Bahamas, what I'm actually doing on my vacation is programming.
So it's a "vacation" only in the HR sense – I'm taking official time off work, to give myself some free time to get my computer game back online.  It's a game I started writing about ten years ago, and spent about seven years developing.  It's been offline for a while and I need to bring it back up, in part so the players will stop stalking me.  It's going to take me at least a week of all-day days, so I had to take a vacation from work to make it happen.
Why did my game go offline?  Not for want of popularity.  It's a pretty successful game for a mostly part-time effort from one person.  I've had over a quarter million individuals try it out (at least getting as far as creating a character), and tens of thousands of people who've spent countless hours playing it over the years.  It's won awards and been featured in magazines; it's attracted the attention of game portals, potential investors, and whole schools full of kids.
Yup, kids.  It was supposed to be a game for college students, but it's been surprisingly popular with teenagers and even pre-teens, who you'd think would be off playing some 3D console game or other.  But I wrote it for myself, and apparently there are sufficient people who like the same kinds of games I do to create a sustainable community.
I took the game down for all sorts of mundane reasons - it needed some upgrades, work got busy, I didn't have lots of time at nights, etc.  But the mundane reasons all really boil down to just one rather deeper problem: the code base is too big for one person to manage.
I've spent nearly ten years of my life building something that's too big.
I've done a lot of thinking about this — more than you would probably guess.  It's occupied a large part of my technical thinking for the past four or five years, and has helped shaped everything I've written in that time, both in blogs and in code.
For the rest of this little rant, I'm going to assume that you're a young, intelligent, college age or even high school age student interested in becoming a better programmer, perhaps even a great programmer.
(Please – don't think I'm implying that I'm a great programmer.  Far from it.  I'm a programmer who's committed decades of terrible coding atrocities, and in the process I've learned some lessons that I'm passing along to you in the hopes that it'll help you in your quest to become a great programmer.)
I have to make the assumption that you're young in order to make my point, because if I assume I'm talking to "experienced" programmers, my blood pressure will rise and I will not be able to focus for long enough to finish my rant.  You'll see why in a bit.
Fortunately for me, you're young and eager to learn, so I can tell you how things really are.  Just keep your eyes open for the next few years, and watch to see if I'm right.

## Minority View

I happen to hold a hard-won minority opinion about code bases.  In particular I believe, quite staunchly I might add, that the worst thing that can happen to a code base is size.
I say "size" as a placeholder for a reasonably well-formed thought for which I seem to have no better word in my vocabulary.  I'll have to talk around it until you can see what I mean, and perhaps provide me with a better word for it.  The word "bloat" might be more accurate, since everyone knows that "bloat" is bad, but unfortunately most so-called experienced programmers do not know how to detect bloat, and they'll point at severely bloated code bases and claim they're skinny as a rail.
Good thing we're not talking to them, eh?
I say my opinion is hard-won because people don't really talk much about code base size; it's not widely recognized as a problem.  In fact it's widely recognized as a non-problem.  This means that anyone sharing my minority opinion is considered a borderline lunatic, since what rational person would rant against a non-problem?
People in the industry are very excited about various ideas that nominally help you deal with large code bases, such as IDEs that can manipulate code as "algebraic structures", and search indexes, and so on.  These people tend to view code bases much the way construction workers view dirt: they want great big machines that can move the dirt this way and that.  There's conservation of dirt at work: you can't compress dirt, not much, so their solution set consists of various ways of shoveling the dirt around.  There are even programming interview questions, surely metaphorical, about how you might go about moving an entire mountain of dirt, one truck at a time.
Industry programmers are excited about solutions to a big non-problem.  It's just a mountain of dirt, and you just need big tools to move it around.  The tools are exciting but the dirt is not.
My minority opinion is that a mountain of code is the worst thing that can befall a person, a team, a company.  I believe that code weight wrecks projects and companies, that it forces rewrites after a certain size, and that smart teams will do
*everything in their power*
to keep their code base from becoming a mountain.  Tools or no tools.  That's what I believe.
It turns out you have to have something bad happen to you before you can hold my minority opinion.  The bad thing that happened to me is that I wrote a beautiful game in an ugly language, and the result was lovely on the outside and quite horrific internally.  The average industry programmer today would not find much wrong with my code base, aside from the missing unit tests (which I now regret) that would, alas, double the size of my game's already massive 500,000-line code base.  So the main thing they would find wrong with it is, viewed in a certain way, that it's not big enough.  If I'd done things perfectly, according to today's fashions, I'd be even worse off than I am now.
Some people will surely miss my point, so I'll clarify: I think unit testing is great.  In fact I think it's critical, and I vastly regret not having unit tests for my game.  My point is that I wrote the game the way most experienced programmers would tell you to write that kind of system, and it's now an appallingly unmanageable code base.  If I'd done the "right thing" with unit tests, it would be twice appalling!  The apparent paradox here is crucial to understanding why I hold my minority belief about code base size.
Most programmers never have anything truly bad happen to them.  In the rare cases when something bad happens, they usually don't notice it as a problem, any more than a construction worker notices dirt as a problem.  There's just a certain amount of dirt at every site, and you have to deal with it: it's not "bad"; it's just a tactical challenge.
Many companies are faced with multiple million lines of code, and they view it as a simple tools issue, nothing more: lots of dirt that needs to be moved around occasionally.
Most people have never had to maintain a half-million line code base singlehandedly, so their view of things will probably be different from mine.  Hopefully you, being the young, eager-to-learn individual that you are, will realize that the only people truly qualified to express opinions on this matter are those who have lived in (and helped create) truly massive code bases.
You may hear some howling in response to my little rant today, and a lot of hand-wavy "he just doesn't understand" dismissiveness.  But I posit that the folks making these assertions have simply never been held accountable for the messes they've made.
When you write your own half-million-line code base, you can't dodge accountability.  I have nobody to blame but myself, and it's given me a perspective that puts me in the minority.
It's not just from my game, either.  That alone might not have taught me the lesson.  In my twenty years in the industry, I have hurled myself forcibly against some of the biggest code bases you've ever imagined, and in doing so I've learned a few things that
*most people never learn*
, not in their whole career.  I'm not asking you to make up your mind on the matter today.  I just hope you'll keep your eyes and ears open as you code for the next few years.

## Invisible Bloat

I'm going to try to define bloat here.  I know in advance that I'll fail, but hopefully just sketching out the problem will etch out some patterns for you.
There are some things that can go wrong with code bases that have a nice intuitive appeal to them, inasmuch as it's not difficult for most people to agree that they're "bad".
One such thing is complexity.  Nobody likes a complex code base.  One measure of complexity that people sometimes use is "cyclomatic complexity", which estimates the possible runtime paths through a given function using a simple static analysis of the code structure.
I'm pretty sure that I don't like complex code bases, but I'm not convinced that cyclomatic complexity measurements have helped.  To get a good cyclomatic complexity score, you just need to break your code up into smaller functions.  Breaking your code into smaller functions has been a staple of "good design" for at least ten years now, in no small part due to the book Refactoring by Martin Fowler.
The problem with Refactoring as applied to languages like Java, and this is really quite central to my thesis today, is that Refactoring makes the code base larger.  I'd estimate that fewer than 5% of the standard refactorings supported by IDEs today make the code smaller.  Refactoring is like cleaning your closet without being allowed to throw anything away.  If you get a bigger closet, and put everything into nice labeled boxes, then your closet will unquestionably be more organized.  But programmers tend to overlook the fact that spring cleaning works best when you're willing to throw away stuff you don't need.
This brings us to the second obviously-bad thing that can go wrong with code bases: copy and paste.  It doesn't take very long for programmers to learn this lesson the hard way.  It's not so much a rule you have to memorize as a scar you're going to get whether you like it or not.  Computers make copy-and-paste really easy, so
*every*
programmer falls into the trap once in a while.  The lesson you eventually learn is that code always changes, always always always, and as soon as you have to change the same thing in N places, where N is more than 1, you'll have earned your scar.
However, copy-and-paste is far more insidious than most scarred industry programmers ever suspect.  The core problem is
*duplication*
, and unfortunately there are patterns of duplication that cannot be eradicated from Java code.  These duplication patterns are everywhere in Java; they're ubiquitous, but Java programmers quickly lose the ability to see them at all.
Java programmers often wonder why Martin Fowler "left" Java to go to Ruby.  Although I don't know Martin, I think it's safe to speculate that "something bad" happened to him while using Java.  Amusingly (for everyone except perhaps Martin himself), I think that his "something bad" may well have been the act of creating the book Refactoring, which showed Java programmers how to make their closets bigger and more organized, while showing Martin that he really wanted more stuff in a nice, comfortable, closet-sized closet.
Martin, am I wrong?
As I predicted would happen, I haven't yet defined bloat except in the vaguest terms.  Why is my game code base half a million lines of code?  What is all that code doing?

## Design Patterns Are Not Features

The other seminal industry book in software design was Design Patterns, which left a mark the width of a two-by-four on the faces of every programmer in the world, assuming the world contains only Java and C++ programmers, which they often do.
Design Patterns was a mid-1990s book that provided twenty-three fancy new boxes for organizing your closet, plus an extensibility mechanism for defining new types of boxes.  It was really great for those of us who were trying to organize jam-packed closets with almost no boxes, bags, shelves or drawers.  All we had to do was remodel our houses to make the closets four times bigger, and suddenly we could make them as clean as a Nordstrom merchandise rack.
Interestingly, sales people didn't get excited about Design Patterns.  Nor did PMs, nor marketing folks, nor even engineering managers.  The only people who routinely get excited about Design Patterns are programmers, and only programmers who use certain languages.  Perl programmers were, by and large, not very impressed with Design Patterns.  However, Java programmers misattributed this; they concluded that Perl programmers must be slovenly, no good bachelors who pile laundry in their closests up to the ceiling.
It's obvious now, though, isn't it?  A design pattern isn't a feature.  A Factory isn't a feature, nor is a Delegate nor a Proxy nor a Bridge.  They "enable" features in a very loose sense, by providing nice boxes to hold the features in.  But boxes and bags and shelves take space.  And design patterns – at least most of the patterns in the "Gang of Four" book – make code bases get bigger.  Tragically, the only GoF pattern that can help code get smaller (Interpreter) is utterly ignored by programmers who otherwise have the names of Design Patterns tatooed on their various body parts.
Dependency Injection is an example of a popular new Java design pattern that programmers using Ruby, Python, Perl and JavaScript have probably never heard of.  And if they've heard of it, they've probably (correctly) concluded that they don't need it.  Dependency Injection is an amazingly elaborate infrastructure for making Java more dynamic in certain ways that are intrinsic to higher-level languages.  And – you guessed it – DI makes your Java code base bigger.
Bigger is just something you have to live with in Java.  Growth is a fact of life.  Java is like a variant of the game of Tetris in which none of the pieces can fill gaps created by the other pieces, so all you can do is pile them up endlessly.

## Millions of Lines of Code

I recently had the opportunity to watch a self-professed Java programmer give a presentation in which one slide listed Problems (with his current Java system) and the next slide listed Requirements (for the wonderful new vaporware system).  The #1 problem he listed was code size: his system has millions of lines of code.
Wow!  I've sure seen
*that*
before, and I could really empathize with him.  Geoworks had well over ten million lines of assembly code, and I'm of the opinion that this helped bankrupt them (although that also appears to be a minority opinion – those industry programmers just never learn!)  And I worked at Amazon for seven years; they have well over a hundred million lines of code in various languages, and "complexity" is frequently cited internally as their worst technical problem.
So I was really glad to see that this guy had listed code size as his #1 problem.
Then I got my surprise.  He went on to his Requirements slide, on which he listed "must scale to millions of lines of code" as a
*requirement*
.  Everyone in the room except me just nodded and accepted this requirement.  I was floored.
Why on earth would you list your #1 problem as a requirement for the new system?  I mean, when you're spelling out requirements, generally you try to
*solve*
problems rather than assume they're going to be created again.  So I stopped the speaker and asked him what the heck he was thinking.
His answer was: well, his system has lots of features, and more features means more code, so millions of lines are Simply Inevitable.  "It's not that Java is verbose!" he added – which is pretty funny, all things considered, since I hadn't said anything about Java or verbosity in my question.
The thing is, if you're just staring in shock at this story and thinking "how could that Java guy be so
*blind*
", you are officially a minority in the programming world.  An unwelcome one, at that.
Most programmers have successfully compartmentalized their beliefs about code base size.  Java programmers are unusually severe offenders but are by no means the only ones.  In one compartment, they know big code bases are bad.  It only takes grade-school arithmetic to appreciate just how bad they can be.  If you have a million lines of code, at 50 lines per "page", that's 20,000 pages of code.  How long would it take you to read a 20,000-page instruction manual?  The effort to simply browse the code base and try to discern its overall structure could take weeks or even months, depending on its density.  Significant architectural changes could take months or even years.
In the other compartment, they think their IDE makes the code size a non-issue.  We'll get to that shortly.
And a million lines is nothing, really.  Most companies would
*love*
to have merely a million lines of code.  Often a single team can wind up with that much after a couple years of hacking.  Big companies these days are pushing tens to hundreds of millions of lines around.
I'll give you the capsule synopsis, the one-sentence summary of the learnings I had from the Bad Thing that happened to me while writing my game in Java: if you begin with the assumption that you need to shrink your code base, you will eventually be
*forced*
to conclude that you cannot continue to use Java.  Conversely, if you begin with the assumption that you must use Java, then you will eventually be
*forced*
to conclude that you will have millions of lines of code.
Is it worth the trade-off?  Java programmers will tell you Yes, it's worth it.  By doing so they're tacitly nodding to their little compartment that realizes big code bases are bad, so you've at least won that battle.
But you should take anything a "Java programmer" tells you with a hefty grain of salt, because an "X programmer", for any value of X, is a weak player.  You have to cross-train to be a decent athlete these days.  Programmers need to be fluent in multiple languages with fundamentally different "character" before they can make truly informed design decisions.
Recently I've been finding that Java is an especially bad value for X.  If you absolutely
*must*
hire an X programmer, make sure it's Y.
I didn't really set out to focus this rant on Java (and Java clones like C#, which despite now being a "better" language still has Java's fundamental character, making it only a marginal win at best.)  To be sure, my minority opinion applies to any code base in any language.  Bloat is bad.
But I find myself focusing on Java because I have this enormous elephant of a code base that I'm trying to revive this week.  Can you blame me?  Hopefully someone with a pet C++ elephant can come along and jump on the minority bandwagon with me.  For now, though, I'll try to finish my explanation of bloat as a bona-fide problem using Java for context.

## Can IDEs Save You?

The Java community believes, with near 100% Belief Compliance, that modern IDEs make code base size a non-issue.  End of story.
There are several problems with this perspective.  One is simple arithmetic again: given enough code, you eventually run out of machine resources for managing the code.  Imagine a project with a billion lines of code, and then imagine trying to use Eclipse or IntelliJ on that project.  The machines – CPU, memory, disk, network – would simply give up.  We know this because twenty-million line code bases are already moving beyond the grasp of modern IDEs on modern machines.
Heck, I've never managed to get Eclipse to pull in and index even my 500,000-line code base, and I've spent weeks trying.  It just falls over, paralyzed.  It literally hangs forever (I can leave it overnight and it makes no progress.)  Twenty million lines?  Forget about it.
It may be possible to mitigate the problem by moving the code base management off the local machine and onto server clusters.  But the core problem is really more cultural than technical: as long as IDE users refuse to admit there is a problem, it's not going to get solved.
Going back to our crazed Tetris game, imagine that you have a tool that lets you manage huge Tetris screens that are hundreds of stories high.  In this scenario, stacking the pieces isn't a problem, so there's no need to be able to eliminate pieces.  This is the cultural problem: they don't realize they're not actually playing the right game anymore.
The second difficulty with the IDE perspective is that Java-style IDEs intrinsically create a circular problem.  The circularity stems from the nature of programming languages: the "game piece" shapes are determined by the language's static type system.  Java's game pieces don't permit code elimination because Java's static type system doesn't have any compression facilities – no macros, no lambdas, no declarative data structures, no templates, nothing that would permit the removal of the copy-and-paste duplication patterns that Java programmers think of as "inevitable boilerplate", but which are in fact easily factored out in dynamic languages.
Completing the circle, dynamic features make it more difficult for IDEs to work their static code-base-management magic.  IDEs don't work as well with dynamic code features, so IDEs are responsible for encouraging the use of languages that require... IDEs.  Ouch.
Java programmers understand this at some level; for instance, Java's popular reflection facility, which allows you to construct method names on the fly and invoke those methods by name, defeats an IDE's ability to perform basic refactorings such as Rename Method.  But because of successful compartmentalization, Java folks point at dynamic languages and howl that (some) automated refactorings aren't possible, when in fact they're just as possible in these languages as they are in Java – which is to say, they're
*partly*
possible.  The refactorings will "miss" to the extent that you're using dynamic facilities, whether you're writing in Java or any other language.  Refactorings are essentially never 100% effective, especially as the code base is shipped offsite with public APIs: this is precisely why Java has a deprecation facility.  You can't rename a method on everyone's machine in the world.  But Java folks continue spouting the provably false belief that automated refactorings work on "all" their code.
I'll bet that by now you're just as glad as I am that we're not talking to Java programmers right now!  Now that I've demonstrated one way (of many) in which they're utterly irrational, it should be pretty clear that their response isn't likely to be a rational one.

## Rational Code Size

The rational response would be to take a very big step back, put all development on hold, and ask a difficult question: "what should I be using instead of Java?"
I did that about four years ago.  That's when I stopped working on my game, putting it into maintenance mode.  I wanted to rewrite it down to, say, 100,000 to 150,000 lines, somewhere in that vicinity, with the exact same functionality.
It took me six months to realize it can't be done with Java, not even with the stuff they added to Java 5, and not even with the stuff they're planning for Java 7 (even if they add the cool stuff, like non-broken closures, that the Java community is resisting tooth and nail.)
It can't be done with Java.  But I do have a big investment in the Java virtual machine, for basically the same reason that Microsoft now has a big investment in .NET.  Virtual machines make sense to me now.  I mean, they "made sense" at some superficial level when I read the marketing brochures, but now that I've written a few interpreters and have dug into native-code compilers, they make a lot more sense.  It's another rant as to why, unfortunately.
So taking for granted today that VMs are "good", and acknowledging that my game is pretty heavily tied to the JVM – not just for the extensive libraries and monitoring tools, but also for more subtle architectural decisions like the threading and memory models – the rational answer to code bloat is to use another JVM language.
One nice thing about JVM languages is that Java programmers can learn them pretty fast, because you get all the libraries, monitoring tools and architectural decisions for free.  The downside is that most Java programmers are X programmers, and, as I said, you don't want X programmers on your team.
But since you're not one of those people who've decided to wear bell-bottom polyester pants until the day you die, even should you live unto five hundred years, you're open to language suggestions.  Good for you!
Three years ago, I set out to figure out which JVM language would be the best code-compressing successor to Java.  That took a lot longer than I expected, and the answer was far less satisfactory than I'd anticipated.  Even now, three years later, the answer is still a year or two away from being really compelling.
I'm patient now, though, so after all the dust settles, I know I've got approximately a two-year window during which today's die-hard Java programmers are writing their next multi-million line disaster.  Right about the time they're putting together their
*next*
Problems/Requirements slide, I think I'll actually have an answer for them.
In the meantime, I'm hoping that I'll have found time to rewrite my game in this language, down from 500,000 lines to 150,000 lines with the exact same functionality (plus at least another 50k+ for unit tests.)

## The Next Java

So what JVM language is going to be the Next Java?
Well, if you're going for pure code compression, you really want a Lisp dialect: Common Lisp or Scheme.  And there are some very good JVM implementations out there.  I've used them.  Unfortunately, a JVM language has to be a drop-in replacement for Java (otherwise a port is going to be a real logistics problem), and none of the Lisp/Scheme implementors seems to have that very high on their priority list.
Plus everyone will spit on you.  People who don't habitually spit will expectorate up to thirty feet, like zoo camels, in order to bespittle you if you even
*suggest*
the possibility of using a Lisp or Scheme dialect at your company.
So it's not gonna be Lisp or Scheme.  We'll have to sacrifice some compression for something a bit more syntactically mainstream.
It could theoretically be Perl 6, provided the Parrot folks ever actually get their stuff working, but they're even more patient than I am, if you get my drift.  Perl 6 really is a pretty nice language design, for the record – I was really infatuated with it back in 2001.  The love affair died about five years ago, though.  And Perl 6 probably won't ever run on the JVM.  It's too dependent on powerful Parrot features that the JVM will never support.  (I'd venture that Parrot probably won't ever support them either, but that would be mean.)
Most likely New Java is going to be an already reasonably popular language with a very good port to the JVM.  It'll be a language with a dedicated development team and a great marketing department.
That narrows the field from 200+ languages down to maybe three or four: JRuby, Groovy, Rhino (JavaScript), and maybe Jython if it comes out of its coma.
Each of these languages (as does Perl 6) provides mechanisms that would permit compression of a well-engineered 500,000-line Java code base by 50% to 75%.  Exactly where the dart lands (between 50% and 75%) remains to be seen, but I'm going to try it myself.
I personally tried Groovy and found it to be an ugly language with a couple of decent ideas.  It wants to be Ruby but lacks Ruby's elegance (or Python's for that matter).  It's been around a long time and does not seem to be gaining any momentum, so I've ruled it out for my own work.  (And I mean
*permanently*
– I will not look at it again.  Groovy's implementation bugs have really burned me.)
I like Ruby and Python a lot, but neither JVM version was up to snuff when I did my evaluation three years ago.  JRuby has had a
*lot*
of work done to it in the meantime.  If the people I work with weren't so dead-set against Ruby, I'd probably go with that, and hope like hell that the implementation is eventually "fast enough" relative to Java.
As it happens, though, I've settled on Rhino.  I'll be working with the Rhino dev team to help bring it up to spec with
[EcmaScript Edition 4](http://www.ecmascript.org)
.  I believe that ES4 brings JavaScript to rough parity with Ruby and Python in terms of (a) expressiveness and (b) the ability to structure and manage larger code bases.  Anything it lacks in sugar, it more than makes up for with its optional type annotations.  And I think JavaScript (especially on ES4 steroids) is an easier sell than Ruby or Python to people who like curly braces, which is anyone currently using C++, Java, C#, JavaScript or Perl.  That's a whooole lot of curly brace lovers.  I'm nothing if not practical these days.
I don't expect today's little rant to convince
*anyone*
to share my minority opinion about code base size.  I know a that few key folks (Bill Gates, for instance, as well as Dave Thomas, Martin Fowler and James Duncan Davidson) have independently reached the same conclusion: namely, that bloat is the worst thing that can happen to code.  But they all got there via painful things happening to them.
I can't exactly wish for something painful to happen to Java developers, since hey, it's already happening; they've already taught themselves to pretend it's not hurting them.
But as for
*you*
, the eager young high school or college student who wants to become a great programmer someday, hopefully I've given you an extra dimension to observe as your tend your code gardens for the next few years.
When you're ready to make the switch, well,
[Mozilla Rhino](http://www.mozilla.org/rhino)
will be ready for you.  It works great today and will be absolutely outstanding a year from now.  And I sincerely hope that JRuby, Jython and friends will also be viable Java alternatives for you as well.  You might even try them out now and see how it goes.
Your code base will thank you for it.