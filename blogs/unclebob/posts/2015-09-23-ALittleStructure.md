---
title: "A Little Structure"
date: 2015-09-23
url: https://blog.cleancoder.com/uncle-bob/2015/09/23/ALittleStructure.html
slug: ALittleStructure
word_count: 1146
---

What is  *Structured Programming* ?

> *Ummm?…  Wasn’t it some ancient history having to do with `GOTO`?*

Ancient.  Hmmm.  Yes, I guess some might consider 1968 to be ancient.  But can you tell me what Structured Programming is?

> *It was a rule that said not to use `GOTO` statements.*

Why do you keep using the past tense?

> *Because nobody cares about Structured Programming anymore.*

They don’t?

> *No, I mean, hardly anybody knows what it is; except that it’s got something to do with not using `GOTO`.*

Do you use  `GOTO` ?

> *Of course not!  I mean, well…  Hardly ever.*

Why not?

> *Well, mostly because the languages I use don’t have `GOTO`.*

Why do you suppose that is?

> *Because you don’t really need it.*

How do you know you don’t need  `GOTO` ?

> *Well…  I haven’t had to use it …   much.*

Have you ever heard of Corrado Bohm or Giuseppe Jacopini?

> *Who?*

Corrado Bohm and Giuseppe Jacopini.  In 1966 they wrote a  [paper](https://en.wikipedia.org/wiki/Structured_program_theorem)  that mathematically proved that  `GOTO`  was not necessary.

> *Huh.  That’s cool…  I guess.*

Actually, yes, it’s very cool.  Because, you see, in 1966 the  `GOTO`  statement was the primary means by which programmers connected their programs together.

> *Really?*

Yes.  For example, here’s an  `if`  statement in  *FORTRAN* :

```
IF (A-10) 22,33,44
```

> *That looks primitive.  What does it mean?*

It means, if the value of the variable  `A`  minus 10 is negative,  `GOTO`  statement 22.  If zero,  `GOTO`  statement 33.  Otherwise  `GOTO`  statement 44.

> *Wow!  That’s kinda gnarly.  So, like, how did you use that?*

So in Java I might say:

```
if (a>10)
  b++;
else
  b--;
```

In  *FORTRAN*  that would be:

```
	IF (A-10) 20,20,30
20	B = B - 1
	GOTO 40
30	B = B + 1
40	...
```

> *Yuk!  Yuk!  That’s awful.*

That’s what we were used to.  We’d never even thought it could be different.

> *And so then those two guys, Bohm and Jacowhatsit…*

Bohm and Jocopini.

> *Yeah, they wrote their paper and everybody stopped using `GOTO`.*

No, not quite.  In fact, not at all.  You see their paper was a pretty technical mathematical proof, so hardly anybody read it.

> *Heh heh, yeah, I get that.  But somebody must have…*

Oh yes.  Several.  But most notably a man named  [Edsger Dijkstra](https://en.wikipedia.org/wiki/Edsger_W._Dijkstra) .

> *Dije…  DIYGE..*

You pronounce his last name: DIKEstruh.  In March of 1968 he wrote a  [letter](http://homepages.cwi.nl/~storm/teaching/reader/Dijkstra68.pdf)  to the ACM.

> *A letter?  To who?*

Yes, a very short note.  It was written to the editors of a magazine called  *The Communications of the ACM* . He titled it  *Go To Statement Considered Harmful* .

> *What did the letter say?  Did it convince everybody?*

No, it really didn’t.  Oh, some people saw the logic right away.  Others were – um – skeptical – for a long time.

> *So what did the letter say?*

Well, you should read it.  It’s pretty short.  But I’ll give you the gist.

He made the case that you could restrict your program to three different control structures:  Sequence, Selection, and Iteration.

> *OK, so – Huh?*

Sequence is when two statements follow each other in sequence like this:

```
doStepOne();
doStepTwo();
```

Those statements might be simple assignments, or procedure calls, or any other kind of valid statement.  They are executed in sequence.  Right?

> *OK, Sure.  So then…  what’s the next one?*

Selection.  One of two statements will be executed based on some boolean value.  Like this:

```
if (someBooleanValue())
	doThisStep();
else
	doOtherStep();
```

> *Yeah, OK.  So then… that last one…*

Iteration.  A statement can be repeated until a boolean value becomes false.  Like this:

```
while(someBooleanValue())
 	doThisStep();
```

> *Yeah, so, sure.  That’s how we write code nowadays.  But you said people didn’t buy into this right away?*

No, they didn’t.  Dijkstra argued that if you restricted yourself to those three structures then…

> *Oh!  Structures.  Structured Programming.  I get it!*

Um.  Yes.  That’s right.  So, if you restrict yourself to those three, um, structures, then you can easily reason about your code.  But if you use unrestricted  `GOTO`  then you can’t.

> *Wait.  What?  Whaddya mean, reason?*

Well, Dijkstra’s argument was that a structured program can be easily analyzed because the state of the system at any line of code, depends only on the boolean values being tested by  *selection*  and  *iteration* , and the list of calling procedures on the stack.

> *Um. sure.  Whatever.*

(Sigh.)  Look, just read his paper, he makes it pretty clear.

> *OK, well, so then what happened.  I mean, how did people become convinced?*

Well, in 1972, Dijkstra wrote a book with  [O. J. Dahl](https://en.wikipedia.org/wiki/Ole-Johan_Dahl) , and  [C. A. R. Hoare](https://en.wikipedia.org/wiki/Tony_Hoare) .  It was called  [Structured Programming](http://www.amazon.com/Structured-Programming-P-I-C-studies-processing/dp/0122005503) .

> *Oh!  So that’s what convinced everybody.*

Well, no.  Though it did – uh –  *elevate*  the controversy.

> *You mean like you guys were having flame wars over this?*

No, we didn’t have Facebook.  We didn’t even have the internet.  But we could write letters to the editors of the various trade journals.  And, let me tell you, some of those letters were  *scathing* .

> *Ha ha.  Sort of like snail mail flames.*

Indeed.  The more things change, the more they stay the same.

Anyway, the good thing was that the book got lots of people talking, and trying things out, and even convinced some people.

> *But not everyone.*

No, not everyone.  Many people continued to hold on to their  `GOTO`  statements; and would not give them up.

> *So then when did that end?*

It ended when people stopped making and using languages that had  `GOTO`  statements, and started using languages that didn’t.

> *You mean like Java?*

Yes.  Like Java.  Nowadays the majority of programmers use a language that has no  `GOTO` .  And an even larger majority avoid using  `GOTO`  even if their language has one.  So, for the most part, Dijsktra’s war has been won.  Structured Programming is the norm today.

> *Wow! So, Hurray for Dijsktra for giving us this new technology…  back in the olden days…*

New Technology?  No, no, you misunderstand.

> *Why?  I mean, this structured programming thingie was like his invention, right?*

Oh, no.  He didn’t invent anything.  What he did was to identify something we  *shouldn’t do* .  That’s not a technology.  That’s a  *discipline* .

> *Huh? I thought Structured Programming made things better.*

Oh, it did.  But not by giving us some new tools or technologies.  It made things better by taking away a damaging tool.

> *Hmmm.  OK.  Yeah, I guess that’s right.  He took `GOTO` away from us.*

It might be better to say that  *Structured Programming imposes discipline upon direct transfer of control.*

> *That sound like gobeltygoop.*

Yes, I suppose it does.
