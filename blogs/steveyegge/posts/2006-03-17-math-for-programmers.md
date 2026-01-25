---
title: "Math For Programmers"
date: 2006-03-17
url: https://steve-yegge.blogspot.com/2006/03/math-for-programmers.html
word_count: 3813
---

I've been working for the past 15 months on repairing my rusty math skills, ever since I read a
[biography](http://www.amazon.com/o/asin/0262011212)
of
[Johnny von Neumann](http://en.wikipedia.org/wiki/Von_Neumann)
.  I've read a huge stack of math books, and I have an even bigger stack of unread math books.  And it's starting to come together.
Let me tell you about it.
**Conventional Wisdom Doesn't Add Up**
First: programmers don't think they need to know math.  I hear that so often; I hardly know anyone who disagrees.  Even programmers who were math majors tell me they don't really use math all that much!  They say it's better to know about design patterns, object-oriented methodologies, software tools, interface design, stuff like that.
And you know what?  They're absolutely right.  You can be a good, solid, professional programmer without knowing much math.
But hey, you don't really need to know how to program, either.  Let's face it: there are a lot of professional programmers out there who realize they're not very good at it, and they still find ways to contribute.
If you're suddenly feeling out of your depth, and everyone appears to be running circles around you, what are your options?  Well, you might discover you're good at project management, or people management, or UI design, or technical writing, or system administration, any number of other important things that "programmers" aren't necessarily any good at.  You'll start filling those niches (because there's always more work to do), and as soon as you find something you're good at, you'll probably migrate towards doing it full-time.
In fact, I don't think you need to know
*anything*
, as long as you can stay alive somehow.
So they're right: you don't need to know math, and you can get by for your entire life just fine without it.
But a few things I've learned recently might surprise you:
1. Math is a lot easier to pick up after you know how to program.  In fact, if you're a halfway decent programmer, you'll find it's almost a snap.
2. They teach math all wrong in school.  Way, WAY wrong.  If you teach yourself math the right way, you'll learn faster, remember it longer, and it'll be much more valuable to you as a programmer.
3. Knowing even a *little* of the right kinds of math can enable you do write some pretty interesting programs that would otherwise be too hard.  In other words, math is something you can pick up a little at a time, whenever you have free time.
4. Nobody knows all of math, not even the best mathematicians.  The field is constantly expanding, as people invent new formalisms to solve their own problems.  And with any given math problem, just like in programming, there's more than one way to do it.  You can pick the one you like best.
5. Math is... ummm, please don't tell anyone I said this; I'll never get invited to another party as long as I live.  But math, well...  I'd better whisper this, so listen up: *(it's actually kinda fun.)*

**The Math You Learned (And Forgot)**
Here's the math I learned in school, as far as I can remember:
*Grade School*
:  Numbers, Counting, Arithmetic, Pre-Algebra ("story problems")
*High School*
:  Algebra, Geometry, Advanced Algebra, Trigonometry, Pre-Calculus (conics and limits)
*College*
:  Differential and Integral Calculus, Differential Equations, Linear Algebra, Probability and Statistics, Discrete Math
How'd they come up with that particular list for high school, anyway?  It's more or less the same courses in most U.S. high schools.  I think it's very similar in other countries, too, except that their students have finished the list by the time they're nine years old.  (Americans really kick butt at monster-truck competitions, though, so it's not a total loss.)
Algebra?  Sure.  No question.  You need that.  And a basic understanding of Cartesian geometry, too.  Those are useful, and you can learn everything you need to know in a few months, give or take.  But the rest of them?  I think an introduction to the basics might be useful, but spending a whole semester or year on them seems ridiculous.
I'm guessing the list was designed to prepare students for science and engineering professions.  The math courses they teach in and high school don't help ready you for a career in programming, and the simple fact is that the number of programming jobs is rapidly outpacing the demand for all other engineering roles.
And even if you're planning on being a scientist or an engineer, I've found it's much easier to learn and appreciate geometry and trig after you understand what exactly math
*is*
— where it came from, where it's going, what it's for.  No need to dive right into memorizing geometric proofs and trigonometric identities.  But that's exactly what high schools have you do.
So the list's no good anymore.  Schools are teaching us the wrong math, and they're teaching it the wrong way.  It's no wonder programmers think they don't need any math: most of the math we learned isn't helping us.
**The Math They Didn't Teach You**
The math computer scientists use regularly, in real life, has very little overlap with the list above.  For one thing, most of the math you learn in grade school and high school is continuous: that is, math on the real numbers.  For computer scientists, 95% or more of the interesting math is discrete: i.e., math on the integers.
I'm going to talk in a future blog about some key differences between computer science, software engineering, programming, hacking, and other oft-confused disciplines.  I got the basic framework for these (upcoming) insights in no small part from Richard Gabriel's
[Patterns Of Software](http://www.amazon.com/o/asin/0195121236)
, so if you absolutely can't wait, go read that.  It's a good book.
For now, though, don't let the term "computer scientist" worry you.  It sounds intimidating, but math isn't the exclusive purview of computer scientists; you can learn it all by yourself as a closet hacker, and be just as good (or better) at it than they are.  Your background as a programmer will help keep you focused on the practical side of things.
The math we use for modeling computational problems is, by and large, math on discrete integers.  This is a generalization.  If you're with me on today's blog, you'll be studying a
*little*
more math from now on than you were planning to before today, and you'll discover places where the generalization isn't true.  But by then, a short time from now, you'll be confident enough to ignore all this and teach yourself math the way
*you*
want to learn it.
For programmers, the most useful branch of discrete math is probability theory.  It's the first thing they should teach you after arithmetic, in grade school.  What's probability theory, you ask?  Why, it's
*counting*
.  How many ways are there to make a Full House in poker?  Or a Royal Flush?  Whenever you think of a question that starts with "how many ways..." or "what are the odds...", it's a probability question.  And as it happens (what are the odds?), it all just turns out to be "simple" counting.  It starts with flipping a coin and goes from there.  It's definitely the first thing they should teach you in grade school after you learn Basic Calculator Usage.
I still have my
[discrete math textbook](http://www.amazon.com/o/asin/0072930330)
from college.  It's a bit heavyweight for a third-grader (maybe), but it does cover a
*lot*
of the math we use in "everyday" computer science and computer engineering.
Oddly enough, my professor didn't tell me what it was for.  Or I didn't hear.  Or something.  So I didn't pay very close attention: just enough to pass the course and forget this hateful topic forever, because I didn't think it had anything to do with programming.  That happened in quite a few of my comp sci courses in college, maybe as many as 25% of them.  Poor me!  I had to figure out what was important on my own, later, the hard way.
I think it would be nice if every math course spent a full week just introducing you to the subject, in the most fun way possible, so you know why the heck you're learning it.  Heck, that's probably true for every course.
Aside from probability and discrete math, there are a few other branches of mathematics that are potentially quite useful to programmers, and they usually don't teach them in school, unless you're a math minor.  This list includes:
- ** Statistics**, some of which is covered in my discrete math book, but it's really a discipline of its own.  A pretty important one, too, but hopefully it needs no introduction.
- **Algebra** and **Linear Algebra** (i.e., matrices).  They should teach Linear Algebra immediately after algebra.  It's pretty easy, and it's amazingly useful in all sorts of domains, including machine learning.
- **Mathematical Logic**.  I have a really cool [totally unreadable book](http://www.amazon.com/o/asin/0486425339) on the subject by Stephen Kleene, the inventor of the Kleene closure and, as far as I know, Kleenex.  Don't read that one.  I swear I've tried 20 times, and never made it past chapter 2.  If anyone has a recommendation for a better introduction to this field, *please* post a comment.  It's obviously important stuff, though.
- **Information Theory** and **[Kolmogorov Complexity](http://www.amazon.com/o/asin/0387948686)**. Weird, eh?  I bet *none* of your high schools taught either of those.  They're both pretty new.  Information theory is (veeery roughly) about data compression, and Kolmogorov Complexity is (also roughly) about algorithmic complexity. I.e., how small you can you make it, how long will it take, how elegant can the program or data structure be, things like that.  They're both fun, interesting and useful.

There are others, of course, and some of the fields overlap.  But it just goes to show: the math that you'll find useful is pretty different from the math your school thought would be useful.
What about calculus?  Everyone teaches it, so it must be important, right?
Well, calculus is actually pretty easy.  Before I learned it, it sounded like one of the hardest things in the universe, right up there with quantum mechanics.  Quantum mechanics is still beyond me, but calculus is nothing.  After I realized programmers can learn math quickly, I picked up my
[Calculus textbook](http://www.amazon.com/o/asin/0471381578)
and got through the entire thing in about a month, reading for an hour an evening.
Calculus is all about continuums — rates of change, areas under curves, volumes of solids.  Useful stuff, but the exact details involve a lot of memorization and a lot of tedium that you don't normally need as a programmer.  It's better to know the overall concepts and techniques, and go look up the details when you need them.
Geometry, trigonometry, differentiation, integration, conic sections, differential equations, and their multidimensional and multivariate versions — these all have important applications.  It's just that you don't need to know them right this second.  So it probably wasn't a great idea to make you spend years and years doing proofs and exercises with them, was it?  If you're going to spend that much time studying math, it ought to be on topics that will remain relevant to you for life.
**The Right Way To Learn Math**
The right way to learn math is breadth-first, not depth-first.  You need to survey the space, learn the names of things, figure out what's what.
To put this in perspective, think about long division.  Raise your hand if you can do long division on paper, right now.  Hands?  Anyone?  I didn't think so.
I went back and looked at the long-division algorithm they teach in grade school, and damn if it isn't annoyingly complicated.  It's deterministic, sure, but you
*never*
have to do it by hand, because it's easier to find a calculator, even if you're stuck on a desert island without electricity.  You'll still have a calculator in your watch, or your dental filling, or something.
Why do they even teach it to you?  Why do we feel vaguely guilty if we can't remember how to do it?  It's not as if we
*need*
to know it anymore.  And besides, if your life were on the line, you know you could perform long division of any arbitrarily large numbers.  Imagine you're imprisoned in some slimy 3rd-world dungeon, and the dictator there won't let you out until you've computed 219308862/103503391.  How would you do it?  Well, easy.  You'd start subtracting the denominator from the numerator, keeping a counter, until you couldn't subtract it anymore, and that'd be the remainder.  If pressed, you could figure out a way to continue using repeated subtraction to estimate the remainder as decimal number (in this case, 0.1185678219, or so my Emacs
tells me.  Close enough!)
You could figure it out because you know that division is just repeated subtraction. The intuitive notion of
*division*
is deeply ingrained now.
The right way to learn math is to ignore the actual algorithms and proofs, for the most part, and to start by learning a little bit about all the techniques: their names, what they're useful for, approximately how they're computed, how long they've been around, (sometimes) who invented them, what their limitations are, and what they're related to.  Think of it as a Liberal Arts degree in mathematics.
Why? Because the first step to applying mathematics is
*problem identification*
.  If you have a problem to solve, and you have no idea where to start, it could take you a long time to figure it out.  But if you know it's a differentiation problem, or a convex optimization problem, or a boolean logic problem, then you at least know where to start looking for the solution.
There are lots and
*lots*
of mathematical techniques and entire sub-disciplines out there now.  If you don't know what combinatorics is, not even the first clue, then you're not very likely to be able to recognize problems for which the solution is found in combinatorics, are you?
But that's actually great news, because it's easier to read about the field and learn the names of everything than it is to learn the actual algorithms and methods for modeling and computing the results.  In school they teach you the Chain Rule, and you can memorize the formula and apply it on exams, but how many students really know what it "means"?  So they're not going to be able to know to apply the formula when they run across a chain-rule problem in the wild.  Ironically, it's easier to know what it is than to memorize and apply the formula.  The chain rule is just how to take the derivative of "chained" functions — meaning, function x() calls function g(), and you want the derivative of x(g()).  Well, programmers know all about functions; we use them every day, so it's much easier to imagine the problem now than it was back in school.
Which is why I think they're teaching math wrong.  They're doing it wrong in several ways.  They're focusing on specializations that aren't proving empirically to be useful to most high-school graduates, and they're teaching those specializations backwards.  You should learn how to count, and how to program, before you learn how to take derivatives and perform integration.
I think the best way to start learning math is to spend 15 to 30 minutes a day surfing in Wikipedia.  It's filled with articles about thousands of little branches of mathematics.  You start with pretty much any article that seems interesting (e.g.
[String theory](http://en.wikipedia.org/wiki/String_theory)
, say, or the
[Fourier transform](http://en.wikipedia.org/wiki/Fourier_transform)
, or
[Tensors](http://en.wikipedia.org/wiki/Tensor)
, anything that strikes your fancy.)  Start reading.  If there's something you don't understand, click the link and read about it.  Do this recursively until you get bored or tired.
Doing this will give you amazing perspective on mathematics, after a few months.  You'll start seeing patterns — for instance, it seems that just about every branch of mathematics that involves a single variable has a more complicated multivariate version, and the multivariate version is almost always represented by matrices of linear equations.  At least for applied math.  So Linear Algebra will gradually bump its way up your list, until you feel compelled to learn how it actually works, and you'll download a PDF or buy a book, and you'll figure out enough to make you happy for a while.
With the Wikipedia approach, you'll also quickly find your way to the
[Foundations of Mathematics](http://en.wikipedia.org/wiki/Foundations_of_mathematics)
, the Rome to which all math roads lead.  Math is almost always about formalizing our "common sense" about some domain, so that we can deduce and/or prove new things about that domain.  Metamathematics is the fascinating study of what the limits are on math itself: the intrinsic capabilities of our formal models, proofs, axiomatic systems, and representations of rules, information, and computation.
One great thing that soon falls by the wayside is notation.  Mathematical notation is the biggest turn-off to outsiders.  Even if you're familiar with summations, integrals, polynomials, exponents, etc., if you see a thick nest of them your inclination is probably to skip right over that sucker as one atomic operation.
However, by surveying math, trying to figure out what problems people have been trying to solve (and which of these might actually prove useful to you someday), you'll start seeing patterns in the notation, and it'll stop being so alien-looking.  For instance, a summation sign (capital-sigma) or product sign (capital-pi) will look scary at first, even if you know the basics.  But if you're a programmer, you'll soon realize it's just a loop: one that sums values, one that multiplies them.  Integration is just a summation over a continuous section of a curve, so that won't stay scary for very long, either.
Once you're comfortable with the many branches of math, and the many different forms of notation, you're well on your way to knowing a lot of useful math.  Because it won't be scary anymore, and next time you see a math problem, it'll jump right out at you.  "Hey," you'll think, "I
*recognize*
that.  That's a multiplication sign!"
And then you should pull out the calculator.  It might be a very fancy calculator such as R, Matlab, Mathematica, or a even C library for support vector machines.  But almost all useful math is heavily automatable, so you might as well get some automated servants to help you with it.
**When Are Exercises Useful?**
After a year of doing part-time hobbyist catch-up math, you're going to be able to do a lot more math in your head, even if you never touch a pencil to a paper.  For instance, you'll see polynomials all the time, so eventually you'll pick up on the arithmetic of polynomials by osmosis.  Same with logarithms, roots, transcendentals, and other fundamental mathematical representations that appear nearly everywhere.
I'm still getting a feel for how many exercises I want to work through by hand.  I'm finding that I like to be able to follow explanations (proofs) using a kind of "plausibility test" — for instance, if I see someone dividing two polynomials, I kinda know what form the result should take, and if their result looks more or less right, then I'll take their word for it.  But if I see the explanation doing something that I've never heard of, or that seems wrong or impossible, then I'll dig in some more.
That's a lot like reading programming-language source code, isn't it?  You don't need to hand-simulate the entire program state as you read someone's code; if you know what approximate shape the computation will take, you can simply check that their result makes sense.  E.g. if the result should be a list, and they're returning a scalar, maybe you should dig in a little more.  But normally you can scan source code almost at the speed you'd read English text (sometimes just as fast), and you'll feel confident that you understand the overall shape and that you'll probably spot any truly egregious errors.
I think that's how mathematically-inclined people (mathematicians and hobbyists) read math papers, or any old papers containing a lot of math.  They do the same sort of sanity checks you'd do when reading code, but no more, unless they're intent on shooting the author down.
With that said, I still occasionally do math exercises.  If something comes up again and again (like algebra and linear algebra), then I'll start doing some exercises to make sure I really understand it.
But I'd stress this: don't let exercises put you off the math.  If an exercise (or even a particular article or chapter) is starting to bore you,
*move on*
.  Jump around as much as you need to.  Let your intuition guide you.  You'll learn much, much faster doing it that way, and your confidence will grow almost every day.
**How Will This Help Me?**
Well, it might not — not right away.  Certainly it will improve your logical reasoning ability; it's a bit like doing exercise at the gym, and your overall mental fitness will get better if you're pushing yourself a little every day.
For me, I've noticed that a few domains I've always been interested in (including artificial intelligence, machine learning, natural language processing, and pattern recognition) use a lot of math.  And as I've dug in more deeply, I've found that the math they use is no more difficult than the sum total of the math I learned in high school; it's just
*different*
math, for the most part.  It's not harder.  And learning it is enabling me to code (or use in my own code) neural networks, genetic algorithms, bayesian classifiers, clustering algorithms, image matching, and other nifty things that will result in cool applications I can show off to my friends.
And I've gradually gotten to the point where I no longer break out in a cold sweat when someone presents me with an article containing math notation: n-choose-k, differentials, matrices, determinants, infinite series, etc.  The notation is actually there to make it easier, but (like programming-language syntax) notation is always a bit tricky and daunting on first contact.  Nowadays I can follow it better, and it no longer makes me feel like a plebian when I don't know it.  Because I know I can figure it out.
And that's a good thing.
And I'll keep getting better at this.  I have lots of years left, and lots of books, and articles.  Sometimes I'll spend a whole weekend reading a math book, and sometimes I'll go for weeks without thinking about it even once.  But like any hobby, if you simply trust that it will be interesting, and that it'll get easier with time, you can apply it as often or as little as you like and still get value out of it.
[Math every day](http://www.cabochon.com/~stevey/blog-rants/blog-math-every-day.html)
.  What a great idea that turned out to be!