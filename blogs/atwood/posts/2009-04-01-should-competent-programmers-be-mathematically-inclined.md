---
title: "Should Competent Programmers be “Mathematically Inclined”"
date: 2009-04-01
url: https://blog.codinghorror.com/should-competent-programmers-be-mathematically-inclined/
slug: should-competent-programmers-be-mathematically-inclined
word_count: 1076
---

One of the more famous [Edsger Dijkstra](http://en.wikipedia.org/wiki/Edsger_W._Dijkstra) quotes is from his 1972 Turing award lecture, [How do we tell truths that might hurt?](http://www.cs.utexas.edu/users/EWD/transcriptions/EWD04xx/EWD498.html)


> **Besides a mathematical inclination**, an exceptionally good mastery of one’s native tongue is the most vital asset of a competent programmer.


Note that he specifically says [native tongue, not English](https://blog.codinghorror.com/the-ugly-american-programmer/). Which makes me wonder why all of Dijkstra’s most important writings were in English, not his native Dutch.


But I digress. Let’s consider the first part of the Dijkstra quote. **Should competent programmers be “mathematically inclined”?** It might be instructive to think of programming as a form of mathematics, at least for one reason: to resist localization. Although there have been attempts to [create localized programming languages](http://en.wikipedia.org/wiki/Non-English-based_programming_languages), as far as I know, nobody has ever tried to localize € or the number 3. They’re universal. So in that sense, programming languages bear a vague, passing resemblance to mathematics. Learn the symbols once and use them everywhere in the world, no matter what your native tongue is.


On the other hand, **I have not found *in practice* that programmers need to be mathematically inclined to become great software developers**. Quite the opposite, in fact. This does depend heavily on what kind of code you’re writing, but the vast bulk of code that *I’ve* seen consists mostly of the “balancing your checkbook” sort of math, nothing remotely like what you’d find in the average college calculus textbook, even.

kg-card-begin: html

```

{
i = j++ / (x + v);
}

```

kg-card-end: html

Not exactly the stuff mathletes are made of.


I never understood the desire to formally equate skill at mathematics with skill at programming. While being a math wonk certainly won’t *hurt* you as a programmer, it’s very hard for me to draw a direct line from “good at math” to “good at programming.” Like Rory, I believe that software development requires some [markedly right-brained sensibilities](https://web.archive.org/web/20080516055248/http://neopoleon.com/blog/posts/13166.aspx).


> When I was growing up, I remember hearing people say things like, “If you like computer programming, then you’ll love math.” I always thought that these people were absolutely nuts. While there is something intrinsically similar about certain types of math and computer programming, the two are different in many more ways than they are similar.
> With math, and I’m not talking about the crazy number-theory math philosophy “Do numbers really exist?” side of things, but with the applied stuff, there are correct answers. You’re either correct or you’re incorrect.
> With coding, the best you can hope for is to do something well. With so many different ways to effect a single outcome, it’s up to some very right-brained sensibilities to determine if you’ve met your goal, as there isn’t anybody (except [another more experienced developer]) who can tell you if you’re right or not.
> If you ignore your right brain, and I’m talking generally about abstraction and aesthetics, then you can slap some code together that might work, but it also might be one hell of a maintenance nightmare. If you focus only on the right brain, you might have something that works, but is so utterly inefficient and personalized that you’re the only person on Earth who could make sense of the code and maintain it.


All those caveats aside, people still advocate the idea that math alone has the power to make you a better programmer. Steve Yegge makes the best case I’ve read for [the programmer-mathematician](http://steve-yegge.blogspot.com/2006/03/math-for-programmers.html), with his five points:

kg-card-begin: html

> Math is a lot easier to pick up after you know how to program.  In fact, if you’re a halfway decent programmer, you’ll find it’s almost a snap. 
> They teach math all wrong in school.  Way, WAY wrong.  If you teach yourself math the right way, you’ll learn faster, remember it longer, and it’ll be much more valuable to you as a programmer. 
>  Knowing even a *little* of the right kinds of math can enable you do write some pretty interesting programs that would otherwise be too hard.  In other words, math is something you can pick up a little at a time, whenever you have free time. 
> Nobody knows all of math, not even the best mathematicians.  The field is constantly expanding, as people invent new formalisms to solve their own problems.  And with any given math problem, just like in programming, there's more than one way to do it.  You can pick the one you like best. 
>   Math is... ummm, please don’t tell anyone I said this; I’ll never get invited to another party as long as I live.  But math, well...  I’d better whisper this, so listen up: *(it’s actually kinda fun.)*

kg-card-end: html

To me, this reads like a broad recipe for becoming intellectually curious and building skill at solving abstract problems. Important programming skills, to be sure, but not necessarily exclusive to the study of math. If math is your preferred way to [sharpen your saw](https://blog.codinghorror.com/sharpening-the-saw/), then have at it – but it’s hardly the *only* way.


I recently received this email:


> I run a small (4 people) web dev shop and I’m finding that younger coders haven’t had the pleasure of writing assembler or managing without library functions. I’ve always found strong math skills to be one of the most useful skills for coding, and when one has Google and a massive library of functions, one doesn’t have to be good at math to get things working, until it either breaks, has edge cases, or brings out OS or library bugs.
> Some quick examples: simplifying tricky equations to determine array indicies or memory offsets; trigonometry to help with physical calculations; mental hex/bin/dec conversion; logic equalities such as DeMorgan’s theorem.


He’s got the right idea; if we’re going to talk about math, let’s get out of the abstract and into the specific. Let’s talk details. Examples. What could be more math-y than that?


**What code have you personally written where a detailed knowledge of math made your work easier?** I can think of some broad categories. Writing a 3D game. Or a physics simulation. Or low-level image filters. Or compression algorithms. The list goes on and on. But if you’re in those situations, you’ll know it.


Maybe I’m a hopeless optimist, but I think most programmers are smart enough to learn whatever math they need [just in time](https://blog.codinghorror.com/keeping-up-and-just-in-time-learning/) to attack the problem at hand.

[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[mathematics](https://blog.codinghorror.com/tag/mathematics/)
[edsger dijkstra](https://blog.codinghorror.com/tag/edsger-dijkstra/)
[technical practices](https://blog.codinghorror.com/tag/technical-practices/)
