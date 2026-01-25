---
title: "Dynamic Languages Strike Back"
date: 2008-05-11
url: https://steve-yegge.blogspot.com/2008/05/dynamic-languages-strike-back.html
word_count: 13199
---

Some guys at Stanford invited me to
[speak at their EE Computer Systems Colloquium](http://www.stanford.edu/class/ee380/)
last week.  Pretty cool, eh?  It was quite an honor.  I wound up giving a talk on dynamic languages:  the tools, the performance, the history, the religion, everything.  It was a lot of fun, and it went over surprisingly well, all things considered.
They've uploaded the video of my talk, but since it's a full hour, I figured I'd transcribe it for those of you who want to just skim it.
This is the first time I've transcribed a talk. It's tricky to decide how faithful to be to my spoken wording and phrasing.  I've opted to try to make it very faithful, with only minor smoothing.
Unfortunately I wound up using continuation-passing style for many of my arguments:  I'd occasionally get started on some train of thought, get sidetracked, and return to it two or three times in the talk before I finally completed it.  However, I've left my rambling as-is, modulo a few editor's notes, additions and corrections in [brackets].
I didn't transcribe Andy's introduction, as it seems immodest to do so.  It was funny, though.
Technical corrections are welcome.  I'm sure I misspoke, oversimplified, over-generalized and even got a few things flat-out wrong.  I think the overall message will survive any technical errors on my part.
**The talk...**
Thank you everybody!  So the sound guys told me that because of a sound glitch in the recording, my normally deep and manly voice, that you can all hear, is going to come through the recording as this sort of whiny, high-pitched geek, but I assure you that's not what I actually sound like.
So I'm going to be talking about dynamic languages.  I assume that you're all dynamic language interest... that you've got an interest, because there's a dude down the hall talking about Scala, which is you know, this very strongly typed JVM language (a bunch of you get up and walk over there – exactly.)  So you know, presumably all the people who are like really fanatical about strong typing, who would potentially maybe get a little offended about some of the sort of colorful comments I might inadvertently make during this talk — which, by the way, are my own opinions and not Google's — well, we'll assume they're all over there.
All right.  I assume you all looked through the slides already, so I don't need to spend a whole lot of time with them.  I'll go into major rant-mode here at the end.  My goal is... for you guys to come away with, sort of a couple of new pictures in your mind, thinking about how languages have evolved over the last 20 years, where they're going, what we can do to fix them, that kind of thing.
Does anyone here know how to use a Mac?  It's showing me this weird, uh... thing... OK.  All right.  Here goes.
So!
Popular opinion of dynamic languages:  slooooow!  They're always talking about how Python is really slow, right?  Python is, what, like 10x to 100x slower?  And they have bad tools.
And also there's this sort of, kind of difficult-to-refute one, that says at millions of lines of code, they're maintenance nightmares, right?  Because they don't have static types.  That one, uh, unfortunately we're not going to be able to talk much about, because not many people have millions-of-lines code bases for us to look at — because dynamic languages wind up with small code bases.  But I'll talk a little bit about it.
So first of all, one of my compatriots here, who's an actual smart person, like probably everybody in this room, you're all waaay smarter than me — I got invited here for the booger jokes, all right? – he's a languages guy, and he said:  "You know, you can't talk about dynamic languages without precisely defining what you mean."
So I'm going to
*precisely*
define it.  Dynamic languages are, by definition...
,
,
,
,
,
... all right?  [
*(laughter)*
] It's the working set of languages that people dismiss today as "dynamic languages."  I'll also include
,
,
[Self](http://en.wikipedia.org/wiki/Self_%28programming_language%29)
,
, some of our stars, you know, from the 70s and 80s that, uh, well they'll come up here today too.
I'm deliberately not going down the path of "well, some static languages have dynamic features, and some dynamic languages have static types", because first of all it's this neverending pit of, you know, argument, and second of all, as you're going to see, it's completely irrelevant to my talk.  The two... sort of qualities that people associate with "dynamic":  one would be sort of... runtime features, starting with eval, and the other would be the lack of type tags, the lack of required type tags, or even just escapes in your type system.  These things work together to produce the tools problems and the performance problems, ok?  And I'll talk about them, and how they're going to be fixed.
All right!
I just talked about that [slide].
So!  Uh... yeah, that's right, I'm at Stanford!  Forgot about that.  So I've been interviewing for about 20 years, at a whole bunch of companies, and yeah, Stan– every school has this sort of profile, right?  You know, the candidates come out with these ideals that their profs have instilled in them.  And Stanford has a really interesting one, by and large: that their undergrads and their grad students come out, and they believe that C and C++ are the fabric with which God wove the Universe.  OK?  And they truly [think]: what is it with all these other languages?
Whereas like MIT and Berkeley, they come out, and they're like "languages, languages, languages!" and you're like, uh, dude, you actually have to
*use*
C and C++, and they're like "oh."  So it's funny, the kinds of profiles that come out.  But this one [first slide bullet point], I mean, it's kind of a funny thing to say, because the guy's a Ph.D., and he's just discovered Turing's thesis.  Of
*course*
all you need is C or C++.  All you need is a Turing machine, right?  You know?
What we're talking about here is fundamentally a very personal, a very political, sort of a, it's almost a fashion statement about who you are, what kind of language you pick.  So, you know... unfortunately we could talk, I mean I've got 2 hours of ranting in me about this topic, but I'm gonna have to, like, kinda like narrow it down to... we're gonna talk about dynamic languages because people are out there today using them.  They're getting stuff done, and it works.  All right?  And they really do have performance and tools issues.
But they're getting resolved in really interesting ways.  And I'm hoping that those of you who are either going out into the industry to start making big things happen, OR, you're researchers, who are going to be publishing the next decade's worth of papers on programming language design, will take some interesting directional lessons out of this talk.  We'll see.
All right.  So why are dynamic languages slow?  Uh, we all know they're slow because... they're dynamic!  Because, ah, the dynamic features defeat the compiler. Compilers are this really well understood, you know, really really thoroughly researched... everybody knows THIS [
*brandish the Dragon Book*
], right?
Compilers!  The
!  From your school!  OK?  It's a great book.  Although interestingly, heh, it's funny:  if you implement everything in this book, what you wind up with is a really naïve compiler.  It's really advanced a long way since... [the book was written] and they know that.
Dynamic languages are slow because all the tricks that compilers can do to try to guess how to generate efficient machine code get completely thrown out the window.  Here's one example.
is really fast, because among other things, the compiler can inline function calls.  It's gonna use some heuristics, so it doesn't get too much code bloat, but if it sees a function call, it can inline it:  it patches it right in, ok, because it knows the address at link time.
— you've got your virtual method dispatch, which is what C++ you know, sort of evangelists, that's the first thing they go after, like in an interview, "tell me how a virtual method table works!"  Right?  Out of all the features in C++, they care a lot about that one, because it's the one they have to pay for at run time, and it drives them nuts!  It drives them nuts because the compiler doesn't know, at run time, the receiver's type.
If you call
,
could be some class that C++ knows about, or it could be some class that got loaded in afterwards.  And so it winds up — this polymorphism winds up meaning the compiler can compile both the caller and the callee, but it can't compile them together.  So you get all the overhead of a function call.  Plus, you know, the method lookup.  Which is more than just the instructions involved.  You're also blowing your instruction cache, and you're messing with all these, potentially, code optimizations that could be happening if it were one basic-block fall-through.
All right.  Please – feel free to stop me or ask questions if I say something that's unclear.  I know, just looking around the room, that most of you probably know this stuff better than I do.
So!  The last [bullet point] is really interesting.  Because nobody has tried, for this latest crop of languages, to optimize them.  They're
*scripting languages*
, right?  They were actually designed to either script some host environment like a browser, or to script Unix.  I mean the goal was to perform these sort of I/O-bound computations; there was no point in making them fast.  Except when people started trying to build larger and larger systems with them:  that's when speed really started becoming an issue.
OK.  So obviously there's a bunch of ways you can speed up a dynamic language.  The number one thing you can do, is you can write a better program.  The algorithm, you know, is gonna trump any of the stuff you're doing at the VM – you can optimize the hell out of Bubble Sort, but...
Native threads would be really nice.  Perl, Python, Ruby, JavaScript, Lua...
*none*
of them has a usable concurrency option right now.  None of them.  I mean, they kinda have them, but they're like, Buyer Beware!  Don't ever use this on a machine with more than one processor.  Or more than one thread.  And then you're OK.  It's just, you know...
So actually, this is funny, because, all right, show of hands here.  We've all heard this for fifteen years now – is it true?  Is Java as fast as C++?  Who says yes?  All right... we've got a small number of hands... so I assume the rest of you are like, don't know, or it doesn't matter, or "No."
[
*Audience member:  "We read your slides."*
]  You read my slides.  OK.  I don't know... I can't remember what I put in my slides.
But it's interesting because C++ is obviously faster for, you know, the short-running [programs], but Java cheated very recently.  With multicore!  This is actually becoming a huge thorn in the side of all the C++ programmers, including my colleagues at Google, who've written vast amounts of C++ code that doesn't take advantage of multicore.  And so the extent to which the cores, you know, the processors become parallel, C++ is gonna fall behind.
Now obviously threads don't scale that well either, right?  So the Java people have got a leg up for a while, because you can use ten threads or a hundred threads, but you're not going to use a million threads!  It's not going to be
on you all of the sudden.  So obviously a better concurrency option – and that's a huge rat's nest that I'm not going to go into right now – but it's gonna be the right way to go.
But for now, Java programs are getting amazing throughput because they can parallelize and they can take advantage of it.  They cheated!  Right?  But threads aside, the JVM has gotten really really fast, and at Google it's now widely admitted on the Java side that Java's just as fast as C++.  [
*(laughter)*
]
So!  It's interesting, because every once in a while, a C++ programmer, you know, they
*flip*
:  they go over to the Dark Side.  I've seen it happen to some of the most brilliant C++ hackers, I mean they're computer scientists, but they're also C++ to the core.  And all of a sudden they're stuck with some, you know, lame JavaScript they had to do as an adjunct to this beautiful backend system they wrote.  And they futz around with it for a while, and then all of a sudden this sort of light bulb goes off, and they're like "Hey, what's up with this?  This is way more productive, you know, and it doesn't seem to be as slow as I'd sort of envisioned it to be."
And then they maybe do some build scripting in Python, and then all of a sudden they come over to my desk and they ask:  "Hey!  Can any of these be
*fast*
?"  Ha, ha, ha!  I mean, these are the same people that, you know, a year ago I'd talk to them and I'd say "why not use...
*anything*
but C++?  Why not use
[D](http://www.digitalmars.com/d/)
?  Why not use
?  Why not use
*anything*
but C++?  Right?
Because we all know that C++ has some very serious problems, that organizations, you know, put hundreds of staff years into fixing.  Portability across compiler upgrades, across platforms, I mean the list goes on and on and on.  C++ is like an evolutionary sort of dead-end.  But, you know, it's fast, right?
And so you ask them, why not use, like, D?  Or Objective-C.  And they say, "well, what if there's a garbage collection pause?"
Oooh!  [
*I mock shudder*
] You know, garbage collection – first of all, generational garbage collectors don't have pauses anymore, but second of all, they're kind of missing the point that they're still running on an operating system that has to do things like process scheduling and memory management.  There
*are*
pauses.  It's not as if you're running DOS!  I hope.  OK?
And so, you know, their whole argument is based on these fallacious, you know, sort of almost pseudo-religious... and often it's the case that they're actually based on things that used to be true, but they're not really true anymore, and we're gonna get to some of the interesting ones here.
But mostly what we're going to be talking about today is the compilers themselves.  Because they're getting really, really smart.
All right, so first of all I've gotta give a nod to these languages... which nobody uses.  OK?
has a bunch of really high-quality compilers.  And when they say they achieve, you know, "C-like speed", you've gotta understand, you know, I mean, there's more to it than just "does this benchmark match this benchmark?"
Everybody knows it's an ROI [calculation].  It's a tradeoff where you're saying:  is it
*sufficiently*
fast now that the extra hardware cost for it being 10 or 20 percent slower (or even 2x slower), you know, is outweighed by the productivity gains we get from having dynamic features and expressive languages.  That's of course the rational approach that everyone takes, right?
No!  Lisp has all those parentheses.  Of course nobody's gonna look at it.  I mean, it's ridiculous how people think about these things.
But with that said, these were actually very good languages.  And let me tell you something that's NOT in the slides, for all those of you who read them in advance, OK?  This is my probably completely wrong... it's certainly over-generalized, but it's a partly true take on what happened to languages and language research and language implementations over the last, say 30 years.
There was a period where they were kind of neck and neck, dynamic and static, you know, there were Fortran and Lisp, you know, and then there was a period where dynamic languages really flourished.  They really took off.  I mean, I'm talking about the research papers, you can look:  there's paper after paper, proofs...
And implementations!  StrongTalk was really interesting.  They added a static type system, an optional static type system on top of Smalltalk that sped it up like 20x, or maybe it was 12x.  But, you know, this is a prototype compiler that never even made it into production.  You've gotta understand that when a researcher does a prototype, right, that comes within, you know, fifty percent of the speed gains you can achieve from a production compiler...  because they haven't done a tenth, a hundredth of the optimizations that you
*could*
do if you were in the industry cranking interns through the problem, right?
I mean HotSpot's VM, it's got like ten years of Sun's implementation into not one, but two compilers in HotSpot, which is a problem they're trying to address.  So we're talking about, you know, a 12x gain really translates to something a lot larger than that when you put it into practice.
In case I forget to mention it, all these compiler optimizations I'm talking about, I do mean
*all*
of them, are composable.  Which is really important.  It's not like you have to choose this way or you have to choose that way.  They're composable, which means they actually reinforce each other.  So God only knows how fast these things can get.
This is the only interesting... this is actually the only, I would say, probably
*original*
, sort of compelling thought for this talk today.  I really – I started to believe this about a week ago.  All right?  Because it's an urban legend [that they change every decade].  You know how there's Moore's Law, and there are all these conjectures in our industry that involve, you know, how things work.  And one of them is that languages get replaced every ten years.
Because that's what was happening up until like 1995.  But the barriers to adoption are really high.  One that I didn't put on the slide here, I mean obviously there's the marketing, you know, and there's the open-source code base, and there are legacy code bases.
There's also, there are also a lot more programmers, I mean many more, orders of magnitude more, around the world today than there were in 1995.  Remember, the dot-com boom made everybody go: "Oooh, I wanna be in Computer Science, right?  Or I just wanna learn Python and go hack."  OK?  Either way.  (The Python hackers probably made a lot more money.)
But what we wound up with was a bunch of entry-level programmers all around the world who know
*one*
language, whichever one it is, and they don't want to switch.  Switching languages:  the second one is your hardest.  Because the first one was hard, and you think the second one's going to be that bad, and that you wasted the entire investment you put into learning the first one.
So, by and large, programmers – you know, the rank-and-file – they pretty much pick a language and they stay with it for their entire career.  And that is why we've got this situation where now, this...  See, there's plenty of great languages out there today.  OK?
I mean obviously you can start with Squeak, sort of the latest Smalltalk fork, and it's beautiful.  Or you can talk about various Lisp implementations out there that are smokin' fast, or they're smokin' good.  Or in one or two cases, both.
But also there's, like, the
[Boo](http://boo.codehaus.org/)
language, the
[io](http://www.iolanguage.com/)
language, there's the
[Scala](http://www.scala-lang.org/)
language, you know, I mean there's
[Nice](http://nice.sourceforge.net/)
, and
[Pizza](http://en.wikipedia.org/wiki/Pizza_%28programming_language%29)
, have you guys heard about these ones?  I mean there's a bunch of good languages out there, right?  Some of them are really good dynamically typed languages.  Some of them are, you know, strongly [statically] typed.  And some are hybrids, which I personally really like.
And nobody's using
*any*
of them!
Now, I mean, Scala might have a chance.  There's a guy giving a talk right down the hall about it, the inventor of – one of the inventors of Scala.  And I think it's a great language and I wish him all the success in the world.  Because it would be nice to have, you know, it would be nice to have that as an alternative to Java.
But when you're out in the industry, you
*can't*
.  You get lynched for trying to use a language that the other engineers don't know.  Trust me.  I've tried it.  I don't know how many of you guys here have actually been out in the industry, but I was talking about this with my intern.  I was, and I think you [
*(point to audience member)*
] said this in the beginning:  this is 80% politics and 20% technology, right?  You know.
And [my intern] is, like, "well I understand the argument" and I'm like "No, no, no!  You've never been in a company where there's an engineer with a Computer Science degree and ten years of experience, an architect, who's in your face
*screaming*
at you, with spittle flying on you, because you suggested using, you know...
[D](http://www.digitalmars.com/d)
.  Or
[Haskell](http://www.haskell.org/)
.  Or Lisp, or
, or take your pick."
In fact, I'll tell you a funny story.  So this... at Google, when I first got there, I was all idealistic.  I'm like, wow, well Google hires all these great computer scientists, and so they must all be completely language-agnostic, and ha, ha, little do I know...  So I'm up there, and I'm like, we've got this product, this totally research-y prototype type thing, we don't know.  We want to put some quick-turnaround kind of work into it.
But Google is really good at building infrastructure for
*scaling*
.  And I mean scaling to, you know, how many gazillion transactions per second or queries per second, you know, whatever.  They scale like nobody's business, but their "Hello, World" takes three days to get through.  At least it did when I first got to Google.  They were
*not*
built for rapid prototyping, OK?
So that means when you try to do what Eric Schmidt talks about and try to generate luck, by having a whole bunch of initiatives, some of which will get lucky, right?  Everybody's stuck trying to scale it from the ground up.  And that was unacceptable to me, so I tried to... I made the famously, horribly, career-shatteringly bad mistake of trying to use Ruby at Google, for this project.
And I became, very quickly, I mean almost overnight, the Most Hated Person At Google.  And, uh, and I'd have arguments with people about it, and they'd be like Nooooooo, WHAT IF...  And ultimately, you know, ultimately they actually convinced me that they were right, in the sense that there actually
*were*
a few things.  There were some taxes that I was imposing on the systems people, where they were gonna have to have some maintenance issues that they wouldn't have [otherwise had].  Those reasons I thought were good ones.
But when I was going through this debate, I actually talked to our VP Alan Eustace, who came up to a visit to Kirkland.  And I was like, "Alan!" (after his talk)  "Let's say, hypothetically, we've got this team who are really smart people..."
And I point to my friend Barry [pretending it's him], and I'm like: "Let's say they want to do something in a programming language that's not one of the supported Google languages.  You know, like what if they wanted to use, you know, Haskell?"
What I really wanted to do at the time was use Lisp, actually, but I didn't say it.  And [Alan] goes, "Well!"  He says, "Well... how would
*you*
feel if there was a team out there who said they were gonna use... LISP!"  [
*(laughter)*
]
He'd pulled his ace out of his [sleeve], and brandished it at me, and I went: "that's what I wanted to use."  And he goes, "Oh."  [
*(turning away quickly)*
]  And that was the end of the conversation.  [
*(laughter)*
]
But you know, ultimately, and it comes up all the time, I mean we've got a bunch of famous Lisp people, and (obviously) famous Python people, and you know, famous language people inside of Google, and of course they'd like to do some experimentation.  But, you know, Google's all about getting stuff done.
So that brings us full circle back to the point of this topic, which is:  the languages we have today, sorted by popularity at this instant, are probably going to stay about that popular for the next ten years.
Sad, isn't it?  Very, very sad.  But that's the way it is.
So how do we fix them?
How – how am I doing for time?  Probably done, huh?  Fifteen minutes?  [
*(audience member:  no, more than that)*
]  OK, good.
So!  I'm gonna talk a little bit about tools, because one interesting thing I noticed when I was putting this thing together, right, was that the ways you solve tools problems for dynamic languages are very similar to the way you solve perf problems.  OK?  And I'm not going to try to keep you guessing or anything.  I'll tell you what the sort of... kernel of the idea is here.
It's that... the notion of "static" versus "dynamic", where you kind of have to do all these optimizations and all these computations statically, on a language, is very old-fashioned.  OK?  And increasingly it's becoming obvious to
*everybody*
, you know, even the C++ crowd, that you get a lot better information at run-time.  *Much* better information.
In particular, let me come back to my inlining example.  Java inlines polymorphic methods!  Now the simplest way to do it was actually invented here at Stanford by Googler Urs Hoelzle, who's, you know, like VP and Fellow there, and it's called, it's now called Polymorphic Inline Caching.  He called it, uh,
[type-feedback compilation](http://research.sun.com/self/papers/pldi94.ps.gz)
, I believe is what he called it.  Great paper.  And it scared everybody, apparently.  The rumors on the mailing lists were that people were terrified of it, I mean it seems too hard.  And if you look at it now, you're like, dang, that was a good idea.
All it is, I mean, I told you the compiler doesn't know the receiver type, right?  But the thing is, in computing, I mean, heuristics work pretty well.  The whole 80/20 rule and the
[Power Law](http://en.wikipedia.org/wiki/Power_law)
apply pretty much unilaterally across the board.  So you can make assumptions like:  the first time through a loop, if a particular variable is a specific instance of a type, then it's probably going to be [the same type] on the remaining iterations of the loop.  OK?
So what he [Urs] does, is he has these counters at hot spots in the code, in the VM.  And they come in and they check the types of the arguments [or operands].  And they say, all right, it looks like a bunch of them appear to be class B, where we thought it might be class A.
So what we're gonna do is generate this fall-through code that says, all right, if it's a B – so they have to put the guard instruction in there; it has to be
*correct*
:  it has to handle the case where they're wrong, OK?  But they can make the guard instruction very, very fast, effectively one instruction, depending on how you do it.  You can compare the address of the intended method, or you can maybe do a type-tag comparison.  There are different ways to do it, but it's fast, and more importantly, if it's
*right*
, which it is 80-90% of the time, it falls through [
*i.e., inlines the method for that type - Ed.*
], which means you maintain your processor pipeline and all that stuff.
So it means they have
*predicted*
the type of the receiver.  They've successfully inlined that.  I mean, you can do a whole bunch of branching, and they actually found out through some experimentation that you only need to do 2 to 4 of these, right, before the gain completely tails off.  So you don't have to generate too much of this.  And they've expanded on this idea now, for the last ten years.
Getting back to my point about what's happening [over the past 30 years], there was an AI winter.  You all remember the AI winter, right?  Where, like, investors were pumping millions of dollars into Smalltalk and Lisp companies who were promising they'd cure world hunger, cure cancer, and everything?
And unfortunately they were using determinism!
They're using heuristics, OK, but you know... before I came to Google, you know, I was really fascinated by something
[Peter Norvig](http://en.wikipedia.org/wiki/Peter_Norvig)
was saying.  He was saying that they don't do natural language processing deterministically any more.  You know, like maybe, conceivably, speculating here, Microsoft Word's grammar checker does it, where you'd have a Chomsky grammar, right?  And you're actually going in and you're doing something like a compiler does, trying to derive the sentence structure.  And you know, whatever your output is, whether it's translation or grammar checking or whatever...
None of that worked!  It all became way too computationally expensive, plus the languages kept changing, and the idioms and all that.  Instead, [Peter was saying] they do it all probablistically.
Now historically, every time you came along, and you just obsoleted a decade of research by saying, "Well, we're just gonna kind of wing it, probabilistically" — and you know, Peter Norvig was saying they get these big data sets of documents that have been translated, in a whole bunch of different languages, and they run a bunch of machine learning over it, and they can actually match your sentence in there to one with a high probability of it being this translation.
And it's usually right!  It certainly works a lot better than deterministic methods, and it's computationally a lot cheaper.
OK, so whenever you do that, it makes people MAD.
Their first instinct is to say "nuh-UUUUUUH!!!!"  Right?  I'm serious!  I'm serious.  It happened when John von Neumann [and others] introduced
[Monte Carlo methods](http://en.wikipedia.org/wiki/Monte_Carlo_method)
.  Everyone was like "arrgggggh", but eventually they come around to it.  They go "yeah, I guess you're right; I'll go back and hit the math books again."
It's happening in programming languages
*today*
.  I mean, as we speak.  I mean, there's a paper I'm gonna tell you about, from October, and it's basically coming along and... it's not
*really*
machine learning, but you're gonna see it's the same kind of [data-driven] thing, right?  It's this "winging it" approach that's actually much cheaper to compute.  And it has much better results, because the runtime has all the information.
So let me just finish the tools really quick.
And I'm not talking to you guys; I'm talking to the people in the screen [i.e. watching the recording] – all these conversations I've had with people who say:  "No type tags means no information!"  I mean, effectively that's what they're saying.
I mean...

```
function foo(a, b) { return a + b; }var bar = 17.6;var x = {a: "hi", b: "there"};
```

What's
?  It's a
*function*
.  How did I know that?  [
*(laughter)*
]  What's
?  What's
?  You know, it's a composite type.  It's an Object.  It has two fields that are strings.  Call it a record, call it a tuple, call it whatever you want:  we know what it is.
The syntax of a language, unless it's Scheme, gives you a lot of clues about the semantics, right?  That's actually the one place, maybe, where lots of syntax actually wins out [over Scheme].  I just thought of that.  Huh.
OK, so... then you get into dynamic languages.  This [code] is all JavaScript.  This is actually something I'm working on right now.  I'm trying to build this JavaScript code graph, and you actually have to know all these tricks.  And of course it's undecidable, right, I mean this is, you know, somebody could be defining a function at the console, and I'm not gonna be able to find that.
So at some point you've gotta kind of draw the line.  What you do is, you look at your corpus, your code base, and see what are the common idioms that people are using.  In JavaScript, you've got a couple of big standard libraries that everybody seems to be including these days, and they all have their slightly different ways of doing function definitions.  Some of them use Object literals; some of them use the horrible
statement, you know, that JavaScript people hate.
But your compiler can figure all these out.  And I was actually going through this
, because they can even handle aliasing, right?  Your IDE for JavaScript, if I say "
", and you know...
Did I handle this here [in the slides]?
Yeah, right here!  And I say,
is an object,
is
, and I have an alias now.  The algorithm for doing this is right here in the
.  It's data-flow analysis.  Now they use it for compiler optimization to do, you know, live variable analysis, register allocation, dead-code elimination, you know, the list kind of goes on.  It's a very useful technique.  You build this big code graph of basic blocks...
So it's actually one of the few static-analysis that's actually carrying over in this new dynamic world where we have all this extra information.  But you can actually use it in JavaScript to figure out function declarations that didn't actually get declared until way later in the code.
Another big point that people miss is that the Java IDEs, you know, that are supposedly always right?  They're wrong.  If you miss
*one time*
, you're wrong.  Right?  In Java Reflection, obviously, the IDE has no information about what's going on in that string, by definition.  It's a string: it's quoted; it's opaque.
And so they always wave their hands and say "Ohhhhh, you can't do Rename Method!"
Even though Rename Method came from the
environment, of course, right?  And you say, "It came from the Smalltalk environment, so yes, you can do Rename Method in dynamic languages."
And they say "NO!  Because it'll miss sometimes!"
To which, I say to you people in the screen, you'd be
*astonished*
at how often the Java IDEs miss.  They miss every single instance of a method name that shows up in an XML configuration file, in a reflection layer, in a database persistence layer where you're matching column names to fields in your classes.  Every time you've deployed some code to some people out in the field...
Rename Method only works in a small set of cases.  These Refactoring tools that, really, they're acting are like the Holy Grail, you can do ALL of that in dynamic languages.  That's the proof, right? [
*I.e., static langs miss as often as dynamic – Ed.*
]
It's not even a very interesting topic, except that I just run across it all the time.  Because you ask people, "hey, you say that you're ten times as productive in Python as in your other language... why aren't you using Python?"
Slow?  Admittedly, well, we'll get to that.
And tools.  Admittedly.  But I think what's happened here is Java has kind of shown the new crop of programmers what Smalltalk showed us back in the 80s, which is that IDEs can work and they can be beautiful.
And
*more importantly*
– and this isn't in the slides either, for those of you who cheated – they
*have*
to be tied to the runtime.  They complain, you know, the Java people are like "Well you have to have all the code loaded into the IDE.  That's not scalable, it's not flexible, they can't simulate the program just to be able to get it correct."
And yet: any sufficiently large Java or C++ system has health checks, monitoring, it opens sockets with listeners so you can ping it programmatically; you can get, you know, debuggers, you can get remote debuggers attached to it; it's got logging, it's got profiling... it's got this long list of things that you need because the static type system failed.
OK...  Why did we have the static type system in the first place?
Let me tell you guys a story that, even if you know all this stuff, is still going to shock you.  I credit Bob Jervis for sharing this with me (the guy who wrote Turbo C.)
So javac, the Java compiler:  what does it do?  Well, it generates bytecode, does some optimizations presumably, and maybe tells you some errors.  And then you ship it off to the JVM.  And what happens to that bytecode?  First thing that happens is they build a tree out of it, because the bytecode verifier has to go in and make sure you're not doing anything [illegal].  And of course you can't do it from a stream of bytes: it has to build a usable representation.  So it effectively rebuilds the source code that you went to all that effort to put into bytecode.
But that's not the end of it, because maybe javac did some optimizations, using the old
.  Maybe it did some constant propagation, maybe it did some loop unrolling, whatever.
The next thing that happens in the JVM is the JIT undoes all the optimizations!  Why?  So it can do
*better*
ones because it has runtime information.
So it undoes all the work that javac did, except maybe tell you that you had a parse error.
And the weird thing is, Java keeps piling... I'm getting into rant-mode here, I can tell.  We're never going to make it to the end of these slides.  Java keeps piling syntax on, you know, but it's not making the language more expressive.  What they're doing is they're adding red tape and bureacracy for stuff you could do back in Java 1.0.
In Java 1.0, when you pulled a String out of a Hashtable you had to cast it as a String, which was really stupid because you said

```
String foo = (String) hash.get(...)
```

You know, it's like... if you had to pick a syntax [for casting], you should at least pick one that specifies what you think it's supposed to be, not what it's becoming –
*obviously*
becoming – on the left side, right?
And everybody was like, "I don't like casting!  I don't like casting!"  So what did they do?  What they
*could*
have done is they could have said, "All right, you don't have to cast anymore.  We know what kind of variable you're trying to put it in.  We'll cast it, and [maybe] you'll get a
."
Instead, they introduced generics, right, which is this huge, massive,
type system that they brought in, where you have to under[stand] – to actually use it you have to know the difference between
[covariant and contravariant](http://en.wikipedia.org/wiki/Covariance_and_contravariance_%28computer_science%29)
return [and argument] types, and you have to understand why every single mathematical... [
*I tail off in strangled frustration...*
]
And then what happens on mailing lists is users say:  "So I'm trying to do X."  And they say: "WELL, for the following category-theoretic reasons ...there's no way to do it."  And they go: "Oh!  Oh.  Then I'm gonna go use JavaScript, then."  Right?
I mean, it's like, what the hell did this type system do for Java?  It introduced inertia and complexity to everybody who's writing tools, to everybody who's writing compilers, to everybody who's writing runtimes, and to everybody who's writing code.  And it didn't make the language more expressive.
So what's happening?  Java 7 is happening.  And I encourage you all to go look at
*that*
train wreck, because oh my God.  Oh, God.  I didn't sleep last night.   I'm all wired right now because I looked at Java 7 last night.  And it was a
*mistake*
.  [
*(laughter)*
]  Ohhh...
OK.  So!  Moving right back along to our
*simple*
dynamic languages, the lesson is:  it's not actually harder to build these tools [for dynamic languages].  It's different.  And nobody's done the work yet, although people are starting to.  And actually
is a company with this
[IDEA](http://www.jetbrains.com/idea/features/javascript_editor.html)
[IDE], and they... my friends show off the JavaScript tool, you know, and it's like, man!  They should do one for Python, and they should do one for every single dynamic language out there, because they kick butt at it.  I'm sure they did all this stuff and more than I'm talking about here.
All right.  Now we can talk about perf.  This is the Crown Jewels of the talk.  Yeah.  So... unfortunately I have to make the disclaimer that everybody thinks about performance wrong, except for you guys 'cuz you all know, right?  But seriously, I mean, you know, you understand, I started out of school...
**sigh**
OK:  I went to the University of Washington and [then] I got hired by this company called Geoworks, doing assembly-language programming, and I did it for
*five years*
.  To us, the Geoworkers, we wrote a whole operating system, the libraries, drivers, apps, you know:  a desktop operating system in assembly.  8086 assembly!  It wasn't even good assembly!  We had four registers!  [Plus the] si [register] if you counted, you know, if you counted 386, right?  It was
*horrible*
.
I mean, actually we kind of liked it.  It was Object-Oriented Assembly.  It's amazing what you can talk yourself into liking, which is the real irony of all this.  And to us, C++ was the ultimate in Roman decadence.  I mean, it was equivalent to going and vomiting so you could eat more.  They had IF!  We had jump CX zero!  Right?  They had "Objects".  Well we did too, but I mean they had syntax for it, right?  I mean it was all just such weeniness.  And we knew that we could outperform any compiler out there because at the time, we could!
So what happened?  Well, they went bankrupt.  Why?  Now I'm probably disagreeing – I know for a fact that I'm disagreeing with every Geoworker out there.  I'm the only one that holds this belief.  But it's because we wrote fifteen million lines of 8086 assembly language.  We had really good tools, world class tools:  trust me, you need 'em.  But at some point, man...
The problem is, picture an ant walking across your garage floor, trying to make a straight line of it.  It ain't gonna make a straight line.  And you know this because you have
*perspective*
.  You can see the ant walking around, going hee hee hee, look at him locally optimize for that rock, and now he's going off this way, right?
This is what we were, when we were writing this giant assembly-language system.  Because what happened was, Microsoft eventually released a platform for mobile devices that was much faster than ours.  OK?  And I started going in with my debugger, going, what?  What is up with this?  This rendering is just really slow, it's like sluggish, you know.  And I went in and found out that some title bar was getting rendered 140 times every time you refreshed the screen.  It wasn't just the title bar.  Everything was getting called multiple times.
Because we couldn't see how the system worked anymore!
Small systems are not only
*easier*
to optimize, they're
*possible*
to optimize.  And I mean globally optimize.
So when we talk about performance, it's all crap.  The most important thing is that you have a small system.  And then the performance will just fall out of it naturally.
That said, all else being equal, let's just pretend that Java can make small systems.  Heh, that's a real stretch, I know.  Let's talk about actual optimization.
And by the way, here are some real examples, sort of like the Geoworks one, where a slower language wound up with a faster system.  It's not just me.  I've seen it all over the place.  Do you know why this one happened?  Why was the
faster than Struts?  This started one of the internet's largest flamewars since Richard Stallman dissed Tcl back in the 80s, you know.  You guys remember that?  [
*(laughter)*
]
I mean, the Java people went
*nuts*
, I mean really really nuts, I mean like angry Orcs, they were just like AAAaaaaauuuugh, they did NOT want to hear it.  OK?  It was because they were serializing everything to and from XML because Java can't do declarations.  That's why.  That's the reason.  I mean, stupid reasons, but performance comes from some strange places.
That said, OK, disclaimers out of the way...
Yeah yeah, people are using them.
Um, yeah.  So JavaScript.  JavaScript has been really interesting to me lately, because JavaScript actually does care about performance.  They're the first of the modern dynamic languages where performance has become an issue not just for the industry at large, but also increasingly for academia.
Why JavaScript?  Well, it was Ajax.  See, what happened was...  Lemme tell ya how it was supposed to be.  JavaScript was going away.  It doesn't matter whether you were Sun or Microsoft or anybody, right?  JavaScript was going away, and it was gonna get replaced with... heh.  Whatever your favorite language was.
I mean, it wasn't actually the same for everybody.  It might have been C#, it might have been Java, it might have been some new language, but it was going to be a
*modern*
language.  A fast language.  It was gonna be a scalable language, in the sense of large-scale engineering.  Building desktop apps.  That's the way it was gonna be.
The way it's
*really*
gonna be, is JavaScript is gonna become one of the smokin'-est fast languages out there.  And I mean
*smokin'*
fast.
Now it's not the only one that's making this claim.  There's actually a lot of other... you guys know about
[PyPy](http://codespeak.net/pypy/dist/pypy/doc/home.html)
?  Python in Python?  Those crack fiends say they can get C-like performance.  Come on... COME ON!  They... I mean, seriously!  That's what they say.
Here's the deal, right?  They're saying it because they're throwing all the old assumptions out.  They can get this performance by using these techniques here, fundamentally.  But if nobody believes them, then even when they achieve this performance it's not gonna matter because still nobody's gonna believe them, so all of this stuff we're talking about is a little bit moot.
Nevertheless, I'm going to tell you about some of the stuff that I know about that's going on in JavaScript.
So type inference.  You
*can*
do type inference.  Except that it's lame, because it doesn't handle weird dynamic features like upconverting integers to Doubles when they overflow.  Which JavaScript does, interestingly enough, which is I guess better behavior than... I mean, it still overflows eventually, right?
We overflowed a
at Google once.  Nobody thought that was possible, but it actually happened.  I'll tell you about that later if you want to know.
So... oh yeah, I already talked about Polymorphic Inline Caches.  Great!  I already talked about a lot of this stuff.
This one's really cool.  This is a trick that somebody came up with, that you can actually – there's a
[paper](http://www.ics.uci.edu/%7Efranz/Site/pubs-pdf/ICS-TR-07-10.pdf)
on it, where you can actually figure out the actual types of any data object in any dynamic language: figure it out the first time through by using this double virtual method lookup.  They've boxed these things.  And then you just expect it to be the same the rest of the time through [the loop], and so all this stuff about having a type-tag saying this is an
– which might not actually be technically correct, if you're going to overflow into a Double, right?  Or maybe you're using an int but what you're really using is a byte's worth of it, you know.  The runtime can actually figure things out around bounds that are undecidable at compile time.
So that's a cool one.
This is the really cool one.  This is the really, really cool one.  Trace trees.  This is a
[paper that came out in October](http://www.ics.uci.edu/%7Efranz/Site/pubs-pdf/C44Prepub.pdf)
.  This is the one, actually... I'll be honest with you, I actually have two optimizations that couldn't go into this talk that are even cooler than this because they haven't published yet.  And I didn't want to let the cat out of the bag before they published.  So this is actually just the tip of the iceberg.
But trace trees, it's a really simple idea.  What you do is your runtime, your VM, you know, it's interpreting instructions and can count them.  Well, it can also record them!  So any time it hits, basically, a branch backwards, which usually means it's going to the beginning of a loop, which usually means it's going to be a hot spot, especially if you're putting a counter there...  Obviously [in] the inner loops, the hot spots will get the highest counts, and they get triggered at a certain level.
It turns on a recorder.  That's all it does.  It starts recording instructions.  It doesn't care about loop boundaries.  It doesn't care about methods.  It doesn't care about modules.  It just cares about "What are you executing?"
And it records these tree – well actually, traces, until they get back to that point.  And it uses some heuristics to throw stuff away if it goes too long or whatever.  But it records right through methods.  And instead of setting up the activation, it just inlines it as it goes.  Inline, inline, inline, right?  So they're big traces, but they're known to be hot spots.
And even here in the
, Aho, Sethi and Ullman, they say, you know, one of the most important things a compiler can do is try to identify what the hot spots are going to be so it can make them efficient.  Because who cares if you're optimizing the function that gets executed once at startup, right?
So these traces wind up being trees, because what can happen is, they branch any time an operand is a different type.  That's how they handle the overflow to Double:  there'll be a branch.  They wind up with these trees.  They've still got a few little technical issues like, for example, growing exponentially on the Game of Life.  There's a
[blog about it](http://andreasgal.com/2008/02/28/tree-folding/)
, um... I'm sorry, I've completely forgotten his name [
*Andreas Gal*
], but I will blog this.  And the guy that's doing these trace trees, he got feedback saying that they've got exponential growth.
So they came up with this novel way of folding the trace trees, right, so there are code paths that are almost identical and they can share, right?
It's all the same kind of stuff they were doing with
*these*
[Dragon Book] data structures back when they were building static compilers.  We are at the very beginning of this research!  What has happened is, we've gone from Dynamic [to] AI Winter... dynamic research stopped, and anybody who was doing it was sort of anathema in the whole academic [community]... worldwide across all the universities.  There were a couple of holdouts.  [
[Dan Friedman](http://en.wikipedia.org/wiki/Daniel_P._Friedman)
and]
[Matthias Felleisen](http://en.wikipedia.org/wiki/Matthias_Felleisen)
, right, the
guys, right?  Holding out hope.
And everybody else went and chased static.  And they've been doing it like crazy.  And they've, in my opinion, reached the theoretical bounds of what they can deliver, and it has FAILED.  These static type systems, they're WRONG.  Wrong in the sense that when you try to do something, and they say:  No, category theory doesn't allow that, because it's not elegant...  Hey man:  who's wrong?  The person who's trying to write the program, or the type system?
And some of the type errors you see in these Hindley-Milner type [systems], or any type system, like "expected (int * int * int)", you know, a tuple, and "but got (int * int * int)", you know [
*(clapping my hands to my head)*
] it's pretty bad, right?  I mean, they've, I think they've failed.  Which is why they're not getting adopted.
Now of course that's really controversial.  There are probably a bunch of type-systems researchers here who are really mad, but...
What's happening is:  as of this Ajax revolution, the industry shifted to trying to optimize JavaScript.  And that has triggered what is going to be a landslide of research in optimizing dynamic languages.
So these tricks I'm telling you about, they're just the beginning of it.  And if we come out of this talk with one thing, it's that it's cool to optimize dynamic languages again!  "Cool" in the sense of getting venture funding, right?  You know, and research grants... "Cool" in the sense of making meaningful differences to all those people writing Super Mario clones in JavaScript.
You know.  It's
*cool*
.
And so I encourage you, if you're a language-savvy kind of person, to jump in and try to help.  Me, I'm probably going to be doing grunt implementations, since I'm not that smart.
And I don't even need to talk about this [last optimization — Escape Analysis], since you already knew it.
All right!  So that's it.  That's my talk.  CPUs... you get all the good information about how a program is running
*at run time*
.  And this has huge implications for the tools and for the performance.  It's going to change the way we work.  It's eventually – God, I hope sooner rather than later – going to obsolete C++ finally.
It's going to be a lot of work, right?
And then, when we finish, nobody's going to use it.  [
*(laughter)*
]  Because, you know.  Because that's just how people are.
That's my talk!  Thanks.  [
*(applause)*
]
Questions?  No questions?  I think we're out of time, right?  [
*(audience:  no, we have half an hour)*
]
**Q:  What's your definition of marketing?**
Hey man, I'm doing it
*right now*
. [
*(laughter)*
]
I am!  In a sense, right?  I mean, like, Perl was a marketing success, right?  But it didn't have Sun or Microsoft or somebody hyping it.  It had, you know, the guy in the cube next to you saying "Hey, check out this Perl.  I know you're using Awk, but Perl's, like, weirder!"
The marketing can happen in any way that gets this message across, this meme out to everybody, in the Richard Dawkins sense.  That's marketing.  And it starts from just telling people:  hey, it's out there.
**Q:  Do you see any of this stuff starting to move into microprocessors or instructions?**
Ah!  I knew somebody was going to ask that.  So unfortunately, the JITs that are doing all these cool code optimizations could potentially be running into these weird impedance mismatches with microprocessors that are doing their own sets of optimizations.  I know
*nothing*
about this except that it's... probably gonna happen.  And, uh, God I hope they talk to each other.  [
*Editor's note:  after the talk, I heard that trace trees started life in hardware, at HP.*
]
**Q:  You could imagine CMS (?) pulling all these stunts and looking at stuff and saying, "Oh, I know that this is just machine language... oh, look!  That's an int, and..."**
Yes.  I do know... that there's a compiler now that compiles [machine code] into microcode, a JIT, you know, I was reading about it.
**Q:  So one problem with performance is that it's not just fast performance vs. slow performance.  What they're having a lot of trouble with is that a function one time takes a millisecond or a microsecond, and another time it takes 300 or 500 or 1000 times longer. [*part of question muted*] Any thoughts on how to improve the performance predictability of dynamic languages?**
Yeah...
**sigh**
.  Well, I think for the forseeable future, I mean honestly having talked to several of the VM implementers, they're not making any claims that JavaScript's going to be as fast as C any time soon.  Not for the forseeable future.  It's going to be very fast, right, but it's not going to be quite... they're not going to make the crazy promises that Sun did.
Which means that these dynamic speedups are primarily going to be useful in long-running distributed processes, for which a little glitch now and then isn't going to matter in the grand scheme of the computation.  Or, they're going to be, you know, the harder one is in clients, where you've got a browser app, and you're hoping that the glitch you're talking about isn't on the order of hundreds of milliseconds.
Generational garbage collectors is the best answer I've got for that, because it reduces the pauses, and frankly, the garbage collectors for all the [new] dynamic languages today are crap.  They're mark-and-sweep, or they're reference counted.  They've got to fix that.  Right out of the starting gate, that's gonna nullify 80 percent of that argument.
For the rest, I don't know.  It's up to you guys.
**Q:  You also have to look at your storage management; you have to understand your storage in your program, and have some sort of better control over that...**
That's right.  As you point out, it's domain-specific.  If your bottleneck is your database, all bets are off.
**Q:  You seem to be equating dynamic language with dynamic encoding, that you have "dynamic language equals JIT"."**
For this talk, yes.  [
*(laughter)*
]
**Q: ...but the same thing can be done for static languages.**
Yeah, absolutely!
**Q:  ...and as soon as the marketing starts getting some market penetration, the C++ people will just simply come around and say, "You can have maintainability *and* performance".**
Yep!  They can, actually.  That's what they'll say.  And I'll say:  "All right.  I'll give you a thousand dollars when you're done."  OK?  Because C++ have actually shot themselves in their own foot.  By adding so many performance hacks into the language, and also actual features into the language for performance, like pointer manipulation, the language itself is large enough that it's very difficult.  It's much more difficult to envision doing a JIT that can handle pointers properly, for example, right?  You can do it!  It's just a
*lot*
more work than it is for these simple languages.  [
*In retrospect, I'm not so sure about this claim.  Trace trees may not care about pointers, so maybe it wouldn't be that hard?  Of course, they'd have to move to a JIT first, requiring an initial slowdown, so it'd probably never happen.  -Ed.*
]
So they're winding up... they're winding up in a situation where they're gonna have to weigh it carefully, and say, "OK:  when all is said and done, is my language actually gonna be faster than these other languages that have gone through this process already?"  Because now we're on a more level playing field.
Especially as it's getting increasingly difficult to predict exactly what the hardware architecture is going to be, and those mismatches tend to have a huge impact on what the JIT actually can do.  I mean, hardware's getting really out there now, and the compiler writers are still trying to figure out what to do about it.  I mean, even the stuff they're doing in the JITs today might not apply tomorrow.
So I realize it's a weak answer, but I'm saying, you know, it's a hard proposition for me to imagine them doing.  They'll try!  Maybe they'll succeed.
**Q:  The other side of dynamic languages is second-order systems:  the ability to do an eval.  And the difficulty with that is intellectual tractability.  Most people use second-order languages to write first-order programs.  Is there any real reason to even have a second-order language for writing Cobol?**
Can they hear these questions in the audio?  Because this is a really good point.
So this is, I mean, I don't know the answer to this.  This is a hard question, OK?
Java has kind of gotten there without even having eval.  They've tiered themselves into sort of second-order people who know how to manipulate the type-theory stuff, you know, right?  People go off to them with batch requests:  "Please write me a type expression that meets my needs".  And it comes back.  So we're already in sort of the same situation we were in with
, you know, or with any sort of macro system, or any eval system.  Which is that really only a few people can be trusted to do it well, and everybody else kind of has to... right?
So I don't know, maybe it's just a cultural... maybe it's already solved, and we just have to live with the fact that some programming languages are going to have dark corners that only a few people know.  It's unfortunate.  It's ugly.
[
*My PhD languages intern, Roshan James, replies to the questioner:  Your usage of the phrase 'second-order', where does that come from?  A comment as to what you're telling us, which is that some sort of phased evaluation, specific to Scheme at least, we're saying... some would say the complexity of writing Scheme macros is roughly on the order of writing a complex higher-order procedure.  It's not much harder.  A well thought out macro system is not a hard thing to use.*
]
...says the Ph.D. languages intern!  He's representing the majority viewpoint, of course.  [
*(laughter)*
]  I'll tell you what:  I'll let you two guys duke it out after the talk, because I want to make sure we get through anybody else's questions.
**Q:  You're assuming you have a garbage-collected environment.  What do you think about reference counting, with appropriate optimization?**
Ummmm...  No.  [
*(laughter)*
]  I mean, come on.  Garbage collection... you guys know that, like, it's faster in Java to allocate an object than it is in C++?  They've got it down to, like, three instructions on some devices, is that right?  And the way the generational garbage collector works is that 90% of the objects get reused.  Plus there's fine-grained interleaving with the way the memory model of the operating system works, to make sure they're dealing with issues with, whaddaya call it, holes in the heap, where you can't allocate, I mean there's a whole bunch of stuff going on. [
*This was me doing my best moron impersonation.  Sigh. -Ed.*
]
So, like, it works.  So why throw the extra burden on the programmer?  Even [in] C++, by the way,
[Stroustroup wants to add garbage collection](http://www.artima.com/cppsource/cpp0x.html)
!
**Q:  If you believe your other arguments, you can do the reference counting or local pooling, and point out when it's actually wrong.**
Right.  The philosophical answer to you guys is:  compilers will eventually get smart enough to deal with these problems better than a programmer can.  This has happened time and again.  [For instance] compilers generate better assembly code [than programmers do].
All the "tricks" that you learned to optimize your Java code, like marking everything final, so that the compiler can inline it –  the VM does that for you now!  And it puts [in] some
hooks to see if you load a class that makes it non-final, and then [if the assumption is invalidated later] it undoes the optimization and pulls the inlining out.
That's how smart the VM is right now.  OK?  You only need a few compiler writers to go out there and obsolete
*all*
the tricks that you learned.  All the memory-pooling tricks...
Hell, you guys remember
and
in Java?  They introduced
recently, which is an unsynchronized version, so they didn't have to have a lock?  Guess what?
[Java 6 optimizes those locks away](http://java.sun.com/performance/reference/whitepapers/6_performance.html)
.  Any time
*you*
can see that the lock isn't needed, they can see it. [
*Editor's Note:  See "Biased locking" in the linked perf whitepaper.  It's an astoundingly cool example of the predictive-heuristic class of techniques I've talked about today.*
]
So now all these tricks, all this common wisdom that programmers share with each other, saying "I heard that this hashtable is 1.75 times faster than blah, so therefore you should...", all the micro-optimizations they're doing – are going to become obsolete!  Because compilers are smart enough to deal with that.
**Q:  You didn't mention APL, which is a very nice dynamic language...**
I didn't mention
[APL](http://en.wikipedia.org/wiki/APL_%28programming_language%29)
!?  Oh my.  Well, I'm sorry.  [
*(laughter)*
]
**Q:  The thing is, well – several of the APL systems, they incorporated most of the list of program transformations you're talking about.  And they did it several decades ago.**
Yeah, so... so you could've said Lisp.  You could've said Smalltalk.  "We did it before!"  And that was kind of, that was one of the important points of the talk, right?  It
*has*
been done before.  But I'm gonna stand by my – especially with APL – I'm going to stand by my assertion that the language popularity ranking is going to stay pretty consistent.  I don't see APL moving 50 slots up on the [list].
I'm sorry, actually.  Well not for that case. [
*(laughter)*
]  But I'm sorry that in general, the languages that got optimized really well, and were really elegant, arguably more so than the languages today, you know, in a lot of ways, but they're not being used.
I tried!  I mean, I tried.  But I couldn't get anybody to use them.  I got lynched, time and again.
**Q:  So what's the light at the end of the tunnel for multithreading?**
Oh, God!  You guys want to be here for another 2 hours? [
*(laughter)*
]  I read the scariest article that I've read in the last 2 years: an interview with, I guess his name was Cliff Click, which I think is a cool name.  He's like the HotSpot -server VM dude, and somebody, Kirk Pepperdine was
[interviewing him on The Server Side](http://www.theserverside.com/tt/knowledgecenter/knowledgecenter.tss?l=MetalMeetsJVM)
.  I just found this randomly.
And they started getting down into the threading, you know, the Java memory model and how it doesn't work well with the actual memory models, the hardware, and he started going through, again and again, problems that every Java programmer – like, nobody knows when the hell to use
, and so all of their reads are unsynchronized and they're getting stale copies...
And he went through – went through problems to which he does not know the answer.  I mean, to where I came away going Oh My God, threads are irreparably busted.  I don't know what to do about it.  I really don't know.
I do know that I did write a half a million lines of Java code for this game, this
[multi-threaded game I wrote](http://www.cabochon.com/)
.  And a lot of weird stuff would happen.  You'd get
s in situations where, you know, you thought you had gone through and done a more or less rigorous proof that it shouldn't have happened, right?
And so you throw in an "if null", right?  And I've got "if null"s all over.  I've got error recovery threaded through this half-million line code base.  It's contributing to the half million lines, I tell ya.  But it's a very robust system.
You
*can*
actually engineer these things, as long as you engineer them with the certain knowledge that you're using threads wrong, and they're going to bite you.  And even if you're using them right, the implementation probably got it wrong somewhere.
It's really scary, man.  I don't... I can't talk about it anymore.  I'll start crying.
**Q:  These great things that IDEs have, what's gonna change there, like what's gonna really help?**
Well, I think the biggest thing about IDEs is... first of all, dynamic languages will catch up, in terms of sort of having feature parity.  The other thing is that IDEs are increasingly going to tie themselves to the running program.  Right?  Because they're already kind of doing it, but it's kind of half-assed, and it's because they still have this notion of static vs. dynamic, compile-time vs. run-time, and these are... really, it's a continuum.  It really is.  You know, I mean, because you can invoke the compiler at run time.
**Q:  Is it allowed at Google to use Lisp and other languages?**
No.  No, it's not OK.  At Google you can use C++, Java, Python, JavaScript... I actually found a legal loophole and used server-side JavaScript for a project.  Or some of our proprietary internal languages.
That's for production stuff.  That's for stuff that armies of people are going to have to maintain.  It has to be high-availability, etc.  I actually wrote a
[long blog about this](http://steve-yegge.blogspot.com/2007/06/rhino-on-rails.html)
that I'll point you to that actually... Like, I actually came around to their way of seeing it.  I did.  Painful as it was.  But they're right.
**Q:  [*question is hard to hear*]**
[
*me paraphrasing*
] Are we going to have something Lisp Machines didn't?
**Q:  Yes.**
Well... no.  [
*(loud laughter)*
]
I say that in all seriousness, actually, even though it sounds funny.  I, you know, I
*live*
in
.  And Emacs is the
.  All the rest of them are at garage sales.  But Emacs
*is*
a Lisp Machine.  It may not be the best Lisp, but it is one.
And you know, T.V Raman, you know, research scientist at Google, who, he doesn't have the use of his sight... he's a completely fully productive programmer, more so than I am, because Emacs is his window to the world.  It's his remote control.
[EmacsSpeak](http://emacspeak.sourceforge.net/)
is his thesis.  It's amazing to watch him work.
Emacs, as a Lisp Machine, is capable of doing
*anything*
that these other things can.  The problem is, nobody wants to learn Lisp.
**Q:  And it doesn't have closures.**
And it doesn't have closures, although you can fake them with macros.
I'm actually having lunch with an [ex-]Emacs maintainer tomorrow.  We're going to talk about how to introduce concurrency, a better rendering engine, and maybe some Emacs Lisp language improvements.  You know, even Emacs has to evolve.
But the general answer to your question is No.  Lisp Machines pretty much had it nailed, as far as I'm concerned.  [
*(shrugging)*
]  Object-oriented programming, maybe?  Scripting?  I dunno.
**Q:  Many years ago, I made the great transition to a fully type-checked system.  And it was wonderful.  And I remember that in the beginning I didn't understand it, and I just did what I had to do.  And one dark night, the compiler gave me this error message, and it was right, and I thought "Oh wow, thank you!"  I'd suddenly figured it out.**
Yes!  "Thank you."  Yes.
Although it's very interesting that it took a long time before it actually told you something useful.  I remember my first experience with a C++ compiler was, it would tell me "blublblbuh!!", except it wouldn't stop there.  It would vomit for screen after screen because it was
[Cfront](http://en.wikipedia.org/wiki/Cfront)
, right?
And the weird thing is, I realized early in my career that I would actually rather have a runtime error than a compile error.  [
*(some laughs)*
]  Because at that time... now this is way contrary to popular opinion.  Everybody wants early error detection.  Oh God, not a runtime error, right?  But the debugger gives you this ability to start poking and prodding, especially in a more dynamic language, where you can start simulating things, you can back it up...  You've got your time-machine debuggers like the
one, that can actually save the states and back up.
You've got amazing tools at your disposal.  You've got your print, your console printer, you've got your logging, right?  [
*Ummm... and eval.  Oops.  -Ed.*
] You've got all these assertions available.  Whereas if the compiler gives you an error that says "expected expression angle-bracket", you don't have a "compiler-debugger" that you can shell into, where you're trying to, like – you could fire up a debugger on the compiler, but I don't recommend it.
So, you know, in some sense, your runtime errors are actually kind of nicer.  When I started with Perl, which was pretty cryptic, you know, and I totally see where you're coming from, because every once in a while the compiler catches an error.  But the argument that I'm making is NOT that compilers don't occasionally help you catch errors.  The argument that I'm making is that you're gonna catch the errors one way or the other.  Especially if you've got unit tests, or QA or whatever.
And the problem is that the type systems, in programming in the large, wind up getting in your way... way too often.  Because the larger the system gets, the more desperate the need becomes for these dynamic features, to try to factor out patterns that weren't evident when the code base was smaller.  And the type system just winds up getting in your way again and again.
Yeah, sure, it catches a few trivial errors, but what happens is, when you go from Java to JavaScript or Python, you switch into a different mode of programming, where you look a lot more carefully at your code.  And I would argue that a compiler can actually get you into a mode where you just submit this batch job to your compiler, and it comes back and says "Oh, no, you forgot a semicolon", and you're like, "Yeah, yeah, yeah."  And you're not even really thinking about it anymore.
Which, unfortunately, means you're not thinking very carefully about the algorithms either.  I would argue that you actually craft better code as a dynamic language programmer in part because you're
*forced*
to.  But it winds up being a good thing.
But again, I – this is all very minority opinion; it's certainly not majority opinion at Google.  All right?  So this is just my own personal bias.
**Q:  [*question too hard to hear over audio, something about is it possible for the compiler at least to offer some help*]**
You know, that's an interesting question.  Why do compiler errors have to be
*errors*
?  Why couldn't you have a compiler that just goes and gives you some advice?  Actually, this is what IDEs are excelling at today.  Right?  At
*warnings*
.  It's like, "ah, I see what you're doing here, and you don't really need to.  You probably shouldn't."
It's weird, because Eclipse's compiler is probably a lot better than javac.  Javac doesn't need to be good for the reasons I described earlier, right?  It all gets torn down by the JIT.  But Eclipse's compiler needs to give you that exact help.  The programmer help, the day-to-day help, I missed a semicolon, I missed this, right?  And Eclipse and IntelliJ, these editors, their compilers are very very good at error recovery, which in a static batch compiler usually just needs to be:  BLAP, got an error!
OK?  So to an extent I think we
*are*
getting tools that come along and act like the little paper-clip in Microsoft Office.  You know.  Maybe not quite like that.
**Q: The only thing I worry about is that there's a chunk of code that you really want to work sometimes, but the error-recovery parts are hard to test.**
That's the part you
*have*
to do at runtime, right?  Well, I mean, when you get into concurrency you're just screwed, but if you're talking about situations where it's very difficult to... I mean, it's computationally impossible to figure out whether all paths through a code graph are taken.  I mean, it's NP-complete, you can't do this, right?  But the VM can tell you which code paths got taken, and if it doesn't [get taken], you can change your unit test to force those code paths to go through, at which point you've now exercised all of your code.  Right?  That's kind of the way, you know, they do it these days.
And I would say it's a pain in the butt, but I mean... it's a pain in the butt because... a static type-systems researcher will tell you that unit tests are a poor man's type system.  The compiler ought to be able to predict these errors and tell you the errors, way in advance of you ever running the program.  And for the type systems they've constructed, this is actually true, by and large, modulo assertion errors and all these weird new runtime errors they actually have to, heh, inject into your system, because of type-system problems.
But by and large, I think what happens is unless the type system actually delivers on its promise, of always being right and always allowing you to model any lambda-calculus computation your little heart desires, OK?  Unless it can do that, it's gonna get in your way at some point.
Now again, this is all personal choice, personal preference.  I think, you know, static compilers and error checkers, they have a lot of value and they're going to be around for a long time.  But dynamic languages could get a lot better about it.
I'm not trying to refute your point. I'm just saying that... there are tradeoffs, when you go to a dynamic language.  I have come around... I've gone from dynamic to static and back to dynamic again, so I've done the whole gamut.  And I've decided that for very large systems, I prefer the dynamic ones, in spite of trade-offs like the one you bring up.
**Q:  Actually you said, for hybrid systems, where pieces of it are dynamic and pieces are static...**
I think some of it has been pretty... there's a great paper from Adobe about it, right?
[Evolutionary programming](http://www.ecmascript.org/es4/spec/evolutionary-programming-tutorial.pdf)
?  Talks about how you prototype your system up, and then you want to lock it down for production, so you find the spots where there are API boundaries that people are going to be using.  You start putting in contracts, in the way of type signatures and type assertions.
Why not build that functionality into the language?  Then you don't have to build a prototype and re-implement it in C++.  That's the thinking, anyway.  It seems like a great idea to me, but it hasn't caught on too much yet.  We'll see. [
*Editor's note:  The main hybrid examples I'm aware of are StrongTalk, Common Lisp, Groovy and EcmaScript Edition 4.  Any others?*
]
All right, well, now we're definitely over time, and I'm sure some of you guys want to go.  So thank you very much!

---

At this point I got mobbed by a bunch of grad students, profs, and various interested people with other questions.  They dumped an absolutely astounding amount of information on me, too – papers to chase down, articles to follow up on, people to meet, books to read.  There was lots of enthusiasm.  Glad they liked it!