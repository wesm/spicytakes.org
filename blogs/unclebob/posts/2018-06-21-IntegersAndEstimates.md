---
title: "Integers and Estimates"
date: 2018-06-21
url: https://blog.cleancoder.com/uncle-bob/2018/06/21/IntegersAndEstimates.html
slug: IntegersAndEstimates
word_count: 1102
---

> *What is this: `a^2 + b^2 = c^2`*

The Pythagorean Theorem.

> *Right.  What else is it?*

An equation in three unknowns.

> *Do you know some solutions to this equation?*

Sure.  (3,4,5) and (5,12,13).

> *Right.  Those are common pythagorean triplets.  Do you know others?*

Well, Google is my friend, let’s see.  (typing)  It looks like (7,24,25) and (9,40,41) all satisfy the equation.

> *Have you noticed that you’ve only supplied integer solutions?*

Oh, right.  I suppose that there are a whole load of non-integer solutions.

> *Have you heard of Diophantus?*

Is that a Greek name?

> *Yes.  Diophantus was interested in equations that had integral solutions.  We call such equations: Diophantine equations.*

So  `a^2 + b^2 = c^2`  is a Diophantine equation?

> *Yes.  And there are many others.  For example: `a^3 + b^3 = c^3`*

Oh, sure.  And what are some solutions?

> *There aren’t any.*

Really?  None?

> *Yes.  None.  That has been proven.  In fact it has been proven that `a^n + b^n = c^n` has no integral solutions for `n>2`.  This is known as Fermat’s conjecture.*

Huh.  OK, well this is kinda interesting I guess, but why should I care?

> *What is a digital computer?*

What do you mean?  This thing that you and I are conversing on is a digital computer.

> *Yes, but what does a digital computer do?*

Uh. It computes digitally?

> *Precisely!  And the word digitally means…?*

Um.  With digits?

> *Exactly!  And are the number of digits finite?*

Of course, though very very large nowadays.

> *…and a finite number of digits is…?*

Oh, I think I see where you are going.  A finite number of digits is an integer.

> *Right.  A digital computer is a computer that computes with integers.  Nothing but integers.*

Well, wait.  What about floating point numbers and rational numbers?

> *They are represented by integers in the computer.  The computer deals with integers, only integers.*

OK.  sure.  Integers.  But what does this have to do with Diophantine equations?

> *What are the inputs to a computer program?*

There are lots of kinds.  Keyboard characters, mouse movements, mouse clicks, network packets.  You name it.

> *They are all made up of integers aren’t they?*

Um.  Yeah, I guess they are.  OK, so every input to a computer program is integral.

> *And what about the outputs?*

Well, yes, pixels, characters, network packets.  They are all composed of integers too.

> *So a digital computer program takes in integers and returns integers.*

Right.  That’s right.  It’s all integers.

> *A digital computer program, therefore, represents a Diophantine equation.*

Wait. What?

> *Integers in.  Integers out.*

OK. sure.  But it’s one big complicated Diophantine equation.

> *Actually, the specification of the program is the equation.  The program finds the solutions to that equation.*

Yeah, yeah, ok.  That’s right.  The specification of a program is a great big Diophantine equation in a bazillion unknowns, and the program that meets that specification finds solutions to that ginormous equation.  Is this useful to know?

> *Who is David Hilbert?*

You mean that guy who designed that funny recursive curve that looks like mosquito netting?

> *(Ahem.) That was one of his accomplishments yes. He also helped Einstein with the General Theory of Relativity.  He was a very great mathematician.*

And he did something with Diophantine equations I’m guessing.

> *Indeed he did many, many things.  Among them was a very famous question.  The question of “Entscheidung” – decidability.*

What did he want to decide?

> *Remember Fermat’s conjecture?*

You mean that equation that has no solutions.   `a^n + b^n = c^n`  where  `n>2` ?

> *Yes, that’s the one.  For a long time there was no proof that `n=2` was the only solution.  How could you disprove that conjecture if you thought it was untrue?*

I could write a program to find counter examples.  Like, maybe  `n=999,999,999`  might work.

> *Right.  And if you found such a solution, you’d have disproven Fermat’s conjecture.  But how long would it take to PROVE the conjecture using that method?*

The program would run forever.  I couldn’t prove it that way.

> *Correct.  What Hilbert wanted was a finite algorithm to determine whether or not a solution exists.  He wanted a way to “decide” whether or not a search, such as the one you suggested, was practical.*

Wait, wait.  What?  He wasn’t asking for the solutions, he was asking for a way to know if there were any solutions?

> *Right.  He wanted a finite algorithm that could tell him whether a given diophantine equation had solutions or not.  That algorithm would not supply the solutions; it would just supply the decision.*

That’s why he called it “decidability”?

> *Entscheidung.  Yes*

Gesundheight!

> *Harumph!  Now.  Who do you think solved the problem of decidability?*

I think you’re about to tell me.

> *Two people whom you’ve heard of.  The two great founders of modern computer science.  Alonzo Church, and Alan Turing.*

Church!  That’s the guy who invented functional programming, right?

> *In a manner of speaking, yes.*

And Turing!  He won world war 2 right?

> *He certainly contributed.  The two of them proved, using very different techniques, that there was no general and finite solution to decidability.*

That must have disappointed Hilbert.

> *Perhaps.  But that’s not the issue.*

Yeah, just what is the issue here?

> *When you are given a program specification, i.e. a Diophantine equation, what is the first thing you are asked to do?*

Estimate it of course.  Folks want to know how long it will take to write the program.

> *And the program is what again, in terms of a that Diophantine equation?*

The program is the … solution … to the … OH!

> *(smile)  I perceive you’ve gotten the point.*

Yeah, like, they are asking me to DECIDE.  An estimate is a decision.

> *And is there a finite method for finding that decision in every case?*

No!  OH, that’s hilarious.

> *Right.  The founding documents of computer science are documents that prove that there is no finite mechanism for deciding if a program can even be written.  The founding of computer science was based on the proof that estimates were not guaranteed.*

Yeah, but we CAN estimate.

> *Yes, we can.  That’s because most specifications are estimable.*

So this has just been a cute little mathematical diversion with no pragmatic result.

> *I suppose you could say that.  But I enjoyed it.  And, after all, I think it’s deliciously ironic that it was the proof of NOESTIMATES that founded computer science.*
