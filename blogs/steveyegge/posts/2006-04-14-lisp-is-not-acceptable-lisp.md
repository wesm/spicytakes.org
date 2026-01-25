---
title: "Lisp is Not an Acceptable Lisp"
date: 2006-04-14
url: https://steve-yegge.blogspot.com/2006/04/lisp-is-not-acceptable-lisp.html
word_count: 3146
---

It's been over four months since Eric Kidd posted his infamous
[Why Ruby is an acceptable LISP](http://www.randomhacks.net/articles/2005/12/03/why-ruby-is-an-acceptable-lisp)
article.  You know, the one that got approximately 6.02e23 comments, ranging from "I agree!" through "I hate you!" to "I bred them together to create a monster!"  Any time the comment thread becomes huge enough to exhibit emergent behavior, up to and including spawning new species of monsters, you know you've touched a nerve.
What amazes me is that nobody's pointed out the obvious counter-observation: Lisp is not an acceptable LISP.  Not for any value of Lisp.  There's nothing magical about this, nothing partisan.  If Lisp were acceptable, then we'd all be using it.
You've all read about the
[Road to Lisp](http://wiki.alu.org/The_Road_to_Lisp_Survey)
.  I was on it for a little over a year.  It's a great road, very enlightening, blah blah blah, but what they fail to mention is that Lisp isn't the at the end of it.  Lisp is just the last semi-civilized outpost you hit before it turns into a dirt road, one that leads into the godawful swamp most of us spend our programming careers slugging around in.  I guarantee you there isn't one single Lisp programmer out there who uses exclusively Lisp.  Instead we spend our time hacking around its inadequacies, often in other languages.
So for four months I've been waiting for someone
*else*
to say it, but so far it's not happening.  Why aren't we admitting it?
Oh, right.  Religion.  I keep forgetting about that.
Lisp programmers are just like all other programmers: they want to write code and get cool stuff done, which presupposes they've already learned the last programming language they'll ever need.  There's all this real-life stuff (jobs, family, stability, all the usual suspects) intruding on you as a programmer, demanding that you quit dorking around looking for the One True Language, and settle down on whatever barren rock you happen to be squatting on at the moment, and call it Good.  So most Lisp programmers — and that's not many, since not many programmers make it even close to that far down the Road — see that last outpost of technical civilization, peer balefully into the swamp, and decide to check into the Lisp hotel for good.  Not realizing, of course, that all its rooms are in the swamp proper.
We all know it's tricky to have a rational discussion about a religion.  Non-Lispers will be able to read this without getting their feathers ruffled.  Some Lispers aren't too far gone, so let's assume we're talking to them, and take a look at some of Lisp's problems that make it flat-out unacceptable.  At least for LISP, you know, the idealized one.
**Problem 1: Which Lisp?**
Sorry, folks, but you can't trivialize this one.  Let's say I'm a new would-be Lisper, just finished walking down that long damn Road, and now that I'm here, I'm ready to start using it.  Which "it" should I use?  The answer is "it depends", and that's pretty unfortunate, because right there you've just lost users.  With Python or Ruby or Java, you've only got one language to choose from.  Or at least you can be comfortable that there's a single
*canonical*
version, and the rest (e.g. Jython) are highly experimental territory.
Pick Scheme, and you have to pick
*a*
Scheme.  Pick Common Lisp, and you have to pick
*a*
Common Lisp.  Heck, there are even two or three flavors of Emacs-Lisp out there.
Most newcomers eventually (and independently) decide the same thing: Scheme is a better language, but Common Lisp is the right choice for production work.  CL has more libraries, and the implementations are somewhat more compatible than Scheme implementations, particularly with respect to macros.  So newcomers heave a deep sigh, and they learn to accept LISP-2, names like rplaca, case-insensitivity, '(ALL CAPS OUTPUT), and all the other zillions of idiosyncracies of a standard Common Lisp implementation.  Eventually, if they stick with Lisp at all, they learn they can override most of these defaults in nonportable ways, which makes things infinitesimally more bearable.
Whatever.  If you're a Lisper, you dealt with all this crap years ago, and now you're committed.  If you're not a Lisper, then you're not very likely to become one any time soon.  In fact your probability of learning Lisp is decreasing over time, as other languages continue to close the gap in the Lispy areas, and simultaneously increase their lead in non-Lispy areas where Lisp is making little (if any) progress.
Let's look at some of those areas.  But first, let me mention one last problem in the "which Lisp" space.  It's dirty laundry that needs airing.  The problem: Paul Graham.  I mean, the guy's a genius, and I love reading his essays, and his startups are doing great things, etc. etc.  You can't fault him.  But he's created something of a problem.
Before Paul Graham, Lisp was dying.  It really was, and let's not get all sentimental or anything; it's just common sense.  A language is always either gaining or losing ground, and Lisp was losing ground all through the 1990s.  Then PG came along with his "I'm not talking to you if you're over 26 years old" essays, each a giant slap in our collective face, and everyone sat up and paid attention to him in a hurry.  And a TON of people started looking very seriously at Lisp.
Lisp might or might not have experienced a revival without Paul's essays, but it's moot: he showed up, and Lisp got real popular, real fast.  And then he said: "Don't use it!"  Sort of.  I mean, that's effectively what he said, isn't it?  By deciding to pre-announce Arc, he Microsofted Lisp.  Killed it with vaporware.  It's a great strategy when you're an evil empire.  I don't
*think*
that's exactly what Paul had in mind, but let's face it: that's what happened.
So Common Lispers grumble about Paul in the hallways.  If I read newsgroups (every time I try, the overall ugliness of humanity drives me away within hours; I only re-attempt it every decade or so) I see them grumbling there too.  He's put them in a tough spot, because he
*did*
use Common Lisp for Viaweb, and his arguments in favor of Lisp (in the general sense) have been compelling enough to bring in newcomers by the droves.  But he's not throwing his weight behind CL.  He's not even taking the marginally-acceptable route (from a damage-control perspective) of recommending Scheme.  Instead, Paul's (*gasp*) starting a new religion.
Arc's going to be a new religion, of course, because programmers just haaaaaave to make it that way.  If it ever appears, anyway.  But will it?  That's the tricky thing about Cathedral-style software; you never can tell.  My prediction: someone will get tired of waiting, and they'll Torvalds Arc into obsolescence before it's ever released.  (If you don't get the reference, it's what Linux did to GNU Hurd).
Long story short: nobody knows what the hell Lisp they're supposed to be using, and it's absolutely killing adoption.
**Problem 2: Worthless Spec**
Oh, ouch, did I have to put it
*quite*
like that?  I mean, c'mon, let's be fair, there are literally hundreds of people out there who disagree.
Unfortunately, the simple fact is that the spec is ancient.  Every time someone talks about updating it, someone screams about time or money or whatever.  The problem is (like the problem with RSS) a people-problem, not a time or money problem.  This is absolutely true in the Scheme world, too.  There are a bunch of old-timer stakeholders who want to have their say.  So you're basically asking a goverment (complete with lobbyists, political parties, the works) to design Lisp if you go that route.  The naysayers are right about one thing: it'll never happen.
Your only other option is to design a new language, and you won't get any help from Lisp people, because they will hate you.  They love pointing to the trail of bodies left in the wake of every pioneer who's tried this before, none of whom has emerged with a "successful" Lisp.  Of course, they haven't been successful because Lispers didn't want to have anything to do with them; Lispers are just as incapacitated by their techno-religious beliefs as folks from other languages.  Religions dislike each other, but no heretic is as damned as someone who starts with your religion and makes a modification to it.  Just ask the Albigensians, for instance.
But what's wrong with Common Lisp?  Do I
*really*
need to say it?  Every single non-standard extension, everything not in the spec, is "wrong" with Common Lisp.  This includes any support for threads, filesystem access, processes and IPC, operating system interoperability, a GUI, Unicode, and the long list of other features missing from the latest hyperspec.
Effectively, everything that can't be solved from
*within*
Lisp is a target.  Lisp is really powerful, sure, but some features can only be effective if they're handled by the implementation.
**Problem 3: CLOS**
*Note:  this section contains a few factual errors pointed out by Pascal Costanza in a comment below.  Some of his corrections are also, of course, opinions, and I've commented on them later in the thread.  In any case, while I thank Pascal for his corrections, the errors I've made are utterly irrelevant to my conclusions.*
CLOS is icky.  I haven't worked with Smalltalk a whole lot, but I've worked with it enough to know that to do OOP right, you have to do it from the ground up.  CLOS was bolted on to Common Lisp.  Everyone knows it, although not many people want to admit it.
It was bolted on very nicely, and it's not my intention to disparage the efforts of the people who created it.  It was an amazing piece of work, and it did a great job of being flexible enough to tie together the conflicting OO systems of existing Lisp implementations.
But let's face it; CLOS has problems.  One obvious one is that
isn't a polymorphic function.  It's one of the first speed bumps you encounter.  You can't create a new kind of measurable object and give it a
method; you have to call it
or
or whatever.  That's part of Lisp's endoskeleton showing; you can see the bolt sticking out plain as the nose on your face.  It's not seamless; it's not orthogonal, and it's not the Right Thing.  But it's not going to change, either.
Another problem is the slot accessor macros.  They're insanely clever, but clever isn't what you want.  You want first-class function access, so you can pass the getters and setters to
,
, etc.  You can work around these things, but they're a leaky abstraction, and enough of those will add up to significant mental resistance to getting things done.  It's like all those weird little rules in Perl:  non-orthogonal rules that add up to forgetting the language every time you leave it alone for more than a week.
What you really want in lieu of CLOS is... complicated.  It's a hard problem.  Lisp
*wants*
to be constructed entirely from macros.  It's part of the purity of the idea of LISP: you only need the seven (or is it five?)  primitives to build the full machine.  Doing CLOS as a bunch of macros was very much in the
*spirit*
of Lisp: it was a Lispy thing to do.
But macros are a
*problem*
.  Yes, they're one of the most important differentiators.  But macros are like having these high-powered band-aids, when what you want is not to be wounded in the first place.  Having the object system — something pretty fundamental to the language, you'd think — written as a bunch of macros doesn't feel right when all is said and done.
When you work with Ruby or Smalltalk or any suitably "pure" OO language (Python doesn't quite count, unfortunately; its bolts are also showing), you realize there are some distinct advantages to having everything be an object.  It's very nice, for instance, to be able to figure out what methods are applicable to a given class (e.g.
from Ruby), and to be able to extend that list with your own new methods.  It's a nice organizational technique.
Of course, that forces you into a single-dispatch model, so it becomes harder to figure out what to do about multi-methods.  Some Python folks have implemented multi-methods for Python, and they do it by making them top-level functions, which makes sense (where else would you put them?)  I'm not claiming that Smalltalk's object model is going to translate straight to Lisp; you have to decide whether cons cells are "objects", for instance, and that's a decision I wouldn't wish on my worst enemy.  I don't envy the person who tackles it.
Regardless of what the solution might be, CLOS remains a problem.  It's over-complicated and yet not quite OOP-y enough or expressive enough.  The problem of reflecting on an object to see which methods are valid for it is one example, but there are tons of others.  Heck, one possibly valid complaint is that it doesn't work very much like the "conventional" OOP systems of C++, Java, Python and Ruby.  There's no real reason it shouldn't be more like them.  But changing CLOS to be simpler and more seamless essentially means replacing it.  And replacing it is probably best done inside the implementation.
In other words, any fix means starting virtually from scratch.
Or maybe you could go the Haskell route and not have OOP at all.  That seems to alienate most programmers, though, despite the attractions of not having to create nouns for everything.  (Have you ever noticed that turning a non-object-oriented program into an object-oriented one in the same language that does the same thing essentially doubles its size?  Try it sometime...)  At the risk of predicting future fashion trends, which is rarely a good idea, I'll venture that objects are going to continue to be trendy for at least a few more decades.  So I think Lisp needs some form of "seamless" OOP.
**Problem 4: Macros**
Macros are one of the worst problems with Lisp, or at least they're one of the biggest unsolved problems.
Yes, they're amazingly powerful and critically important and blah Blah BLAH.  You can read all about them elsewhere.  Paul Graham's
[On Lisp](http://www.paulgraham.com/onlisp.html)
is the best reference I've found.
But they're fraught with problems.  One is that they're not hygienic.  You should at least have the option of requesting hygienic macros.  Various papers have been published, and implementations implemented, for hygienic
.  Yeah, it's hellishly hard to get right, and it's overkill for many situations, but it really does need to be offered as an option.  A
*portable*
one.
For that matter, you should also have a choice between Scheme-style pattern-matching macros and Lisp-style code-style macros.  They're very different, and each kind is better (cleaner) in some situations.  People often act as if hygiene is synonymous with define-syntax, but the pattern-template style is orthogonal to the question of hygiene.
Style considerations aside, macros have tool problems.  Macros are notoriously hard to debug, and honestly it needn't be that way.  If your editor knows all about macros, then you should be able to click to see the expansion, and click again to see its sub-expansions, all the way down to the primitive functions.  Some editors can do this, but none of them (that I'm aware of) handle macros as cleanly or seamlessly as they do normal functions.
Syntax in general is a problem.  Lisp has a
*little*
syntax, and it shows up occasionally as, for instance, '(foo) being expanded as (quote foo), usually when you least expect it.  Truth be told, Lisp should probably have a skinnable syntax.  That implies a canonical abstract syntax tree, which of course hasn't been defined (and in many implementations isn't even available to you, the way it is in the Io language, say).  Once you've got a canonical AST defined, syntax should, in theory, be like CSS chrome.  Of course, there are plenty of bodies left in the trail of this particular theory as well.  Someday...
In any case, because macros are rarely supported "well enough" by the tools, and because they're not first-class functions, and so on, they wind up being second-class citizens.  The rule "you should only use a macro when nothing else will do" implies that they really are a last resort, which (to me) is synonymous with band-aid.  Yes, it's wonderful that you
*have*
the band-aid — or maybe duct tape is a better analogy — certainly you miss them dearly when you're working in other languages.  But you don't want to have to build your entire object system with duct tape.
So macros, like the object system, need to be re-thought from the ground up.  There's undoubtedly enough research in the space that someone could throw together a working definition in no time, something just good enough for today's programmers, the ones who expect (and rightfully so, I might add) to be able to name their methods "length" without getting a compiler error.
**Problem 4: Type System**
See, that's
*just exactly*
the problem with type systems.  They can make sure you use headings, but they can't ensure you get the numbering right.
Well, it'll take me forever to talk about this one, so I'll have to leave it for another blog.  The problem is that the type system has to be extensible and skinnable, and I'm not strictly talking about user-defined types in the sense of OOP or CLOS.  Unfortunately it really is a huge open issue, one that'll take longer than this blog to sort through, so I'll have to leave it for today.
Lisp, for all the strengths of its flexible type system, hasn't got this issue right either.  Otherwise Haskell and OCaml (and C++, gack) wouldn't be kicking its ass all over the performance map.  'nuff said, at least for now.  [And no, they don't quite have it right either.]
I promise I'll talk about type systems soon.  But I also promised some friends I'd make my blogs shorter.
**There *is* no acceptable Lisp**
This is a problem.  It's not a little teeny one, either.  The Lisp communities (yeah, there are a bunch) are going to have to realize that if Lisp is
*ever*
going to be massively successful, it needs an overhaul.  Or maybe a revolution.  Contrary to what some might tell you, it doesn't need a committee, and it doesn't need a bunch of money.  Linux proved exactly the opposite.  Lisp needs a benevolent dictator.  Lisp needs to ditch the name "Lisp", since it scares people.  And Lisp needs to learn from the lessons of the 45 years of languages that have followed it.
And no, I'm not the guy.  You're all far more qualified to tackle this problem than I am.  Especially if you're under 26.